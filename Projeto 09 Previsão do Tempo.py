import requests

class Cabreúva :
    def obter_previsao_tempo(self, Cabreúva):
        API_KEY = '53ff75bc97b003a5eed37522ea1fa1ba'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            temperatura = dados['main']['temp']
            descricao = dados['weather'][0]['description']
            print(f"Previsão do tempo para {cidade}: Temperatura: {temperatura}°C, Condição: {descricao}")
        else:
            print("Erro ao obter previsão do tempo.")

# Substitua "53ff75bc97b003a5eed37522ea1fa1ba"
Cabreúva = Cabreúva()
cidade = "Cabreúva"
Cabreúva.obter_previsao_tempo(Cabreúva)
