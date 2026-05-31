import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Evaluación Oral", layout="wide")

# Estilos visuales rápidos para asemejar tu interfaz
st.markdown("""
    <style>
    .titulo-panel { font-size: 24px; font-weight: bold; margin-bottom: 20px; }
    .cuadro-cedula { background-color: #E8F5E9; padding: 20px; border-radius: 5px; border-left: 5px solid #2E7D32; color: #1B5E20; font-size: 20px; font-weight: bold; }
    .titulo-controles { font-size: 18px; font-weight: bold; margin-top: 30px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# 1. Base de datos simulada de tus Cédulas
DATOS_CEDULAS = {
    1: "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
    2: "CÉDULA 2.- Fuentes del Derecho y la Ley.",
    3: "CÉDULA 3.- Interpretación e Integración de la Ley.",
    4: "CÉDULA 4.- Efectos de la Ley en el Tiempo y el Espacio.",
    5: "CÉDULA 5.- Sujetos de Derecho y Personas Naturales."
}

# 2. Inicializar el estado de la aplicación (Cédula actual)
if "cedula_actual" not in st.session_state:
    st.session_state.cedula_actual = 1

# --- INTERFAZ GRÁFICA ---

# Encabezado lateral simulado
st.caption("Soporte Técnico: Método Cognuss II  \nMiguel López Lavados")

# Título Principal
st.markdown('<div class="titulo-panel">👨‍🏫 PANEL DIRECTO DE EVALUACIÓN ORAL (CÉDULAS 1 A 5)</div>', unsafe_allow_html=True)

# Fila de botones superiores (Cédulas individuales)
cols_superiores = st.columns(5)
for i in range(1, 6):
    # Si la cédula es la activa, resalta visualmente de alguna forma (Streamlit type primary)
    tipo_boton = "primary" if st.session_state.cedula_actual == i else "secondary"
    if cols_superiores[i-1].button(f"Cédula {i}", key=f"btn_top_{i}", type=tipo_boton, use_container_width=True):
        st.session_state.cedula_actual = i

st.write("---")

# Contenido de la Cédula Seleccionada
contenido = DATOS_CEDULAS.get(st.session_state.cedula_actual, "Cédula no encontrada")
st.markdown(f'<div class="cuadro-cedula">📍 {contenido}</div>', unsafe_allow_html=True)

# Controles del Examinador en la parte inferior
st.markdown('<div class="titulo-controles">🎲 CONTROLES DEL EXAMINADOR</div>', unsafe_allow_html=True)

col_ant, col_sig, _ = st.columns([1, 1, 4])

# Funciones de navegación
def avanzar():
    if st.session_state.cedula_actual < 5:
        st.session_state.cedula_actual += 1

def retroceder():
    if st.session_state.cedula_actual > 1:
        st.session_state.cedula_actual -= 1

# Botones de control físico
btn_anterior = col_ant.button("⬅️ Anterior", on_click=retroceder, use_container_width=True)
btn_siguiente = col_sig.button("➡️ Siguiente", on_click=avanzar, use_container_width=True)


# --- INYECCIÓN DE JAVASCRIPT (ATAJOS DE TECLADO) ---
# Este script escucha globalmente las teclas y hace clic invisible en tus botones de Streamlit
st.components.v1.html(
    """
    <script>
    const doc = window.parent.document;
    
    doc.addEventListener('keydown', function(e) {
        // Detener acciones nativas del navegador (ej: que Backspace te mande a la página anterior de Chrome)
        if (e.key === 'Backspace' || e.key === ' ' || e.key === 'Enter') {
            e.preventDefault();
        }
        
        // Buscar todos los elementos botón generados por Streamlit
        const botones = Array.from(doc.querySelectorAll('button'));
        
        // Identificar los botones correctos por su texto interno
        const botonAnterior = botones.find(b => b.innerText.includes('Anterior'));
        const botonSiguiente = botones.find(b => b.innerText.includes('Siguiente'));
        
        // Ejecución de eventos según la tecla presionada
        if (e.key === 'Backspace' && botonAnterior) {
            botonAnterior.click();
        } else if ((e.key === ' ' || e.key === 'Enter') && botonSiguiente) {
            botonSiguiente.click();
        }
    });
    </script>
    """,
    height=0,
)
