# Importamos Flask y jsonify de flask y request
from flask import Flask, jsonify, request
from flask_cors import CORS  # Importa CORS desde flask_cors
# Importamos el controlador PredictionController
from controllers.prediction_controller import PredictionController
# Importamos el controlador DataController
from controllers.data_controller import DataController
# Importamos Gemini

app = Flask(__name__)  # Instanciamos la aplicacion
CORS(app)
# Instanciamos el controlador PredictionController
prediction_controller = PredictionController()
data_controller = DataController()  # Instanciamos el controlador DataController


@app.route('/')  # Ruta principal
def index():  # Metodo index
    return 'Hola Mundo!'  # Retornamos un hola mundo


@app.route('/predict', methods=['POST'])  # Ruta para predecir
def predict():  # Metodo para predecir
    datarequest = request.get_json()  # Obtenemos la data
    response = prediction_controller.consult(
        datarequest)  # Obtenemos la respuesta
    return jsonify(response), 201  # Retornamos la respuesta


@app.route('/consult', methods=['GET'])  # Ruta para consultar
def consult():  # Metodo para consultar
    id_tipo = request.args.get('id_tipo')  # Obtenemos el id del tipo
    id_anio = request.args.get('id_anio')  # Obtenemos el id del anio
    data = data_controller.consult(id_tipo, id_anio)  # Obtenemos la data
    return jsonify(data)  # Retornamos la data


@app.route("/data", methods=["GET"])
def getDataByType():
    id_tipo = request.args.get("id_tipo")
    data = data_controller.get_data_by_type(id_tipo)
    return jsonify(data), 200


@app.route("/save-data", methods=["POST",])
def saveData():
    datarequest = request.get_json()
    try:
        if data_controller.data_exists(datarequest["id_tipo"], datarequest["id_anio"], datarequest["mes"]):
            response = {
                "status": "error",
                "message": "Data already exist"
            }
            return jsonify(response), 409
        else:
            data_controller.save_data(datarequest)
        response = {
            "status": "success",
            "message": "Data save successfully",
            "data": datarequest
        }
        return jsonify(response), 201
    except Exception as e:
        response = {
            "status": "error",
            "message": str(e),
        }
        return jsonify(response), 500


@app.route("/update-data", methods=["PATCH",])
def updateData():
    datarequest = request.get_json()
    try:
        if data_controller.data_exists(datarequest["id_tipo"], datarequest["id_anio"], datarequest["mes"]):
            data_controller.update_data(datarequest)
            response = {
                "status": "success",
                "message": "Data update successfully",
                "data": datarequest
            }
            return jsonify(response), 200
        else:
            response = {
                "status": "error",
                "message": "Data does not exist",
            }
            return jsonify(response), 201
    except Exception as e:
        response = {
            "status": "error",
            "message": str(e),
        }
        return jsonify(response), 500
