import streamlit as st
import random
import time
from datetime import datetime

# Control de caducidad (30 de Junio de 2026)
FECHA_LIMITE = datetime(2026, 6, 30, 23, 59, 59)
if datetime.now() > FECHA_LIMITE:
    st.error("❌ LA LICENCIA DE ESTA APLICACIÓN HA CADUCADO. CONTACTE AL ADMINISTRADOR.")
    st.stop()

st.set_page_config(page_title="MÉTODO COGNUSS 2 - Reloj", layout="wide")

# Estilos CSS Limpios con el diseño exacto de la diapositiva (Fondo Claro, Azul y Púrpura)
st.markdown(
    """
    <style>
    .stApp { 
        background-color: #FFFFFF; 
        color: #0B1E36; 
        font-family: Arial, sans-serif; 
    }
    .header-banner {
        background-color: #0B1E36;
        color: #FFFFFF;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 25px;
        text-align: center;
    }
    .box-minutero {
        background-color: #E8F0FE;
        border-left: 5px solid #1A73E8;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 15px;
    }
    .box-horario {
        background-color: #F3E5F5;
        border-left: 5px solid #7B1FA2;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 15px;
    }
    .box-segundero {
        background-color: #E8F5E9;
        border-left: 5px solid #2E7D32;
        padding: 15px;
        border-radius: 4px;
        margin-bottom: 15px;
    }
    div.stButton > button { 
        background-color: #0B1E36 !important; 
        color: #FFFFFF !important; 
        font-weight: bold !important; 
        width: 100%;
        padding: 10px;
        border-radius: 5px;
    }
    div.stButton > button:hover { 
        background-color: #1A73E8 !important; 
    }
    .circle-slot {
        display: inline-block;
        width: 50px;
        height: 50px;
        line-height: 50px;
        text-align: center;
        margin: 5px;
        border-radius: 50%;
        font-weight: bold;
    }
    .slot-vacia { background-color: #EEEEEE; color: #444444; border: 1px solid #CCCCCC; }
    .slot-activa { background-color: #7B1FA2; color: #FFFFFF; border: 2px solid #0B1E36; }
    .slot-leida { background-color: #2E7D32; color: #FFFFFF; text-decoration: line-through; }
    </style>
    """,
    unsafe_allow_html=True
)

# Base de datos oficial alineada con el Cedulario de la diapositiva
CONOCIMIENTO_CEDULARIO = {
    1: {"tema": "DERECHO Y MORAL", "pregunta": "¿Cuál es la diferencia estructural entre el Orden Jurídico y el Orden Moral respecto a la Bilateralidad/Unilateralidad?", "correcta": "El Derecho es Bilateral (concede facultades a terceros para exigir el cumplimiento), mientras que la Moral es Unilateral (impone deberes al sujeto sin otorgar derechos correlativos a otra persona)."},
    2: {"tema": "NORMA JURÍDICA", "pregunta": "¿Qué distingue a las Normas Imperativas de las Permisivas ante el margen de la voluntad particular?", "correcta": "Las Normas Imperativas no pueden ser modificadas ni anuladas por acuerdo de particulares (absolutas), mientras que las Permisivas otorgan una opción donde el sujeto decide si ejerce el derecho o renuncia a él."},
    3: {"tema": "VIGENCIA, VALIDEZ Y EFICACIA", "pregunta": "¿Cuál es la diferencia entre una derogación legal de tipo Total y una de tipo Parcial?", "correcta": "La Derogación Total deja sin efecto la totalidad del cuerpo legal preexistente, mientras que la Parcial elimina solo algunas disposiciones específicas manteniendo el resto de la ley antigua vigente."},
    4: {"tema": "PLENITUD HERMÉTICA Y LAGUNAS DEL DERECHO", "pregunta": "¿Qué mandata el principio de inexcusabilidad consagrado en el art. 76 de la Constitución a los jueces?", "correcta": "Obliga a los jueces a resolver los conflictos sometidos a su conocimiento, incluso si no existe una ley expresa que regule el caso, debiendo fallar utilizando los principios generales del derecho."},
    5: {"tema": "FUENTES DEL ORDENAMIENTO JURÍDICO", "pregunta": "Defina la diferencia de naturaleza entre las Fuentes Materiales y las Fuentes Formales.", "correcta": "Las Fuentes Materiales son hechos de la realidad social (metajurídicos) que determinan el contenido; las Fuentes Formales son actos jurídicos normativos institucionales con fuerza obligatoria."},
    6: {"tema": "LA COSTUMBRE", "pregunta": "En el ordenamiento del Derecho Civil chileno, ¿cuándo tiene valor legal la costumbre?", "correcta": "Según el Artículo 2 del Código Civil, la costumbre solo constituye derecho en los casos en que la propia ley se remite expresamente a ella (Secundum legem)."},
    7: {"tema": "JURISPRUDENCIA Y DOCTRINA", "pregunta": "Explique el alcance del Efecto Relativo de las sentencias judiciales chilenas según el artículo 3° inciso 2° del Código Civil.", "correcta": "Las sentencias judiciales solo poseen fuerza obligatoria respecto de las partes que intervinieron en ese juicio específico. En Chile no existe el precedente obligatorio automático."},
    8: {"tema": "LA RELACIÓN JURÍDICA", "pregunta": "¿Cuáles son las condiciones simultáneas requeridas para el principio de existencia legal de la persona natural (Art. 74 CC)?", "correcta": "1. Separación completa de la madre; 2. Que los lazos del cordón sean cortados; 3. Haber sobrevivido un momento siquiera a dicha separación."},
    9: {"tema": "LA PERSONA JURÍDICA", "pregunta": "¿Cómo se subclasifican las personas jurídicas de Derecho Privado según sus fines?", "correcta": "Se subclasifican en entidades Con fines de lucro (Sociedades Comerciales como S.A., S.R.L., SpA) y entidades Sin fines de lucro (Corporaciones y Fundaciones)."},
    10: {"tema": "DERECHOS REALES Y PERSONALES", "pregunta": "Defina el concepto legal de Derecho Real según lo estipulado en el Artículo 577 del Código Civil.", "correcta": "Es el derecho que tenemos sobre una cosa sin respecto a determinada persona, naciendo de la concurrencia de un Título y un Modo de Adquirir."},
    11: {"tema": "LÍMITES Y ABUSO DEL DERECHO", "pregunta": "¿Cuándo ocurre técnicamente el fenómeno del Abuso del Derecho?", "correcta": "Ocurre cuando un sujeto ejerce un derecho legal legítimo, pero de una manera desviada, con dolo, negligencia o con el único fin de causar daño a otra persona."},
    12: {"tema": "LOS BIENES (O COSAS) - CLASIFICACIÓN", "pregunta": "¿Qué define a los bienes muebles por anticipación regulados en el artículo 571 del Código Civil?", "correcta": "Son productos de los inmuebles y cosas accesorias a ellos que se consideran muebles, aun antes de su separación, para el efecto de constituir un derecho sobre ellos."},
    13: {"tema": "RÉGIMEN JURÍDICO DE LOS BIENES", "pregunta": "Compare la formalidad de venta exigida para un bien mueble frente a un bien inmueble.", "correcta": "La venta de bienes muebles es meramente consensual (acuerdo simple), mientras que la de inmuebles es solemne y exige obligatoriamente ser otorgada por Escritura Pública (Art. 1801 CC)."},
    14: {"tema": "BIENES COMERCIABLES E INCOMERCIABLES", "pregunta": "Diferencie los Bienes Nacionales de Uso Público de los Bienes Fiscales respecto a su comerciabilidad.", "correcta": "Los de Uso Público son strictly incomerciables, inalienables e imprescriptibles; los Bienes Fiscales son comerciables internamente y el Estado puede venderlos o arrendarlos."}
}

if "posiciones_reloj" not in st.session_state:
    st.session_state.posiciones_reloj = list(range(1, 15))
if "cedula_activa" not in st.session_state:
    st.session_state.cedula_activa = None
if "evaluacion" not in st.session_state:
    st.session_state.evaluacion = None

# Banner Superior igual a la diapositiva
st.markdown(
    """
    <div class='header-banner'>
        <h1>MÉTODO COGNUSS 2: RELOJ DEL CONOCIMIENTO</h1>
        <p>PRUEBA DE TEORÍA DEL DERECHO — 14 PREGUNTAS DEL CEDULARIO</p>
    </div>
    """, 
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎡 Esfera del Reloj (14 Posiciones)")
    
    if len(st.session_state.posiciones_reloj) > 0:
        if st.button("🔄 HACER GIRAR EL RELOJ COGNUSS 2"):
            st.session_state.evaluacion = None
            seleccionada = random.choice(st.session_state.posiciones_reloj)
            st.session_state.posiciones_reloj.remove(seleccionada)
            st.session_state.cedula_activa = seleccionada
    else:
        st.success("🎉 ¡Excelente! Completaste el recorrido del reloj de 14 horas.")
        if st.button("♻️ Reiniciar Esfera"):
            st.session_state.posiciones_reloj = list(range(1, 15))
            st.session_state.cedula_activa = None
            st.rerun()

    # Representación de las posiciones circulares del reloj
    st.write("")
    html_esfera = "<div>"
    for pos in range(1, 15):
        if pos == st.session_state.cedula_activa:
            html_esfera += f"<div class='circle-slot slot-activa'>{pos}</div>"
        elif pos not in st.session_state.posiciones_reloj:
            html_esfera += f"<div class='circle-slot slot-leida'>{pos}</div>"
        else:
            html_esfera += f"<div class='circle-slot slot-vacia'>{pos}</div>"
    html_esfera += "</div>"
    st.markdown(html_esfera, unsafe_allow_html=True)

with col2:
    st.subheader("📋 Desglose del Motor de Examen")
    
    if st.session_state.cedula_activa:
        item = CONOCIMIENTO_CEDULARIO[st.session_state.cedula_activa]
        
        # 1. MINUTERO (Contexto)
        st.markdown(
            f"""
            <div class='box-minutero'>
                <b style='color: #1A73E8;'>⏱️ MINUTERO (CONTEXTO):</b><br>
                <span>Usted se encuentra posicionado en la <b>Pregunta N° {st.session_state.cedula_activa}</b> del Cedulario Oficial.</span>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # 2. HORARIO (Pregunta)
        st.markdown(
            f"""
            <div class='box-horario'>
                <b style='color: #7B1FA2;'>🕐 HORARIO (PREGUNTA):</b><br>
