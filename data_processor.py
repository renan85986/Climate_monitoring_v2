import json
from influxdb_client import InfluxDBClient, BucketsApi
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime, timezone


#conf influxdb
INFLUX_URL = "https://us-east-1-1.aws.cloud2.influxdata.com/"
INFLUX_TOKEN = "yyq7CPXnftjn_IgmBKlol5pfocEITI8i4JxzeCpz7tljcJFl3NxYmQKxZeQMtY-o1LvcGeCRNOX7sCAMzYYsqA=="
INFLUX_ORG = "UFMG"
INFLUX_BUCKET = "Sensores"

influx_connection = InfluxDBClient(url = INFLUX_URL, token = INFLUX_TOKEN, org = INFLUX_ORG) #cria conexão com o influxdb
escrita_influx = influx_connection.write_api(write_options=SYNCHRONOUS) #define objeto para escrita, synchronous diz que o codigo espera a resposta antes de continuar, bloqueando o resto do codigo
def check_string(value):
        
        return f'"{value}"' if isinstance(value, str) else str(value) #"""Se for uma string, coloca entre aspas duplas, senão retorna a string do valor"""

def format_tag(value):
    #""" Substitui espaços por underscore (_) e remove vírgulas para tags do InfluxDB """
    return value.replace(" ", "_").replace(",", "")

#variaveis globais
tmp, umi, prs, vnt, snc, cli = None, None, None, None, None, None

def leitura_mensagem(topico, payload):
    topico_mensagem = topico
    payload_mensagem = json.loads(payload)

    #print(f"O tópico é:{topico_mensagem} e a mensagem: {payload_mensagem}")
    global tmp, umi, prs, vnt, snc, cli 

    if "temperatura" in topico_mensagem:
       tmp =  temperatura.processa_temperatura(payload_mensagem)
    elif "pressao" in topico_mensagem:
       prs = pressao.processa_pressao(payload_mensagem)
    elif "umidade" in topico_mensagem:
        umi = umidade.processa_umidade(payload_mensagem)
    elif "vento" in topico_mensagem:
        vnt = vento.processa_vento(payload_mensagem)
    elif "sensacao_termica" in topico_mensagem:
        snc = sensacao.processa_sensacao(payload_mensagem)
    elif "clima" in topico_mensagem:
        cli = clima.processa_clima(payload_mensagem) 
     
    if tmp and prs and umi and vnt and snc and cli:
        checar_alarmes(tmp,prs,umi,vnt,snc,cli)             

class temperatura:
    def __init__(self, temp_atual, temp_max, temp_min, temp_media, temp_6h_atual, temp_12h_atual, temp_18h_atual, temp_24h_atual, temp_6h_seguinte, temp_12h_seguinte, temp_18h_seguinte, temp_24h_seguinte, timestamp, cidade):
        self.temp_atual = temp_atual
        self.temp_max = temp_max
        self.temp_min = temp_min 
        self.temp_media = temp_media
        self.temp_6h_atual = temp_6h_atual
        self.temp_12h_atual = temp_12h_atual
        self.temp_18h_atual = temp_18h_atual
        self.temp_24h_atual = temp_24h_atual
        self.temp_6h_seguinte = temp_6h_seguinte
        self.temp_12h_seguinte = temp_12h_seguinte
        self.temp_18h_seguinte = temp_18h_seguinte 
        self.temp_24h_seguinte = temp_24h_seguinte
        self.timestamp = timestamp
        self.cidade = cidade

    def processa_temperatura(payload_temp):
        cidade = payload_temp['cidade']
        cidade = format_tag(cidade)
        timestamp = payload_temp['timestamp']
        timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
        timestamp = int(timestamp.timestamp() * 1e9)
        temp_atual = payload_temp['temperatura_atual']['temp_atual']
        #print(f"Temperatura atual: {temp_atual}")
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
        data_point_temperatura = f"temperatura,sensor=temperatura,local={cidade} temp_atual={temp_atual} {timestamp}\n"\
                    f"temperatura,sensor=temperatura,local={cidade} temp_max={temp_max} {timestamp}\n"\
                    f"temperatura,sensor=temperatura,local={cidade} temp_min={temp_min} {timestamp}\n"\
                    f"temperatura,sensor=temperatura,local={cidade} temp_media={temp_media} {timestamp}\n"\
                    f"temperatura,sensor=temperatura,local={cidade} temp_6h_atual={temp_6h_atual} {timestamp}\n"\
                    f"temperatura,sensor=temperatura,local={cidade} temp_12h_atual={temp_12h_atual} {timestamp}\n"\
                    f"temperatura,sensor=temperatura,local={cidade} temp_18h_atual={temp_18h_atual} {timestamp}\n"\
                    f"temperatura,sensor=temperatura,local={cidade} temp_24h_atual={temp_24h_atual} {timestamp}\n"\
                    f"temperatura,sensor=temperatura,local={cidade} temp_6h_seguinte={temp_6h_seguinte} {timestamp}\n"\
                    f"temperatura,sensor=temperatura,local={cidade} temp_12h_seguinte={temp_12h_seguinte} {timestamp}\n"\
                    f"temperatura,sensor=temperatura,local={cidade} temp_18h_seguinte={temp_18h_seguinte} {timestamp}\n"\
                    f"temperatura,sensor=temperatura,local={cidade} temp_24h_seguinte={temp_24h_seguinte} {timestamp}"
        
        escrita_influx.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=data_point_temperatura)
        return temperatura(temp_atual, temp_max, temp_min, temp_media, temp_6h_atual, temp_12h_atual, temp_18h_atual, temp_24h_atual, temp_6h_seguinte, temp_12h_seguinte, temp_18h_seguinte, temp_24h_seguinte, timestamp, cidade)


class pressao:
    def __init__(self, pressao_atual, pressao_6h_atual, pressao_12h_atual, pressao_18h_atual, pressao_24h_atual, pressao_6h_seguinte, pressao_12h_seguinte, pressao_18h_seguinte, pressao_24h_seguinte, timestamp, cidade):
        self.pressao_atual = pressao_atual
        self.pressao_6h_atual = pressao_6h_atual
        self.pressao_12h_atual = pressao_12h_atual
        self.pressao_18h_atual = pressao_18h_atual
        self.pressao_24h_atual = pressao_24h_atual
        self.pressao_6h_seguinte = pressao_6h_seguinte
        self.pressao_12h_seguinte = pressao_12h_seguinte
        self.pressao_18h_seguinte = pressao_18h_seguinte 
        self.pressao_24h_seguinte = pressao_24h_seguinte
        self.timestamp = timestamp
        self.cidade = cidade

    def processa_pressao(payload_pressao):
        timestamp = payload_pressao['timestamp']
        timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
        timestamp = int(timestamp.timestamp() * 1e9)
        cidade = payload_pressao['cidade']
        cidade = format_tag(cidade)
        pressao_atual = payload_pressao['pressao_atual']['pressao_atual']
        pressao_6h_atual = payload_pressao['pressao_dia_atual_6h']['pressao_6h']
        pressao_12h_atual = payload_pressao['pressao_dia_atual_12h']['pressao_12h']
        pressao_18h_atual = payload_pressao['pressao_dia_atual_18h']['pressao_18h']
        pressao_24h_atual = payload_pressao['pressao_dia_atual_24h']['pressao_24h']
        pressao_6h_seguinte = payload_pressao['pressao_dia_seguinte_6h']['pressao_6h']
        pressao_12h_seguinte = payload_pressao['pressao_dia_seguinte_12h']['pressao_12h']
        pressao_18h_seguinte = payload_pressao['pressao_dia_seguinte_18h']['pressao_18h']
        pressao_24h_seguinte = payload_pressao['pressao_dia_seguinte_24h']['pressao_24h']
        data_point_pressao = f"pressao,sensor=pressao,local={cidade} pressao_atual={pressao_atual} {timestamp}\n"\
                    f"pressao,sensor=pressao,local={cidade} pressao_6h_atual={pressao_6h_atual} {timestamp}\n"\
                    f"pressao,sensor=pressao,local={cidade} pressao_12h_atual={pressao_12h_atual} {timestamp}\n"\
                    f"pressao,sensor=pressao,local={cidade} pressao_18h_atual={pressao_18h_atual} {timestamp}\n"\
                    f"pressao,sensor=pressao,local={cidade} pressao_24h_atual={pressao_24h_atual} {timestamp}\n"\
                    f"pressao,sensor=pressao,local={cidade} pressao_6h_seguinte={pressao_6h_seguinte} {timestamp}\n"\
                    f"pressao,sensor=pressao,local={cidade} pressao_12h_seguinte={pressao_12h_seguinte} {timestamp}\n"\
                    f"pressao,sensor=pressao,local={cidade} pressao_18h_seguinte={pressao_18h_seguinte} {timestamp}\n"\
                    f"pressao,sensor=pressao,local={cidade} pressao_24h_seguinte={pressao_24h_seguinte} {timestamp}"
        
        escrita_influx.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=data_point_pressao)
        return pressao(pressao_atual, pressao_6h_atual, pressao_12h_atual, pressao_18h_atual, pressao_24h_atual, pressao_6h_seguinte, pressao_12h_seguinte, pressao_18h_seguinte, pressao_24h_seguinte, timestamp, cidade)

class umidade:
    def __init__(self, umidade_atual, umidade_media, umidade_6h_atual, umidade_12h_atual, umidade_18h_atual, umidade_24h_atual, umidade_6h_seguinte, umidade_12h_seguinte, umidade_18h_seguinte, umidade_24h_seguinte, timestamp, cidade):
        self.umidade_atual = umidade_atual
        self.umidade_dia_atual_todo = umidade_media       
        self.umidade_6h_atual = umidade_6h_atual
        self.umidade_12h_atual = umidade_12h_atual
        self.umidade_18h_atual = umidade_18h_atual
        self.umidade_24h_atual = umidade_24h_atual
        self.umidade_6h_seguinte = umidade_6h_seguinte
        self.umidade_12h_seguinte = umidade_12h_seguinte
        self.umidade_18h_seguinte = umidade_18h_seguinte 
        self.umidade_24h_seguinte = umidade_24h_seguinte
        self.timestamp = timestamp
        self.cidade = cidade

    def processa_umidade(payload_umidade):
        timestamp = payload_umidade['timestamp']
        timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
        timestamp = int(timestamp.timestamp() * 1e9)
        cidade = payload_umidade['cidade']
        cidade = format_tag(cidade)
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
        data_point_umidade = f"umidade,sensor=umidade,local={cidade} umidade_atual={umidade_atual} {timestamp}\n"\
                    f"umidade,sensor=umidade,local={cidade} umidade_media={umidade_media} {timestamp}\n"\
                    f"umidade,sensor=umidade,local={cidade} umidade_6h_atual={umidade_6h_atual} {timestamp}\n"\
                    f"umidade,sensor=umidade,local={cidade} umidade_12h_atual={umidade_12h_atual} {timestamp}\n"\
                    f"umidade,sensor=umidade,local={cidade} umidade_18h_atual={umidade_18h_atual} {timestamp}\n"\
                    f"umidade,sensor=umidade,local={cidade} umidade_24h_atual={umidade_24h_atual} {timestamp}\n"\
                    f"umidade,sensor=umidade,local={cidade} umidade_6h_seguinte={umidade_6h_seguinte} {timestamp}\n"\
                    f"umidade,sensor=umidade,local={cidade} umidade_12h_seguinte={umidade_12h_seguinte} {timestamp}\n"\
                    f"umidade,sensor=umidade,local={cidade} umidade_18h_seguinte={umidade_18h_seguinte} {timestamp}\n"\
                    f"umidade,sensor=umidade,local={cidade} umidade_24h_seguinte={umidade_24h_seguinte} {timestamp}"
        escrita_influx.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=data_point_umidade)
        return umidade(umidade_atual, umidade_media, umidade_6h_atual, umidade_12h_atual, umidade_18h_atual, umidade_24h_atual, umidade_6h_seguinte, umidade_12h_seguinte, umidade_18h_seguinte, umidade_24h_seguinte, timestamp, cidade)


class vento:
    def __init__(self, vento_atual, vento_6h_atual, vento_12h_atual, vento_18h_atual, vento_24h_atual, vento_6h_seguinte, vento_12h_seguinte, vento_18h_seguinte, vento_24h_seguinte, timestamp, cidade):
        self.vento_atual = vento_atual     
        self.vento_6h_atual = vento_6h_atual
        self.vento_12h_atual = vento_12h_atual
        self.vento_18h_atual = vento_18h_atual
        self.vento_24h_atual = vento_24h_atual
        self.vento_6h_seguinte = vento_6h_seguinte
        self.vento_12h_seguinte = vento_12h_seguinte
        self.vento_18h_seguinte = vento_18h_seguinte 
        self.vento_24h_seguinte = vento_24h_seguinte
        self.timestamp = timestamp
        self.cidade = cidade

    def processa_vento(payload_vento):
        timestamp = payload_vento['timestamp']
        timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
        timestamp = int(timestamp.timestamp() * 1e9)
        cidade = payload_vento['cidade']
        cidade = format_tag(cidade)
        vento_atual = payload_vento['vento_atual']['vento_atual']
        vento_6h_atual = payload_vento['vento_dia_atual_6h']['vento_6h']
        vento_12h_atual = payload_vento['vento_dia_atual_12h']['vento_12h']
        vento_18h_atual = payload_vento['vento_dia_atual_18h']['vento_18h']
        vento_24h_atual = payload_vento['vento_dia_atual_24h']['vento_24h']
        vento_6h_seguinte = payload_vento['vento_dia_seguinte_6h']['vento_6h']
        vento_12h_seguinte = payload_vento['vento_dia_seguinte_12h']['vento_12h']
        vento_18h_seguinte = payload_vento['vento_dia_seguinte_18h']['vento_18h']
        vento_24h_seguinte = payload_vento['vento_dia_seguinte_24h']['vento_24h']
        data_point_vento = f"vento,sensor=vento,local={cidade} vento_atual={vento_atual} {timestamp}\n"\
                   f"vento,sensor=vento,local={cidade} vento_6h_atual={vento_6h_atual} {timestamp}\n"\
                   f"vento,sensor=vento,local={cidade} vento_12h_atual={vento_12h_atual} {timestamp}\n"\
                   f"vento,sensor=vento,local={cidade} vento_18h_atual={vento_18h_atual} {timestamp}\n"\
                   f"vento,sensor=vento,local={cidade} vento_24h_atual={vento_24h_atual} {timestamp}\n"\
                   f"vento,sensor=vento,local={cidade} vento_6h_seguinte={vento_6h_seguinte} {timestamp}\n"\
                   f"vento,sensor=vento,local={cidade} vento_12h_seguinte={vento_12h_seguinte} {timestamp}\n"\
                   f"vento,sensor=vento,local={cidade} vento_18h_seguinte={vento_18h_seguinte} {timestamp}\n"\
                   f"vento,sensor=vento,local={cidade} vento_24h_seguinte={vento_24h_seguinte} {timestamp}"
        escrita_influx.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=data_point_vento)
        return vento(vento_atual, vento_6h_atual, vento_12h_atual, vento_18h_atual, vento_24h_atual, vento_6h_seguinte, vento_12h_seguinte, vento_18h_seguinte, vento_24h_seguinte, timestamp, cidade)

class clima:
    def __init__(self, clima_atual, clima_dia, clima_6h_atual, clima_12h_atual, clima_18h_atual, clima_24h_atual, clima_6h_seguinte, clima_12h_seguinte, clima_18h_seguinte, clima_24h_seguinte, timestamp, cidade):
        self.clima_atual = clima_atual
        self.clima_dia_atual_todo = clima_dia       
        self.clima_6h_atual = clima_6h_atual
        self.clima_12h_atual = clima_12h_atual
        self.clima_18h_atual = clima_18h_atual
        self.clima_24h_atual = clima_24h_atual
        self.clima_6h_seguinte = clima_6h_seguinte
        self.clima_12h_seguinte = clima_12h_seguinte
        self.clima_18h_seguinte = clima_18h_seguinte 
        self.clima_24h_seguinte = clima_24h_seguinte
        self.timestamp = timestamp
        self.cidade = cidade


    def processa_clima(payload_clima):
        timestamp = payload_clima['timestamp']
        timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
        timestamp = int(timestamp.timestamp() * 1e9)
        cidade = payload_clima['cidade']
        cidade = format_tag(cidade)
        clima_atual = payload_clima['clima_atual']['clima_atual']
        print(f"clima atual: {clima_atual}")
        clima_dia = payload_clima['clima_dia_atual_todo']['clima_dia']
        clima_6h_atual = payload_clima['clima_dia_atual_6h']['clima_6h']
        clima_12h_atual = payload_clima['clima_dia_atual_12h']['clima_12h']
        clima_18h_atual = payload_clima['clima_dia_atual_18h']['clima_18h']
        clima_24h_atual = payload_clima['clima_dia_atual_24h']['clima_24h']
        clima_6h_seguinte = payload_clima['clima_dia_seguinte_6h']['clima_6h']
        clima_12h_seguinte = payload_clima['clima_dia_seguinte_12h']['clima_12h']
        clima_18h_seguinte = payload_clima['clima_dia_seguinte_18h']['clima_18h']
        clima_24h_seguinte = payload_clima['clima_dia_seguinte_24h']['clima_24h']
        data_point_clima = f"clima,sensor=clima,local={cidade} clima_atual={check_string(clima_atual)} {timestamp}\n"\
                   f"clima,sensor=clima,local={cidade} clima_6h_atual={check_string(clima_6h_atual)} {timestamp}\n"\
                   f"clima,sensor=clima,local={cidade} clima_12h_atual={check_string(clima_12h_atual)} {timestamp}\n"\
                   f"clima,sensor=clima,local={cidade} clima_18h_atual={check_string(clima_18h_atual)} {timestamp}\n"\
                   f"clima,sensor=clima,local={cidade} clima_24h_atual={check_string(clima_24h_atual)} {timestamp}\n"\
                   f"clima,sensor=clima,local={cidade} clima_6h_seguinte={check_string(clima_6h_seguinte)} {timestamp}\n"\
                   f"clima,sensor=clima,local={cidade} clima_12h_seguinte={check_string(clima_12h_seguinte)} {timestamp}\n"\
                   f"clima,sensor=clima,local={cidade} clima_18h_seguinte={check_string(clima_18h_seguinte)} {timestamp}\n"\
                   f"clima,sensor=clima,local={cidade} clima_24h_seguinte={check_string(clima_24h_seguinte)} {timestamp}"

        escrita_influx.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=data_point_clima)
        return clima(clima_atual, clima_dia, clima_6h_atual, clima_12h_atual, clima_18h_atual, clima_24h_atual, clima_6h_seguinte, clima_12h_seguinte, clima_18h_seguinte, clima_24h_seguinte, timestamp, cidade)

class sensacao:
    def __init__(self, sensacao_termica_atual, timestamp, cidade):
        self.sensacao_termica = sensacao_termica_atual
        self.timestamp = timestamp
        self.cidade = cidade

    def processa_sensacao(payload_sensacao):
        timestamp = payload_sensacao['timestamp']
        timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
        timestamp = int(timestamp.timestamp() * 1e9)
        sensacao_termica_atual = payload_sensacao['sensacao_termica_atual']
        cidade = payload_sensacao['cidade']
        cidade = format_tag(cidade)
        data_point_sensacao = f"sensacao,sensor=sensacao,local={cidade} sensacao_termica={sensacao_termica_atual} {timestamp}"
        escrita_influx.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=data_point_sensacao)
        #print(f"Sensacao atual: {sensacao_termica_atual}")
        return sensacao(sensacao_termica_atual, timestamp, cidade)

def alarme_tempestade_severa(pressao_atual, vento_atual, umidade_atual, cidade, timestamp):
    
    if pressao_atual < 980 and vento_atual > 50 and umidade_atual > 85:
        data_point_alarme_ts = f"alarme,maquina=REN1,local={cidade} nome_alarme=\"tempestade_severa\" {timestamp}"
        escrita_influx.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=data_point_alarme_ts)

        print(f"Tempestade severa detectada, pressao:{pressao_atual}, vento:{vento_atual}, umidade:{umidade_atual}")
        return True
    else:
        #print("tempestade severa nao detectada")
        return False
    
def alarme_sensacao_termica_extrema(sensacao_termica, temp_atual, vento_atual, umidade_atual, cidade, timestamp):
    
    if abs(sensacao_termica - temp_atual) > 5 and vento_atual > 20 and (umidade_atual < 30 or umidade_atual > 80) :
        data_point_alarme_ste = f"alarme,maquina=REN1,local={cidade} nome_alarme=\"sensacao_termica_extrema\" {timestamp}"
        escrita_influx.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=data_point_alarme_ste)       
        print(f"Sensação térmica extrema detectada, temperatura:{temp_atual}, sensacao:{sensacao_termica}, umidade:{umidade_atual}")
        return True
    else:
        return False
    
def alarme_onda_calor(sensacao_termica, temp_atual, umidade_atual, cidade, timestamp):
    
    if temp_atual > 20 and sensacao_termica > 20 and  umidade_atual > 0 :
        data_point_alarme_oc = f"alarme,maquina=REN1,local={cidade} nome_alarme=\"onda_calor\" {timestamp}"
        escrita_influx.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=data_point_alarme_oc)
        print(f"Onda de calor detectada, temperatura:{temp_atual}, umidade:{umidade_atual} alta pode aumentar a sensacao:{sensacao_termica},")
        return True
    else:
        return False

def alarme_onda_frio(sensacao_termica, temp_atual, vento_atual, cidade, timestamp):
    
    if temp_atual < 5 and sensacao_termica < 0 and  vento_atual > 20 :
        data_point_alarme_of = f"alarme,maquina=REN1,local={cidade} nome_alarme=\"onda_frio\" {timestamp}"
        escrita_influx.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=data_point_alarme_of)
        print(f"Onda de frio detectada, temperatura:{temp_atual}, sensacao termica caiu {sensacao_termica} devido ao vento forte {vento_atual},")
        return True
    else:
        return False

def alarme_tendencia_aumento_temperatura(temp_atual, temp_6h_atual, temp_12h_atual, temp_18h_atual, temp_24h_atual, cidade, timestamp):
    
    if abs(temp_atual - temp_6h_atual) > 5 or abs(temp_atual - temp_12h_atual) > 5 or abs(temp_atual - temp_18h_atual) > 5 or abs(temp_atual - temp_24h_atual) > 5 :
        data_point_alarme_tat = f"alarme,maquina=REN1,local={cidade} nome_alarme=\"tendencia_aumento\" {timestamp}"
        escrita_influx.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=data_point_alarme_tat)
        print(f"Tendencia de mudança brusca de temperatura em um periodo de 6 horas!")
        return True
    else:
        return False
    


def checar_alarmes(temperatura, pressao, umidade, vento, sensacao, clima):
    #print("checando alarmes")
    alarme_tempestade_severa(pressao.pressao_atual, vento.vento_atual, umidade.umidade_atual, pressao.cidade, pressao.timestamp)
    alarme_sensacao_termica_extrema(sensacao.sensacao_termica, temperatura.temp_atual, vento.vento_atual, umidade.umidade_atual, pressao.cidade, sensacao.timestamp)
    alarme_onda_calor(sensacao.sensacao_termica, temperatura.temp_atual, umidade.umidade_atual, pressao.cidade, sensacao.timestamp)
    alarme_onda_frio(sensacao.sensacao_termica, temperatura.temp_atual, vento.vento_atual, pressao.cidade, sensacao.timestamp)
    alarme_tendencia_aumento_temperatura(temperatura.temp_atual, temperatura.temp_6h_atual, temperatura.temp_12h_atual, temperatura.temp_18h_atual, temperatura.temp_24h_atual, pressao.cidade, temperatura.timestamp)
    