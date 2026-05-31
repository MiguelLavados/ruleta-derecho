import streamlit as st
import datetime

# CONFIGURACIÓN GENERAL
st.set_page_config(page_title="EXAMINADOR", layout="centered")

# CADUCIDAD DE LICENCIA
if datetime.date.today() > datetime.date(2026, 6, 30):
    st.error("⏳ Licencia caducada. Disponible hasta el 30 de junio de 2026.")
    st.stop()

# ENCABEZADO FORMAL
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>EXAMINADOR DE TEORÍA DEL DERECHO</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color: #4B5563;'>Profesor Jaime Esponda</h3>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### ℹ️ Credenciales")
    st.caption("Método Cognuss II\n\nDesarrollado por Miguel López Lavados")

st.divider()

st.subheader("🎯 Panel Central: Seleccione el Módulo de Examen")
modulo = st.selectbox(
    "Elija el rango de Cédulas a evaluar en tiempo real:",
    ["--- Seleccione un Módulo ---", "Módulo A: Cédulas 1 a 5", "Módulo B: Cédulas 6 a 10", "Módulo C: Cédulas 11 a 14"]
)

# LÍNEAS CORTADAS EN BLOQUES PARA EVITAR EL LÍMITE DE GITHUB
DATOS_EXAMEN = {
    1: {
        "titulo": "CÉDULA 1 - EL DERECHO Y LA MORAL. NORMAS DE USO SOCIAL",
        "preguntas": [
            {
                "sub": "1.1", 
                "preg": "¿Cuáles son las características principales de la norma moral?",
                "opciones": [
                    "A) Autónoma, interior, unilateral, incoercible.",
                    "B) Heterónoma, exterior, bilateral, coercible.",
                    "C) Exterior, bilateral, coercible."
                ],
                "correcta": "A) Autónoma, interior, unilateral, incoercible.",
                "explicacion": "Regula el fuero interno íntimo de la conciencia y "
                               "carece de fuerza coactiva estatal."
            },
            {
                "sub": "1.2", 
                "preg": "¿Cuál es la diferencia formal de obligatoriedad entre Derecho y Moral?",
                "opciones": [
                    "A) El Derecho es coercible y bilateral; la Moral es incoercible.",
                    "B) Ambos ordenamientos imponen multas de forma idéntica.",
                    "C) El Derecho es unilateral y la Moral es coercible."
                ],
                "correcta": "A) El Derecho es coercible and bilateral; la Moral es incoercible.",
                "explicacion": "El Derecho cuenta con el imperio del aparato público "
                               "para imponer su cumplimiento por la fuerza."
            }
        ]
    },
    2: {
        "titulo": "CÉDULA 2 - LA NORMA JURÍDICA Y SU ESTRUCTURA LÓGICA",
        "preguntas": [
            {
                "sub": "2.1", 
                "preg": "¿Cuáles son las características esenciales de la norma jurídica?",
                "opciones": [
                    "A) Heterónoma, exterior, bilateral, coercible.",
                    "B) Autónoma, interior, unilateral, incoercible.",
                    "C) Heterónoma, interior, unilateral, incoercible."
                ],
                "correcta": "A) Heterónoma, exterior, bilateral, coercible.",
                "explicacion": "Nace de una potestad externa, rige actos manifestados y "
                               "confiere deberes y facultades correlativas."
            },
            {
                "sub": "2.2", 
                "preg": "¿Cuál es la estructura lógica interna de una norma jurídica?",
                "opciones": [
                    "A) Juicio hipotético que enlaza Supuesto de Hecho con Consecuencia.",
                    "B) Mandato categórico abstracto sin hipótesis de conducta.",
                    "C) Sugerencia moral que prescribe conductas deseables."
                ],
                "correcta": "A) Juicio hipotético que enlaza Supuesto de Hecho con Consecuencia.",
                "explicacion": "Establece que si se realiza la hipótesis fáctica, "
                               "se debe aplicar el efecto legal coactivo."
            }
        ]
    },
    3: {
        "titulo": "CÉDULA 3 - VIGENCIA, VALIDEZ Y EFICACIA NORMATIVA",
        "preguntas": [
            {
                "sub": "3.1", 
                "preg": "¿Qué define la validez jurídica según el iuspositivismo?",
                "opciones": [
                    "A) Haber sido creada por órgano competente y según procedimiento.",
                    "B) La conformidad moral absoluta con los dictámenes de justicia.",
                    "C) El desuso social generalizado de las normas comunitarias."
                ],
                "correcta": "A) Haber sido creada por órgano competente y según procedimiento.",
                "explicacion": "El positivismo asocia la validez a la regularidad "
                               "de su producción formal dentro del sistema."
            }
        ]
    },
    4: {
        "titulo": "CÉDULA 4 - PLENITUD HERMÉTICA Y LAGUNAS DEL DERECHO",
        "preguntas": [
            {
                "sub": "4.1", 
                "preg": "Conforme al principio de inexcusabilidad, ¿cuál es el deber del juez?",
                "opciones": [
                    "A) No puede excusarse de fallar ni aun por falta de ley.",
                    "B) Puede suspender el juicio indefinidamente a la espera de ley.",
                    "C) Debe declarar absueltas a las partes si las leyes fallan."
                ],
                "correcta": "A) No puede excusarse de fallar ni aun por falta de ley.",
                "explicacion": "El juez está obligado a dictar sentencia siempre, "
                               "debiendo integrar el sistema si hay vacíos."
            }
        ]
    },
    5: {
        "titulo": "CÉDULA 5 - FUENTES DEL DERECHO. MATERIALES Y FORMALES",
        "preguntas": [
            {
                "sub": "5.1", 
                "preg": "Cuál es la distinción científica entre Fuentes Materiales y Formales?",
                "opciones": [
                    "A) Materiales son factores sociales; Formales son expresiones (ley).",
                    "B) Materiales aluden a libros; formales a ceremonias."
                ],
                "correcta": "A) Materiales son factores sociales; Formales son expresiones (ley).",
                "explicacion": "La fuente material provee el contenido político-social; "
                               "la formal confiere fuerza vinculante."
            }
        ]
    },
    6: {
        "titulo": "CÉDULA 6 - LA COSTUMBRE JURÍDICA",
        "preguntas": [
            {
                "sub": "6.1", 
                "preg": "¿Cuáles son los dos elementos de la costumbre jurídica?",
                "opciones": [
                    "A) Práctica constante (Material) y Opinio Iuris (Espiritual).",
                    "B) Hábitos comunitarios transitorios desprovistos de sanción."
                ],
                "correcta": "A) Práctica constante (Material) y Opinio Iuris (Espiritual).",
                "explicacion": "Requiere la repetición uniforme de un acto y la "
                               "conciencia social de responder a un deber legal."
            }
        ]
    },
    7: {
        "titulo": "CÉDULA 7 - CONSTITUCIONALISMO Y JERARQUÍA NORMATIVA",
        "preguntas": [
            {
                "sub": "7.1", 
                "preg": "¿Qué implica el principio de supremacía constitucional (Art. 6 CPR)?",
                "options": [
                    "A) Toda norma inferior debe subordinarse formal y materialmente.",
                    "B) La Constitución es modificable por resolución judicial ordinaria."
                ],
                "correcta": "A) Toda norma inferior debe subordinarse formal y materialmente.",
                "explicacion": "La Carta Fundamental es la norma cúspide que vincula "
                               "a todos los órganos del Estado."
            }
        ]
    },
    8: {
        "titulo": "CÉDULA 8 - LA JURISPRUDENCIA COMO FUENTE DEL DERECHO",
        "preguntas": [
            {
                "sub": "8.1", 
                "preg": "Respecto al efecto relativo de sentencias (Art. 3 CC), ¿cuál es la regla?",
                "opciones": [
                    "A) Las sentencias solo tienen fuerza obligatoria en las causas actuales.",
                    "B) Los fallos de la Corte Suprema constituyen leyes generales."
                ],
                "correcta": "A) Las sentencias solo tienen fuerza obligatoria en las causas actuales.",
                "explicacion": "Chile no sigue el sistema del precedente obligatorio anglosajón."
            }
        ]
    },
    9: {
        "titulo": "CÉDULA 9 - INTERPRETACIÓN DE LA LEY. REGLAS",
        "preguntas": [
            {
                "sub": "9.1", 
                "preg": "¿Cuáles son los cuatro elementos de interpretación en el Código Civil?",
                "opciones": [
                    "A) Gramatical, Lógico, Histórico y Sistemático.",
                    "B) Político, Económico, Sociológico e Internacional."
                ],
                "correcta": "A) Gramatical, Lógico, Histórico y Sistemático.",
                "explicacion": "Establecidos explícitamente por los Arts. 19 al 24 del Código Civil."
            }
        ]
    },
    10: {
        "titulo": "CÉDULA 10 - LOS SUJETOS DE DERECHO. PERSONAS",
        "preguntas": [
            {
                "sub": "10.1", 
                "preg": "¿Cuándo se inicia la existencia legal de la persona natural?",
                "opciones": [
                    "A) Al nacer, al separarse de la madre y sobrevivir un momento.",
                    "B) Desde la concepción en el vientre materno plenamente."
                ],
                "correcta": "A) Al nacer, al separarse de la madre y sobrevivir un momento.",
                "explicacion": "Cumplimiento taxativo del Artículo 74 del Código Civil."
            }
        ]
    },
    11: {
        "titulo": "CÉDULA 11 - ATRIBUTOS DE LA PERSONALIDAD",
