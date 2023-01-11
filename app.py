from sigma import SigmaFinBot
from payments import createPayment
import time

ultimoIdMsg = ''

while True:

    responseBot = SigmaFinBot().obterResultados()

    idMsg = responseBot['update_id']

    try:

        if responseBot['my_chat_member']['new_chat_member']['status'] != 'kicked':

            if idMsg != ultimoIdMsg:
                
                ######################################### Mensagem inicial - /START #########################################
            
                try: 

                    if responseBot['message']['entities'][0]['type'] == 'bot_command' and responseBot['message']['text'] == '/start':

                        idChat = responseBot['message']['from']['id']
                        nome = responseBot['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Olá, {nome}. como vai? \n\nBem-vindo ao Sigma Bet Bot, o melhor robô de estatísticas para apostas esportivas do Brasil! 🤖⚽ \n\nDas opções abaixo, em qual tema posso te ajudar? \n\n🏆 Grupo VIP \n", ["🏆"])
                        ultimoIdMsg = responseBot['update_id']

                except:
                        
                    pass
                    
                ######################################### Fluxo ---> ⬅ Menu Principal #########################################

                try:

                    if responseBot['message']['text'] == '[🗿 MENU]' and responseBot['message']['chat']['type'] == 'private':

                        idChat = responseBot['message']['from']['id']
                        nome = responseBot['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Bem-vindo ao menu principal, {nome}. tudo certo? \n\nDas opções abaixo, em qual tema posso te ajudar? \n\n🏆 Grupo VIP \n", ["🏆"])
                        ultimoIdMsg = responseBot['update_id']
                
                except:

                    pass
                
                ######################################### Fluxo ---> 🏆 Grupo VIP #########################################

                try:

                    if responseBot['message']['text'] == '🏆' and responseBot['message']['chat']['type'] == 'private':

                        idChat = responseBot['message']['from']['id']
                        nome = responseBot['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Perfeito, {nome}! A respeito do Grupo VIP, qual das opções abaixo posso te ajudar? \n\n📕 Informações sobre o Grupo VIP \n🚀 Desejo entrar para o Grupo VIP\n💵 Gerar o pix para o pagamento mensal\n❌ Sair do grupo VIP", ["📕","🚀", "💵", "❌"])
                        ultimoIdMsg = responseBot['update_id']
                
                except:

                    pass

                try:

                    if responseBot['message']['text'] == '🚀' and responseBot['message']['chat']['type'] == 'private':

                        idChat = responseBot['message']['from']['id']
                        nome = responseBot['message']['from']['first_name']
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"Um enorme prazer em saber disso, {nome}! \n\nO valor mensal para permanecer no Grupo VIP recebendo as estatísticas em tempo real dos jogos é de R$29,90 [Somente PIX]. \n\nAssim que identificamos o pagamento, automaticamente adicionaremos você ao Grupo VIP para LUCRAR MUITO! 😎\n\nDas opções abaixo, clique para: \n💸 Realizar pagamento \n[🗿 MENU] Voltar para o menu principal", ["💸","[🗿 MENU]"])
                        ultimoIdMsg = responseBot['update_id']
                
                except:

                    pass

                try:

                    if responseBot['message']['text'] == '💸' and responseBot['message']['chat']['type'] == 'private':

                        idChat = responseBot['message']['from']['id']
                        nome = responseBot['message']['from']['first_name']

                        payment = createPayment(idChat, nome)
                        SigmaFinBot().enviarMensagem(idChat, f"Recebemos sua solicitação de pagamento, {nome}! \n\n⬇️ Chave Pix ⬇️")
                        SigmaFinBot().enviarMensagem(idChat, f"{payment['chavePix']}")
                        SigmaFinBot().enviarMensagemGuiada(idChat, f"\n\nSegue abaixo as informações do pagamento: \n\nId pagamento: {payment['idPagamento']} \nMeio de pagamento: {payment['nomeGateway']} \nPagador: {payment['pagador']} \nValor: {payment['valor']} \nDescrição: {payment['descPagamento']} \nMais informações: {payment['detalhesPag']} \n\nEspero e vejo você lá no Grupo VIP, {nome}! 🚀", ["[🗿 MENU]"])
                        ultimoIdMsg = responseBot['update_id']
                
                except:

                    pass

    except:

        if idMsg != ultimoIdMsg:

            ######################################### Mensagem inicial - /START #########################################
            
            try: 

                if responseBot['message']['entities'][0]['type'] == 'bot_command' and responseBot['message']['text'] == '/start':

                    idChat = responseBot['message']['from']['id']
                    nome = responseBot['message']['from']['first_name']
                    SigmaFinBot().enviarMensagemGuiada(idChat, f"Olá, {nome}. como vai? \n\nBem-vindo ao Sigma Bet Bot, o melhor robô de estatísticas para apostas esportivas do Brasil! 🤖⚽ \n\nDas opções abaixo, em qual tema posso te ajudar? \n\n🏆 Grupo VIP \n", ["🏆"])
                    ultimoIdMsg = responseBot['update_id']

            except:
                    
                pass
                
            ######################################### Fluxo ---> ⬅ Menu Principal #########################################

            try:

                if responseBot['message']['text'] == '[🗿 MENU]' and responseBot['message']['chat']['type'] == 'private':

                    idChat = responseBot['message']['from']['id']
                    nome = responseBot['message']['from']['first_name']
                    SigmaFinBot().enviarMensagemGuiada(idChat, f"Bem-vindo ao menu principal, {nome}. tudo certo? \n\nDas opções abaixo, em qual tema posso te ajudar? \n\n🏆 Grupo VIP \n", ["🏆"])
                    ultimoIdMsg = responseBot['update_id']
            
            except:

                pass            
            
            ######################################### Fluxo ---> 🏆 Grupo VIP #########################################

            try:

                if responseBot['message']['text'] == '🏆' and responseBot['message']['chat']['type'] == 'private':

                    idChat = responseBot['message']['from']['id']
                    nome = responseBot['message']['from']['first_name']
                    SigmaFinBot().enviarMensagemGuiada(idChat, f"Perfeito, {nome}! A respeito do Grupo VIP, qual das opções abaixo posso te ajudar? \n\n📕 Informações sobre o Grupo VIP \n🚀 Desejo entrar para o Grupo VIP\n💵 Gerar o pix para o pagamento mensal\n❌ Sair do grupo VIP", ["📕","🚀", "💵", "❌"])
                    ultimoIdMsg = responseBot['update_id']
            
            except:

                pass

            try:

                if responseBot['message']['text'] == '🚀' and responseBot['message']['chat']['type'] == 'private':

                    idChat = responseBot['message']['from']['id']
                    nome = responseBot['message']['from']['first_name']
                    SigmaFinBot().enviarMensagemGuiada(idChat, f"Um enorme prazer em saber disso, {nome}! \n\nO valor mensal para permanecer no Grupo VIP recebendo as estatísticas em tempo real dos jogos é de R$29,90 [Somente PIX]. \n\nAssim que identificamos o pagamento, automaticamente adicionaremos você ao Grupo VIP para LUCRAR MUITO! 😎\n\nDas opções abaixo, clique para: \n💸 Realizar pagamento \n[🗿 MENU] Voltar para o menu principal", ["💸","[🗿 MENU]"])
                    ultimoIdMsg = responseBot['update_id']
            
            except:

                pass

            try:

                if responseBot['message']['text'] == '💸' and responseBot['message']['chat']['type'] == 'private':

                    idChat = responseBot['message']['from']['id']
                    nome = responseBot['message']['from']['first_name']
                    payment = createPayment(idChat, nome)
                    SigmaFinBot().enviarMensagem(idChat, f"Recebemos sua solicitação de pagamento, {nome}! \n\n⬇️ Chave Pix ⬇️")
                    SigmaFinBot().enviarMensagem(idChat, f"{payment['chavePix']}")
                    SigmaFinBot().enviarMensagemGuiada(idChat, f"\n\nSegue abaixo as informações do pagamento: \n\nId pagamento: {payment['idPagamento']} \nMeio de pagamento: {payment['nomeGateway']} \nPagador: {payment['pagador']} \nValor: {payment['valor']} \nDescrição: {payment['descPagamento']} \nMais informações: {payment['detalhesPag']} \n\nEspero e vejo você lá no Grupo VIP, {nome}! 🚀", ["[🗿 MENU]"])
                    ultimoIdMsg = responseBot['update_id']
                
            except:

                pass

    time.sleep(1)