import repositories.executeQuery as DB
import services.HMInventorySvc as Op

class mainOperations():
    def __init__(self,name='',mark='',price='',amount='',operation=''):
        self.name = name
        self.mark = mark
        self.price = price
        self.amount = amount
        self.operation = operation
        
    def callOperations(self):
        errorValues = ['AGREGAR_ARTICULO','OBTENER_ARTICULOS','ELIMINAR_ARTICULOS']
        if (self.operation).upper in errorValues:
            print("Debe seleccionar una operacion valida")
        else:
            query = Op.HMInventory(self.name,self.mark,self.price,self.amount,self.operation).selectOperation()
            if query:
                result = DB.execQuery(query).executeQuery()
                return result

#Prueba para obtener registros
#print(mainOperations('Prueba7','Prueba7',None,None,'GET_ITEMS').callOperations())

#Prueba para insertar un articulo en la bdd
#print(mainOperations('Prueba8','Prueba7','100','1600','ADD_ITEM').callOperations())

#Prueba para eliminar un articulo, nombre es obligatorio
#print(mainOperations('Prueba7','Prueba7','100','1000','DELETE_ITEM').callOperations())

