import paho.mqtt.client as mqtt  # import the client1
import time

topic = "zigbee2mqtt/0x00158d00094d2413"
myGlobalMessagePayload = ''   #HERE!


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True  # set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_message(client, userdata, msg):
    print("----------------------------")
    global myGlobalMessagePayload
    myGlobalMessagePayload  = msg.payload   #HERE!
    print("----------------------------")
    print(msg.topic+" "+str(msg.payload))

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
