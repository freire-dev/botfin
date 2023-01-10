import requests

class SigmaFinBot:

    def __init__(self):

        self.token = '5948859286:AAEPwfdudgTNad-Y2OZmVmd1nuOHNqzK2sk'
        self.urlBase = f"https://api.telegram.org/bot{self.token}/"

    def enviarMensagem(self, idChat, mensagem):

        chatId = idChat
        link_post = f'{self.urlBase}sendMessage?chat_id={chatId}&text={mensagem}'
        requests.post(link_post)

    def obterResultados(self):

        resp = requests.get(self.urlBase + "getUpdates")
        json = resp.json()['result'][-1]
        print('Resposive 200', json)
        return json