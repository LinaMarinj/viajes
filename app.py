import streamlit as st
from openpyxl import Workbook, load_workbook
from datetime import datetime
import os

# Configuración del estilo
st.markdown(
    """
    <style> 
    .withScreencast > div { 
        background-image: url('http://alavion.like-themes.com/wp-content/uploads/2018/02/SLIDE_02.jpg'); 
        background-size: cover; 
        background-position: center; 
        background-attachment: fixed; 
    } 
    .withScreencast header { 
        background: none !important; 
    } 
    .stForm { 
        background-color: rgba(255, 255, 255, 0.8); 
        border-radius: 10px; 
    } 
    </style>
    """,
    unsafe_allow_html=True
)

st.title("¡A Viajar!")

# Inicializar variables de sesión
if 'reservar' not in st.session_state:
    st.session_state.reservar = False

# Función para guardar en Excel (SOLO DATOS DEL SEGUNDO PROYECTO)
def guardar_reserva(datos):
    try:
        filename = "reservas_viajes.xlsx"
        
        # Crear archivo nuevo o cargar existente
        if not os.path.exists(filename):
            wb = Workbook()
            ws = wb.active
            ws.append([
                "Destino", 
                "Personas", 
                "Fecha Viaje", 
                "Fecha Registro"
            ])
        else:
            wb = load_workbook(filename)
            ws = wb.active
        
        # Agregar nueva fila con formato de fecha
        fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M")
        nueva_fila = [
            datos['destino'],
            datos['personas'],
            datos['fecha'].strftime("%Y-%m-%d"),
            fecha_registro
        ]
        
        ws.append(nueva_fila)
        wb.save(filename)
        return True
        
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return False

# Formulario principal (SOLO DATOS DEL PROYECTO 2)
with st.form("reserva_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        destino = st.selectbox("Destino", [
            "España", "Dubai", "Francia", 
            "Italia", "Brasil"
        ])
        
    with col2:
        personas = st.number_input(
            "Personas", 
            min_value=1, 
            max_value=10,
            help="Número de viajeros"
        )
    
    fecha = st.date_input(
        "Fecha del viaje", 
        min_value=datetime.today(),
        format="DD/MM/YYYY"
    )
    
    if st.form_submit_button("Confirmar Reserva"):
        # Validar datos
        if personas > 0 and fecha:
            # Preparar datos para guardar
            datos_reserva = {
                'destino': destino,
                'personas': personas,
                'fecha': fecha
            }
            
            # Guardar en Excel
            if guardar_reserva(datos_reserva):
                st.balloons()
                st.success("Reserva registrada exitosamente!")
                st.session_state.reservar = True
            else:
                st.error("Error al guardar la reserva")
        else:
            st.warning("Completa todos los campos correctamente")

# Mensaje final
if st.session_state.get('reservar'):
    st.write("---")
    st.subheader("Detalles de la reserva:")
    st.write(f"*Destino:* {destino}")
    st.write(f"*Viajeros:* {personas} personas")
    st.write(f"*Fecha:* {fecha.strftime('%d/%m/%Y')}")