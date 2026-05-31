import streamlit as st
import datetime

st.set_page_config(page_title="EXAMINADOR", layout="centered")

if datetime.date.today() > datetime.date(2026, 6, 30):
    st.error("La aplicación ha caducado.")
    st.stop()

st.markdown("<h2 style='text-align:center; color: #1E3A8A;'>EXAMINADOR DE TEORÍA DEL DERECHO</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color: #4B5563;'>Profesor Jaime Esponda</h4>", unsafe_allow_html=True)

with st.sidebar:
    st.caption("🛠️ **Soporte Técnico:**\nMétodo Cognuss II\nMiguel López Lavados")

st.divider()

# INITIALIZACIÓN SEGURA DE ESTADOS CON LLAVES
if "sel_cedula" not in st.session_state:
    st.session_state["sel_cedula"] = 1
if "p_idx" not in st.session_state:
    st.session_state["p_idx"] = 0
if "historial_notas" not in st.session_state:
    st.session_state["historial_notas"] = {}

# BANCO DE DATOS REAL CON ALTERNATIVAS VARIABLES ENUNCIADO POR ENUNCIADO
DATOS_EXAMEN = {
    1: {
        "titulo": "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
        "preguntas": [
            {"sub": "1.1", "preg": "¿Características de la norma moral?", "opts": ["A) Bilateral, exterior y coercible estatal.", "B) Unilateral, interior, autónoma e incoercible."], "ok": "B", "fund": "Obliga solo la conciencia y carece de imperio coactivo público."},
            {"sub": "1.2", "preg": "¿Qué distingue formalmente al Derecho de la Moral?", "opts": ["A) El Derecho es coercible y bilateral; la Moral es incoercible y unilateral.", "B) El Derecho es de fuero puramente interno y autónomo."], "ok": "A", "fund": "El Derecho cuenta con el imperio del aparato público para imponerse."},
            {"sub": "1.3 a)", "preg": "¿Concepto doctrinal de las normas de trato social?", "opts": ["A) Mandatos imperativos escritos por el Congreso.", "B) Pautas de decoro, cortesía y urbanidad dictadas por el grupo."], "ok": "B", "fund": "Consisten en costumbres variables de convivencia comunitaria difusa."},
            {"sub": "1.3 b)", "preg": "¿Diferencia de sanción con la norma jurídica?", "opts": ["A) El uso social acarrea rechazo; la jurídica un castigo estatal.", "B) El uso social aplica multas y cárcel directas."], "ok": "A", "fund": "La transgresión legal gatilla penas públicas punitivas por jueces."}
        ]
    },
    2: {
        "titulo": "CÉDULA 2.- La norma jurídica.",
        "preguntas": [
            {"sub": "2.1", "preg": "¿Características constitutivas de la norma jurídica?", "opts": ["A) Heterónoma, exterior, bilateral y coercible.", "B) Autónoma, interior, unilateral e incoercible."], "ok": "A", "fund": "Emana de potestad externa, rige actos manifestados y es correlativa."},
            {"sub": "2.2", "preg": "¿Cómo operan las normas imperativas y permisivas?", "opts": ["A) Las Imperativas otorgan opción; las Permisivas imponen nulidad.", "B) Las Imperativas ordenan absolutamente; las Permisivas conceden opción."], "ok": "B", "fund": "Imperativa: prohibición entre cónyuges. Permisiva: facultad de vender."},
            {"sub": "2.3", "preg": "¿Estructura lógica de la norma jurídica?", "opts": ["A) Juicio hipotético: Supuesto de Hecho y Consecuencia.", "B) Declaración categórica exenta de efectos coactivos."], "ok": "A", "fund": "Si se realiza la hipótesis legal, se gatilla el efecto coactivo."}
        ]
    },
    3: {
        "titulo": "CÉDULA 3.- Vigencia, validez y eficacia del Derecho positivo.",
        "preguntas": [
            {"sub": "3.1 a/b", "preg": "¿Cuándo principia la vigencia formal en Chile?", "opts": ["A) Desde la aprobación en comisiones parlamentarias.", "B) Por regla general, desde su publicación en el Diario Oficial."], "ok": "B", "fund": "Fija el marco de obligatoriedad temporal del precepto positivo."},
            {"sub": "3.1 c)", "preg": "En relación al cese, ¿cómo opera la derogación Tácita?", "opts": ["A) Cuando la nueva ley contiene disposiciones incompatibles con la anterior.", "B) Cuando el nuevo texto declara explícitamente qué artículos caen."], "ok": "A", "fund": "Se fundamenta en la incompatibilidad lógica de los preceptos."},
            {"sub": "3.2 a)", "preg": "¿Qué es conceptualmente la validez jurídica?", "opts": ["A) Conformidad con las normas superiores que fija su pertinencia.", "B) El grado fáctico de cumplimiento material de los ciudadanos."], "ok": "A", "fund": "Implica la existencia formal legítima fundada en la jerarquía."},
            {"sub": "3.2 b)", "preg": "¿Qué sustenta la validez según el Iuspositivismo?", "opts": ["A) La regularidad formal de su producción por los órganos del Estado.", "B) La concordancia de los artículos con ideales de justicia natural."], "ok": "A", "fund": "El positivismo opera bajo la separación de Derecho y Moral."},
            {"sub": "3.3", "preg": "¿Qué representa técnicamente la eficacia?", "opts": ["A) El grado fáctico de acatamiento ciudadano y aplicación judicial.", "B) La protocolización burocrática de los borradores oficiales."], "ok": "A", "fund": "Mide si la directriz legal es efectivamente obedecida."}
        ]
    },
    4: {
        "titulo": "CÉDULA 4.- La plenitud hermética del ordenamiento y las lagunas.",
        "preguntas": [
            {"sub": "4.1", "preg": "¿Qué manda el principio de inexcusabilidad (Art. 76 CPR)?", "opts": ["A) Autoriza a rechazar causas ante vacíos de la legislación.", "B) Obliga a jueces a resolver litigios aun sin ley expresa aplicable."], "ok": "B", "fund": "El juez debe fallar siempre, integrando el sistema ante vacíos."},
            {"sub": "4.2", "preg": "¿Qué postula técnicamente la plenitud hermética?", "opts": ["A) El ordenamiento como un todo es completo y provee solución.", "B) Los códigos escritos particulares carecen de vacíos normativos."], "ok": "A", "fund": "El sistema posee normas de clausura y auto-integración."},
            {"sub": "4.3", "preg": "¿Cómo procede la solución por vía de integración?", "opts": ["A) El magistrado llena el vacío usando analogía y equidad natural.", "B) Suspende el proceso de forma obligatoria."], "ok": "A", "fund": "Construye la regla de fallo desde las bases del ordenamiento."},
            {"sub": "4.4", "preg": "¿Cuáles son los criterios para resolver antinomias?", "opts": ["A) Criterio de Jerarquía, Especialidad y Temporalidad.", "B) Ponderación económica y residencia del demandado."], "ok": "A", "fund": "Reglas para mantener la coherencia y unidad interna del Derecho."}
        ]
    },
    5: {
        "titulo": "CÉDULA 5.- Fuentes del ordenamiento jurídico.",
        "preguntas": [
            {"sub": "5.1", "preg": "¿Distinción entre Fuentes Materiales y Formales?", "opts": ["A) Materiales: factores sociales; Formales: canales de expresión (ley).", "B) Materiales: libros de papel; Formales: discursos del Congreso."], "ok": "A", "fund": "La causa político-social frente al envase dotado de imperio."},
            {"sub": "5.2", "preg": "¿Cuáles son las fuentes formales principales en Chile?", "opts": ["A) Únicamente la legislación penal parlamentaria escrita.", "B) La Constitución, la ley, los tratados, reglamentos, costumbre y fallos."], "ok": "B", "fund": "El derecho positivo consagra una estructura plural de producción."},
            {"sub": "5.3 a/b/c", "preg": "¿Cómo define la ley el Código Civil (Art. 1)?", "opts": ["A) Declaración de voluntad soberana que manda, prohíbe o permite.", "B) Mandato coyuntural particular expedido por la judicatura."], "ok": "A", "fund": "Redactada por Andrés Bello de carácter general y abstracto."},
            {"sub": "5.3 d)", "preg": "Respecto al espacio, ¿qué estatuye la territorialidad (Art. 14 CC)?", "opts": ["A) La ley obliga a todos los habitantes, incluso extranjeros, dentro.", "B) Inmunidad jurisdiccional absoluta para los turistas."], "ok": "A", "fund": "Un extranjero en el territorio debe cumplir la ley chilena."},
            {"sub": "5.3 e)", "preg": "En cuanto al tiempo, ¿cuál es el alcance de la irretroactividad (Art. 9 CC)?", "opts": ["A) Faculta al Estado a castigar retroactivamente conductas.", "B) La ley solo dispone para el futuro, salvo favor penal."], "ok": "B", "fund": "Resguarda la certeza impidiendo alterar situaciones consolidadas."}
        ]
    }
}

st.write("### 👨‍🏫 PANEL DIRECTO DE EVALUACIÓN ORAL (CÉDULAS 1 A 5)")

# COLUMNAS CON OPERACIONES INDEXADAS SEGURAS
b1, b2, b3, b4, b5 = st.columns(5)
with b1:
    if st.button("Cédula 1", use_container_width=True):
        st.session_state["sel_cedula"] = 1
        st.session_state["p_idx"] = 0
        st.rerun()
with b2:
    if st.button("Cédula 2", use_container_width=True):
        st.session_state["sel_cedula"] = 2
        st.session_state["p_idx"] = 0
        st.rerun()
with b3:
    if st.button("Cédula 3", use_container_width=True):
        st.session_state["sel_cedula"] = 3
        st.session_state["p_idx"] = 0
        st.rerun()
with b4:
    if st.button("Cédula 4", use_container_width=True):
        st.session_state["sel_cedula"] = 4
        st.session_state["p_idx"] = 0
        st.rerun()
with b5:
    if st.button("Cédula 5", use_container_width=True):
        st.session_state.sel_cedula = 5
        st.session_state["p_idx"] = 0
        st.rerun()

st.write("---")

c_actual = st.session_state["sel_cedula"]
item_c = DATOS_EXAMEN[c_actual]
total_p = len(item_c["preguntas"])
idx = st.session_state["p_idx"]
p_act = item_c["preguntas"][idx]

st.success(f"### 📍 {item_c['titulo']}")
st.write(f"**Interrogación del Subpunto {idx + 1} de {total_p}**")
st.progress((idx + 1) / total_p)
st.markdown(f"#### Subpunto {p_act['sub']}: {p_act['preg']}")

clave_corr = f"corr_{c_actual}_{idx}"
if clave_corr not in st.session_state:
    st.session_state[clave_corr] = None

# ENUNCIADOS ESPECÍFICOS REALES
seleccion = st.radio("Seleccione la respuesta del alumno:", options=p_act["opts"], index=None, key=f"ev_{c_actual}_{idx}")

st.text_area("Anotaciones y comentarios de la comisión:", height=70, key=f"nt_{c_actual}_{idx}")

