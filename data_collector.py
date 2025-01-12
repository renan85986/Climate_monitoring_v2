import paho.mqtt.client as mqtt
import time
import requests

#configuração api open weather map
api_key = "91a8c6f027231dcd0a2bbf297c28210c"
url_base = "http://api.openweathermap.org/data/2.5/weather?"
cidade = input("Qual cidade você quer saber o clima?")

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


#configuração publisher mqtt
#mqtt_client = mqtt.Client(client_id ='data_collector')
#mqtt_client.connect(host='localhost', port=1883)
#mqtt_client.loop_start()


#while True:
#    mqtt_client.publish("/temperatura", "35.5")
#    time.sleep(10)
