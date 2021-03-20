import sqlite3

class logInDB():
    "get user and password from db, return acessLevel or False if is not user"
    def __init__(self,userName='',password=''):
        self.userName = userName
        self.password = password
        #self.dataBase = "inventarioHM.db"
        
    def getUserFromDB(self):
        #try:
            connection = sqlite3.connect("repositories/inventarioHM.db")
            isUser = connection.execute("select accessLevel from users where user = ? AND password = ?",(self.userName,self.password))
            isUser = isUser.fetchone()
            connection.close()
            if isUser != None:
                return isUser
            else:
                return False
        #except : 
        #    print("Failed to conect to database")
        
test = logInDB('ddebortoli','password').getUserFromDB()