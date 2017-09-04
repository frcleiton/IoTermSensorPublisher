# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import json
import random
import Adafruit_DHT
from datetime import datetime

MQTT_ADDRESS = '192.168.56.101'
# descomente esta linha para usar o servidor da Fundação Eclipse.
# MQTT_ADDRESS = 'iot.eclipse.org'
MQTT_PORT = 8883
# descomente esta linha caso seu servidor possua autenticação.
MQTT_AUTH = Auth('ticimed', 'cimed@2017')
MQTT_TIMEOUT = 60
UNIDADE = 'MG'
SETOR = 'TI'
SENSOR = 'RP01'


def send_message():
    client = mqtt.Client()
    # descomente esta linha caso seu servidor possua autenticação.
    client.username_pw_set(MQTT_AUTH.user, MQTT_AUTH.pwd)
    client.connect(MQTT_ADDRESS, MQTT_PORT, MQTT_TIMEOUT)

    #faz a leitura do sensor
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 17)
    time = str( datetime.now() )
    send_msg = {
        'datahora': time,
		'temperatura': temperature,
		'umidade': humidity
    }

    result, mid = client.publish(UNIDADE+'/'+SETOR+'/'+SENSOR, payload=json.dumps(send_msg), qos=2)
    print('Mensagem enviada ao canal: %d' % mid)

if __name__ == '__main__':
    send_message()
