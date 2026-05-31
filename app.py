import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Evaluación Oral", layout="wide")

# 1. ESTILOS CSS REVISADOS (Para pintar las pestañas activas e inactivas)
# Nota: Forzamos la eliminación de los márgenes inferiores de botones fantasmas
st.markdown("""
<style>
    .titulo-panel { font-size: 24px; font-weight: bold; margin-bottom: 20px; }
    .cuadro-cedula { background-color: #E8F5E9; padding: 20px; border-radius: 5px; border-left: 5px solid #2E7D32; color: #1B5E20; font-size: 20px; font-weight: bold; margin-bottom: 20px;}
    .cuadro-pregunta { background-color: #ECEFF1; padding: 20px; border-radius: 5px; border-left: 5px solid #455A64; color: #263238; font-size: 18px; margin-top: 15px; }
    .cuadro-nota { background-color: #FFF3E0; padding: 25px; border-radius: 5px; border-left: 5px solid #FB8C00; font-size: 22px; text-align: center; }
    
    /* Forzar estilos personalizados a los botones superiores según su estado simulado */
    div.stButton > button.btn-activa {
        background-color: #FF5252 !important;
        color: white !important;
        border: 1px solid #FF5252 !important;
    }
    div.stButton > button.btn-inactiva {
        background-color: #F5F5F5 !important;
        color: #333333 !important;
        border: 1px solid #E0E0E0 !important;
    }
</style>
""", unsafe_allow_html=True)

# 2. BASE DE DATOS DE CÉDULAS Y SUBPREGUNTAS
DATOS_CEDULAS = {
    1: "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
    2: "CÉDULA 2.- Fuentes del Derecho y la Ley.",
    3: "CÉDULA 3.- Interpretación e Integración de la Ley.",
    4: "CÉDULA 4.- Efectos de la Ley en el Tiempo y el Espacio.",
    5: "CÉDULA 5.- Sujetos de Derecho y Personas Naturales."
}

SUBPREGUNTAS = {
    1: [
        {"enunciado": "¿Cuál es la principal sanción ante el incumplimiento de una norma jurídica?", "alternativas": ["A) El remordimiento de conciencia.", "B) La exclusión social del grupo.", "C) La coacción del Estado (sanción legal organizada)."], "correcta": 2}
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
        {
            "enunciado": "¿Cuándo comienza legalmente la personalidad de una persona natural según el Código Civil?",
            "alternativas": ["A) Al momento de la concepción.", "B) Al nacer, esto es, al separarse completamente de la madre y sobrevivir un momento siquiera.", "C) A los 18 años de edad."],
            "correcta": 1
        },
        {
            "enunciado": "La existencia natural de la persona humana comienza con:",
            "alternativas": ["A) El nacimiento.", "B) La inscripción en el Registro Civil.", "C) La concepción."],
            "correcta": 2
        }
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

# 4. CAPTURAR COMANDOS DIRECTOS DESDE JAVASCRIPT MEDIANTE QUERY PARAMS (Evita usar botones ocultos)
# El script JS actualizará la URL silenciosamente y Streamlit reaccionará inmediatamente
query_params = st.query_transform(st.experimental_get_query_params() if hasattr(st, 'experimental_get_query_params') else st.query_params)

if "accion" in query_params:
    accion = query_params["accion"]
    # Limpiar el parámetro de inmediato para que no se repita en el siguiente bucle
    if hasattr(st, 'experimental_set_query_params'):
        st.experimental_set_query_params()
    else:
        st.query_params.clear()
        
    # --- EJECUTAR ACCIONES DE TECLADO ---
    if accion == "espacio" and st.session_state.fase == "SELECCION_CEDULA":
        # Avanza de forma cíclica (1 -> 2 -> 3 -> 4 -> 5 -> 1)
        st.session_state.cedula_actual = 1 if st.session_state.cedula_actual == 5 else st.session_state.cedula_actual + 1
        
    elif accion == "backspace" and st.session_state.fase == "SELECCION_CEDULA":
        # Retrocede de forma cíclica (1 -> 5 -> 4 -> 3 -> 2 -> 1)
        st.session_state.cedula_actual = 5 if st.session_state.cedula_actual == 1 else st.session_state.cedula_actual - 1
        
    elif accion == "backspace" and st.session_state.fase == "SUBPREGUNTAS":
        if st.session_state.pregunta_index > 0:
            st.session_state.pregunta_index -= 1
        else:
            st.session_state.fase = "SELECCION_CEDULA"
            st.session_state.pregunta_index = 0
            
    elif accion == "enter":
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

# ANCLA OCULTA PARA PASARLE LA FASE ACTUAL A JAVASCRIPT
st.markdown(f'<div id="fase-app" data-fase="{st.session_state.fase}" style="display:none;"></div>', unsafe_allow_html=True)

# 5. INTERFAZ GRÁFICA CENTRAL
st.caption("Soporte Técnico: Método Cognuss II \nMiguel López Lavados")
st.markdown('<div class="titulo-panel">👨‍🏫 PANEL DIRECTO DE EVALUACIÓN ORAL (CÉDULAS 1 A 5)</div>', unsafe_allow_html=True)

# Fila superior de Cédulas limpia
cols_superiores = st.columns(5)
for i in range(1, 6):
    # Asignamos clases CSS personalizadas para asegurar que la activa se distinga perfectamente
    clase_css = "btn-activa" if st.session_state.cedula_actual == i else "btn-inactiva"
    cols_superiores[i-1].button(f"Cédula {i}", key=f"btn_top_{i}", type="secondary", use_container_width=True, help=None)
    # Inyectamos dinámicamente la clase al botón correspondiente
    st.markdown(f"<script>window.parent.document.querySelectorAll('button')[{i-1}].className += ' {clase_css}';</script>", unsafe_allow_html=True)

st.write("---")

# Cuadro de la Cédula Activa
contenido_cedula = DATOS_CEDULAS.get(st.session_state.cedula_actual, "Cédula no encontrada")
st.markdown(f'<div class="cuadro-cedula">📍 {contenido_cedula}</div>', unsafe_allow_html=True)

# 6. ZONA DE EVALUACIÓN DINÁMICA
if st.session_state.fase == "SUBPREGUNTAS":
    lista_preguntas = SUBPREGUNTAS.get(st.session_state.cedula_actual, [])
    idx = st.session_state.pregunta_index
    progreso = f"Pregunta {idx + 1} de {len(lista_preguntas)}"
    
    st.subheader(f"📝 Zona de Evaluación: {progreso}")
    
    pregunta_data = lista_preguntas[idx]
    st.markdown(f'<div class="cuadro-pregunta">❓ {pregunta_data["enunciado"]}</div>', unsafe_allow_html=True)
    st.write("")
    
    opcion_guardada = st.session_state.respuestas_alumno.get(idx, 0)
    
    seleccion = st.radio(
        "Selecciona la alternativa correcta:",
        options=range(len(pregunta_data["alternativas"])),
        format_func=lambda x: pregunta_data["alternativas"][x],
        index=opcion_guardada,
        key=f"radio_preg_{idx}"
    )
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

# 7. INYECCIÓN DE JAVASCRIPT ULTRA-LIMPIO (SIN BOTONES OCULTOS)
# El JavaScript modifica la URL agregando la acción de la tecla, lo que refresca el backend de Streamlit con la orden
st.components.v1.html(
    """
    <script>
    const doc = window.parent.document;
    
    if(window.parent._keyHandler) {
        doc.removeEventListener('keydown', window.parent._keyHandler);
    }

    window.parent._keyHandler = function(e) {
        const contenedorFase = doc.getElementById('fase-app');
        const faseActual = contenedorFase ? contenedorFase.getAttribute('data-fase') : "SELECCION_CEDULA";

        if (e.key === 'Backspace' || e.key === ' ' || e.key === 'Enter') {
            // Permitir que el Enter funcione nativamente si está cambiando el radio button
