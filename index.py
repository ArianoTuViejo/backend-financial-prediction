from flask import Flask, jsonify, request # Importamos Flask y jsonify de flask y request
from controllers.prediction_controller import PredictionController # Importamos el controlador PredictionController
from controllers.data_controller import DataController # Importamos el controlador DataController
# Importamos Gemini

app = Flask(__name__) # Instanciamos la aplicacion
prediction_controller = PredictionController() # Instanciamos el controlador PredictionController
data_controller = DataController() # Instanciamos el controlador DataController

@app.route('/') # Ruta principal
def index(): # Metodo index
    return 'Hola Mundo!' # Retornamos un hola mundo

@app.route('/predict', methods=['POST']) # Ruta para predecir
def predict(): # Metodo para predecir
    datarequest = request.get_json() # Obtenemos la data
    response = prediction_controller.consult(datarequest) # Obtenemos la respuesta
    return jsonify(response), 201 # Retornamos la respuesta

@app.route('/consult', methods=['GET']) # Ruta para consultar
def consult(): # Metodo para consultar
    id_tipo = request.args.get('id_tipo') # Obtenemos el id del tipo
    id_anio = request.args.get('id_anio') # Obtenemos el id del anio
    data =data_controller.consult(id_tipo, id_anio) # Obtenemos la data
    return jsonify(data) # Retornamos la data 