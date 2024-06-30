import mysql.connector # Importamos el modulo de mysql para conectarnos a la base de datos

class DataModel:
    # Metodo para conectarse a la base de datos
    def connect(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="prediccion"
        )

    def obtener_datos_tabla(self, id_tipo, id_anio): # Metodo para obtener los datos de la tabla
        connection = self.connect() # Nos conectamos a la base de datos
        cursor = connection.cursor(dictionary=True) # Creamos un cursor para obtener los datos
        
        cursor.execute(f"SELECT * FROM data where id_tipo = {id_tipo} and id_anio = {id_anio}") # Ejecutamos la consulta
        resultados = cursor.fetchall() # Obtenemos todos los resultados

        cursor.close() # Cerramos el cursor
        connection.close() # Cerramos la conexion

        return resultados   # Retornamos los resultados
    
    #Obtener el nombre del tipo
    def obtener_nombre_tipo(self, id_tipo):
        connection = self.connect()
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute(f"SELECT tipo FROM tipo_data where id = {id_tipo}")
        resultados = cursor.fetchall()

        cursor.close()
        connection.close()

        return resultados
    
    #Obtener el nombre del anio
    def obtener_nombre_anio(self, id_anio):
        connection = self.connect()
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute(f"SELECT anio FROM anios where id = {id_anio}")
        resultados = cursor.fetchall()

        cursor.close()
        connection.close()

        return resultados
    
   