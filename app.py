import streamlit as st
import random
import time
from datetime import datetime

# 1. CONTROL DE CADUCIDAD REQUERIDO (30 de Junio de 2026)
FECHA_LIMITE = datetime(2026, 6, 30, 23, 59, 59)
if datetime.now() > FECHA_LIMITE:
    st.error("❌ LA LICENCIA DE ESTA APLICACIÓN HA CADUCADO (30 DE JUNIO DE 2026). CONTACTE AL ADMINISTRADOR.")
    st.stop()

# Configuración del entorno de visualización amplia
st.set_page_config(page_title="COGNUSS - Reloj del Conocimiento", layout="wide")

# Estilos CSS de Consola Jurídica USS
st.markdown(
    """
    <style>
    .stApp { background-color: #0b0c10; color: #c5c6c7; font-family: monospace; }
    h1, h2, h3, h4 { color: #ffffff !important; font-family: monospace; }
    .ruleta-box { background-color: #1f2833; border: 2px dashed #45a29e; padding: 20px; border-radius: 8px; text-align: center; }
    .card-respuesta { background-color: #0b0c10; border-left: 5px solid #66fcf1; padding: 15px; margin-top: 10px; border-radius: 4px; }
    .timer-digital { background-color: #1a1a1a; border: 2px solid #ff4b4b; padding: 10px; border-radius: 5px; text-align: center; font-size: 28px; font-weight: bold; color: #ff4b4b; }
    </style>
    """,
    unsafe_allow_html=True
)

# Base de datos de sub-preguntas y respuestas correctas basadas en el Cedulario Oficial
CONOCIMIENTO_CEDULARIO = {
    1: {"titulo": "CÉDULA 1.- El Derecho y la Moral", "pregunta": "¿Cuál es la diferencia estructural entre el Orden Jurídico y el Orden Moral respecto a la Bilateralidad/Unilateralidad?", "correcta": "El Derecho es Bilateral (concede facultades a terceros para exigir el cumplimiento), mientras que la Moral es Unilateral (impone deberes al sujeto sin otorgar derechos correlativos a otra persona)."},
    2: {"titulo": "CÉDULA 2.- La Norma Jurídica", "pregunta": "¿Qué distingue a las Normas Imperativas de las Permisivas ante el margen de la voluntad particular?", "correcta": "Las Normas Imperativas no pueden ser modificadas ni anuladas por acuerdo de particulares (absolutas), mientras que las Permisivas otorgan una opción donde el sujeto decide si ejerce el derecho o renuncia a él."},
    3: {"titulo": "CÉDULA 3.- Vigencia, Validez y Eficacia", "pregunta": "¿Cuál es la diferencia entre una derogación legal de tipo Total y una de tipo Parcial?", "correcta": "La Derogación Total deja sin efecto la totalidad del cuerpo legal preexistente, mientras que la Parcial elimina solo algunas disposiciones específicas manteniendo el resto de la ley antigua vigente."},
    4: {"titulo": "CÉDULA 4.- Plenitud Hermética", "pregunta": "¿Qué mandata el principio de inexcusabilidad consagrado en el art. 76 de la Constitución a los jueces?", "correcta": "Obliga a los jueces a resolver los conflictos sometidos a su conocimiento, incluso si no existe una ley expresa que regule el caso, debiendo fallar utilizando los principios generales del derecho."},
    5: {"titulo": "CÉDULA 5.- Fuentes del Ordenamiento", "pregunta": "Defina la diferencia de naturaleza entre las Fuentes Materiales y las Fuentes Formales.", "correcta": "Las Fuentes Materiales son hechos de la realidad social (metajurídicos) que determinan el contenido; las Fuentes Formales son actos jurídicos normativos institucionales con fuerza obligatoria."},
    6: {"titulo": "CÉDULA 6.- La Costumbre", "pregunta": "¿Cuándo tiene valor legal la costumbre dentro del ordenamiento del Derecho Civil chileno?", "correcta": "Según el Artículo 2 del Código Civil, la costumbre solo constituye derecho en los casos en que la propia ley se remite expresamente a ella (Secundum legem)."},
    7: {"titulo": "CÉDULA 7.- Jurisprudencia y Doctrina", "pregunta": "Explique el alcance del Efecto Relativo de las sentencias judiciales chilenas según el artículo 3° inciso 2° del Código Civil.", "correcta": "Las sentencias judiciales solo poseen fuerza obligatoria respecto de las partes que intervinieron en ese juicio específico. En Chile no existe el precedente obligatorio automático."},
    8: {"titulo": "CÉDULA 8.- La Relación Jurídica", "pregunta": "¿Cuáles son las 3 condiciones simultáneas requeridas para el principio de existencia legal de la persona natural (Art. 74 CC)?", "correcta": "1. Separación completa de la madre; 2. Que los lazos del cordón sean cortados; 3. Haber sobrevivido un momento siquiera a dicha separación."},
    9: {"titulo": "CÉDULA 9.- La Persona Jurídica", "pregunta": "¿Cómo se subclasifican las personas jurídicas de Derecho Privado según sus fines?", "correcta": "Se subclasifican en entidades Con fines de lucro (Sociedades Comerciales como S.A., S.R.L., SpA) y entidades Sin fines de lucro (Corporaciones y Fundaciones)."},
    10: {"titulo": "CÉDULA 10.- Derechos Reales y Personales", "pregunta": "Defina el concepton legal de Derecho Real según lo estipulado en el Artículo 577 del Código Civil.", "correcta": "Es el derecho que tenemos sobre una cosa sin respecto a determinada persona, naciendo de la concurrencia de un Título y un Modo de Adquirir."},
    11: {"titulo": "CÉDULA 11.- Límites de los Derechos Subjetivos", "pregunta": "¿Cuándo ocurre técnicamente el fenómeno del Abuso del Derecho?", "correcta": "Ocurre cuando un sujeto ejerce un derecho legal legítimo, pero de una manera desviada, con dolo, negligencia o con el único fin de causar daño a otra persona."},
    12: {"titulo": "CÉDULA 12.- Los Bienes y su Clasificación", "pregunta": "¿Qué define a los bienes muebles por anticipación regulados en el artículo 571 del Código Civil?", "correcta": "Son productos de los inmuebles y cosas accesorias a ellos que se consideran muebles, aun antes de su separación, para el efecto de constituir un derecho sobre ellos."},
    13: {"titulo": "CÉDULA 13.- Régimen Jurídico de los Bienes", "pregunta": "Compare la formalidad de venta exigida para un bien mueble frente a un bien inmueble.", "correcta": "La venta de bienes muebles es meramente consensual (acuerdo simple), mientras que la de inmuebles es solemne y exige obligatoriamente ser otorgada por Escritura Pública (Art. 1801 CC)."},
    14: {"titulo": "CÉDULA 14.- Bienes Comerciables e Incomerciables", "pregunta": "Diferencie los Bienes Nacionales de Uso Público de los Bienes Fiscales respecto a su comerciabilidad.", "correcta": "Los de Uso Público son estrictamente incomerciables, inalienables e imprescriptibles; los Bienes Fiscales son comerciables internamente y el Estado puede venderlos o arrendarlos."}
}

# Inicialización del balotario aleatorio persistente
if "posiciones_ruleta" not in st.session_state:
    st.session_state.posiciones_ruleta = list(range(1, 15))
if "cedula_activa" not in st.session_state:
    st.session_state.cedula_activa = None
if "mostrar_respuesta" not in st.session_state:
    st.session_state.mostrar_respuesta = False
if "evaluacion" not in st.session_state:
    st.session_state.evaluacion = None

# Encabezado técnico del software
st.title("⏳ RELOJ DEL CONOCIMIENTO: AUTOESTUDIO JURÍDICO")
st.text("ENTORNO EVALUATIVO ACTIVO - UNIVERSIDAD SAN SEBASTIÁN")
st.text("==========================================================================================")

# Estructuración de las ventanas en pantalla
col_izq, col_der = st.columns(2)

with col_izq:
    st.header("🎡 Estado de la Ruleta (14 Posiciones)")
    posiciones_restantes = len(st.session_state.posiciones_ruleta)
    st.write(f"Cédulas en el balotario: **{posiciones_restantes} / 14**")
    
    if posiciones_restantes > 0:
        if st.button("🔄 ACCIONAR GIRO ALEATORIO"):
            st.session_state.evaluacion = None
            st.session_state.mostrar_respuesta = False
            
            with st.spinner("Girando componentes del reloj..."):
                time.sleep(0.6)
                seleccionada = random.choice(st.session_state.posiciones_ruleta)
                st.session_state.posiciones_ruleta.remove(seleccionada)
                st.session_state.cedula_activa = seleccionada
                st.session_state.mostrar_respuesta = True
    else:
        st.success("🎉 ¡Perfecto! Has recorrido las 14 posiciones de la ruleta.")
        if st.button("♻️ Recargar Reloj del Conocimiento"):
            st.session_state.posiciones_ruleta = list(range(1, 15))
            st.session_state.cedula_activa = None
            st.session_state.mostrar_respuesta = False
            st.rerun()
            
    # Dibujo visual plano de la ruleta de 14 posiciones
    salida_visual = ""
    for pos in range(1, 15):
        if pos == st.session_state.cedula_activa:
            salida_visual += f" 🎯[POS {pos:02d}] "
        elif pos not in st.session_state.posiciones_ruleta:
            salida_visual += f" 🚫[USADA] "
        else:
            salida_visual += f" 🔘[POS {pos:02d}] "
        if pos == 7: 
            salida_visual += "\n\n"
    st.text(salida_visual)

with col_der:
    st.header("📋 Ventana Lateral de Evaluación")
    
    if st.session_state.cedula_activa and st.session_state.mostrar_respuesta:
        id_c = st.session_state.cedula_activa
        datos = CONOCIMIENTO_CEDULARIO[id_c]
        
        st.subheader(datos["titulo"])
        st.markdown(f"**Sub-Pregunta Evaluativa:**\n*{datos['pregunta']}*")
        st.write("---")
        
        # Marcador dinámico lateral para lectura en voz alta
        placeholder_cronometro = st.empty()
        placeholder_respuesta = st.empty()
        
        placeholder_cronometro.markdown("<div class='timer-digital'>⏱️ LECTURA EN VOZ ALTA ACTIVA</div>", unsafe_allow_html=True)
        placeholder_respuesta.markdown(
            f"""
            <div class='card-respuesta'>
                <span style='color: #66fcf1; font-weight: bold;'>[RESPUESTA CORRECTA OFICIAL]</span><br>
                <p style='font-size: 16px; color: #ffffff; margin-top: 5px;'>{datos['correcta']}</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # Botonera académica de registro de desempeño
