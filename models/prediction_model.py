
import google.generativeai as genai # Importamos la libreria de google para el uso de la inteligencia artificial
import os # Importamos la libreria os
from models.data_model import  DataModel # Importamos el modelo DataModel

class PredictionModel: # Clase PredictionModel
    
    
    def __init__(self): # Constructor
        genai.configure(api_key=os.getenv("GEMINI_API_KEY")) # Configuramos la api key
        self.model = genai.GenerativeModel(model_name="gemini-pro") # Instanciamos el modelo generativo
        
    def consult(self, datarequest): # Metodo para consultar
        
        print("DATA REQUEST: ", datarequest) # Imprimimos la data
        
        # Meses
        meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
         'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
        
        dataModel = DataModel() # Instanciamos el modelo DataModel
        
        # Obtenemos los datos de la tabla
        data_consulta = dataModel.obtener_datos_tabla(datarequest['tipo_dato'], datarequest['tipo_anio']) 
        
        # Obtenemos el nombre del tipo
        tipo_data_nombre = dataModel.obtener_nombre_tipo(datarequest['tipo_dato'])[0]['tipo']
        
        # Obtenemos el nombre del anio
        tipo_anio_nombre = dataModel.obtener_nombre_anio(datarequest['tipo_anio'])[0]['anio']
        
        # Obtenemos los totales
        array_totales = []
        for element in data_consulta:
            array_totales.append(element['total'])

        # Obtenemos el mes con mayor cantidad de datos
        consult = ("De acuerdo a este arreglo de meses ", str(meses)," tenemos que los ", str(tipo_data_nombre), " una empresa en el año ", str(tipo_anio_nombre), "son estos ",
        str(array_totales), " Dime que mes es el que tuvo una mayor cantidad de", str(tipo_data_nombre),"y en un valor aparte dime el monto")
    
        # Imprimimos la consulta
        print("Consulta: ", consult)
        
         # Genera el contenido con el modelo
        response = self.model.generate_content(consult)
        print("CONSULTA EXITOSA: ")

        # Imprime la respuesta
        print(response.text)
        
        return response.text # Retornamos la respuesta
    