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

# Estilos CSS de Alta Gama para clonar milimétricamente la infografía COGNUSS 2
st.markdown('<style>.stApp { background-color: #FFFFFF; color: #0B1E36; font-family: "Segoe UI", Arial, sans-serif; padding-bottom: 80px; } .banner-superior-cognuss { background-color: #0F1E36; color: #FFFFFF; padding: 24px; border-radius: 4px; margin-bottom: 25px; text-align: left; border-left: 8px solid #4A90E2; } .banner-superior-cognuss h1 { font-size: 28px !important; color: #FFFFFF !important; margin: 0; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; } .banner-superior-cognuss h2 { font-size: 16px !important; color: #BACCDA !important; margin: 5px 0 0 0; font-weight: normal; letter-spacing: 1px; } .card-metodo-azul { background-color: #1F2E54; color: #FFFFFF; padding: 18px; border-radius: 6px; margin-bottom: 15px; } .card-metodo-blanca { background-color: #F4F6FA; border: 1px solid #D0D7DE; padding: 18px; border-radius: 6px; margin-bottom: 15px; } .esfera-piaget-total { background-color: #0F1E36; color: #FFFFFF; border: 10px solid #2B4C7E; border-radius: 50%; width: 320px; height: 320px; margin: 0 auto 20px auto; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0px 10px 25px rgba(0,0,0,0.15); } .box-minutero-uss { background-color: #F5FAF6; border-left: 6px solid #2ECC71; padding: 15px; border-radius: 4px; margin-bottom: 12px; } .box-horario-full { background-color: #F4F7FC; border-left: 6px solid #1A73E8; padding: 15px; border-radius: 4px; margin-bottom: 12px; } .box-segundero-uss { background-color: #FDF5F5; border-left: 6px solid #E74C3C; padding: 15px; border-radius: 4px; margin-bottom: 12px; } .desvanecer-texto-fino { animation: fadeOutCognuss 35s forwards; font-size: 15px; color: #111111; line-height: 1.5; } @keyframes fadeOutCognuss { 0% { opacity: 1; } 85% { opacity: 0.1; } 100% { opacity: 0; display: none; } } div.stButton > button { background-color: #1F2E54 !important; color: #FFFFFF !important; font-weight: bold !important; padding: 10px 20px !important; border-radius: 4px !important; width: 100%; border: none !important; } div.stButton > button:hover { background-color: #4A90E2 !important; }</style>', unsafe_allow_html=True)

# Base de datos indexada con el Cedulario USS Oficial (Las 14 Cédulas Completas)
CEDULARIO_MÉTODO_COGNUSS = {
    1: {
        'cedula': 'CEDULA 1.- El Derecho y la Moral. Normas de uso y trato social.',
        'concepto': 'La norma moral, características. Derecho y Moral: diferencias entre ambos órdenes. Normas de uso y trato social: concepto, características y diferencias con la norma jurídica.',
        'pregunta': 'Explaye sobre el paralelo estructural entre el Orden Jurídico y el Orden Moral respecto a los criterios de Bilateralidad/Unilateralidad y Coercibilidad/Incoercibilidad.',
        'fina': 'El Derecho regula la conducta intersubjetiva externa mediante la BILATERALIDAD (concede facultades recíprocas para exigir el cumplimiento) y la COERCIBILIDAD (potestad legítima del Estado para usar la fuerza pública). En contraposición, la Moral opera de manera UNILATERAL (impone deberes al sujeto sin otorgar derechos correlativos a un tercero) e INCOERCIBLE (su cumplimiento debe ser espontáneo y carece de sanción física institucionalizada).'
    },
    2: {
        'cedula': 'CEDULA 2.- La norma jurídica.',
        'concepto': 'Características. Clasificación entre normas jurídicas imperativas y permisivas. Estructura lógica de la norma jurídica.',
        'pregunta': 'Explique técnicamente la clasificación de las normas jurídicas imperativas frente a las permisivas ante el margen de la voluntad particular.',
        'fina': 'Las Normas Imperativas mandan o prohíben de forma absoluta e inmodificable por el acuerdo de particulares (orden público), mientras que las Normas Permisivas otorgan un derecho subjetivo o facultad lícita donde el titular decide libremente si ejerce la acción o renuncia a ella.'
    },
    3: {
        'cedula': 'CEDULA 3.- Vigencia, validez y eficacia del Derecho positivo.',
        'concepto': 'Vigencia: concepto, momentos. Derogación de la ley. Validez: doctrinas de legitimidad (Iusnaturalismo e Iuspositivismo). Eficacia.',
        'pregunta': 'Describa exhaustivamente la clasificación jurídica de la Derogación de la Ley en el ordenamiento chileno.',
        'fina': 'La derogación es la pérdida de vigencia de una ley por una posterior. Se clasifica en EXPRESA (cuando la nueva ley lo indica textualmente) o TÁCITA (cuando hay incompatibilidad absoluta de contenidos). Asimismo, puede ser TOTAL (anula la integridad del cuerpo legal preexistente) o PARCIAL (elimina solo ciertos artículos manteniendo el resto vigente).'
    },
    4: {
        'cedula': 'CEDULA 4.- La plenitud hermética del ordenamiento jurídico y las lagunas del Derecho.',
        'concepto': 'Introducción constitucional: principio de inexcusabilidad. Concepto de plenitud hermética. Lagunas del Derecho y solución judicial. Conflicto entre normas.',
        'pregunta': '¿Qué mandata el principio constitucional de inexcusabilidad (Art. 76 CPR) a los magistrados y cómo deben integrar las lagunas?',
        'fina': 'Consagrado en el Art. 76 de la Constitución, obliga a los jueces a resolver los conflictos sometidos a su conocimiento formal, sin poder excusarse aun por falta de ley expresa. Para solucionar las lagunas, el juez debe integrar el sistema recurriendo de forma secuencial a la analogía jurídica, la equidad natural y los principios generales del derecho.'
    },
    5: {
        'cedula': 'CEDULA 5.- Fuentes del ordenamiento jurídico.',
        'concepto': 'Concepto y tipos de fuente (materiales y formales). Clasificación de fuentes formales. La ley: concepto, elementos, características y efectos.',
        'pregunta': 'Establezca la diferencia de naturaleza entre las Fuentes Materiales y las Fuentes Formales del Derecho.',
        'fina': 'Las Fuentes Materiales son los factores, hechos sociales, políticos, morales o económicos (metajurídicos) que determinan el contenido de la norma. Las Fuentes Formales son los actos y procedimientos técnico-institucionales (ley, costumbre, jurisprudencia) mediante los cuales se manifiesta el derecho con fuerza obligatoria.'
    },
    6: {
        'cedula': 'CEDULA 6.- La costumbre.',
        'concepto': 'La costumbre: concepto y elementos. La costumbre en el Derecho Civil, Derecho Comercial, Derecho Internacional Público, Derecho Penal y Derecho Procesal.',
        'pregunta': '¿Cuál es el valor legal exacto de la costumbre dentro del Derecho Civil chileno en comparación al Derecho Comercial?',
        'fina': 'En el Derecho Civil, según el Artículo 2 del Código Civil, la costumbre solo constituye derecho cuando la propia ley se remite expresamente a ella (secundum legem). En cambio, en el Derecho Comercial, posee valor en silencio de la ley (praeter legem) cuando reúne los requisitos formales del artículo 4° del Código de Comercio.'
    },
    7: {
        'cedula': 'CEDULA 7.- La jurisprudencia y la doctrina, como fuentes formales del Derecho.',
        'concepto': 'La jurisprudencia: concepto, la norma del Código Civil and la práctica de los tribunales chilenos. La doctrina y la discusión sobre su carácter.',
        'pregunta': 'Explique el alcance del Efecto Relativo de las sentencias judiciales en Chile conforme al artículo 3° inciso 2° del Código Civil.',
        'fina': 'Las sentencias judiciales dictadas por los tribunales chilenos poseen fuerza obligatoria de manera estricta y exclusiva respecto de las partes que intervinieron en ese litigio específico. En Chile no rige el precedente obligatorio automático anglosajón, por lo que los fallos no sientan ley general.'
    },
    8: {
        'cedula': 'CEDULA 8. La Relación Jurídica.',
        'concepto': 'Concepto y elementos. La persona, sujeto de la relación jurídica. La persona natural. Principio y fin de su existencia.',
        'pregunta': 'Mencione y explique las condiciones simultáneas requeridas para el principio de existencia legal de la persona natural (Art. 74 CC).',
        'fina': 'Para que comience la existencia legal de la persona natural se exigen tres requisitos concurrentes: 1) Que la criatura nazca viva; 2) Que se separe completamente de su madre; y 3) Haber sobrevivido a dicha separación un momento siquiera (los lazos del cordón umbilical deben ser cortados sin que la criatura muera en el acto).'
    },
    9: {
        'cedula': 'CEDULA 9. La persona jurídica.',
        'concepto': 'Concepto. Tipos de personas jurídicas (Público y Privado). Responsabilidad civil: contractual y extracontractual. Responsabilidad penal: Ley N° 21.595.',
        'pregunta': '¿Cómo se subclasifican las personas jurídicas de Derecho Privado según sus fines estructurales?',
        'fina': 'Se dividen estrictamente en entidades CON fines de lucro (Sociedades Comerciales como Colectivas, Anónimas, de Responsabilidad Limitada y SpA, donde el objeto es repartir utilidades entre socios) y entidades SIN fines de lucro (Corporaciones y Fundaciones, donde los excedentes se reinvierten en el objeto de beneficencia).'
    },
    10: {
        'cedula': 'CEDULA 10.- Derechos reales y derechos personales.',
        'concepto': 'Derecho real: concepto y principales derechos reales (dominio o propiedad, herencia, usufructo, uso y habitación). Derecho personal: concepto y elementos.',
        'pregunta': 'Defina el concepto legal de Derecho Real según lo estipulado de forma exacta en el Artículo 577 del Código Civil.',
