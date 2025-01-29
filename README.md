# Monitoramento Climático de Cidades 
## 📌 Descrição
O projeto de monitoramento climático de cidades realiza o monitoramento em tempo real de dados climáticos de qualquer cidade no mundo. Inclui dados de temperatura, umidade, velocidade do vento, pressão, umidade e sensação térmica. 
A combinação dessas métricas geram alarmes importantes para condições adversas ou extremas detectadas no local desejado.

## Comunicação
O projeto segue um fluxo simples, que utiliza o protocolo MQTT para comunicação entre seus elementos e a linguagem Python no desenvolvimento
O broker MQTT utilizado foi o Mosquitto, a ferramente de banco de dados temporal foi o InfluxDB e a ferramenta de visualização de dados foi o Grafana 

## Sobre o código
Além de uma estrutura de código auxiliar para criação do cliente MQTT, os códigos responsáveis pela coleta e processamento dos dados são:
## _data_collector.py_
Se comunica com a weather API(https://www.weatherapi.com/), fazendo requisições de dados a cada 10 segundos, o payload vindo da API contém dados de temperatura, umidade, pressão, vento e sensação térmica do dia atual e da previsão do dia seguinte da cidade 

![image](https://github.com/user-attachments/assets/a4ee6597-aa90-4d48-92f0-5385f7510c2f)

Após receber a mensagem vinda da API, extrai o conteúdo do payload e insere em pacotes JSON, formatados com timestamp do momento da medição, e os valores relacionados àquele sensor 

![image](https://github.com/user-attachments/assets/2fbbf0ae-1c6c-40c3-acf7-dbec1ecfc79e)

Depois de recebidos e organizados os dados, o _data_collector_ se inscreve no tópico "sensor_monitors", que contém todos os sensores. E publica os dados separadamente por tópico de sensor, além de uma mensagem inicial informando a periodicidade das medições e os sensores utilizados

![image](https://github.com/user-attachments/assets/867ec760-cc5f-4c7a-b34a-0ccffcf26d2f)

## _data_processor.py_
O data processor se inscreve nos tópicos dos sensores publicados pelo data collector, e recebe os dados via MQTT. Após receber os dados, extrai eles do payload e alimenta as classes relacionadas a cada medição, que contém todos os dados relacionados a cada sensor

![image](https://github.com/user-attachments/assets/5c2d2e5a-01a0-488c-8f4c-1fb384d12d6d)

Após lidos, cada classe de sensor chama a função _checar_alarmes_ que verifica uma combinação de métricas para gerar alarmes de acordo. Os alarmes são:

### 🚨Alarme de tendência de aumento de temperatura
Gera um alarme caso a diferença absoluta entre a temperatura atual e a temperatura prevista para intervalos completos de 6h passa de 5°C

### 🚨Alarme de  onda de frio
Gera um alarme caso a temperatura atual for menor do que 5°C, a sensação térmica for abaixo de zero e a velocidade do vento atual ultrapassar > 15km/h

### 🚨Alarme de  onda de calor
Gera um alarme caso a temperatura atual for maior do que 30°C, a sensação térmica for maior do que 35°C e a umidade do ar for maior do que 60% (eleva a sensação térmica) ou menor do que 30% (aumenta o risco de desidratação e incêndios)

### 🚨Alarme de sensação térmica extrema
Gera um alarme caso a diferença absoluta entre a sensação térmica atual e a temperatura atual forem maior do que 5°C, a velocidade do vento maior do que 20km/h e a umidade do ar for maior do que 60% (eleva a sensação térmica) ou menor do que 30% (aumenta o risco de desidratação e incêndios)

### 🚨Alarme de tempestade severa
Gera um alarme caso a pressão atmosférica atual for menor do que 980hPa, a velocidade do vento for maior do que 50km/h e a umidade do ar for maior do que 85%

Depois de ler os dados e processar em alarmes, o processor persiste os dados em um banco de dados temporal, o InfluxDB, na mesma taxa que recebe os dados do coletor (a cada 10 segundos)

![image](https://github.com/user-attachments/assets/8f281ef4-42ad-4329-8233-7110299c56e1)

## Visualização de dados 
Com uma ótima integração nativa do InfluxDB com o Grafana, a interface faz consultas ao banco de dados e permite a visualização dos dados além dos alarmes disparados da última cidade registrada

![image](https://github.com/user-attachments/assets/d170bfac-5f76-433e-92e9-0277e3d4c108)  ![image](https://github.com/user-attachments/assets/8f0ebd3c-cdc7-4d60-ae8a-02f5ed29e939)

