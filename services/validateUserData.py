
#!/usr/bin/python

class logIn():
    "LogIn class"
    def __init__(self,userName=None,password=None):
        
        #Variables for logIn
        self.user = userName
        self.password = password
                       
    def validateInput(self):
        "Function that verifies that the user's data is valid"
        listOfNotValidParameters = ['','NULL','NONE',None]
        if self.user in listOfNotValidParameters:
            print("Usuario es un parametro obligatorio")
        elif self.password in listOfNotValidParameters:
            print("Contraseña es un parametro obligatorio")
        else:
            return False
        


    