import streamlit as st
import random
import time
from datetime import datetime
import streamlit.components.v1 as components

# Control de caducidad requerido (30 de Junio de 2026)
FECHA_LIMITE = datetime(2026, 6, 30, 23, 59, 59)
if datetime.now() > FECHA_LIMITE:
    st.error("❌ LA LICENCIA DE ESTA APLICACIÓN HA CADUCADO. CONTACTE AL ADMINISTRADOR.")
    st.stop()

st.set_page_config(page_title="MÉTODO COGNUSS 2 - Reloj del Conocimiento", layout="wide")

# Estilos CSS institucionales y animaciones de desvanecimiento
st.markdown(
    """
    <style>
    .stApp { background-color: #FFFFFF; color: #0B1E36; font-family: Arial, sans-serif; }
    .header-banner { background-color: #0B1E36; color: #FFFFFF; padding: 18px; border-radius: 8px; text-align: center; margin-bottom: 20px; }
    .box-minutero { background-color: #E8F0FE; border-left: 5px solid #1A73E8; padding: 15px; border-radius: 4px; margin-bottom: 12px; font-size:15px; }
    .box-horario { background-color: #F3E5F5; border-left: 5px solid #7B1FA2; padding: 15px; border-radius: 4px; margin-bottom: 12px; font-size:15px; }
    .box-segundero { background-color: #E8F5E9; border-left: 5px solid #2E7D32; padding: 15px; border-radius: 4px; margin-bottom: 12px; font-size:15px; }
    
    .desvanecer-respuesta {
        animation: fadeOutEffect 35s forwards;
        font-weight: bold;
        color: #2E7D32;
    }
    @keyframes fadeOutEffect {
        0% { opacity: 1; }
        90% { opacity: 0.1; }
        100% { opacity: 0; display: none; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Base de datos basada exactamente en el Cedulario USS
CEDULARIO_COMPLETO = {
    1: {
        "titulo": "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
        "subpreguntas": [
            {"id": "1.1", "texto": "Explique las características principales de la norma moral.", "correcta": "Es unilateral, interior, incoercible y autónoma.", "distractores": ["Es bilateral, exterior, coercible y heterónoma.", "Es coercible, bilateral, interior y heterónoma.", "Es unilateral, exterior, coercible y autónoma."]},
            {"id": "1.2", "texto": "Detalle las diferencias fundamentales entre el orden del Derecho y el orden de la Moral.", "correcta": "El Derecho es bilateral y coercible; la Moral es unilateral e incoercible.", "distractores": ["El Derecho es puramente interior; la Moral regula la coacción del Estado.", "El Derecho es unilateral; la Moral posee plena fuerza coercitiva estatal.", "No existen diferencias estructurales ni de coercibilidad entre ambos."]},
            {"id": "1.3", "texto": "Defina el concepto de normas de uso y trato social, sus características y diferencias con la norma jurídica.", "correcta": "Son prescripciones de conducta social, exteriores, incoercibles y heterónomas. Carecen de coacción estatal.", "distractores": ["Son normas escritas dictadas por los tribunales de justicia chilenos.", "Tienen exactamente la misma estructura obligatoria y punitiva que una ley civil.", "Son mandatos interiores, autónomos e impuestos por el propio individuo."]}
        ]
    },
    2: {
        "titulo": "CÉDULA 2.- La norma jurídica.",
        "subpreguntas": [
            {"id": "2.1", "texto": "Mencione y explique las características esenciales de la norma jurídica.", "correcta": "Es bilateral, exterior, coercible y heterónoma.", "distractores": ["Es unilateral, interior, incoercible y autónoma.", "Es autónoma, puramente interior, obligatoria y coercible.", "Es unilateral, exterior, coercible y autónoma."]},
            {"id": "2.2", "texto": "Explique la clasificación entre normas jurídicas imperativas y permisivas.", "correcta": "Las imperativas ordenan o prohíben de forma absoluta; las permisivas conceden una facultad o derecho.", "distractores": ["Las imperativas otorgan consejos morales; las permisivas obligan a pagar multas.", "Ambas categorías carecen de fuerza legal formal dentro de Chile.", "Las imperativas permiten la renuncia libre; las permisivas imponen sanciones de cárcel."]},
            {"id": "2.3", "texto": "Describa la estructura lógica interna de una norma jurídica ordinaria.", "correcta": "Se compone de un supuesto de hecho (condición) y una consecuencia jurídica (sanción o efecto).", "distractores": ["Se compone únicamente de un preámbulo histórico y una sugerencia moral.", "Consiste en un mandato unilateral dictado sin condiciones previas.", "Está formada solo por principios generales intangibles sin sanción asociada."]}
        ]
    },
    3: {
        "titulo": "CÉDULA 3.- Vigencia, validez y eficacia del Derecho positivo.",
        "subpreguntas": [
            {"id": "3.1", "texto": "Defina vigencia, su momento de inicio y la clasificación de la derogación de la ley.", "correcta": "Fuerza obligatoria tras su publicación. Puede ser expresa o tácita, total o parcial.", "distractores": ["Es el desuso prolongado de la norma legal por razones de justicia.", "Es la conformidad valórica con los derechos humanos universales.", "Es el período de discusión parlamentaria previo a la aprobación de la ley."]},
            {"id": "3.2", "texto": "Explique el concepto de validez y los fundamentos de legitimidad de las dos principales doctrinas jurídicas.", "correcta": "Conformidad con normas superiores. Iusnaturalismo (justicia/moral) e Iuspositivismo (forma/órganos estatales).", "distractores": ["Validez comercial. Iusnaturalismo (leyes físicas) e Iuspositivismo (acuerdos privados).", "Es el desuso de la ley. Doctrinas contractuales y sociológicas del conflicto.", "La obligatoriedad derivada del plebiscito popular directo exclusivamente."]},
            {"id": "3.3", "texto": "Explique el concepto técnico de eficacia dentro del Derecho positivo.", "correcta": "Es el grado efectivo de cumplimiento y aplicación real de la norma por sus destinatarios y tribunales.", "distractores": ["Es la firma del Presidente de la República que ratifica el texto.", "Es el proceso técnico de redacción lingüística sin errores sintácticos.", "Es la velocidad con la que el Congreso aprueba un proyecto urgente."]}
        ]
    },
    4: {
        "titulo": "CÉDULA 4.- La plenitud hermética del ordenamiento jurídico y las lagunas del Derecho.",
        "subpreguntas": [
            {"id": "4.1", "texto": "Explique el Principio de Inexcusabilidad desde su perspectiva constitucional.", "correcta": "Consagrado en el Art. 76 CPR: obliga a los jueces a resolver prestigiosos litigios aun a falta de ley expresa.", "distractores": ["Permite a los jueces excusarse de fallar si el caso carece de regulación.", "Obliga al Congreso a redactar leyes exprés en menos de 30 días.", "Faculta a las partes a anular el juicio si no encuentran un artículo exacto."]},
            {"id": "4.2", "texto": "Defina el concepto de plenitud hermética del ordenamiento jurídico.", "correcta": "Postulado doctrinal que afirma que el sistema jurídico contiene soluciones para todo conflicto social.", "distractores": ["Es el secreto absoluto bajo el cual se mantienen las deliberaciones judiciales.", "Significa que las leyes nunca pueden ser modificadas ni derogadas por el poder legislativo.", "Norma que prohíbe la entrada de influencias o tratados de derecho internacional."]},
            {"id": "4.3", "texto": "Identifique en qué casos se observan lagunas del Derecho y cuál es su solución judicial.", "correcta": "Vacíos legales por omisión técnica. El juez integra usando analogía, equidad y principios generales.", "distractores": ["Falta de presupuesto judicial. Se soluciona mediante decretos de emergencia.", "Contradicción total entre dos códigos. Se soluciona archivando la causa sin dictar fallo.", "Omisión de firmas en el diario oficial. Se soluciona republicando el texto."]}
        ]
    }
}

# Inicialización de estados de Streamlit
if "posiciones_reloj" not in st.session_state:
    st.session_state.posiciones_reloj = list(CEDULARIO_COMPLETO.keys())
if "cedula_activa" not in st.session_state:
    st.session_state.cedula_activa = None
if "subpregunta_index" not in st.session_state:
    st.session_state.subpregunta_index = 0
if "respuestas_correctas" not in st.session_state:
    st.session_state.respuestas_correctas = 0
if "total_respondidas" not in st.session_state:
    st.session_state.total_respondidas = 0
if "modalidad" not in st.session_state:
    st.session_state.modalidad = None
if "alternativas_mezcladas" not in st.session_state:
    st.session_state.alternativas_mezcladas = []

# Cabecera
st.markdown(
    """
    <div class='header-banner'>
        <h1>MÉTODO COGNUSS 2: EL RELOJ JURÍDICO DEL CONOCIMIENTO</h1>
        <h3>EXAMEN DE INTRODUCCIÓN AL DERECHO — UNIVERSIDAD SAN SEBASTIÁN</h3>
    </div>
    """, unsafe_allow_html=True
)

col_izq, col_der = st.columns([1.1, 1])

with col_izq:
    st.subheader("🎡 Esfera Mecánica del Reloj")
    
    # JavaScript y Canvas HTML5 completamente depurados para dibujar el círculo al cargar
    canvas_html = """
    <div style="text-align:center;">
        <canvas id="canvas_clock" width="340" height="340" style="background:#FFFFFF; border-radius:50%; box-shadow: 0 4px 10px rgba(0,0,0,0.15);"></canvas><br>
        <button id="btn_spin" style="background-color:#0B1E36; color:white; border:none; padding:12px 20px; font-weight:bold; border-radius:6px; font-size:15px; cursor:pointer; width:85%; margin-top:15px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">=== ACCIONAR GIRO MECÁNICO ===</button>
    </div>
    <script>
        const canvas = document.getElementById('canvas_clock');
        const ctx = canvas.getContext('2d');
        const totalHours = 14;
        const r = 140;
        let angleOffset = 0;
        let running = false;

        function draw() {
            ctx.clearRect(0, 0, 340, 340);
            ctx.save();
            ctx.translate(170, 170);
            
            // Cuerpo del reloj circular
            ctx.beginPath();
            ctx.arc(0, 0, r, 0, 2 * Math.PI);
            ctx.lineWidth = 6;
