import requests
import json
import urllib.parse

class SigmaFinBot:

    def __init__(self):

        self.token = '5826602075:AAEHbmyCiJ1AilxXiGYNyKg3XmIdc87lzkA'
        self.urlBase = f"https://api.telegram.org/bot{self.token}/"

    def enviarMensagem(self, idChat, mensagem):

        chatId = idChat
        link_post = f'{self.urlBase}sendMessage?chat_id={chatId}&text={mensagem}'
        requests.post(link_post)

    def enviarMensagemGuiada(self, idChat, texto, buttonsList):

        print(buttonsList)
        chatId = idChat
        btnObject = {"keyboard": [buttonsList], "one_time_keyboard": True, "resize_keyboard": True, "is_persistent": False}
        buttonsOptions = json.dumps(btnObject)
        buttonsOptions = urllib.parse.quote(f"{buttonsOptions}".encode('utf8'))
        link_post = f'{self.urlBase}sendMessage?chat_id={chatId}&text={texto}&reply_markup={buttonsOptions}'
        requests.post(link_post)

    def obterResultados(self):

        resp = requests.get(self.urlBase + "getUpdates")
        json = resp.json()['result'][-1]
        try:
            print(f"Respose [200] | ID User: {json['message']['from']['id']} ----> Message: {json['message']['text']} ")
        except:
            print('Response [200]')
        return json