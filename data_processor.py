import json

def leitura_mensagem(topico, payload):
    topico_mensagem = topico
    payload_mensagem = json.loads(payload)

    #print(f"O tópico é:{topico_mensagem} e a mensagem: {payload_mensagem}")

    if "temperatura" in topico_mensagem:
        temperatura.processa_temperatura(payload_mensagem)
    elif "pressao" in topico_mensagem:
        pressao.processa_pressao(payload_mensagem)
    elif "umidade" in topico_mensagem:
        umidade.processa_umidade(payload_mensagem)
    elif "vento" in topico_mensagem:
        vento.processa_vento(payload_mensagem)
    elif "sensacao_termica" in topico_mensagem:
        sensacao.processa_sensacao(payload_mensagem)
    elif "clima" in topico_mensagem:
        clima.processa_clima(payload_mensagem)               

class temperatura:
    def __init__(self, temp_atual, temp_max, temp_min, temp_media, temp_6h_atual, temp_12h_atual, temp_18h_atual, temp_24h_atual, temp_6h_seguinte, temp_12h_seguinte, temp_18h_seguinte, temp_24h_seguinte):
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
        return temperatura(temp_atual, temp_max, temp_min, temp_media, temp_6h_atual, temp_12h_atual, temp_18h_atual, temp_24h_atual, temp_6h_seguinte, temp_12h_seguinte, temp_18h_seguinte, temp_24h_seguinte)


class pressao:
    def __init__(self, pressao_atual, pressao_6h_atual, pressao_12h_atual, pressao_18h_atual, pressao_24h_atual, pressao_6h_seguinte, pressao_12h_seguinte, pressao_18h_seguinte, pressao_24h_seguinte):
        self.pressao_atual = pressao_atual
        self.pressao_6h_atual = pressao_6h_atual
        self.pressao_12h_atual = pressao_12h_atual
        self.pressao_18h_atual = pressao_18h_atual
        self.pressao_24h_atual = pressao_24h_atual
        self.pressao_6h_seguinte = pressao_6h_seguinte
        self.pressao_12h_seguinte = pressao_12h_seguinte
        self.pressao_18h_seguinte = pressao_18h_seguinte 
        self.pressao_24h_seguinte = pressao_24h_seguinte

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
        return(pressao_atual, pressao_6h_atual, pressao_12h_atual, pressao_18h_atual, pressao_24h_atual, pressao_6h_seguinte, pressao_12h_seguinte, pressao_18h_seguinte, pressao_24h_seguinte)

class umidade:
    def __init__(self, umidade_atual, umidade_media, umidade_6h_atual, umidade_12h_atual, umidade_18h_atual, umidade_24h_atual, umidade_6h_seguinte, umidade_12h_seguinte, umidade_18h_seguinte, umidade_24h_seguinte):
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
        return(umidade_atual, umidade_media, umidade_6h_atual, umidade_12h_atual, umidade_18h_atual, umidade_24h_atual, umidade_6h_seguinte, umidade_12h_seguinte, umidade_18h_seguinte, umidade_24h_seguinte)


class vento:
    def __init__(self, vento_atual, vento_6h_atual, vento_12h_atual, vento_18h_atual, vento_24h_atual, vento_6h_seguinte, vento_12h_seguinte, vento_18h_seguinte, vento_24h_seguinte):
        self.vento_atual = vento_atual     
        self.vento_6h_atual = vento_6h_atual
        self.vento_12h_atual = vento_12h_atual
        self.vento_18h_atual = vento_18h_atual
        self.vento_24h_atual = vento_24h_atual
        self.vento_6h_seguinte = vento_6h_seguinte
        self.vento_12h_seguinte = vento_12h_seguinte
        self.vento_18h_seguinte = vento_18h_seguinte 
        self.vento_24h_seguinte = vento_24h_seguinte

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
        return(vento_atual, vento_6h_atual, vento_12h_atual, vento_18h_atual, vento_24h_atual, vento_6h_seguinte, vento_12h_seguinte, vento_18h_seguinte, vento_24h_seguinte)

class clima:
    def __init__(self, clima_atual, clima_dia, clima_6h_atual, clima_12h_atual, clima_18h_atual, clima_24h_atual, clima_6h_seguinte, clima_12h_seguinte, clima_18h_seguinte, clima_24h_seguinte):
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

    def processa_clima(payload_clima):
        clima_atual = payload_clima['clima_atual']['clima_atual']
        clima_dia = payload_clima['clima_dia_atual_todo']['clima_dia']
        clima_6h_atual = payload_clima['clima_dia_atual_6h']['clima_6h']
        clima_12h_atual = payload_clima['clima_dia_atual_12h']['clima_12h']
        clima_18h_atual = payload_clima['clima_dia_atual_18h']['clima_18h']
        clima_24h_atual = payload_clima['clima_dia_atual_24h']['clima_24h']
        clima_6h_seguinte = payload_clima['clima_dia_seguinte_6h']['clima_6h']
        clima_12h_seguinte = payload_clima['clima_dia_seguinte_12h']['clima_12h']
        clima_18h_seguinte = payload_clima['clima_dia_seguinte_18h']['clima_18h']
        clima_24h_seguinte = payload_clima['clima_dia_seguinte_24h']['clima_24h']
        return(clima_atual, clima_dia, clima_6h_atual, clima_12h_atual, clima_18h_atual, clima_24h_atual, clima_6h_seguinte, clima_12h_seguinte, clima_18h_seguinte, clima_24h_seguinte)

class sensacao:
    def __init__(self, sensacao_termica_atual):
        self.sensacao_termica = sensacao_termica_atual

    def processa_sensacao(payload_sensacao):
        sensacao_termica_atual = payload_sensacao['sensacao_termica_atual']
        return(sensacao_termica_atual)

def alarme_tempestade_severa(pressao_atual, vento_atual, umidade_atual):
    if pressao_atual < 980 and vento_atual > 50 and umidade_atual > 85:
        print(f"Tempestade severa detectada, pressao:{pressao_atual}, vento:{vento_atual}, umidade:{umidade_atual}")
        return True
    else:
        return False
    
def alarme_sensacao_termica_extrema(sensacao_termica, temp_atual, vento_atual, umidade_atual):
    if abs(sensacao_termica - temp_atual) > 5 and vento_atual > 20 and (umidade_atual < 30 or umidade_atual > 80) :
        print(f"Sensação térmica extrema detectada, temperatura:{temp_atual}, sensacao:{sensacao_termica}, umidade:{umidade_atual}")
        return True
    else:
        return False
    
def alarme_onda_calor(sensacao_termica, temp_atual, umidade_atual):
    if temp_atual > 30 and sensacao_termica > 35 and  umidade_atual > 70 :
        print(f"Onda de calor detectada, temperatura:{temp_atual}, umidade:{umidade_atual} alta pode aumentar a sensacao:{sensacao_termica},")
        return True
    else:
        return False

def alarme_onda_frio(sensacao_termica, temp_atual, vento_atual):
    if temp_atual < 5 and sensacao_termica < 0 and  vento_atual > 20 :
        print(f"Onda de frio detectada, temperatura:{temp_atual}, sensacao termica caiu {sensacao_termica} devido ao vento forte {vento_atual},")
        return True
    else:
        return False

def alarme_tendencia_aumento_temperatura(temp_atual, temp_6h_atual, temp_12h_atual, temp_18h_atual, temp_24h_atual):
    if abs(temp_atual - temp_6h_atual) > 5 or abs(temp_atual - temp_12h_atual) > 5 or abs(temp_atual - temp_18h_atual) > 5 or abs(temp_atual - temp_24h_atual) > 5 :
        print(f"Tendencia de mudança brusca de temperatura em um periodo de 6 horas!")
        return True
    else:
        return False