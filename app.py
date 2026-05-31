import streamlit as st

st.set_page_config(page_title="EXAMINADOR", layout="centered")

st.markdown("<h2 style='text-align:center; color: #1E3A8A;'>EXAMINADOR DE TEORÍA DEL DERECHO</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color: #4B5563;'>Profesor Jaime Esponda</h4>", unsafe_allow_html=True)

with st.sidebar:
    st.caption("🛠️ **Soporte Técnico:**\nMétodo Cognuss II\nMiguel López Lavados")

st.divider()

# MENÚ DIRECTO PARA EL PROFESOR
st.subheader("📚 Panel de Interrogación Directa")
cedula_sel = st.selectbox(
    "Seleccione el Subpunto del Cedulario Oficial a evaluar:",
    [
        "--- Elija un Subpunto ---",
        "1.1. La norma moral, características.",
        "1.2. Derecho y Moral: diferencias entre ambos órdenes.",
        "1.3. Normas de uso y trato social: concepto y diferencias.",
        "2.1. La norma jurídica: Características.",
        "2.2. Clasificación entre normas imperativas y permisivas.",
        "2.3. Estructura lógica de la norma jurídica.",
        "3.1. Vigencia: concepto, momento y derogación de la ley.",
        "3.2. Validez: concepto y las dos principales doctrinas.",
        "3.3. Eficacia: concepto fáctico sociológico.",
        "4.1. Introducción constitucional: principio de inexcusabilidad.",
        "4.2. Concepto de plenitud hermética del ordenamiento.",
        "4.3. Casos en que se observan lagunas y solución judicial.",
        "4.4. Conflicto entre normas positivas y criterios de solución.",
        "5.1. Concepto y tipos de fuente (materiales y formales).",
        "5.2. Fuentes formales del Derecho: clasificación.",
        "5.3. La ley: concepto, elementos, características y efectos."
    ]
)

# CARGA DINÁMICA ULTRA LIGERA DE RESPUESTAS AUTOMÁTICAS
RESPUESTAS = {
    "1.1. La norma moral, características.": {
        "preg": "¿Cuáles son las características principales de la norma moral?",
        "opts": ["A) Unilateral, Interior, Autónoma, Incoercible.", "B) Bilateral, Exterior, Heterónoma, Coercible."],
        "ok": "A) Unilateral, Interior, Autónoma, Incoercible.",
        "fund": "Regula la rectitud íntima de la conciencia (fuero interno) sin fuerza coactiva."
    },
    "1.2. Derecho y Moral: diferencias entre ambos órdenes.": {
        "preg": "¿Cuál es la distinción formal de coacción entre ambos?",
        "opts": ["A) El Derecho es coercible y bilateral; la Moral es incoercible y unilateral.", "B) Ambos ordenamientos imponen multas estatales de forma idéntica."],
        "ok": "A) El Derecho es coercible y bilateral; la Moral es incoercible y unilateral.",
        "fund": "El Derecho cuenta con el imperio del Estado para obligar por la fuerza física legítima."
    },
    "1.3. Normas de uso y trato social: concepto y diferencias.": {
        "preg": "¿Qué caracteriza a los usos sociales frente a la norma jurídica?",
        "opts": ["A) Son unilaterales y su infracción acarrea reproche o aislamiento social.", "B) Otorgan acciones legales ante los tribunales civiles para exigir su cumplimiento."],
        "ok": "A) Son unilaterales y su infracción acarrea reproche o aislamiento social.",
        "fund": "Emanan de la colectividad de forma difusa; carecen de castigo institucional legal."
    },
    "2.1. La norma jurídica: Características.": {
        "preg": "¿Cuáles son las notas constitutivas de la norma jurídica?",
        "opts": ["A) Heterónoma, Exterior, Bilateral y Coercible.", "B) Autónoma, Interior, Unilateral e Incoercible."],
        "ok": "A) Heterónoma, Exterior, Bilateral y Coercible.",
        "fund": "Emana de autoridad externa, regula actos manifestados y confiere deberes correlativos."
    },
    "2.2. Clasificación entre normas imperativas y permisivas.": {
        "preg": "¿Cómo operan las normas imperativas frente a las permisivas?",
        "opts": ["A) Imperativas ordenan o prohíben absolutamente; Permisivas conceden opción o facultad.", "B) Imperativas otorgan un derecho opcional; Permisivas aplican cárcel inmediata."],
        "ok": "A) Imperativas ordenan o prohíben absolutamente; Permisivas conceden opción o facultad.",
        "fund": "Ejemplo: Es imperativa la prohibición de venta entre cónyuges; permisiva la facultad de vender."
    },
    "2.3. Estructura lógica de la norma jurídica.": {
        "preg": "¿Cuál es la composición analítica de la norma jurídica?",
        "opts": ["A) Un juicio hipotético estructurado en un Supuesto de Hecho y una Consecuencia.", "B) Una orden categórica directa desprovista de hipótesis fácticas previas."],
        "ok": "A) Un juicio hipotético estructurado en un Supuesto de Hecho y una Consecuencia.",
        "fund": "Determina que si ocurre la hipótesis factual contemplada, debe aplicarse el efecto legal."
    },
    "3.1. Vigencia: concepto, momento y derogación de la ley.": {
        "preg": "¿Cómo se clasifica formalmente la derogación de una ley?",
        "opts": ["A) Expresa, Tácita, Total y Parcial.", "B) Absoluta, Relativa fáctica y por Desuso."],
        "ok": "A) Expresa, Tácita, Total y Parcial.",
        "fund": "Expresa lo declara; Tácita opera por incompatibilidad; Parcial elimina solo incisos."
    },
    "3.2. Validez: concepto y las dos principales doctrinas.": {
        "preg": "¿Qué postulan el Iuspositivismo y el Iusnaturalismo sobre la validez?",
        "opts": ["A) Positivismo exige legalidad formal; Iusnaturalismo exige justicia de fondo moral.", "B) Positivismo se basa en la moral universal; Iusnaturalismo en la fuerza soberana."],
        "ok": "A) Positivismo exige legalidad formal; Iusnaturalismo exige justicia de fondo moral.",
        "fund": "El positivismo asocia la validez a la regularidad del proceso de creación del Estado."
    },
    "3.3. Eficacia: concepto fáctico sociológico.": {
        "preg": "¿Qué representa técnicamente la eficacia del Derecho?",
        "opts": ["A) El grado fáctico de acatamiento ciudadano y aplicación efectiva por los jueces.", "B) La mera promulgación y escrituración formal de los artículos en los códigos."],
        "ok": "A) El grado fáctico de acatamiento ciudadano y aplicación efectiva por los jueces.",
        "fund": "La eficacia mide el impacto sociológico real de la norma jurídica en los hechos."
    },
    "4.1. Introducción constitucional: principio de inexcusabilidad.": {
        "preg": "¿Qué deber impone el principio de inexcusabilidad (Art. 76 CPR)?",
        "opts": ["A) Obliga a los jueces a resolver conflictos aun sin ley expresa aplicable.", "B) Faculta a tribunales a rechazar la demanda ante vacíos de la legislación."],
        "ok": "A) Obliga a los jueces a resolver conflictos aun sin ley expresa aplicable.",
        "fund": "Reclamada su intervención legal, el juez debe fallar integrando analogía o equidad."
    },
    "4.2. Concepto de plenitud hermética del ordenamiento.": {
        "preg": "¿Qué postula técnicamente la plenitud hermética?",
        "opts": ["A) El ordenamiento como un todo es completo y provee siempre una solución sistémica.", "B) Las leyes particulares describen de forma perfecta toda la realidad futura escrita."],
        "ok": "A) El ordenamiento como un todo es completo y provee siempre una solución sistémica.",
        "fund": "El sistema posee normas de clausura y auto-integración jurídica interna."
    },
    "4.3. Casos en que se observan lagunas y solución judicial.": {
        "preg": "¿Cómo procede el magistrado ante un vacío de la ley mediante integración?",
        "opts": ["A) Llena la laguna recurriendo a analogía, principios generales y equidad natural.", "B) Suspende el proceso y deriva la resolución de forma obligatoria al parlamento."],
        "ok": "A) Llena la laguna recurriendo a analogía, principios generales y equidad natural.",
        "fund": "Extrae la regla de fallo desde las premisas y bases racionales del ordenamiento."
    },
    "4.4. Conflicto entre normas positivas y criterios de solución.": {
        "preg": "¿Cuáles son los tres criterios clásicos para resolver antinomias?",
        "opts": ["A) Jerarquía (superior), Especialidad (específica) y Temporalidad (posterior).", "B) Cuantía del juicio, antigüedad de la corte y residencia del demandado."],
        "ok": "A) Jerarquía (superior), Especialidad (específica) y Temporalidad (posterior).",
        "fund": "Reglas fundamentales de la hermenéutica para mantener la coherencia unitaria del Derecho."
    },
    "5.1. Concepto y tipos de fuente (materiales y formales).": {
        "preg": "¿Cuál es el paralelo conceptual entre fuentes materiales y formales?",
        "opts": ["A) Materiales: factores sociales/reales; Formales: canales de expresión obligatoria.", "B) Materiales: libros de papel; Formales: discursos solemnes del Congreso."],
        "ok": "A) Materiales: factores sociales/reales; Formales: canales de expresión obligatoria.",
        "fund": "La causa político-social frente al envase dotado de imperio vinculante (ej. ley)."
    },
    "5.2. Fuentes formales del Derecho: clasificación.": {
        "preg": "¿Cuáles son las fuentes formales principales reconocidas en Chile?",
        "opts": ["A) La Constitución, la ley, los tratados, reglamentos, costumbre y jurisprudencia.", "B) Únicamente la legislación parlamentaria escrita dictada por el Congreso."],
        "ok": "A) La Constitución, la ley, los tratados, reglamentos, costumbre y jurisprudencia.",
        "fund": "El derecho nacional consagra una estructura articulada de producción normativa."
    },
    "5.3. La ley: concepto, elementos, características y efectos.": {
        "preg": "En cuanto al tiempo, ¿qué consagra el Principio de Irretroactividad (Art. 9 CC)?",
        "opts": ["A) La ley solo dispone para el futuro y jamás rige hacia el pasado, salvo favorabilidad penal.", "B) Faculta al Estado a castigar de forma automática las conductas lícitas del pasado."],
        "ok": "A) La ley solo dispone para el futuro y jamás rige hacia el pasado, salvo favorabilidad penal.",
