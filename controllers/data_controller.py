
from models.data_model import DataModel  # Importamos el modelo DataModel


class DataController:  # Clase DataController

    def __init__(self):  # Constructor
        self.model = DataModel()  # Instanciamos el modelo

    def consult(self, id_tipo, id_anio):  # Metodo para consultar el id del tipo y el id del anio
        data = self.model.obtener_datos_tabla(
            id_tipo, id_anio)  # Obtenemos los datos de la tabla
        return data  # Retornamos los datos

    def data_exists(self, id_tipo, id_anio, mes):
        data = self.model.existe_registro(id_tipo, id_anio, mes)
        return data

    def save_data(self, data):
        data = self.model.guardar_data(data)
        return data

    def update_data(self, data):
        data = self.model.actualizar_data(data)
        return data

    def get_data_by_type(self, type_id):
        data = self.model.obtener_data_por_tipo(type_id)
        return data
