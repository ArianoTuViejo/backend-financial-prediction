from  models.prediction_model import PredictionModel

class PredictionController:
    
    def __init__(self): # Constructor
        self.model = PredictionModel() # Instanciamos el modelo
        
    def consult(self, datarequest): # Metodo para consultar
        print("DATA REQUEST: ", datarequest) # Imprimimos la data
        data = self.model.consult(datarequest) # Obtenemos la data
        return data # Retornamos la data
    
    