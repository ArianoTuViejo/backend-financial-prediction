
from models.data_model import DataModel # Importamos el modelo DataModel

class DataController: # Clase DataController
    
    def __init__(self): # Constructor
        self.model = DataModel() # Instanciamos el modelo
        
    def consult(self, id_tipo, id_anio): # Metodo para consultar el id del tipo y el id del anio
        data = self.model.obtener_datos_tabla(id_tipo, id_anio) # Obtenemos los datos de la tabla
        return data # Retornamos los datos
    