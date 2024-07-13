# Importamos el modulo de mysql para conectarnos a la base de datos
import mysql.connector


class DataModel:
    # Metodo para conectarse a la base de datos
    def connect(self):
        return mysql.connector.connect(
            host="localhost",
            port=3310,
            user="root",
            password="Ariano2784",
            database="prediccion"
        )

    # Metodo para obtener los datos de la tabla
    def obtener_datos_tabla(self, id_tipo, id_anio):
        connection = self.connect()  # Nos conectamos a la base de datos
        # Creamos un cursor para obtener los datos
        cursor = connection.cursor(dictionary=True)

        # Ejecutamos la consulta
        cursor.execute(
            f"SELECT * FROM data where id_tipo = {id_tipo} and id_anio = {id_anio}")
        resultados = cursor.fetchall()  # Obtenemos todos los resultados

        cursor.close()  # Cerramos el cursor
        connection.close()  # Cerramos la conexion

        return resultados   # Retornamos los resultados

    # Obtener el nombre del tipo
    def obtener_nombre_tipo(self, id_tipo):
        connection = self.connect()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(f"SELECT tipo FROM tipo_data where id = {id_tipo}")
        resultados = cursor.fetchall()

        cursor.close()
        connection.close()

        return resultados

    # Obtener el nombre del anio
    def obtener_nombre_anio(self, id_anio):
        connection = self.connect()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(f"SELECT anio FROM anios where id = {id_anio}")
        resultados = cursor.fetchall()

        cursor.close()
        connection.close()

        return resultados

    def obtener_data_por_tipo(self, id_tipo):
        connection = self.connect()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            f"SELECT * FROM data where id_tipo = {id_tipo}")
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results

    def existe_registro(self, id_tipo, id_anio, mes):
        connection = self.connect()
        cursor = connection.cursor(dictionary=True)

        sql = "SELECT COUNT(*) as count FROM data WHERE id_tipo = %s AND id_anio = %s AND mes = %s"
        cursor.execute(sql, (id_tipo, id_anio, mes))
        resultado = cursor.fetchone()

        cursor.close()
        connection.close()

        return resultado['count'] > 0

    def guardar_data(self, data):
        connection = self.connect()
        cursor = connection.cursor()

        sql = "INSERT INTO data (id_tipo, id_anio, mes, total) VALUES (%s, %s, %s, %s)"
        values = (data['id_tipo'], data['id_anio'], data['mes'], data['total'])
        cursor.execute(sql, values)
        connection.commit()

        cursor.close()
        connection.close()

    def actualizar_data(self, data):
        connection = self.connect()
        cursor = connection.cursor()

        sql = "UPDATE data SET total = %s WHERE id_tipo = %s AND id_anio = %s AND mes = %s"
        values = (data['total'], data['id_tipo'], data['id_anio'], data['mes'])
        cursor.execute(sql, values)
        connection.commit()

        cursor.close()
        connection.close()
