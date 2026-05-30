import streamlit as st

st.set_page_config(layout="centered")

CEDULAS = [
    "CEDULA 1.- El Derecho y la Moral. Normas de uso y trato social. 1.1. La norma moral, características. 1.2. Derecho y Moral: diferencias entre ambos órdenes. 1.3. Normas de uso y trato social: a) concepto. b) características y diferencias con la norma jurídica.",
    "CEDULA 2.-La norma jurídica. 2.1. Características. 2.2. Classification entre normas jurídicas imperativas y permisivas. 2.3. Estructura lógica de la norma jurídica",
    "CEDULA 3.- Vigencia, validez y eficacia del Derecho positivo. 3.1. Vigencia a) concepto b) momento de la vigencia. c) la derogación de la ley: concepto y clasificación. 3.2. Validez a) concepto b) fundamentos de la validez del Derecho y presupuestos últimos de su legitimidad: en qué consisten las dos principales doctrinas. 3.3. Eficacia: concepto.",
    "CEDULA 4.- La plenitud hermética del ordenamiento jurídico y las lagunas del Derecho. 4.1. Introducción constitucional: principio de inexcusabilidad. 4.2 Concepto de plenitud hermética del ordenamiento jurídico. 4.3. Casos en que se observan lagunas del Derecho; solución judicial. 4.4. Conflicto entre normas jurídicas positivas (del mismo nivel jerárquico y de diverso nivel jerárquico): criterios de solución judicial.",
    "CEDULA 5.- Fuentes del ordenamiento jurídico. 5.1. Concepto y tipos de fuente (materiales y formales) 5.2. Fuentes formales del Derecho: clasificación. 5.3. La ley: a) concepto b) elementos c) características d) efectos de la ley en cuanto al espacio e) efectos de la ley en cuanto al tiempo.",
    "CEDULA 6.- La costumbre. 6.1. La costumbre a) concepto b) elementos. 6.2. La costumbre en el Derecho Civil, el Derecho Comercial, el Derecho Internacional Público, el Derecho Penal y el Derecho Procesal.",
    "CEDULA 7.-La jurisprudencia y la doctrina, como fuentes formales del Derecho. 7.1. La jurisprudencia a) concepto b) la norma del Código Civil y la práctica de los tribunales chilenos. 7.2. La doctrina a) concepto b) la discusión sobre su carácter de fuente formal del Derecho.",
    "CEDULA 8. La Relación Jurídica. 8.1. a) concepto b) elementos 8.2. La persona, sujeto de la relación jurídica. La persona natural. Principio y fin de su existencia.",
    "CEDULA 9. La persona jurídica. 9.1. Concepto. 9.2. Tipos de personas jurídicas. a) de Derecho Público y b) de Derecho Privado. 9.3. Responsabilidad de las personas jurídicas: a) responsabilidad civil: contractual y extracontractual (delictual o cuasi delictual). Alcance de la responsabilidad de las personas jurídicas por actos de sus dependientes. 9.4. Responsabilidad penal de las personas jurídicas. LEY N° 21.595.",
    "CEDULA 10.- Derechos reales y derechos personales. 10.1. Derecho real. Concepto. Principales derechos reales (derecho de dominio o propiedad, derecho real de herencia), demás derechos reales (de usufructo, de uso y habitación) conceptos y facultades que comprende cada uno. 10.2. Derecho personal. Concepto. Elementos.",
    "CEDULA 11.- Límites en el ejercicio de los derechos subjetivos y el abuso del derecho. 11.1. Limitaciones intrínsecas y extrínsecas de los derechos. a) Limitaciones intrínsecas: la buena fe, otras limitaciones. b) Limitaciones extrínsecas.",
    "CEDULA 12. Los bienes (o cosas). Clasificación. 12.1. Bienes muebles: por naturaleza y por anticipación. Bienes muebles semovientes e inanimados. Registro de los bienes muebles. 12.2. Bienes inmuebles. Concepto. a) Bienes inmuebles por naturaleza y por adherencia o destinación.",
    "CEDULA 13. 13.1. Diferente régimen jurídico de los bienes muebles e inmuebles. 13.2. Cosas registrables y no registrables. 13.3. Cosas (o bienes) específicas y genéricas.",
    "CEDULA 14. Bienes o cosas comerciables e incomerciables. 14.1. Cosas comerciables e incomerciables (subclasificación) . 14.2. Bienes nacionales de uso público (concesiones) y bienes fiscales (el Fisco)."
]

PREGUNTAS = [
    ["1.1. La norma moral, características.", "1.2. Derecho y Moral: diferencias entre ambos órdenes.", "1.3. Normas de uso y trato social: a) concepto. b) características y diferencias con la norma jurídica."],
    ["2.1. Características.", "2.2. Clasificación entre normas jurídicas imperativas y permisivas.", "2.3. Estructura lógica de la norma jurídica"],
    ["3.1. Vigencia a) concepto b) momento de la vigencia. c) la derogación de la ley: concepto y clasificación.", "3.2. Validez a) concepto b) fundamentos de la validez del Derecho y presupuestos últimos de su legitimidad: en qué consisten las dos principales doctrinas.", "3.3. Eficacia: concepto."],
    ["4.1. Introducción constitucional: principio de inexcusabilidad.", "4.2 Concepto de plenitud hermética del ordenamiento jurídico.", "4.3. Casos en que se observan lagunas del Derecho; solución judicial.", "4.4. Conflicto entre normas jurídicas positivas (del mismo nivel jerárquico y de diverso nivel jerárquico): criterios de solución judicial."],
    ["5.1. Concepto y tipos de fuente (materiales y formales)", "5.2. Fuentes formales del Derecho: clasificación.", "5.3. La ley: a) concepto b) elementos c) características d) efectos de la ley en cuanto al espacio e) efectos de la ley en cuanto al tiempo."],
    ["6.1. La costumbre a) concepto b) elementos.", "6.2. La costumbre en el Derecho Civil, el Derecho Comercial, el Derecho Internacional Público, el Derecho Penal y el Derecho Procesal."],
    ["7.1. La jurisprudencia a) concepto b) la norma del Código Civil y la práctica de los tribunales chilenos.", "7.2. La doctrina a) concepto b) la discusión sobre su carácter de fuente formal del Derecho."],
    ["8.1. a) concepto b) elementos", "8.2. La persona, sujeto de la relación jurídica. La persona natural. Principio y fin de su existencia."],
    ["9.1. Concepto.", "9.2. Tipos de personas jurídicas. a) de Derecho Público y b) de Derecho Privado.", "9.3. Responsabilidad de las personas jurídicas: a) responsabilidad civil: contractual y extracontractual (delictual o cuasi delictual). Alcance de la responsabilidad de las personas jurídicas por actos de sus dependientes.", "9.4. Responsabilidad penal de las personas jurídicas. LEY N° 21.595."],
    ["10.1. Derecho real. Concepto. Principales derechos reales (derecho de dominio o propiedad, derecho real de herencia), demás derechos reales (de usufructo, de uso y habitación) conceptos y facultades que comprende cada uno.", "10.2. Derecho personal. Concepto. Elementos."],
    ["11.1. Limitaciones intrínsecas y extrínsecas de los derechos. a) Limitaciones intrínsecas: la buena fe, otras limitaciones. b) Limitaciones extrínsecas."],
    ["12.1. Bienes muebles: por naturaleza y por anticipación. Bienes muebles semovientes e inanimados. Registro de los bienes muebles.", "12.2. Bienes inmuebles. Concepto. a) Bienes inmuebles por naturaleza y por adherencia o destinación."],
    ["13.1. Diferente régimen jurídico de los bienes muebles e inmuebles.", "13.2. Cosas registrables y no registrables.", "13.3. Cosas (o bienes) específicas y genéricas."],
    ["14.1. Cosas comerciables e incomerciables (subclasificación) .", "14.2. Bienes nacionales de uso público (concesiones) y bienes fiscales (el Fisco)."]
]

seleccion = st.selectbox(
    "Seleccione Cédula",
    options=list(range(1, 15)),
    format_func=lambda x: f"Cédula {x:02d}"
)

idx = seleccion - 1

st.markdown(f"**{CEDULAS[idx]}**")

for subpregunta in PREGUNTAS[idx]:
    st.write(subpregunta)
