import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Evaluación Oral", layout="wide")

# Estilos visuales adaptados
st.markdown("""
<style>
    .titulo-panel { font-size: 24px; font-weight: bold; margin-bottom: 20px; }
    .cuadro-cedula { background-color: #E8F5E9; padding: 20px; border-radius: 5px; border-left: 5px solid #2E7D32; color: #1B5E20; font-size: 20px; font-weight: bold; margin-bottom: 20px;}
    .cuadro-pregunta { background-color: #ECEFF1; padding: 20px; border-radius: 5px; border-left: 5px solid #455A64; color: #263238; font-size: 18px; margin-top: 15px; }
    .opcion-seleccionada { background-color: #E3F2FD; padding: 10px; border-radius: 5px; border: 1px solid #1E88E5; font-weight: bold; color: #0D47A1; }
    .opcion-normal { padding: 10px; color: #333; }
    .cuadro-nota { background-color: #FFF3E0; padding: 25px; border-radius: 5px; border-left: 5px solid #FB8C00; font-size: 22px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# 1. BASE DE DATOS DE CÉDULAS Y SUBPREGUNTAS
DATOS_CEDULAS = {
    1: "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
    2: "CÉDULA 2.- Fuentes del Derecho y la Ley.",
    3: "CÉDULA 3.- Interpretación e Integración de la Ley.",
    4: "CÉDULA 4.- Efectos de la Ley en el Tiempo y el Espacio.",
    5: "CÉDULA 5.- Sujetos de Derecho y Personas Naturales."
}

# Subpreguntas por cada cédula (Cada una con alternativas y el índice de la respuesta correcta)
SUBPREGUNTAS = {
    5: [
        {
            "enunciado": "¿Cuándo comienza legalmente la personalidad de una persona natural según el Código Civil?",
            "alternativas": ["A) Al momento de la concepción.", "B) Al nacer, esto es, al separarse completamente de la madre y sobrevivir un momento siquiera.", "C) A los 18 años de edad."],
            "correcta": 1 # Corresponde a la opción B
        },
        {
            "enunciado": "La existencia natural de la persona humana comienza con:",
            "alternativas": ["A) El nacimiento.", "B) La inscripción en el Registro Civil.", "C) La concepción."],
            "correcta": 2 # Corresponde a la opción C
        }
    ]
}

# 2. INICIALIZAR ESTADOS DE LA APLICACIÓN
if "cedula_actual" not in st.session_state:
    st.session_state.cedula_actual = 1
if "fase" not in st.session_state:
    st.session_state.fase = "SELECCION_CEDULA"  # Estados: SELECCION_CEDULA, SUBPREGUNTAS, EVALUACION_TERMINADA
if "pregunta_index" not in st.session_state:
    st.session_state.pregunta_index = 0
if "respuestas_alumno" not in st.session_state:
    st.session_state.respuestas_alumno = {} # Guardará {indice_pregunta: opcion_seleccionada}

# 3. FUNCIONES DE LOGICA DE NAVEGACIÓN (Llamadas por botones invisibles)
def js_accion_siguiente():
    if st.session_state.fase == "SELECCION_CEDULA":
        if st.session_state.cedula_actual < 5:
            st.session_state.cedula_actual += 1
            
    elif st.session_state.fase == "SUBPREGUNTAS":
        preguntas_disponibles = SUBPREGUNTAS.get(st.session_state.cedula_actual, [])
        # Avanzar a la siguiente pregunta si quedan
        if st.session_state.pregunta_index < len(preguntas_disponibles) - 1:
            st.session_state.pregunta_index += 1
        else:
            # Si no quedan más preguntas, pasa a la pantalla de evaluación de nota
            st.session_state.fase = "EVALUACION_TERMINADA"

def js_accion_anterior():
    if st.session_state.fase == "SELECCION_CEDULA":
        if st.session_state.cedula_actual > 1:
            st.session_state.cedula_actual -= 1
            
    elif st.session_state.fase == "SUBPREGUNTAS":
        if st.session_state.pregunta_index > 0:
            st.session_state.pregunta_index -= 1
        else:
            # Si retrocede en la primera pregunta, vuelve a la selección de Cédula
            st.session_state.fase = "SELECCION_CEDULA"
            st.session_state.pregunta_index = 0

def js_accion_enter_cedula():
    # Solo actúa si está en modo selección de cédula para entrar a dar el examen
    if st.session_state.fase == "SELECCION_CEDULA":
        preguntas_disponibles = SUBPREGUNTAS.get(st.session_state.cedula_actual, [])
        if preguntas_disponibles:
            st.session_state.fase = "SUBPREGUNTAS"
            st.session_state.pregunta_index = 0
            st.session_state.respuestas_alumno = {} # Limpiar respuestas anteriores

# 4. INTERFAZ GRÁFICA (ZONA VISUAL)
st.caption("Soporte Técnico: Método Cognuss II \nMiguel López Lavados")
st.markdown('<div class="titulo-panel">👨‍🏫 PANEL DIRECTO DE EVALUACIÓN ORAL (CÉDULAS 1 A 5)</div>', unsafe_allow_html=True)

# Fila de botones superiores de las Cédulas
cols_superiores = st.columns(5)
for i in range(1, 6):
    tipo_boton = "primary" if st.session_state.cedula_actual == i else "secondary"
    if cols_superiores[i-1].button(f"Cédula {i}", key=f"btn_top_{i}", type=tipo_boton, use_container_width=True):
        st.session_state.cedula_actual = i
        st.session_state.fase = "SELECCION_CEDULA"

st.write("---")

# Mostrar cuadro de la Cédula Activa
contenido_cedula = DATOS_CEDULAS.get(st.session_state.cedula_actual, "Cédula no encontrada")
st.markdown(f'<div class="cuadro-cedula">📍 {contenido_cedula}</div>', unsafe_allow_html=True)


# 5. RENDERIZADO DINÁMICO SEGÚN LA FASE ACTUAL
if st.session_state.fase == "SUBPREGUNTAS":
    lista_preguntas = SUBPREGUNTAS.get(st.session_state.cedula_actual, [])
    idx = st.session_state.pregunta_index
    progreso = f"Pregunta {idx + 1} de {len(lista_preguntas)}"
    
    st.subheader(f"📝 Zona de Evaluación: {progreso}")
    
    # Mostrar enunciado de la subpregunta
    pregunta_data = lista_preguntas[idx]
    st.markdown(f'<div class="cuadro-pregunta">❓ {pregunta_data["enunciado"]}</div>', unsafe_allow_html=True)
    st.write("")
    
    # Mostrar alternativas interactivas usando un radio nativo de Streamlit
    # El alumno puede usar las flechas del teclado arriba/abajo para cambiar la opción y ENTER para validar
    opcion_guardada = st.session_state.respuestas_alumno.get(idx, 0)
    
    seleccion = st.radio(
        "Selecciona la alternativa correcta:",
        options=range(len(pregunta_data["alternativas"])),
        format_func=lambda x: pregunta_data["alternativas"][x],
        index=opcion_guardada,
        key=f"radio_preg_{idx}"
    )
    # Guardar selección de manera inmediata en el estado
    st.session_state.respuestas_alumno[idx] = seleccion


elif st.session_state.fase == "EVALUACION_TERMINADA":
    st.markdown('<div class="cuadro-nota">📊 EVALUACIÓN FINALIZADA</div>', unsafe_allow_html=True)
    
    lista_preguntas = SUBPREGUNTAS.get(st.session_state.cedula_actual, [])
    buenas = 0
    malas = 0
    
    # Procesar cálculo de buenas y malas
    for idx, preg in enumerate(lista_preguntas):
        ans_alumno = st.session_state.respuestas_alumno.get(idx, None)
        if ans_alumno == preg["correcta"]:
            buenas += 1
        else:
            malas += 1
            
    total_p = len(lista_preguntas)
    
    # Cálculo de nota Chilena estándar (Escala de 1.0 a 7.0 con exigencia al 60%)
    if total_p > 0:
        porcentaje = buenas / total_p
        if porcentaje >= 0.6:
            nota = 4.0 + (porcentaje - 0.6) * (3.0 / 0.4)
        else:
            nota = 1.0 + porcentaje * (3.0 / 0.6)
    else:
        nota = 1.0

    # Despliegue de métricas finales limpias
    c1, c2, c3 = st.columns(3)
    c1.metric("Preguntas Correctas", f"✅ {buenas}")
    c2.metric("Preguntas Incorrectas", f"❌ {malas}")
    c3.metric("Nota Obtenida", f"🎓 {nota:.1f}")
    
    if st.button("Reiniciar Cédula / Volver", type="primary"):
        st.session_state.fase = "SELECCION_CEDULA"
        st.session_state.pregunta_index = 0
        st.session_state.respuestas_alumno = {}


# 6. BOTONES INVISIBLES PARA ENLAZAR EL JAVASCRIPT
# Creamos un contenedor oculto para que no arruine el diseño visual
with st.container():
    st.markdown("""<style> div[key="btn_js_ant"] button, div[key="btn_js_sig"] button, div[key="btn_js_ent"] button { display: none !important; } </style>""", unsafe_allow_html=True)
    st.button("InvisibleAnt", key="btn_js_ant", on_click=js_accion_anterior)
    st.button("InvisibleSig", key="btn_js_sig", on_click=js_accion_siguiente)
    st.button("InvisibleEnt", key="btn_js_ent", on_click=js_accion_enter_cedula)


# 7. INYECCIÓN REVISADA DE JAVASCRIPT DE CAPTURA GLOBAL
st.components.v1.html(
    """
    <script>
    const doc = window.parent.document;
    doc.addEventListener('keydown', function(e) {
        // Capturar elementos ocultos creados por Streamlit por su texto interno
        const botones = Array.from(doc.querySelectorAll('button'));
        const btnAnt = botones.find(b => b.innerText.includes('InvisibleAnt'));
        const btnSig = botones.find(b => b.innerText.includes('InvisibleSig'));
        const btnEnt = botones.find(b => b.innerText.includes('InvisibleEnt'));

        // Prevenir comportamientos nativos molestos del navegador
        if (e.key === 'Backspace' || e.key === ' ' || e.key === 'Enter') {
            // Permitir que Enter y flechas funcionen con normalidad si el foco está dentro de las opciones (Radio)
            if(doc.activeElement.type === 'radio' && e.key === 'Enter') {
               // Dejar pasar para que registre el cambio interno
            } else {
               e.preventDefault();
            }
        }

        // CONTROL DE EVENTOS SEGÚN EN QUÉ ESCENARIO SE ENCUENTRA LA APP
        if (e.key === 'Backspace' && btnAnt) {
            btnAnt.click();
        } 
        else if (e.key === ' ' && btnSig) {
            btnSig.click();
        } 
        else if (e.key === 'Enter') {
            // El primer Enter ingresará a las subpreguntas; los siguientes irán avanzando
            if (btnEnt) btnEnt.click();
            if (btnSig) btnSig.click();
        }
    });
    </script>
    """,
    height=0,
)
