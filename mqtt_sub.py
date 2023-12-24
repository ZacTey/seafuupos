
import time
import paho.mqtt.client as paho
from paho import mqtt
import random
from paho.mqtt import client as mqtt_client

broker = "c49cac5c55a44e66b1d15452286ce452.s1.eu.hivemq.cloud"
port = 8883
topic = "encyclopedia/#"
username = "seafuu"
password = "Seafuu!2345"

def connect_mqtt():
    def on_connect(client, userdata, flags, rc, properties = None):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    # client = mqtt_client.Client(client_id)
    client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic, qos=1)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()