import mysql.connector

def showUserByLogin(Login):
    myDb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="userdb"
    )

#afahana miinisiliser le requete
    myCursor = myDb.cursor()
    #sql = "SELECT * FROM user WHERE login = {}" format(login)
    sql = "SELECT * FROM user WHERE Login = '%s'" %Login
    myCursor.execute(sql)

    #formation anakiray voaloahany iany no alaiy = fetchone
    myResults= myCursor.fetchone()
    return myResults


