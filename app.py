import streamlit as st
import datetime

# CONFIGURACIÓN GENERAL DE LA INTERFAZ
st.set_page_config(page_title="EXAMINADOR", layout="centered")

# SISTEMA DE CADUCIDAD SOLICITADO
if datetime.date.today() > datetime.date(2026, 6, 30):
    st.error("⏳ Licencia caducada. Disponible hasta el 30 de junio de 2026.")
    st.stop()

# ENCABEZADO FORMAL INSTITUTIONAL
st.markdown("<h1 style='text-align:center; color: #1E3A8A;'>EXAMINADOR DE TEORÍA DEL DERECHO</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color: #4B5563;'>Profesor Jaime Esponda</h3>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### ℹ️ Credenciales")
    st.caption("Método Cognuss II\n\nDesarrollado por Miguel López Lavados")

st.divider()

# CEDULARIO OFICIAL COMPLETO DESGLOSADO POR SUBPUNTOS EXACTOS
DATOS_EXAMEN = {
    1: {
        "titulo": "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
        "preguntas": [
            {
                "sub": "1.1", 
                "preg": "En relación a las características de la norma moral, ¿cuál de las siguientes combinaciones es correcta?",
                "opciones": [
                    "A) Es unilateral (no faculta a un tercero), interior (regula intenciones), autónoma e incoercible.",
                    "B) Es bilateral (otorga facultades judiciales), exterior, heterónoma y enteramente coercible."
                ],
                "correcta": "A) Es unilateral (no faculta a un tercero), interior (regula intenciones), autónoma e incoercible.",
                "explicacion": "La norma moral apela estrictamente a la conciencia individual (fuero interno) y carece de sanción institucional por la fuerza pública."
            },
            {
                "sub": "1.2", 
                "preg": "Frente al paralelo estructural entre ambos órdenes, ¿cuál es la distinción formal de obligatoriedad entre Derecho y Moral?",
                "opciones": [
                    "A) El Derecho regula conductas manifestadas (exterior) y es coercible; la Moral rige intenciones (interior) y es incoercible.",
                    "B) El Derecho es unilateral y carece de imperio; la Moral concede acciones judiciales colectivas exigibles ante los tribunales chilenos."
                ],
                "correcta": "A) El Derecho regula conductas manifestadas (exterior) y es coercible; la Moral rige intenciones (interior) y es incoercible.",
                "explicacion": "Conforme al documento USS, el Derecho cuenta con el aparato estatal de coacción legítima; la Moral opera de forma autónoma en el sujeto."
            },
            {
                "sub": "1.3 a)", 
                "preg": "¿Cuál es el concepto doctrinal exacto que define a las normas de uso o trato social (usos sociales)?",
                "opciones": [
                    "A) Son pautas de decoro, cortesía y urbanidad dictadas de manera difusa por la colectividad o grupo social.",
                    "B) Son mandatos jurídicos expresos escritos y tipificados en los códigos sustantivos civiles y procesales por el parlamento."
                ],
                "correcta": "A) Son pautas de decoro, cortesía y urbanidad dictadas de manera difusa por la colectividad o grupo social.",
                "explicacion": "Los usos sociales consisten en prácticas de convivencia común variables, tales como el saludo o las reglas de vestimenta en ciertas instancias."
            },
            {
                "sub": "1.3 b)", 
                "preg": "¿Cuáles son las características esenciales de los usos sociales y su diferencia formal con la norma jurídica?",
                "opciones": [
                    "A) Los usos sociales son heterónomos, exteriores y unilaterales (su sanción es el reproche social); las jurídicas son coercibles institucionales.",
                    "B) Los usos sociales otorgan facultades jurídicas exigibles a terceros; las normas del Derecho imponen únicamente el remordimiento íntimo."
                ],
                "correcta": "A) Los usos sociales son heterónomos, exteriores y unilaterales (su sanción es el reproche social); las jurídicas son coercibles institucionales.",
                "explicacion": "La norma jurídica cuenta con sanciones institucionalizadas (multa, embargo, prisión); el uso social se castiga con el aislamiento o reprobación social."
            }
        ]
    },
    2: {
        "titulo": "CÉDULA 2.- La norma jurídica.",
        "preguntas": [
            {
                "sub": "2.1", 
                "preg": "¿Cuáles son las notas constitutivas y esenciales que caracterizan a la norma jurídica?",
                "opciones": [
                    "A) Es heterónoma (autoridad externa), exterior, bilateral (correlativa de derechos y deberes) y potencialmente coercible.",
                    "B) Es puramente autónoma, interior, unilateral en sus efectos y de observancia incoercible u optativa por el sujeto obligado."
                ],
                "correcta": "A) Es heterónoma (autoridad externa), exterior, bilateral (correlativa de derechos y deberes) y potencialmente coercible.",
                "explicacion": "A diferencia de otros ordenamientos, la bilateralidad implica que frente al obligado siempre existe un sujeto facultado para exigir legalmente el cumplimiento."
            },
            {
                "sub": "2.2", 
                "preg": "Respecto al criterio del mandato principal, ¿cómo opera la clasificación entre normas imperativas y permisivas?",
                "opciones": [
                    "A) Las Imperativas ordenan o prohíben una conducta sin admitir pacto en contrario; las Permisivas confieren una aptitud legítima u opción de actuar.",
                    "B) Las Imperativas confieren un consejo optativo; las Permisivas anulan de manera absoluta el texto general de la Constitución Política."
                ],
                "correcta": "A) Las Imperativas ordenan o prohíben una conducta sin admitir pacto en contrario; las Permisivas confieren una aptitud legítima u opción de actuar.",
                "explicacion": "Ejemplo oficial: La prohibición de compraventa entre cónyuges no separados judicialmente es imperativa; la facultad del dueño de vender su propiedad es permisiva."
            },
            {
                "sub": "2.3", 
                "preg": "¿Cuál es la estructura lógica interna de una norma jurídica ordinaria de acuerdo a la doctrina clásica?",
                "opciones": [
                    "A) Se compone formalmente como un juicio hipotético que enlaza un Supuesto de Hecho (hipótesis fáctica) con una Consecuencia Jurídica (efecto o sanción).",
                    "B) Consiste en una orden de carácter categórico absoluto que prescribe un castigo inmediato sin contemplar ninguna hipótesis de conducta previa."
                ],
                "correcta": "A) Se compone formalmente como un juicio hipotético que enlaza un Supuesto de Hecho (hipótesis fáctica) con una Consecuencia Jurídica (efecto o sanción).",
                "explicacion": "Sigue la premisa formal: si se realiza fácticamente la hipótesis contemplada por el legislador, debe aplicarse el efecto o sanción decretado en la norma."
            }
        ]
    },
    3: {
        "titulo": "CÉDULA 3.- Vigencia, validez y eficacia del Derecho positivo.",
        "preguntas": [
            {
                "sub": "3.1 a/b", 
                "preg": "¿Qué define formalmente el concepto de vigencia y en qué momento principia de acuerdo a las reglas generales en Chile?",
                "opciones": [
                    "A) Es la fuerza obligatoria formal de la ley; principia por regla general a partir de su publicación material en el Diario Oficial.",
                    "B) Es la justicia interna y moral de la norma; principia desde el momento de la discusión técnica en las salas de comisiones parlamentarias."
                ],
                "correcta": "A) Es la fuerza obligatoria formal de la ley; principia por regla general desde su publicación material en el Diario Oficial.",
                "explicacion": "La vigencia determina el marco de obligatoriedad temporal del precepto legal positivo, vinculando a todos los habitantes de la República."
            },
            {
                "sub": "3.1 c)", 
                "preg": "En relación a la pérdida de vigencia, ¿cuál es el concepto técnico de derogación de la ley y cómo se clasifica doctrinalmente?",
                "opciones": [
                    "A) Es la pérdida de efectos por obra de otra ley posterior; se clasifica en Expresa o Tácita, y en Total o Parcial.",
                    "B) Es la anulación formal por desuso o desobediencia civil colectiva; se clasifica en Absoluta o Fáctica según la materia civil."
                ],
                "correcta": "A) Es la pérdida de efectos por obra de otra ley posterior; se clasifica en Expresa o Tácita, y en Total o Parcial.",
                "explicacion": "Expresa cuando la nueva ley lo declara; Tácita cuando contiene disposiciones incompatibles con la ley antigua; Parcial si altera solo algunos artículos."
            },
            {
                "sub": "3.2 a)", 
                "preg": "¿Cómo se conceptualiza de forma técnica la validez de las normas jurídicas dentro del ordenamiento positivo?",
                "opciones": [
                    "A) Es la existencia formal y obligatoriedad específica de la norma fundamentada en su conformidad con las reglas superiores del sistema.",
                    "B) Es el grado efectivo de cumplimiento material, espontáneo y sociológico que exhibe un grupo social ante un artículo de un código."
                ],
                "correcta": "A) Es la existencia formal y obligatoriedad específica de la norma fundamentada en su conformidad con las reglas superiores del sistema.",
