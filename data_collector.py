import paho.mqtt.client as mqtt
import time
import requests
import keyboard
import threading

#variáveis globais
parar = False
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

 while True: #loop interno, faz requisições a cada tempo determinado no time.sleep e publica no broker
      if parar:
        parar = False
        break
 
      url_final = f"{url_base}appid={api_key}&q={cidade}"
      requisicao = requests.get(url_final)

      print(requisicao.json())
      dados = requisicao.json()

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
        
      mqtt_client.publish("/temperatura", temperatura)
      mqtt_client.publish("/pressao", pressao)
      mqtt_client.publish("/umidade", umidade)
      mqtt_client.publish("/clima", clima)
      mqtt_client.publish("/vento", vento)
      time.sleep(10)

