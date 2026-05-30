import streamlit as st
import random
import time
from datetime import datetime

# 1. CONTROL DE CADUCIDAD REQUERIDO (30 de Junio de 2026)
FECHA_LIMITE = datetime(2026, 6, 30, 23, 59, 59)
if datetime.now() > FECHA_LIMITE:
    st.error('❌ LA LICENCIA DE ESTA APLICACIÓN HA CADUCADO (30 DE JUNIO DE 2026). CONTACTE AL ADMINISTRADOR.')
    st.stop()

st.set_page_config(page_title='RELOJ COGNUSS 2 - EXAMINADOR IA', layout='wide')

# Estilos CSS de Alta Relojería basados fielmente en la infografía Cognuss 2
st.markdown(
    """
    <style>
    .stApp { background-color: #FFFFFF; color: #0F1E36; font-family: "Segoe UI", sans-serif; padding-bottom: 80px; }
    .banner-superior { background-color: #0F1E36; color: white; padding: 20px; border-radius: 4px; margin-bottom: 20px; }
    .esfera-total { background-color: #0F1E36; color: #FFFFFF; border: 10px solid #2B4C7E; border-radius: 50%; width: 280px; height: 280px; margin: 0 auto; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0px 8px 20px rgba(0,0,0,0.15); }
    .box-minutero { background-color: #F5FAF6; border-left: 6px solid #2ECC71; padding: 18px; margin-bottom: 15px; border-radius: 4px; }
    .box-horario { background-color: #F4F7FC; border-left: 6px solid #1A73E8; padding: 18px; margin-bottom: 15px; border-radius: 4px; }
    .box-segundero { background-color: #FDF5F5; border-left: 6px solid #E74C3C; padding: 18px; margin-bottom: 15px; border-radius: 4px; }
    .desvanecer-texto { animation: fadeOut 35s forwards; font-size: 15px; color: #111111; line-height: 1.5; }
    @keyframes fadeOut { 0% { opacity: 1; } 85% { opacity: 0.1; } 100% { opacity: 0; display: none; } }
    div.stButton > button { background-color: #0F1E36 !important; color: white !important; font-weight: bold !important; }
    </style>
    """, 
    unsafe_allow_html=True
)

# Base de datos indexada con el temario LITERAL completo de las 14 Cédulas USS
CEDULARIO_LITERAL = {
    1: {
        'cedula_full': 'CEDULA 1.- El Derecho y la Moral. Normas de uso y trato social. 1.1. La norma moral, características. 1.2. Derecho y Moral: diferencias entre ambos órdenes. 1.3. Normas de uso y trato social: a) concepto. b) características y diferencias con la norma jurídica.',
        'subpreguntas': [
            {'sub': '1.1', 'pregunta': 'Explaye sobre la norma moral y describa detalladamente sus características esenciales.', 'fina': 'La norma moral es UNILATERAL (no confiere derechos a terceros), INTERIOR (valora la intención), INCOERCIBLE (cumplimiento voluntario sin fuerza estatal) y AUTÓNOMA (autoimpuesta).'},
            {'sub': '1.2', 'pregunta': 'Establezca las diferencias fundamentales entre el orden del Derecho y el orden de la Moral.', 'fina': 'El Derecho es bilateral, exterior, coercible y heterónomo. La Moral es unilateral, interior, incoercible y autónoma.'},
            {'sub': '1.3', 'pregunta': 'Defina las normas de uso y trato social, sus características y diferencias con la norma jurídica.', 'fina': 'Son prescripciones de decoro exterior, incoercibles y heterónomas. Se diferencian del Derecho porque carecen de coacción institucional estatal.'}
        ]
    },
    2: {
        'cedula_full': 'CEDULA 2.- La norma jurídica. 2.1. Características. 2.2. Clasificación entre normas jurídicas imperativas y permisivas. 2.3. Estructura lógica de la norma jurídica',
        'subpreguntas': [
            {'sub': '2.1', 'pregunta': 'Analice las características esenciales de la norma jurídica.', 'fina': 'Es bilateral (correlativa), exterior (regula actos), coercible (fuerza pública estatal legítima) y heterónoma (dictada por un tercero).'},
            {'sub': '2.2', 'pregunta': 'Explique la clasificación de normas jurídicas imperativas frente a las permisivas.', 'fina': 'Imperativas mandan o prohíben absolutamente limitando la autonomía; Permisivas conceden una facultad o derecho renunciable.'},
            {'sub': '2.3', 'pregunta': 'Describa la estructura lógica interna de una norma jurídica ordinaria.', 'correcta': 'Se estructura mediante un juicio hipotético: un Supuesto de Hecho (hipótesis condicional) y una Consecuencia Jurídica (efecto o sanción).', 'fina': 'Se compone de un Supuesto de Hecho (condición normativa) y una Consecuencia Jurídica (sanción, efecto o nacimiento de un derecho).'}
        ]
    },
    3: {
        'cedula_full': 'CEDULA 3.- Vigencia, validez y eficacia del Derecho positivo. 3.1. Vigencia a) concepto b) momento de la vigencia. c) la derogación de la ley: concepto y clasificación. 3.2. Validez a) concepto b) fundamentos de la validez del Derecho y presupuestos últimos de su legitimidad: en qué consisten las dos principales doctrinas. 3.3. Eficacia: concepto.',
        'subpreguntas': [
            {'sub': '3.1', 'pregunta': 'Defina vigencia, momento de inicio y la clasificación jurídica de la derogación legal en Chile.', 'fina': 'Vigencia es la fuerza obligatoria tras la publicación. Derogación es la pérdida de esta; puede ser expresa o tácita, total o parcial.'},
            {'sub': '3.2', 'pregunta': 'Explique el concepto de validez y los fundamentos de legitimidad según el Iusnaturalismo y el Iuspositivismo.', 'fina': 'Validez es conformidad con las normas jerárquicas superiores. El Iusnaturalismo fundamenta la legitimidad en la justicia/moral intrínseca; el Iuspositivismo en la legalidad formal.'},
            {'sub': '3.3', 'pregunta': 'Defina detalladamente el concepto técnico de eficacia dentro del Derecho positivo.', 'fina': 'Es una condición fáctica: representa el grado efectivo de cumplimiento, observancia y aplicación real de la norma por parte de sus destinatarios y tribunales.'}
        ]
    },
    4: {
        'cedula_full': 'CEDULA 4.- La plenitud hermética del ordenamiento jurídico y las lagunas del Derecho. 4.1. Introducción constitucional: principio de inexcusabilidad. 4.2 Concepto de plenitud hermética del ordenamiento jurídico. 4.3. Casos en que se observan lagunas del Derecho; solución judicial. 4.4. Conflicto entre normas jurídicas positivas (del mismo nivel jerárquico y de diverso nivel jerárquico): criterios de solución judicial.',
        'subpreguntas': [
            {'sub': '4.1', 'pregunta': 'Explique el Principio de Inexcusabilidad consagrado en el Artículo 76 de la Constitución.', 'fina': 'Establece que reclamada la intervención de los tribunales en forma legal y en negocios de su competencia, no pueden excusarse de fallar ni aun por falta de ley.'},
            {'sub': '4.2', 'pregunta': 'Defina el concepto doctrinal de la plenitud hermética del ordenamiento jurídico.', 'fina': 'Es el postulado que afirma que el sistema legal es completo y autosuficiente, conteniendo las herramientas normativas o de integración para resolver todo conflicto.'},
            {'sub': '4.3', 'pregunta': 'Identifique cuándo se observan lagunas del Derecho y cuál es su solución por medio de la integración.', 'fina': 'Hay lagunas ante un vacío legal. El juez integra el ordenamiento aplicando jerárquicamente la analogía jurídica, la equidad natural y los principios generales.'},
            {'sub': '4.4', 'pregunta': 'Detalle los criterios de solución judicial ante el conflicto entre normas jurídicas positivas de igual y diverso nivel.', 'fina': 'Se aplican los principios clásicos: Jerarquía (ley superior deroga inferior), Temporalidad (ley posterior deroga anterior) y Especialidad (ley especial prima sobre general).'}
        ]
    },
    5: {
        'cedula_full': 'CEDULA 5.- Fuentes del ordenamiento jurídico. 5.1. Concepto y tipos de fuente (materiales y formales) 5.2. Fuentes formales del Derecho: clasificación. 5.3. La ley: a) concepto b) elementos c) características d) efectos de la ley en cuanto al espacio e) efectos de la ley en cuanto al tiempo.',
        'subpreguntas': [
            {'sub': '5.1', 'pregunta': 'Establezca la diferencia entre Fuentes Materiales y Fuentes Formales del Derecho.', 'fina': 'Materiales son factores reales (sociales, políticos, morales) que determinan el contenido. Formales son los modos técnico-institucionales de manifestación obligatoria.'},
            {'sub': '5.2', 'pregunta': 'Mencione la clasificación general de las Fuentes Formales.', 'fina': 'Se clasifican principalmente en Ley (potestad legislativa), Costumbre, Jurisprudencia (fallos de tribunales) y la Doctrina (estudios jurídicos científicos).'},
            {'sub': '5.3', 'pregunta': 'Explaye sobre el concepto de ley, sus elementos, características y sus efectos en el tiempo y el espacio.', 'fina': 'Declaración de la voluntad soberana (Art 1 CC). Es universal y obligatoria. En el espacio rige la territorialidad; en el tiempo, la irretroactividad (Art 9 CC).'}
        ]
    },
    6: {
        'cedula_full': 'CEDULA 6.- La costumbre. 6.1. La costumbre a) concepto b) elementos. 6.2. La costumbre en el Derecho Civil, el Derecho Comercial, el Derecho Internacional Público, el Derecho Penal y el Derecho Procesal.',
        'subpreguntas': [
            {'sub': '6.1', 'pregunta': 'Defina el concepto de costumbre jurídica y desglose sus dos elementos constitutivos.', 'fina': 'Es la repetición constante de una conducta por el grupo social. Elementos: Material (repetición generalizada) y Espiritual/Opinio iuris (convicción de obligatoriedad).'},
            {'sub': '6.2', 'pregunta': 'Analice el valor legal de la costumbre en las distintas ramas del Derecho chileno.', 'fina': 'En Civil: solo según la ley (Art 2 CC). En Comercial: en silencio de ley (Art 4 CCom). En Penal: rechazada absolutamente por el principio de legalidad formal.'}
        ]
    },
    7: {
        'cedula_full': 'CEDULA 7.-La jurisprudencia y la doctrina, como fuentes formales del Derecho. 7.1. La jurisprudencia a) concepto b) la norma del Código Civil y la práctica de los tribunales chilenos. 7.2. La doctrina a) concepto b) la discusión sobre su carácter de fuente formal del Derecho.',
        'subpreguntas': [
