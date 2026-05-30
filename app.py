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

# Estilos CSS exactos de la infografía oficial para estructurar los tres componentes
st.markdown('<style>.stApp { background-color: #FFFFFF; color: #0F1E36; font-family: "Segoe UI", sans-serif; padding-bottom: 80px; } .banner-superior { background-color: #0F1E36; color: white; padding: 20px; border-radius: 4px; margin-bottom: 20px; } .esfera-total { background-color: #0F1E36; color: #FFFFFF; border: 10px solid #2B4C7E; border-radius: 50%; width: 280px; height: 280px; margin: 0 auto; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0px 8px 20px rgba(0,0,0,0.15); } .box-minutero { background-color: #F5FAF6; border-left: 6px solid #2ECC71; padding: 18px; margin-bottom: 15px; border-radius: 4px; } .box-horario { background-color: #F4F7FC; border-left: 6px solid #1A73E8; padding: 18px; margin-bottom: 15px; border-radius: 4px; } .box-segundero { background-color: #FDF5F5; border-left: 6px solid #E74C3C; padding: 18px; margin-bottom: 15px; border-radius: 4px; } .desvanecer-texto { animation: fadeOut 35s forwards; font-size: 15px; color: #111111; line-height: 1.5; } @keyframes fadeOut { 0% { opacity: 1; } 85% { opacity: 0.1; } 100% { opacity: 0; display: none; } } div.stButton > button { background-color: #0F1E36 !important; color: white !important; font-weight: bold !important; }</style>', unsafe_allow_html=True)

# Base de datos unificada sintácticamente al 100% sin mezclas de llaves
CEDULARIO = {
    1: {
        'cedula_full': 'CEDULA 1.- El Derecho y la Moral. Normas de uso y trato social. 1.1. La norma moral, características. 1.2. Derecho y Moral: diferencias entre ambos órdenes. 1.3. Normas de uso y trato social: a) concepto. b) características y diferencias con la norma jurídica.',
        'subpreguntas': [{'sub': '1.1', 'pregunta': 'Explaye sobre la norma moral y describa detalladamente sus características esenciales.', 'fina': 'La norma moral es UNILATERAL (no confiere derechos a terceros), INTERIOR (valora la intención), INCOERCIBLE (cumplimiento voluntario sin fuerza estatal) y AUTÓNOMA (autoimpuesta).'}]
    },
    2: {
        'cedula_full': 'CEDULA 2.- La norma jurídica. 2.1. Características. 2.2. Clasificación entre normas jurídicas imperativas y permisivas. 2.3. Estructura lógica de la norma jurídica',
        'subpreguntas': [{'sub': '2.1', 'pregunta': 'Analice las características esenciales de la norma jurídica.', 'fina': 'Es bilateral (correlativa), exterior (regula actos), coercible (fuerza pública estatal legítima) y heterónoma (dictada por un tercero).'}]
    },
    3: {
        'cedula_full': 'CEDULA 3.- Vigencia, validez y eficacia del Derecho positivo. 3.1. Vigencia a) concepto b) momento de la vigencia. c) la derogación de la ley: concepto y clasificación. 3.2. Validez a) concepto b) fundamentos de la validez del Derecho.',
        'subpreguntas': [{'sub': '3.1', 'pregunta': 'Defina vigencia, momento de inicio y la clasificación jurídica de la derogación legal en Chile.', 'fina': 'Vigencia es la fuerza obligatoria tras la publicación. Derogación es la pérdida de esta; puede ser expresa o tácita, total o parcial.'}]
    },
    4: {
        'cedula_full': 'CEDULA 4.- La plenitud hermética del ordenamiento jurídico y las lagunas del Derecho. 4.1. Introducción constitucional: principio de inexcusabilidad. 4.2 Concepto de plenitud hermética. 4.3. Casos de lagunas; solución judicial.',
        'subpreguntas': [{'sub': '4.1', 'pregunta': 'Explique el Principio de Inexcusabilidad consagrado en el Artículo 76 de la Constitución.', 'fina': 'Establece que reclamada la intervención de los tribunales en forma legal y en negocios de su competencia, no pueden excusarse de fallar ni aun por falta de ley.'}]
    },
    5: {
        'cedula_full': 'CEDULA 5.- Fuentes del ordenamiento jurídico. 5.1. Concepto and tipos de fuente (materiales y formales) 5.2. Fuentes formales del Derecho: clasificación. 5.3. La ley: a) concepto b) elementos c) características d) efectos.',
        'subpreguntas': [{'sub': '5.1', 'pregunta': 'Establezca la diferencia entre Fuentes Materiales y Fuentes Formales del Derecho.', 'fina': 'Materiales son factores reales (sociales, políticos, morales) que determinan el contenido. Formales son los modos técnico-institucionales de manifestación obligatoria.'}]
    },
    6: {
        'cedula_full': 'CEDULA 6.- La costumbre. 6.1. La costumbre a) concepto b) elementos. 6.2. La costumbre en el Derecho Civil, el Derecho Comercial, el Derecho Internacional Público, el Derecho Penal y el Derecho Procesal.',
        'subpreguntas': [{'sub': '6.1', 'pregunta': 'Defina el concepto de costumbre jurídica y desglose sus dos elementos constitutivos.', 'fina': 'Es la repetición constante de una conducta por el grupo social. Elementos: Material (repetición generalizada) y Espiritual (convicción de obligatoriedad).'}]
    },
    7: {
        'cedula_full': 'CEDULA 7.-La jurisprudencia y la doctrina, como fuentes formales del Derecho. 7.1. La jurisprudencia a) concepto b) la norma del Código Civil. 7.2. La doctrina a) concepto b) discusión sobre su carácter.',
        'subpreguntas': [{'sub': '7.1', 'pregunta': 'Explique el concepto de jurisprudencia y el alcance del Efecto Relativo de las sentencias (Art. 3 inc 2 CC).', 'fina': 'Jurisprudencia es el hábito de fallar de los tribunales. El Art 3 CC fija el efecto relativo: las sentencias solo obligan a las partes que intervinieron en el juicio.'}]
    },
    8: {
        'cedula_full': 'CEDULA 8. La Relación Jurídica. 8.1. a) concepto b) elementos 8.2. La persona, sujeto de la relación jurídica. La persona natural. Principio y fin de su existencia.',
        'subpreguntas': [{'sub': '8.2', 'pregunta': 'Explaye sobre la persona natural, detallando legalmente el principio y fin de su existencia.', 'fina': 'Existencia natural inicia con la concepción; existencia legal al nacer vivo y separarse (Art 74 CC). El fin de la existencia se produce por la muerte real o presunta.'}]
    },
    9: {
        'cedula_full': 'CEDULA 9. La persona jurídica. 9.1. Concepto. 9.2. Tipos de personas jurídicas. a) de Derecho Público y b) de Derecho Privado. 9.3. Responsabilidad civil. 9.4. Responsabilidad penal de las personas jurídicas. LEY N° 21.595.',
        'subpreguntas': [{'sub': '9.1', 'pregunta': 'Defina el concepto de persona jurídica según el ordenamiento civil.', 'fina': 'Ente ficticio capaz de ejercer derechos, contraer obligaciones civiles y ser representado judicial y extrajudicialmente (Art 545 del Código Civil).'}]
    },
    10: {
        'cedula_full': 'CEDULA 10.- Derechos reales y derechos personales. 10.1. Derecho real. Concepto. Principales derechos reales. 10.2. Derecho personal. Concepto. Elementos.',
        'subpreguntas': [{'sub': '10.1', 'pregunta': 'Defina Derecho Real (Art. 577 CC) y enumere las facultades que confiere el derecho de dominio.', 'fina': 'El que tenemos sobre una cosa sin respecto a determinada persona. El dominio confiere tres facultades jurídicas absolutas: Uso, Goce y Disposición.'}]
    },
    11: {
        'cedula_full': 'CEDULA 11.- Límites en el ejercicio de los derechos subjetivos y el abuso del derecho. 11.1. Limitaciones intrínsecas y extrínsecas de los derechos. a) Limitaciones intrínsecas: la buena fe. b) Limitaciones extrínsecas.',
        'subpreguntas': [{'sub': '11.1', 'pregunta': 'Explique el fenómeno técnico del Abuso del Derecho y diferencie las limitaciones intrínsecas de las extrínsecas.', 'fina': 'Ocurre al ejercer un derecho lícito desviándose de su finalidad social para dañar. Intrínsecas nacen de la naturaleza del derecho (buena fe); Extrínsecas del derecho ajeno.'}]
    },
    12: {
        'cedula_full': 'CEDULA 12. Los bienes (o cosas). Clasificación. 12.1. Bienes muebles: por naturaleza y por anticipación. 12.2. Bienes inmuebles. Concepto. a) Bienes inmuebles por naturaleza y por adherencia o destinación.',
        'subpreguntas': [{'sub': '12.1', 'pregunta': '¿Qué define a los bienes muebles por anticipación regulados en el artículo 571 del Código Civil?', 'fina': 'Son aquellos productos de los inmuebles y las cosas accesorias a ellos que se consideran anticipadamente como bienes muebles, aun antes de su separación física, para el solo efecto de constituir derechos sobre ellos.'}]
    },
    13: {
        'cedula_full': 'CEDULA 13. 13.1. Diferente régimen jurídico de los bienes muebles e inmuebles. 13.2. Cosas registrables y no registrables. 13.3. Cosas (o bienes) específicas y genéricas.',
        'subpreguntas': [{'sub': '13.1', 'pregunta': 'Compare técnicamente el régimen jurídico de los bienes muebles frente al de los inmuebles.', 'fina': 'Inmuebles exigen solemnidades formales (Escritura Pública y Registro CBR). Muebles son consensuales y se transfieren por tradición simple.'}]
    },
    14: {
        'cedula_full': 'CEDULA 14. Bienes o cosas comerciables e incomerciables. 14.1. Cosas comerciables e incomerciables (subclasificación) . 14.2. Bienes nacionales de uso público (concesiones) y bienes fiscales (el Fisco).',
        'subpreguntas': [{'sub': '14.2', 'pregunta': 'Establezca el paralelo conceptual definitivo entre los Bienes Nacionales de Uso Público y los Bienes Fiscales.', 'fina': 'Uso Público pertenecen a la nación y son incomerciables, inalienables e imprescriptibles (plazas). Fiscales son propiedad privada del Estado y son comerciables.'}]
    }
}

if 'posicion' not in st.session_state:
    st.session_state.posicion = None
if 'sub_activa' not in st.session_state:
    st.session_state.sub_activa = None
