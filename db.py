import mysql.connector
from sigma import SigmaFinBot
from payments import statusPayment, createPayment
from datetime import datetime, timedelta

class db:

    def __init__(self):
        
        self.mydb = mysql.connector.connect(
            host='sql654.main-hosting.eu',
            user='u935568132_luancfreire',
            password='@55h9wy5cL',
            database='u935568132_SigmaBet'
        )

        self.mycursor = self.mydb.cursor()

        hoje = datetime.now().date()
        self.ult6dias = hoje - timedelta(days=6)

    def listarPagto(self):

        self.mycursor.execute(f"SELECT * FROM payments WHERE dataExpPix >= '{self.ult6dias}' ORDER BY id DESC")
        myresult = self.mycursor.fetchall()
        listResult = []

        for x in myresult:
            listResult.append(x)

        dataPag = {
            "qtdPag": listResult.__len__(),
            "listPag": listResult
        }

        print(dataPag)

        return dataPag


    def listarMembros(self):

        self.mycursor.execute("SELECT * FROM members ORDER BY id DESC")
        myresult = self.mycursor.fetchall()
        listResult = []

        for x in myresult:
            listResult.append(x)

        dataMembros = {
            "qtdMembros": listResult.__len__(),
            "listMembros": listResult
        }

        print(dataMembros)

        return dataMembros


    def addPagDb(self, idUser, nomeUser, dataGer, dataVenc):

        idUser = str(idUser)

        dataPagto = self.listarPagto()
        dataMembros = self.listarMembros()
        countPagto = 0
        countMembro = 0
        addPagto = False
        msgEnviada = False

        while countPagto != dataPagto['qtdPag']:

            if idUser == dataPagto['listPag'][countPagto][1]:

                while countMembro != dataMembros['qtdMembros']:

                    if idUser == dataMembros['listMembros'][countMembro][1]: #Caso for membro

                        if dataMembros['listMembros'][countMembro][3] == 'N':  # Membro inativo

                            if dataPagto['listPag'][countPagto][5] == 'pending':

                                SigmaFinBot().enviarMensagem(idUser, f"Olá, {nomeUser}. Você já está com um pagamento em aberto. Segue chave pix abaixo para efetuar o pagamento:")
                                SigmaFinBot().enviarMensagemGuiada(idUser, f"{dataPagto['listPag'][countPagto][4]}", ["[🗿 MENU]"])
                                msgEnviada = True
                                addPagto = True
                                countPagto = dataPagto['qtdPag']
                                countMembro = dataMembros['qtdMembros']

                            else:

                                novoPag = createPayment(idUser, nomeUser, dataVenc)
                                detalhesPag = statusPayment(novoPag['idPagamento'])
                                self.mycursor.execute(f"INSERT INTO payments VALUES(DEFAULT, '{idUser}', '{nomeUser}', '{novoPag['idPagamento']}', '{novoPag['chavePix']}', '{detalhesPag['status']}', NULL, '{dataGer}', '{dataVenc}');")
                                self.mydb.commit()
                                addPagto = True
                                countPagto = dataPagto['qtdPag']
                                countMembro = dataMembros['qtdMembros']

                        elif dataMembros['listMembros'][countMembro][3] == 'Y':  # Membro ativo

                            if dataMembros['listMembros'][countMembro][5] == 'cancelled': #Não efetuou o pagamento do pix no prazo correto. Nesse caso é preciso enviar um novo pagamento, alterando a data de vencimento.
                            
                                novoPag = createPayment(idUser, nomeUser, dataVenc)
                                detalhesPag = statusPayment(novoPag['idPagamento'])
                                self.mycursor.execute(f"INSERT INTO payments VALUES(DEFAULT, '{idUser}', '{nomeUser}', '{novoPag['idPagamento']}', '{novoPag['chavePix']}', '{detalhesPag['status']}', NULL, '{dataGer}', '{dataVenc}');")
                                self.mydb.commit()
                                addPagto = True
                                countPagto = dataPagto['qtdPag']
                                countMembro = dataMembros['qtdMembros']

                            elif dataMembros['listMembros'][countMembro][5] == 'pending': #Pagamento pendente

                                SigmaFinBot().enviarMensagem(idUser, f"Olá, {nomeUser}. Você já está com um pagamento em aberto. Segue chave pix abaixo para efetuar o pagamento:")
                                SigmaFinBot().enviarMensagemGuiada(idUser, f"{dataPagto['listPag'][countPagto][4]}", ["[🗿 MENU]"])
                                msgEnviada = True
                                addPagto = True
                                countPagto = dataPagto['qtdPag']
                                countMembro = dataMembros['qtdMembros']

                            elif dataMembros['listMembros'][countMembro][5] == 'approved': #Membro está no prazo de pagamento. Logo, não precisa pagar outra vez.

                                SigmaFinBot().enviarMensagemGuiada(idUser, f"Olá, {nomeUser}! Você ainda não precisa efetuar o pagamento do mês.", ["[🗿 MENU]"])
                                msgEnviada = True
                                addPagto = True
                                countPagto = dataPagto['qtdPag']
                                countMembro = dataMembros['qtdMembros']

                        elif countMembro == (dataMembros['qtdMembros'] - 1):

                            if idUser == dataMembros['listMembros'][countMembro][1]:

                                if dataMembros['listMembros'][countMembro][3] == 'N': #Membro inativo

                                    novoPag = createPayment(idUser, nomeUser, dataVenc)
                                    detalhesPag = statusPayment(novoPag['idPagamento'])
                                    self.mycursor.execute(f"INSERT INTO payments VALUES(DEFAULT, '{idUser}', '{nomeUser}', '{novoPag['idPagamento']}', '{novoPag['chavePix']}', '{detalhesPag['status']}', NULL, '{dataGer}', '{dataVenc}');")
                                    self.mydb.commit()
                                    addPagto = True
                                    countPagto = dataPagto['qtdPag']
                                    countMembro = dataMembros['qtdMembros']

                                elif dataMembros['listMembros'][countMembro][3] == 'Y':  # Membro ativo

                                    SigmaFinBot().enviarMensagemGuiada(idUser, f"Olá, {nomeUser}! Você ainda não precisa efetuar o pagamento do mês.", ["[🗿 MENU]"])
                                    msgEnviada = True
                                    addPagto = True
                                    countPagto = dataPagto['qtdPag']
                                    countMembro = dataMembros['qtdMembros']

                    else:  #Não é membro

                        countPagto += 1
                        countMembro += 1

            else:  #Não é membro
                
                countPagto += 1

        if addPagto == False: #Verificando se um não membro já gerou pagamento

            countPagto = 0

            while countPagto != dataPagto['qtdPag']:

                if idUser == dataPagto['listPag'][countPagto][1]:

                    SigmaFinBot().enviarMensagem(idUser, f"Olá, {nomeUser}. Você já está com um pagamento em aberto. Segue chave pix abaixo para efetuar o pagamento:")
                    SigmaFinBot().enviarMensagemGuiada(idUser, f"{dataPagto['listPag'][countPagto][4]}", ["[🗿 MENU]"])
                    msgEnviada = True
                    addPagto = True
                    countPagto = dataPagto['qtdPag']

                else:

                    countPagto += 1

        if addPagto == False: #Adicionando pagamento para não membros                  

            novoPag = createPayment(idUser, nomeUser, dataVenc)
            detalhesPag = statusPayment(novoPag['idPagamento'])
            self.mycursor.execute(f"INSERT INTO payments VALUES(DEFAULT, '{idUser}', '{nomeUser}', '{novoPag['idPagamento']}', '{novoPag['chavePix']}', '{detalhesPag['status']}', NULL, '{dataGer}', '{dataVenc}');")
            self.mydb.commit()

        try:

            data = {
                "msgEnviada": msgEnviada,
                "idPagamento": novoPag['idPagamento'],
                "nomeGateway": novoPag['nomeGateway'],
                "pagador": novoPag['pagador'],
                "valor": novoPag['valor'],
                "descPagamento": novoPag['descPagamento'],
                "chavePix": novoPag['chavePix'],
                "detalhesPag": detalhesPag['linkDetalhes']
            }
            
        except:

            data = {"msgEnviada": msgEnviada}
            
        return data