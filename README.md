
## PREDICCIÓN FINANCIERA CON GEMINI

La predicción financiera es el proceso de utilizar datos históricos y actuales para prever movimientos futuros en los mercados financieros, como precios de acciones, tasas de interés, y otros activos. Con la evolución de la inteligencia artificial (IA), estos procesos se han vuelto más precisos y eficientes. Gemini representa una plataforma avanzada o un conjunto de herramientas basadas en IA que facilita este tipo de análisis financiero.

#### APLICADO A GEMINI:
La predicción financiera con el uso de inteligencia artificial (IA) para analizar datos de mercado y prever futuros movimientos de las empresas; utilizando técnicas avanzadas de aprendizaje automático (Machine Learning) y análisis de datos.

#### ¿COMO FUNCIONA?
Existen diferentes casos de uso:
- Obtener la Data de la base de datos y retornarla
- Generar las predicciones y retornar la petición
- Almacenar Data que manda el Front (Sin Implementar)

En este caso lo utilizaremos para que nos muestre la data de la base de datos y la retorno y nos realice las predicciones

#### REQUERIMIENTOS:
-	Tener una apikey de Gemini
-	Editor de código como visual code
-	Tener Python instalado.

#### VAMOS AL CODIGO:
Aplicamos estos comandos en la terminal, ruta donde esta nuestro proyecto.

**1. crearmos una carpteta venv:**:
```bash
  py -3 -m venv venv
```

**2. activamos los ambientes virtuales con:**:
```bash
  . venv/scripts/activate
```

**3. activamos los ambientes virtuales en windows, tendremos que navegar y activar:**:
```PowerShell
  cd .\venv\
  cd .\scripts\
  activate
    "(venv)"
```

**En caso salga un error al activar el entorno virtual usar Powershell como administrador y ejecutar los siguientes comandos:**:
```PowerShell
  Get-ExecutionPolicy
  Set-ExecutionPolicy Unrestricted
```

**4. intalamos las librerias requeridas:**:
```bash
  pip install -r requirements.txt
```


**EXTRA: si no quieres intalar las librerias requeridas puedes solo intalar flask y las librerías de Gemini:**:
```bash
  pip install Flask google-generativeai
```




#### LEVANTAR EL PROYECTO:

Para levantar el proyecto necesitamos estas variables de entorno, en este caso estoy usando la terminal de git en Windows usamos export

Nota: si se cierra vsCode, tendremos que activar el ambiente virtual, descrito en el paso anterior: venv/scripts/actívate

Para Windows se cambia export por 
```shell
  $env:FLASK_APP = "index.py"
  $env:GEMINI_API_KEY="##############################"
  flask run
```


Con terminal de GIT
```shell
  export FLASK_APP=index.py 
  export GEMINI_API_KEY="##############################"
  flask run
```


## API Referencias

#### Obtener la data

Vamos a obtener la data de la base de datos

```http
  GET / consult
```

#### Hacer la predicción

Hacemos la petición para que nos haga la petición de los meses que tuvo una mayor cantidad de ingresos/egresos de tal año, en este caso tenemos que el id de ingresos es 1 y el de egresos es 2
```http
  GET /predict?id_tipo=1&id_anio=2
```

