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

DATOS_EXAMEN = {
    1: {
        "titulo": "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
        "preguntas": [
            {
                "sub": "1.1", "preg": "La norma moral, características esenciales.",
                "opciones": ["A) Unilateral, Interior, Autónoma, Incoercible.", "B) Bilateral, Exterior, Heterónoma, Coercible."],
                "correcta": "A) Unilateral, Interior, Autónoma, Incoercible.",
                "explicacion": "Regula el fuero interno del sujeto y no otorga derechos."
            },
            {
                "sub": "1.2", "preg": "Derecho y Moral: diferencias entre ambos órdenes.",
                "opciones": [
                    "A) El Derecho es Coercible y Bilateral; la Moral es Incoercible.",
                    "B) El Derecho es de fuero puramente interno y autónomo."
                ],
                "correcta": "A) El Derecho es Coercible y Bilateral; la Moral es Incoercible.",
                "explicacion": "El Derecho admite el uso de la fuerza pública coactiva estatal."
            },
            {
                "sub": "1.3 a)", "preg": "Normas de uso y trato social: concepto.",
                "opciones": [
                    "A) Pautas de decoro y cortesía dictadas por la sociedad civil.",
                    "B) Mandatos imperativos escritos de forma parlamentaria."
                ],
                "correcta": "A) Pautas de decoro y cortesía dictadas por la sociedad civil.",
                "explicacion": "Consisten en costumbres urbanas variables y no tipificadas."
            },
            {
                "sub": "1.3 b)", "preg": "Normas de uso y trato social: diferencias.",
                "opciones": [
                    "A) Usos sociales acarrean rechazo; las jurídicas castigo estatal.",
                    "B) Los usos confieren acciones legales directas ante tribunales."
                ],
                "correcta": "A) Usos sociales acarrean rechazo; las jurídicas castigo estatal.",
                "explicacion": "La norma jurídica impone multas, privación de libertad o embargos."
            }
        ]
    },
    2: {
        "titulo": "CÉDULA 2.- La norma jurídica.",
        "preguntas": [
            {
                "sub": "2.1", "preg": "La norma jurídica: Características.",
                "opciones": ["A) Heterónoma, Exterior, Bilateral, Coercible.", "B) Autónoma, Interior, Unilateral, Incoercible."],
                "correcta": "A) Heterónoma, Exterior, Bilateral, Coercible.",
                "explicacion": "Emana de autoridad externa, rige actos manifestados y es coactiva."
            },
            {
                "sub": "2.2", "preg": "Clasificación: Normas imperativas vs permisivas.",
                "opciones": [
                    "A) Imperativas ordenan u prohíben; Permisivas conceden opción.",
                    "B) Imperativas otorgan derecho opcional; Permisivas imponen cárcel."
                ],
                "correcta": "A) Imperativas ordenan u prohíben; Permisivas conceden opción.",
                "explicacion": "Imperativas limitan voluntad; permisivas facultan vender la casa."
            },
            {
                "sub": "2.3", "preg": "Estructura lógica de la norma jurídica.",
                "opciones": ["A) Juicio hipotético: Supuesto de Hecho y Consecuencia.", "B) Mandato categórico directo sin hipótesis factuales previas."],
                "correcta": "A) Juicio hipotético: Supuesto de Hecho y Consecuencia.",
                "explicacion": "Si ocurre la hipótesis fáctica, se aplica el efecto legal."
            }
        ]
    },
    3: {
        "titulo": "CÉDULA 3.- Vigencia, validez y eficacia del Derecho positivo.",
        "preguntas": [
            {
                "sub": "3.1 a/b", "preg": "Vigencia: concepto y momento.",
                "opciones": ["A) Fuerza obligatoria; inicia desde la publicación oficial.", "B) Rectitud moral; obliga desde el debate parlamentario."],
                "correcta": "A) Fuerza obligatoria; inicia desde la publicación oficial.",
                "explicacion": "Determina el momento exacto en que el precepto obliga."
            },
            {
                "sub": "3.1 c)", "preg": "La derogación de la ley: clasificación.",
                "opciones": ["A) Pérdida de efectos por otra ley: Expresa, Tácita, Total, Parcial.", "B) Pérdida de validez por el desuso social prolongado."],
                "correcta": "A) Pérdida de efectos por otra ley: Expresa, Tácita, Total, Parcial.",
                "explicacion": "Expresa anula formalmente; Tácita opera por incompatibilidad."
            },
            {
                "sub": "3.2 a)", "preg": "Validez: concepto.",
                "opciones": ["A) Existencia formal y obligatoriedad basada en el sistema.", "B) Grado de cumplimiento sociológico real en la calle."],
                "correcta": "A) Existencia formal y obligatoriedad basada en el sistema.",
                "explicacion": "La validez implica la pertenencia legítima al orden jerárquico."
            },
            {
                "sub": "3.2 b)", "preg": "Fundamentos de validez: doctrinas.",
                "opciones": ["A) Iusnaturalista (justicia) e Iuspositivista (legalidad formal).", "B) Sociológica (fuerza real) and Contractualista privada."],
                "correcta": "A) Iusnaturalista (justicia) e Iuspositivista (legalidad formal).",
                "explicacion": "Positivismo trata la forma; derecho natural exige justicia moral."
            },
            {
                "sub": "3.3", "preg": "Eficacia: concepto.",
                "opciones": ["A) Grado fáctico de acatamiento ciudadano y aplicación judicial.", "B) La mera escrituración formal previa de las normas."],
                "correcta": "A) Grado fáctico de acatamiento ciudadano y aplicación judicial.",
                "explicacion": "La eficacia mide el plano real de obediencia de una norma."
            }
        ]
    },
    4: {
        "titulo": "CÉDULA 4.- La plenitud hermética y las lagunas del Derecho.",
        "preguntas": [
            {
                "sub": "4.1", "preg": "Principio de inexcusabilidad (Art. 76 CPR).",
                "opciones": ["A) Obliga a jueces a resolver conflictos aun sin ley expresa.", "B) Faculta a tribunales a rechazar causas ante vacíos legales."],
                "correcta": "A) Obliga a jueces a resolver conflictos aun sin ley expresa.",
                "explicacion": "El juez debe fallar siempre, integrando el sistema ante vacíos."
            },
            {
                "sub": "4.2", "preg": "Concepto de plenitud hermética.",
                "opciones": ["A) El ordenamiento es completo y provee siempre solución.", "B) Postulado empírico que niega las lagunas en los códigos."],
                "correcta": "A) El ordenamiento es completo y provee siempre solución.",
                "explicacion": "El sistema posee normas de clausura y auto-integración."
            },
            {
                "sub": "4.3", "preg": "Lagunas del Derecho; solución judicial.",
                "opciones": ["A) Vacío legal; el juez integra mediante analogía y equidad.", "B) Choque de artículos; el juez deriva de forma obligatoria."],
                "correcta": "A) Vacío legal; el juez integra mediante analogía y equidad.",
                "explicacion": "La integración faculta al magistrado a construir la regla de fallo."
            },
            {
                "sub": "4.4", "preg": "Conflicto entre normas: criterios.",
                "opciones": ["A) Se resuelve mediante: Jerarquía, Especialidad y Temporalidad.", "B) Se resuelve ponderando el costo o volumen del expediente."],
                "correcta": "A) Se resuelve mediante: Jerarquía, Especialidad y Temporalidad.",
                "explicacion": "Jerarquía (superior prima), Especialidad (especial), Temporalidad (posterior)."
            }
        ]
    },
    5: {
        "titulo": "CÉDULA 5.- Fuentes del ordenamiento izquierdo.",
        "preguntas": [
            {
                "sub": "5.1", "preg": "Concepto y tipos de fuente.",
                "opciones": ["A) Materiales: factores sociales; Formales: modos obligatorios.", "B) Materiales: códigos; Formales: discursos parlamentarios."],
                "correcta": "A) Materiales: factores sociales; Formales: modos obligatorios.",
                "explicacion": "Material es la causa real; formal es el canal dotado de imperio."
            },
            {
                "sub": "5.2", "preg": "Fuentes formales: clasificación.",
                "opciones": ["A) CPR, Ley, Tratados, Reglamentos, Costumbre, Jurisprudencia.", "B) Se reducen exclusivamente a la legislación parlamentaria."],
                "correcta": "A) CPR, Ley, Tratados, Reglamentos, Costumbre, Jurisprudencia.",
                "explicacion": "El derecho positivo consagra un orden jerárquico de producción."
            },
            {
                "sub": "5.3 a/b/c", "preg": "La ley: concepto, elementos y características.",
                "opciones": ["A) Declaración de voluntad soberana que manda, prohíbe o permite.", "B) Mandato coyuntural judicial para dirimir un litigio privado."],
                "correcta": "A) Declaración de voluntad soberana que manda, prohíbe o permite.",
