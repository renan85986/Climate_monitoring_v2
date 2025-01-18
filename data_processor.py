import json

def leitura_mensagem(topico, payload):
    topico_mensagem = topico
    payload_mensagem = json.loads(payload)

    #print(f"O tópico é:{topico_mensagem} e a mensagem: {payload_mensagem}")

    if "temperatura" in topico_mensagem:
        processa_temperatura(payload_mensagem)


def processa_temperatura(payload_temp):
    temp_atual = payload_temp['temperatura_atual']['temp_atual']
    temp_max = payload_temp['temperatura_dia_atual_todo']['temp_max']
    temp_min = payload_temp['temperatura_dia_atual_todo']['temp_min']
    temp_media = payload_temp['temperatura_dia_atual_todo']['temp_media']
    temp_6h_atual = payload_temp['temperatura_dia_atual_6h']['temp_6h']
    temp_12h_atual = payload_temp['temperatura_dia_atual_12h']['temp_12h']
    temp_18h_atual = payload_temp['temperatura_dia_atual_18h']['temp_18h']
    temp_24h_atual = payload_temp['temperatura_dia_atual_24h']['temp_24h']
    temp_6h_seguinte = payload_temp['temperatura_dia_seguinte_6h']['temp_6h']
    temp_12h_seguinte = payload_temp['temperatura_dia_seguinte_12h']['temp_12h']
    temp_18h_seguinte = payload_temp['temperatura_dia_seguinte_18h']['temp_18h']
    temp_24h_seguinte = payload_temp['temperatura_dia_seguinte_24h']['temp_24h']


    print(f"a temperatura atual :{temp_atual}")
    print(f"a temperatura max:{temp_max}")
    print(f"a temperatura min :{temp_min}")
    print(f"a temperatura media :{temp_media}")
    print(f"a temperatura as 6:{temp_6h_atual}")
    print(f"a temperatura as 12 :{temp_12h_atual}")
    print(f"a temperatura as 18 :{temp_18h_atual}")
    print(f"a temperatura as 24 :{temp_24h_atual}")
    print(f"a temperatura as 6 :{temp_6h_seguinte}")
    print(f"a temperatura as 12 :{temp_12h_seguinte}")
    print(f"a temperatura as 18 :{temp_18h_seguinte}")
    print(f"a temperatura as 24 :{temp_24h_seguinte}")

