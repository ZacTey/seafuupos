
import time
import paho.mqtt.client as paho
from paho import mqtt
import random
from paho.mqtt import client as mqtt_client


broker = "c49cac5c55a44e66b1d15452286ce452.s1.eu.hivemq.cloud"
port = 8883
topic = "encyclopedia/temperature"
username = "seafuu"
password = "Seafuu!2345"

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    #client = mqtt_client.Client(client_id)
    client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# client.publish("encyclopedia/temperature", payload="hot", qos=1)
def publish(client):
    msg_count = 1
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > 5:
            break


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == '__main__':
    run()