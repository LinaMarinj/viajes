<h1 align="left">¡Viaja ya!✈️</h1>

###

<p align="left">Sistema de Reserva de Viajes 🌎</p>

###

<p align="left">Este proyecto ofrece un sistema básico para reservar viajes, con cinco destinos disponibles. Los usuarios pueden ingresar los datos del viaje y la información del titular de la reserva. Al finalizar, pueden revisar los detalles de la reserva y visualizar un historial de viajes con los destinos más visitados.<br><br>El objetivo es proporcionar una solución rápida y eficiente para gestionar reservas de viajes.</p>

###

<h2 align="left"></h2>

###

<h2 align="left">Instrucciones de instalación y configuración</h2>

###

Sigue estos pasos para clonar el repositorio, configurar el entorno virtual, instalar las dependencias y ejecutar la aplicación.

1. Clonar el repositorio - Abre la terminal y ejecuta:
``` bash
git clone https://github.com/LinaMarinj/viajes.git
```

2. Acceder a la carpeta del proyecto - Navega al directorio clonado:
``` bash
cd nombre-de-la-carpeta
```


3. Abrir el proyecto en Visual Studio Code - Inicia VS Code desde la terminal:
``` bash
code .
```
También puedes abrir Visual Studio Code manualmente y seleccionar la carpeta del proyecto desde "Archivo" > "Abrir carpeta".


4. Abrir una nueva terminal en Visual Studio Code:


  - En Windows, presiona Ctrl + ñ.
  - O, desde el menú superior, haz clic en los tres puntos ... y selecciona New Terminal.


5. Seleccionar el perfil de terminal recomendado:

   En la terminal, haz clic en la flecha hacia abajo llamada Launch Profile y elige Command Prompt (CMD).

6. Configurar un entorno virtual - Ejecuta el siguiente comando:
``` bash
   python -m venv .venv
```

7. Activar el entorno virtual:
``` bash
   -Windows:
    .venv\Scripts\activate

  -Linux/macOS:
   source .venv/bin/activate
```


8. Instalar las dependencias del proyecto ejecutando:

``` bash
   pip install -r requirements.txt
```
   
Nota: No cierres la terminal mientras se instalan las dependencias, ya que interrumpirás el proceso.

9. Ejecutar la aplicación Usa Streamlit para iniciar la app:
``` bash
    streamlit run app.py
```

 
