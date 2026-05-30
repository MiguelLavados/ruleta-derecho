import streamlit as st
import random
import time
from datetime import datetime

# CONTROL DE CADUCIDAD REQUERIDO
FECHA_LIMITE = datetime(2026, 6, 30, 23, 59, 59)
if datetime.now() > FECHA_LIMITE:
    st.error("❌ LA LICENCIA DE ESTA APLICACIÓN HA CADUCADO (30 DE JUNIO DE 2026).")
    st.stop()

st.set_page_config(page_title="COGNUSS 2 - TEORÍA DEL DERECHO", layout="wide")

# Estilos CSS de ventanas rectangulares secuenciales limpias e institucionales
st.markdown(
    """
    <style>
    .stApp { background-color: #FFFFFF; color: #0F1E36; font-family: sans-serif; padding-bottom: 80px; }
    .rect-banner { background-color: #0F1E36; color: white; padding: 20px; border-radius: 4px; text-align: center; margin-bottom: 20px; }
    .rect-cedula { background-color: #F5FAF6; border-left: 8px solid #2ECC71; padding: 20px; margin-bottom: 15px; border-radius: 4px; }
    .rect-pregunta { background-color: #F4F7FC; border-left: 8px solid #1A73E8; padding: 20px; margin-bottom: 15px; border-radius: 4px; }
    .rect-respuesta { background-color: #FDF5F5; border-left: 8px solid #E74C3C; padding: 20px; margin-bottom: 15px; border-radius: 4px; }
    .desvanecer-texto { animation: fadeOut 25s forwards; font-size: 15px; color: #E74C3C; font-weight: bold; line-height: 1.5; }
    @keyframes fadeOut { 0% { opacity: 1; } 85% { opacity: 0.1; } 100% { opacity: 0; display: none; } }
    </style>
    """, 
    unsafe_allow_html=True
)

st.markdown('<div class="rect-banner"><h1>COGNUSS 2 - TEORÍA DEL DERECHO</h1><p>MÉTODO COGNUSS II - PROFESOR JAIME ESPONDA & MIGUEL LÓPEZ LAVADOS</p></div>', unsafe_allow_html=True)

CEDULAS_LITERALES = [
    "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social. 1.1. La norma moral, características. 1.2. Derecho y Moral: diferencias entre ambos órdenes. 1.3. Normas de uso y trato social: a) concepto. b) características y diferencias con la norma jurídica.",
    "CÉDULA 2.- La norma jurídica. 2.1. Características. 2.2. Clasificación entre normas jurídicas imperativas y permisivas. 2.3. Estructura lógica de la norma jurídica.",
    "CÉDULA 3.- Vigencia, validez y eficacia del Derecho positivo. 3.1. Vigencia a) concepto b) momento de la vigencia. c) la derogación de la ley: concepto y clasificación. 3.2. Validez a) concepto b) fundamentos de la validez del Derecho. 3.3. Eficacia: concepto.",
    "CÉDULA 4.- La plenitud hermética del ordenamiento jurídico y las lagunas del Derecho. 4.1. Introducción constitucional: principio de inexcusabilidad. 4.2 Concepto de plenitud hermética del ordenamiento jurídico. 4.3. Casos en que se observan lagunas del Derecho; solución judicial. 4.4. Conflicto entre normas jurídicas positivas: criterios de solución judicial.",
    "CÉDULA 5.- Fuentes del ordenamiento jurídico. 5.1. Concepto y tipos de fuente (materiales y formales) 5.2. Fuentes formales del Derecho: clasificación. 5.3. La ley: a) concepto b) elementos c) características d) efectos de la ley en cuanto al espacio e) efectos de la ley en cuanto al tiempo.",
    "CÉDULA 6.- La costumbre. 6.1. La costumbre a) concepto b) elementos. 6.2. La costumbre en el Derecho Civil, el Derecho Comercial, el Derecho Internacional Público, el Derecho Penal y el Derecho Procesal.",
    "CÉDULA 7.- La jurisprudencia y la doctrina, como fuentes formales del Derecho. 7.1. La jurisprudencia a) concepto b) la norma del Código Civil y la práctica de los tribunales chilenos. 7.2. La doctrina a) concepto b) la discusión sobre su carácter de fuente formal del Derecho.",
    "CÉDULA 8.- La Relación Jurídica. 8.1. a) concepto b) elementos 8.2. La persona, sujeto de la relación jurídica. La persona natural. Principio y fin de su existencia.",
    "CÉDULA 9.- La persona jurídica. 9.1. Concepto. 9.2. Tipos de personas jurídicas. a) de Derecho Público y b) de Derecho Privado. 9.3. Responsabilidad de las personas jurídicas: a) responsabilidad civil: contractual y extracontractual. 9.4. Responsabilidad penal de las personas jurídicas. LEY N° 21.595.",
    "CÉDULA 10.- Derechos reales y derechos personales. 10.1. Derecho real. Concepto. Principales derechos reales (derecho de dominio o propiedad, derecho real de herencia), demás derechos reales (de usufructo, de uso y habitación) conceptos y facultades que comprende cada uno. 10.2. Derecho personal. Concepto. Elementos.",
    "CÉDULA 11.- Límites en el ejercicio de los derechos subjetivos y el abuso del derecho. 11.1. Limitaciones intrínsecas y extrínsecas de los derechos. a) Limitaciones intrínsecas: la buena fe, otras limitaciones. b) Limitaciones extrínsecas.",
    "CÉDULA 12.- Los bienes (o cosas). Clasificación. 12.1. Bienes muebles: por naturaleza y por anticipación. Bienes muebles semovientes e inanimados. Registro de los bienes muebles. 12.2. Bienes inmuebles. Concepto. a) Bienes inmuebles por naturaleza y por adherencia o destinación.",
    "CÉDULA 13.- Diferente régimen jurídico de los bienes muebles e inmuebles. 13.2. Cosas registrables y no registrables. 13.3. Cosas (o bienes) específicas y genéricas.",
    "CÉDULA 14.- Bienes o cosas comerciables e incomerciables. 14.1. Cosas comerciables e incomerciables (subclasificación). 14.2. Bienes nacionales de uso público (concesiones) y bienes fiscales (el Fisco)."
]

SUBPREGUNTAS_POOL = {
    1: [
        {"sub": "1.1", "preg": "Explaye sobre la norma moral y describa detalladamente sus características esenciales.", "ok": "La norma moral regula la conducta humana orientada al bien. Es unilateral, interior, incoercible y autónoma."},
        {"sub": "1.2", "preg": "Establezca detalladamente las diferencias fundamentales entre el orden del Derecho y el orden de la Moral.", "ok": "El Derecho regula la conducta externa mediante la bilateralidad y coercibilidad estatal. La Moral opera en el fuero interno mediante la unilateralidad e incoercibilidad."},
        {"sub": "1.3", "preg": "Defina las normas de uso y trato social, sus características y diferencias estructurales con la norma jurídica.", "ok": "Son prescripciones de conducta social de carácter exterior, incoercibles y heterónomas. Carecen de coacción de la fuerza estatal."}
    ],
    2: [
        {"sub": "2.1", "preg": "Analice y explaye las características esenciales de la norma jurídica.", "ok": "Es bilateral (correlativa), exterior (regula actos materiales), coercible (fuerza estatal) y heterónoma (voluntad externa)."},
        {"sub": "2.2", "preg": "Explique la clasificación de normas jurídicas imperativas frente a las permisivas.", "ok": "Las imperativas mandan o prohíben absolutamente limando la autonomía; las permisivas conceden una facultad o derecho subjetivo lícito."},
        {"sub": "2.3", "preg": "Describa la estructura lógica interna de una norma jurídica ordinaria.", "ok": "Se compone formalmente mediante un juicio hipotético estructurado en: un Supuesto de Hecho y una Consecuencia Jurídica."}
    ],
    3: [
        {"sub": "3.1", "preg": "Defina vigencia, momento de inicio y la clasificación jurídica de la derogación legal en Chile.", "ok": "Vigencia es la fuerza obligatoria tras la publicación. Derogación es la pérdida de esta; puede ser expresa o tácita, total o parcial."},
        {"sub": "3.2", "preg": "Explique el concepto de validez y los fundamentos de legitimidad según el Iusnaturalismo y el Iuspositivismo.", "ok": "Validez es conformidad con las normas superiores. El Iusnaturalismo se funda en la justicia/moral; el Iuspositivismo en la legalidad formal."},
        {"sub": "3.3", "preg": "Defina detalladamente el concepto técnico de eficacia dentro del Derecho positivo.", "ok": "Es una condición fáctica: representa el grado efectivo de cumplimiento y aplicación real de la norma por sus destinatarios y jueces."}
    ],
    4: [
        {"sub": "4.1", "preg": "Explique el Principio de Inexcusabilidad consagrado en el Artículo 76 de la Constitución.", "ok": "Establece que reclamada la intervención de los tribunales en forma legal, no pueden excusarse de fallar ni aun por falta de ley."},
        {"sub": "4.2", "preg": "Defina el concepto doctrinal de la plenitud hermética del ordenamiento jurídico.", "ok": "Es el postulado que afirma que el sistema legal es completo y cerrado, conteniendo herramientas normativas para resolver todo conflicto."},
        {"sub": "4.3", "preg": "Identifique cuándo se observan lagunas del Derecho y cuál es su solución por medio de la integración.", "ok": "Hay lagunas ante un vacío legal. El juez integra el ordenamiento aplicando la analogía, la equidad natural y los principios generales."},
        {"sub": "4.4", "preg": "Detalle los criterios de solución judicial ante el conflicto entre normas jurídicas positivas de igual y diverso nivel.", "ok": "Se aplican los principios clásicos: Jerarquía (ley superior deroga inferior), Temporalidad (ley posterior deroga anterior) y Especialidad (ley especial prima sobre general)."}
    ],
    5: [
        {"sub": "5.1", "preg": "Establezca la diferencia entre Fuentes Materiales y Fuentes Formales del Derecho.", "ok": "Materiales son factores reales (sociales, políticos) que determinan el contenido. Formales son los modos de manifestación obligatoria."},
        {"sub": "5.2", "preg": "Mencione la clasificación general de las Fuentes Formales.", "ok": "Se clasifican principalmente en Ley (potestad legislativa), Costumbre, Jurisprudencia (fallos) y la Doctrina (estudios de juristas)."},
        {"sub": "5.3", "preg": "Explaye sobre el concepto de ley, sus elementos, características y sus efectos en el tiempo y el espacio.", "ok": "Declaración de la voluntad soberana (Art 1 CC). Territorial en el espacio (Art 14 CC) e irretroactiva en el tiempo (Art 9 CC)."}
    ],
    6: [
        {"sub": "6.1", "preg": "Defina el concepto de costumbre jurídica y desglose sus dos elementos constitutivos.", "ok": "Repetición constante de conductas. Elementos: Material (práctica uniforme) y Espiritual (convicción de obligatoriedad / Opinio Iuris)."
}]
}      
