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

# BASE DE DATOS REAL EXTRAÍDA DE LAS TABLAS DEL PDF USS
DATOS_EXAMEN = {
    1: {
        "titulo": "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
        "preguntas": [
            {
                "sub": "1.1", "preg": "La norma moral, características esenciales.",
                "opciones": [
                    "A) Unilateral, Interior, Autónoma, Incoercible.",
                    "B) Bilateral, Exterior, Heterónoma, Coercible."
                ],
                "correcta": "A) Unilateral, Interior, Autónoma, Incoercible.",
                "explicacion": "Regula el fuero interno del sujeto y no otorga derechos correlativos a otra persona."
            },
            {
                "sub": "1.2", "preg": "Derecho y Moral: diferencias estructurales entre ambos órdenes.",
                "opciones": [
                    "A) El Derecho es Coercible y Bilateral; la Moral es Incoercible y Unilateral.",
                    "B) El Derecho es de fuero puramente interno, autónomo e incoercible."
                ],
                "correcta": "A) El Derecho es Coercible y Bilateral; la Moral es Incoercible y Unilateral.",
                "explicacion": "El Derecho admite el uso de la fuerza pública (ej. desalojo); la Moral se sanciona con culpa o remordimiento interna."
            },
            {
                "sub": "1.3 a)", "preg": "Normas de uso y trato social: concepto doctrinal.",
                "opciones": [
                    "A) Son pautas de decoro, cortesía y urbanidad dictadas por la sociedad civil de forma difusa.",
                    "B) Son mandatos obligatorios escritos y tipificados previamente en un cuerpo legal por el Estado."
                ],
                "correcta": "A) Son pautas de decoro, cortesía y urbanidad dictadas por la sociedad civil de forma difusa.",
                "explicacion": "Consisten en modales o costumbres urbanas cuya determinación es variable según la época o grupo social."
            },
            {
                "sub": "1.3 b)", "preg": "Normas de uso y trato social: características y diferencias con la norma jurídica.",
                "opciones": [
                    "A) Los usos sociales acarrean rechazo o aislamiento social y son unilaterales; las de Derecho conllevan castigo institucional.",
                    "B) Los usos sociales confieren acciones legales directas ante tribunales para exigir el saludo obligatorio."
                ],
                "correcta": "A) Los usos sociales acarrean rechazo o aislamiento social y son unilaterales; las de Derecho conllevan castigo institucional.",
                "explicacion": "La norma jurídica aplica multas, privación de libertad o embargos a través de las instituciones del Estado."
            }
        ]
    },
    2: {
        "titulo": "CÉDULA 2.- La norma jurídica.",
        "preguntas": [
            {
                "sub": "2.1", "preg": "La norma jurídica: Características esenciales.",
                "opciones": [
                    "A) Heterónoma, Exterior, Bilateral, Coercible.",
                    "B) Autónoma, Interior, Unilateral, Incoercible."
                ],
                "correcta": "A) Heterónoma, Exterior, Bilateral, Coercible.",
                "explicacion": "Emana de la potestad del legislador, rige actos manifestados y confiere facultades de exigibilidad correlativas."
            },
            {
                "sub": "2.2", "preg": "Clasificación entre normas jurídicas imperativas (y prohibitivas) y permisivas (o facultativas).",
                "opciones": [
                    "A) Las Imperativas ordenan o prohíben absolutamente sin margen de voluntad; las Permisivas conceden una aptitud legítima u opción.",
                    "B) Las Imperativas otorgan un derecho plenamente renunciable; las Permisivas imponen cárcel inmediata ante su desuso."
                ],
                "correcta": "A) Las Imperativas ordenan o prohíben absolutamente sin margen de voluntad; las Permisivas conceden una aptitud legítima u opción.",
                "explicacion": "Ejemplo del PDF: Es imperativa la prohibición de compraventa entre cónyuges; es permisiva la facultad del dueño de vender o no su casa."
            },
            {
                "sub": "2.3", "preg": "Estructura lógica de la norma jurídica ordinaria.",
                "opciones": [
                    "A) Se compone formalmente como un juicio hipotético estructurado en: un Supuesto de Hecho y una Consecuencia Jurídica.",
                    "B) Consiste en una orden de castigo directa que opera fácticamente sin describir ninguna circunstancia o hipótesis previa."
                ],
                "correcta": "A) Se compone formalmente como un juicio hipotético estructurado en: un Supuesto de Hecho y una Consecuencia Jurídica.",
                "explicacion": "Establece técnicamente que ante la realización de la hipótesis prevista en la ley se activa obligatoriamente la consecuencia legal."
            }
        ]
    },
    3: {
        "titulo": "CÉDULA 3.- Vigencia, validez y eficacia del Derecho positivo.",
        "preguntas": [
            {
                "sub": "3.1 a/b", "preg": "Vigencia: concepto y momento de la vigencia en la legislación nacional.",
                "opciones": [
                    "A) Es la fuerza obligatoria formal de la ley; principia por regla general desde su publicación en el Diario Oficial.",
                    "B) Es el valor de la justicia interna; obliga de forma inmediata desde su firma privada en las notarías."
                ],
                "correcta": "A) Es la fuerza obligatoria formal de la ley; principia por regla general desde su publicación en el Diario Oficial.",
                "explicacion": "La vigencia determina el marco temporal formal a partir del cual el precepto positivo obliga a todos los habitantes."
            },
            {
                "sub": "3.1 c)", "preg": "La derogación de la ley: concepto y clasificación doctrinaria.",
                "opciones": [
                    "A) Pérdida de efectos por otra ley. Se clasifica en: Expresa, Tácita, Total y Parcial.",
                    "B) Pérdida de obligatoriedad por mutuo acuerdo. Se clasifica en: Absoluta y Relativa fáctica."
                ],
                "correcta": "A) Pérdida de efectos por otra ley. Se clasifica en: Expresa, Tácita, Total y Parcial.",
                "explicacion": "Expresa lo declara; Tácita opera por incompatibilidad de preceptos; Parcial elimina solo algunas disposiciones o incisos."
            },
            {
                "sub": "3.2 a)", "preg": "Validez de las normas jurídicas: concepto técnico.",
                "opciones": [
                    "A) Conformidad con las normas superiores que determina su pertenencia y obligatoriedad dentro del sistema.",
                    "B) El grado fáctico de cumplimiento material espontáneo que exhiben los ciudadanos ante un código."
                ],
                "correcta": "A) Conformidad con las normas superiores que determina su pertenencia y obligatoriedad dentro del sistema.",
                "explicacion": "La validez implica la existencia formal de la norma fundamentada en la jerarquía legal."
            },
            {
                "sub": "3.2 b)", "preg": "Fundamentos de la validez y presupuestos de legitimidad: en qué consisten las dos principales doctrinas.",
                "opciones": [
                    "A) Doctrina Iusnaturalista (fundada en la justicia material y moral universales) y Doctrina Iuspositivista (legalidad formal).",
                    "B) Doctrina Sociológica (acatamiento fáctico) y Doctrina Contractualista de relaciones privadas internacionales."
                ],
                "correcta": "A) Doctrina Iusnaturalista (fundada en la justicia material y moral universales) y Doctrina Iuspositivista (legalidad formal).",
                "explicacion": "El positivismo asocia la validez a que sea creada por órgano competente y proceso formal; el derecho natural a que sea justa."
            },
            {
                "sub": "3.3", "preg": "Eficacia de las normas del Derecho positivo: concepto sociológico.",
                "opciones": [
                    "A) Es una condición fáctica: representa el grado real de cumplimiento por sus destinatarios y de aplicación por los jueces.",
                    "B) Consiste en el correcto archivo y numeración secuencial de los proyectos legislativos aprobados por el parlamento."
                ],
                "correcta": "A) Es una condición fáctica: representa el grado real de cumplimiento por sus destinatarios y de aplicación por los jueces.",
                "explicacion": "Mide el plano sociológico y empírico: representa si la ley es efectivamente obedecida y respetada en la realidad práctica de la sociedad."
            }
        ]
    },
    4: {
        "titulo": "CÉDULA 4.- La plenitud hermética del ordenamiento jurídico y las lagunas del Derecho.",
        "preguntas": [
            {
                "sub": "4.1", "preg": "Introducción constitucional: principio de inexcusabilidad (Art. 76 CPR / Art. 10 COT).",
                "opciones": [
                    "A) Obliga a los jueces a resolver conflictos aun sin ley expresa que regule el caso, recurriendo a principios generales.",
