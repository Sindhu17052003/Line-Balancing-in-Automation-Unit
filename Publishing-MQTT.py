# python 3.6

import random
import time
import pandas as pd

from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
topic = "Face_Teal"

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client
def publish(client):
    msg_count = 0
    while True:
        time.sleep(3)
        msg1 = f"messages: {msg_count}"
        
        result = client.publish(topic, msg1)
        
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg1}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        df=pd.read_csv('face_count.csv')
        last_row = df.iloc[-1]
        msg_count=last_row.to_dict()

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
