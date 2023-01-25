import requests
import json
import urllib.parse

class SigmaFinBot:

    def __init__(self):

        self.token = '5961072934:AAFUd8pQIxTaTc6fxkUE9M8UTdxrxUAoi00'
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

    def obterResultados(self, ultimoIdMsg):

        if ultimoIdMsg == '': #Inicio/Start do bot no servidor

            resp = requests.get(self.urlBase + "getUpdates")
            json = resp.json()['result'][-1]

            return json

        else:

            resp = requests.get(self.urlBase + "getUpdates")
            json = resp.json()['result'][-1]
            ultimoIdMsgAPI = json['update_id']

            if ultimoIdMsgAPI > ultimoIdMsg:

                index = -1
                diferenca = ultimoIdMsgAPI - ultimoIdMsg
                indexFinal = (index - diferenca)
                listaMsgs = []

                while index != indexFinal:

                    try:

                        json = resp.json()['result'][index]
                        if json['message']['chat']['type'] == 'private':
                            listaMsgs.append(json)
                            index -= 1

                    except:

                        index -= 1
                        pass
                
                print(listaMsgs)
                return listaMsgs

            elif ultimoIdMsgAPI == ultimoIdMsg:

                json = resp.json()['result'][-1]
                return json