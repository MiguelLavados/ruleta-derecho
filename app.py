import streamlit as st
from cedulas import DATOS_EXAMEN

st.set_page_config(page_title="EXAMINADOR DE TEORÍA DEL DERECHO", layout="centered")

st.markdown("<h1 style='text-align: center; color: #1E3A8A; margin-bottom: 0;'>EXAMINADOR DE TEORÍA DEL DERECHO</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #4B5563; font-weight: normal; margin-top: 0;'>Profesor Jaime Esponda</h3>", unsafe_allow_html=True)

with st.sidebar:
    st.write("")
    st.caption("---")
    st.caption("🛠️ **Soporte Técnico:**")
    st.caption("Método Cognuss II — Miguel López Lavados")

if "cedula" not in st.session_state: st.session_state.cedula = None
if "respuestas_usuario" not in st.session_state: st.session_state.respuestas_usuario = {}
if "evaluado" not in st.session_state: st.session_state.evaluado = False

st.write("---")
st.write("### 👨‍🏫 SELECCIÓN DIRECTA DE CÉDULA")

cols = st.columns(5)
for idx, i in enumerate(range(1, 15)):
    with cols[idx % 5]:
        if st.button(f"Cédula {i}", use_container_width=True):
            st.session_state.cedula = i
            st.session_state.evaluado = False
            st.session_state.respuestas_usuario = {}

st.write("---")

if st.session_state.cedula:
    datos_cedula = DATOS_EXAMEN[st.session_state.cedula]
    st.success(f"### 📍 {datos_cedula['titulo']}")
    
    if not datos_cedula["preguntas"]:
        st.info("Esta cédula está habilitada, esperando que incorporemos sus contenidos.")
    else:
        for idx, p in enumerate(datos_cedula["preguntas"]):
            st.markdown(f"#### Pregunta {p['sub']}: {p['preg']}")
            clave_pregunta = f"p_{p['sub']}"
            st.session_state.respuestas_usuario[clave_pregunta] = st.radio("Selecciona:", options=p["opciones"], key=clave_pregunta, index=None)

        if not st.session_state.evaluado and st.button("📝 EVALUAR EXAMEN", type="primary", use_container_width=True):
            st.session_state.evaluado = True
            st.rerun()

        if st.session_state.evaluado:
            st.write("---")
            correctas = 0
            total = len(datos_cedula["preguntas"])
            for p in datos_cedula["preguntas"]:
                clave = f"p_{p['sub']}"
                resp = st.session_state.respuestas_usuario.get(clave)
                if resp == p["correcta"]:
                    correctas += 1
                    st.success(f"✅ **Pregunta {p['sub']}: Correcta.**")
                else:
                    st.error(f"❌ **Pregunta {p['sub']}: Incorrecta.**\n\n**Correcta:** {p['correcta']}")
            
            nota = round(1.0 + (correctas / total) * 6.0, 1) if total > 0 else 1.0
            st.metric(label="⭐⭐ NOTA FINAL ⭐⭐", value=f"{nota}")
