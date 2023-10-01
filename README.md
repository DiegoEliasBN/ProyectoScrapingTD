# ProyectoScrapingTD

Proyecto final de la clase de Tratamiento de Datos - Maestría Ciberseguridad 

### ¿Qué es Scraping?

El web scraping es un conjunto de prácticas utilizadas para extraer automáticamente — o `«scrapear»` — datos de la web.

# Explicación del proceso de Scraping 

### ¿Qué necesitaremos? 

Para este tipo de procesos necesitaremos.

| Programas | Enlace                                                      |
|-----------|-------------------------------------------------------------|
| PyCharm   | https://www.jetbrains.com/pycharm/download/?section=windows |
| MongoDB   | https://account.mongodb.com/account/login                   |
| Anaconda  | https://www.anaconda.com/download                           |

### Paso: 1

Utilizando Pycharm crearemos un nuevo proyectyo en `.py` 

En nuestro archivo principal del proyecto debemos improtar las siguientes librerias a utilizar.

import `.selenium`

import `.webdriver-manager`

En caso de no tener instalada dichas librerias, podríamos ejecutar en la terminal la instalación 

```commandline

py -m pip install selenium
py -m pip install webdriver-manager

```
![img_1.png](img_1.png)
### Paso: 2
Utilizar Chrome para abrir la página para la extracción de datos

```commandline
from webdriver_manager.chrome import ChromeDriverManager 
driver = webdriver.Chrome
```
### Paso: 3

Determinamos la URL de la web a realizar la extracción de datos

```commandline
driver.get('https://www.airbnb.com/')
```

### Paso: 4

En esta ocasión vamos a extraer los títulos de los sitios recomendados dentro de Airbnb.

![img.png](img.png)

### Paso: 5

Utilizaremos MongoDB como base de datos para almacenar los datos obtenidos. 

Crearemos la conexión a la base de datos mediante el método de driver. 

```commandline

from pymongo.mongo_client import MongoClient 

```
Más la cadena de conexión que nos brinde MongoDB 

### Paso: 6

Si ejecutamos el archivo `mongodb.py` debería establecer la conexión exitosamente. 

![img_2.png](img_2.png)

