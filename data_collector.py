import paho.mqtt.client as mqtt

mqtt_client = mqtt.Client(client_id ='data_collector')
mqtt_client.connect(host='localhost', port=1883)
mqtt_client.publish(topic="/temperatura", payload='{35.5}')

