import json

def leitura_mensagem(topico, payload):
    topico_mensagem = topico
    payload_mensagem = json.loads(payload)

    #print(f"O tópico é:{topico_mensagem} e a mensagem: {payload_mensagem}")

    if "temperatura" in topico_mensagem:
        processa_temperatura(payload_mensagem)
    elif "pressao" in topico_mensagem:
        processa_pressao(payload_mensagem)
    elif "umidade" in topico_mensagem:
        processa_umidade(payload_mensagem)
    elif "vento" in topico_mensagem:
        processa_vento(payload_mensagem)
    elif "sensacao_termica" in topico_mensagem:
        processa_sensacao(payload_mensagem)       


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
''''
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
'''

def processa_pressao(payload_pressao):
    pressao_atual = payload_pressao['pressao_atual']['pressao_atual']
    pressao_6h_atual = payload_pressao['pressao_dia_atual_6h']['pressao_6h']
    pressao_12h_atual = payload_pressao['pressao_dia_atual_12h']['pressao_12h']
    pressao_18h_atual = payload_pressao['pressao_dia_atual_18h']['pressao_18h']
    pressao_24h_atual = payload_pressao['pressao_dia_atual_24h']['pressao_24h']
    pressao_6h_seguinte = payload_pressao['pressao_dia_seguinte_6h']['pressao_6h']
    pressao_12h_seguinte = payload_pressao['pressao_dia_seguinte_12h']['pressao_12h']
    pressao_18h_seguinte = payload_pressao['pressao_dia_seguinte_18h']['pressao_18h']
    pressao_24h_seguinte = payload_pressao['pressao_dia_seguinte_24h']['pressao_24h']

'''
    print(f"a pressao atual :{pressao_atual}")
    print(f"a pressao as 6:{pressao_6h_atual}")
    print(f"a pressao as 12 :{pressao_12h_atual}")
    print(f"a pressao as 18 :{pressao_18h_atual}")
    print(f"a pressao as 24 :{pressao_24h_atual}")
    print(f"a pressao as 6 :{pressao_6h_seguinte}")
    print(f"a pressao as 12 :{pressao_12h_seguinte}")
    print(f"a pressao as 18 :{pressao_18h_seguinte}")
    print(f"a pressao as 24 :{pressao_24h_seguinte}")
'''

def processa_umidade(payload_umidade):
    umidade_atual = payload_umidade['umidade_atual']['umidade_atual']
    umidade_media = payload_umidade['umidade_dia_atual_todo']['umidade_media']
    umidade_6h_atual = payload_umidade['umidade_dia_atual_6h']['umidade_6h']
    umidade_12h_atual = payload_umidade['umidade_dia_atual_12h']['umidade_12h']
    umidade_18h_atual = payload_umidade['umidade_dia_atual_18h']['umidade_18h']
    umidade_24h_atual = payload_umidade['umidade_dia_atual_24h']['umidade_24h']
    umidade_6h_seguinte = payload_umidade['umidade_dia_seguinte_6h']['umidade_6h']
    umidade_12h_seguinte = payload_umidade['umidade_dia_seguinte_12h']['umidade_12h']
    umidade_18h_seguinte = payload_umidade['umidade_dia_seguinte_18h']['umidade_18h']
    umidade_24h_seguinte = payload_umidade['umidade_dia_seguinte_24h']['umidade_24h']
'''
    print(f"a umidade atual :{umidade_atual}")
    print(f"a umidade media :{umidade_media}")
    print(f"a umidade as 6:{umidade_6h_atual}")
    print(f"a umidade as 12 :{umidade_12h_atual}")
    print(f"a umidade as 18 :{umidade_18h_atual}")
    print(f"a umidade as 24 :{umidade_24h_atual}")
    print(f"a umidade as 6 :{umidade_6h_seguinte}")
    print(f"a umidade as 12 :{umidade_12h_seguinte}")
    print(f"a umidade as 18 :{umidade_18h_seguinte}")
    print(f"a umidade as 24 :{umidade_24h_seguinte}")
'''


def processa_vento(payload_vento):
    vento_atual = payload_vento['vento_atual']['vento_atual']
    vento_6h_atual = payload_vento['vento_dia_atual_6h']['vento_6h']
    vento_12h_atual = payload_vento['vento_dia_atual_12h']['vento_12h']
    vento_18h_atual = payload_vento['vento_dia_atual_18h']['vento_18h']
    vento_24h_atual = payload_vento['vento_dia_atual_24h']['vento_24h']
    vento_6h_seguinte = payload_vento['vento_dia_seguinte_6h']['vento_6h']
    vento_12h_seguinte = payload_vento['vento_dia_seguinte_12h']['vento_12h']
    vento_18h_seguinte = payload_vento['vento_dia_seguinte_18h']['vento_18h']
    vento_24h_seguinte = payload_vento['vento_dia_seguinte_24h']['vento_24h']

'''
    print(f"a vento atual :{vento_atual}")
    print(f"a vento as 6:{vento_6h_atual}")
    print(f"a vento as 12 :{vento_12h_atual}")
    print(f"a vento as 18 :{vento_18h_atual}")
    print(f"a vento as 24 :{vento_24h_atual}")
    print(f"a vento as 6 :{vento_6h_seguinte}")
    print(f"a vento as 12 :{vento_12h_seguinte}")
    print(f"a vento as 18 :{vento_18h_seguinte}")
    print(f"a vento as 24 :{vento_24h_seguinte}")
'''

def processa_sensacao(payload_sensacao):
    sensacao_termica_atual = payload_sensacao['sensacao_termica_atual']


  #  print(f"a sensacao atual :{sensacao_termica_atual}")
