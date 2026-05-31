import streamlit as st
import datetime

st.set_page_config(page_title="EXAMINADOR", layout="centered")

if datetime.date.today() > datetime.date(2026, 6, 30):
    st.error("⏳ Licencia caducada. Disponible hasta el 30 de junio de 2026.")
    st.stop()

st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>EXAMINADOR DE TEORÍA DEL DERECHO</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color: #4B5563;'>Profesor Jaime Esponda</h3>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### ℹ️ Credenciales")
    st.caption("Método Cognuss II\n\nDesarrollado por Miguel López Lavados")

st.divider()

# MATRIZ OFICIAL DE TITULOS REQUERIDOS
TITULOS = {
    1: "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
    2: "CÉDULA 2.- La norma jurídica.",
    3: "CÉDULA 3.- Vigencia, validez y eficacia del Derecho positivo.",
    4: "CÉDULA 4.- La plenitud hermética del ordenamiento jurídico y las lagunas del Derecho.",
    5: "CÉDULA 5.- Fuentes del ordenamiento jurídico."
}

# SUBPUNTOS DEL CEDULARIO OFICIAL SOLICITADOS
SUBPUNTOS = {
    1: ["1.1. La norma moral, características.", "1.2. Derecho y Moral: diferencias entre ambos órdenes.", "1.3 a) Normas de uso y trato social: concepto.", "1.3 b) Normas de uso y trato social: características y diferencias con la norma jurídica."],
    2: ["2.1. La norma jurídica: Características.", "2.2. Clasificación entre normas jurídicas imperativas y permisivas.", "2.3. Estructura lógica de la norma jurídica."],
    3: ["3.1 a/b) Vigencia: concepto y momento de la vigencia.", "3.1 c) La derogación de la ley: concepto y clasificación.", "3.2 a) Validez: concepto.", "3.2 b) Fundamentos de la validez del Derecho y presupuestos: las dos principales doctrinas.", "3.3. Eficacia: concepto."],
    4: ["4.1. Introducción constitucional: principio de inexcusabilidad.", "4.2. Concepto de plenitud hermética del ordenamiento jurídico.", "4.3. Casos en que se observan lagunas del Derecho; solución judicial.", "4.4. Conflicto entre normas jurídicas positivas: criterios de solución judicial."],
    5: ["5.1. Concepto y tipos de fuente (materiales y formales).", "5.2. Fuentes formales del Derecho: clasificación.", "5.3 a/b/c) La ley: concepto, elementos y características.", "5.3 d) La ley: efectos de la ley en cuanto al espacio.", "5.3 e) La ley: efectos de la ley en cuanto al tiempo."]
}

# RESPUESTAS CORRECTAS FIJAS EXTRAÍDAS DE TU DOCUMENTO
CORRECTAS = {
    "1.1": ("A) Unilateral, Interior, Autónoma, Incoercible.", "Regula el fuero interno íntimo y no confiere acción legal a terceros."),
    "1.2": ("A) El Derecho es Coercible y Bilateral; la Moral es Incoercible y Unilateral.", "El Derecho cuenta con el aparato público para imponerse; la Moral apela a la conciencia."),
    "1.3 a)": ("A) Pautas de decoro, cortesía y urbanidad dictadas por la sociedad de forma difusa.", "Consisten en modales de convivencia variables no tipificados legalmente."),
    "1.3 b)": ("A) Los usos sociales acarrean rechazo social y son unilaterales; las de Derecho son coercibles.", "Las infracciones a normas jurídicas conllevan multas, embargos o cárcel estatal."),
    "2.1": ("A) Heterónoma, Exterior, Bilateral, Coercible.", "Emana de autoridad externa, rige actos manifestados y confiere facultades correlativas."),
    "2.2": ("A) Las Imperativas ordenan o prohíben absolutamente; las Permisivas conceden opción.", "Ejemplo: Es imperativa la prohibición de compraventa entre cónyuges."),
    "2.3": ("A) Un juicio hipotético estructurado en un Supuesto de Hecho y una Consecuencia.", "Determina que si ocurre la hipótesis fáctica se debe aplicar el efecto legal coactivo."),
    "3.1 a/b)": ("A) Fuerza obligatoria formal de la ley; inicia desde su publicación oficial.", "La vigencia fija el marco temporal exacto a partir del cual el precepto vincula."),
    "3.1 c)": ("A) Pérdida de efectos por otra ley: Expresa, Tácita, Total y Parcial.", "Expresa lo declara; Tácita opera por incompatibilidad; Parcial remueve incisos."),
    "3.2 a)": ("A) Existencia formal y obligatoriedad basada en la regularidad del sistema.", "La validez implica la pertenencia legítima de la norma a la jerarquía del orden."),
    "3.2 b)": ("A) Doctrina Iuspositivista (legalidad formal) y Doctrina Iusnaturalista (justicia de fondo).", "El positivismo atiende al órgano competente; el derecho natural a la moral."),
    "3.3.": ("A) Grado fáctico de acatamiento ciudadano y de aplicación por los jueces.", "La eficacia mide el impacto sociológico real de la norma jurídica en los hechos."),
    "4.1.": ("A) Obliga a jueces a resolver conflictos aun sin ley expresa (Art. 76 CPR).", "El juez está obligado a fallar siempre, debiendo integrar el sistema ante vacíos."),
    "4.2.": ("A) Cualidad sistémica; el ordenamiento es completo y provee siempre herramientas.", "Postula que aunque la ley tenga lagunas, el ordenamiento como un todo es hermético."),
    "4.3.": ("A) Vacío legal; el juez integra mediante analogía, principios y equidad natural.", "La integración faculta al magistrado a construir la solución desde las bases del sistema."),
    "4.4.": ("A) Se resuelve mediante los criterios de Jerarquía, Especialidad y Temporalidad.", "Jerarquía (superior prima), Especialidad (especial), Temporalidad (posterior deroga)."),
    "5.1.": ("A) Materiales: factores sociales/políticos; Formales: modos obligatorios de expresión.", "La fuente material es la causa real; la formal es el envase dotado de imperio legal."),
    "5.2.": ("A) La Constitución, la ley, los tratados, los reglamentos, costumbre y jurisprudencia.", "El sistema reconoce una estructura pluralista de producción de normas."),
    "5.3 a/b/c)": ("A) Declaración de voluntad soberana que manda, prohíbe o permite (Art. 1 CC).", "Emana del legislador siguiendo el proceso formal que prescribe la Carta Fundamental."),
    "5.3 d)": ("A) Principio de Territorialidad (Art. 14 CC: obliga a todos los habitantes).", "Las directrices del Estado obligan a chilenos y extranjeros dentro de las fronteras."),
    "5.3 e)": ("A) Principio de Irretroactividad (Art. 9 CC: dispone solo para el futuro).", "Protege la certeza jurídica impidiendo sancionar hacia el pasado conductas pretéritas.")
}

if "sel_cedula" not in st.session_state: st.session_state.sel_cedula = 1
if "p_idx" not in st.session_state: st.session_state.p_idx = 0
if "corregido" not in st.session_state: st.session_state.corregido = False

st.write("### 👨‍🏫 PANEL DIRECTO DE EVALUACIÓN ORAL (CÉDULAS 1 A 5)")

# BOTONERA RECTIFICADA
b1, b2, b3, b4, b5 = st.columns(5)
with b1:
    if st.button("Cédula 1", use_container_width=True): st.session_state.sel_cedula = 1; st.session_state.p_idx = 0; st.session_state.corregido = False; st.rerun()
with b2:
    if st.button("Cédula 2", use_container_width=True): st.session_state.sel_cedula = 2; st.session_state.p_idx = 0; st.session_state.corregido = False; st.rerun()
with b3:
    if st.button("Cédula 3", use_container_width=True): st.session_state.sel_cedula = 3; st.session_state.p_idx = 0; st.session_state.corregido = False; st.rerun()
with b4:
    if st.button("Cédula 4", use_container_width=True): st.session_state.sel_cedula = 4; st.session_state.p_idx = 0; st.session_state.corregido = False; st.rerun()
with b5:
    if st.button("Cédula 5", use_container_width=True): st.session_state.sel_cedula = 5; st.session_state.p_idx = 0; st.session_state.corregido = False; st.rerun()

st.write("---")

c_actual = st.session_state.sel_cedula
t_items = SUBPUNTOS[c_actual]
total_p = len(t_items)
idx = st.session_state.p_idx
sub_nombre = t_items[idx]

st.success(f"### 📍 {TITULOS[c_actual]}")
st.write(f"**Interrogación del Subpunto {idx + 1} de {total_p}**")
st.progress((idx + 1) / total_p)
st.markdown(f"#### {sub_nombre}")

# BUSCAR CLAVE DE PREGUNTA
clave_busca = sub_nombre.split(" ")[0].replace(".-", "").strip()

# OPCIONES ESTÁNDAR DEL EXAMEN ORAL
opciones_radio = [
    "A) Opción Doctrinal A: Solución formal imperativa y coercible regulada por el ordenamiento chileno.",
    "B) Opción Doctrinal B: Infracción o postulado ajeno a las bases obligatorias institucionales de la materia."
]

seleccion = st.radio("Seleccione la respuesta del alumno:", options=opciones_radio, index=None, key=f"ev_{c_actual}_{idx}")

st.text_area("Anotaciones y comentarios de la comisión:", height=70, key=f"nt_{c_actual}_{idx}")

if st.button("📝 Evaluar Respuesta", use_container_width=True):
    if seleccion is None:
        st.warning("Por favor, marque una opción antes de calificar.")
    else:
        st.session_state.corregido = True

if st.session_state.corregido and seleccion is not None:
    res_data = CORRECTAS.get(clave_busca, ("A) Opción Doctrinal A: Solución formal imperativa y coercible regulada por el ordenamiento chileno.", "Fundamento del temario oficial."))
    
    if "A)" in seleccion:
        st.success("🎯 ¡CORRECTO!")
    else:
        st.error("❌ INCORRECTO.")
        st.info(f"**Respuesta Correcta Esperada:**\n{res_data[0]}")
    st.warning(f"**Fundamento Técnico (Ratio Iuris):**\n{res_data[1]}")

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
