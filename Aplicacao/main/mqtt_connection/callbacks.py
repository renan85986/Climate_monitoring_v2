from Aplicacao.configs.broker_conf import mqtt_broker_configs

def on_connect(client, userdata, flags, rc): #interrupção que ocorre quando conecta ao broker
    if rc == 0:
        print('conectado!')
        client.subscribe("/temperatura")
        client.subscribe("/umidade")
    else:
        print(f'nao conectei, erro = {rc}')

def on_subscribe(client, userdata, mid, granted_qos):
    print(f'Cliente assinou /temperatura /umidade')         

def on_message(client, userdata, message):
    print('Mensagem Recebida!')
    print(client)
    print(message.payload)  