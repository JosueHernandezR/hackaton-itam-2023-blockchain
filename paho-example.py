import paho.mqtt.client as mqtt  # import the client1
import time
import requests
import json

topic = "zigbee2mqtt/0x00158d00094d2413"
url = "http://localhost/api/v1/sensor_door_window/"
headers = {'Content-Type': 'application/json'} 

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True  # set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_message(client, userdata, msg):
    print("----------------------------")
    json_data = json.loads(msg.payload.decode("utf-8"))
    json_data = {'id_sensor': str(topic), **json_data}
    print(json.dumps(json_data))
    x = requests.post(url, json=json_data, headers=headers)
    print(x)
    if x.status_code == 422:
        # Si el código de estado es 422, muestra el contenido de la respuesta
        print(x.json())  # Puedes usar .text en lugar de .json() si la respuesta no es JSON

        # También puedes acceder a la información adicional proporcionada por el servidor en el encabezado de respuesta
        print(x.headers)
    

mqtt.Client.connected_flag = False  # create flag in class
broker = "localhost"
client = mqtt.Client("python1")  # create new instance
client.on_connect = on_connect
client.connect(broker)  # connect to broker
client.subscribe(topic=topic)
client.on_message = on_message  # bind call back function
client.loop_forever()
# print("Connecting to broker ", broker)


# # while not client.connected_flag:  # wait in loop
# #     print("In wait loop")
# print("in Main Loop")
# print(myGlobalMessagePayload)

# # client.loop_stop()    #Stop loop

# # client.disconnect() # disconnect
