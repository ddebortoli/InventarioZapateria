import sqlite3

conexion=sqlite3.connect("inventarioHM.db")
conexion.execute("insert into users(accessLevel,user,password) values (?,?,?)", (1,"ddebortoli","password"))

try:
    conexion.execute("""create table users (
                              id integer primary key autoincrement,
                              accessLevel integer,
                              user text,
                              password text
                        )""")
    print("se creo la tabla articulos")                        
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")                    
conexion.close()
