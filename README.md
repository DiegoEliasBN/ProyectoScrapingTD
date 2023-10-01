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
Debemos instalar las librerias. 

import `.selenium`

import `.webdriver-manager`

```commandline

py -m pip install selenium
py -m pip install webdriver-manager

```
![img_1.png](img_1.png)

### Paso: 2
Utilizar Chrome para abrir la página para la extracción de datos

```commandline
from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver-manager

```
