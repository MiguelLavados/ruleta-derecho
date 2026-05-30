import streamlit as st
import random
import time
from datetime import datetime
import streamlit.components.v1 as components

# Control de caducidad (30 de Junio de 2026)
FECHA_LIMITE = datetime(2026, 6, 30, 23, 59, 59)
if datetime.now() > FECHA_LIMITE:
    st.error("❌ LA LICENCIA DE ESTA APLICACIÓN HA CADUCADO. CONTACTE AL ADMINISTRADOR.")
    st.stop()

st.set_page_config(page_title="MÉTODO COGNUSS 2 - Reloj", layout="wide")

# Estilos de la aplicación
st.markdown(
    """
    <style>
    .stApp { background-color: #FFFFFF; color: #0B1E36; font-family: Arial, sans-serif; }
    .header-banner { background-color: #0B1E36; color: #FFFFFF; padding: 15px; border-radius: 8px; text-align: center; margin-bottom: 20px;}
    .box-minutero { background-color: #E8F0FE; border-left: 5px solid #1A73E8; padding: 15px; border-radius: 4px; margin-bottom: 12px; }
    .box-horario { background-color: #F3E5F5; border-left: 5px solid #7B1FA2; padding: 15px; border-radius: 4px; margin-bottom: 12px; }
    .box-segundero { background-color: #E8F5E9; border-left: 5px solid #2E7D32; padding: 15px; border-radius: 4px; margin-bottom: 12px; }
    div.stButton > button { background-color: #7B1FA2 !important; color: white !important; font-weight: bold; width: 100%; padding: 12px; border-radius: 6px; font-size: 16px; }
    </style>
    """,
    unsafe_allow_html=True
)

CONOCIMIENTO_CEDULARIO = {
    1: {"tema": "DERECHO Y MORAL", "pregunta": "¿Cuál es la diferencia estructural entre el Orden Jurídico y el Orden Moral respecto a la Bilateralidad/Unilateralidad?", "correcta": "El Derecho es Bilateral, mientras que la Moral es Unilateral."},
    2: {"tema": "NORMA JURÍDICA", "pregunta": "¿Qué distingue a las Normas Imperativas de las Permisivas ante el margen de la voluntad?", "correcta": "Las Imperativas son absolutas e inmodificables; las Permisivas otorgan opciones renunciables."},
    3: {"tema": "VIGENCIA, VALIDEZ Y EFICACIA", "pregunta": "¿Cuál es la diferencia entre una derogación legal de tipo Total y una de tipo Parcial?", "correcta": "La Total elimina todo el cuerpo legal; la Parcial solo elimina artículos específicos."},
    4: {"tema": "PLENITUD HERMÉTICA Y LAGUNAS DEL DERECHO", "pregunta": "¿Qué mandata el principio de inexcusabilidad consagrado en el art. 76 de la CPR?", "correcta": "Obliga a los jueces a resolver conflictos aun sin ley expresa, usando principios generales."},
    5: {"tema": "FUENTES DEL ORDENAMIENTO JURÍDICO", "pregunta": "Defina la diferencia de naturaleza entre las Fuentes Materiales y las Fuentes Formales.", "correcta": "Materiales son hechos sociales reales; Formales son las normas escritas obligatorias."},
    6: {"tema": "LA COSTUMBRE", "pregunta": "En el ordenamiento del Derecho Civil chileno, ¿cuándo tiene valor legal la costumbre?", "correcta": "Solo cuando la ley se remite expresamente a ella (Art. 2 Código Civil)."},
    7: {"tema": "JURISPRUDENCIA Y DOCTRINA", "pregunta": "Explique el alcance del Efecto Relativo de las sentencias judiciales (Art. 3 inc 2 CC).", "correcta": "Las sentencias solo obligan a las partes que litigaron en ese juicio específico."},
    8: {"tema": "LA RELACIÓN JURÍDICA", "pregunta": "Mencione los tres requisitos de existencia legal de la persona natural (Art. 74 CC).", "correcta": "Nacer viva, separarse completamente de la madre y sobrevivir un momento siquiera."},
    9: {"tema": "LA PERSONA JURÍDICA", "pregunta": "¿Cómo se subclasifican las personas jurídicas de Derecho Privado según sus fines?", "correcta": "Con fines de lucro (sociedades) y sin fines de lucro (corporaciones/fundaciones)."},
    10: {"tema": "DERECHOS REALES Y PERSONALES", "pregunta": "Defina el concepto legal de Derecho Real según el Artículo 577 del Código Civil.", "correcta": "Es el derecho que se tiene sobre una cosa sin respecto a determinada persona."},
    11: {"tema": "LÍMITES Y ABUSO DEL DERECHO", "pregunta": "¿Cuándo ocurre técnicamente el fenómeno del Abuso del Derecho?", "correcta": "Cuando se ejerce un derecho legítimo de forma desviada con el fin único de dañar."},
    12: {"tema": "LOS BIENES (O COSAS) - CLASIFICACIÓN", "pregunta": "¿Qué define a los bienes muebles por anticipación (Art. 571 CC)?", "correcta": "Productos de inmuebles que se consideran muebles antes de separarse para constituir derechos."},
    13: {"tema": "RÉGIMEN JURÍDICO DE LOS BIENES", "pregunta": "Compare la formalidad de venta exigida para un bien mueble frente a un bien inmueble.", "correcta": "Muebles es consensual (simple acuerdo); Inmuebles requiere Escritura Pública."},
    14: {"tema": "BIENES COMERCIABLES E INCOMERCIABLES", "pregunta": "Diferencie los Bienes Nacionales de Uso Público de los Bienes Fiscales.", "correcta": "Uso Público son totalmente incomerciables; Fiscales pertenecen al Estado y son comerciables."}
}

if "historial_ruleta" not in st.session_state:
    st.session_state.historial_ruleta = []
if "seleccion_actual" not in st.session_state:
    st.session_state.seleccion_actual = None

st.markdown(
    """
    <div class='header-banner'>
        <h1>MÉTODO COGNUSS 2: EL RELOJ DEL CONOCIMIENTO</h1>
        <p>REPLICANDO EL MOTOR EVALUATIVO DE PREGUNTAS ENDÓGENAS</p>
    </div>
    """, unsafe_allow_html=True
)

col1, col2 = st.columns([1.2, 1])

with col1:
    st.write("### 🎡 Ruleta / Reloj de Cédulas")
    
    # Renderizado dinámico del Reloj de Agujas/Ruleta usando Canvas HTML5
    canvas_html = """
    <div style="text-align:center;">
        <canvas id="canvas" width="400" height="400"></canvas><br>
        <button id="spinBtn" style="background-color:#0B1E36; color:white; border:none; padding:12px 24px; font-weight:bold; border-radius:5px; font-size:16px; cursor:pointer; width:80%;">🎯 INICIAR GIRO MECÁNICO</button>
    </div>
    <script>
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        const sections = 14;
        const radius = 180;
        let currentAngle = 0;
        let isSpinning = false;

        function drawClock() {
            ctx.clearRect(0,0,400,400);
            ctx.translate(200, 200);
            
            // Dibujar círculo externo (Esfera del Reloj)
            ctx.beginPath();
            ctx.arc(0, 0, radius, 0, 2 * Math.PI);
            ctx.lineWidth = 6;
            ctx.strokeStyle = '#0B1E36';
            ctx.fillStyle = '#F8F9FA';
            ctx.fill();
            ctx.stroke();

            // Dibujar divisiones de horas
            for(let i=1; i<=sections; i++) {
                let angle = (i * 2 * Math.PI / sections) + currentAngle;
                ctx.rotate(angle);
                ctx.beginPath();
                ctx.moveTo(0,0);
                ctx.lineTo(0, -radius);
                ctx.strokeStyle = '#CCCCCC';
                ctx.lineWidth = 2;
                ctx.stroke();
                
                // Texto de la Posición
                ctx.fillStyle = '#0B1E36';
                ctx.font = 'bold 14px Arial';
                ctx.fillText(i, -5, -radius + 25);
                ctx.rotate(-angle);
            }

            // Aguja de Selección Fija (Indicador superior de la ruleta)
            ctx.beginPath();
            ctx.moveTo(-10, -radius - 10);
            ctx.lineTo(10, -radius - 10);
            ctx.lineTo(0, -radius + 10);
            ctx.fillStyle = '#7B1FA2';
            ctx.fill();
            
            ctx.translate(-200, -200);
        }

        document.getElementById('spinBtn').addEventListener('click', () => {
            if(isSpinning) return;
            isSpinning = true;
            let speed = Math.random() * 0.4 + 0.3;
            let friction = 0.98;
            
            function animate() {
                currentAngle += speed;
                speed *= friction;
                drawClock();
                
                if(speed > 0.002) {
                    requestAnimationFrame(animate);
                } else {
                    isSpinning = false;
                    // Calcular qué número cayó apuntando arriba
                    let normalizedAngle = (2 * Math.PI - (currentAngle % (2 * Math.PI))) % (2 * Math.PI);
                    let selected = Math.floor((normalizedAngle / (2 * Math.PI)) * sections) + 1;
                    if(selected > 14) selected = 14;
                    
                    // Enviar resultado de vuelta a Streamlit
                    window.parent.postMessage({type: 'streamlit:setComponentValue', value: selected}, '*');
                }
            }
            animate();
        });
        drawClock();
    </script>
    """
    
    # Capturar la selección interactiva de la ruleta animada
    resultado_ruleta = components.html(canvas_html, height=460)
    
    # Botón puente nativo para cuando termine la animación de Javascript
    if resultado_ruleta:
        st.session_state.seleccion_actual = int(resultado_ruleta)

with col2:
    st.write("### 📋 Desglose del Reloj Cognuss 2")
    
    if st.session_state.seleccion_actual:
        id_c = st.session_state.seleccion_actual
        item = CONOCIMIENTO_CEDULARIO[id_c]
        
        # Estructura tripartita solicitada: Minutero, Horario y Segundero
        st.markdown(
            f"""
            <div class='box-minutero'>
                <b style='color: #1A73E8;'>⏱️ MINUTERO (CONTEXTO):</b><br>
                <span>Usted se encuentra posicionado en la <b>Cédula / Posición N° {id_c}</b></span>
            </div>
            <div class='box-horario'>
                <b style='color: #7B1FA2;'>🕐 HORARIO (PREGUNTA):</b><br>
                <span style='font-size: 13px; text-transform:uppercase;'><b>EJE TEMÁTICO:</b> {item['tema']}</span><br>
                <p style='font-size: 15px; font-style: italic; margin-top: 5px;'>"{item['pregunta']}"</p>
            </div>
            <div class='box-segundero'>
                <b style='color: #2E7D32;'>🎯 SEGUNDERO (RESPUESTA FINA):</b><br>
