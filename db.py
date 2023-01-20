import mysql.connector
from sigma import SigmaFinBot
from payments import statusPayment, createPayment

class db:

    def __init__(self):
        
        self.mydb = mysql.connector.connect(
            host='sql654.main-hosting.eu',
            user='u935568132_luancfreire',
            password='@55h9wy5cL',
            database='u935568132_SigmaBet'
        )

        self.mycursor = self.mydb.cursor()

    def listarPagto(self):

        self.mycursor.execute("SELECT * FROM payments ORDER BY id DESC")
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

        while countPagto != dataPagto['qtdPag']:

            if idUser == dataPagto['listPag'][countPagto][1]:

                while countMembro != dataMembros['qtdMembros']:

                    if idUser == dataMembros['listMembros'][countMembro][1]: #Caso for membro

                        if dataMembros['listMembros'][countMembro][3] == 'N':  # Membro inativo

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
                                SigmaFinBot().enviarMensagem(idUser, f"{detalhesPag['chavePix']}")
                                addPagto = True
                                countPagto = dataPagto['qtdPag']
                                countMembro = dataMembros['qtdMembros']

                            elif dataMembros['listMembros'][countMembro][5] == 'approved': #Membro está no prazo de pagamento. Logo, não precisa pagar outra vez.

                                SigmaFinBot().enviarMensagem(idUser, f"Olá, {nomeUser}! Você ainda não precisa efetuar o pagamento do mês.")
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

                                    SigmaFinBot().enviarMensagem(idUser, f"Olá, {nomeUser}. Você já está com um pagamento em aberto. Segue chave pix abaixo para efetuar o pagamento:")
                                    SigmaFinBot().enviarMensagem(idUser, f"{detalhesPag['chavePix']}")
                                    addPagto = True
                                    countPagto = dataPagto['qtdPag']
                                    countMembro = dataMembros['qtdMembros']

                    else:  #Não é membro

                        countMembro += 1

            else:  #Não é membro
                
                countPagto += 1
                countMembro += 1

        if addPagto == False:

            novoPag = createPayment(idUser, nomeUser, dataVenc)
            detalhesPag = statusPayment(novoPag['idPagamento'])
            self.mycursor.execute(f"INSERT INTO payments VALUES(DEFAULT, '{idUser}', '{nomeUser}', '{novoPag['idPagamento']}', '{novoPag['chavePix']}', '{detalhesPag['status']}', NULL, '{dataGer}', '{dataVenc}');")
            self.mydb.commit()

        data = {
        "idPagamento": novoPag['idPagamento'],
        "nomeGateway": novoPag['nomeGateway'],
        "pagador": novoPag['pagador'],
        "valor": novoPag['valor'],
        "descPagamento": novoPag['descPagamento'],
        "chavePix": novoPag['chavePix'],
        "detalhesPag": detalhesPag['linkDetalhes']
        }

        return data