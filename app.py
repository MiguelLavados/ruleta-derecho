import streamlit as st
import time
import datetime

# --- Caducidad de la aplicación ---
if datetime.date.today() > datetime.date(2026, 6, 30):
    st.error("⏳ La aplicación ha caducado. Disponible solo hasta el 30 de junio de 2026.")
    st.stop()

st.set_page_config(page_title="EXAMINADOR", layout="centered")

st.markdown("<h2 style='text-align: center;'>EXAMINADOR DE TEORÍA DEL DERECHO</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Profesor Jaime Esponda</h4>", unsafe_allow_html=True)

with st.sidebar:
    st.caption("🛠️ **Soporte Técnico:**\nMétodo Cognuss II\nMiguel López Lavados")

# ---------------- DATOS DEL EXAMEN ----------------
# Aquí debes copiar todas las preguntas de tu PDF en formato de 4 alternativas.
# Ejemplo de Cédula 1:

DATOS_EXAMEN = {
    1: {
        "titulo": "CÉDULA 1.- El Derecho y la Moral",
        "preguntas": [
            {
                "sub": "1.1",
                "preg": "¿Características de la norma moral?",
                "opciones": [
                    "A) Autónoma, interior, unilateral, incoercible.",
                    "B) Heterónoma, exterior, bilateral, coercible.",
                    "C) Exterior, bilateral, coercible.",
                    "D) Interior, autónoma, coercible."
                ],
                "correcta": "A) Autónoma, interior, unilateral, incoercible.",
                "explicacion": "Regula el fuero interno y no usa la fuerza."
            },
            {
                "sub": "1.2",
                "preg": "¿Diferencia formal entre Derecho y Moral?",
                "opciones": [
                    "A) El Derecho es coercible y bilateral; la Moral es incoercible y unilateral.",
                    "B) Ambos son autónomos e interiores.",
                    "C) El Derecho es autónomo y unilateral.",
                    "D) La Moral es coercible y bilateral."
                ],
                "correcta": "A) El Derecho es coercible y bilateral; la Moral es incoercible y unilateral.",
                "explicacion": "El Derecho cuenta con la fuerza coactiva del Estado."
            }
        ]
    },
    # --- Aquí debes continuar con las cédulas 2 a 14 usando el mismo formato ---
}

# ---------------- ESTADO DE SESIÓN ----------------
if "cedula" not in st.session_state:
    st.session_state.cedula = 1
if "pregunta_idx" not in st.session_state:
    st.session_state.pregunta_idx = 0

# ---------------- NAVEGACIÓN ----------------
st.write("---")
st.write("### 👨‍🏫 Selección de Cédula")

cols = st.columns(5)
for idx, i in enumerate(range(1, 15)):
    with cols[idx % 5]:
        if st.button(f"Cédula {i}", key=f"btn_{i}"):
            st.session_state.cedula = i
            st.session_state.pregunta_idx = 0

cedula = DATOS_EXAMEN.get(st.session_state.cedula, None)

if cedula and cedula["preguntas"]:
    pregunta = cedula["preguntas"][st.session_state.pregunta_idx]

    st.subheader(cedula["titulo"])
    st.write(f"{pregunta['sub']} {pregunta['preg']}")

    # Alternativas
    respuesta = st.radio("Selecciona una opción:", pregunta["opciones"], key=f"radio_{pregunta['sub']}")

    # Respuesta escrita
    texto = st.text_area("Escribe tu respuesta:", key=f"texto_{pregunta['sub']}")

    # Botón para mostrar respuesta correcta
    if st.button("Ver respuesta"):
        placeholder = st.empty()
        placeholder.success(f"✅ Respuesta correcta: {pregunta['correcta']}\n\nℹ️ {pregunta['explicacion']}")
        time.sleep(25)
        placeholder.empty()

    # Navegación entre preguntas
    col1, col2 = st.columns(2)
    if col1.button("⬅️ Anterior"):
        if st.session_state.pregunta_idx > 0:
            st.session_state.pregunta_idx -= 1
    if col2.button("➡️ Siguiente"):
        if st.session_state.pregunta_idx < len(cedula["preguntas"]) - 1:
            st.session_state.pregunta_idx += 1
else:
    st.warning("⚠️ Esta cédula aún no tiene preguntas cargadas.")
