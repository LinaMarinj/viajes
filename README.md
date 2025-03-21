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

## Guía de Uso para la Aplicación "¡A Viajar!"
¡Bienvenido(a) a tu asistente de viajes! Esta aplicación te permitirá reservar tus viajes de manera sencilla. Sigue estos pasos para utilizarla sin problemas:

1. Inicio
Al abrir la aplicación, verás un título que dice "Bienvenido(a) ¡A Viajar!" acompañado de un fondo agradable. Aquí podrás comenzar tu reserva.

2. Selecciona tu Destino y Número de Viajeros
En el primer formulario, escoge tu destino entre las opciones disponibles como España, Dubai, Francia, Italia o Brasil.
Indica cuántas personas viajarán contigo (puedes elegir entre 1 y 10 viajeros).
Selecciona la fecha de tu viaje.
Cuando completes estos campos, presiona el botón Reservar para continuar.

3. Datos Personales
Una vez que hayas reservado tu destino y el número de personas, se abrirá un nuevo formulario donde tendrás que ingresar tus datos personales:

Cédula: Escribe tu número de identificación (sin puntos ni guiones).
Teléfono: Ingresa tu número de celular (sin espacios ni guiones).
Nombre y Apellido: Introduce tu nombre y apellido completos.
Correo Electrónico: Asegúrate de ingresar un correo electrónico válido.
Cuando termines, haz clic en Confirmar compra para continuar.

4. Confirmación de Reserva
Si todo está correcto, verás un mensaje que confirma tu reserva con éxito. 🎉 Además, aparecerán todos los detalles de tu viaje y tus datos personales en pantalla. La aplicación también guarda la información en un archivo de Excel para que puedas revisar el historial de tus reservas.

5. Ver el Historial de Reservas
Si ya tienes reservas anteriores, la aplicación mostrará un gráfico con el número de viajeros por destino y fecha, lo que te permitirá ver fácilmente cuántas personas han viajado contigo y cuándo lo hicieron.

6. Nueva Reserva
Si deseas hacer una nueva reserva, puedes hacer clic en el botón 🔄 Nueva Reserva y el sistema te permitirá comenzar nuevamente.

¡Eso es todo! Disfruta de tu experiencia y buen viaje. ✈️

## Dependencias
Streamlit
Es la herramienta principal que permite crear la interfaz web interactiva. Con Streamlit, la aplicación muestra formularios, gráficos y mensajes en la pantalla de manera sencilla, sin necesidad de conocimientos profundos en desarrollo web.

pandas
Se utiliza para gestionar y manipular datos, especialmente para leer y escribir archivos de Excel. Esto permite que la aplicación guarde y recupere las reservas de viaje en un formato organizado.

os
Es un módulo de Python que ayuda a interactuar con el sistema operativo. En este caso, se usa para verificar si el archivo donde se almacenan las reservas ya existe, y para gestionar la creación y actualización de ese archivo.

Plotly Express
Esta dependencia se encarga de crear gráficos interactivos. La aplicación utiliza Plotly Express para generar un gráfico que muestra el historial de reservas, permitiendo visualizar de manera clara la información de los viajes realizados.

openpyxl
Es una biblioteca especializada en trabajar con archivos Excel. Permite crear nuevos archivos, cargar archivos existentes y modificar su contenido. Aquí se usa para almacenar la información de las reservas en un archivo de Excel.

datetime
Este módulo gestiona fechas y horas. La aplicación lo utiliza para registrar la fecha y hora en la que se realiza cada reserva, asegurando que se guarde la información con la marca de tiempo correcta.

Cada una de estas dependencias cumple un rol específico que, en conjunto, hacen posible que la aplicación sea interactiva, almacene datos y presente información de manera visual y amigable para el usuario.

## Contribuciones de cada miembro
@LinaMarinj
Se crea formulario con los campos necesarios para hacer la reserva
Se crear el readme con toda la informacion y descripcion del proyecto
Se organiza el diseño y estilos de toda la aplicacion

@Juancode88
mejoras del repo incial y se agrega función de guardar registros en excel

@JONZLCESDE
se agrega la grafica y se actualiza el requirements porque requeri de unas dependencias para q la chart funcionara
