import streamlit as st
import random
import time
from datetime import datetime

# CONTROL DE CADUCIDAD REQUERIDO (30 de Junio de 2026)
FECHA_LIMITE = datetime(2026, 6, 30, 23, 59, 59)
if datetime.now() > FECHA_LIMITE:
    st.error("❌ LA LICENCIA DE ESTA APLICACIÓN HA CADUCADO (30 DE JUNIO DE 2026).")
    st.stop()

st.set_page_config(page_title="COGNUSS 2 - TEORÍA DEL DERECHO", layout="centered")

# Estilos CSS de ventanas rectangulares secuenciales limpias
st.markdown(
    """
    <style>
    .stApp { background-color: #FFFFFF; color: #0F1E36; font-family: sans-serif; }
    .rect-banner { background-color: #0F1E36; color: white; padding: 20px; border-radius: 4px; text-align: center; margin-bottom: 20px; }
    .rect-cedula { background-color: #F5FAF6; border-left: 8px solid #2ECC71; padding: 20px; margin-bottom: 15px; border-radius: 4px; }
    .rect-pregunta { background-color: #F4F7FC; border-left: 8px solid #1A73E8; padding: 20px; margin-bottom: 15px; border-radius: 4px; }
    .rect-respuesta { background-color: #FDF5F5; border-left: 8px solid #E74C3C; padding: 20px; margin-bottom: 15px; border-radius: 4px; }
    .desvanecer-texto { animation: fadeOut 25s forwards; font-size: 15px; color: #111111; line-height: 1.5; }
    @keyframes fadeOut { 0% { opacity: 1; } 85% { opacity: 0.1; } 100% { opacity: 0; display: none; } }
    </style>
    """, 
    unsafe_allow_html=True
)

CEDULAS_TEXTO = [
    "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social. 1.1. La norma moral, características. 1.2. Derecho y Moral: diferencias entre ambos órdenes. 1.3. Normas de uso y trato social: a) concepto. b) características y diferencias con la norma jurídica.",
    "CÉDULA 2.- La norma jurídica. 2.1. Características. 2.2. Clasificación entre normas jurídicas imperativas y permisivas. 2.3. Estructura lógica de la norma jurídica.",
    "CÉDULA 3.- Vigencia, validez y eficacia del Derecho positivo. 3.1. Vigencia a) concepto b) momento de la vigencia. c) la derogación de la ley: concepto y clasificación. 3.2. Validez a) concepto b) fundamentos de la validez del Derecho y presupuestos últimos de su legitimidad: en qué consisten las dos principales doctrinas. 3.3. Eficacia: concepto.",
    "CÉDULA 4.- La plenitud hermética del ordenamiento jurídico y las lagunas del Derecho. 4.1. Introducción constitucional: principio de inexcusabilidad. 4.2 Concepto de plenitud hermética del ordenamiento jurídico. 4.3. Casos en que se observan lagunas del Derecho; solución judicial. 4.4. Conflicto entre normas jurídicas positivas (del mismo nivel jerárquico y de diverso nivel jerárquico): criterios de solución judicial.",
    "CÉDULA 5.- Fuentes del ordenamiento jurídico. 5.1. Concepto y tipos de fuente (materiales y formales) 5.2. Fuentes formales del Derecho: clasificación. 5.3. La ley: a) concepto b) elementos c) características d) efectos de la ley en cuanto al espacio e) efectos de la ley en cuanto al tiempo.",
    "CÉDULA 6.- La costumbre. 6.1. La costumbre a) concepto b) elementos. 6.2. La costumbre en el Derecho Civil, el Derecho Comercial, el Derecho Internacional Público, el Derecho Penal y el Derecho Procesal.",
    "CÉDULA 7.- La jurisprudencia y la doctrina, como fuentes formales del Derecho. 7.1. La jurisprudencia a) concepto b) la norma del Código Civil y la práctica de los tribunales chilenos. 7.2. La doctrina a) concepto b) la discusión sobre su carácter de fuente formal del Derecho.",
    "CÉDULA 8.- La Relación Jurídica. 8.1. a) concepto b) elementos 8.2. La persona, sujeto de la relación jurídica. La persona natural. Principio y fin de su existencia.",
    "CÉDULA 9.- La persona jurídica. 9.1. Concepto. 9.2. Tipos de personas jurídicas. a) de Derecho Público y b) de Derecho Privado. 9.3. Responsabilidad de las personas jurídicas: a) responsabilidad civil: contractual y extracontractual (delictual o cuasi delictual). Alcance de la responsabilidad de las personas jurídicas por actos de sus dependientes. 9.4. Responsabilidad penal de las personas jurídicas. LEY N° 21.595.",
    "CÉDULA 10.- Derechos reales y derechos personales. 10.1. Derecho real. Concepto. Principales derechos reales (derecho de dominio o propiedad, derecho real de herencia), demás derechos reales (de usufructo, de uso y habitación) conceptos y facultades que comprende cada uno. 10.2. Derecho personal. Concepto. Elementos.",
    "CÉDULA 11.- Límites en el ejercicio de los derechos subjetivos y el abuso del derecho. 11.1. Limitaciones intrínsecas y extrínsecas de los derechos. a) Limitaciones intrínsecas: la buena fe, otras limitaciones. b) Limitaciones extrínsecas.",
    "CÉDULA 12.- Los bienes (o cosas). Clasificación. 12.1. Bienes muebles: por naturaleza y por anticipación. Bienes muebles semovientes e inanimados. Registro de los bienes muebles. 12.2. Bienes inmuebles. Concepto. a) Bienes inmuebles por naturaleza y por adherencia o destinación.",
    "CÉDULA 13.- Diferente régimen jurídico de los bienes muebles e inmuebles. 13.2. Cosas registrables y no registrables. 13.3. Cosas (o bienes) específicas y genéricas.",
    "CÉDULA 14.- Bienes o cosas comerciables e incomerciables. 14.1. Cosas comerciables e incomerciables (subclasificación). 14.2. Bienes nacionales de uso público (concesiones) y bienes fiscales (el Fisco)."
]

PREGUNTAS = [
    "Explaye sobre el paralelo estructural entre el Derecho y la Moral conforme a los criterios de Bilateralidad, Exterioridad, Heteronomía y Coercibilidad. Desglose las Normas de Uso Social.",
    "Diferencie las Normas Imperativas de las Normas Permisivas en el ordenamiento civil chileno. ¿Cuál es el efecto de la infracción y el margen de la voluntad?",
    "Explique las clasificaciones de la Derogación de la Ley (Expresa, Tácita, Total, Parcial) y diferencie las doctrinas de validez Iusnaturalista e Iuspositivista.",
    "Defina el Principio de Inexcusabilidad (Art. 76 inc 2 CPR) y explique el concepto de Plenitud Hermética junto a los mecanismos de integración ante Lagunas y Antinomias.",
    "Establezca el paralelo conceptual entre Fuentes Materiales y Formales, y explique los efectos de la ley en el Espacio (Territorialidad) y el Tiempo (Irretroactividad).",
    "Defina Costumbre Jurídica, sus elementos (Objetivo y Subjetivo) y analice su valor en el Derecho Civil (Art. 2 CC) frente al Derecho Comercial (Art. 4 CCom) y Penal.",
    "Explique el concepto de Jurisprudencia frente al de Doctrina, analizando el alcance del Efecto Relativo de las sentencias judiciales (Art. 3 inc. 2° CC) en Chile.",
    "Defina Relación Jurídica, sus elementos constitutivos y detalle las tres condiciones simultáneas exigidas para la Existencia Legal de la persona natural (Art. 74 CC).",
    "Defina Persona Jurídica (Art. 545 CC), diferencie las de Derecho Público de las de Privado y explique el régimen actual de su Responsabilidad Penal (Ley N° 21.595).",
    "Establezca el paralelo estructural entre Derechos Reales (Art. 577 CC) y Personales (Art. 578 CC), detallando el catálogo de derechos reales del Código Civil y sus facultades.",
    "Analice las limitaciones intrínsecas de los derechos subjetivos explayando sobre la Buena Fe Objetiva (Art. 1546 CC) y la doctrina del Abuso del Derecho.",
    "Clasifique los Bienes Muebles (Semovientes, Inanimados, Anticipación - Art. 571 CC) y los Bienes Inmuebles (Naturaleza, Adherencia, Destinación - Art. 570 CC).",
    "Compare el Régimen Jurídico de bienes muebles e inmuebles en cuanto a su Tradición (Art. 684 vs 686 CC), formalidades de venta, prescripción y garantías.",
    "Defina Cosas Comerciables e Incomerciables (Naturaleza y Destino), estableciendo el paralelo definitivo entre Bienes Nacionales de Uso Público y Bienes Fiscales (Art. 589 CC)."
]

RESPUESTAS = [
    "Derecho es Bilateral (concede facultades a terceros), Exterior (ejecución material), Heterónomo (dictado por el Estado) y Coercible (admite fuerza pública). Moral es Unilateral (impone deberes sin facultades), Interior (pureza de intención), Autónomo (conciencia libre) e Incoercible (sanción interna). Normas de uso social: origen de la norma en la sociedad civil de forma difusa, sanción es el rechazo social.",
    "Imperativas (y Prohibitivas): ordenan o prohíben absolutamente; no modificables por particulares; infracción causa nulidad absoluta o cárcel. Permisivas (o Facultativas): conceden una aptitud legítima u opción renunciable; no existe infracción si el sujeto opta por no usar la facultad legal.",
    "Derogación: Expresa (declaración explícita), Tácita (incompatibilidad), Total (elimina toda la ley), Parcial (elimina algunos incisos). Validez Iusnaturalista: se funda en la justicia material y principios morales universales; la Iuspositivista en la legalidad formal del órgano competente y proceso regular.",
    "Inexcusabilidad (Art. 76 inc. 2° CPR): obliga a jueces a resolver conflictos aun sin ley expresa. Plenitud Hermética considera al sistema cerrado y completo. Las lagunas (vacíos legales) se integran mediante analogía, equidad y principios generales; las antinomias se resuelven por jerarquía, especialidad y temporalidad.",
    "Fuentes Materiales: factores sociales/morales que determinan el contenido. Formales: procedimientos con fuerza obligatoria. Espacio: Territorialidad (Art. 14 CC), obliga a todos los habitantes del territorio nacional. Tiempo: Irretroactividad (Art. 9 CC), la ley solo dispone para el futuro.",
    "Costumbre es la repetición constante con convicción de necesidad jurídica (Opinio Iuris). Elementos: Objetivo (práctica general uniforme) y Subjetivo (creencia de obligatoriedad). Derecho Civil: solo según la ley (Art. 2 CC). Comercial: en silencio de la ley (Art. 4 CCom). Penal: no tiene valor alguno por legalidad estricta.",
