DATOS_EXAMEN = {
    1: {
        "titulo": "CÉDULA 1.- El Derecho y la Moral. Normas de uso y trato social.",
        "preguntas": [
            {
                "sub": "1.1", "preg": "¿Cuáles son las características principales de la norma moral?",
                "opciones": ["A) Autónoma, interior, unilateral e incoercible.", "B) Heterónoma, exterior, bilateral y coercible."],
                "correcta": "A) Autónoma, interior, unilateral e incoercible.", "explicacion": "Nace del propio sujeto, regula el fuero interno y es incoercible."
            },
            {
                "sub": "1.2", "preg": "Respecto a las diferencias entre Derecho y Moral, ¿cuál es CORRECTA?",
                "opciones": ["A) El Derecho es coercible mientras que la Moral es incoercible.", "B) El Derecho es unilateral y la Moral es bilateral."],
                "correcta": "A) El Derecho es coercible mientras que la Moral es incoercible.", "explicacion": "El Derecho cuenta con el aparato coactivo del Estado."
            }
        ]
    },
    2: {
        "titulo": "CÉDULA 2.- La Norma Jurídica. Características. Estructura lógica.",
        "preguntas": [
            {
                "sub": "2.1", "preg": "¿Cuáles son las características esenciales de la norma jurídica?",
                "opciones": ["A) Es heterónoma, exterior, bilateral y coercible.", "B) Es autónoma, interior y carente de sanción."],
                "correcta": "A) Es heterónoma, exterior, bilateral y coercible.", "explicacion": "Proviene de autoridad externa y es imponible por la fuerza."
            }
        ]
    }
}

# Habilitar el resto de las cédulas de forma limpia
for i in range(3, 15):
    DATOS_EXAMEN[i] = {"titulo": f"CÉDULA {i}.- (Pendiente de traspaso de contenidos)", "preguntas": []}
