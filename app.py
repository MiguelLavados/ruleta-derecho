import streamlit as st
import random
import time

st.set_page_config(page_title="RELOJ COGNUSS 2 - EXAMINADOR IA", layout="wide")

# Estilos CSS de la infografía oficial para estructurar Minutero, Horario y Segundero
st.markdown('<style>.stApp { background-color: #FFFFFF; color: #0F1E36; font-family: "Segoe UI", sans-serif; padding-bottom: 80px; } .banner-superior { background-color: #0F1E36; color: white; padding: 20px; border-radius: 4px; margin-bottom: 20px; } .esfera-total { background-color: #0F1E36; color: #FFFFFF; border: 10px solid #2B4C7E; border-radius: 50%; width: 280px; height: 280px; margin: 0 auto; display: flex; flex-direction: column; justify-content: center; align-items: center; box-shadow: 0px 8px 20px rgba(0,0,0,0.15); } .box-minutero { background-color: #F5FAF6; border-left: 6px solid #2ECC71; padding: 18px; margin-bottom: 15px; border-radius: 4px; } .box-horario { background-color: #F4F7FC; border-left: 6px solid #1A73E8; padding: 18px; margin-bottom: 15px; border-radius: 4px; } .box-segundero { background-color: #FDF5F5; border-left: 6px solid #E74C3C; padding: 18px; margin-bottom: 15px; border-radius: 4px; } .desvanecer-texto { animation: fadeOut 35s forwards; font-size: 15px; color: #111111; line-height: 1.5; } @keyframes fadeOut { 0% { opacity: 1; } 85% { opacity: 0.1; } 100% { opacity: 0; display: none; } } div.stButton > button { background-color: #0F1E36 !important; color: white !important; font-weight: bold !important; }</style>', unsafe_allow_html=True)

# Listas lineales independientes para evitar de forma absoluta errores de llaves abiertas
CEDULAS_TEXTO = [
    "CEDULA 1.- El Derecho y la Moral. Normas de uso y trato social. 1.1. La norma moral, características. 1.2. Derecho y Moral: diferencias entre ambos órdenes. 1.3. Normas de uso y trato social: a) concepto. b) características y diferencias con la norma jurídica.",
    "CEDULA 2.-La norma jurídica. 2.1. Características. 2.2. Clasificación entre normas jurídicas imperativas y permisivas. 2.3. Estructura lógica de la norma jurídica",
    "CEDULA 3.- Vigencia, validez y eficacia del Derecho positivo. 3.1. Vigencia a) concepto b) momento de la vigencia. c) la derogación de la ley: concepto y clasificación. 3.2. Validez a) concepto b) fundamentos de la validez del Derecho y presupuestos últimos de su legitimidad: en qué consisten las dos principales doctrinas. 3.3. Eficacia: concepto.",
    "CEDULA 4.- La plenitud hermética del ordenamiento jurídico y las lagunas del Derecho. 4.1. Introducción constitucional: principio de inexcusabilidad. 4.2 Concepto de plenitud hermética del ordenamiento jurídico. 4.3. Casos en que se observan lagunas del Derecho; solución judicial. 4.4. Conflicto entre normas jurídicas positivas (del mismo nivel jerárquico y de diverso nivel jerárquico): criterios de solución judicial.",
    "CEDULA 5.- Fuentes del ordenamiento jurídico. 5.1. Concepto y tipos de fuente (materiales y formales) 5.2. Fuentes formales del Derecho: clasificación. 5.3. La ley: a) concepto b) elementos c) características d) efectos de la ley en cuanto al espacio e) efectos de la ley en cuanto al tiempo.",
    "CEDULA 6.- La costumbre. 6.1. La costumbre a) concepto b) elementos. 6.2. La costumbre en el Derecho Civil, el Derecho Comercial, el Derecho Internacional Público, el Derecho Penal y el Derecho Procesal.",
    "CEDULA 7.-La jurisprudencia y la doctrina, como fuentes formales del Derecho. 7.1. La jurisprudencia a) concepto b) la norma del Código Civil y la práctica de los tribunales chilenos. 7.2. La doctrina a) concepto b) la discusión sobre su carácter de fuente formal del Derecho.",
    "CEDULA 8. La Relación Jurídica. 8.1. a) concepto b) elementos 8.2. La persona, sujeto de la relación jurídica. La persona natural. Principio y fin de su existencia.",
    "CEDULA 9. La persona jurídica. 9.1. Concepto. 9.2. Tipos de personas jurídicas. a) de Derecho Público y b) de Derecho Privado. 9.3. Responsabilidad de las personas jurídicas: a) responsabilidad civil: contractual y extracontractual (delictual o cuasi delictual). Alcance de la responsabilidad de las personas jurídicas por actos de sus dependientes. 9.4. Responsabilidad penal de las personas jurídicas. LEY N° 21.595.",
    "CEDULA 10.- Derechos reales y derechos personales. 10.1. Derecho real. Concepto. Principales derechos reales (derecho de dominio o propiedad, derecho real de herencia), demás derechos reales (de usufructo, de uso y habitación) conceptos y facultades que comprende cada uno. 10.2. Derecho personal. Concepto. Elementos.",
    "CEDULA 11.- Límites en el ejercicio de los derechos subjetivos y el abuso del derecho. 11.1. Limitaciones intrínsecas y extrínsecas de los derechos. a) Limitaciones intrínsecas: la buena fe, otras limitaciones. b) Limitaciones extrínsecas.",
    "CEDULA 12. Los bienes (o cosas). Clasificación. 12.1. Bienes muebles: por naturaleza y por anticipación. Bienes muebles semovientes e inanimados. Registro de los bienes muebles. 12.2. Bienes inmuebles. Concepto. a) Bienes inmuebles por naturaleza y por adherencia o destinación.",
    "CEDULA 13. 13.1. Diferente régimen jurídico de los bienes muebles e inmuebles. 13.2. Cosas registrables y no registrables. 13.3. Cosas (o bienes) específicas y genéricas.",
    "CEDULA 14. Bienes o cosas comerciables e incomerciables. 14.1. Cosas comerciables e incomerciables (subclasificación) . 14.2. Bienes nacionales de uso público (concesiones) y bienes fiscales (el Fisco)."
]

PREGUNTAS_MÉTODO = [
    "Explaye sobre el paralelo estructural entre el Orden Jurídico y el Orden Moral respecto a los criterios de Bilateralidad y Coercibilidad.",
    "Explique la estructura lógica interna de una norma jurídica ordinaria y la clasificación entre normas imperativas y permisivas.",
    "Describa la clasificación jurídica de la Derogación de la Ley en Chile y diferencie los conceptos de vigencia, validez y eficacia.",
    "Analice el principio constitucional de inexcusabilidad (Art. 76 CPR) y los mecanismos judiciales para integrar las lagunas del Derecho.",
    "Establezca las diferencias entre Fuentes Materiales y Formales, y explaye sobre los efectos de la ley en el tiempo y el espacio.",
    "¿Cuál es el valor legal exacto de la costumbre dentro del Derecho Civil chileno en comparación al Derecho Comercial y Penal?",
    "Explique el alcance del Efecto Relativo de las sentencias judiciales (Art. 3 inc 2 CC) y el carácter formal de la doctrina.",
    "Mencione los requisitos de existencia legal de la persona natural (Art. 74 CC) y analice los elementos de la relación jurídica.",
    "Diferencie las personas jurídicas de Derecho Público y Privado, y explique su responsabilidad penal según la Ley N° 21.595.",
    "Defina Derecho Real según el Artículo 577 del Código Civil y enumere las facultades que comprende el derecho de dominio.",
    "Explique en qué consiste la doctrina del Abuso del Derecho y diferencie las limitaciones intrínsecas de las extrínsecas.",
    "Clasifique los bienes inmuebles (naturaleza, adherencia, destinación) y los bienes muebles por anticipación (Art. 571 CC).",
    "Compare el régimen jurídico de bienes muebles e inmuebles respecto a su tradición, registro formal y solemnidades de venta.",
    "Diferencie los Bienes Nacionales de Uso Público de los Bienes Fiscales respecto a su comerciabilidad y régimen de concesiones."
]

RESPUESTAS_FINAS = [
    "El Derecho es BILATERAL y COERCIBLE (uso legítimo de la fuerza estatal). La Moral es UNILATERAL e INCOERCIBLE (cumplimiento espontáneo).",
    "Imperativas mandan/prohíben absolutamente (orden público); Permisivas conceden facultades lícitas. Estructura: Supuesto y Consecuencia.",
    "Derogación: Expresa/Tácita, Total/Parcial. Vigencia: fuerza obligatoria publicada. Validez: legalidad formal. Eficacia: aplicación real.",
    "Inexcusabilidad obliga a fallar aun sin ley expresa. Integración judicial se realiza mediante analogía, equidad y principios generales.",
    "Fuentes Materiales: hechos sociales/políticos que determinan contenido. Formales: procedimientos con fuerza obligatoria (ley, costumbre).",
    "En Derecho Civil solo rige según la ley (Art 2 CC). En Derecho Comercial rige en silencio de la ley (Art 4 CCom). En Penal se prohíbe.",
    "Las sentencias judiciales poseen fuerza obligatoria de forma exclusiva respecto de las partes del juicio. No sientan ley general.",
    "Existencia legal exige: nacer vivo, separarse completamente de la madre y sobrevivir un momento siquiera a los lazos del cordón.",
    "Público actúan por potestad estatal; Privado por autonomía de voluntad. Ley 21.595 regula los delitos económicos corporativos directos.",
    "Derecho Real es el que tenemos sobre una cosa sin respecto a determinada persona (erga omnes). Dominio faculta Uso, Goce y Disposición.",
    "Abuso ocurre al ejercer un derecho lícito desviándose de su fin social para dañar a otro. Intrínsecas: buena fe. Extrínsecas: derecho ajeno.",
    "Muebles por anticipación son productos inmuebles considerados muebles antes de separarse para contratos. Inmuebles no se transportan.",
    "Inmuebles exigen solemnidad obligatoria por Escritura Pública e Inscripción CBR. Muebles son consensuales y de tradición simple.",
    "Bienes de Uso Público pertenecen a toda la nación y son incomerciables (calles). Fiscales son patrimonio privado del Estado y comerciables."
]

if 'posicion' not in st.session_state:
    st.session_state.posicion = None
if 'modo' not in st.session_state:
    st.session_state.modo = None

st.markdown('<div class="banner-superior"><h1>6️⃣ PRUEBA DE TEORÍA DEL DERECHO</h1><h2>14 PREGUNTAS — RELOJ COGNUSS 2 - EXAMINADOR IA</h2></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.8, 1, 1.2])

with col1:
