import streamlit as st

st.set_page_config(page_title="EXAMINADOR DE TEORÍA DEL DERECHO", layout="centered")

st.markdown("<h1 style='text-align: center; color: #1E3A8A; margin-bottom: 0;'>EXAMINADOR DE TEORÍA DEL DERECHO</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #4B5563; font-weight: normal; margin-top: 0;'>Profesor Jaime Esponda</h3>", unsafe_allow_html=True)

with st.sidebar:
    st.write("")
    st.caption("---")
    st.caption("🛠️ **Soporte Técnico:**")
    st.caption("Método Cognuss II — Miguel López Lavados")

DATOS_EXAMEN = {
    1: {
        "titulo": "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
        "preguntas": [
            {"sub": "1.1", "preg": "¿Cuáles son las características principales de la norma moral?", "opciones": ["A) Autónoma, interior, unilateral e incoercible.", "B) Heterónoma, exterior, bilateral y coercible."], "correcta": "A) Autónoma, interior, unilateral e incoercible."},
            {"sub": "1.2", "preg": "Respecto a las diferencias entre Derecho y Moral, ¿cuál es CORRECTA?", "opciones": ["A) El Derecho es coercible mientras que la Moral es incoercible.", "B) El Derecho es unilateral y la Moral es bilateral."], "correcta": "A) El Derecho es coercible mientras que la Moral es incoercible."},
            {"sub": "1.3", "preg": "¿Cuál es el concepto y características de las normas de uso y trato social?", "opciones": ["A) Son pautas de decoro y cortesía, de carácter heterónomo, exterior y unilateral.", "B) Son mandatos jurídicos coercibles estatales."], "correcta": "A) Son pautas de decoro y cortesía, de carácter heterónomo, exterior y unilateral."}
        ]
    },
    2: {
        "titulo": "CÉDULA 2.- La Norma Jurídica. Características. Estructura lógica.",
        "preguntas": [
            {"sub": "2.1", "preg": "¿Cuáles son las características esenciales de la norma jurídica?", "opciones": ["A) Es heterónoma, exterior, bilateral y coercible.", "B) Es autónoma, interior e incoercible."], "correcta": "A) Es heterónoma, exterior, bilateral y coercible."},
            {"sub": "2.2", "preg": "¿Cómo operan las normas jurídicas imperativas frente a las permisivas?", "opciones": ["A) Las imperativas mandan o prohíben; las permisivas conceden una facultad o derecho.", "B) Ambas otorgan consejos opcionales de conducta."], "correcta": "A) Las imperativas mandan o prohíben; las permisivas conceden una facultad o derecho."}
        ]
    },
    3: {"titulo": "CÉDULA 3.- Vigencia, Validez y Eficacia de las Normas Jurídicas.", "preguntas": [{"sub": "3.1", "preg": "¿Qué define la vigencia y la derogación legal en Chile?", "opciones": ["A) Vigencia es la fuerza obligatoria tras la publicación. Derogación es la pérdida de esta.", "B) La vigencia comienza y termina solo por mutuo acuerdo."], "correcta": "A) Vigencia es la fuerza obligatoria tras la publicación. Derogación es la pérdida de esta."}]},
    4: {"titulo": "CÉDULA 4.- El Principio de Inexcusabilidad, Plenitud Hermética y Solución de Conflictos.", "preguntas": [{"sub": "4.1", "preg": "¿Qué consagra el Principio de Inexcusabilidad en el Art. 76 de la Constitución?", "opciones": ["A) Reclamada su intervención en forma legal, los tribunales no pueden excusarse de fallar ni aun por falta de ley.", "B) Los jueces pueden negarse si la ley no es clara."], "correcta": "A) Reclamada su intervención en forma legal, los tribunales no pueden excusarse de fallar ni aun por falta de ley."}]},
    5: {"titulo": "CÉDULA 5.- Las Fuentes del Derecho. Materiales y Formales.", "preguntas": [{"sub": "5.1", "preg": "¿Cuál es la diferencia entre Fuentes Materiales y Fuentes Formales del Derecho?", "opciones": ["A) Materiales son factores reales (sociales); Formales son los modos de manifestación (ley).", "B) Las materiales son libros jurídicos; las formales son discursos políticos."], "correcta": "A) Materiales son factores reales (sociales); Formales son los modos de manifestación (ley)."}]},
    6: {"titulo": "CÉDULA 6.- La Costumbre Jurídica.", "preguntas": [{"sub": "6.1", "preg": "¿Qué es la costumbre jurídica y cuáles son sus dos elementos constitutivos?", "opciones": ["A) Repetición de conductas con elemento Material (práctica) y Espiritual (Opinio Iuris).", "B) Modas pasajeras del comportamiento social."], "correcta": "A) Repetición de conductas con elemento Material (práctica) y Espiritual (Opinio Iuris)."}]}
}

for i in range(7, 15):
    DATOS_EXAMEN[i] = {"titulo": f"CÉDULA {i}.- (Pendiente de contenidos)", "preguntas": []}

if "cedula" not in st.session_state: st.session_state.cedula = None
if "respuestas_usuario" not in st.session_state: st.session_state.respuestas_usuario = {}
if "evaluado" not in st.session_state: st.session_state.evaluado = False

st.write("---")
st.write("### 👨‍🏫 SELECCIÓN DIRECTA DE CÉDULA EXAMINADORA")

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
        for p in datos_cedula["preguntas"]:
            st.markdown(f"#### Pregunta {p['sub']}: {p['preg']}")
            clave = f"p_{p['sub']}"
            st.session_state.respuestas_usuario[clave] = st.radio("Selecciona:", options=p["opciones"], key=clave, index=None)

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
            st.metric(label="⭐⭐ NOTA FINAL EXAMEN ⭐⭐", value=f"{nota}")
