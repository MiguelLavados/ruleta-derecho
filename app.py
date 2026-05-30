import streamlit as st

st.set_page_config(page_title="EXAMINADOR", layout="centered")

st.markdown("<h2 style='text-align: center;'>EXAMINADOR DE TEORÍA DEL DERECHO</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Profesor Jaime Esponda</h4>", unsafe_allow_html=True)

with st.sidebar:
    st.caption("🛠️ **Soporte Técnico:**\nMétodo Cognuss II\nMiguel López Lavados")

DATOS_EXAMEN = {
    1: {
        "titulo": "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
        "preguntas": [
            {
                "sub": "1.1", 
                "preg": "¿Características de la norma moral?",
                "opciones": ["A) Autónoma, interior, unilateral, incoercible.", "B) Heterónoma, exterior, bilateral, coercible."],
                "correcta": "A) Autónoma, interior, unilateral, incoercible.",
                "explicacion": "Regula el fuero interno y no usa la fuerza."
            },
            {
                "sub": "1.2", 
                "preg": "¿Diferencia formal entre Derecho y Moral?",
                "opciones": ["A) El Derecho es coercible y bilateral; la Moral es incoercible y unilateral.", "B) Ambos son autónomos e interiores."],
                "correcta": "A) El Derecho es coercible y bilateral; la Moral es incoercible and unilateral.",
                "explicacion": "El Derecho cuenta con la fuerza coactiva del Estado."
            },
            {
                "sub": "1.3", 
                "preg": "¿Qué es la norma de trato social?",
                "opciones": ["A) Decoro y cortesía, heterónoma, exterior, unilateral. Sanción: reproche.", "B) Mandato coactivo estatal."],
                "correcta": "A) Decoro y cortesía, heterónoma, exterior, unilateral. Sanción: reproche.",
                "explicacion": "Impuesta por el grupo social, no tiene exigencia legal."
            }
        ]
    },
    2: {
        "titulo": "CÉDULA 2.- La Norma Jurídica. Características. Estructura lógica.",
        "preguntas": [
            {
                "sub": "2.1", 
                "preg": "¿Características de la norma jurídica?",
                "opciones": ["A) Heterónoma, exterior, bilateral, coercible.", "B) Autónoma, interior, unilateral, incoercible."],
                "correcta": "A) Heterónoma, exterior, bilateral, coercible.",
                "explicacion": "Emana de autoridad externa y es imponible por la fuerza."
            },
            {
                "sub": "2.2", 
                "preg": "¿Normas imperativas, prohibitivas y permisivas?",
                "opciones": ["A) Imperativas mandan; Prohibitivas impiden; Permisivas facultan.", "B) Son consejos opcionales."],
                "correcta": "A) Imperativas mandan; Prohibitivas impiden; Permisivas facultan.",
                "explicacion": "Es la clasificación según la naturaleza del mandato."
            },
            {
                "sub": "2.3", 
                "preg": "¿Estructura lógica de la norma jurídica?",
                "opciones": ["A) Juicio hipotético: Supuesto de Hecho y Consecuencia.", "B) Orden categórica directa sin hipótesis."],
                "correcta": "A) Juicio hipotético: Supuesto de Hecho y Consecuencia.",
                "explicacion": "Si se cumple el supuesto, se aplica el efecto legal."
            }
        ]
    },
    3: {
        "titulo": "CÉDULA 3.- Vigencia, Validez y Eficacia de las Normas Jurídicas.",
        "preguntas": [
            {
                "sub": "3.1", 
                "preg": "¿Vigencia y derogación en Chile?",
                "opciones": ["A) Vigencia: fuerza obligatoria (publicación). Derogación: pérdida (ley).", "B) Termina solo por mutuo acuerdo."],
                "correcta": "A) Vigencia: fuerza obligatoria (publicación). Derogación: pérdida (ley).",
                "explicacion": "La derogación puede ser expresa o tácita."
            },
            {
                "sub": "3.2", 
                "preg": "¿Validez según Iusnaturalismo e Iuspositivismo?",
                "opciones": ["A) Iusnaturalismo: justicia de fondo. Iuspositivismo: forma legal.", "B) Depende del criterio del ciudadano."],
                "correcta": "A) Iusnaturalismo: justicia de fondo. Iuspositivismo: forma legal.",
                "explicacion": "Forma versus fondo moral."
            },
            {
                "sub": "3.3", 
                "preg": "¿Qué es la eficacia de la norma?",
                "opciones": ["A) Grado real de acatamiento y aplicación social.", "B) La mera publicación en el diario oficial."],
                "correcta": "A) Grado real de acatamiento y aplicación social.",
                "explicacion": "Es la aplicación fáctica de la norma."
            }
        ]
    },
    4: {
        "titulo": "CÉDULA 4.- La plenitud hermética y lagunas del Derecho.",
        "preguntas": [
            {
                "sub": "4.1", 
                "preg": "¿Qué exige el principio de inexcusabilidad (Art.76 CPR)?", 
                "opciones": ["A) Tribunales deben fallar siempre, aun sin ley expresa.", "B) Permite archivar el caso si la ley es confusa."], 
                "correcta": "A) Tribunales deben fallar siempre, aun sin ley expresa.",
                "explicacion": "Obliga al juez a integrar el ordenamiento."
            },
            {
                "sub": "4.2", 
                "preg": "¿Qué es la plenitud hermética del ordenamiento?", 
                "opciones": ["A) El sistema es completo y da solución a todo conflicto.", "B) Las leyes describen toda la realidad futura."], 
                "correcta": "A) El sistema es completo y da solución a todo conflicto.",
                "explicacion": "El ordenamiento no posee vacíos absolutos."
            },
            {
                "sub": "4.3", 
                "preg": "¿Cómo se resuelve una laguna mediante integración?", 
                "opciones": ["A) Usando analogía, principios generales y equidad.", "B) Derivando el caso al Parlamento."], 
                "correcta": "A) Usando analogía, principios generales y equidad.",
                "explicacion": "Llenar el vacío con las bases del sistema."
            },
            {
                "sub": "4.4", 
                "preg": "¿Criterios para resolver antinomias?", 
                "opciones": ["A) Jerarquía, Temporalidad y Especialidad.", "B) Antigüedad del tribunal y cuantía."], 
                "correcta": "A) Jerarquía, Temporalidad y Especialidad.",
                "explicacion": "Reglas para mantener la coherencia interna."
            }
        ]
    },
    5: {
        "titulo": "CÉDULA 5.- Las Fuentes del Derecho. Materiales y Formales.",
        "preguntas": [
            {
                "sub": "5.1", 
                "preg": "¿Diferencia entre fuentes materiales y formales?", 
                "opciones": ["A) Materiales: factores sociales; Formales: modos de expresión (ley).", "B) Materiales: libros; Formales: discursos."], 
                "correcta": "A) Materiales: factores sociales; Formales: modos de expresión (ley).",
                "explicacion": "Origen político/social versus canal obligatorio."
            },
            {
                "sub": "5.2", 
                "preg": "¿Fuentes formales principales en Chile?", 
                "opciones": ["A) CPR, Ley, Tratados, Reglamentos, Jurisprudencia, Costumbre.", "B) Solo la ley escrita parlamentaria."], 
                "correcta": "A) CPR, Ley, Tratados, Reglamentos, Jurisprudencia, Costumbre.",
                "explicacion": "Pluralidad de modos de producción normativa."
            },
            {
                "sub": "5.3", 
                "preg": "¿Definición de ley (Art.1 Código Civil)?", 
                "opciones": ["A) Voluntad soberana que manda, prohíbe o permite.", "B) Orden directa del poder ejecutivo."], 
                "correcta": "A) Voluntad soberana que manda, prohíbe o permite.",
                "explicacion": "Definición legal clásica en Chile."
            }
        ]
    },
    6: {
        "titulo": "CÉDULA 6.- La Costumbre Jurídica.",
        "preguntas": [
            {
                "sub": "6.1", 
                "preg": "¿Qué es la costumbre jurídica y sus elementos?", 
                "opciones": ["A) Repetición de conducta. Elementos: Material y Espiritual.", "B) Hábitos privados sin valor legal."], 
                "correcta": "A) Repetición de conducta. Elementos: Material y Espiritual.",
                "explicacion": "Práctica constante más convicción de obligatoriedad."
            },
            {
                "sub": "6.2", 
                "preg": "¿Clasificación de la costumbre ante la ley?", 
                "opciones": ["A) Secundum legem, praeter legem, contra legem.", "B) Civil, comercial e internacional."], 
                "correcta": "A) Secundum legem, praeter legem, contra legem.",
                "explicacion": "Mide la relación jerárquica con la legislación."
            },
            {
                "sub": "6.3", 
                "preg": "¿Valor de la costumbre en Derecho Civil y Comercial?", 
                "opciones": ["A) Civil: cuando la ley remite. Comercial: en silencio de ley.", "B) Tiene valor absoluto sobre la ley escrita."], 
                "correcta": "A) Civil: cuando la ley remite. Comercial: en silencio de ley.",
                "explicacion": "Art. 2 del Código Civil y Art. 4 del Código de Comercio."
            }
        ]
    }
}

for i in range(7, 15):
    DATOS_EXAMEN[i] = {"titulo": f"CÉDULA {i}.- (Pendiente)", "preguntas": []}

if "cedula" not in st.session_state: st.session_state.cedula = None
if "respuestas" not in st.session_state: st.session_state.respuestas = {}
if "evaluado" not in st.session_state: st.session_state.evaluado = False

st.write("---")
st.write("### 👨‍🏫 SELECCIÓN DIRECTA DE CÉDULA")

cols = st.columns(5)
for idx, i in enumerate(range(1, 15)):
    with cols[idx % 5]:
