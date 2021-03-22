import sqlite3
from re import search

class execQuery():
    def __init__(self,query=''):
        self.query = query
        
    def executeQuery(self):
        try:
            listOfComitts = ['INSERT','UPDATE']
            connection = sqlite3.connect("repositories/inventarioHM.db")
            result = connection.execute(self.query).fetchall()
            connection.commit()
            return result
        except sqlite3.IntegrityError:
            print("This article already exists in the database!")
            return False
        finally:
            connection.close()