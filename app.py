import streamlit as st
import datetime

st.set_page_config(page_title="EXAMINADOR", layout="centered")

if datetime.date.today() > datetime.date(2026, 6, 30):
    st.error("La aplicación ha caducado.")
    st.stop()

st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>EXAMINADOR DE TEORÍA DEL DERECHO</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color: #4B5563;'>Profesor Jaime Esponda</h3>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### ℹ️ Credenciales")
    st.caption("Método Cognuss II\n\nDesarrollado por Miguel López Lavados")

st.divider()

TITULOS = {
    1: "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
    2: "CÉDULA 2.- La norma jurídica.",
    3: "CÉDULA 3.- Vigencia, validez y eficacia del Derecho positivo.",
    4: "CÉDULA 4.- La plenitud hermética del ordenamiento jurídico y las lagunas del Derecho.",
    5: "CÉDULA 5.- Fuentes del ordenamiento jurídico."
}

# CONTENIDO EXHAUSTIVO Y VARIABLES CRUZADAS VERDADERAS (Escala Dinámica A/B)
ESTRUCTURA_EXAMEN = {
    1: {
        "preguntas": [
            {
                "sub": "1.1", "preg": "¿Cuáles son las características esenciales que aíslan a la norma moral?",
                "opts": ["A) Es bilateral, de fuero externo, heterónoma y enteramente coercible por el Estado.", "B) Es unilateral, de fuero interno, autónoma en su origen e incoercible fáctico."],
                "ok": "B", "fund": "La moral obliga solo la conciencia del sujeto y carece de imperio coactivo institucional."
            },
            {
                "sub": "1.2", "preg": "Derecho y Moral: ¿Cuál es el paralelo formal según su ámbito de aplicación?",
                "opts": ["A) El Derecho regula actos manifestados (exterior); la Moral regula la pureza de la intención (interior).", "B) La Moral exige la ejecución material del acto; al Derecho le importa la aceptación íntima."],
                "ok": "A", "fund": "Cumplir un contrato por miedo a la multa es válido para el Derecho, pero carece de mérito moral."
            },
            {
                "sub": "1.3 a)", "preg": "¿Cuál es el concepto doctrinal que define a los usos o normas de trato social?",
                "opts": ["A) Son imperativos categóricos impersonales dictados por los tribunales en lo civil.", "B) Son pautas de decoro, cortesía y urbanidad establecidas de forma difusa por la colectividad."],
                "ok": "B", "fund": "Consisten en modales o costumbres de convivencia común que varían según el grupo social."
            },
            {
                "sub": "1.3 b)", "preg": "¿Qué diferencia sustantiva separa la sanción de un uso social de la norma jurídica?",
                "opts": ["A) El uso social acarrea rechazo, reprobación o aislamiento; la norma jurídica conlleva castigo del Estado.", "B) El uso social aplica penas corporales de cárcel; el Derecho acarrea remordimiento íntimo."],
                "ok": "A", "fund": "La transgresión jurídica activa multas o prisiones; el uso social solo el reproche del entorno."
            }
        ]
    },
    2: {
        "preguntas": [
            {
                "sub": "2.1", "preg": "¿Cuáles son las notas características e indispensables de la norma jurídica?",
                "opts": ["A) Autonomía de la conciencia, unilateralidad absoluta e incoercibilidad civil general.", "B) Heteronomía legislativa, exterioridad conductual, bilateralidad y coercibilidad potencial."],
                "ok": "B", "fund": "Nace de una potestad externa, rige actos manifestados y otorga facultad correlativa a un tercero."
            },
            {
                "sub": "2.2", "preg": "Frente al margen de la autonomía de la voluntad, ¿cómo operan las normas imperativas y permisivas?",
                "opts": ["A) Las Imperativas mandan o prohíben sin admitir pacto; las Permisivas confieren una opción legítima.", "B) Las Imperativas otorgan una opción renunciable; las Permisivas imponen nulidades absolutas directas."],
                "ok": "A", "fund": "Es imperativa la prohibición de venta entre cónyuges; permisiva la facultad del dueño de enajenar."
            },
            {
                "sub": "2.3", "preg": "¿Cuál es la estructura lógica interna de una norma jurídica según la teoría tradicional?",
                "opts": ["A) Se compone como un juicio hipotético estructurado en un Supuesto de Hecho y una Consecuencia.", "B) Consiste en una declaración política abstracta exenta de consecuencias coactivas puntuales."],
                "ok": "A", "fund": "Determina que ante la realización fáctica de la hipótesis legal se gatilla el efecto punitivo."
            }
        ]
    },
    3: {
        "preguntas": [
            {
                "sub": "3.1 a/b", "preg": "¿Qué es la vigencia de una norma y cuándo principia por regla general en Chile?",
                "opts": ["A) Es el valor ético intrínseco de la norma; principia desde su aprobación unánime por el Senado.", "B) Es la fuerza obligatoria formal de la ley; principia desde su publicación en el Diario Oficial."],
                "ok": "B", "fund": "Establece el marco temporal exacto a partir del cual el precepto positivo obliga a los habitantes."
            },
            {
                "sub": "3.1 c)", "preg": "En relación a la pérdida de vigencia, ¿cómo opera la derogación Tácita de una ley?",
                "opts": ["A) Cuando la nueva ley contiene disposiciones que no pueden conciliarse con las de la ley anterior.", "B) Cuando el nuevo texto legal declara de manera explícita qué artículos del pasado quedan abolidos."],
                "ok": "A", "fund": "La derogación tácita se fundamenta en la incompatibilidad lógica entre el precepto antiguo y el nuevo."
            },
            {
                "sub": "3.2 a)", "preg": "¿Cómo se conceptualiza de forma técnica la validez dentro del Derecho positivo?",
                "opts": ["A) Es la existencia formal y obligatoriedad de la norma fundada en su conformidad con las reglas superiores.", "B) Representa el grado material de cumplimiento sociológico que exhibe espontáneamente la calle."],
                "ok": "A", "fund": "Implica que la norma pertenece legítimamente al orden jerárquico por emanar del órgano competente."
            },
            {
                "sub": "3.2 b)", "preg": "¿Qué presupuesto sustenta la validez normativa según la doctrina Iuspositivista?",
                "opts": ["A) La concordancia moral y sintonía intrínseca de los artículos con los ideales de justicia natural.", "B) La regularidad formal de su producción bajo las competencias y procesos que dicta el Estado."],
                "ok": "B", "fund": "El positivismo opera bajo la separación conceptual tajante entre la validez del Derecho y la Moral."
            },
            {
                "sub": "3.3", "preg": "¿Qué representa técnicamente la eficacia de las leyes en el orden social?",
                "opts": ["A) El grado fáctico de acatamiento por los ciudadanos y de aplicación real por los jueces.", "B) La correcta protocolización y archivo administrativo de los borradores en el Congreso."],
                "ok": "A", "fund": "Mide el plano del hecho empírico: si la directriz legal es efectivamente obedecida en la práctica."
            }
        ]
    },
    4: {
        "preguntas": [
            {
                "sub": "4.1", "preg": "¿Qué deber impone el principio de inexcusabilidad a la magistratura (Art. 76 CPR)?",
                "opts": ["A) Autoriza a rechazar demandas si los códigos sustantivos poseen redacciones confusas o ambiguas.", "B) Obliga a los jueces a resolver conflictos de su competencia, aun ante la falta de ley expresa aplicable."],
                "ok": "B", "fund": "El juez no puede negarse a administrar justicia; ante vacíos debe integrar mediante la equidad natural."
            },
            {
                "sub": "4.2", "preg": "¿Qué postula técnicamente el concepto dogmático de plenitud hermética del ordenamiento?",
                "opts": ["A) El ordenamiento como un todo es completo y sistemático, proveyendo siempre una solución jurídica.", "B) Los textos legislativos individuales redactados por las cámaras carecen por completo de vacíos."],
                "ok": "A", "fund": "Distingue las lagunas de la ley (vacíos en códigos) de la autosuficiencia del sistema integral."
            },
            {
                "sub": "4.3", "preg": "¿Cómo procede judicialmente la solución de una laguna jurídica por vía de integración?",
                "opts": ["A) El magistrado llena el vacío legal recurriendo a la analogía, principios generales y equidad natural.", "B) Se archivan los expedientes y se suspende el proceso remitiendo los antecedentes al Parlamento."],
                "ok": "A", "fund": "La integración faculta al juez a extraer la regla de fallo desde las premisas racionales del sistema."
            },
            {
                "sub": "4.4", "preg": "Frente a antinomias normativas vigentes, ¿cuál es el orden clásico de los criterios de solución?",
                "opts": ["A) Criterio de Jerarquía (norma superior), Especialidad (norma específica) y Temporalidad (posterior).", "B) Ponderación económica del daño patrimonial, antigüedad del tribunal y residencia fiscal."],
                "ok": "A", "fund": "Reglas lógicas fundamentales de la hermenéutica para mantener la coherencia y unidad del Derecho."
            }
        ]
    },
    5: {
        "preguntas": [
            {
                "sub": "5.1", "preg": "¿Cuál es la distinción científica entre Fuentes Materiales y Fuentes Formales?",
                "opts": ["A) Materiales son factores de la realidad social; Formales son los procedimientos obligatorios (ley).", "B) Materiales aluden a libros escritos; Formales a ceremonias y discursos solemnes del Congreso."],
