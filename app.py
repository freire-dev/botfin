from sigma import SigmaFinBot
from db import db
from free_users import dbfree
import time
from datetime import datetime, timedelta

ultimoIdMsg = ''

while True:

    try:

        count = 0
        responseBot = SigmaFinBot().obterResultados(ultimoIdMsg)

        if type(responseBot) is dict:

            idMsg = responseBot['update_id']
            qtdLoop = 1

        elif type(responseBot) is list:

            idMsg = responseBot[0]['update_id']
            qtdLoop = responseBot.__len__()

    except:

        ultimoIdMsg = ''
        idMsg = ''

    if idMsg != ultimoIdMsg:

        indexLoop = qtdLoop - 1

        while count != qtdLoop:

            msgRespondida = False

            if type(responseBot) is dict:

                ######################################### Mensagem inicial - /START #########################################
                
                try: 

                    if responseBot['message']['entities'][0]['type'] == 'bot_command' and responseBot['message']['text'] == '/start':

                        idChat = responseBot['message']['from']['id']
                        nome = responseBot['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Olá, {nome}. como vai? \n\nBem-vindo ao Sigma Bet Bot, o melhor robô de estatísticas para apostas esportivas do Brasil! 🤖⚽ \n\nDas opções abaixo, em qual tema posso te ajudar? \n\n🏆 Grupo VIP \n", ["🏆"])
                        msgRespondida = True

                except:
                        
                    pass

                    
                ######################################### Fluxo ---> ⬅ Menu Principal #########################################

                try:

                    if responseBot['message']['text'] == '[🗿 MENU]' and responseBot['message']['chat']['type'] == 'private':

                        idChat = responseBot['message']['from']['id']
                        nome = responseBot['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Bem-vindo ao menu principal, {nome}. tudo certo? \n\nDas opções abaixo, em qual tema posso te ajudar? \n\n🏆 Grupo VIP \n", ["🏆"])
                        msgRespondida = True

                except:

                    pass
                
                ######################################### Fluxo ---> 🏆 Grupo VIP #########################################

                try:

                    if responseBot['message']['text'] == '🏆' and responseBot['message']['chat']['type'] == 'private':

                        idChat = responseBot['message']['from']['id']
                        nome = responseBot['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Perfeito, {nome}! A respeito do Grupo VIP, qual das opções abaixo posso te ajudar? \n\n📕 Informações sobre o Grupo VIP \n🚀 Desejo entrar para o Grupo VIP\n💵 Gerar o pix para o pagamento mensal", ["📕","🚀", "💵"])
                        msgRespondida = True

                except:

                    pass

                try:

                    if responseBot['message']['text'] == '📕' and responseBot['message']['chat']['type'] == 'private':

                        idChat = responseBot['message']['from']['id']
                        nome = responseBot['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Boa, {nome}! O Sigma bet é um grupo VIP que recebe estatísticas em tempo real de partidas AO VIVO de futebol do mundo todo. \n\nOs tipos de estatísticas: \n\n⏩ Probabilidade de Over 0.5 \n⏩ Probabilidade de Over 1.5 \n⏩ Probabilidade de Over 2.5 \n⏩ Probabilidade de Over 3.5 \n🥇 Chances de ganhar \n🥅 Placar \n⛳ Escanteios \n⚽ Chance de Gol \n💪🏻 Ofensividade \n🟢 Dominância \n⚽ Expectativa de Gol \n⏰ Ataques por minuto \n👟 Posse de Bola \n👹 Chutes perigosos \n🟨 Cartão amarelo \n🟥 Cartão vermelho", ['[🗿 MENU]'])
                        msgRespondida = True

                except:

                    pass

                try:

                    if responseBot['message']['text'] == '🚀' and responseBot['message']['chat']['type'] == 'private':

                        idChat = responseBot['message']['from']['id']
                        nome = responseBot['message']['from']['first_name']

                        try:

                            username = responseBot['message']['from']['username']

                            addUserFree = dbfree().addUserFree(idChat, nome, username)

                            if addUserFree == 'Usuário adicionado':

                                SigmaFinBot().enviarMensagemGuiada(idChat, f"Um enorme prazer em saber disso, {nome}! \n\nComo cortesia, para você conhecer melhor o bot de estatística, iremos adicioná-lo automáticamente para uma degustação 0800 por 2 horas para fazer suas apostas. \n\nAproveite!!!", ["[🗿 MENU]"])

                            elif addUserFree == 'Já foi usuário free':
                            
                                SigmaFinBot().enviarMensagemGuiada(idChat, f"Um enorme prazer em saber disso, {nome}! \n\nO valor mensal para permanecer no Grupo VIP recebendo as estatísticas em tempo real dos jogos é de R$29,90 [Somente PIX]. \n\nAssim que identificamos o pagamento, automaticamente adicionaremos você ao Grupo VIP para LUCRAR MUITO! 😎\n\nDas opções abaixo, clique para: \n💸 Realizar pagamento \n[🗿 MENU] Voltar para o menu principal", ["💸","[🗿 MENU]"])

                            msgRespondida = True

                        except:

                            SigmaFinBot().enviarMensagemGuiada(idChat, f"{nome}, foi identificado que você não possuí nome de usuário definido no Telegram. Para participar no grupo, precisará definí-lo. \n\nCaso não saiba como definir o nome do usuário no Telegram, veja o vídeo: https://www.youtube.com/watch?v=7B9HJ0tT9Ns", ["[🗿 MENU]"])
                            msgRespondida = True

                except:

                    pass

                try:

                    if responseBot['message']['text'] == '💸' or responseBot['message']['text'] == '💵' and responseBot['message']['chat']['type'] == 'private':

                        dataHoje = datetime.now().date()
                        dataExp = dataHoje + timedelta(days = 2)
                        idChat = responseBot['message']['from']['id']
                        nome = responseBot['message']['from']['first_name']

                        try:

                            username = responseBot['message']['from']['username']

                            payment = db().addPagDb(idChat, nome, username, dataHoje, dataExp)
                            dataExp = dataExp.strftime("%d/%m/%Y")

                            if payment['msgEnviada'] == False:

                                SigmaFinBot().enviarMensagem(idChat, f"Recebemos sua solicitação de pagamento, {nome}! \n\n⬇️ Chave Pix ⬇️")
                                SigmaFinBot().enviarMensagem(idChat, f"{payment['chavePix']}")
                                SigmaFinBot().enviarMensagemGuiada(idChat, f"Segue abaixo as informações do pagamento: \n\nId pagamento: {payment['idPagamento']} \nMeio de pagamento: {payment['nomeGateway']} \nPagador: {payment['pagador']} \nValor: {payment['valor']} \nDescrição: {payment['descPagamento']} \nData de vencimento: {dataExp} \n\nEspero e vejo você lá no Grupo VIP, {nome}! 🚀", ["[🗿 MENU]"])
                                msgRespondida = True
                            
                            else:

                                msgRespondida = True
                                pass

                        except:

                            SigmaFinBot().enviarMensagemGuiada(idChat, f"{nome}, foi identificado que você não possuí nome de usuário definido no Telegram. Para participar no grupo, precisará definí-lo. \n\nCaso não saiba como definir o nome do usuário no Telegram, veja o vídeo: https://www.youtube.com/watch?v=7B9HJ0tT9Ns", ["[🗿 MENU]"])
                            msgRespondida = True

                except:

                    pass

                ######################################### Mensagem padrão para qualquer outra msg #########################################

                try:

                    if msgRespondida == False:

                        idChat = responseBot['message']['from']['id']
                        nome = responseBot['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Olá, {nome}. tudo certo? \n\nInfelizmente não compreendi o que você deseja... Aconselho você em clicar no botão [🗿 MENU] e checar nosso menu com opções de atendimento.", ["[🗿 MENU]"])

                except:

                    pass

            if type(responseBot) is list:

                ######################################### Mensagem inicial - /START #########################################
                
                try: 

                    if responseBot[indexLoop]['message']['entities'][0]['type'] == 'bot_command' and responseBot[indexLoop]['message']['text'] == '/start':

                        idChat = responseBot[indexLoop]['message']['from']['id']
                        nome = responseBot[indexLoop]['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Olá, {nome}. como vai? \n\nBem-vindo ao Sigma Bet Bot, o melhor robô de estatísticas para apostas esportivas do Brasil! 🤖⚽ \n\nDas opções abaixo, em qual tema posso te ajudar? \n\n🏆 Grupo VIP \n", ["🏆"])
                        msgRespondida = True

                except:
                        
                    pass

                    
                ######################################### Fluxo ---> ⬅ Menu Principal #########################################

                try:

                    if responseBot[indexLoop]['message']['text'] == '[🗿 MENU]' and responseBot[indexLoop]['message']['chat']['type'] == 'private':

                        idChat = responseBot[indexLoop]['message']['from']['id']
                        nome = responseBot[indexLoop]['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Bem-vindo ao menu principal, {nome}. tudo certo? \n\nDas opções abaixo, em qual tema posso te ajudar? \n\n🏆 Grupo VIP \n", ["🏆"])
                        msgRespondida = True

                except:

                    pass            
                
                ######################################### Fluxo ---> 🏆 Grupo VIP #########################################

                try:

                    if responseBot[indexLoop]['message']['text'] == '🏆' and responseBot[indexLoop]['message']['chat']['type'] == 'private':

                        idChat = responseBot[indexLoop]['message']['from']['id']
                        nome = responseBot[indexLoop]['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Perfeito, {nome}! A respeito do Grupo VIP, qual das opções abaixo posso te ajudar? \n\n📕 Informações sobre o Grupo VIP \n🚀 Desejo entrar para o Grupo VIP\n💵 Gerar o pix para o pagamento mensal", ["📕","🚀", "💵"])
                        msgRespondida = True

                except:

                    pass

                try:

                    if responseBot[indexLoop]['message']['text'] == '📕' and responseBot[indexLoop]['message']['chat']['type'] == 'private':

                        idChat = responseBot[indexLoop]['message']['from']['id']
                        nome = responseBot[indexLoop]['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Boa, {nome}! O Sigma bet é um grupo VIP que recebe estatísticas em tempo real de partidas AO VIVO de futebol do mundo todo. \n\nOs tipos de estatísticas: \n\n⏩ Probabilidade de Over 0.5 \n⏩ Probabilidade de Over 1.5 \n⏩ Probabilidade de Over 2.5 \n⏩ Probabilidade de Over 3.5 \n🥇 Chances de ganhar \n🥅 Placar \n⛳ Escanteios \n⚽ Chance de Gol \n💪🏻 Ofensividade \n🟢 Dominância \n⚽ Expectativa de Gol \n⏰ Ataques por minuto \n👟 Posse de Bola \n👹 Chutes perigosos \n🟨 Cartão amarelo \n🟥 Cartão vermelho", ['[🗿 MENU]'])
                        msgRespondida = True

                except:

                    pass

                try:

                    if responseBot[indexLoop]['message']['text'] == '🚀' and responseBot[indexLoop]['message']['chat']['type'] == 'private':

                        idChat = responseBot[indexLoop]['message']['from']['id']
                        nome = responseBot[indexLoop]['message']['from']['first_name']

                        try:

                            username = responseBot[indexLoop]['message']['from']['username']

                            addUserFree = dbfree().addUserFree(idChat, nome, username)

                            if addUserFree == 'Usuário adicionado':

                                SigmaFinBot().enviarMensagemGuiada(idChat, f"Um enorme prazer em saber disso, {nome}! \n\nComo cortesia, para você conhecer melhor o bot de estatística, iremos adicioná-lo automáticamente para uma degustação 0800 por 2 horas para fazer suas apostas. \n\nAproveite!!!", ["[🗿 MENU]"])

                            elif addUserFree == 'Já foi usuário free':
                            
                                SigmaFinBot().enviarMensagemGuiada(idChat, f"Um enorme prazer em saber disso, {nome}! \n\nO valor mensal para permanecer no Grupo VIP recebendo as estatísticas em tempo real dos jogos é de R$29,90 [Somente PIX]. \n\nAssim que identificamos o pagamento, automaticamente adicionaremos você ao Grupo VIP para LUCRAR MUITO! 😎\n\nDas opções abaixo, clique para: \n💸 Realizar pagamento \n[🗿 MENU] Voltar para o menu principal", ["💸","[🗿 MENU]"])

                            msgRespondida = True

                        except:

                            SigmaFinBot().enviarMensagemGuiada(idChat, f"{nome}, foi identificado que você não possuí nome de usuário definido no Telegram. Para participar no grupo, precisará definí-lo. \n\nCaso não saiba como definir o nome do usuário no Telegram, veja o vídeo: https://www.youtube.com/watch?v=7B9HJ0tT9Ns", ["[🗿 MENU]"])
                            msgRespondida = True

                except:

                    pass

                try:

                    if responseBot[indexLoop]['message']['text'] == '💸' or responseBot[indexLoop]['message']['text'] == '💵' and responseBot[indexLoop]['message']['chat']['type'] == 'private':

                        dataHoje = datetime.now().date()
                        dataExp = dataHoje + timedelta(days = 2)
                        idChat = responseBot[indexLoop]['message']['from']['id']
                        nome = responseBot[indexLoop]['message']['from']['first_name']

                        try: 

                            username = responseBot[indexLoop]['message']['from']['username']
                            
                            payment = db().addPagDb(idChat, nome, username, dataHoje, dataExp)
                            dataExp = dataExp.strftime("%d/%m/%Y")

                            if payment['msgEnviada'] == False:
                                SigmaFinBot().enviarMensagem(idChat, f"Recebemos sua solicitação de pagamento, {nome}! \n\n⬇️ Chave Pix ⬇️")
                                SigmaFinBot().enviarMensagem(idChat, f"{payment['chavePix']}")
                                SigmaFinBot().enviarMensagemGuiada(idChat, f"Segue abaixo as informações do pagamento: \n\nId pagamento: {payment['idPagamento']} \nMeio de pagamento: {payment['nomeGateway']} \nPagador: {payment['pagador']} \nValor: {payment['valor']} \nDescrição: {payment['descPagamento']} \nData de vencimento: {dataExp} \n\nEspero e vejo você lá no Grupo VIP, {nome}! 🚀", ["[🗿 MENU]"])
                                msgRespondida = True
                        
                            else:

                                msgRespondida = True
                                pass

                        except:

                            SigmaFinBot().enviarMensagemGuiada(idChat, f"{nome}, foi identificado que você não possuí nome de usuário definido no Telegram. Para participar no grupo, precisará definí-lo. \n\nCaso não saiba como definir o nome do usuário no Telegram, veja o vídeo: https://www.youtube.com/watch?v=7B9HJ0tT9Ns", ["[🗿 MENU]"])
                            msgRespondida = True

                except:

                    pass

                ######################################## Mensagem padrão para qualquer outra msg #########################################

                try:

                    if msgRespondida == False:

                        idChat = responseBot[indexLoop]['message']['from']['id']
                        nome = responseBot[indexLoop]['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Olá, {nome}. tudo certo? \n\nInfelizmente não compreendi o que você deseja... Aconselho você em clicar no botão [🗿 MENU] e checar nosso menu com opções de atendimento.", ["[🗿 MENU]"])

                except:

                    pass

            if qtdLoop > 1:
                indexLoop -= 1

            count += 1
    
    try:

        if type(responseBot) is dict:
            ultimoIdMsg = responseBot['update_id']
        
        elif type(responseBot) is list:
            ultimoIdMsg = responseBot[0]['update_id']

    except:

        pass
    
    time.sleep(1)