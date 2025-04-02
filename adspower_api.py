import requests

ADSP_API_URL = "http://local.adspower.net:50325/api/v1/browser/start"

def iniciar_navegador(profile_id):
    params = {"user_id": profile_id}
    resposta = requests.get(ADSP_API_URL, params=params)
    if resposta.status_code == 200:
        dados = resposta.json()
        return dados["data"]["ws"]["selenium"]
    else:
        raise Exception("Erro ao iniciar perfil no AdsPower")
