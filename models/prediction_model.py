
# Importamos la libreria de google para el uso de la inteligencia artificial
import google.generativeai as genai
import os  # Importamos la libreria os
from models.data_model import DataModel  # Importamos el modelo DataModel


class PredictionModel:  # Clase PredictionModel

    def __init__(self):  # Constructor
        # Configuramos la api key
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        # Instanciamos el modelo generativo
        self.model = genai.GenerativeModel(model_name="gemini-pro")

    def consult(self, datarequest):  # Metodo para consultar

        print("DATA REQUEST: ", datarequest)  # Imprimimos la data

        # Meses
        meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
                 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

        dataModel = DataModel()  # Instanciamos el modelo DataModel

        # Obtenemos los datos de la tabla
        data_consulta = dataModel.obtener_datos_tabla(
            datarequest['tipo_dato'], datarequest['tipo_anio'])

        # Obtenemos el nombre del tipo
        tipo_data_nombre = dataModel.obtener_nombre_tipo(
            datarequest['tipo_dato'])[0]['tipo']

        # Obtenemos el nombre del anio
        tipo_anio_nombre = dataModel.obtener_nombre_anio(
            datarequest['tipo_anio'])[0]['anio']

        # Obtenemos los totales
        array_totales = []
        for element in data_consulta:
            array_totales.append(element['total'])

        # Obtenemos el mes con mayor cantidad de datos
        # consult = ("De acuerdo a este arreglo de meses ", str(meses)," tenemos que los ", str(tipo_data_nombre), " una empresa en el año ", str(tipo_anio_nombre), "son estos ",
        # str(array_totales), " Dime que mes es el que tuvo una mayor cantidad de", str(tipo_data_nombre),"y en un valor aparte dime el monto")
        # consult = ("De acuerdo a este arreglo de meses ", str(meses)," tenemos que los ", str(tipo_data_nombre), " una empresa en el año ", str(tipo_anio_nombre), "son estos ",
        # str(array_totales), "devuelve una prediccion con regresión lineal de estos datos de los", str(tipo_data_nombre),"del siguiente mes")

        consult = (f"Predice el total de {str(tipo_data_nombre)} para el siguiente mes basado en los datos de ingresos del año {tipo_anio_nombre}: {
                   array_totales}", "Solo necesito que me devuelvas el ingreso total predicho para el siguiente mes, no necesito que me pases más texto, solo el dato final")

        # Imprimimos la consulta
        print("Consulta: ", consult)

        # Genera el contenido con el modelo
        response = self.model.generate_content(consult)
        print("CONSULTA EXITOSA: ")

        try:
            prediction_text = response.text
            predict_income = float(prediction_text)

            return {"prediction": predict_income}
        except (ValueError, IndexError) as e:
            print(f"Error al procesar la respuesta del modelo: {e}")
            return {"message": "Error: No se pudo obtener una predicción válida"}