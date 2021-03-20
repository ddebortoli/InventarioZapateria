import sqlite3
class execQuery():
    def __init__(self,query=''):
        self.query = query
        
    def executeQuery(self):
        try:
            connection = sqlite3.connect("repositories/inventarioHM.db")
            result = connection.execute(self.query).fetchall()
            return result
        except:
            print("Error al conectar")
            return False
