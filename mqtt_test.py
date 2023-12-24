
# ========================= RESULT ==============================
#C:\Users\admin\Desktop\django_fos>python mqtt_test.py
#CONNACK received with code Success.
#print which topic was subscribed to: 1 [<paho.mqtt.reasoncodes.ReasonCodes object at 0x000001F90EAF5E10>]
#print message, useful for checking if it was successful encyclopedia/temperature 1 b'hot'
#with this callback you can see if your publish was successful: 2


import time
import paho.mqtt.client as paho
from paho import mqtt

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("with this callback you can see if your publish was successful: >>>" + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("print which topic was subscribed to: >>>" + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print("print message, useful for checking if it was successful >>>", msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("seafuu", "Seafuu!2345")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
#client.connect("c49cac5c55a44e66b1d15452286ce452.s1.eu.hivemq.cloud", 8883)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
#client.subscribe("encyclopedia/#", qos=1)

# a single publish, this can also be done in loops, etc.
#client.publish("encyclopedia/temperature", payload="hot", qos=1)

print("connecting to broker ")
client.connect("c49cac5c55a44e66b1d15452286ce452.s1.eu.hivemq.cloud", 8883)



client.loop_start() #start loop to process received messages
print("subscribing ")
topic1 = "PrintSuccess"
topic2 = "[Prn0C2F290A2506002300008C74D8EC9566]"



client.subscribe("PrintSuccess/#", qos=2)
time.sleep(2)


print("publishing ")

client.publish("PrintSuccess/Prn0C2F290A2506002300008C74D8EC9566",
               "030053696D706C655072696E740048656C6C6F2C20576F726C64210D0A",
               qos=2)

time.sleep(4)
client.disconnect() #disconnect
client.loop_stop() #stop loop


# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
# client.loop_forever()

