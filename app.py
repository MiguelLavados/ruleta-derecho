import streamlit as st
import random

st.set_page_config(page_title="COGNUSS 2 - TEORÍA DEL DERECHO", layout="centered")
st.markdown("<h2 style='text-align: center;'>MÉTODO COGNUSS II - PROFESOR JAIME ESPONDA & MIGUEL LÓPEZ LAVADOS</h2>", unsafe_allow_html=True)

DATOS_EXAMEN = {
    1: {
        "titulo": "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
        "preguntas": [
            {
                "sub": "1.1",
                "preg": "¿Cuáles son las características principales de la norma moral?",
                "opciones": [
                    "A) Autónoma, interior, unilateral e incoercible.",
                    "B) Heterónoma, exterior, bilateral y coercible.",
                    "C) Autónoma, exterior, bilateral e incoercible.",
                    "D) Heterónoma, interior, unilateral y coercible."
                ],
                "correcta": "A) Autónoma, interior, unilateral e incoercible.",
                "explicacion": "La norma moral nace del propio sujeto (autónoma), regula el fuero interno, es unilateral porque no faculta a otro a exigir su cumplimiento, y es incoercible."
            },
            {
                "sub": "1.2",
                "preg": "Respecto a las diferencias entre Derecho y Moral, ¿cuál es CORRECTA?",
                "opciones": [
                    "A) El Derecho es unilateral y la Moral es bilateral.",
                    "B) El Derecho es coercible (fuerza estatal) mientras que la Moral es incoercible.",
                    "C) Ambos ordenamientos regulan exclusivamente el fuero interno.",
                    "D) La Moral es heterónoma porque proviene del poder legislativo."
                ],
                "correcta": "B) El Derecho es coercible (fuerza estatal) mientras que la Moral es incoercible.",
                "explicacion": "El Derecho cuenta con el aparato coactivo del Estado; la Moral pertenece a la conciencia individual."
            },
            {
                "sub": "1.3",
                "preg": "¿Cuál es el concepto y características de las normas de uso y trato social?",
                "opciones": [
                    "A) Son normas dictadas por el Congreso que imponen multas de carácter penal.",
                    "B) Son pautas de decoro y cortesía, de carácter heterónomo, exterior y unilateral, cuya sanción es el reproche social.",
                    "C) Son imperativos puramente autónomos que se confunden con los deberes religiosos.",
                    "D) Son mandatos jurídicos coercibles que facultan legalmente a exigir el saludo."
                ],
                "correcta": "B) Son pautas de decoro y cortesía, de carácter heterónomo, exterior y unilateral, cuya sanción es el reproche social.",
                "explicacion": "Son impuestas por la sociedad, regulan la conducta externa, no confieren facultades de exigencia legal y conllevan reproche o aislamiento social."
            }
        ]
    },
    2: {
        "titulo": "CÉDULA 2.- La Norma Jurídica. Características. Estructura lógica.",
        "preguntas": [
            {
                "sub": "2.1",
                "preg": "¿Cuáles son las características esenciales que diferencian a la norma jurídica de otras normas?",
                "opciones": [
                    "A) Es puramente autónoma, interior, unilateral y de cumplimiento optativo.",
                    "B) Es heterónoma, exterior, bilateral y coercible.",
                    "C) Es incoercible, interior, unilateral y dictada por la propia conciencia.",
                    "D) Es autónoma, exterior, unilateral y carente de sanción institucional."
                ],
                "correcta": "B) Es heterónoma, exterior, bilateral y coercible.",
                "explicacion": "Proviene de una autoridad externa (heterónoma), regula actos declarados (exterior), impone deberes y concede derechos (bilateral) y es obligatoria por la fuerza (coercible)."
            },
            {
                "sub": "2.2",
                "preg": "¿Cómo operan las normas jurídicas imperativas frente a las permisivas?",
                "opciones": [
                    "A) Las imperativas mandan o prohíben limitando la autonomía; las permisivas conceden una facultad o derecho subjetivo lícito.",
                    "B) Las imperativas otorgan consejos opcionales; las permisivas obligan bajo penas de cárcel.",
                    "C) Ambas otorgan libertades absolutas sin imponer deberes en ningún caso.",
                    "D) Las permisivas anulan la constitución; las imperativas solo rigen en contratos privados."
                ],
                "correcta": "A) Las imperativas mandan o prohíben limitando la autonomía; las permisivas conceden una facultad o derecho subjetivo lícito.",
                "explicacion": "Las normas imperativas imponen mandatos insoslayables, mientras que las permisivas habilitan jurídicamente a los sujetos a actuar legítimamente."
            },
            {
                "sub": "2.3",
                "preg": "¿Cuál es la estructura lógica interna de una norma jurídica ordinaria según la doctrina clásica?",
                "opciones": [
                    "A) Un consejo moral seguido de una sanción divina voluntaria.",
                    "B) Se compone formalmente mediante un juicio hipotético estructurado en: un Supuesto de Hecho y una Consecuencia Jurídica.",
                    "C) Una declaración política de buenas intenciones sin enlaces formales.",
                    "D) Un mandato imperativo que solo contiene castigos sin describir ninguna conducta previa."
                ],
                "correcta": "B) Se compone formalmente mediante un juicio hipotético estructurado en: un Supuesto de Hecho y una Consecuencia Jurídica.",
                "explicacion": "La estructura establece que si ocurre la hipótesis (supuesto de hecho), debe seguirse la consecuencia (efecto jurídico o sanción)."
            }
        ]
    },
    3: {
        "titulo": "CÉDULA 3.- Vigencia, Validez y Eficacia de las Normas Jurídicas.",
        "preguntas": [
            {
                "sub": "3.1",
                "preg": "¿Qué define la vigencia de la derogación legal en Chile?",
                "opciones": [
                    "A) Vigencia es la fuerza obligatoria tras la publicación. Derogación es la pérdida de esta; puede ser expresa o tácita, total o parcial.",
                    "B) La vigencia comienza con la firma del contrato y termina con el mutuo acuerdo siempre.",
                    "C) La vigencia es optativa para los jueces y la derogación solo la dicta el Tribunal Internacional.",
                    "D) Una ley nunca pierde vigencia a menos que toda la población vote en contra de ella."
                ],
                "correcta": "A) Vigencia es la fuerza obligatoria tras la publicación. Derogación es la pérdida de esta; puede ser expresa o tácita, total o parcial.",
                "explicacion": "La ley obliga desde su publicación oficial y pierde su fuerza obligatoria mediante otra ley (derogación), de forma explícita o por incompatibilidad."
            },
            {
                "sub": "3.2",
                "preg": "¿Cómo se define el concepto de validez según el Iusnaturalismo y el Iuspositivismo?",
                "opciones": [
                    "A) El Iusnaturalismo la basa en la firma del Presidente; el Iuspositivismo en las costumbres del pueblo.",
                    "B) Validez es conformidad con las normas superiores. El Iusnaturalismo se funda en la justicia/moral; el Iuspositivismo en la legalidad formal.",
                    "C) Ambos coinciden en que la validez depende exclusivamente del criterio subjetivo de cada ciudadano.",
                    "D) Para el Iuspositivismo la moral es el único requisito; para el Iusnaturalismo la fuerza es lo único que importa."
                ],
                "correcta": "B) Validez es conformidad con las normas superiores. El Iusnaturalismo se funda en la justicia/moral; el Iuspositivismo en la legalidad formal.",
                "explicacion": "El iusnaturalismo exige subordinación al derecho natural (justicia), mientras que el iuspositivismo exige que la norma haya sido creada por el órgano competente siguiendo el procedimiento legal."
            },
            {
                "sub": "3.3",
                "preg": "¿Qué es el concepto técnico de eficacia dentro del Derecho positivo?",
                "opciones": [
                    "A) Es una condición fáctica: representa el grado efectivo de cumplimiento y aplicación real de la norma por sus destinatarios y jueces.",
                    "B) Es la publicación de la ley en el diario oficial sin importar si se cumple o no.",
                    "C) Es el costo económico que le toma al Estado redactar y aprobar un proyecto de ley.",
                    "D) Es la intención interna del legislador al proponer una reforma constitucional."
                ],
                "correcta": "A) Es una condición fáctica: representa el grado efectivo de cumplimiento y aplicación real de la norma por sus destinatarios y jueces.",
                "explicacion": "Una norma es eficaz cuando los ciudadanos la obedecen en la práctica y los tribunales la aplican al resolver conflictos."
            }
        ]
    }
}

if "cedula" not in st.session_state:
    st.session_state.cedula = None
if "respuestas_usuario" not in st.session_state:
    st.session_state.respuestas_usuario = {}
if "evaluado" not in st.session_state:
    st.session_state.evaluado = False

st.write("---")

if st.button("🎰 ¡GIRAR RULETA PARA SELECCIONAR CÉDULA!", use_container_width=True):
    st.session_state.cedula = random.choice(list(DATOS_EXAMEN.keys()))
    st.session_state.respuestas_usuario = {}
    st.session_state.evaluado = False

if st.session_state.cedula:
    datos_cedula = DATOS_EXAMEN[st.session_state.cedula]
