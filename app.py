import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Evaluación Oral", layout="wide")

# 1. ESTILOS CSS REVISADOS (Ocultamiento invisible infalible)
st.markdown("""
<style>
    .titulo-panel { font-size: 24px; font-weight: bold; margin-bottom: 20px; }
    .cuadro-cedula { background-color: #E8F5E9; padding: 20px; border-radius: 5px; border-left: 5px solid #2E7D32; color: #1B5E20; font-size: 20px; font-weight: bold; margin-bottom: 20px;}
    .cuadro-pregunta { background-color: #ECEFF1; padding: 20px; border-radius: 5px; border-left: 5px solid #455A64; color: #263238; font-size: 18px; margin-top: 15px; }
    .cuadro-nota { background-color: #FFF3E0; padding: 25px; border-radius: 5px; border-left: 5px solid #FB8C00; font-size: 22px; text-align: center; }
    
    /* Forzar a los botones técnicos a ser invisibles y no ocupar espacio vertical */
    .boton-fantasma {
        opacity: 0 !important;
        position: absolute !important;
        height: 0px !important;
        width: 0px !important;
        overflow: hidden !important;
        margin: 0 !important;
        padding: 0 !important;
        pointer-events: none !important;
    }
</style>
""", unsafe_allow_html=True)

# 2. BASE DE DATOS DE CÉDULAS (TÍTULOS)
DATOS_CEDULAS = {
    1: "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
    2: "CÉDULA 2.- La norma jurídica. Clasificación.",
    3: "CÉDULA 3.- Vigencia, validez y eficacia del Derecho positivo.",
    4: "CÉDULA 4.- La plenitud hermética del ordenamiento jurídico y las lagunas del Derecho.",
    5: "CÉDULA 5.- Fuentes del ordenamiento jurídico. Derechos reales y bienes."
}

# 3. BANCO COMPLETO DE SUBPREGUNTAS EXTRAÍDAS FIELMENTE DEL DOCUMENTO
SUBPREGUNTAS = {
    1: [
        {
            "enunciado": "Según el paralelo estructural, ¿cuál es la diferencia en la obligatoriedad entre el Orden Jurídico y el Orden Moral?",
            "alternativas": [
                "A) El Derecho es unilateral y la Moral es bilateral.",
                "B) El Derecho es bilateral (concede facultades para exigir el cumplimiento) y la Moral es unilateral (impone deberes sin otorgar derechos correlativos).",
                "C) Ambos son bilaterales pero varían según el grupo social social civil."
            ],
            "correcta": 1
        },
        {
            "enunciado": "Respecto a la manifestación de la conducta, ¿qué prioriza el Orden Moral frente al Orden Jurídico?",
            "alternativas": [
                "A) Le importa principalmente la ejecución material de la conducta externa.",
                "B) Prioriza la validez formal dictada por el legislador soberano.",
                "C) Prioriza la pureza de la intención y el motivo interno del actuar del sujeto."
            ],
            "correcta": 2
        },
        {
            "enunciado": "Si una norma es dictada por un tercero (Estado) y obliga al sujeto sin requerir su aprobación de conciencia, el criterio aplicado es:",
            "alternativas": [
                "A) Autonomía.",
                "B) Heteronomía.",
                "C) Incoercibilidad."
            ],
            "correcta": 1
        },
        {
            "enunciado": "¿Cuál es el origen y la naturaleza de la sanción de las Normas de Uso y Trato Social?",
            "alternativas": [
                "A) Nacen del legislador y su sanción es un castigo institucionalizado como multas.",
                "B) Nacen de la sociedad civil de forma difusa y su sanción es el rechazo social, reprobación o aislamiento.",
                "C) Nacen de los tribunales y su sanción es el remordimiento de la conciencia interna."
            ],
            "correcta": 1
        }
    ],
    2: [
        {
            "enunciado": "¿Qué caracteriza a las Normas Imperativas y Prohibitivas frente a la voluntad de los particulares?",
            "alternativas": [
                "A) Conceden una opción; el sujeto decide si ejerce el derecho o renuncia a él voluntariamente.",
                "B) No pueden ser modificadas ni anuladas por el acuerdo de los particulares y su infracción provoca nulidad absoluta o penas.",
                "C) Permiten al propietario vender o arrendar de manera arbitraria sus cosas muebles."
            ],
            "correcta": 1
        },
        {
            "enunciado": "¿Cuál es un ejemplo de norma permisiva o facultativa en el Derecho Chileno?",
            "alternativas": [
                "A) La prohibición de celebrar contratos de compraventa entre cónyuges.",
                "B) La facultad del propietario de vender su casa o arrendarla a un tercero.",
                "C) La obligación legal de respetar la luz roja del semáforo al conducir."
            ],
            "correcta": 1
        }
    ],
    3: [
        {
            "enunciado": "¿Cuándo se produce una derogación de tipo 'Tácita' según el régimen legal?",
            "alternativas": [
                "A) Cuando la nueva ley declara explícitamente qué artículos del pasado quedan sin efecto.",
                "B) Cuando la nueva ley contiene normas incompatibles con la ley antigua, aunque no la mencione explícitamente.",
                "C) Cuando se elimina la totalidad del cuerpo legal preexistente de forma previa."
            ],
            "correcta": 1
        },
        {
            "enunciado": "Frente al fundamento de validez, ¿qué postula la Doctrina Iuspositivista?",
            "alternativas": [
                "A) Que la validez depende de la justicia material y la concordancia con principios morales universales.",
                "B) Que existe una conexión intrínseca donde una ley profundamente injusta no es verdadero Derecho.",
                "C) Que se funda en la legalidad formal: la norma debe ser creada por el órgano competente según el proceso legal."
            ],
            "correcta": 2
        }
    ],
    4: [
        {
            "enunciado": "¿En qué consiste el Principio de Inexcusabilidad consagrado en el artículo 76 inciso 2° de la Constitución?",
            "alternativas": [
                "A) Obliga a los jueces a resolver los conflictos aun si no existe una ley expresa que regule el caso.",
                "B) Permite al juez excusarse de fallar si hay un vacío tecnológico completamente nuevo.",
                "C) Exige que el legislador redacte leyes escritas y precisas para evitar las lagunas del derecho."
            ],
            "correcta": 0
        },
        {
            "enunciado": "Cuando se presenta una Antinomia (conflicto entre normas), ¿cuáles son los tres criterios de solución judicial?",
            "alternativas": [
                "A) Analogía, equidad natural y principios generales del derecho.",
                "B) Jerarquía (norma superior), Especialidad (norma especial) y Temporalidad (ley posterior).",
                "C) Territorialidad, irretroactividad y extraterritorialidad material."
            ],
            "correcta": 1
        }
    ],
    5: [
        {
            "enunciado": "¿Qué condiciones simultáneas exige el artículo 74 del Código Civil para el principio de la existencia legal de la persona natural?",
            "alternativas": [
                "A) La concepción biológica y la inscripción inmediata en el Registro Civil de la República.",
                "B) Separación completa de la madre, que el cordón esté cortado y haber sobrevivido un momento siquiera.",
                "C) Permanecer en el vientre materno y adquirir derechos hereditarios suspensivos."
            ],
            "correcta": 1
        },
        {
            "enunciado": "Según el artículo 577, ¿cuál es la definición y un ejemplo de un Derecho Real?",
            "alternativas": [
                "A) El que solo puede reclamarse de ciertas personas; por ejemplo, un crédito de consumo bancario.",
                "B) El vínculo obligacional de dar, hacer o no hacer; por ejemplo, un contrato de arriendo de un fundo.",
                "C) El que tenemos sobre una cosa sin respecto a determinada persona; por ejemplo, el Derecho de Dominio."
            ],
            "correcta": 2
        },
        {
            "enunciado": "Los tractores o animales destinados permanentemente al uso, cultivo y beneficio de un fundo, corresponden a:",
            "alternativas": [
                "A) Bienes muebles por naturaleza inanimados.",
                "B) Bienes inmuebles por destinación (Art. 570 del Código Civil).",
                "C) Bienes inmuebles por adherencia absoluta."
            ],
            "correcta": 1
        },
        {
            "enunciado": "¿Cómo se efectúa el Modo de Adquirir (Tradición) de los Bienes Inmuebles en Chile?",
            "alternativas": [
                "A) Por la entrega material de la cosa o por señas simbólicas inmediatas.",
                "B) Mediante la firma de un contrato meramente consensual verbal.",
                "C) De forma solemne mediante la inscripción del título en el Conservador de Bienes Raíces (Art. 686 CC)."
            ],
            "correcta": 2
        }
    ]
}

# 4. INICIALIZAR ESTADOS DE LA APLICACIÓN
if "cedula_actual" not in st.session_state:
    st.session_state.cedula_actual = 1
if "fase" not in st.session_state:
    st.session_state.fase = "SELECCION_CEDULA"
if "pregunta_index" not in st.session_state:
    st.session_state.pregunta_index = 0
if "respuestas_alumno" not in st.session_state:
    st.session_state.respuestas_alumno = {}

# 5. LÓGICA DE NAVEGACIÓN ASOCIADA A LAS TECLAS CHILENAS
def click_anterior():
    if st.session_state.fase == "SELECCION_CEDULA":
        st.session_state.cedula_actual = 5 if st.session_state.cedula_actual == 1 else st.session_state.cedula_actual - 1
    elif st.session_state.fase == "SUBPREGUNTAS":
        if st.session_state.pregunta_index > 0:
            st.session_state.pregunta_index -= 1
        else:
            st.session_state.fase = "SELECCION_CEDULA"
