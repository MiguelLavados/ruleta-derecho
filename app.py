import streamlit as st

st.set_page_config(page_title="EXAMINADOR", layout="centered")

st.markdown("<h2 style='text-align: center;'>EXAMINADOR DE TEORÍA DEL DERECHO</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Profesor Jaime Esponda</h4>", unsafe_allow_html=True)

with st.sidebar:
    st.caption("🛠️ **Soporte Técnico:**\nMétodo Cognuss II\nMiguel López Lavados")

# ---------------- DATOS DEL EXAMEN ----------------
DATOS_EXAMEN = {
    1: {
        "titulo": "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
        "preguntas": [
            {
                "sub": "1.1", 
                "preg": "¿Características de la norma moral?",
                "opciones": ["A) Autónoma, interior, unilateral, incoercible.", "B) Heterónoma, exterior, bilateral, coercible."],
                "correcta": "A) Autónoma, interior, unilateral, incoercible.",
                "explicacion": "Regula el fuero interno y no usa la fuerza."
            },
            {
                "sub": "1.2", 
                "preg": "¿Diferencia formal entre Derecho y Moral?",
                "opciones": ["A) El Derecho es coercible y bilateral; la Moral es incoercible y unilateral.", "B) Ambos son autónomos e interiores."],
                "correcta": "A) El Derecho es coercible y bilateral; la Moral es incoercible y unilateral.",
                "explicacion": "El Derecho cuenta con la fuerza coactiva del Estado."
            },
            {
                "sub": "1.3", 
                "preg": "¿Qué es la norma de trato social?",
                "opciones": ["A) Decoro y cortesía, heterónoma, exterior, unilateral. Sanción: reproche.", "B) Mandato coactivo estatal."],
                "correcta": "A) Decoro y cortesía, heterónoma, exterior, unilateral. Sanción: reproche.",
                "explicacion": "Impuesta por el grupo social, no tiene exigencia legal."
            }
        ]
    },
    # --- resto de las cédulas igual que tu definición ---
}

# Agregar cédulas pendientes
for i in range(7, 15):
    DATOS_EXAMEN[i] = {"titulo": f"CÉDULA {i}.- (Pendiente)", "preguntas": []}

# ---------------- ESTADO DE SESIÓN ----------------
if "cedula" not in st.session_state:
    st.session_state.cedula = None
if "respuestas" not in st.session_state:
    st.session_state.respuestas = {}
if "evaluado" not in st.session_state:
    st.session_state.evaluado = False

# ---------------- SELECCIÓN DE CÉDULA ----------------
st.write("---")
st.write("### 👨‍🏫 SELECCIÓN DIRECTA DE CÉDULA")

cols = st.columns(5)
for idx, i in enumerate(range(1, 15)):
    with cols[idx % 5]:
        if st.button(f"Cédula {i}", key=f"btn_{i}"):
            st.session_state.cedula = i
            st.session_state.evaluado = False

# ---------------- MOSTRAR PREGUNTAS ----------------
if st.session_state.cedula:
    cedula = DATOS_EXAMEN[st.session_state.cedula]
    st.subheader(cedula["titulo"])

    for pregunta in cedula["preguntas"]:
        respuesta = st.radio(
            f"{pregunta['sub']} {pregunta['preg']}",
            pregunta["opciones"],
            key=f"resp_{pregunta['sub']}"
        )
        st.session_state.respuestas[pregunta['sub']] = respuesta

    if st.button("Evaluar respuestas"):
        st.session_state.evaluado = True

    if st.session_state.evaluado:
        st.write("### 📊 Resultados")
        correctas = 0
        total = len(cedula["preguntas"])
        for pregunta in cedula["preguntas"]:
            sub = pregunta["sub"]
            resp = st.session_state.respuestas
