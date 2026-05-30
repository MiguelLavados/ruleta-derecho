import streamlit as st
import random
import time
from datetime import datetime

# Control de caducidad requerido (30 de Junio de 2026)
FECHA_LIMITE = datetime(2026, 6, 30, 23, 59, 59)
if datetime.now() > FECHA_LIMITE:
    st.error('❌ LA LICENCIA DE ESTA APLICACIÓN HA CADUCADO. CONTACTE AL ADMINISTRADOR.')
    st.stop()

st.set_page_config(page_title='RELOJ COGNUSS 2 - EXAMINADOR IA', layout='wide')

# Estilos CSS de Alta Relojería basados fielmente en la infografía Cognuss 2
st.markdown('<style>.stApp { background-color: #F4F6F9; color: #0B1E36; font-family: "Segoe UI", Arial, sans-serif; } .header-cognuss { background-color: #0B1E36; color: #FFFFFF; padding: 20px; border-radius: 6px; text-align: center; margin-bottom: 25px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); } .header-cognuss h1 { font-size: 26px !important; letter-spacing: 2px; color: #FFFFFF !important; margin: 0; font-weight: bold; } .header-cognuss p { font-size: 13px; color: #D4AF37; margin: 5px 0 0 0; letter-spacing: 1px; } .box-minutero-full { background-color: #FFFFFF; border-top: 5px solid #2ECC71; padding: 20px; border-radius: 6px; margin-bottom: 15px; box-shadow: 0 3px 10px rgba(0,0,0,0.05); } .box-horario-full { background-color: #FFFFFF; border-top: 5px solid #1A73E8; padding: 20px; border-radius: 6px; margin-bottom: 15px; box-shadow: 0 3px 10px rgba(0,0,0,0.05); } .box-segundero-full { background-color: #FFFFFF; border-top: 5px solid #E74C3C; padding: 20px; border-radius: 6px; margin-bottom: 15px; box-shadow: 0 3px 10px rgba(0,0,0,0.05); } .reloj-esfera-uss { background-color: #0B1E36; color: #FFFFFF; padding: 20px; border-radius: 50%; width: 340px; height: 340px; margin: 0 auto; text-align: center; display: flex; flex-direction: column; justify-content: center; align-items: center; border: 10px solid #D4AF37; box-shadow: 0px 10px 25px rgba(0,0,0,0.3); } .desvanecer-respuesta { animation: fadeOutEffect 35s forwards; font-size: 16px; color: #2C3E50; line-height: 1.6; } @keyframes fadeOutEffect { 0% { opacity: 1; } 85% { opacity: 0.1; } 100% { opacity: 0; display: none; } }</style>', unsafe_allow_html=True)

# Base de datos indexada con el Cedulario USS y explayada con detalle doctrinal
CEDULARIO_OFICIAL = {
    1: {
        'cedula': 'CEDULA 1.- El Derecho y la Moral. Normas de uso y trato social.',
        'subpreguntas': [
            {'id': '1.1', 'texto': 'Explaye sobre la norma moral y describa detalladamente el alcance de sus características esenciales.', 'correcta': 'La norma moral regula la conducta humana orientada al bien. Es UNILATERAL (frente al sujeto obligado no existe un tercero facultado para exigir el cumplimiento), INTERIOR (atiende a los motivos rectores del obrar y la pureza del acto), INCOERCIBLE (su cumplimiento debe ser espontáneo y carece de sanción física impuesta por el Estado) y AUTÓNOMA (el propio individuo la reconoce de manera libre).', 'distractores': ['Es bilateral, puesto que otorga facultades correlativas y multas estatales por desobedecerla.', 'Es un mandato puramente heterónomo dictado de manera externa y coercible por el Congreso Nacional.', 'Es una regla exterior que solo sanciona resultados sin medir la pureza e intención del acto humano.']},
            {'id': '1.2', 'texto': 'Establezca detalladamente las diferencias estructurales entre el orden del Derecho y el orden de la Moral.', 'correcta': 'El Derecho regula la conducta intersubjetiva externa mediante la BILATERALIDAD (concede facultades recíprocas) y la COERCIBILIDAD (posibilidad legítima de aplicar la fuerza estatal). En contraposición, la Moral opera en el fuero interno (UNILATERALIDAD) y carece de mecanismos forzados de coacción física (INCOERCIBILIDAD).', 'distractores': ['Ambos órdenes comparten de forma exacta la coacción y sanción punitiva estatal bajo tutela judicial.', 'El Derecho es puramente interior y autónomo, mientras que la Moral es enteramente exterior y heterónoma.', 'La diferencia radica únicamente en el espacio de aplicación territorial, manteniendo idénticas estructuras jurídicas.']},
            {'id': '1.3', 'texto': 'Explaye sobre las normas de uso y trato social: concepto, características esenciales y diferencias estructurales con la norma jurídica.', 'correcta': 'Son directrices de conducta de carácter EXTERIOR (importa el cumplimiento del acto formal) e INCOERCIBLE (la sanción es el reproche social, pero nunca la fuerza pública). Son HETERÓNOMAS. A diferencia de la norma jurídica, carecen de un aparato institucional coercible.', 'distractores': ['Son normas dictadas bajo ley solemne que el juez aplica de forma coercible en los juicios civiles.', 'Tienen rango constitucional y conllevan multas recaudadas formalmente por la Tesorería General.', 'Son mandatos completamente internos y autónomos que el individuo jamás externaliza frente a su entorno social.']}
        ]
    },
    2: {
        'cedula': 'CEDULA 2.- La norma jurídica.',
        'subpreguntas': [
            {'id': '2.1', 'texto': 'Analice y explaye de forma técnica las características esenciales de la norma jurídica.', 'correcta': 'Es BILATERAL (establece una correlación entre deberes de un sujeto y derechos de otro), EXTERIOR (valora primariamente el comportamiento manifestado), COERCIBLE (ante el incumplimiento, se activa la potestad del Estado) y HETERÓNOMA (es creada por una voluntad ajena y superior al sujeto obligado).', 'distractores': ['Es una pauta puramente interior, incoercible, autónoma y desligada de la fuerza pública estatal.', 'Se caracteriza por ser unilateral y autónoma, naciendo exclusivamente del fuero íntimo del ciudadano.', 'Es una regla que no admite coacción y cuya validez depende exclusivamente del agrado individual del sujeto.']},
            {'id': '2.2', 'texto': 'Explique técnicamente la clasificación entre normas jurídicas imperativas y permisivas.', 'correcta': 'Las IMPERATIVAS mandan o prohíben de forma absoluta, limitando la autonomía de la voluntad; las PERMISIVAS conceden una facultad o derecho subjetivo a su titular, otorgándole un marco de libertad lícita.', 'distractores': ['Las imperativas aconsejan conductas y las permisivas imponen castigos de presidio mayor.', 'Son categorías en desuso que carecen de aplicación formal dentro de los Códigos chilenos actuales.', 'Las imperativas posibilitan la libre modificación por acuerdo de particulares y las permisivas lo prohíben.']},
            {'id': '2.3', 'texto': 'Describa exhaustivamente la estructura lógica de la norma jurídica.', 'correcta': 'Se estructura formalmente mediante un Juicio Hipotético compuesto por dos elementos correlativos: 1) El Supuesto de Hecho (la hipótesis que prevé un hecho social) y 2) La Consecuencia Jurídica (el efecto legal, sanción o derecho que se activa).', 'distractores': ['Es una estructura lineal simple que carece de hipótesis previa y opera solo como consejos.', 'Se compone exclusivamente de un relato descriptivo histórico que no impone sanciones ni efectos.', 'Consiste en un mandato unilateral donde la consecuencia se produce sin necesidad de un supuesto previo.']}
        ]
    }
}

if 'cedula_activa' not in st.session_state:
    st.session_state.cedula_activa = None
if 'subpregunta_index' not in st.session_state:
    st.session_state.subpregunta_index = 0
if 'respuestas_correctas' not in st.session_state:
    st.session_state.respuestas_correctas = 0
if 'total_respondidas' not in st.session_state:
    st.session_state.total_respondidas = 0
if 'modalidad' not in st.session_state:
    st.session_state.modalidad = None
if 'alternativas_mezcladas' not in st.session_state:
    st.session_state.alternativas_mezcladas = []

# Título Minimalista
st.markdown('<div class="header-cognuss"><h1>SISTEMA COGNUSS 2 — EXAMINADOR IA</h1><p>MÉTODO DE DOMINIO PROGRESIVO DEL CONOCIMIENTO — UNIVERSIDAD SAN SEBASTIÁN</p></div>', unsafe_allow_html=True)

col_izq, col_der = st.columns([1, 1.2])

with col_izq:
    st.subheader('🎡 Esfera Mecánica Cognuss 2')
    
    texto_reloj = f'{st.session_state.cedula_activa:02d}' if st.session_state.cedula_activa else 'XII'
    sub_texto = 'GIRO PROCESADO' if st.session_state.cedula_activa else 'MECANISMO ARMADO'
        
    st.markdown(f'<div class="reloj-esfera-uss"><span style="font-size: 11px; color: #D4AF37; font-weight: bold; letter-spacing: 3px;">{sub_texto}</span><span style="font-size: 84px; font-weight: 300; color: #FFFFFF; font-family: "Times New Roman", serif; margin: 5px 0;">{texto_reloj}</span><span style="font-size: 10px; color: #FAFAFA; letter-spacing: 2px;">RELOJ JURÍDICO</span></div>', unsafe_allow_html=True)
    
    st.write('')
    if st.button('🎯 ACCIONAR GIRO MECÁNICO DEL RELOJ'):
        st.session_state.modalidad = None
        st.session_state.subpregunta_index = 0
        
        placeholder_anim = st.empty()
        for i in range(8):
            num_falso = random.randint(1, 14)
            placeholder_anim.markdown(f'<h4 style="text-align:center; color:#0B1E36; font-weight:400;">⏱️ BUSCANDO CÉDULA: {num_falso:02d}</h4>', unsafe_allow_html=True)
            time.sleep(0.08)
        placeholder_anim.empty()
        
        st.session_state.cedula_activa = random.randint(1, 2)
        st.rerun()

    st.write('---')
    st.markdown('### 📊 Evaluación y Nota Estimada')
    if st.session_state.total_respondidas > 0:
        porcentaje = (st.session_state.respuestas_correctas / st.session_state.total_respondidas) * 100
        nota = 1.0 + (porcentaje * 0.06)
        st.info(f'Preguntas: {st.session_state.total_respondidas} | Aciertos: {st.session_state.respuestas_correctas}')
        st.metric(label='PONDERACIÓN DE NOTA JURÍDICA USS', value=f'{nota:.1f}')
    else:
        st.text('Accione el Reloj para iniciar.')

with col_der:
    st.subheader('📋 Desglose Técnico en Pantalla')
    
    if st.session_state.cedula_activa:
        cedula_data = CEDULARIO_OFICIAL[st.session_state.cedula_activa]
        subpreguntas = cedula_data['subpreguntas']
