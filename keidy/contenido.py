# contenido.py

# ================================================================
#  CONFIGURACIÓN DE RUTAS
# ================================================================
CARPETA_IMAGENES = "imagenes"

# Gráficos del informe: cada uno indica tras qué sección va (anclas: "ubicacion" | "estructura")
GRAFICOS = [
    {"numero": 1, "tras": "ubicacion", "titulo": "Gráfico 1. Representación cartográfica y ubicación espacial de la empresa.", "ancho_cm": 5, "lista": "Representación cartográfica y ubicación espacial de la empresa", "pagina": "3"},
    {"numero": 2, "tras": "estructura", "titulo": "Gráfico 2. Organigrama estructural y niveles jerárquicos de la organización.", "ancho_cm": 12},
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
AUTOR_DATOS = "Autor: Keidy Guzmán\nC.I.: 28.706.352"
FECHA_LUGAR = "El Tigre, julio de 2026"

# ================================================================
#  DATOS DE LA EMPRESA (CAPÍTULO I)
# ================================================================
RAZON_SOCIAL = "Lubricantes y Equipos Varyna, C.A."
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

POBLACION = "La población de trabajadores de Lubricantes y Equipos Varyná C.A. está conformada por personal administrativo, técnico y operativo. Toda la empresa trabaja de manera coordinada para garantizar la calidad de los servicios prestados, recayendo sobre el área de procura administrativa la responsabilidad de asegurar la disponibilidad oportuna de materiales y repuestos para la continuidad operativa."

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
