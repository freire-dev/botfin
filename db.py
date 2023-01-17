import mysql.connector
from payments import statusPayment, createPayment

mydb = mysql.connector.connect(
    host='sql654.main-hosting.eu',
    user='u935568132_luancfreire',
    password='@55h9wy5cL',
    database='u935568132_SigmaBet'
)

mycursor = mydb.cursor()


def listarPagto():

    mycursor.execute("SELECT * FROM payments ORDER BY id DESC")
    myresult = mycursor.fetchall()
    listResult = []

    for x in myresult:
        listResult.append(x)

    dataPag = {
        "qtdPag": listResult.__len__(),
        "listPag": listResult
    }

    print(dataPag)

    return dataPag


def listarMembros():

    mycursor.execute("SELECT * FROM members ORDER BY id DESC")
    myresult = mycursor.fetchall()
    listResult = []

    for x in myresult:
        listResult.append(x)

    dataMembros = {
        "qtdMembros": listResult.__len__(),
        "listMembros": listResult
    }

    print(dataMembros)

    return dataMembros


def addPagDb(idUser, nomeUser, idPix, chavePix, statusPix, dataGerPix, dataVenc):

    dataPagto = listarPagto()
    dataMembros = listarMembros()
    countPagto = 0
    countMembro = 0

    while countPagto != dataPagto['qtdPag']:

        if idUser == dataPagto['listPag'][countPagto][1]:

            while countMembro != dataMembros['qtdMembros']:

                if idUser == dataMembros['listMembros'][countMembro][1]: #Caso for membro

                    if dataMembros['listMembros'][countMembro][3] == 'N':  # Membro inativo

                        createPayment(idUser, nomeUser, dataVenc)
                        mycursor.execute(f"INSERT INTO payments (id, membroId, nomeMembro, idPix, chavePix, statusPix, ativo, dataInicio, dataFim) VALUES(default, {idUser}, '{nomeUser}', {idPix}, '{chavePix}', '{statusPix}', NULL, '{dataGerPix}', '{dataVenc}');")
                        mydb.commit()
                        countPagto = dataPagto['qtdPag']
                        countMembro = dataMembros['qtdMembros']

                    elif dataMembros['listMembros'][countMembro][3] == 'Y':  # Membro ativo

                        if dataMembros['listMembros'][countMembro][5] == 'cancelled': #Não efetuou o pagamento do pix no prazo correto. Nesse caso é preciso enviar um novo pagamento, alterando a data de vencimento.
                          
                          createPayment(idUser, nomeUser, dataVenc)
                          mycursor.execute(f"INSERT INTO payments (id, membroId, nomeMembro, idPix, chavePix, statusPix, ativo, dataInicio, dataFim) VALUES(default, {idUser}, '{nomeUser}', {idPix}, '{chavePix}', '{statusPix}', NULL, '{dataGerPix}', '{dataVenc}');")
                          mydb.commit()
                          countPagto = dataPagto['qtdPag']
                          countMembro = dataMembros['qtdMembros']

                        elif dataMembros['listMembros'][countMembro][5] == 'pending': #Pagamento pendente

                          #Reenviar informações de pagamento.
                          pass

                        elif dataMembros['listMembros'][countMembro][5] == 'accepted': #Membro está no prazo de pagamento. Logo, não precisa pagar outra vez.

                          #Notificar ao membro que o mesmo já realizou o pagamento do mês.
                          pass

                    elif countMembro == (dataMembros['qtdMembros'] - 1):

                        if idUser == dataMembros['listMembros'][countMembro][1]:

                          if dataMembros['listMembros'][countMembro][3] == 'N': #Membro inativo

                            createPayment(idUser, nomeUser, dataVenc)
                            mycursor.execute(f"INSERT INTO payments (id, membroId, nomeMembro, idPix, chavePix, statusPix, ativo, dataInicio, dataFim) VALUES(default, {idUser}, '{nomeUser}', {idPix}, '{chavePix}', '{statusPix}', NULL, '{dataGerPix}', '{dataVenc}');")
                            mydb.commit()
                            countPagto = dataPagto['qtdPag']
                            countMembro = dataMembros['qtdMembros']

                          elif dataMembros['listMembros'][countMembro][3] == 'Y':  # Membro ativo

                            countMembro = dataMembros['qtdMembros']
                            pass

                        else: #Não é membro

                          createPayment(idUser, nomeUser, dataVenc)
                          mycursor.execute(f"INSERT INTO payments (id, membroId, nomeMembro, idPix, chavePix, statusPix, ativo, dataInicio, dataFim) VALUES(default, {idUser}, '{nomeUser}', {idPix}, '{chavePix}', '{statusPix}', NULL, '{dataGerPix}', '{dataVenc}');")
                          mydb.commit()
                          countPagto = dataPagto['qtdPag']

        else:  #Não é membro

            createPayment(idUser, nomeUser, dataVenc)
            mycursor.execute(f"INSERT INTO payments (id, membroId, nomeMembro, idPix, chavePix, statusPix, ativo, dataInicio, dataFim) VALUES(default, {idUser}, '{nomeUser}', {idPix}, '{chavePix}', '{statusPix}', NULL, '{dataGerPix}', '{dataVenc}');")
            mydb.commit()
            countPagto = dataPagto['qtdPag']

    mycursor.execute(f"INSERT INTO payments (id, membroId, nomeMembro, idPix, chavePix, statusPix, ativo, dataInicio, dataFim) VALUES(default, {idUser}, '{nomeUser}', {idPix}, '{chavePix}', '{statusPix}', NULL, '{dataGerPix}', '{dataVenc}');")
    mydb.commit()

statusPayment(53513716364)