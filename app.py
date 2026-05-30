import streamlit as st

st.set_page_config(page_title="EXAMINADOR", layout="centered")

st.markdown("<h2 style='text-align: center;'>EXAMINADOR DE TEORÍA DEL DERECHO</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Profesor Jaime Esponda</h4>", unsafe_allow_html=True)

with st.sidebar:
    st.caption("🛠️ **Soporte Técnico:**\nMétodo Cognuss II\nMiguel López Lavados")

# --- Tus datos del examen (los dejo igual que los que compartiste) ---
DATOS_EXAMEN = { ... }  # aquí va todo tu diccionario tal cual

for i in range(7, 15):
    DATOS_EXAMEN[i] = {"titulo": f"CÉDULA {i}.- (Pendiente)", "preguntas": []}

# --- Estado de sesión ---
if "cedula" not in st.session_state:
    st.session_state.cedula = None
if "respuestas" not in st.session_state:
    st.session_state.respuestas = {}
if "evaluado" not in st.session_state:
    st.session_state.evaluado = False

st.write("---")
st.write("### 👨‍🏫 SELECCIÓN DIRECTA DE CÉDULA")

cols = st.columns(5)
for idx, i in enumerate(range(1, 15)):
    with cols[idx % 5]:
        if st.button(f"Cédula {i}", key=f"btn_{i}"):
            st.session_state.cedula = i
            st.session_state.evaluado = False

# --- Mostrar preguntas de la cédula seleccionada ---
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
            resp = st.session_state.respuestas.get(sub, None)
            if resp == pregunta["correcta"]:
                st.success(f"{sub}: Correcto ✅ - {pregunta['explicacion']}")
                correctas += 1
            else:
                st.error(f"{sub}: Incorrecto ❌ - {pregunta['explicacion']}")
        st.info(f"Resultado final: {correctas}/{total} correctas")
