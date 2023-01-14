import mysql.connector

mydb = mysql.connector.connect(
  host='sql654.main-hosting.eu', 
  user='u935568132_luancfreire', 
  password='@55h9wy5cL',
  database='u935568132_SigmaBet'
)

mycursor = mydb.cursor()

def listarPag():

  mycursor.execute("SELECT * FROM payments")
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

def addPagDb(membroId, idPix, chavePix, statusPix, ativo, dataInicio, dataFim):

  data = listarPag()
  count = 0

  while count != data['qtdPag']:

    if membroId == data['listPag'][0][1]:

      pass

    else:

      count += 1
  

  mycursor.execute(f"INSERT INTO payments (id, membroId, nomeMembro, idPix, chavePix, statusPix, ativo, dataInicio, dataFim) VALUES(default, 123, 'Membro Teste 3', 12345678910, 'ChavePix', 'pending', 'N', '2023-01-13', NULL);")
  mydb.commit()

listarPag()