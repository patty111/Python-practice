# subscriber.py

import paho.mqtt.client as mqtt
import json

HOST = "127.0.0.1"
PORT = 1883
USER = ""
PASS = ""
TOPIC = "TEST"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    # msg.topic
    messages = json.loads(msg.payload)['messages']
    if (messages == 'Git'): print("Hub")

if __name__ == '__main__':

    client = mqtt.Client()
    # client.username_pw_set(USER, PASS)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.loop_forever()