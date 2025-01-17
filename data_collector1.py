import paho.mqtt.client as mqtt
import time
import requests
import keyboard
import threading
import json
from datetime import datetime, timezone

#variáveis globais
periodicidade = 10
parar = False
msg_inicial={
        "machine_id": "REN1",
        "sensors":[
            {
                "sensor_id": "1",
                "data_type": "float",
                "data_interval": periodicidade
            },
            {
                "sensor_id": "2",
                "data_type": "float",
                "data_interval": periodicidade
            },
            {
                "sensor_id": "3",
                "data_type": "float",
                "data_interval": periodicidade
            },
            {
                "sensor_id": "4",
                "data_type": "string",
                "data_interval": periodicidade
            },
            {
                "sensor_id": "5",
                "data_type": "float",
                "data_interval": periodicidade
            }
            ]
 }
#configuração api open weather map
api_key = "91a8c6f027231dcd0a2bbf297c28210c"
url_base = "http://api.openweathermap.org/data/2.5/weather?"
#configuração publisher mqtt
mqtt_client = mqtt.Client(client_id ='data_collector')
mqtt_client.connect(host='localhost', port=1883)
mqtt_client.loop_start()

def monitorar_tecla(): #função que executa em uma thread externa para monitorar a tecla p
  global parar
  while True:
        if keyboard.is_pressed("p"):
          parar = True
          print("tecla p pressionada")
          break
  
#loop externo, quando volta nele seta a cidade a ser monitorada  
while True:
 cidade = input("Qual cidade você quer saber o clima?")
 thread = threading.Thread(target=monitorar_tecla, daemon=True)
 thread.start()
 mqtt_client.publish("/sensor_monitors", payload=json.dumps(msg_inicial))
 

 while True: #loop interno, faz requisições a cada tempo determinado no time.sleep e publica no broker
      if parar:
        parar = False
        break
 
      url_final = f"{url_base}appid={api_key}&q={cidade}"
      requisicao = requests.get(url_final)

      print(requisicao.json())
      dados = requisicao.json()
      
      #captura o tempo da requisição e converte para o formato timestamp
      timestamp = datetime.now(timezone.utc)
      iso_timestamp = timestamp.isoformat(timespec='seconds').replace('+00:00','Z')
      #print(iso_timestamp)

      if dados['cod'] == 200:
        temperatura = dados['main']['temp']
        pressao = dados['main']['pressure']
        umidade = dados['main']['humidity']
        clima = dados['weather'][0]['description']
        vento = dados['wind']['speed']
        print(f"Cidade: {cidade}")
        print(f"Clima: {clima}")
        print(f"Temperatura é de: {temperatura - 273.15:.2f}°C")
        print(f"Pressão é de: {pressao}kPa")
        print(f"A umidade é: {umidade}%")
        print(f"A velocidade do vento é: {vento}m/s")
      else:
        print("Alguma coisa deu errado, tente outra cidade!")
        break
      
      temperatura = temperatura - 273.15
      temperatura_json = {
         "timestamp": iso_timestamp,
         "value" : temperatura 
      }

      pressao_json = {
         "timestamp": iso_timestamp,
         "value": pressao 
      }

      umidade_json = {
         "timestamp": iso_timestamp,
         "value": umidade
      } 

      clima_json = {
         "timestamp": iso_timestamp,
         "value": clima
      } 

      vento_json = {
         "timestamp": iso_timestamp,
         "value": vento
      }  
      
      mqtt_client.publish("/sensor_monitors/REN1/temperatura", payload=json.dumps(temperatura_json))
      mqtt_client.publish("/sensor_monitors/REN1/pressao", payload=json.dumps(pressao_json))
      mqtt_client.publish("/sensor_monitors/REN1/umidade", payload=json.dumps(umidade_json))
      mqtt_client.publish("/sensor_monitors/REN1/clima", payload=json.dumps(clima_json))
      mqtt_client.publish("/sensor_monitors/REN1/vento", payload=json.dumps(vento_json))

      time.sleep(periodicidade)
      
      mqtt_client.publish("/sensor_monitors", payload=json.dumps(msg_inicial))

