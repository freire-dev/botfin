from sigma import SigmaFinBot
from db import db
import time
from datetime import datetime, timedelta

ultimoIdMsg = ''

while True:

    count = 0
    responseBot = SigmaFinBot().obterResultados(ultimoIdMsg)

    if type(responseBot) is dict:

        idMsg = responseBot['update_id']
        qtdLoop = 1

    elif type(responseBot) is list:

        idMsg = responseBot[0]['update_id']
        qtdLoop = responseBot.__len__()

    if idMsg != ultimoIdMsg:

        indexLoop = qtdLoop - 1

        while count != qtdLoop:

            if type(responseBot) is dict:

                ######################################### Mensagem inicial - /START #########################################
                
                try: 

                    if responseBot['message']['entities'][0]['type'] == 'bot_command' and responseBot['message']['text'] == '/start':

                        idChat = responseBot['message']['from']['id']
                        nome = responseBot['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Olá, {nome}. como vai? \n\nBem-vindo ao Sigma Bet Bot, o melhor robô de estatísticas para apostas esportivas do Brasil! 🤖⚽ \n\nDas opções abaixo, em qual tema posso te ajudar? \n\n🏆 Grupo VIP \n", ["🏆"])

                except:
                        
                    pass
                    
                ######################################### Fluxo ---> ⬅ Menu Principal #########################################

                try:

                    if responseBot['message']['text'] == '[🗿 MENU]' and responseBot['message']['chat']['type'] == 'private':

                        idChat = responseBot['message']['from']['id']
                        nome = responseBot['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Bem-vindo ao menu principal, {nome}. tudo certo? \n\nDas opções abaixo, em qual tema posso te ajudar? \n\n🏆 Grupo VIP \n", ["🏆"])
                
                except:

                    pass
                
                ######################################### Fluxo ---> 🏆 Grupo VIP #########################################

                try:

                    if responseBot['message']['text'] == '🏆' and responseBot['message']['chat']['type'] == 'private':

                        idChat = responseBot['message']['from']['id']
                        nome = responseBot['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Perfeito, {nome}! A respeito do Grupo VIP, qual das opções abaixo posso te ajudar? \n\n📕 Informações sobre o Grupo VIP \n🚀 Desejo entrar para o Grupo VIP\n💵 Gerar o pix para o pagamento mensal\n❌ Sair do grupo VIP", ["📕","🚀", "💵", "❌"])
                
                except:

                    pass

                try:

                    if responseBot['message']['text'] == '🚀' and responseBot['message']['chat']['type'] == 'private':

                        idChat = responseBot['message']['from']['id']
                        nome = responseBot['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Um enorme prazer em saber disso, {nome}! \n\nO valor mensal para permanecer no Grupo VIP recebendo as estatísticas em tempo real dos jogos é de R$29,90 [Somente PIX]. \n\nAssim que identificamos o pagamento, automaticamente adicionaremos você ao Grupo VIP para LUCRAR MUITO! 😎\n\nDas opções abaixo, clique para: \n💸 Realizar pagamento \n[🗿 MENU] Voltar para o menu principal", ["💸","[🗿 MENU]"])
                
                except:

                    pass

                try:

                    if responseBot['message']['text'] == '💸' and responseBot['message']['chat']['type'] == 'private':

                        dataHoje = datetime.now().date()
                        dataExp = dataHoje + timedelta(days = 2)
                        idChat = responseBot['message']['from']['id']
                        nome = responseBot['message']['from']['first_name']
                        payment = db().addPagDb(idChat, nome, dataHoje, dataExp)
                        dataExp = dataExp.strftime("%d/%m/%Y")
                        SigmaFinBot().enviarMensagem(idChat, f"Recebemos sua solicitação de pagamento, {nome}! \n\n⬇️ Chave Pix ⬇️")
                        SigmaFinBot().enviarMensagem(idChat, f"{payment['chavePix']}")
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Segue abaixo as informações do pagamento: \n\nId pagamento: {payment['idPagamento']} \nMeio de pagamento: {payment['nomeGateway']} \nPagador: {payment['pagador']} \nValor: {payment['valor']} \nDescrição: {payment['descPagamento']} \nData de vencimento: {dataExp} \n\nEspero e vejo você lá no Grupo VIP, {nome}! 🚀", ["[🗿 MENU]"])
                    
                except:

                    pass

            if type(responseBot) is list:

                ######################################### Mensagem inicial - /START #########################################
                
                try: 

                    if responseBot[indexLoop]['message']['entities'][0]['type'] == 'bot_command' and responseBot[indexLoop]['message']['text'] == '/start':

                        idChat = responseBot[indexLoop]['message']['from']['id']
                        nome = responseBot[indexLoop]['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Olá, {nome}. como vai? \n\nBem-vindo ao Sigma Bet Bot, o melhor robô de estatísticas para apostas esportivas do Brasil! 🤖⚽ \n\nDas opções abaixo, em qual tema posso te ajudar? \n\n🏆 Grupo VIP \n", ["🏆"])

                except:
                        
                    pass
                    
                ######################################### Fluxo ---> ⬅ Menu Principal #########################################

                try:

                    if responseBot[indexLoop]['message']['text'] == '[🗿 MENU]' and responseBot[indexLoop]['message']['chat']['type'] == 'private':

                        idChat = responseBot[indexLoop]['message']['from']['id']
                        nome = responseBot[indexLoop]['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Bem-vindo ao menu principal, {nome}. tudo certo? \n\nDas opções abaixo, em qual tema posso te ajudar? \n\n🏆 Grupo VIP \n", ["🏆"])
                
                except:

                    pass            
                
                ######################################### Fluxo ---> 🏆 Grupo VIP #########################################

                try:

                    if responseBot[indexLoop]['message']['text'] == '🏆' and responseBot[indexLoop]['message']['chat']['type'] == 'private':

                        idChat = responseBot[indexLoop]['message']['from']['id']
                        nome = responseBot[indexLoop]['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Perfeito, {nome}! A respeito do Grupo VIP, qual das opções abaixo posso te ajudar? \n\n📕 Informações sobre o Grupo VIP \n🚀 Desejo entrar para o Grupo VIP\n💵 Gerar o pix para o pagamento mensal\n❌ Sair do grupo VIP", ["📕","🚀", "💵", "❌"])
                
                except:

                    pass

                try:

                    if responseBot[indexLoop]['message']['text'] == '🚀' and responseBot[indexLoop]['message']['chat']['type'] == 'private':

                        idChat = responseBot[indexLoop]['message']['from']['id']
                        nome = responseBot[indexLoop]['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Um enorme prazer em saber disso, {nome}! \n\nO valor mensal para permanecer no Grupo VIP recebendo as estatísticas em tempo real dos jogos é de R$29,90 [Somente PIX]. \n\nAssim que identificamos o pagamento, automaticamente adicionaremos você ao Grupo VIP para LUCRAR MUITO! 😎\n\nDas opções abaixo, clique para: \n💸 Realizar pagamento \n[🗿 MENU] Voltar para o menu principal", ["💸","[🗿 MENU]"])
                
                except:

                    pass

                try:

                    if responseBot[indexLoop]['message']['text'] == '💸' and responseBot[indexLoop]['message']['chat']['type'] == 'private':

                        dataHoje = datetime.now().date()
                        dataExp = dataHoje + timedelta(days = 2)
                        idChat = responseBot[indexLoop]['message']['from']['id']
                        nome = responseBot[indexLoop]['message']['from']['first_name']
                        payment = db().addPagDb(idChat, nome, dataHoje, dataExp)
                        dataExp = dataExp.strftime("%d/%m/%Y")
                        SigmaFinBot().enviarMensagem(idChat, f"Recebemos sua solicitação de pagamento, {nome}! \n\n⬇️ Chave Pix ⬇️")
                        SigmaFinBot().enviarMensagem(idChat, f"{payment['chavePix']}")
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Segue abaixo as informações do pagamento: \n\nId pagamento: {payment['idPagamento']} \nMeio de pagamento: {payment['nomeGateway']} \nPagador: {payment['pagador']} \nValor: {payment['valor']} \nDescrição: {payment['descPagamento']} \nData de vencimento: {dataExp} \n\nEspero e vejo você lá no Grupo VIP, {nome}! 🚀", ["[🗿 MENU]"])
                    
                except:

                    pass

            if qtdLoop > 1:
                indexLoop -= 1

            count += 1
    
    if type(responseBot) is dict:
        ultimoIdMsg = responseBot['update_id']
    
    elif type(responseBot) is list:
        ultimoIdMsg = responseBot[0]['update_id']
    
    time.sleep(1)