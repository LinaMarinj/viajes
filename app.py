import streamlit as st

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

if "reservar" not in st.session_state:
    st.session_state.reservar = False

if "comprar" not in st.session_state:
    st.session_state.comprar = False 

with st.form("reserva"):
    destino = st.selectbox("Destino", ["Seleciona un destino","España", "Dubai", "Francia", "Italia","Brasil"])
    personas = st.number_input("Personas a viajar", min_value=1, max_value=10)
    fecha =st.date_input("Fecha del viaje", min_value="today")
    reservar = st.form_submit_button("Reservar")


if reservar:
    st.session_state.reservar = True
   
if st.session_state.reservar:
     st.subheader("Información de la reserva")
     with st.form("comprador"):
        cedula = st.number_input("Cédula", min_value=0)
        nombre = st.text_input("Nombre", placeholder="Tú nombre")
        apellido = st.text_input("Apellido", placeholder="Tú apellido")
        telefono = st.number_input("Télefono", min_value=0)
        correo = st.text_input("Correo Electronico", placeholder="tucorreo@gmail.com")
        comprar = st.form_submit_button("comprar")

     if comprar:
        st.session_state.comprar = True

if st.session_state.comprar: 
    st.write("Reserva realizada con éxito ✅")    
