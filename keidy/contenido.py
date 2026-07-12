# contenido.py

# ================================================================
#  CONFIGURACIÓN DE RUTAS
# ================================================================
CARPETA_IMAGENES = "imagenes"

# Gráficos del informe: cada uno indica tras qué sección va (anclas: "ubicacion" | "estructura")
GRAFICOS = [
    {"numero": 1, "tras": "ubicacion", "titulo": "Gráfico 1. Representación cartográfica y ubicación espacial de la empresa.", "ancho_cm": 5, "lista": "Representación cartográfica y ubicación espacial de la empresa", "pagina": "3"},
    {"numero": 2, "tras": "estructura", "titulo": "Gráfico 2. Organigrama estructural y niveles jerárquicos de la organización.", "ancho_cm": 12, "lista": "Organigrama estructural y niveles jerárquicos de la organización", "pagina": "4"},
]

# Textos introductorios del Capítulo II
PLANIFICACION_INTRO_TEXTO = "La planificación establece la relación entre cada objetivo específico y las actividades técnicas a ejecutar para el desarrollo de la propuesta de optimización:"
CRONOGRAMA_INTRO_TEXTO = "El cronograma estructura temporalmente las fases de diagnóstico, análisis y diseño de la propuesta, distribuidas a lo largo de las seis (6) semanas de duración de la pasantía:"

# Título del Cuadro 2 (Cronograma)
CUADRO_CRONOGRAMA_TITULO = "Cuadro 2. Cronograma de actividades del proyecto."

# Lista de Cuadros (índice preliminar): (número, descripción, página)
CUADROS_INDICE = [
    ("1", "Planificación integral de objetivos específicos", "5"),
    ("2", "Cronograma de actividades del proyecto", "6"),
]

# ================================================================
#  DATOS DE LA PORTADA
# ================================================================
MEMBRETE = [
    "REPÚBLICA BOLIVARIANA DE VENEZUELA",
    "MINISTERIO DEL PODER POPULAR PARA LA EDUCACIÓN",
    "INSTITUTO UNIVERSITARIO DE TECNOLOGÍA",
    "\"ELÍAS CALIXTO POMPA\" (IUTECP)",
    "EL TIGRE, ESTADO ANZOÁTEGUI"
]

TITULO_PROYECTO = "PROPUESTA DE OPTIMIZACIÓN DEL PROCESO DE PROCURA EN EL DEPARTAMENTO ADMINISTRATIVO DE LUBRICANTES Y EQUIPOS VARYNA, C.A."
AUTOR_DATOS = [
    "Autor: Keidy Guzmán",
    "C.I.: 28.706.352",
    "",
    "Tutor Industrial: [Nombre del Tutor Industrial]",
    "C.I.: [Cédula del Tutor Industrial]",
    "",
    "Tutor Académico: [Nombre del Tutor Académico]",
    "C.I.: [Cédula del Tutor Académico]"
]
FECHA_LUGAR = "El Tigre, julio de 2026"

# ================================================================
#  PÁGINAS PRELIMINARES
# ================================================================
DEDICATORIA = "Aquí va la dedicatoria."

AGRADECIMIENTOS = "Aquí van los agradecimientos."

RESUMEN_TEXTO = (
    "Aquí va el resumen del informe. El presente informe describe la propuesta de optimización del proceso "
    "de procura en el departamento administrativo de Lubricantes y Equipos Varyna, C.A. La investigación se "
    "enmarca en la modalidad de proyecto factible apoyado en un diagnóstico de campo. [Completar con el resto "
    "del resumen: objetivo general, metodología, resultados y conclusiones principales.]"
)

PALABRAS_CLAVE = "procura, optimización, proceso administrativo, proyecto factible, pasantías."

INTRODUCCION_TEXTO = (
    "Aquí va la introducción. La presente pasantía, desarrollada como requisito para optar al título de Técnico "
    "Superior Universitario en Administración, tiene como propósito proponer mejoras procedimentales para "
    "optimizar el proceso de procura en el departamento administrativo de Lubricantes y Equipos Varyna, C.A. "
    "[Completar con la estructura del informe: capítulos, enfoque metodológico y alcance.]"
)

# ================================================================
#  DATOS DE LA EMPRESA (CAPÍTULO I)
# ================================================================
RAZON_SOCIAL = "Lubricantes y Equipos Varyna, C.A."

IDENTIFICACION_EMPRESA = (
    "La práctica profesional se desarrolla en Lubricantes y Equipos Varyna, C.A., empresa venezolana con más "
    "de treinta y seis (36) años de trayectoria en el sector petrolero, industrial y de construcción.Su actividad "
    "principal se enfoca en el procesamiento y suministro de productos químicos especializados, el tratamiento "
    "de crudo y la provisión de maquinaria pesada para operaciones industriales."
)

RESENA_HISTORICA = [
    "Lubricantes y Equipos Varyná C.A. es una empresa venezolana con más de treinta y seis (36) años de trayectoria en el sector petrolero, industrial y de construcción, consolidándose como una organización de amplia experiencia y reconocimiento dentro del mercado nacional. Desde sus inicios, la empresa ha orientado sus esfuerzos al desarrollo de soluciones integrales que contribuyan al fortalecimiento de las actividades productivas del país.",
    "Como empresa integrante del Grupo Corporativo VTC, ha profesionalizado un crecimiento sostenido basado en la innovación, la calidad de sus servicios y el compromiso con sus clientes. Su actividad principal se enfoca en el procesamiento y suministro de productos químicos especializados, el tratamiento de crudo y la provisión de maquinaria pesada para operaciones industriales."
]

MISION = "Brindar a nuestros clientes objetivos, soluciones de calidad en las áreas en las cuales nos desempeñamos, para contribuir de manera significativa en sus resultados. Aportando valor con nuestras respuestas a sus requerimientos. En la búsqueda de un mejor país y de una mejor humanidad."
VISION = "Ser el conglomerado de empresas líderes en cada una de las categorías en las que participamos, generando modelos de negocios altamente competitivos, atendiendo a nuestros distintos beneficiarios con productos y servicios de calidad."

VALORES = [
    ("Planificación", "Estructuración anticipada de las adquisiciones para optimizar los recursos financieros de la organización."),
    ("Responsabilidad", "Cumplimiento eficiente de los compromisos adquiridos con clientes, proveedores y trabajadores."),
    ("Integridad", "Actuar con honestidad, ética y transparencia en todas las operaciones de la empresa."),
    ("Transparencia", "Garantizar la trazabilidad y la claridad en los procesos de selección y adjudicación de compras.")
]

OBJETIVOS_ORG = [
    "Proporcionar soluciones eficientes y oportunas a las necesidades de sus clientes.",
    "Mantener altos estándares de calidad en los productos y servicios ofrecidos.",
    "Asegurar el abastecimiento continuo y eficiente de insumos mediante una gestión administrativa transparente."
]

UBICACION = "Calle 23 de enero entre calle principal el palomar y calle la paz sector vista al sol, San José de Guanipa Edo. Anzoátegui."

POBLACION = [
    "La población de trabajadores de Lubricantes y Equipos Varyná C.A. está conformada por personal administrativo, técnico y operativo. Toda la empresa trabaja de manera coordinada para garantizar la calidad de los servicios prestados, recayendo sobre el área de procura administrativa la responsabilidad de asegurar la disponibilidad oportuna de materiales y repuestos para la continuidad operativa."
]

ORGANIGRAMA_TEXTO = "A continuación, se presenta la estructura organizativa de la empresa, reflejando las líneas de mando y la distribución de los departamentos administrativos y de procura:"

# ================================================================
#  DIAGNÓSTICO SITUACIONAL (CAPÍTULO II)
# ================================================================
SITUACION_PROBLEMATICA = [
    "En el departamento administrativo de Lubricantes y Equipos Varyna, C.A., se ha identificado una situación desfavorable relacionada con el control y flujo procedimental de la procura. En la actualidad, las solicitudes de compras de materiales e insumos críticos presentan marcados retrasos debido a la ausencia de un canal formalizado de recepción, lo que ocasiona que las requisiciones no sigan una ruta clara de procesamiento.",
    "Esta falta de estandarización administrativa genera cuellos de botella en las instancias de aprobación, pérdida de trazabilidad en el seguimiento de las cotizaciones y tiempos prolongados para la adquisición definitiva de los insumos. Como consecuencia directa, se producen retrasos logísticos en las obras operativas y una sobrecarga de funciones correctivas en el personal de compras, haciendo necesaria una propuesta de optimización procedimental adaptada a los estándares organizacionales vigentes."
]

OBJETIVO_GENERAL = "Proponer mejoras procedimentales para optimizar el proceso de procura en el departamento administrativo de Lubricantes y Equipos Varyna, C.A., con la finalidad de agilizar los tiempos de adquisición y fortalecer el control interno de las operaciones de compras."

OBJETIVOS_ESPECIFICOS = [
    "Diagnosticar el proceso actual de procura en el departamento administrativo de la empresa para identificar el flujo secuencial de las solicitudes de compra.",
    "Identificar las debilidades y cuellos de botella presentes en las fases de seguimiento, cotización y aprobación de las adquisiciones.",
    "Analizar las causas organizativas que generan retrasos y tiempos prolongados en el ciclo de adquisición de insumos y materiales.",
    "Diseñar una propuesta de mejora procedimental que agilice los tiempos de respuesta y optimice el control de la procura en el área administrativa."
]

PLANIFICACION_DATOS = [
    (
        "Diagnosticar el proceso actual de procura en el departamento administrativo.",
        "Aplicación de guías de observación directa y entrevistas al personal encargado del ciclo de compras de la empresa.",
        "Guía de entrevista, libreta de notas de campo, computadora de oficina.",
        "Mapeo situacional del flujo actual de las solicitudes de compra elaborado."
    ),
    (
        "Identificar las debilidades y cuellos de botella en el seguimiento y aprobación.",
        "Revisión y análisis de los tiempos promedio de respuesta en expedientes de compras anteriores y detección de fases críticas.",
        "Hojas de registro, histórico de órdenes de compra, software de oficina.",
        "Matriz de criticidad con los puntos de retraso documental identificados."
    ),
    (
        "Analizar las causas organizativas que generan retrasos en la adquisición.",
        "Clasificación analítica de los factores determinantes de las demoras mediante mesas de trabajo técnica con la administración.",
        "Diagramas causa-efecto, material de papelería, marco de control de procesos.",
        "Informe analítico con la jerarquización de las causas raíz de las demoras."
    ),
    (
        "Diseñar una propuesta de mejora procedimental para el control de la procura.",
        "Redacción del nuevo flujo de trabajo optimizado, asignación formal de roles y diseño de plantillas estandarizadas para cotizaciones.",
        "Procesador de texto, guías metodológicas de administración, normativas de la empresa.",
        "Propuesta metodológica de optimización de procura formulada y validada."
    ),
]

CRONOGRAMA_DATOS = [
    ("Inducción y reconocimiento del departamento administrativo y del área de compras.",       [True,  False, False, False, False]),
    ("Levantamiento preliminar de información sobre el flujo operativo de procura.",           [True,  True,  False, False, False]),
    ("Aplicación de entrevistas y detección de cuellos de botella en las aprobaciones.",        [False, True,  True,  False, False]),
    ("Análisis cuantitativo y cualitativo de las causas que provocan los retrasos.",            [False, False, True,  True,  False]),
    ("Diseño de las estrategias procedimentales de mejora y nuevos formatos de control.",       [False, False, False, True,  True ]),
    ("Revisión final de la propuesta de optimización y presentación formal a la gerencia.",    [False, False, False, False, True ]),
]

# ================================================================
#  CAPÍTULO III - Marco Teórico
# ================================================================
BASES_TEORICAS = [
    {
        "titulo": "Aquí va el título de la primera base teórica",
        "parrafos": [
            "Aquí va el desarrollo teórico del primer tema. [Completar con la definición y autores que sustentan este concepto.]",
            "Aquí va un segundo párrafo de desarrollo. [Completar con la aplicación del concepto al proyecto.]"
        ],
        "cita_larga": None
    },
    {
        "titulo": "Aquí va el título de la segunda base teórica",
        "parrafos": [
            "Aquí va el desarrollo teórico del segundo tema. [Completar con la definición y autores que sustentan este concepto.]"
        ],
        "cita_larga": None
    },
]

POST_CITA_TEXTO = "Aquí va el comentario posterior a la cita (opcional, solo si se usa cita larga)."

# ================================================================
#  CAPÍTULO IV - Actividades Realizadas
# ================================================================
ACTIVIDADES_DESCRIPCION = "Durante las seis (6) semanas de práctica profesional, se ejecutaron fases sucesivas de diagnóstico, análisis y diseño de la propuesta de optimización:"

ACTIVIDADES_LISTA = [
    {
        "semana": 1,
        "operativa": "Aquí va la actividad operativa de la semana 1. [Completar con la tarea realizada en la empresa.]",
        "investigacion": "Aquí va la actividad de investigación de la semana 1. [Completar con la tarea académica realizada.]"
    },
    {
        "semana": 2,
        "operativa": "Aquí va la actividad operativa de la semana 2. [Completar con la tarea realizada en la empresa.]",
        "investigacion": "Aquí va la actividad de investigación de la semana 2. [Completar con la tarea académica realizada.]"
    },
    {
        "semana": 3,
        "operativa": "Aquí va la actividad operativa de la semana 3. [Completar con la tarea realizada en la empresa.]",
        "investigacion": "Aquí va la actividad de investigación de la semana 3. [Completar con la tarea académica realizada.]"
    },
    {
        "semana": 4,
        "operativa": "Aquí va la actividad operativa de la semana 4. [Completar con la tarea realizada en la empresa.]",
        "investigacion": "Aquí va la actividad de investigación de la semana 4. [Completar con la tarea académica realizada.]"
    },
    {
        "semana": 5,
        "operativa": "Aquí va la actividad operativa de la semana 5. [Completar con la tarea realizada en la empresa.]",
        "investigacion": "Aquí va la actividad de investigación de la semana 5. [Completar con la tarea académica realizada.]"
    },
    {
        "semana": 6,
        "operativa": "Aquí va la actividad operativa de la semana 6. [Completar con la tarea realizada en la empresa.]",
        "investigacion": "Aquí va la actividad de investigación de la semana 6. [Completar con la tarea académica realizada.]"
    }
]

# ================================================================
#  CAPÍTULO V - Conclusiones y Recomendaciones
# ================================================================
CONCLUSIONES = [
    "Aquí va la conclusión correspondiente al primer objetivo específico. [Completar con el logro alcanzado.]",
    "Aquí va la conclusión correspondiente al segundo objetivo específico. [Completar con el logro alcanzado.]",
    "Aquí va la conclusión correspondiente al tercer objetivo específico. [Completar con el logro alcanzado.]",
    "Aquí va la conclusión correspondiente al cuarto objetivo específico. [Completar con el logro alcanzado.]"
]

RECOMENDACIONES = [
    "Aquí va la primera recomendación. [Completar con la acción sugerida.]",
    "Aquí va la segunda recomendación. [Completar con la acción sugerida.]",
    "Aquí va la tercera recomendación. [Completar con la acción sugerida.]",
    "Aquí va la cuarta recomendación. [Completar con la acción sugerida.]"
]

# ================================================================
#  Referencias Bibliográficas
# ================================================================
REFERENCIAS_LISTA = [
    "Aquí va la primera referencia bibliográfica en formato APA. [Completar con autor, año, título, editorial y ciudad.]",
    "Aquí va la segunda referencia bibliográfica en formato APA. [Completar con autor, año, título, editorial y ciudad.]",
    "Aquí va la tercera referencia bibliográfica en formato APA. [Completar con autor, año, título, editorial y ciudad.]"
]

# ================================================================
#  Anexos
# ================================================================
ANEXOS_LISTA = [
    ("ANEXO A", "Aquí va la descripción del Anexo A"),
    ("ANEXO B", "Aquí va la descripción del Anexo B"),
    ("ANEXO C", "Aquí va la descripción del Anexo C")
]
