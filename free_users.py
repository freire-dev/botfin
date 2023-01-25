import mysql.connector
from datetime import datetime, timedelta

class dbfree:

    def __init__(self):
        
        self.mydb = mysql.connector.connect(
            host='sql654.main-hosting.eu',
            user='u935568132_luancfreire',
            password='@55h9wy5cL',
            database='u935568132_SigmaBet'
        )

        self.mycursor = self.mydb.cursor()

    def listarUsers(self):

        self.mycursor.execute("SELECT * FROM free_users ORDER BY id DESC")
        myresult = self.mycursor.fetchall()
        listResult = []

        for x in myresult:
            listResult.append(x)

        dataUsers = {
            "qtdUsers": listResult.__len__(),
            "listUsers": listResult
        }

        print(dataUsers)

        return dataUsers
    
    def addUserFree(self, idUser, nomeUser):

        users = self.listarUsers()
        acao = False
        countUsers = 0
        dataEntrada = datetime.now() - timedelta(hours= 3) # Ajustando o horário da Europa com o Brasil
        dataSaida = dataEntrada + timedelta(days = 360, hours=2) #Depois da fase de testes remover os dias e deixar somente hours=2

        while countUsers != users['qtdUsers']:

            if idUser == int(users['listUsers'][countUsers][1]):

                status = 'Já foi usuário free'
                acao = True
                countUsers = users['qtdUsers']

            else: 

                countUsers += 1

        if acao == False:

            self.mycursor.execute(f"INSERT INTO free_users VALUES(DEFAULT, '{idUser}', '{nomeUser}', 'N', 'Y', '{dataEntrada}', '{dataSaida}');")
            self.mydb.commit()
            status = 'Usuário adicionado'
            print(f"Usuário de ID {idUser} - {nomeUser} foi adicionado ao grupo gratuitamente por 2 horas.")

        return status