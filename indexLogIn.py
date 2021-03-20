import services.validateUserData as Operations
import repositories.userConexionRepository as DB

class MainLogIn():
    def __init__(self,userName='',password=''):
        self.userName = userName
        self.password = password
    
    def callFunction(self):
        Error = Operations.logIn(self.userName,self.password).validateInput()
        if not Error:
            userPrivileges = DB.logInDB(self.userName,self.password).getUserFromDB()
            if userPrivileges:
                return True
            else:
                return False

def test1(user,password):
    test1 = MainLogIn(user,password).callFunction()
    if test1:
        print("Exito al logearse")
    else:
        print("Usuario o contraseña incorrectos")
        
#test1('ddebortoli','password')