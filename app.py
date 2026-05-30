import streamlit as st
import datetime

# CONFIGURACIÓN INICIAL
st.set_page_config(page_title="EXAMINADOR INSTITUCIONAL", layout="centered")

# CADUCIDAD REGLAMENTARIA
if datetime.date.today() > datetime.date(2026, 6, 30):
    st.error("⏳ Licencia caducada. Disponible hasta el 30 de junio de 2026.")
    st.stop()

# ENCABEZADO FORMAL
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>EXAMINADOR DE TEORÍA DEL DERECHO</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color: #4B5563;'>Profesor Jaime Esponda</h4>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### ℹ️ Credenciales")
    st.caption("Método Cognuss II\n\nDesarrollado por Miguel López Lavados")

st.divider()

# =====================================================
# PANTALLA PRINCIPAL: SELECCIÓN DE MÓDULOS DE EVALUACIÓN
# =====================================================
st.subheader("🎯 Panel Central: Seleccione el Módulo de Examen")
modulo = st.selectbox(
    "Elija el rango de Cédulas a evaluar en tiempo real:",
    ["--- Seleccione un Módulo ---", "Módulo A: Cédulas 1 a 5", "Módulo B: Cédulas 6 a 10", "Módulo C: Cédulas 11 a 14"]
)

# BASE DE DATOS DEL MÓDULO A (CÉDULAS 1 A 5 COMPLETAS Y EXTENSAS)
DATOS_MODULO_A = {
    1: {
        "titulo": "CÉDULA 1 - EL DERECHO Y LA MORAL. NORMAS DE USO SOCIAL",
        "preguntas": [
            {
                "sub": "1.1", "preg": "¿Cuáles son las características principales de la norma moral?",
                "opciones": ["Autónoma, interior, unilateral, incoercible.", "Heterónoma, exterior, bilateral, coercible.", "Exterior, bilateral, incoercible."],
                "correcta": "Autónoma, interior, unilateral, incoercible.",
                "explicacion": "Regula la rectitud íntima de la conciencia y carece de fuerza coactiva estatal."
            },
            {
                "sub": "1.2", "preg": "¿Cuál es la diferencia formal de obligatoriedad entre Derecho y Moral?",
                "opciones": ["El Derecho es coercible y bilateral; la Moral es incoercible y unilateral.", "Ambos son de cumplimiento autónomo e interior.", "El Derecho es unilateral y la Moral es coercible."],
                "correcta": "El Derecho es coercible y bilateral; la Moral es incoercible y unilateral.",
                "explicacion": "El Derecho cuenta con el imperio del aparato público para imponerse de forma coactiva."
            },
            {
                "sub": "1.3", "preg": "¿Qué es conceptualmente una norma de uso o trato social y cuál es su sanción?",
                "opciones": ["Pauta de decoro y cortesía, heterónoma, exterior y unilateral. Sanción: reproche social.", "Mandato jurídico dictado por el Congreso. Sanción: presidio.", "Imperativo puramente autónomo. Sanción: remordimiento."],
                "correcta": "Pauta de decoro y cortesía, heterónoma, exterior y unilateral. Sanción: reproche social.",
                "explicacion": "Proviene del entorno social externo, regula el comportamiento visible y su incumplimiento genera rechazo."
            }
        ]
    },
    2: {
        "titulo": "CÉDULA 2 - LA NORMA JURÍDICA. CARACTERÍSTICAS Y ESTRUCTURA LÓGICA",
        "preguntas": [
            {
                "sub": "2.1", "preg": "¿Cuáles son las características esenciales que configuran a la norma jurídica?",
                "opciones": ["Heterónoma, exterior, bilateral y coercible.", "Autónoma, interior, unilateral e incoercible.", "Heterónoma, interior, unilateral e incoercible."],
                "correcta": "Heterónoma, exterior, bilateral y coercible.",
                "explicacion": "Es dictada por una autoridad superior externa, rige actos manifestados y cuenta con coacción legítima."
            },
            {
                "sub": "2.2", "preg": "¿Cómo operan las normas jurídicas imperativas, prohibitivas y permisivas?",
                "opciones": ["Las imperativas mandan a hacer; las prohibitivas impiden absolutamente; las permisivas facultan o autorizan.", "Las imperativas confieren sugerencias; las prohibitivas aconsejan; las permisivas obligan.", "Todas imponen castigos criminales de manera idéntica sin matices lícitos."],
                "correcta": "Las imperativas mandan a hacer; las prohibitivas impiden absolutamente; las permisivas facultan o autorizan.",
                "explicacion": "Clasificación tradicional según la naturaleza del mandato legal."
            },
            {
                "sub": "2.3", "preg": "¿Cuál es la estructura lógica interna de una norma jurídica ordinaria según la doctrina?",
                "opciones": ["Un juicio hipotético estructurado en: un Supuesto de Hecho y una Consecuencia Jurídica.", "Un juicio categórico imperativo que prescribe un castigo inmediato sin premisas.", "Una sugerencia moral que prescribe conductas meramente deseables."],
                "correcta": "Un juicio hipotético estructurado en: un Supuesto de Hecho y una Consecuencia Jurídica.",
                "explicacion": "Establece que ante la realización fáctica de la hipótesis legal se gatilla el efecto coactivo normativo."
            }
        ]
    },
    3: {
        "titulo": "CÉDULA 3 - VIGENCIA, VALIDEZ Y EFICACIA DE LAS NORMAS JURÍDICAS",
        "preguntas": [
            {
                "sub": "3.1", "preg": "¿Qué define la vigencia formal de una norma en Chile y cómo opera la derogación?",
                "opciones": ["Fuerza obligatoria tras la publicación en el Diario Oficial. Se extingue por otra ley.", "El reconocimiento voluntario de las partes. Se extingue por el desuso social.", "La firma del Presidente de la República. Se extingue por orden judicial."],
                "correcta": "Fuerza obligatoria tras la publicación en el Diario Oficial. Se extingue por otra ley.",
                "explicacion": "La ley obliga desde su publicación. Pierde su fuerza mediante otra ley de forma expresa o tácita."
            },
            {
                "sub": "3.2", "preg": "¿Cómo conceptualizan la validez de la norma la doctrina iusnaturalista y iuspositivista?",
                "opciones": ["Iusnaturalismo exige justicia de fondo; Iuspositivismo exige legalidad formal.", "Iusnaturalismo se basa en la fuerza; Iuspositivismo se basa en contratos privados.", "Ambas escuelas coinciden en que la validez formal depende del arbitrio ciudadano."],
                "correcta": "Iusnaturalismo exige justicia de fondo; Iuspositivismo exige legalidad formal.",
                "explicacion": "El positivismo asocia la validez a la regularidad de producción formal; el iusnaturalismo a la justicia moral."
            },
            {
                "sub": "3.3", "preg": "¿Qué representa técnicamente el concept de eficacia dentro del Derecho positivo?",
                "opciones": ["El grado fáctico y sociológico de cumplimiento real por los destinatarios y aplicación de jueces.", "El proceso burocrático de archivo y numeración de las leyes en ministerios.", "La intención o voluntad interna que tuvo el legislador al redactar."],
                "correcta": "El grado fáctico y sociológico de cumplimiento real por los destinatarios y aplicación de jueces.",
                "explicacion": "La eficacia mide el impacto real de la norma jurídica en los hechos sociales."
            }
        ]
    },
    4: {
        "titulo": "CÉDULA 4 - LA PLENITUD HERMÉTICA DEL ORDENAMIENTO JURÍDICO Y LAS LAGUNAS DEL DERECHO",
        "preguntas": [
            {
                "sub": "4.1", "preg": "Conforme al principio de inexcusabilidad (Art. 76 CPR), ¿cuál es el deber fundamental del juez?",
                "opciones": ["Reclamada su intervención en forma legal, no puede excusarse de fallar ni aun por falta de ley.", "Está facultado para archivar y suspender la causa si no existe un artículo exacto.", "Debe remitir los antecedentes al Parlamento de forma obligatoria."],
                "correcta": "Reclamada su intervención en forma legal, no puede excusarse de fallar ni aun por falta de ley.",
                "explicacion": "El magistrado debe dictar sentencia obligatoriamente, recurriendo a la integración para llenar vacíos."
            },
            {
                "sub": "4.2", "preg": "¿Qué postula técnicamente el concepto dogmático de plenitud hermética?",
                "opciones": ["El ordenamiento como sistema total es completo y provee siempre solución a todo conflicto.", "Las leyes particulares cubren explícitamente todas las transformaciones de la historia.", "El Derecho es un conjunto cerrado de prohibiciones absolutas inaplicables."],
                "correcta": "El ordenamiento como sistema total es completo y provee siempre solución a todo conflicto.",
                "explicacion": "Postula que aunque la ley tenga lagunas específicas, el ordenamiento como todo hermético no posee vacíos."
            },
            {
                "sub": "4.3", "preg": "¿Cómo procede el juez ante una laguna de la ley mediante la integración?",
                "opciones": ["Llena el vacío legal recurriendo a la analogía, principios generales y equidad natural.", "Aplica su propio criterio moral subjetivo de forma libre.", "Dicta un decreto legislativo de común acuerdo con los abogados."],
                "correcta": "Llena el vacío legal recurriendo a la analogía, principios generales y equidad natural.",
                "explicacion": "La integración faculta al juez a extraer una solución armónica desde las premisas y principios del sistema."
            },
            {
                "sub": "4.4", "preg": "¿Cuáles son los criterios lógicos clásicos para resolver antinomias?",
                "opciones": ["Jerarquía (ley superior), Temporalidad (ley posterior) y Especialidad (ley específica).", "Antigüedad del tribunal, cuantía económica y residencia.", "Grado académico de legisladores y orden alfabético."],
