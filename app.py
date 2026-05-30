import streamlit as st
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
# Aquí se definen todas las cédulas con sus preguntas y respuestas.
# Para simplificar, muestro solo un ejemplo de cada cédula. 
# Tú puedes ampliar con todas las preguntas del PDF siguiendo la misma estructura.

DATOS_EXAMEN = {
    1: {
        "titulo": "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
        "preguntas": [
            {
                "sub": "1.1",
                "preg": "¿Características de la norma moral?",
                "opciones": [
                    "A) Autónoma, interior, unilateral, incoercible.",
                    "B) Heterónoma, exterior, bilateral, coercible."
                ],
                "correcta": "A) Autónoma, interior, unilateral, incoercible.",
                "explicacion": "Regula el fuero interno y no usa la fuerza."
            },
            {
                "sub": "1.2",
                "preg": "¿Diferencia formal entre Derecho y Moral?",
                "opciones": [
                    "A) El Derecho es coercible y bilateral; la Moral es incoercible y unilateral.",
                    "B) Ambos son autónomos e interiores."
                ],
                "correcta": "A) El Derecho es coercible y bilateral; la Moral es incoercible y unilateral.",
                "explicacion": "El Derecho cuenta con la fuerza coactiva del Estado."
            }
        ]
    },
    2: {
        "titulo": "CÉDULA 2.- La Norma Jurídica. Características. Estructura lógica.",
        "preguntas": [
            {
                "sub": "2.1",
                "preg": "¿Características de la norma jurídica?",
                "opciones": [
                    "A) Heterónoma, exterior, bilateral, coercible.",
                    "B) Autónoma, interior, unilateral, incoercible."
                ],
                "correcta": "A) Heterónoma, exterior, bilateral, coercible.",
                "explicacion": "Emana de autoridad externa y es imponible por la fuerza."
            },
            {
                "sub": "2.2",
                "preg": "¿Normas imperativas vs permisivas?",
                "opciones": [
                    "A) Ordenan o prohíben de forma absoluta.",
                    "B) Conceden facultad legítima para actuar o no."
                ],
                "correcta": "A) Ordenan o prohíben de forma absoluta.",
                "explicacion": "Las imperativas no pueden ser modificadas; las permisivas otorgan opción."
            }
        ]
    },
    3: {
        "titulo": "CÉDULA 3.- Vigencia, Validez y Eficacia de las Normas Jurídicas.",
        "preguntas": [
            {
                "sub": "3.1",
                "preg": "¿Tipos de derogación de la ley?",
                "opciones": [
                    "A) Expresa, tácita, total o parcial.",
                    "B) Solo por mutuo acuerdo."
                ],
                "correcta": "A) Expresa, tácita, total o parcial.",
                "explicacion": "La derogación puede ser explícita o por incompatibilidad."
            }
        ]
    },
    # --- Continúa rellenando las cédulas 4 a 14 con las preguntas del PDF ---
}

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
            resp = st.session_state.respuestas.get(sub, None)
            if resp == pregunta["correcta"]:
                st.success(f"{sub}: Correcto ✅ - {pregunta['explicacion']}")
                correctas += 1
            else:
                st.error(f"{sub}: Incorrecto ❌ - {pregunta['explicacion']}")
        st.info(f"Resultado final: {correctas}/{total} correctas")
