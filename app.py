import streamlit as st
import datetime
from preguntas import DATOS_EXAMEN

# CONFIGURACIÓN GENERAL
st.set_page_config(page_title="EXAMINADOR", layout="centered")

# CADUCIDAD DE LICENCIA
if datetime.date.today() > datetime.date(2026, 6, 30):
    st.error("⏳ Licencia caducada. Disponible hasta el 30 de junio de 2026.")
    st.stop()

# ENCABEZADO FORMAL INSTITUCIONAL
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>EXAMINADOR DE TEORÍA DEL DERECHO</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color: #4B5563;'>Profesor Jaime Esponda</h3>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### ℹ️ Credenciales")
    st.caption("Método Cognuss II\n\nDesarrollado por Miguel López Lavados")

st.divider()

if "sel_cedula" not in st.session_state: st.session_state.sel_cedula = 1
if "p_idx" not in st.session_state: st.session_state.p_idx = 0
if "corregido" not in st.session_state: st.session_state.corregido = False

st.write("### 👨‍🏫 PANEL DIRECTO DE EVALUACIÓN ORAL (CÉDULAS 1 A 5)")

# BOTONERA DE EXAMEN DIRECTO
b1, b2, b3, b4, b5 = st.columns(5)
with b1:
    if st.button("Cédula 1", use_container_width=True):
        st.session_state.sel_cedula = 1; st.session_state.p_idx = 0; st.session_state.corregido = False; st.rerun()
with b2:
    if st.button("Cédula 2", use_container_width=True):
        st.session_state.sel_cedula = 2; st.session_state.p_idx = 0; st.session_state.corregido = False; st.rerun()
with b3:
    if st.button("Cédula 3", use_container_width=True):
        st.session_state.sel_cedula = 3; st.session_state.p_idx = 0; st.session_state.corregido = False; st.rerun()
with b4:
    if st.button("Cédula 4", use_container_width=True):
        st.session_state.sel_cedula = 4; st.session_state.p_idx = 0; st.session_state.corregido = False; st.rerun()
with b5:
    if st.button("Cédula 5", use_container_width=True):
        st.session_state.sel_cedula = 5; st.session_state.p_idx = 0; st.session_state.corregido = False; st.rerun()

st.write("---")

if st.session_state.sel_cedula in DATOS_EXAMEN:
    item = DATOS_EXAMEN[st.session_state.sel_cedula]
    st.success(f"### 📍 {item['titulo']}")
    
    idx = st.session_state.p_idx
    total_p = len(item["preguntas"])
    p_act = item["preguntas"][idx]
    
    st.write(f"**Interrogación del Subpunto {idx + 1} de {total_p}**")
    st.progress((idx + 1) / total_p)
    st.markdown(f"#### Subpunto {p_act['sub']}: {p_act['preg']}")
    
    # ALTERNATIVAS TOTALMENTE EN BLANCO
    seleccion = st.radio(
        "Seleccione la respuesta del alumno:",
        options=p_act["opciones"],
        index=None,
        key=f"eval_{st.session_state.sel_cedula}_{idx}"
    )
    
    st.text_area("Anotaciones y comentarios de la comisión:", height=70, key=f"notes_{st.session_state.sel_cedula}_{idx}")
    
    if st.button("📝 Evaluar Respuesta", use_container_width=True):
        if seleccion is None:
            st.warning("Por favor, marque una opción válida antes de calificar al alumno.")
        else:
            st.session_state.corregido = True

    # REVISIÓN FIJA PERSISTENTE EN PANTALLA
    if st.session_state.corregido and seleccion is not None:
        if seleccion in p_act["correcta"] or p_act["correcta"] in seleccion:
            st.success("🎯 ¡CORRECTO!")
        else:
            st.error("❌ INCORRECTO.")
            st.info(f"**Respuesta Correcta Esperada:**\n{p_act['correcta']}")
        st.warning(f"**Fundamento Doctrinario del Temario:**\n{p_act['explicacion']}")

    # NAVEGACIÓN TOTALMENTE REPARADA (AVANZA SIN TRABARSE)
    st.write("")
    n1, n2 = st.columns(2)
    with n1:
        if st.button("⬅️ Anterior Subpunto", use_container_width=True):
            if st.session_state.p_idx > 0:
                st.session_state.p_idx -= 1
                st.session_state.corregido = False
                st.rerun()
    with n2:
        if st.button("➡️ Siguiente Subpunto", use_container_width=True):
            if st.session_state.p_idx < total_p - 1:
                st.session_state.p_idx += 1
                st.session_state.corregido = False
                st.rerun()
