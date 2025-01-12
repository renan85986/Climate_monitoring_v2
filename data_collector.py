import paho.mqtt.client as mqtt
import time

mqtt_client = mqtt.Client(client_id ='data_collector')
mqtt_client.connect(host='localhost', port=1883)


mqtt_client.loop_start()


while True:
    mqtt_client.publish("/temperatura", "35.5")
    time.sleep(10)
