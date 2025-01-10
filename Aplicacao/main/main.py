import time
from Aplicacao.configs.broker_conf import mqtt_broker_configs
from Aplicacao.main.mqtt_connection.mqtt_client import mqtt_client


def start():
    cliente = mqtt_client(
    mqtt_broker_configs["HOST"],
    mqtt_broker_configs["PORT"],
    mqtt_broker_configs["CLIENT_NAME"],
    mqtt_broker_configs["KEEPALIVE"])
    cliente.start_connection()

    while True: time.sleep(0.001) #persiste a conexão por 1 min e começa o loop para deixar o cliente ativo 