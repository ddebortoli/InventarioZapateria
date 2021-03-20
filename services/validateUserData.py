
#!/usr/bin/python

class logIn():
    "LogIn class"
    def __init__(self,userName=None,password=None):
        
        #Variables for logIn
        self.user = userName
        self.password = password
                       
    def validateInput(self):
        "Funcion que comprueba si los datos del usuario son correctos"
        listOfNotValidParameters = ['','NULL','NONE',None]
        if self.user in listOfNotValidParameters:
            print("Usuario es un parametro obligatorio")
        elif self.password in listOfNotValidParameters:
            print("contraseña es un parametro obligatorio")
        else:
            return False
        


    