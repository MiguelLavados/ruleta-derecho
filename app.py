import streamlit as st
import datetime
from preguntas import DATOS_EXAMEN

# CONFIGURACIÓN GENERAL
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

clave_corr = f"corr_{c_actual}_{idx}"
if clave_corr not in st.session_state: st.session_state[clave_corr] = None

# ELIMINADA LA REDUNDANCIA REQUERIDA (SE VAN LOS TEXTOS DE OPCIÓN A/B)
seleccion = st.radio("Seleccione la respuesta del alumno:", options=p_act["opciones"], index=None, key=f"ev_{c_actual}_{idx}")

st.text_area("Anotaciones y comentarios de la comisión:", height=70, key=f"nt_{c_actual}_{idx}")

if st.button("📝 Evaluar Respuesta", use_container_width=True):
    if seleccion is None:
        st.warning("Por favor, marque una opción antes de calificar.")
    else:
        st.session_state[clave_corr] = seleccion
        st.rerun()

if st.session_state[clave_corr] is not None:
    if st.session_state[clave_corr] == p_act["correcta"]:
        st.success("🎯 ¡CORRECTO!")
    else:
        st.error("❌ INCORRECTO.")
        st.info(f"**Respuesta Correcta Esperada:**\n{p_act['correcta']}")
    st.warning(f"**Fundamento Técnico (Ratio Iuris):**\n{p_act['explicacion']}")

# CALCULO DE NOTA FINAL AL LLEGAR AL ULTIMO SUBPUNTO DE LA CEDULA
if idx == total_p - 1:
    st.write("---")
    st.write("### 📊 CIERRE DE EVALUACIÓN DE LA CÉDULA")
    if st.button("🏁 CÁLCULO DE NOTA INSTITUCIONAL", type="primary", use_container_width=True):
        correctas = 0
        for i in range(total_p):
            p_check = item_c["preguntas"][i]
            if st.session_state.get(f"corr_{c_actual}_{i}") == p_check["correcta"]:
                correctas += 1
        
        porcentaje = (correctas / total_p) * 100
        if porcentaje >= 60:
            nota = 4.0 + (porcentaje - 60) * (3.0 / 40)
        else:
            nota = 1.0 + porcentaje * (3.0 / 60)
        st.session_state.historial_notas[c_actual] = round(nota, 1)

if c_actual in st.session_state.historial_notas:
    n_final = st.session_state.historial_notas[c_actual]
    if n_final >= 4.0:
        st.balloons()
        st.metric(label="⭐⭐ NOTA FINAL CÉDULA ⭐⭐", value=f"{n_final}", delta="APROBADO")
    else:
        st.metric(label="❌ NOTA FINAL CÉDULA ❌", value=f"{n_final}", delta="REPROBADO", delta_color="inverse")

st.write("")
n1, n2 = st.columns(2)
with n1:
    if st.button("⬅️ Anterior Subpunto", use_container_width=True):
        if st.session_state.p_idx > 0:
            st.session_state.p_idx -= 1
            st.rerun()
with n2:
    if st.button("➡️ Siguiente Subpunto", use_container_width=True):
        if st.session_state.p_idx < total_p - 1:
            st.session_state.p_idx += 1
            st.rerun()
