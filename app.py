import streamlit as st
import datetime

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

# PANEL CENTRAL: SELECCIÓN ESTRATÉGICA DE MÓDULOS
st.subheader("🎯 Panel Central: Seleccione el Módulo de Examen")
modulo = st.selectbox(
    "Elija el rango de Cédulas a evaluar en tiempo real:",
    ["--- Seleccione un Módulo ---", "Módulo A: Cédulas 1 a 5", "Módulo B: Cédulas 6 a 10", "Módulo C: Cédulas 11 a 14"]
)

# BASE DE DATOS OPTIMIZADA (CÉDULAS 1 A 14 DISTRIBUIDAS POR MÓDULOS)
DATOS_MÓDULOS = {
    "Módulo A: Cédulas 1 a 5": {
        1: {
            "titulo": "CÉDULA 1 - EL DERECHO Y LA MORAL. NORMAS DE USO SOCIAL",
            "preguntas": [
                {"sub": "1.1", "preg": "¿Características de la norma moral?", "opciones": ["Autónoma, interior, unilateral, incoercible.", "Heterónoma, exterior, bilateral, coercible.", "Exterior, bilateral, incoercible."], "correcta": "Autónoma, interior, unilateral, incoercible.", "explicacion": "Regula el fuero interno íntimo de la conciencia y carece de fuerza coactiva estatal."},
                {"sub": "1.2", "preg": "¿Diferencia formal de coacción entre Derecho y Moral?", "opciones": ["El Derecho es coercible y bilateral; la Moral es incoercible.", "Ambos ordenamientos imponen multas de forma idéntica.", "El Derecho es unilateral y la Moral es coercible."], "correcta": "El Derecho es coercible y bilateral; la Moral es incoercible.", "explicacion": "El Derecho cuenta con el imperio del aparato público para imponer su cumplimiento por la fuerza."},
                {"sub": "1.3", "preg": "¿Qué es una norma de trato social y su sanción?", "opciones": ["Pauta de decoro, heterónoma, exterior, unilateral. Sanción: reproche.", "Mandato jurídico dictado por el Congreso. Sanción: presidio.", "Imperativo autónomo e interior. Sanción: remordimiento."], "correcta": "Pauta de decoro, heterónoma, exterior, unilateral. Sanción: reproche.", "explicacion": "Proviene del entorno social externo, rige conductas visibles y su infracción genera rechazo social."}
            ]
        },
        2: {
            "titulo": "CÉDULA 2 - LA NORMA JURÍDICA Y SU ESTRUCTURA LÓGICA",
            "preguntas": [
                {"sub": "2.1", "preg": "¿Cuáles son las características esenciales de la norma jurídica?", "opciones": ["Heterónoma, exterior, bilateral, coercible.", "Autónoma, interior, unilateral, incoercible.", "Heterónoma, interior, unilateral, incoercible."], "correcta": "Heterónoma, exterior, bilateral, coercible.", "explicacion": "Nace de una potestad externa, rige actos manifestados y confiere deberes y facultades correlativas."},
                {"sub": "2.2", "preg": "¿Cuál es la estructura lógica interna de una norma jurídica?", "opciones": ["Juicio hipotético que enlaza Supuesto de Hecho con Consecuencia.", "Mandato categórico abstracto sin hipótesis de conducta previa.", "Sugerencia moral que prescribe conductas deseables."], "correcta": "Juicio hipotético que enlaza Supuesto de Hecho con Consecuencia.", "explicacion": "Establece que si se realiza la hipótesis fáctica, se debe aplicar el efecto legal coactivo."}
            ]
        },
        3: {
            "titulo": "CÉDULA 3 - VIGENCIA, VALIDEZ Y EFICACIA NORMATIVA",
            "preguntas": [
                {"sub": "3.1", "preg": "¿Qué define la validez jurídica según el iuspositivismo?", "opciones": ["Haber sido creada por órgano competente y según procedimiento legal.", "La conformidad moral absoluta con los dictámenes de la justicia natural.", "El desuso social generalizado de las normas por la comunidad."], "correcta": "Haber sido creada por órgano competente y según procedimiento legal.", "explicacion": "El positivismo asocia la validez a la regularidad de su producción formal dentro del sistema."},
                {"sub": "3.2", "preg": "¿Qué representa el concepto técnico de eficacia dentro del Derecho?", "opciones": ["El grado fáctico de acatamiento ciudadano y aplicación real de jueces.", "La mera promulgación del texto legal en el Diario Oficial.", "El costo presupuestario anual que toma fiscalizar las frontiers."], "correcta": "El grado fáctico de acatamiento ciudadano y aplicación real de jueces.", "explicacion": "La eficacia mide el impacto fáctico y real de la norma jurídica en los hechos sociales."}
            ]
        },
        4: {
            "titulo": "CÉDULA 4 - PLENITUD HERMÉTICA Y LAGUNAS DEL DERECHO",
            "preguntas": [
                {"sub": "4.1", "preg": "Conforme al principio de inexcusabilidad, ¿cuál es el deber del juez?", "opciones": ["No puede excusarse de fallar ni aun por falta de ley en la contienda.", "Puede suspender el juicio indefinidamente a la espera de una ley.", "Debe declarar absueltas a las partes si las leyes son confusas."], "correcta": "No puede excusarse de fallar ni aun por falta de ley en la contienda.", "explicacion": "El juez está obligado a dictar sentencia siempre, debiendo integrar el sistema si hay vacíos."},
                {"sub": "4.2", "preg": "¿Qué criterios lógicos solucionan el conflicto normativo o antinomia?", "opciones": ["Jerarquía (superior), Temporalidad (posterior) y Especialidad (específica).", "Antigüedad del tribunal, cuantía económica y residencia.", "Costo de la tramitación, fecha de la demanda y cantidad de folios."], "correcta": "Jerarquía (superior), Temporalidad (posterior) y Especialidad (específica).", "explicacion": "Son los principios lógicos que resuelven contradicciones para mantener la coherencia."}
            ]
        },
        5: {
            "titulo": "CÉDULA 5 - FUENTES DEL DERECHO. MATERIALES Y FORMALES",
            "preguntas": [
                {"sub": "5.1", "preg": "Cuál es la distinción científica entre Fuentes Materiales y Formales?", "opciones": ["Materiales son factores reales (sociales); Formales son modos de expresión (ley).", "Materiales aluden a libros escritos; formales a ceremonias legislativas.", "No existe distinción técnica; ambas aluden al texto de los códigos."], "correcta": "Materiales son factores reales (sociales); Formales son modos de expresión (ley).", "explicacion": "La fuente material provee el contenido político-social; la formal confiere fuerza vinculante."}
            ]
        }
    },
    "Módulo B: Cédulas 6 a 10": {
        6: {
            "titulo": "CÉDULA 6 - LA COSTUMBRE JURÍDICA",
            "preguntas": [
                {"sub": "6.1", "preg": "¿Cuáles son los dos elementos constitutivos de la costumbre jurídica?", "opciones": ["Práctica constante (Material) y convicción de obligatoriedad (Opinio Iuris).", "Hábitos comunitarios transitorios desprovistos de sanción legal.", "Precedentes dictados de forma obligatoria por los tribunales."], "correcta": "Práctica constante (Material) y convicción de obligatoriedad (Opinio Iuris).", "explicacion": "Requiere la repetición uniforme de un acto y la conciencia social de responder a un deber legal."}
            ]
        },
        7: {
            "titulo": "CÉDULA 7 - CONSTITUCIONALISMO Y JERARQUÍA NORMATIVA",
            "preguntas": [
                {"sub": "7.1", "preg": "¿Qué implica el principio de supremacía constitucional (Art. 6 CPR)?", "opciones": ["Toda norma inferior debe subordinarse formal y materialmente a la Constitución.", "La Constitución es modificable por simple resolución judicial de primera instancia.", "Los tratados internacionales privados derogan los derechos fundamentales chilenos."], "correcta": "Toda norma inferior debe subordinarse formal y materialmente a la Constitución.", "explicacion": "La Carta Fundamental es la norma cúspide que vincula a todos los órganos del Estado."}
            ]
        },
        8: {
            "titulo": "CÉDULA 8 - LA JURISPRUDENCIA COMO FUENTE DEL DERECHO",
            "preguntas": [
                {"sub": "8.1", "preg": "Respecto al efecto relativo de las sentencias (Art. 3 CC), ¿cuál es la regla?", "opciones": ["Las sentencias solo tienen fuerza obligatoria respecto de las causas en que se pronunciaren.", "Los fallos de la Corte Suprema constituyen leyes de alcance general.", "Las sentencias de apelación son obligatorias para todo contrato mercantil."], "correcta": "Las sentencias solo tienen fuerza obligatoria respecto de las causas en que se pronunciaren.", "explicacion": "Chile no sigue el sistema del precedente obligatorio anglosajón; rige el efecto relativo."}
            ]
        },
        9: {
            "titulo": "CÉDULA 9 - INTERPRETACIÓN DE LA LEY. REGLAS",
            "preguntas": [
                {"sub": "9.1", "preg": "¿Cuáles son los cuatro elementos de interpretación clásicos en el Código Civil?", "opciones": ["Gramatical, Lógico, Histórico y Sistemático (Arts. 19 al 24 CC).", "Político, Económico, Sociológico e Internacional abstracto.", "Doctrinal extranjero, jurisprudencial previo, costumbrista y judicial."], "correcta": "Gramatical, Lógico, Histórico y Sistemático (Arts. 19 al 24 CC).", "explicacion": "Son los elementos matrices establecidos por la codificación para desentrañar el verdadero sentido de la ley."}
            ]
        },
        10: {
            "titulo": "CÉDULA 10 - LOS SUJETOS DE DERECHO. PERSONAS",
            "preguntas": [
