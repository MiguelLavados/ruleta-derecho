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

# CONTEXTO PEDAGÓGICO COMPLETOUSS CON NOTA CRUZADA REAL A/B
DATOS_EXAMEN = {}

DATOS_EXAMEN[1] = {
    "titulo": TITULOS[1],
    "preguntas": [
        {"sub": "1.1", "preg": "¿Características de la norma moral?", "opts": ["A) Bilateral, exterior y coercible.", "B) Unilateral, interior, autónoma e incoercible."], "ok": "B", "fund": "Obliga solo la conciencia y carece de fuerza coactiva estatal."},
        {"sub": "1.2", "preg": "¿Qué distingue formalmente al Derecho de la Moral?", "opts": ["A) El Derecho es coercible y bilateral; la Moral es incoercible y unilateral.", "B) El Derecho es puramente interior y autónomo."], "ok": "A", "fund": "El Derecho cuenta con el imperio coactivo institucional del Estado."},
        {"sub": "1.3 a)", "preg": "¿Concepto doctrinal de las normas de trato social?", "opts": ["A) Mandatos imperativos escritos por el Congreso.", "B) Pautas de decoro, cortesía y urbanidad dictadas por el grupo."], "ok": "B", "fund": "Consisten en costumbres de convivencia comunitaria variables."},
        {"sub": "1.3 b)", "preg": "¿Diferencia de sanción con la norma jurídica?", "opts": ["A) El uso social acarrea rechazo o reproche social; la jurídica un castigo institucional estatal.", "B) El uso social aplica multas y cárcel."], "ok": "A", "fund": "La transgresión legal gatilla penas públicas sancionadas por jueces."}
    ]
}

DATOS_EXAMEN[2] = {
    "titulo": TITULOS[2],
    "preguntas": [
        {"sub": "2.1", "preg": "¿Características constitutivas de la norma jurídica?", "opts": ["A) Heterónoma, exterior, bilateral y coercible.", "B) Autónoma, interior, unilateral e incoercible."], "ok": "A", "fund": "Emana de potestad externa, rige actos manifestados y es correlativa."},
        {"sub": "2.2", "preg": "¿Cómo operan las normas imperativas y permisivas?", "opts": ["A) Las Imperativas otorgan opción; las Permisivas imponen nulidad absoluta.", "B) Las Imperativas ordenan o prohíben absolutamente; las Permisivas conceden facultad u opción."], "ok": "B", "fund": "Imperativa: prohibición de venta entre cónyuges. Permisiva: facultad de enajenar."},
        {"sub": "2.3", "preg": "¿Estructura lógica de la norma jurídica?", "opts": ["A) Juicio hipotético que enlaza Supuesto de Hecho con Consecuencia.", "B) Declaración categórica exenta de efectos normativos."], "ok": "A", "fund": "Si se realiza fácticamente la hipótesis legal, se gatilla el efecto coactivo."}
    ]
}

DATOS_EXAMEN[3] = {
    "titulo": TITULOS[3],
    "preguntas": [
        {"sub": "3.1 a/b", "preg": "¿Cuándo principia la vigencia formal en Chile?", "opts": ["A) Desde la aprobación en comisiones.", "B) Por regla general, desde su publicación en el Diario Oficial."], "ok": "B", "fund": "Fija el marco de obligatoriedad temporal del precepto positivo."},
        {"sub": "3.1 c)", "preg": "¿Cómo opera la derogación Tácita de una ley?", "opts": ["A) Cuando la nueva ley contiene disposiciones incompatibles con la ley anterior.", "B) Cuando el nuevo texto declara de forma explícita qué artículos caducan."], "ok": "A", "fund": "Se fundamenta en la incompatibilidad lógica infranqueable de preceptos."},
        {"sub": "3.2 a)", "preg": "¿Qué es conceptualmente la validez jurídica?", "opts": ["A) Conformidad con las normas superiores que determina su pertenencia al sistema.", "B) El grado fáctico de cumplimiento voluntario de los ciudadanos."], "ok": "A", "fund": "Implica la existencia formal legítima fundada en la jerarquía."},
        {"sub": "3.2 b)", "preg": "¿Qué sustenta la validez según el Iuspositivismo?", "opts": ["A) La regularidad formal de su producción por los órganos que dicta el Estado.", "B) La concordancia intrínseca de los artículos con ideales de justicia natural."], "ok": "A", "fund": "El positivismo opera bajo la separación conceptual tajante entre Derecho y Moral."},
        {"sub": "3.3", "preg": "¿Qué representa técnicamente la eficacia?", "opts": ["A) El grado fáctico de acatamiento ciudadano y de aplicación por los jueces.", "B) La protocolización burocrática de los borradores."], "ok": "A", "fund": "Mide si la directriz legal es efectivamente obedecida en la práctica."}
    ]
}

DATOS_EXAMEN[4] = {
    "titulo": "CÉDULA 4.- Plenitud hermética y lagunas.",
    "preguntas": [
        {"sub": "4.1", "preg": "¿Qué manda el principio de inexcusabilidad (Art. 76 CPR)?", "opts": ["A) Autoriza a rechazar causas ante vacíos de la legislación.", "B) Obliga a los jueces a resolver conflictos de su competencia, aun sin ley expresa aplicable."], "ok": "B", "fund": "El juez no puede negarse a administrar justicia; ante lagunas debe integrar el sistema."},
        {"sub": "4.2", "preg": "¿Qué postula técnicamente la plenitud hermética?", "opts": ["A) El ordenamiento como un todo es completo y provee siempre solución jurídica.", "B) Los códigos escritos particulares carecen por completo de vacíos normativos."], "ok": "A", "fund": "El sistema posee normas de clausura y mecanismos auto-integrativos."},
        {"sub": "4.3", "preg": "¿Cómo procede la solución por vía de integración?", "opts": ["A) El magistrado llena el vacío recurriendo a analogía, principios y equidad natural.", "B) Suspende el proceso de forma obligatoria."], "ok": "A", "fund": "Construye la regla de fallo desde las bases del propio ordenamiento."},
        {"sub": "4.4", "preg": "¿Cuáles son los criterios para resolver antinomias?", "opts": ["A) Criterio de Jerarquía, Especialidad y Temporalidad.", "B) Ponderación económica, antigüedad de la corte y residencia."], "ok": "A", "fund": "Reglas para mantener la coherencia y unidad interna del Derecho."}
    ]
}

DATOS_EXAMEN[5] = {
    "titulo": "CÉDULA 5.- Fuentes del ordenamiento jurídico.",
    "preguntas": [
        {"sub": "5.1", "preg": "¿Distinción entre Fuentes Materiales y Formales?", "opts": ["A) Materiales: factores sociales/reales; Formales: canales de expresión obligatoria (ley).", "B) Materiales: libros de papel; Formales: discursos del Congreso."], "ok": "A", "fund": "La causa político-social real frente al envase técnico dotado de imperio legal."},
        {"sub": "5.2", "preg": "¿Cuáles son las fuentes formales principales en Chile?", "opts": ["A) Únicamente la legislación penal parlamentaria escrita.", "B) La Constitución, la ley, los tratados internacionales, reglamentos, costumbre y jurisprudencia."], "ok": "B", "fund": "El derecho positivo consagra una estructura plural y articulada de producción."},
        {"sub": "5.3 a/b/c", "preg": "¿Cómo define la ley el Código Civil (Art. 1)?", "opts": ["A) Declaración de voluntad soberana que manda, prohíbe o permite.", "B) Mandato coyuntural particular expedido por la judicatura ordinaria."], "ok": "A", "fund": "Nota característica redactada por Andrés Bello de carácter general y abstracto."},
        {"sub": "5.3 d)", "preg": "¿Qué estatuye el principio de territorialidad (Art. 14 CC)?", "opts": ["A) La ley es obligatoria para todos los habitantes de la República, incluso extranjeros, dentro de las fronteras.", "B) Inmunidad jurisdiccional absoluta para los turistas."], "ok": "A", "fund": "Un extranjero que transita por el territorio debe cumplir estrictamente la ley chilena."},
        {"sub": "5.3 e)", "preg": "¿Cuál es el alcance del Principio de Irretroactividad (Art. 9 CC)?", "opts": ["A) Faculta al Estado a castigar retroactivamente conductas lícitas.", "B) La ley solo dispone para el futuro y jamás rige hacia atrás, salvo favor penal."], "ok": "B", "fund": "Resguarda la certeza jurídica impidiendo alterar situaciones consolidadas pretéritas."}
    ]
}

if "sel_cedula" not in st.session_state: st.session_state.sel_cedula = 1
if "p_idx" not in st.session_state: st.session_state.p_idx = 0
if "historial_notas" not in st.session_state: st.session_state.historial_notas = {}

st.write("### 👨‍🏫 PANEL DIRECTO DE EVALUACIÓN ORAL (CÉDULAS 1 A 5)")

b1, b2, b3, b4, b5 = st.columns(5)
with b1:
    if st.button("Cédula 1", use_container_width=True): st.session_state.sel_cedula = 1; st.session_state.p_idx = 0; st.session_state.rerun()
with b2:
    if st.button("Cédula 2", use_container_width=True): st.session_state.sel_cedula = 2; st.session_state.p_idx = 0; st.session_state.rerun()
with b3:
    if st.button("Cédula 3", use_container_width=True): st.session_state.sel_cedula = 3; st.session_state.p_idx = 0; st.session_state.rerun()
with b4:
    if st.button("Cédula 4", use_container_width=True): st.session_state.sel_cedula = 4; st.session_state.p_idx = 0; st.session_state.rerun()
with b5:
    if st.button("Cédula 5", use_container_width=True): st.session_state.sel_cedula = 5; st.session_state.p_idx = 0; st.session_state.rerun()

st.write("---")

c_actual = st.session_state.sel_cedula
item_c = DATOS_EXAMEN[c_actual]
total_p = len(item_c["preguntas"])
idx = st.session_state.p_idx
p_act = item_c["preguntas"][idx]

st.success(f"### 📍 {item_c['titulo']}")
st.write(f"**Interrogación del Subpunto {idx + 1} de {total_p}**")
st.progress((idx + 1) / total_p)
st.markdown(f"#### Subpunto {p_act['sub']}: {p_act['preg']}")

