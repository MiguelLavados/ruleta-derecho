import streamlit as st

st.set_page_config(page_title="EXAMINADOR DE TEORÍA DEL DERECHO", layout="centered")

# TÍTULO FORMAL DEL EXAMINADOR Y EL PROFESOR
st.markdown("<h1 style='text-align: center; color: #1E3A8A; margin-bottom: 0;'>EXAMINADOR DE TEORÍA DEL DERECHO</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #4B5563; font-weight: normal; margin-top: 0;'>Profesor Jaime Esponda</h3>", unsafe_allow_html=True)

# CRÉDITOS ESCONDIDOS DISCRETAMENTE EN LA BARRA LATERAL IZQUIERDA
with st.sidebar:
    st.write("")
    st.write("")
    st.caption("---")
    st.caption("🛠️ **Desarrollo y Soporte Técnico:**")
    st.caption("Método Cognuss II — Miguel López Lavados")
    st.caption("Todos los derechos reservados © 2026")

# BANCO DE PREGUNTAS (CÉDULAS 1 A 6 COMPLETAS CON ALTERNATIVAS)
DATOS_EXAMEN = {
    1: {
        "titulo": "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
        "preguntas": [
            {
                "sub": "1.1", "preg": "¿Cuáles son las características principales de la norma moral?",
                "opciones": ["A) Autónoma, interior, unilateral e incoercible.", "B) Heterónoma, exterior, bilateral y coercible.", "C) Autónoma, exterior, bilateral e incoercible."],
                "correcta": "A) Autónoma, interior, unilateral e incoercible.",
                "explicacion": "Nace del propio sujeto (autónoma), regula el fuero interno (interior) y es incoercible."
            },
            {
                "sub": "1.2", "preg": "Respecto a las diferencias entre Derecho y Moral, ¿cuál es CORRECTA?",
                "opciones": ["A) El Derecho es unilateral y la Moral es bilateral.", "B) El Derecho es coercible (fuerza estatal) mientras que la Moral es incoercible.", "C) Ambos ordenamientos regulan exclusivamente el fuero interno."],
                "correcta": "B) El Derecho es coercible (fuerza estatal) mientras que la Moral es incoercible.",
                "explicacion": "El Derecho cuenta con el aparato coactivo institucional del Estado."
            },
            {
                "sub": "1.3", "preg": "¿Cuál es el concepto y características de las normas de uso y trato social?",
                "opciones": ["A) Son normas dictadas por el Congreso que imponen multas.", "B) Son pautas de decoro y cortesía, de carácter heterónomo, exterior y unilateral, cuya sanción es el reproche social.", "C) Son imperativos puramente autónomos."],
                "correcta": "B) Son pautas de decoro y cortesía, de carácter heterónomo, exterior y unilateral, cuya sanción es el reproche social.",
                "explicacion": "Establecidas por el grupo social externo, no otorgan acción legal para exigir su cumplimiento."
            }
        ]
    },
    2: {
        "titulo": "CÉDULA 2.- La Norma Jurídica. Characteristics. Estructura lógica.",
        "preguntas": [
            {
                "sub": "2.1", "preg": "¿Cuáles son las características esenciales de la norma jurídica?",
                "opciones": ["A) Es autónoma, interior y carente de sanción.", "B) Es heterónoma, exterior, bilateral y coercible.", "C) Es incoercible y dictada por la conciencia."],
                "correcta": "B) Es heterónoma, exterior, bilateral y coercible.",
                "explicacion": "Proviene de autoridad externa, regula actos manifestados, es bilateral e imponible por la fuerza."
            },
            {
                "sub": "2.2", "preg": "¿Cómo operan las normas jurídicas imperativas frente a las permisivas?",
                "opciones": ["A) Las imperativas mandan o prohíben limitando la autonomía; las permisivas conceden una facultad o derecho subjetivo lícito.", "B) Las imperativas otorgan consejos opcionales.", "C) Ambas otorgan libertades absolutas."],
                "correcta": "A) Las imperativas mandan o prohíben limitando la autonomía; las permisivas conceden una facultad o derecho subjetivo lícito.",
                "explicacion": "Las imperativas son mandatos obligatorios; las permisivas habilitan jurídicamente una conducta."
            },
            {
                "sub": "2.3", "preg": "¿Cuál es la estructura lógica interna de una norma jurídica ordinaria?",
                "opciones": ["A) Un consejo moral sin enlaces lógicos.", "B) Se compone formalmente mediante un juicio hipotético estructurado en: un Supuesto de Hecho y una Consecuencia Jurídica.", "C) Un mandato puro sin hipótesis previa."],
                "correcta": "B) Se compone formalmente mediante un juicio hipotético estructurado en: un Supuesto de Hecho y una Consecuencia Jurídica.",
                "explicacion": "Establece que ante la realización de un supuesto fáctico se debe activar una consecuencia legal."
            }
        ]
    },
    3: {
        "titulo": "CÉDULA 3.- Vigencia, Validez y Eficacia de las Normas Jurídicas.",
        "preguntas": [
            {
                "sub": "3.1", "preg": "¿Qué define la vigencia y la derogación legal en Chile?",
                "opciones": ["A) Vigencia es la fuerza obligatoria tras la publicación. Derogación es la pérdida de esta; puede ser expresa o tácita, total o parcial.", "B) La vigencia comienza y termina solo por mutuo acuerdo.", "C) La ley nunca pierde vigencia."],
                "correcta": "A) Vigencia es la fuerza obligatoria tras la publicación. Derogación es la pérdida de esta; puede ser expresa o tácita, total o parcial.",
                "explicacion": "La vigencia inicia con la publicación en el Diario Oficial y se extingue mediante otra ley."
            },
            {
                "sub": "3.2", "preg": "¿Cómo se define la validez según el Iusnaturalismo y el Iuspositivismo?",
                "opciones": ["A) El Iusnaturalismo la basa en contratos privados; el Iuspositivismo en costumbres.", "B) Validez es conformidad con las normas superiores. El Iusnaturalismo se funda en la justicia/moral; el Iuspositivismo en la legalidad formal.", "C) Depende del criterio subjetivo de cada ciudadano."],
                "correcta": "B) Validez es conformidad con las normas superiores. El Iusnaturalismo se funda en la justicia/moral; el Iuspositivismo en la legalidad formal.",
                "explicacion": "El iusnaturalismo exige justicia intrínseca; el iuspositivismo requiere creación formal competente."
            },
            {
                "sub": "3.3", "preg": "¿Qué es el concepto técnico de eficacia dentro del Derecho positivo?",
                "opciones": ["A) Es una condición fáctica: representa el grado de cumplimiento y aplicación real de la norma por sus destinatarios y jueces.", "B) Es la mera publicación de la ley.", "C) Es el costo económico que toma aprobar un proyecto."],
                "correcta": "A) Es una condición fáctica: representa el grado de cumplimiento y aplicación real de la norma por sus destinatarios y jueces.",
                "explicacion": "La eficacia mide si la norma es efectivamente obedecida y aplicada en la práctica social."
            }
        ]
    },
    4: {
        "titulo": "CÉDULA 4.- El Principio de Inexcusabilidad, Plenitud Hermética y Solución de Conflictos.",
        "preguntas": [
            {
                "sub": "4.1", "preg": "¿Qué consagra el Principio de Inexcusabilidad en el Art. 76 de la Constitución?",
                "opciones": ["A) Los jueces pueden negarse a fallar si la ley es confusa.", "B) Reclamada la intervención en forma legal, los tribunales no pueden excusarse de fallar ni aun por falta de ley.", "C) Permite postergar los juicios indefinidamente."],
                "correcta": "B) Reclamada la intervención en forma legal, los tribunales no pueden excusarse de fallar ni aun por falta de ley.",
                "explicacion": "Obliga a los jueces a resolver el litigio recurriendo a la integración del derecho."
            },
            {
                "sub": "4.2", "preg": "¿Qué es el principio doctrinal de la plenitud hermética del ordenamiento jurídico?",
                "opciones": ["A) Que el Derecho tiene vacíos insalvables.", "B) Es el postulado que afirma que el sistema es completo y siempre contiene una solución para todo conflicto social.", "C) Que las leyes solo aplican de forma secreta."],
                "correcta": "B) Es el postulado que afirma que el sistema es completo y siempre contiene una solución para todo conflicto social.",
                "explicacion": "Establece que aunque existan lagunas legales, el ordenamiento como sistema total no tiene vacíos."
            },
            {
                "sub": "4.3", "preg": "¿Cuándo se observan lagunas del Derecho y cuál es su solución por medio de la integración?",
                "opciones": ["A) Hay lagunas ante un vacío legal; el juez integra mediante la equidad natural y principios generales.", "B) Se solucionan dictando una nueva ley express en el Parlamento.", "C) Se archiva el caso sin resolución definitiva."],
                "correcta": "A) Hay lagunas ante un vacío legal; el juez integra mediante la equidad natural y principios generales.",
                "explicacion": "A falta de ley expresa, el juez llena el vacío usando herramientas de integración jurídica."
            },
            {
                "sub": "4.4", "preg": "¿Qué criterios solucionan conflictos entre normas de igual y diverso nivel?",
                "opciones": ["A) Jerarquía (ley superior deroga inferior), Temporalidad (ley posterior deroga anterior) y Especialidad.", "B) Criterio de votación popular directa.", "C) El criterio del tribunal más antiguo."],
                "correcta": "A) Jerarquía (ley superior deroga inferior), Temporalidad (ley posterior deroga anterior) y Especialidad.",
                "explicacion": "Son los tres principios clásicos de resolución de antinomias jurídicas."
            }
        ]
    },
    5: {
        "titulo": "CÉDULA 5.- Las Fuentes del Derecho. Materiales y Formales.",
        "preguntas": [
            {
