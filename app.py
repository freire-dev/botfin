from sigma import SigmaFinBot
import time

ultimoIdMsg = ''

while True:

    responseBot = SigmaFinBot().obterResultados()

    idMsg = responseBot['update_id']

    try:

        if responseBot['my_chat_member']['new_chat_member']['status'] != 'kicked':

            if idMsg != ultimoIdMsg:
        
                if responseBot['message']['entities'][0]['type'] == 'bot_command' and responseBot['message']['text'] == '/start':

                    idChat = responseBot['message']['from']['id']
                    SigmaFinBot().enviarMensagem(idChat, 'Bem-vindo, pequeno gafanhoto!')
                    ultimoIdMsg = responseBot['update_id']
    except:

        if idMsg != ultimoIdMsg:

            if responseBot['message']['entities'][0]['type'] == 'bot_command' and responseBot['message']['text'] == '/start':

                idChat = responseBot['message']['from']['id']
                SigmaFinBot().enviarMensagem(idChat, 'Bem-vindo, pequeno gafanhoto!')
                ultimoIdMsg = responseBot['update_id']

    time.sleep(5)