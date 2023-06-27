import json
import os
from typing import Any

import ipfshttpclient2

from robonomicsinterface import Account, Launch
from robonomicsinterface.utils import ipfs_qm_hash_to_32_bytes, web_3_auth
from substrateinterface import Keypair, KeypairType

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

seed = "movie gain vessel where allow enjoy repeat govern nurse easily pave nephew"
command = {
    "platform": "switch",
    "name": "turn_off",
    "params": {
        "entity_id": "switch.2gang_switch_l1"
    }
}
controller_address = "4FLuhfypbrwpznu3imYqR8Ne56XHBTtNkqyG1AMgmkBUszGc"
sub_owner_address = "4HW1xG4dhrDPMDEEToHZFdvhd5f7iNs5mcGzhjhiNMYHfSYY"
url = "ipfs-gateway.multi-agent.io"
port = 443
encrypt = True


def encrypt_message(
    message, sender_keypair: Keypair, recipient_public_key: bytes
) -> str:
    """
    Encrypt message with sender private key and recepient public key

    :param message: Message to encrypt
    :param sender_keypair: Sender account Keypair
    :param recipient_public_key: Recepient public key

    :return: encrypted message
    """
    encrypted = sender_keypair.encrypt_message(message, recipient_public_key)
    return f"0x{encrypted.hex()}"


def dispatch(action: str, entity_id: str) -> Any:
    message = json.dumps({
        "platform": "switch",
        "name": action,
        "params": {
            "entity_id": entity_id
        }
    })
    print(f"Message: {message}")
    sender = Account(seed, crypto_type=KeypairType.ED25519)
    if encrypt:
        recepient = Keypair(
            ss58_address=controller_address, crypto_type=KeypairType.ED25519
        )
        message = encrypt_message(
            message, sender.keypair, recepient.public_key)
        print(f"Ecrypted message: {message}")

    filename = "temporal_file"
    with open(filename, "w") as f:
        f.write(message)

    usr, pwd = web_3_auth(seed)
    with ipfshttpclient2.connect(
        addr=f"/dns4/{url}/tcp/{port}/https", auth=(usr, pwd)
    ) as client:
        result_ipfs = client.add(filename, pin=False)["Hash"]
    print(f"IPFS hash: {result_ipfs}")
    print(f"IPFS hash for launch {ipfs_qm_hash_to_32_bytes(result_ipfs)}")
    os.remove(filename)

    launch = Launch(sender, rws_sub_owner=sub_owner_address)
    res = launch.launch(controller_address, result_ipfs)
    print(f"Transaction result: {res}")
    return res

@router.get("/")
async def activity(
    *,
    action: str,
    entity_id: str,
) -> Any:
    response = dispatch(action=action, entity_id=entity_id)
    return response