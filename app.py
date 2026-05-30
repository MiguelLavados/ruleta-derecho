import streamlit as st

st.set_page_config(page_title="EXAMINADOR DE TEORÍA DEL DERECHO", layout="centered")

# TÍTULO FORMAL INSTITUCIONAL
st.markdown("<h1 style='text-align: center; color: #1E3A8A; margin-bottom: 0;'>EXAMINADOR DE TEORÍA DEL DERECHO</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #4B5563; font-weight: normal; margin-top: 0;'>Profesor Jaime Esponda</h3>", unsafe_allow_html=True)

with st.sidebar:
    st.write("")
    st.caption("---")
    st.caption("🛠️ **Soporte Técnico:**")
    st.caption("Método Cognuss II — Miguel López Lavados")

# REVISIÓN Y DESGLOSE COMPLETO DEL CEDULARIO (CÉDULAS 1 A 6 TOTALMENTE DESARROLLADAS)
DATOS_EXAMEN = {
    1: {
        "titulo": "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
        "preguntas": [
            {
                "sub": "1.1", 
                "preg": "En relación a la norma moral, ¿cuáles son sus características esenciales y sus implicancias doctrinarias?", 
                "opciones": [
                    "A) Es autónoma (surge del propio sujeto), interior (regula la pureza de la intención), unilateral (no confiere facultades de exigencia a un tercero) e incoercible (no admite la fuerza estatal).", 
                    "B) Es heterónoma (impuesta por el legislador), exterior (regula solo el resultado físico), bilateral (otorga derechos a otros) y coercible (coactiva)."
                ], 
                "correcta": "A) Es autónoma (surge del propio sujeto), interior (regula la pureza de la intención), unilateral (no confiere facultades de exigencia a un tercero) e incoercible (no admite la fuerza estatal).",
                "explicacion": "La norma moral apela a la conciencia del individuo (fuero interno). Nadie puede exigir judicialmente el cumplimiento de un deber moral, careciendo de sanción institucional forzosa."
            },
            {
                "sub": "1.2", 
                "preg": "Respecto a las diferencias entre Derecho y Moral, ¿cuál es el criterio de distinción formal y de obligatoriedad?", 
                "opciones": [
                    "A) El Derecho regula el fuero externo, es bilateral, heterónomo y esencialmente coercible; la Moral regula el fuero interno, es unilateral, autónoma e incoercible.", 
                    "B) Ambos ordenamientos comparten las mismas características, diferenciándose únicamente en el costo de su incumplimiento económico."
                ], 
                "correcta": "A) El Derecho regula el fuero externo, es bilateral, heterónomo y esencialmente coercible; la Moral regula el fuero interno, es unilateral, autónoma e incoercible.",
                "explicacion": "El Derecho cuenta con el aparato coactivo estatal para imponerse frente al sujeto de forma heterónoma; la Moral requiere la aceptación libre y voluntaria de la conciencia del individuo."
            },
            {
                "sub": "1.3", 
                "preg": "En cuanto a las normas de uso y trato social (usos sociales), ¿cuál es su concepto, características y distinción con la norma jurídica?", 
                "opciones": [
                    "A) Son pautas de decoro, cortesía y urbanidad dictadas por la colectividad; son heterónomas, exteriores y unilaterales, cuya sanción es el reproche o aislamiento social, careciendo de coercibilidad legal.", 
                    "B) Son imperativos autónomos absolutos que facultan legalmente a cualquier ciudadano a exigir el saludo en la vía pública pública mediante el auxilio de la fuerza."
                ], 
                "correcta": "A) Son pautas de decoro, cortesía and urbanidad dictadas por la colectividad; son heterónomas, exteriores y unilaterales, cuya sanción es el reproche o aislamiento social, careciendo de coercibilidad legal.",
                "explicacion": "Los usos sociales vienen desde fuera (heterónomos) y exigen conducta externa (exterior), pero son unilaterales porque no habilitan a un tercero a entablar una demanda judicial. Su sanción es el rechazo del grupo."
            }
        ]
    },
    2: {
        "titulo": "CÉDULA 2.- La Norma Jurídica. Características. Estructura lógica.",
        "preguntas": [
            {
                "sub": "2.1", 
                "preg": "¿Cuáles son las características esenciales de la norma jurídica y cómo se fundamenta su imperio?", 
                "opciones": [
                    "A) Es heterónoma (creada por una voluntad ajena), exterior (regula conductas manifestadas), bilateral (correlativa de derechos y deberes) y coercible (coacción legítima potencial).", 
                    "B) Es autónoma, puramente interior, unilateral y carente de sanción punitiva o institucional."
                ], 
                "correcta": "A) Es heterónoma (creada por una voluntad ajena), exterior (regula conductas manifestadas), bilateral (correlativa de derechos y deberes) y coercible (coacción legítima potencial).",
                "explicacion": "La bilateralidad implica que frente al obligado siempre hay un sujeto facultado para exigir el cumplimiento. La coercibilidad permite el uso legítimo de la fuerza social organizada para asegurar su eficacia."
            },
            {
                "sub": "2.2", 
                "preg": "¿Cómo operan las normas jurídicas imperativas frente a las prohibitivas y permisivas?", 
                "opciones": [
                    "A) Las imperativas ordenan hacer algo; las prohibitivas imponen una abstención absoluta; las permisivas conceden una facultad o autorización legítima para actuar.", 
                    "B) Las permisivas anulan la obligatoriedad general de la Constitución; las imperativas operan únicamente como consejos opcionales."
                ], 
                "correcta": "A) Las imperativas ordenan hacer algo; las prohibitivas imponen una abstención absoluta; las permisivas conceden una facultad o autorización legítima para actuar.",
                "explicacion": "Constituye la clasificación de las normas según su mandato. Las permisivas confieren un derecho subjetivo lícito para remover obstáculos del actuar jurídico."
            },
            {
                "sub": "2.3", 
                "preg": "¿Cuál es la estructura lógica interna de una norma jurídica ordinaria según la doctrina tradicional?", 
                "opciones": [
                    "A) Se compone formalmente como un juicio hipotético que enlaza un Supuesto de Hecho (hipótesis de conducta) con una Consecuencia Jurídica (efecto o sanción).", 
                    "B) Consiste en una orden categórica directa que prohíbe conductas sin describir ninguna circunstancia o hipótesis previa."
                ], 
                "correcta": "A) Se compone formalmente como un juicio hipotético que enlaza un Supuesto de Hecho (hipótesis de conducta) con una Consecuencia Jurídica (efecto o sanción).",
                "explicacion": "Estructura: 'Dado A (supuesto), debe ser B (consecuencia)'. Si se realiza la hipótesis fáctica contemplada en la ley, se gatilla de forma coactiva la consecuencia punitiva o reguladora."
            }
        ]
    },
    3: {
        "titulo": "CÉDULA 3.- Vigencia, Validez y Eficacia de las Normas Jurídicas.",
        "preguntas": [
            {
                "sub": "3.1", 
                "preg": "¿Qué define la vigencia de una norma en Chile y a través de qué mecanismos opera la derogación?", 
                "opciones": [
                    "A) La vigencia es la fuerza obligatoria formal tras su publicación en el Diario Oficial. Se extingue por derogación (obra de otra ley), la cual puede ser expresa o tácita, total o parcial.", 
                    "B) La vigencia queda al arbitrio del uso de los particulares y la derogación solo puede emanar de tratados internacionales."
                ], 
                "correcta": "A) La vigencia es la fuerza obligatoria formal tras su publicación en el Diario Oficial. Se extingue por derogación (obra de otra ley), la cual puede ser expresa o tácita, total o parcial.",
                "explicacion": "Conforme al Código Civil, la ley es obligatoria desde su publicación. La derogación tácita ocurre cuando la nueva ley contiene disposiciones que no pueden conciliarse con las de la ley anterior."
            },
            {
                "sub": "3.2", 
                "preg": "¿Cómo conceptualizan la validez de la norma jurídica la doctrina iusnaturalista y iuspositivista?", 
                "opciones": [
                    "A) El iusnaturalismo condiciona la validez a la justicia intrínseca (concordancia con el derecho natural); el iuspositivismo la reduce a la legalidad formal (órgano competente y procedimiento legal).", 
                    "B) Ambas escuelas coinciden en que el único criterio válido para fundar el derecho es la fuerza fáctica del gobernante."
                ], 
                "correcta": "A) El iusnaturalismo condiciona la validez a la justicia intrínseca (concordancia con el derecho natural); el iuspositivismo la reduce a la legalidad formal (órgano competente y procedimiento legal).",
                "explicacion": "Para Kelsen (iuspositivismo), una norma es válida si deriva su fuerza de una norma superior del sistema. Para el iusnaturalismo, una norma radicalmente injusta no es derecho."
            },
            {
                "sub": "3.3", 
                "preg": "¿Qué representa técnicamente el concepto de eficacia dentro del Derecho positivo?", 
                "opciones": [
                    "A) Es un hecho fáctico y sociológico: representa el grado efectivo de acatamiento por parte de los ciudadanos y de aplicación real por los tribunales.", 
                    "B) Consiste en el cumplimiento de los plazos administrativos internos del Congreso para la tramitación de las leyes."
                ], 
