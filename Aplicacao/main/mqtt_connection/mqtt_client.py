import paho.mqtt.client as mqtt

class mqtt_client: #classe de conexão
    def __init__(self, broker_ip: str, port: int, client_name: str, keepalive=60): #metodo construtor
        self.__broker_ip = broker_ip #atributos privados sempre começam com __
        self.__port = port
        self.__client_name = "renanzao"
        self.__keepalive = keepalive # envia pings para o broker para sinalizar que está ativo
   
    def start_connection(self):
        mqtt_cliente = mqtt.Client(client_id=self.__client_name) #identifico a variavel mqtt_client como um cliente mqtt com o nome
        mqtt_cliente.connect(host = self.__broker_ip, port = self.__port, keepalive = self.__keepalive)
        mqtt_cliente.loop_start() #fica num loop esperando por informações do broker 