import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Evaluación Oral", layout="wide")

# 1. ESTILOS CSS LIMPIOS (Sin botones basura que ocultar)
st.markdown("""
<style>
    .titulo-panel { font-size: 24px; font-weight: bold; margin-bottom: 20px; }
    .cuadro-cedula { background-color: #E8F5E9; padding: 20px; border-radius: 5px; border-left: 5px solid #2E7D32; color: #1B5E20; font-size: 20px; font-weight: bold; margin-bottom: 20px;}
    .cuadro-pregunta { background-color: #ECEFF1; padding: 20px; border-radius: 5px; border-left: 5px solid #455A64; color: #263238; font-size: 18px; margin-top: 15px; }
    .cuadro-nota { background-color: #FFF3E0; padding: 25px; border-radius: 5px; border-left: 5px solid #FB8C00; font-size: 22px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# 2. BASE DE DATOS DE CÉDULAS Y SUBPREGUNTAS CHILENAS REALES
DATOS_CEDULAS = {
    1: "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
    2: "CÉDULA 2.- Fuentes del Derecho y la Ley.",
    3: "CÉDULA 3.- Interpretación e Integración de la Ley.",
    4: "CÉDULA 4.- Efectos de la Ley en el Tiempo y el Espacio.",
    5: "CÉDULA 5.- Sujetos de Derecho y Personas Naturales."
}

SUBPREGUNTAS = {
    1: [
        {"enunciado": "¿Cuál es la principal sanción ante el incumplimiento de una norma jurídica?", "alternativas": ["A) El remordimiento de conciencia.", "B) La exclusión social del grupo.", "C) La coacción del Estado (sanción legal organizada)."], "correcta": 2},
        {"enunciado": "Las normas de uso y trato social se caracterizan por ser:", "alternativas": ["A) Unilaterales y de incoercibilidad.", "B) Bilaterales y exigibles judicialmente.", "C) Dictadas por el Congreso Nacional."], "correcta": 0}
    ],
    2: [
        {"enunciado": "¿Qué tipo de fuente del derecho corresponde a la jurisprudencia?", "alternativas": ["A) Fuente formal material.", "B) Fuente formal indirecta.", "C) Fuente histórica."], "correcta": 1}
    ],
    3: [
        {"enunciado": "La interpretación de la ley realizada por el legislador se denomina:", "alternativas": ["A) Interpretación doctrinal.", "B) Interpretación auténtica o legal.", "C) Interpretación judicial."], "correcta": 1}
    ],
    4: [
        {"enunciado": "Por regla general, las leyes en Chile comienzan a regir desde:", "alternativas": ["A) Su aprobación en el Congreso.", "B) Su publicación en el Diario Oficial.", "C) Su firma por el Presidente."], "correcta": 1}
    ],
    5: [
        {"enunciado": "¿Cuándo comienza legalmente la personalidad de una persona natural según el Código Civil?", "alternativas": ["A) Al momento de la concepción.", "B) Al nacer, esto es, al separarse completamente de la madre y sobrevivir un momento siquiera.", "C) A los 18 años de edad."], "correcta": 1},
        {"enunciado": "La existencia natural de la persona humana comienza con:", "alternativas": ["A) El nacimiento.", "B) La inscripción en el Registro Civil.", "C) La concepción."], "correcta": 2}
    ]
}

# 3. INICIALIZAR ESTADOS DE LA APLICACIÓN
if "cedula_actual" not in st.session_state:
    st.session_state.cedula_actual = 1
if "fase" not in st.session_state:
    st.session_state.fase = "SELECCION_CEDULA"
if "pregunta_index" not in st.session_state:
    st.session_state.pregunta_index = 0
if "respuestas_alumno" not in st.session_state:
    st.session_state.respuestas_alumno = {}

# 4. RECEPTOR DE COMANDOS DE TECLADO DESDE EL COMPONENTE WEB JS
# Recibe las pulsaciones de teclas guardadas en la URL de forma totalmente transparente
query_params = st.query_params
if "tecla" in query_params:
    tecla_pulsada = query_params["tecla"]
    st.query_params.clear() # Limpiar la cola inmediatamente para que no se duplique el comando
    
    # Lógica de navegación pura en Python (Sin clics fantasmas)
    if tecla_pulsada == "backspace":
        if st.session_state.fase == "SELECCION_CEDULA":
            st.session_state.cedula_actual = 5 if st.session_state.cedula_actual == 1 else st.session_state.cedula_actual - 1
        elif st.session_state.fase == "SUBPREGUNTAS":
            if st.session_state.pregunta_index > 0:
                st.session_state.pregunta_index -= 1
            else:
                st.session_state.fase = "SELECCION_CEDULA"
                st.session_state.pregunta_index = 0
                
    elif tecla_pulsada == "espacio" and st.session_state.fase == "SELECCION_CEDULA":
        st.session_state.cedula_actual = 1 if st.session_state.cedula_actual == 5 else st.session_state.cedula_actual + 1
        
    elif tecla_pulsada == "enter":
        if st.session_state.fase == "SELECCION_CEDULA":
            st.session_state.fase = "SUBPREGUNTAS"
            st.session_state.pregunta_index = 0
            st.session_state.respuestas_alumno = {}
        elif st.session_state.fase == "SUBPREGUNTAS":
            preguntas_disponibles = SUBPREGUNTAS.get(st.session_state.cedula_actual, [])
            if st.session_state.pregunta_index < len(preguntas_disponibles) - 1:
                st.session_state.pregunta_index += 1
            else:
                st.session_state.fase = "EVALUACION_TERMINADA"

# Pasar la fase actual de la App a una etiqueta HTML oculta leída por JS
st.markdown(f'<div id="estado-fase" data-fase="{st.session_state.fase}" style="display:none;"></div>', unsafe_allow_html=True)


# 5. INTERFAZ GRÁFICA SUPERIOR
st.caption("Soporte Técnico: Método Cognuss II \nMiguel López Lavados")
st.markdown('<div class="titulo-panel">👨‍🏫 PANEL DIRECTO DE EVALUACIÓN ORAL (CÉDULAS 1 A 5)</div>', unsafe_allow_html=True)

# Pestañas de Cédulas superiores
cols_superiores = st.columns(5)
for i in range(1, 6):
    tipo_boton = "primary" if st.session_state.cedula_actual == i else "secondary"
    if cols_superiores[i-1].button(f"Cédula {i}", key=f"btn_top_{i}", type=tipo_boton, use_container_width=True):
        st.session_state.cedula_actual = i
        st.session_state.fase = "SELECCION_CEDULA"

st.write("---")

# Cuadro descriptivo de la Cédula activa
contenido_cedula = DATOS_CEDULAS.get(st.session_state.cedula_actual, "Cédula no encontrada")
st.markdown(f'<div class="cuadro-cedula">📍 {contenido_cedula}</div>', unsafe_allow_html=True)


# 6. MÓDULOS DE RENDERIZADO DE EVALUACIÓN
if st.session_state.fase == "SUBPREGUNTAS":
    lista_preguntas = SUBPREGUNTAS.get(st.session_state.cedula_actual, [])
    idx = st.session_state.pregunta_index
    progreso = f"Pregunta {idx + 1} de {len(lista_preguntas)}"
    
    st.subheader(f"📝 Zona de Evaluación: {progreso}")
    
    pregunta_data = lista_preguntas[idx]
    st.markdown(f'<div class="cuadro-pregunta">❓ {pregunta_data["enunciado"]}</div>', unsafe_allow_html=True)
    st.write("")
    
    # Recuperar índice si ya respondió antes
    opcion_guardada = st.session_state.respuestas_alumno.get(idx, None)
    
    seleccion = st.radio(
        "Selecciona la alternativa correcta:",
        options=range(len(pregunta_data["alternativas"])),
        format_func=lambda x: pregunta_data["alternativas"][x],
        index=opcion_guardada,
        key=f"radio_actual_{st.session_state.cedula_actual}_{idx}"
    )
    # Guardar en memoria inmediatamente al cambiar de opción
    st.session_state.respuestas_alumno[idx] = seleccion

elif st.session_state.fase == "EVALUACION_TERMINADA":
    st.markdown('<div class="cuadro-nota">📊 EVALUACIÓN FINALIZADA</div>', unsafe_allow_html=True)
    
    lista_preguntas = SUBPREGUNTAS.get(st.session_state.cedula_actual, [])
    buenas = 0
    for idx, preg in enumerate(lista_preguntas):
        ans_alumno = st.session_state.respuestas_alumno.get(idx, None)
        if ans_alumno == preg["correcta"]:
            buenas += 1
            
    total_p = len(lista_preguntas)
    malas = total_p - buenas
    
    # Fórmula de nota estándar chilena al 60% de exigencia
    if total_p > 0:
        porcentaje = buenas / total_p
        if porcentaje >= 0.6:
            nota = 4.0 + (porcentaje - 0.6) * (3.0 / 0.4)
        else:
            nota = 1.0 + porcentaje * (3.0 / 0.6)
    else:
        nota = 1.0

    c1, c2, c3 = st.columns(3)
    c1.metric("Preguntas Correctas", f"✅ {buenas}")
    c2.metric("Preguntas Incorrectas", f"❌ {malas}")
    c3.metric("Nota Obtenida", f"🎓 {nota:.1f}")
    
    if st.button("Reiniciar Cédula / Volver", type="primary"):
        st.session_state.fase = "SELECCION_CEDULA"
        st.session_state.pregunta_index = 0
        st.session_state.respuestas_alumno = {}


# 7. INYECCIÓN DE CAPTURA DE TECLADO INLINE DIRECTO (Cero fallos de sintaxis)
# Se encarga de capturar las teclas y notificarlas directo a la URL de forma asíncrona
js_captura_limpia = (
    '<script>'
    'const doc = window.parent.document;'
    'if(window.parent._keyHandler) { doc.removeEventListener("keydown", window.parent._keyHandler); }'
    'window.parent._keyHandler = function(e) {'
    '  const elFase = doc.getElementById("estado-fase");'
    '  const faseActual = elFase ? elFase.getAttribute("data-fase") : "SELECCION_CEDULA";'
    '  if (e.key === "Backspace" || e.key === " " || e.key === "Enter") {'
    '    if (doc.activeElement && doc.activeElement.type === "radio" && e.key !== "Enter") { return; }'
    '    e.preventDefault();'
    '    let comando = "";'
    '    if (e.key === "Backspace") { comando = "backspace"; }'
    '    else if (e.key === " " && faseActual === "SELECCION_CEDULA") { comando = "espacio"; }'
    '    else if (e.key === "Enter") { comando = "enter"; }'
    '    if (comando !== "") {'
    '      const url = new URL(window.parent.location.href);'
    '      url.searchParams.set("tecla", comando);'
    '      window.parent.history.replaceState({}, "", url.toString());'
    '      const btnRefresh = doc.querySelector(".stActionButton");'
    '      if (btnRefresh) { btnRefresh.click(); }'
    '      else { window.parent.location.reload(); }'
    '    }'
    '  }'
    '};'
    'doc.addEventListener("keydown", window.parent._keyHandler);'
    '</script>'
)

