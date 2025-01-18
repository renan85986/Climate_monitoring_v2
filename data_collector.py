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
api_key = "ea394377cf604d64b9e181828251701"
url_base = "http://api.weatherapi.com/v1/forecast.json?"
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
 
      url_final = f"{url_base}key={api_key}&q={cidade}&days=2&aqi=no&alerts=no"
      requisicao = requests.get(url_final)

      #print(requisicao.json())
      dados = requisicao.json()
      
      #captura o tempo da requisição e converte para o formato timestamp
      timestamp = datetime.now(timezone.utc)
      iso_timestamp = timestamp.isoformat(timespec='seconds').replace('+00:00','Z')
      #print(iso_timestamp)

      if "error" in dados:
        print("Alguma coisa deu errado, tente outra cidade!")
        break
      else:
        #dados agora
        data_atualizado = dados['current']['last_updated']
        temperatura_atual = dados['current']['temp_c']
        pressao_atual = dados['current']['pressure_mb']
        umidade_atual = dados['current']['humidity']
        clima_atual = dados['current']['condition']['text']
        vento_atual = dados['current']['wind_kph']
        sensacao_termica_atual = dados['current']['feelslike_c']
        #dados dia atual
        temperatura_max = dados['forecast']['forecastday'][0]['day']['maxtemp_c']
        temperatura_min = dados['forecast']['forecastday'][0]['day']['mintemp_c']
        temperatura_media = dados['forecast']['forecastday'][0]['day']['avgtemp_c']
        umidade_media = dados['forecast']['forecastday'][0]['day']['avghumidity']
        chuva_total = dados['forecast']['forecastday'][0]['day']['totalprecip_mm']
        clima = dados['forecast']['forecastday'][0]['day']['condition']['text']
        #dados dia atual por hora
        hora_atual_6h= dados['forecast']['forecastday'][0]['hour'][6]['time']
        temperatura_atual_6h= dados['forecast']['forecastday'][0]['hour'][6]['temp_c']
        vento_atual_6h = dados['forecast']['forecastday'][0]['hour'][6]['wind_kph']
        pressao_atual_6h = dados['forecast']['forecastday'][0]['hour'][6]['pressure_mb']
        umidade_atual_6h = dados['forecast']['forecastday'][0]['hour'][6]['humidity']
        chuva_atual_6h = dados['forecast']['forecastday'][0]['hour'][6]['precip_mm']
        clima_atual_6h = dados['forecast']['forecastday'][0]['hour'][6]['condition']['text']

        hora_atual_12h= dados['forecast']['forecastday'][0]['hour'][12]['time'] 
        temperatura_atual_12h= dados['forecast']['forecastday'][0]['hour'][12]['temp_c']
        vento_atual_12h = dados['forecast']['forecastday'][0]['hour'][12]['wind_kph']
        pressao_atual_12h = dados['forecast']['forecastday'][0]['hour'][12]['pressure_mb']
        umidade_atual_12h = dados['forecast']['forecastday'][0]['hour'][12]['humidity']
        chuva_atual_12h = dados['forecast']['forecastday'][0]['hour'][12]['precip_mm']
        clima_atual_12h = dados['forecast']['forecastday'][0]['hour'][12]['condition']['text']

        hora_atual_18h= dados['forecast']['forecastday'][0]['hour'][18]['time']
        temperatura_atual_18h= dados['forecast']['forecastday'][0]['hour'][18]['temp_c']
        vento_atual_18h = dados['forecast']['forecastday'][0]['hour'][18]['wind_kph']
        pressao_atual_18h = dados['forecast']['forecastday'][0]['hour'][18]['pressure_mb']
        umidade_atual_18h = dados['forecast']['forecastday'][0]['hour'][18]['humidity']
        chuva_atual_18h = dados['forecast']['forecastday'][0]['hour'][18]['precip_mm']
        clima_atual_18h = dados['forecast']['forecastday'][0]['hour'][18]['condition']['text']

        hora_atual_24h= dados['forecast']['forecastday'][0]['hour'][23]['time']
        temperatura_atual_24h= dados['forecast']['forecastday'][0]['hour'][23]['temp_c']
        vento_atual_24h = dados['forecast']['forecastday'][0]['hour'][23]['wind_kph']
        pressao_atual_24h = dados['forecast']['forecastday'][0]['hour'][23]['pressure_mb']
        umidade_atual_24h = dados['forecast']['forecastday'][0]['hour'][23]['humidity']
        chuva_atual_24h = dados['forecast']['forecastday'][0]['hour'][23]['precip_mm']
        clima_atual_24h = dados['forecast']['forecastday'][0]['hour'][23]['condition']['text']

        #dados dia seguinte por hora
        hora_seguinte_6h= dados['forecast']['forecastday'][1]['hour'][6]['time']
        temperatura_seguinte_6h= dados['forecast']['forecastday'][1]['hour'][6]['temp_c']
        vento_seguinte_6h = dados['forecast']['forecastday'][1]['hour'][6]['wind_kph']
        pressao_seguinte_6h = dados['forecast']['forecastday'][1]['hour'][6]['pressure_mb']
        umidade_seguinte_6h = dados['forecast']['forecastday'][1]['hour'][6]['humidity']
        chuva_seguinte_6h = dados['forecast']['forecastday'][1]['hour'][6]['precip_mm']
        clima_seguinte_6h = dados['forecast']['forecastday'][1]['hour'][6]['condition']['text']

        hora_seguinte_12h= dados['forecast']['forecastday'][1]['hour'][12]['time'] 
        temperatura_seguinte_12h= dados['forecast']['forecastday'][1]['hour'][12]['temp_c']
        vento_seguinte_12h = dados['forecast']['forecastday'][1]['hour'][12]['wind_kph']
        pressao_seguinte_12h = dados['forecast']['forecastday'][1]['hour'][12]['pressure_mb']
        umidade_seguinte_12h = dados['forecast']['forecastday'][1]['hour'][12]['humidity']
        chuva_seguinte_12h = dados['forecast']['forecastday'][1]['hour'][12]['precip_mm']
        clima_seguinte_12h = dados['forecast']['forecastday'][1]['hour'][12]['condition']['text']

        hora_seguinte_18h= dados['forecast']['forecastday'][1]['hour'][18]['time']
        temperatura_seguinte_18h= dados['forecast']['forecastday'][1]['hour'][18]['temp_c']
        vento_seguinte_18h = dados['forecast']['forecastday'][1]['hour'][18]['wind_kph']
        pressao_seguinte_18h = dados['forecast']['forecastday'][1]['hour'][18]['pressure_mb']
        umidade_seguinte_18h = dados['forecast']['forecastday'][1]['hour'][18]['humidity']
        chuva_seguinte_18h = dados['forecast']['forecastday'][1]['hour'][18]['precip_mm']
        clima_seguinte_18h = dados['forecast']['forecastday'][1]['hour'][18]['condition']['text']

        hora_seguinte_24h= dados['forecast']['forecastday'][1]['hour'][23]['time']
        temperatura_seguinte_24h= dados['forecast']['forecastday'][1]['hour'][23]['temp_c']
        vento_seguinte_24h = dados['forecast']['forecastday'][1]['hour'][23]['wind_kph']
        pressao_seguinte_24h = dados['forecast']['forecastday'][1]['hour'][23]['pressure_mb']
        umidade_seguinte_24h = dados['forecast']['forecastday'][1]['hour'][23]['humidity']
        chuva_seguinte_24h = dados['forecast']['forecastday'][1]['hour'][23]['precip_mm']
        clima_seguinte_24h = dados['forecast']['forecastday'][1]['hour'][23]['condition']['text']      


      #temperatura = temperatura - 273.15
      temperatura_json = {
         "timestamp": iso_timestamp,
          "temperatura_atual":{ 
            "temp_atual" : temperatura_atual
          },
          "temperatura_dia_atual_todo":{ 
            "temp_max" : temperatura_max,
            "temp_min" : temperatura_min,
            "temp_media" : temperatura_media
          },
          "temperatura_dia_atual_6h":{ 
            "temp_6h" : temperatura_atual_6h
          },
          "temperatura_dia_atual_12h":{ 
            "temp_12h" : temperatura_atual_12h
          }, 
          "temperatura_dia_atual_18h":{ 
            "temp_18h" : temperatura_atual_18h
          },
          "temperatura_dia_atual_24h":{ 
            "temp_24h" : temperatura_atual_24h
          },
          "temperatura_dia_seguinte_6h":{ 
            "temp_6h" : temperatura_seguinte_6h
          },
          "temperatura_dia_seguinte_12h":{ 
            "temp_12h" : temperatura_seguinte_12h
          }, 
          "temperatura_dia_seguinte_18h":{ 
            "temp_18h" : temperatura_seguinte_18h
          },
          "temperatura_dia_seguinte_24h":{ 
            "temp_24h" : temperatura_seguinte_24h
          }                 
      }

      pressao_json = {
         "timestamp": iso_timestamp,
          "pressao_atual":{ 
            "pressao_atual" : pressao_atual
          },
          "pressao_dia_atual_6h":{ 
            "pressao_6h" : pressao_atual_6h
          },
          "pressao_dia_atual_12h":{ 
            "pressao_12h" : pressao_atual_12h
          }, 
          "pressao_dia_atual_18h":{ 
            "pressao_18h" : pressao_atual_18h
          },
          "pressao_dia_atual_24h":{ 
            "pressao_24h" : pressao_atual_24h
          },
          "pressao_dia_seguinte_6h":{ 
            "pressao_6h" : pressao_seguinte_6h
          },
          "pressao_dia_seguinte_12h":{ 
            "pressao_12h" : pressao_seguinte_12h
          }, 
          "pressao_dia_seguinte_18h":{ 
            "pressao_18h" : pressao_seguinte_18h
          },
          "pressao_dia_seguinte_24h":{ 
            "pressao_24h" : pressao_seguinte_24h
          }                 
      }

      umidade_json = {
         "timestamp": iso_timestamp,
          "umidade_atual":{ 
            "umidade_atual" : umidade_atual
          },
          "umidade_dia_atual_todo":{ 
            "umidade_media" : umidade_media
          },
          "umidade_dia_atual_6h":{ 
            "umidade_6h" : umidade_atual_6h
          },
          "umidade_dia_atual_12h":{ 
            "umidade_12h" : umidade_atual_12h
          }, 
          "umidade_dia_atual_18h":{ 
            "umidade_18h" : umidade_atual_18h
          },
          "umidade_dia_atual_24h":{ 
            "umidade_24h" : umidade_atual_24h
          },
          "umidade_dia_seguinte_6h":{ 
            "umidade_6h" : umidade_seguinte_6h
          },
          "umidade_dia_seguinte_12h":{ 
            "umidade_12h" : umidade_seguinte_12h
          }, 
          "umidade_dia_seguinte_18h":{ 
            "umidade_18h" : umidade_seguinte_18h
          },
          "umidade_dia_seguinte_24h":{ 
            "umidade_24h" : umidade_seguinte_24h
          }                 
      }

      clima_json = {
         "timestamp": iso_timestamp,
          "clima_atual":{ 
            "clima_atual" : clima_atual
          },
          "clima_dia_atual_todo":{ 
            "clima_dia" : clima
          },
          "clima_dia_atual_6h":{ 
            "clima_6h" : clima_atual_6h
          },
          "clima_dia_atual_12h":{ 
            "clima_12h" : clima_atual_12h
          }, 
          "clima_dia_atual_18h":{ 
            "clima_18h" : clima_atual_18h
          },
          "clima_dia_atual_24h":{ 
            "clima_24h" : clima_atual_24h
          },
          "clima_dia_seguinte_6h":{ 
            "clima_6h" : clima_seguinte_6h
          },
          "clima_dia_seguinte_12h":{ 
            "clima_12h" : clima_seguinte_12h
          }, 
          "clima_dia_seguinte_18h":{ 
            "clima_18h" : clima_seguinte_18h
          },
          "clima_dia_seguinte_24h":{ 
            "clima_24h" : clima_seguinte_24h
          }                
      }

      vento_json = {
         "timestamp": iso_timestamp,
          "vento_atual":{ 
            "vento_atual" : vento_atual
          },
          "vento_dia_atual_6h":{ 
            "vento_6h" : vento_atual_6h
          },
          "vento_dia_atual_12h":{ 
            "vento_12h" : vento_atual_12h
          }, 
          "vento_dia_atual_18h":{ 
            "vento_18h" : vento_atual_18h
          },
          "vento_dia_atual_24h":{ 
            "vento_24h" : vento_atual_24h
          },
          "vento_dia_seguinte_6h":{ 
            "vento_6h" : vento_seguinte_6h
          },
          "vento_dia_seguinte_12h":{ 
            "vento_12h" : vento_seguinte_12h
          }, 
          "vento_dia_seguinte_18h":{ 
            "vento_18h" : vento_seguinte_18h
          },
          "vento_dia_seguinte_24h":{ 
            "vento_24h" : vento_seguinte_24h
          }                 
      }  
      
      sensacao_termica_json = {
         "timestamp" : iso_timestamp,
         "sensacao_termica_atual" : sensacao_termica_atual
      }

      mqtt_client.publish("/sensor_monitors/REN1/temperatura", payload=json.dumps(temperatura_json))
      mqtt_client.publish("/sensor_monitors/REN1/pressao", payload=json.dumps(pressao_json))
      mqtt_client.publish("/sensor_monitors/REN1/umidade", payload=json.dumps(umidade_json))
      mqtt_client.publish("/sensor_monitors/REN1/clima", payload=json.dumps(clima_json))
      mqtt_client.publish("/sensor_monitors/REN1/vento", payload=json.dumps(vento_json))
      mqtt_client.publish("/sensor_monitors/REN1/sensacao_termica", payload=json.dumps(sensacao_termica_json))

      time.sleep(periodicidade)
      
      mqtt_client.publish("/sensor_monitors", payload=json.dumps(msg_inicial))

