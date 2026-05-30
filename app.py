import streamlit as st
import random

# Configuración de página
st.set_page_config(page_title="COGNUSS 2 - TEORÍA DEL DERECHO", layout="centered")

st.markdown("<h2 style='text-align: center;'>MÉTODO COGNUSS II - PROFESOR JAIME ESPONDA & MIGUEL LÓPEZ LAVADOS</h2>", unsafe_allow_html=True)

# 1. BANCO DE PREGUNTAS CON ENCABEZADOS Y ALTERNATIVAS
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
                "explicacion": "La norma moral nace del propio sujeto (autónoma), regula la pureza de las intenciones (interior), no faculta a otro a exigir su cumplimiento (unilateral) y no se aplica por la fuerza (incoercible)."
            },
            {
                "sub": "1.2",
                "preg": "Respecto a las diferencias entre Derecho y Moral, ¿cuál de las siguientes afirmaciones es CORRECTA?",
                "opciones": [
                    "A) El Derecho es unilateral y la Moral es bilateral.",
                    "B) El Derecho es coercible (se puede aplicar la fuerza) mientras que la Moral es incoercible.",
                    "C) Ambos ordenamientos regulan exclusivamente el fuero interno del individuo.",
                    "D) La Moral es heterónoma porque proviene de una autoridad externa legislativa."
                ],
                "correcta": "B) El Derecho es coercible (se puede aplicar la fuerza) mientras que la Moral es incoercible.",
                "explicacion": "El Derecho cuenta con el aparato estatal para hacer cumplir sus normas de manera coactiva; la Moral pertenece al fuero interno e íntimo."
            },
            {
                "sub": "1.3",
                "preg": "¿Cuál es el concepto y características esenciales de los usos o normas de trato social?",
                "opciones": [
                    "A) Son normas dictadas por el Congreso que imponen multas obligatorias de carácter penal.",
                    "B) Son pautas de decoro y cortesía, de carácter heterónomo, exterior y unilateral, cuya sanción es el reproche social.",
                    "C) Son imperativos puramente autónomos que se confunden en su totalidad con los deberes religiosos.",
                    "D) Son mandatos jurídicos coercibles que facultan legalmente a un tercero a exigir el saludo en la vía pública."
                ],
                "correcta": "B) Son pautas de decoro and cortesía, de carácter heterónomo, exterior y unilateral, cuya sanción es el reproche social.",
                "explicacion": "Se imponen por la sociedad (heterónomas), regulan la conducta externa (exterior), no confieren un derecho exigible judicialmente (unilateral) y conllevan el aislamiento o desaprobación del grupo."
            }
        ]
    }
}

# 2. LÓGICA DE CONTROL DE LA APP
if "cedula" not in st.session_state:
    st.session_state.cedula = None
if "respuestas_usuario" not in st.session_state:
    st.session_state.respuestas_usuario = {}
if "evaluado" not in st.session_state:
    st.session_state.evaluado = False

st.write("---")

# Botón principal para girar la ruleta
if st.button("🎰 ¡GIRAR RULETA PARA SELECCIONAR CÉDULA!", use_container_width=True):
    st.session_state.cedula = random.choice(list(DATOS_EXAMEN.keys()))
    st.session_state.respuestas_usuario = {}
    st.session_state.evaluado = False

# Mostrar examen interactivo si hay una cédula activa
if st.session_state.cedula:
    datos_cedula = DATOS_EXAMEN[st.session_state.cedula]
    
    # Encabezado completo solicitado
    st.success(f"### 📍 {datos_cedula['titulo']}")
    st.write("Responde las siguientes preguntas para calcular tu calificación:")
    
    # Desplegar preguntas de alternativas
    for idx, p in enumerate(datos_cedula["preguntas"]):
        st.markdown(f"#### Pregunta {p['sub']}: {p['preg']}")
        
        # Guardar selección del usuario
        clave_pregunta = f"p_{p['sub']}"
        st.session_state.respuestas_usuario[clave_pregunta] = st.radio(
            "Selecciona tu respuesta:",
            options=p["opciones"],
            key=clave_pregunta,
            index=None
        )
        st.write("")

    # Botón para evaluar el examen
    if not st.session_state.evaluado:
        if st.button("📝 EVALUAR EXAMEN Y VER NOTA", type="primary"):
            st.session_state.evaluado = True
            st.rerun()

    # Mostrar resultados y notas
    if st.session_state.evaluado:
        st.write("---")
        st.write("### 📊 RESULTADOS DEL EXAMEN")
        
        correctas = 0
        total = len(datos_cedula["preguntas"])
        
        for p in datos_cedula["preguntas"]:
            clave = f"p_{p['sub']}"
            resp = st.session_state.respuestas_usuario.get(clave)
            
            if resp == p["correcta"]:
                correctas += 1
                st.success(f"✅ **Pregunta {p['sub']}: Correcta.**")
            else:
                st.error(f"❌ **Pregunta {p['sub']}: Incorrecta.**\n\nTu respuesta: {resp}\n\n**Correcta:** {p['correcta']}")
                st.info(f"💡 *Fundamento:* {p['explicacion']}")
        
        # Cálculo de nota Chilena estándar (Escala al 60% de exigencia)
        if total > 0:
            porcentaje = (correctas / total) * 100
            if porcentaje >= 60:
                nota = 4.0 + (porcentaje - 60) * (3.0 / 40)
            else:
                nota = 1.0 + porcentaje * (3.0 / 60)
            nota = round(nota, 1)
        else:
            nota = 1.0
            
        if nota >= 4.0:
            st.balloons()
            st.metric(label="⭐⭐ NOTA FINAL ⭐⭐", value=f"{nota}", delta="APROBADO")
        else:
            st.metric(label="❌ NOTA FINAL ❌", value=f"{nota}", delta="- REPROBADO", delta_color="inverse")
            
        st.write("👉 Presiona el botón **¡GIRAR RULETA!** arriba para pasar a otra unidad.")
