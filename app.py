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

DATOS_EXAMEN = {
    1: {
        "titulo": "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social",
        "preguntas": [
            {
                "sub": "1.2", 
                "preg": "Respecto al paralelo estructural, ¿qué distingue al Derecho de la Moral?",
                "opciones": [
                    "A) El Derecho es bilateral, exterior, heterónomo y coercible; la Moral es unilateral, interior, autónoma e incoercible.",
                    "B) El Derecho prioriza la pureza de la intención interna; la Moral exige coacción física estatal."
                ],
                "correcta": "A) El Derecho es bilateral, exterior, heterónomo y coercible; la Moral es unilateral, interior, autónoma e incoercible.",
                "explicacion": "El Derecho concede facultades a terceros y es coercible (fuerza pública); la Moral impone deberes internos sin coacción."
            },
            {
                "sub": "1.3", 
                "preg": "Según la naturaleza de la sanción, ¿cómo se diferencia un uso social de una norma jurídica?",
                "opciones": [
                    "A) El uso social acarrea rechazo, reprobación o aislamiento; la norma jurídica conlleva un castigo institucional (multa, cárcel).",
                    "B) El uso social es escrito y tipificado; la norma jurídica es difusa e imprecisa según la época."
                ],
                "correcta": "A) El uso social acarrea rechazo, reprobación o aislamiento; la norma jurídica conlleva un castigo institucional (multa, cárcel).",
                "explicacion": "Los usos sociales nacen de forma difusa en la sociedad civil; las normas jurídicas emanan de órganos estatales autorizados."
            }
        ]
    },
    2: {
        "titulo": "CÉDULA 2.- La norma jurídica",
        "preguntas": [
            {
                "sub": "2.2", 
                "preg": "Frente al margen de la voluntad, ¿cómo operan las Normas Imperativas frente a las Permisivas?",
                "opciones": [
                    "A) Las Imperativas no pueden ser modificadas por acuerdo de particulares; las Permisivas otorgan una opción al sujeto.",
                    "B) Las Imperativas otorgan una opción lícita; las Permisivas imponen nulidad absoluta si se infringen."
                ],
                "correcta": "A) Las Imperativas no pueden ser modificadas por acuerdo de particulares; las Permisivas otorgan una opción al sujeto.",
                "explicacion": "Las imperativas ordenan o prohíben de forma absoluta (ej. compraventa entre cónyuges); las permisivas conceden una aptitud legítima."
            }
        ]
    },
    3: {
        "titulo": "CÉDULA 3.- Vigencia, validez y eficacia del Derecho positivo",
        "preguntas": [
            {
                "sub": "3.1", 
                "preg": "¿Cuál es la diferencia técnica entre una Derogación Tácita y una Derogación Parcial?",
                "opciones": [
                    "A) Tácita ocurre por incompatibilidad con la ley nueva; Parcial elimina solo algunas disposiciones manteniendo el resto vigente.",
                    "B) Tácita deroga la totalidad del cuerpo legal; Parcial declara explícitamente qué artículos del pasado quedan sin efecto."
                ],
                "correcta": "A) Tácita ocurre por incompatibilidad con la ley nueva; Parcial elimina solo algunas disposiciones manteniendo el resto vigente.",
                "explicacion": "La derogación expresa se declara explícitamente. La total deja sin efecto todo el cuerpo legal preexistente."
            },
            {
                "sub": "3.2", 
                "preg": "En relación al fundamento de validez, ¿qué postula el Iuspositivismo frente al Iusnaturalismo?",
                "opciones": [
                    "A) El Iuspositivismo se funda en la legalidad formal (órgano y proceso); el Iusnaturalismo en la justicia material.",
                    "B) El Iuspositivismo exige una conexión intrínseca con la moral; el Iusnaturalismo exige solo el poder del Estado."
                ],
                "correcta": "A) El Iuspositivismo se funda en la legalidad formal (órgano y proceso); el Iusnaturalismo en la justicia material.",
                "explicacion": "Para el positivismo rige la separación conceptual entre Derecho y Moral; el iusnaturalismo exige concordancia ética."
            }
        ]
    },
    4: {
        "titulo": "CÉDULA 4.- La plenitud hermética del ordenamiento jurídico y las lagunas del Derecho",
        "preguntas": [
            {
                "sub": "4.1", 
                "preg": "¿Qué consagra el Principio de Inexcusabilidad (Art. 76 inc 2° CPR y Art. 10 inc 2° COT)?",
                "opciones": [
                    "A) Obliga a los jueces a resolver los conflictos sometidos a su conocimiento, incluso si no existe una ley expresa aplicable.",
                    "B) Permite al magistrado abstenerse o rechazar una demanda ante un daño tecnológico o vacío legal nuevo."
                ],
                "correcta": "A) Obliga a los jueces a resolver los conflictos sometidos a su conocimiento, incluso si no existe una ley expresa aplicable.",
                "explicacion": "El juez no puede negarse a fallar por falta de ley; debe integrar el sistema utilizando los principios generales del derecho."
            },
            {
                "sub": "4.2", 
                "preg": "Qué establece el concepto técnico de plenitud hermética?",
                "opciones": [
                    "A) El ordenamiento es un sistema completo y cerrado que ofrece herramientas de integración para llenar vacíos.",
                    "B) Postula la coexistencia de contradicciones insalvables resueltas mediante los criterios de Jerarquía."
                ],
                "correcta": "A) El ordenamiento es un sistema completo y cerrado que ofrece herramientas de integración para llenar vacíos.",
                "explicacion": "Las lagunas son vacíos legales específicos que se solucionan judicialmente mediante la integración (analogía o equidad natural)."
            }
        ]
    },
    5: {
        "titulo": "CÉDULA 5.- Fuentes del ordenamiento jurídico",
        "preguntas": [
            {
                "sub": "5.1", 
                "preg": "Cuál es el paralelo técnico entre las Fuentes Materiales y las Fuentes Formales?",
                "opciones": [
                    "A) Materiales son factores de la realidad social; Formales son los procedimientos institucionales obligatorios.",
                    "B) Materiales son leyes publicadas; Formales son hechos reales espontáneos."
                ],
                "correcta": "A) Materiales son factores de la realidad social; Formales son los procedimientos institucionales obligatorios.",
                "explicacion": "Las fuentes materiales determinan el contenido normativo; las fuentes formales se manifiestan con fuerza vinculante."
            }
        ]
    }
}

if "sel_cedula" not in st.session_state: st.session_state.sel_cedula = None
if "p_idx" not in st.session_state: st.session_state.p_idx = 0
if "corregido_ok" not in st.session_state: st.session_state.corregido_ok = False

st.write("### 👨‍🏫 PANEL DEL PROFESOR: EVALUACIÓN DE PREGUNTAS (CÉDULAS 1 A 5)")

b1, b2, b3, b4, b5 = st.columns(5)
with b1:
    if st.button("Cédula 1", use_container_width=True):
        st.session_state.sel_cedula = 1
        st.session_state.p_idx = 0
        st.session_state.corregido_ok = False
        st.rerun()
with b2:
    if st.button("Cédula 2", use_container_width=True):
        st.session_state.sel_cedula = 2
        st.session_state.p_idx = 0
        st.session_state.corregido_ok = False
        st.rerun()
with b3:
    if st.button("Cédula 3", use_container_width=True):
        st.session_state.sel_cedula = 3
        st.session_state.p_idx = 0
        st.session_state.corregido_ok = False
        st.rerun()
with b4:
    if st.button("Cédula 4", use_container_width=True):
        st.session_state.sel_cedula = 4
        st.session_state.p_idx = 0
        st.session_state.corregido_ok = False
        st.rerun()
with b5:
    if st.button("Cédula 5", use_container_width=True):
        st.session_state.sel_cedula = 5
        st.session_state.p_idx = 0
        st.session_state.corregido_ok = False
        st.rerun()

st.write("---")

if st.session_state.sel_cedula in DATOS_EXAMEN:
    item = DATOS_EXAMEN[st.session_state.sel_cedula]
    st.success(f"### 📍 {item['titulo']}")
    
    idx = st.session_state.p_idx
    total_p = len(item["preguntas"])
    p_act = item["preguntas"][idx]
    
    st.write(f"**Pregunta {idx + 1} de {total_p}**")
    st.progress((idx + 1) / total_p)
    st.markdown(f"#### {p_act['sub']}. {p_act['preg']}")
    
    seleccion = st.radio(
        "Seleccione la respuesta del alumno:",
        options=p_act["opciones"],
        index=None,
        key=f"eval_{st.session_state.sel_cedula}_{idx}"
    )
    
    st.text_area("Anotaciones adicionales del examen oral:", height=70, key=f"notes_{st.session_state.sel_cedula}_{idx}")
    
    # ESTRUCTURA PLANA TOTALMENTE INMUNE A ERRORES DE IDENTACIÓN
    if st.button("📝 Corregir e Inyectar Sanción", use_container_width=True):
        if seleccion is None:
            st.warning("Por favor, marque una alternativa antes de calificar.")
