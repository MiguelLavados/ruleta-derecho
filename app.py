            {
                "sub": "5.1", "preg": "¿Cuál es la diferencia entre Fuentes Materiales y Fuentes Formales?",
                "opciones": ["A) Materiales son factores reales; Formales son los modos de manifestación.", "B) Las materiales son los libros; las formales son discursos."],
                "correcta": "A) Materiales son factores reales; Formales son los modos de manifestación.",
                "explicacion": "Materiales son la causa social/política; formales son las leyes obligatorias."
            }
        ]
    },
    6: {
        "titulo": "CÉDULA 6.- La Costumbre Jurídica.",
        "preguntas": [
            {
                "sub": "6.1", "preg": "¿Qué es la costumbre jurídica y sus elementos?",
                "opciones": ["A) Repetición de conductas. Elementos: Material y Espiritual.", "B) Modas pasajeras sin valor normativo."],
                "correcta": "A) Repetición de conductas. Elementos: Material y Espiritual.",
                "explicacion": "Requiere uso generalizado en el tiempo y convicción de obligatoriedad."
            }
        ]
    }
}

# Cédulas del 7 al 14 vacías por ahora
for i in range(7, 15):
    DATOS_EXAMEN[i] = {"titulo": f"CÉDULA {i}.- (Pendiente de contenidos)", "preguntas": []}

if "cedula" not in st.session_state: st.session_state.cedula = None
if "respuestas_usuario" not in st.session_state: st.session_state.respuestas_usuario = {}
if "evaluado" not in st.session_state: st.session_state.evaluado = False

st.write("---")
st.write("### 👨‍🏫 SELECCIÓN DIRECTA DE CÉDULA")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("Cédula 1", use_container_width=True): st.session_state.cedula = 1; st.session_state.evaluado = False; st.session_state.respuestas_usuario = {}
    if st.button("Cédula 6", use_container_width=True): st.session_state.cedula = 6; st.session_state.evaluado = False; st.session_state.respuestas_usuario = {}
    if st.button("Cédula 11", use_container_width=True): st.session_state.cedula = 11; st.session_state.evaluado = False; st.session_state.respuestas_usuario = {}
with col2:
    if st.button("Cédula 2", use_container_width=True): st.session_state.cedula = 2; st.session_state.evaluado = False; st.session_state.respuestas_usuario = {}
    if st.button("Cédula 7", use_container_width=True): st.session_state.cedula = 7; st.session_state.evaluado = False; st.session_state.respuestas_usuario = {}
    if st.button("Cédula 12", use_container_width=True): st.session_state.cedula = 12; st.session_state.evaluado = False; st.session_state.respuestas_usuario = {}
with col3:
    if st.button("Cédula 3", use_container_width=True): st.session_state.cedula = 3; st.session_state.evaluado = False; st.session_state.respuestas_usuario = {}
    if st.button("Cédula 8", use_container_width=True): st.session_state.cedula = 8; st.session_state.evaluado = False; st.session_state.respuestas_usuario = {}
    if st.button("Cédula 13", use_container_width=True): st.session_state.cedula = 13; st.session_state.evaluado = False; st.session_state.respuestas_usuario = {}
with col4:
    if st.button("Cédula 4", use_container_width=True): st.session_state.cedula = 4; st.session_state.evaluado = False; st.session_state.respuestas_usuario = {}
    if st.button("Cédula 9", use_container_width=True): st.session_state.cedula = 9; st.session_state.evaluado = False; st.session_state.respuestas_usuario = {}
    if st.button("Cédula 14", use_container_width=True): st.session_state.cedula = 14; st.session_state.evaluado = False; st.session_state.respuestas_usuario = {}
with col5:
    if st.button("Cédula 5", use_container_width=True): st.session_state.cedula = 5; st.session_state.evaluado = False; st.session_state.respuestas_usuario = {}
    if st.button("Cédula 10", use_container_width=True): st.session_state.cedula = 10; st.session_state.evaluado = False; st.session_state.respuestas_usuario = {}

st.write("---")

if st.session_state.cedula:
    datos_cedula = DATOS_EXAMEN[st.session_state.cedula]
    st.success(f"### 📍 {datos_cedula['titulo']}")
    
    if not datos_cedula["preguntas"]:
        st.info("Esta cédula está esperando contenido.")
    else:
        for idx, p in enumerate(datos_cedula["preguntas"]):
            st.markdown(f"#### Pregunta {p['sub']}: {p['preg']}")
            clave_pregunta = f"p_{p['sub']}"
            st.session_state.respuestas_usuario[clave_pregunta] = st.radio("Selecciona:", options=p["opciones"], key=clave_pregunta, index=None)

        if not st.session_state.evaluado:
            if st.button("📝 EVALUAR EXAMEN", type="primary", use_container_width=True):
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
