import streamlit as st
import datetime

# =====================================================
# CONFIGURACIÓN INICIAL
# =====================================================

st.set_page_config(
    page_title="EXAMINADOR",
    layout="centered"
)

# =====================================================
# CADUCIDAD
# =====================================================

if datetime.date.today() > datetime.date(2026, 6, 30):
    st.error(
        "⏳ La aplicación ha caducado. Disponible solo hasta el 30 de junio de 2026."
    )
    st.stop()

# =====================================================
# ENCABEZADO
# =====================================================

st.markdown(
    "<h2 style='text-align:center;'>EXAMINADOR DE TEORÍA DEL DERECHO</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align:center;'>Profesor Jaime Esponda</h4>",
    unsafe_allow_html=True
)

with st.sidebar:
    st.markdown("### ℹ️ Información")
    st.caption(
        "Método Cognuss II\n\n"
        "Desarrollado por Miguel López Lavados"
    )

# =====================================================
# BASE DE DATOS DEL EXAMEN
# =====================================================

DATOS_EXAMEN = {
    1: {
        "titulo": "CÉDULA 1 - EL DERECHO Y LA MORAL",
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
                "explicacion": (
                    "La norma moral regula el fuero interno "
                    "y no utiliza fuerza coactiva."
                )
            },
            {
                "sub": "1.2",
                "preg": "¿Diferencia formal entre Derecho y Moral?",
                "opciones": [
                    "A) El Derecho es coercible y bilateral; "
                    "la Moral es incoercible y unilateral.",
                    "B) Ambos son autónomos e interiores.",
                    "C) El Derecho es autónomo y unilateral.",
                    "D) La Moral es coercible y bilateral."
                ],
                "correcta": (
                    "A) El Derecho es coercible y bilateral; "
                    "la Moral es incoercible y unilateral."
                ),
                "explicacion": (
                    "El Derecho cuenta con la posibilidad "
                    "de aplicar coerción mediante el Estado."
                )
            }
        ]
    },

    2: {
        "titulo": "CÉDULA 2",
        "preguntas": []
    },

    3: {
        "titulo": "CÉDULA 3",
        "preguntas": []
    },

    4: {
        "titulo": "CÉDULA 4",
        "preguntas": []
    },

    5: {
        "titulo": "CÉDULA 5",
        "preguntas": []
    },

    6: {
        "titulo": "CÉDULA 6",
        "preguntas": []
    },

    7: {
        "titulo": "CÉDULA 7",
        "preguntas": []
    },

    8: {
        "titulo": "CÉDULA 8",
        "preguntas": []
    },

    9: {
        "titulo": "CÉDULA 9",
        "preguntas": []
    },

    10: {
        "titulo": "CÉDULA 10",
        "preguntas": []
    },

    11: {
        "titulo": "CÉDULA 11",
        "preguntas": []
    },

    12: {
        "titulo": "CÉDULA 12",
        "preguntas": []
    },

    13: {
        "titulo": "CÉDULA 13",
        "preguntas": []
    },

    14: {
        "titulo": "CÉDULA 14",
        "preguntas": []
    }
}

# =====================================================
# ESTADO DE SESIÓN
# =====================================================

if "cedula" not in st.session_state:
    st.session_state.cedula = 1

if "pregunta_idx" not in st.session_state:
    st.session_state.pregunta_idx = 0

# =====================================================
# SELECCIÓN DE CÉDULA
# =====================================================

st.divider()
st.subheader("📚 Selección de Cédula")

cols = st.columns(5)

for idx, numero in enumerate(range(1, 15)):
    with cols[idx % 5]:
        if st.button(
            f"Cédula {numero}",
            use_container_width=True,
            key=f"cedula_{numero}"
        ):
            st.session_state.cedula = numero
            st.session_state.pregunta_idx = 0
            st.rerun()

# =====================================================
# CARGAR CÉDULA
# =====================================================

cedula = DATOS_EXAMEN.get(st.session_state.cedula)

if not cedula:
    st.error("No existe la cédula seleccionada.")
    st.stop()

if len(cedula["preguntas"]) == 0:
    st.warning(
        "⚠️ Esta cédula aún no tiene preguntas cargadas."
    )
    st.stop()

# =====================================================
# PREGUNTA ACTUAL
# =====================================================

indice = st.session_state.pregunta_idx
total = len(cedula["preguntas"])

pregunta = cedula["preguntas"][indice]

# =====================================================
# PROGRESO
# =====================================================

st.subheader(cedula["titulo"])

st.write(
    f"**Pregunta {indice + 1} de {total}**"
)

st.progress((indice + 1) / total)

st.markdown("---")

st.write(
    f"### {pregunta['sub']} - {pregunta['preg']}"
)

# =====================================================
# RESPUESTA MULTIPLE CHOICE
# =====================================================

respuesta = st.radio(
    "Seleccione una alternativa:",
    pregunta["opciones"],
    key=f"radio_{st.session_state.cedula}_{indice}"
)

# =====================================================
# RESPUESTA DESARROLLADA
# =====================================================

st.text_area(
    "Respuesta desarrollada (opcional):",
    height=120,
    key=f"texto_{st.session_state.cedula}_{indice}"
)

# =====================================================
# BOTÓN CORREGIR
# =====================================================

if st.button("✅ Corregir respuesta"):

    if respuesta == pregunta["correcta"]:
        st.success("Correcto.")
    else:
        st.error("Incorrecto.")

    st.info(
        f"Respuesta correcta:\n\n"
        f"{pregunta['correcta']}"
    )

    st.warning(
        f"Explicación:\n\n"
        f"{pregunta['explicacion']}"
    )

# =====================================================
# NAVEGACIÓN
# =====================================================

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "⬅️ Anterior",
        use_container_width=True
    ):
        if st.session_state.pregunta_idx > 0:
            st.session_state.pregunta_idx -= 1
            st.rerun()

with col2:
    if st.button(
        "➡️ Siguiente",
        use_container_width=True
    ):
        if st.session_state.pregunta_idx < total - 1:
            st.session_state.pregunta_idx += 1
            st.rerun()
