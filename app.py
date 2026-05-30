import streamlit as st
import random
import time

st.set_page_config(page_title='RELOJ COGNUSS 2', layout='wide')

# Estilos de la infografía oficial
st.markdown('<style>.stApp { background-color: #FFFFFF; color: #0F1E36; font-family: "Segoe UI", sans-serif; } .banner-superior { background-color: #0F1E36; color: white; padding: 20px; border-radius: 4px; margin-bottom: 20px; } .esfera-total { background-color: #0F1E36; color: #FFFFFF; border: 10px solid #2B4C7E; border-radius: 50%; width: 260px; height: 260px; margin: 0 auto; display: flex; flex-direction: column; justify-content: center; align-items: center; } .box-minutero { background-color: #F5FAF6; border-left: 6px solid #2ECC71; padding: 15px; margin-bottom: 12px; } .box-horario { background-color: #F4F7FC; border-left: 6px solid #1A73E8; padding: 15px; margin-bottom: 12px; } .box-segundero { background-color: #FDF5F5; border-left: 6px solid #E74C3C; padding: 15px; margin-bottom: 12px; } .desvanecer-texto { animation: fadeOut 35s forwards; } @keyframes fadeOut { 0% { opacity: 1; } 85% { opacity: 0.1; } 100% { opacity: 0; display: none; } }</style>', unsafe_allow_html=True)

CEDULARIO = {
    1: {'cedula': 'CÉDULA 01', 'eje': 'DERECHO Y MORAL', 'pregunta': 'Paralelo estructural entre Orden Jurídico y Moral.', 'fina': 'El Derecho es BILATERAL y COERCIBLE. La Moral es UNILATERAL e INCOERCIBLE.'},
    2: {'cedula': 'CÉDULA 02', 'eje': 'LA NORMA JURÍDICA', 'pregunta': 'Clasificación de normas imperativas frente a permisivas.', 'fina': 'Imperativas mandan/prohíben absolutamente; Permisivas conceden facultades lícitas renunciables.'},
    3: {'cedula': 'CÉDULA 03', 'eje': 'VIGENCIA, VALIDEZ Y EFICACIA', 'pregunta': 'Clasificación de la Derogación de la Ley en Chile.', 'fina': 'Puede ser Expresa o Tácita, y a su vez Total (toda la ley) o Parcial (algunos artículos).'},
    4: {'cedula': 'CÉDULA 04', 'eje': 'PLENITUD HERMÉTICA', 'pregunta': 'Principio constitucional de inexcusabilidad (Art. 76 CPR).', 'fina': 'Jueces deben resolver conflictos sin excusas, integrando con equidad, analogía y principios.'},
    5: {'cedula': 'CÉDULA 05', 'eje': 'FUENTES DEL ORDENAMIENTO', 'pregunta': 'Diferencia entre Fuentes Materiales y Fuentes Formales.', 'fina': 'Materiales: hechos sociales/políticos que determinan contenido. Formales: normas obligatorias escritas.'},
    6: {'cedula': 'CÉDULA 06', 'eje': 'LA COSTUMBRE', 'pregunta': 'Valor legal de la costumbre en el Derecho Civil chileno.', 'fina': 'Según Art. 2 CC, solo constituye derecho cuando la ley se remite expresamente a ella.'},
    7: {'cedula': 'CÉDULA 07', 'eje': 'JURISPRUDENCIA Y DOCTRINA', 'pregunta': 'Alcance del Efecto Relativo de las sentencias (Art. 3 inc 2 CC).', 'fina': 'Las sentencias poseen fuerza obligatoria exclusivamente respecto de las partes del juicio.'},
    8: {'cedula': 'CÉDULA 08', 'eje': 'LA RELACIÓN JURÍDICA', 'pregunta': 'Requisitos de existencia legal de la persona natural (Art. 74 CC).', 'fina': 'Exige nacer vivo, separarse completamente de la madre y sobrevivir un momento siquiera.'},
    9: {'cedula': 'CÉDULA 09', 'eje': 'LA PERSONA JURÍDICA', 'pregunta': 'Subclasificación de las personas jurídicas de Derecho Privado.', 'fina': 'Se dividen en Con fines de lucro (Sociedades) y Sin fines de lucro (Corporaciones/Fundaciones).'},
    10: {'cedula': 'CÉDULA 10', 'eje': 'DERECHOS REALES Y PERSONALES', 'pregunta': 'Defina el concepto legal de Derecho Real (Art. 577 CC).', 'fina': 'Es el derecho que tenemos sobre una cosa sin respecto a determinada persona (erga omnes).'},
    11: {'cedula': 'CÉDULA 11', 'eje': 'LÍMITES Y ABUSO DEL DERECHO', 'pregunta': '¿Cuándo ocurre el fenómeno del Abuso del Derecho?', 'fina': 'Cuando un sujeto ejerce un derecho lícito pero desviado de su fin, buscando dañar a otro.'},
    12: {'cedula': 'CÉDULA 12', 'eje': 'LOS BIENES Y SU CLASIFICACIÓN', 'pregunta': 'Definición de bienes muebles por anticipación (Art. 571 CC).', 'fina': 'Productos de inmuebles (yerbas, maderas) considerados muebles antes de separarse para contratos.'},
    13: {'cedula': 'CÉDULA 13', 'eje': 'RÉGIMEN JURÍDICO DE BIENES', 'pregunta': 'Formalidad de venta de un bien mueble frente a un inmueble.', 'fina': 'Muebles es consensual (simple acuerdo); Inmuebles exige solemnidad de Escritura Pública.'},
    14: {'cedula': 'CÉDULA 14', 'eje': 'BIENES COMERCIABLES', 'pregunta': 'Diferencia entre Bienes de Uso Público y Bienes Fiscales.', 'fina': 'Uso Público: de la nación, incomerciables (plazas). Fiscales: del Estado, comerciables.'}
}

if 'posicion' not in st.session_state:
    st.session_state.posicion = None
if 'modo' not in st.session_state:
    st.session_state.modo = None

st.markdown('<div class="banner-superior"><h1>6️⃣ PRUEBA DE TEORÍA DEL DERECHO</h1><h2>14 PREGUNTAS — RELOJ COGNUSS 2 - EXAMINADOR IA</h2></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.8, 1, 1.2])

with col1:
    st.markdown('<div style="background:#1F2E54; color:white; padding:15px; border-radius:4px;"><b>📋 INSTRUCCIONES</b><br><small>• Gira el reloj para recorrer las 14 preguntas.<br>• Responde de forma oral o con alternativas.</small></div>', unsafe_allow_html=True)

with col2:
    if st.button('🎯 ACCIONAR GIRO DEL RELOJ'):
        st.session_state.modo = None
        st.session_state.posicion = random.randint(1, 14)
        st.rerun()
        
    hora = f"{st.session_state.posicion:02d}" if st.session_state.posicion else "XII"
    st.markdown(f'<div class="esfera-total"><span style="font-size:11px; color:#4A90E2;">RELOJ JURÍDICO</span><span style="font-size:72px; font-family:serif;">{hora}</span><span>COGNUSS 2</span></div>', unsafe_allow_html=True)

with col3:
    if st.session_state.posicion:
        data = CEDULARIO[st.session_state.posicion]
        st.markdown(f'<div class="box-minutero"><b>🟢 MINUTERO (CONTEXTO):</b><br>{data["cedula"]} - {data["eje"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="box-horario"><b>🔵 HORARIO (PREGUNTA):</b><br><i>"{data["pregunta"]}"</i></div>', unsafe_allow_html=True)
        
        if not st.session_state.modo:
            c_oral, c_alt = st.columns(2)
            if c_oral.button('🗣️ EXAMEN ORAL'):
                st.session_state.modo = 'ORAL'
                st.rerun()
            if c_alt.button('📝 ALTERNATIVAS'):
                st.session_state.modo = 'ALTS'
                st.rerun()
        elif st.session_state.modo == 'ORAL':
            st.markdown(f'<div class="box-segundero"><b>🔴 SEGUNDERO (RESPUESTA FIN):</b><br><p class="desvanecer-texto">{data["fina"]}</p></div>', unsafe_allow_html=True)
            if st.button('✅ SIGUIENTE GIRO'):
                st.session_state.posicion = None
                st.session_state.modo = None
                st.rerun()
        elif st.session_state.modo == 'ALTS':
            opciones = [data['fina'], "Doctrina civil derogada.", "Mandato regulatorio judicial."]
            random.shuffle(opciones)
            st.radio("Seleccione la opción correcta:", opciones)
            if st.button('📥 ENVIAR'):
                st.session_state.posicion = None
                st.session_state.modo = None
                st.rerun()
    else:
        st.info("Haga clic en '🎯 ACCIONAR GIRO DEL RELOJ' para comenzar.")
