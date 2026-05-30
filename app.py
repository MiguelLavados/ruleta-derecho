import streamlit as st
import random
import time
from datetime import datetime

# Importación segura desde el archivo local de base de datos
from cedulas import CEDULARIO_COMPLETO

# CONTROL DE CADUCIDAD REQUERIDO (30 de Junio de 2026)
FECHA_LIMITE = datetime(2026, 6, 30, 23, 59, 59)
if datetime.now() > FECHA_LIMITE:
    st.error("❌ LA LICENCIA DE ESTA APLICACIÓN HA CADUCADO (30 DE JUNIO DE 2026).")
    st.stop()

st.set_page_config(page_title="COGNUSS 2 - TEORÍA DEL DERECHO", layout="wide")

st.markdown(
    """
    <style>
    .stApp { background-color: #FFFFFF; color: #0F1E36; font-family: sans-serif; padding-bottom: 80px; }
    .rect-banner { background-color: #0F1E36; color: white; padding: 20px; border-radius: 4px; text-align: center; margin-bottom: 20px; }
    .rect-cedula { background-color: #F5FAF6; border-left: 8px solid #2ECC71; padding: 20px; margin-bottom: 15px; border-radius: 4px; }
    .rect-pregunta { background-color: #F4F7FC; border-left: 8px solid #1A73E8; padding: 20px; margin-bottom: 15px; border-radius: 4px; }
    .rect-respuesta { background-color: #FDF5F5; border-left: 8px solid #E74C3C; padding: 20px; margin-bottom: 15px; border-radius: 4px; }
    .desvanecer-texto { animation: fadeOut 25s forwards; font-size: 15px; color: #E74C3C; font-weight: bold; line-height: 1.5; }
    @keyframes fadeOut { 0% { opacity: 1; } 85% { opacity: 0.1; } 100% { opacity: 0; display: none; } }
    </style>
    """, 
    unsafe_allow_html=True
)

st.markdown('<div class="rect-banner"><h1>COGNUSS 2 - TEORÍA DEL DERECHO</h1><p>MÉTODO COGNUSS II - PROFESOR JAIME ESPONDA & MIGUEL LÓPEZ LAVADOS</p></div>', unsafe_allow_html=True)

if 'cedula_seleccionada' not in st.session_state:
    st.session_state.cedula_seleccionada = None
if 'item_index' not in st.session_state:
    st.session_state.item_index = 0
if 'modo_examen' not in st.session_state:
    st.session_state.modo_examen = None
if 'score_correctas' not in st.session_state:
    st.session_state.score_correctas = 0
if 'score_totales' not in st.session_state:
    st.session_state.score_totales = 0
if 'opciones_mezcladas' not in st.session_state:
    st.session_state.opciones_mezcladas = []

st.write("### 📂 Selector de Cédulas del Balotario Oficial")
fila1 = st.columns(7)
fila2 = st.columns(7)

for i in range(1, 8):
    if fila1[i-1].button(f"Cédula {i:02d}"):
        st.session_state.cedula_seleccionada = i
        st.session_state.item_index = 0
        st.session_state.modo_examen = None
        st.session_state.opciones_mezcladas = []
        st.rerun()

for i in range(8, 15):
    if fila2[i-8].button(f"Cédula {i:02d}"):
        st.session_state.cedula_seleccionada = i
        st.session_state.item_index = 0
        st.session_state.modo_examen = None
        st.session_state.opciones_mezcladas = []
        st.rerun()

st.write("---")

if st.session_state.cedula_seleccionada is not None:
    c_id = st.session_state.cedula_seleccionada
    data_cedula = CEDULARIO_COMPLETO[c_id]
    lista_sub = data_cedula['items']
    sub_idx = st.session_state.item_index
    
    if sub_idx < len(lista_sub):
        sub_pregunta_actual = lista_sub[sub_idx]
        
        st.markdown(f'<div class="rect-cedula"><b>🟢 ENUNCIADO COMPLETO DE LA CÉDULA:</b><br><b>{data_cedula["cedula_full"]}</b></div>', unsafe_allow_html=True)
        st.write(f"### 📋 Evaluando Subpregunta {sub_pregunta_actual['sub']} de la Cédula:")
        
        if st.session_state.modo_examen is None:
            st.write("**Seleccione la vía de respuesta que desea tomar para este ítem:**")
            col_o, col_a = st.columns(2)
            if col_o.button("🗣️ VÍA ESCRITO / ORAL (Voz Alta)"):
                st.session_state.modo_examen = "ORAL"
                st.rerun()
            if col_a.button("📝 VÍA CUATRO ALTERNATIVAS"):
                st.session_state.modo_examen = "ALTS"
                distractores = [
                    "Constituye un mandato de orden moral puramente interno e incoercible que carece de sanción estatal.",
                    "Es una disposición de derecho adjetivo transitoria que fue derogada expresamente por la judicatura.",
                    "Norma civil reglamentaria que posee efectos de extraterritorialidad sin requerir declaración."
                ]
                opciones_mezcla = [sub_pregunta_actual['ok']] + distractores
                random.shuffle(opciones_mezcla)
                st.session_state.opciones_mezcladas = opciones_mezcla
                st.rerun()
        else:
            st.markdown(f'<div class="rect-pregunta"><b>🔵 PREGUNTA FORMULADA:</b><br><span style="font-size:15px; font-weight:bold;">"{sub_pregunta_actual["pregunta"]}"</span></div>', unsafe_allow_html=True)
            
            if st.session_state.modo_examen == "ORAL":
                st.markdown(f'<div class="rect-respuesta"><b>🎯 RESPUESTA CORRECTA OFICIAL (SE DIFUMINA EN 25 SEGUNDOS):</b><br><p class="desvanecer-texto">{sub_pregunta_actual["ok"]}</p></div>', unsafe_allow_html=True)
                
                c_ok, c_bad = st.columns(2)
                if c_ok.button("👍 RESPONDÍ BIEN"):
                    st.session_state.score_correctas += 1
                    st.session_state.score_totales += 1
                    st.session_state.item_index += 1
                    st.session_state.modo_examen = None
                    st.rerun()
                if c_bad.button("👎 REQUIERO REPASO"):
                    st.session_state.score_totales += 1
                    st.session_state.item_index += 1
                    st.session_state.modo_examen = None
                    st.rerun()
                    
            elif st.session_state.modo_examen == "ALTS":
                opcion_sel = st.radio("Seleccione la opción correcta de la lista (sin premarcar):", st.session_state.opciones_mezcladas, index=None, key=f"radio_{c_id}_{sub_idx}")
                
                if st.button('📥 ENVIAR RESPUESTA ACADÉMICA'):
                    if opcion_sel == sub_pregunta_actual['ok']:
                        st.success("🎯 ¡BIEN! Doctrina legal validada con éxito.")
                        st.session_state.score_correctas += 1
                    else:
                        st.error(f"❌ MAL. La respuesta correcta oficial es:\n\n{sub_pregunta_actual['ok']}")
                    time.sleep(2.5)
                    st.session_state.score_totales += 1
                    st.session_state.item_index += 1
                    st.session_state.modo_examen = None
                    st.session_state.opciones_mezcladas = []
                    st.rerun()
    else:
        st.success(f"🎉 ¡Cédula {c_id:02d} completada!")
        st.markdown("### 📊 Cartola y Evaluación Final del Examen")
        if st.session_state.score_totales > 0:
            porcentaje = (st.session_state.score_correctas / st.session_state.score_totales) * 100
            nota_final = 4.0 + ((porcentaje - 60) / 40) * 3.0 if porcentaje >= 60 else 1.0 + (porcentaje / 60) * 3.0
            st.metric(label="NOTA ESTIMADA EN ESCALA JURÍDICA USS", value=f"{nota_final:.1f}")
            st.info(f"Ítems Totales: {st.session_state.score_totales} | Correctas: {st.session_state.score_correctas}")
        
        if st.button("🔄 REINICIAR CONTADORES Y VOLVER A INTERROGAR"):
            st.session_state.cedula_seleccionada = None
            st.session_state.item_index = 0
            st.session_state.score_correctas = 0
            st.session_state.score_totales = 0
            st.rerun()
else:
    st.info("Por favor, pinche cualquiera de las 14 Cédulas en la botonera superior.")

st.write("---")
st.markdown("### 🗂️ *Propiedad Intelectual & Créditos*")
st.write("• **Profesor Titular:** Dr. Jaime Esponda")
st.write("• **Desarrollador & Alumno:** Miguel López Lavados")
st.write("• **IA:** Agente Colaborador Integrado")
