# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import json
import random
#import Adafruit_DHT
from datetime import datetime

#Servidor Local
MQTT_ADDRESS = 'ubuntuIoTserver'
MQTT_PORT = 8883
MQTT_TIMEOUT = 60

client = mqtt.Client()

def publish_value(value, topic):

    time = str( datetime.now() )

    if value is not None:
        send_msg = {
            'event': {
                'value':value,
                'timestamp': time
            }
        }

        result, mid = client.publish(topic, payload=json.dumps(send_msg), qos=1, retain=True )
        print "%s - %s" % (topic, send_msg)
        print('Mensagem enviada ao canal: %d' % mid)

def read_sensor():
    # descomente esta linha caso seu servidor possua autenticação.
    client.username_pw_set('ticimed', 'cimed@2017')
    client.connect(MQTT_ADDRESS, MQTT_PORT, MQTT_TIMEOUT)

    #faz a leitura do sensor
    #humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 17)
    temperature = random.randint(-10, 40)
    humidity = random.randint(0,100)

    publish_value(temperature, "MG/TI/RP01/Temperatura")
    publish_value(humidity, "MG/TI/RP01/Umidade")

if __name__ == '__main__':
    read_sensor()
