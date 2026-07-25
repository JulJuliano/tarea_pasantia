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
PLANIFICACION_INTRO_TEXTO = "La planificación establece la relación entre cada objetivo específico y las actividades técnicas a ejecutar para el desarrollo de la propuesta de simplificación administrativa:"
CRONOGRAMA_INTRO_TEXTO = "El cronograma estructura temporalmente las fases de diagnóstico, análisis y diseño de la propuesta, distribuidas a lo largo de las diez (10) semanas de duración de la pasantía:"

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
    "\"ELÍAS CALIXTO POMPA\"",
    "EL TIGRE, ESTADO ANZOÁTEGUI"
]

TITULO_PROYECTO = "PROPUESTA DE SIMPLIFICACIÓN ADMINISTRATIVA DE LA PROCURA EN LUBRICANTES Y EQUIPOS VARYNA, C.A."
AUTOR_DATOS = [
    "Autor:",
    "Keidy Guzmán",
    "C.I.: 28.706.352",
    "",
    "Tutor Industrial:",
    "Martina Rondón",
    "C.I.: 12.208.768",
    "",
    "Tutor Académico:",
    "Dra. Carmen J. Álvarez",
    "C.I.: 14.452.956"
]
FECHA_LUGAR = "El Tigre, julio de 2026"

# ================================================================
#  PÁGINAS PRELIMINARES
# ================================================================
DEDICATORIA = ""

AGRADECIMIENTOS = ""

RESUMEN_TEXTO = (
    "El presente informe describe la propuesta de simplificación administrativa del proceso "
    "de procura en el departamento administrativo de Lubricantes y Equipos Varyna, C.A. La investigación se "
    "enmarca en la modalidad de proyecto factible apoyado en un diagnóstico de campo. Durante el estudio se "
    "identificó la ausencia de canales formalizados de recepción de requisiciones, tiempos de respuesta "
    "prolongados en las fases de cotización y aprobación, y la inexistencia de formatos estandarizados de "
    "control. La propuesta contempla un nuevo flujo de trabajo procedimental simplificado, plantillas "
    "estandarizadas de solicitud y orden de compra, y una matriz de autorización por monto, orientadas a "
    "fortalecer el control interno y agilizar el ciclo de adquisición de insumos y materiales."
)

PALABRAS_CLAVE = "procura, simplificación administrativa, proceso administrativo, proyecto factible, pasantías."

INTRODUCCION_TEXTO = (
    "La presente pasantía, desarrollada como requisito para optar al título de Técnico Superior Universitario "
    "en Administración, tiene como propósito proponer la simplificación administrativa del proceso de "
    "procura en el departamento administrativo de Lubricantes y Equipos Varyna, C.A. La investigación parte "
    "del diagnóstico de las deficiencias actuales en el ciclo de adquisición de insumos y materiales, "
    "identificando los factores que generan retrasos operativos y complejidades innecesarias en el control "
    "interno del departamento. El informe se estructura en cinco capítulos: el Capítulo I presenta la realidad "
    "organizacional de la empresa; el Capítulo II desarrolla el diagnóstico situacional y la planificación "
    "del proyecto; el Capítulo III sustenta las bases teóricas que orientan la propuesta; el Capítulo IV "
    "describe las actividades ejecutadas durante las diez semanas de pasantía; y el Capítulo V presenta las "
    "conclusiones y recomendaciones derivadas del proceso investigativo."
)

# ================================================================
#  DATOS DE LA EMPRESA (CAPÍTULO I)
# ================================================================
RAZON_SOCIAL = "Lubricantes y Equipos Varyna, C.A."


RESENA_HISTORICA = [
    "Lubricantes y Equipos Varyná, C.A. es una empresa venezolana fundada con la visión de responder a las crecientes demandas operativas e industriales del país. A lo largo de más de treinta y seis (36) años de trayectoria ininterrumpida, la organización se ha consolidado en el sector petrolero, industrial y de construcción, posicionándose como un aliado estratégico de alta confiabilidad en el mercado nacional gracias a su capacidad de respuesta y solvencia técnica.",
    "Desde sus primeros años de operaciones, la empresa enfocó su estrategia en la diversificación técnica de sus servicios, pasando de ser un proveedor local de insumos a una estructura corporativa especializada en el procesamiento y suministro de productos químicos de alto rendimiento, tratamiento químico de crudo y provisión de maquinaria pesada para proyectos de gran escala. Este desarrollo progresivo le permitió establecer estándares operacionales alineados con las exigencias de la industria energética regional y nacional.",
    "Su integración como parte fundamental del Grupo Corporativo VTC marcó un hito en su madurez organizacional, impulsando un crecimiento sostenido mediante la profesionalización de sus procesos, la adopción de tecnologías de vanguardia y la consolidación de alianzas comerciales de largo alcance. Hoy en día, Lubricantes y Equipos Varyná, C.A. mantiene su compromiso con el desarrollo productivo del país, sustentando su liderazgo en la innovación continua, la calidad de servicio y el fortalecimiento constante de su capital humano y capacidad logística."
]

MISION = "Brindar a nuestros clientes objetivos, soluciones de calidad en las áreas en las cuales nos desempeñamos, para contribuir de manera significativa en sus resultados. Aportando valor con nuestras respuestas a sus requerimientos. En la búsqueda de un mejor país y de una mejor humanidad."
VISION = "Ser el conglomerado de empresas líderes en cada una de las categorías en las que participamos, generando modelos de negocios altamente competitivos, atendiendo a nuestros distintos beneficiarios con productos y servicios de calidad."

VALORES = [
    ("Planificación", "Estructuración anticipada de las adquisiciones para optimizar los recursos financieros de la organización."),
    ("Responsabilidad", "Cumplimiento eficiente de los compromisos adquiridos con clientes, proveedores y trabajadores."),
    ("Integridad", "Actuar con honestidad, ética y transparencia en todas las operaciones de la empresa."),
    ("Transparencia", "Garantizar la trazabilidad y la claridad en los procesos de selección y adjudicación de compras.")
]

OBJETIVO_GENERAL_EMPRESA = "Posicionarse como una empresa líder en el sector petrolero, industrial y de construcción a nivel nacional, garantizando la provisión oportuna de productos químicos especializados, tratamiento de crudo y maquinaria pesada, mediante una gestión administrativa, operacional y de procura transparente, eficiente y orientada a la calidad total."

OBJETIVOS_ESPECIFICOS_EMPRESA = [
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
    "En el departamento administrativo de Lubricantes y Equipos Varyna, C.A., se ha identificado una situación desfavorable relacionada con la complejidad y dispersión del flujo procedimental de la procura. En la actualidad, las solicitudes de compras de materiales e insumos críticos presentan marcados retrasos debido a la ausencia de un canal formalizado de recepción, lo que ocasiona que las requisiciones no sigan una ruta clara ni simplificada de procesamiento.",
    "Esta falta de estandarización y simplificación administrativa genera cuellos de botella en las instancias de aprobación, pérdida de trazabilidad en el seguimiento de las cotizaciones y tiempos prolongados para la adquisición definitiva de los insumos. Como consecuencia directa, se producen retrasos logísticos en las obras operativas y una sobrecarga de funciones correctivas en el personal de compras, haciendo necesaria una propuesta de simplificación procedimental adaptada a los estándares organizacionales vigentes."
]

OBJETIVO_GENERAL = "Proponer la simplificación administrativa del proceso de procura en el departamento administrativo de Lubricantes y Equipos Varyna, C.A., con la finalidad de reducir la complejidad procedimental, agilizar los tiempos de adquisición y fortalecer el control interno de las operaciones de compras."

OBJETIVOS_ESPECIFICOS = [
    "Diagnosticar el proceso actual de procura en el departamento administrativo de la empresa para identificar los pasos y procedimientos susceptibles de simplificación.",
    "Identificar las complejidades, redundancias y cuellos de botella presentes en las fases de seguimiento, cotización y aprobación de las adquisiciones.",
    "Analizar las causas organizativas que generan retrasos y procedimientos innecesariamente complejos en el ciclo de adquisición de insumos y materiales.",
    "Diseñar una propuesta de simplificación administrativa que reduzca los pasos procedimentales, agilice los tiempos de respuesta y optimice el control de la procura en el área administrativa."
]

PLANIFICACION_DATOS = [
    (
        "Diagnosticar el proceso actual de procura e identificar los pasos susceptibles de simplificación.",
        "Aplicación de guías de observación directa y entrevistas al personal encargado del ciclo de compras de la empresa.",
        "Guía de entrevista, libreta de notas de campo, computadora de oficina.",
        "Mapeo situacional del flujo actual de las solicitudes de compra elaborado."
    ),
    (
        "Identificar complejidades, redundancias y cuellos de botella en el seguimiento y aprobación.",
        "Revisión y análisis de los tiempos promedio de respuesta en expedientes de compras anteriores y detección de fases críticas y pasos duplicados.",
        "Hojas de registro, histórico de órdenes de compra, software de oficina.",
        "Matriz de criticidad con los puntos de complejidad y retraso documental identificados."
    ),
    (
        "Analizar las causas organizativas que generan procedimientos innecesariamente complejos.",
        "Clasificación analítica de los factores determinantes de las demoras y redundancias mediante mesas de trabajo técnica con la administración.",
        "Diagramas causa-efecto, material de papelería, marco de control de procesos.",
        "Informe analítico con la jerarquización de las causas raíz de la complejidad procedimental."
    ),
    (
        "Diseñar una propuesta de simplificación administrativa para el control de la procura.",
        "Redacción del nuevo flujo de trabajo simplificado, asignación formal de roles y diseño de plantillas estandarizadas para cotizaciones.",
        "Procesador de texto, guías metodológicas de administración, normativas de la empresa.",
        "Propuesta de simplificación administrativa de la procura formulada y validada."
    ),
]

CRONOGRAMA_DATOS = [
    # ACTIVIDADES DEL PROYECTO (6)
    ("Reconocimiento del departamento y levantamiento del flujo actual de procura.",        [True,  True,  False, False, False, False, False, False, False, False]),
    ("Aplicación de entrevistas y detección de cuellos de botella en las aprobaciones.",   [False, False, True,  True,  False, False, False, False, False, False]),
    ("Análisis cuantitativo y cualitativo de causas de retraso en el ciclo de compras.",   [False, False, False, True,  True,  False, False, False, False, False]),
    ("Diseño del nuevo flujo optimizado, roles y plantillas de control.",                  [False, False, False, False, False, True,  True,  False, False, False]),
    ("Redacción y validación de la propuesta de mejora procedimental.",                    [False, False, False, False, False, False, True,  True,  False, False]),
    ("Presentación formal de la propuesta a la gerencia y ajustes finales.",               [False, False, False, False, False, False, False, False, True,  True ]),
    # ACTIVIDADES DE OFICINA (4)
    ("Inducción institucional y familiarización con el sistema de compras vigente.",       [True,  False, False, False, False, False, False, False, False, False]),
    ("Apoyo en la recepción y tramitación de solicitudes de compra del departamento.",     [False, False, True,  False, True,  False, False, False, False, False]),
    ("Seguimiento a cotizaciones y actualización de expedientes de proveedores.",          [False, False, False, False, False, True,  False, True,  False, False]),
    ("Apoyo en el cierre administrativo del período y archivo de órdenes de compra.",      [False, False, False, False, False, False, False, False, True,  True ]),
]

# ================================================================
#  CAPÍTULO III - Marco Teórico
# ================================================================
BASES_TEORICAS = [
    {
        "titulo": "Procura y Gestión de Compras",
        "parrafos": [
            "La procura se define como el conjunto de actividades orientadas a la adquisición de bienes, materiales e insumos necesarios para el funcionamiento continuo de una organización. Monterroso (2002) establece que la gestión de abastecimiento eficiente no se limita a la ejecución de compras, sino que abarca la planificación de necesidades, la selección de proveedores, la negociación de condiciones y el control del cumplimiento de los requerimientos en tiempo, calidad y costo.",
            "En el contexto del departamento administrativo de Lubricantes y Equipos Varyna, C.A., la procura cumple un rol estratégico al garantizar la disponibilidad oportuna de insumos para las operaciones industriales y de campo. La ausencia de procedimientos formalizados en este ciclo genera interrupciones en la cadena de suministro interna, evidenciando la necesidad de una propuesta de optimización procedimental que estandarice cada fase del proceso de adquisición."
        ],
        "cita_larga": {
            "texto": "La gestión de compras y abastecimiento comprende un conjunto de actividades que permiten identificar las necesidades de materiales e insumos de la organización, seleccionar adecuadamente a los proveedores, negociar las condiciones de adquisición más convenientes y asegurar que los bienes requeridos lleguen en las cantidades correctas, en el momento oportuno y al menor costo posible, contribuyendo directamente a la eficiencia operativa de la empresa.",
            "autor": "(Monterroso, 2002, p. 3)"
        }
    },
    {
        "titulo": "Proceso Administrativo",
        "parrafos": [
            "El proceso administrativo constituye el marco conceptual fundamental que rige el funcionamiento de las organizaciones modernas. Chiavenato (2006) lo describe como el conjunto secuencial e interrelacionado de funciones de planificación, organización, dirección y control, orientadas al logro eficiente de los objetivos organizacionales mediante el uso racional de los recursos disponibles.",
            "Aplicado al contexto de la procura, el proceso administrativo provee la estructura metodológica necesaria para formalizar cada etapa del ciclo de compras. La planificación define las necesidades y tiempos de adquisición; la organización asigna responsabilidades claras a cada actor del proceso; la dirección asegura la ejecución coordinada de las actividades; y el control verifica el cumplimiento de los procedimientos y detecta desviaciones que requieren corrección."
        ],
        "cita_larga": None
    },
    {
        "titulo": "Control Interno en los Procesos de Compras",
        "parrafos": [
            "El control interno se define como el proceso diseñado e implementado por la dirección de una organización para proporcionar una seguridad razonable sobre la consecución de los objetivos en las categorías de eficiencia operativa, confiabilidad de la información financiera y cumplimiento de las normas aplicables. Mantilla (2005) señala que un sistema de control interno robusto en el área de compras minimiza los riesgos de fraude, duplicidad de pagos y adquisiciones no autorizadas.",
            "En el proceso de procura de Lubricantes y Equipos Varyna, C.A., el fortalecimiento del control interno implica la definición de niveles de autorización por monto de compra, la implementación de formularios estandarizados de solicitud y la trazabilidad documental de cada expediente desde la requisición hasta la orden de compra cerrada. Estas medidas reducen la discrecionalidad en las decisiones de adquisición y aumentan la transparencia del proceso."
        ],
        "cita_larga": None
    },
    {
        "titulo": "Simplificación Administrativa de Procesos",
        "parrafos": [
            "La simplificación administrativa consiste en la revisión sistemática y el rediseño de los procedimientos organizacionales con el propósito de eliminar pasos innecesarios, reducir la burocracia interna y facilitar la ejecución ágil de las operaciones. Según Harrington (1993), un proceso simplificado debe ser comprensible para todos los actores involucrados, ejecutable con el menor número de pasos posible y orientado a resultados medibles y verificables.",
            "En el ámbito de la administración de compras, la simplificación procedimental se traduce en la reducción de los ciclos de aprobación, la unificación de los formatos de cotización y la clarificación de los roles y responsabilidades de cada actor. El resultado esperado es una disminución verificable de los tiempos de respuesta en la adquisición de insumos y una mayor capacidad de la organización para atender sus necesidades de abastecimiento de forma oportuna y transparente."
        ],
        "cita_larga": None
    },
    {
        "titulo": "Proyecto Factible como Modalidad de Investigación",
        "parrafos": [
            "La Universidad Pedagógica Experimental Libertador (UPEL, 2016) define el proyecto factible como la investigación, elaboración y desarrollo de una propuesta de un modelo operativo viable para solucionar problemas, requerimientos o necesidades de organizaciones o grupos sociales. Esta modalidad exige la comprobación de la viabilidad técnica y operativa de la solución planteada, sustentada en un diagnóstico de campo que evidencie la situación deficitaria que da origen a la propuesta.",
            "Arias (2012) complementa esta definición señalando que el proyecto factible avanza hasta proponer y, en muchos casos, desarrollar la solución, demostrando su aplicabilidad en el contexto real. El presente trabajo se enmarca en esta modalidad al partir del diagnóstico del proceso de procura en Lubricantes y Equipos Varyna, C.A., para proponer un conjunto de mejoras procedimentales cuya implementación es técnica y operativamente viable para la organización."
        ],
        "cita_larga": None
    }
]

POST_CITA_TEXTO = ""

# ================================================================
#  CAPÍTULO IV - Actividades Realizadas
# ================================================================
ACTIVIDADES_DESCRIPCION = "Durante las diez (10) semanas de práctica profesional, se ejecutaron fases sucesivas de diagnóstico, análisis y diseño de la propuesta de simplificación administrativa:"

ACTIVIDADES_LISTA = [
    {
        "semana": 1,
        "operativa": "Inducción institucional, recorrido por las instalaciones, presentación ante el equipo del departamento administrativo y familiarización con los procedimientos generales de la empresa y el área de procura.",
        "investigacion": "Observación directa del flujo procedimental de las solicitudes de compra, identificación preliminar de las etapas del ciclo de procura y formulación inicial de la situación problemática en términos de complejidad administrativa."
    },
    {
        "semana": 2,
        "operativa": "Apoyo en la recepción, clasificación y registro de solicitudes de compra pendientes, y familiarización con el sistema de seguimiento de cotizaciones vigente en el departamento.",
        "investigacion": "Levantamiento detallado del flujo secuencial de las adquisiciones mediante entrevistas informales al personal encargado y elaboración del mapeo situacional del proceso actual."
    },
    {
        "semana": 3,
        "operativa": "Colaboración en la tramitación de requisiciones de materiales e insumos, apoyo en la comunicación con proveedores y actualización del registro de cotizaciones en proceso.",
        "investigacion": "Aplicación de guía de entrevista estructurada al personal de compras y administración para identificar los cuellos de botella en las fases de seguimiento y aprobación."
    },
    {
        "semana": 4,
        "operativa": "Apoyo en el seguimiento de órdenes de compra abiertas, verificación del estatus de cotizaciones pendientes de respuesta y actualización del registro de proveedores activos.",
        "investigacion": "Revisión y análisis de expedientes históricos de compras para determinar los tiempos promedio de respuesta en cada fase del ciclo de adquisición e identificación de las etapas críticas."
    },
    {
        "semana": 5,
        "operativa": "Tramitación de solicitudes de compra recibidas durante la semana, apoyo en la elaboración de cuadros comparativos de cotizaciones y actualización de la base de proveedores.",
        "investigacion": "Análisis cualitativo y cuantitativo de las causas organizativas que generan retrasos mediante diagramas causa-efecto y clasificación jerárquica de los factores determinantes."
    },
    {
        "semana": 6,
        "operativa": "Colaboración en el seguimiento a cotizaciones pendientes de aprobación gerencial y apoyo en la actualización de expedientes de compras activos del período.",
        "investigacion": "Diseño del nuevo flujo de trabajo simplificado para el proceso de procura, con reducción de pasos, definición de puntos de control, responsables de cada etapa y tiempos máximos de respuesta por fase."
    },
    {
        "semana": 7,
        "operativa": "Apoyo en la recepción y procesamiento de requisiciones urgentes del período, y colaboración en la verificación de disponibilidad presupuestaria para compras en trámite.",
        "investigacion": "Diseño de las plantillas estandarizadas de solicitud de cotización, orden de compra y seguimiento de estatus, adaptadas a los requerimientos operativos del departamento."
    },
    {
        "semana": 8,
        "operativa": "Seguimiento a las órdenes de compra en proceso y apoyo en la actualización de los registros de proveedores y expedientes de adquisiciones del período administrativo.",
        "investigacion": "Redacción del documento de propuesta de simplificación administrativa, integrando el nuevo flujo simplificado, los formatos diseñados y las recomendaciones de mejora de control interno."
    },
    {
        "semana": 9,
        "operativa": "Apoyo en el cierre administrativo del ciclo de compras del período y colaboración en el archivo ordenado de las órdenes de compra gestionadas durante la pasantía.",
        "investigacion": "Validación de la propuesta de simplificación con el tutor industrial, incorporación de observaciones y ajustes al documento final para su presentación formal."
    },
    {
        "semana": 10,
        "operativa": "Presentación formal de la propuesta de mejora ante la gerencia del departamento administrativo y firma de la carta de aprobación del tutor industrial.",
        "investigacion": "Consolidación y revisión final del informe académico de pasantías, incorporación de los anexos definitivos y preparación del documento para la entrega institucional."
    }
]

# ================================================================
#  CAPÍTULO V - Conclusiones y Recomendaciones
# ================================================================
CONCLUSIONES = [
    "Se diagnosticó que el proceso actual de procura carece de una ruta simplificada de procesamiento de solicitudes, lo que genera que las requisiciones no sigan un canal claro desde su origen hasta la orden de compra, prolongando los tiempos de respuesta y dificultando el seguimiento de cada adquisición.",
    "Se identificaron como principales complejidades y cuellos de botella la ausencia de formatos estandarizados de solicitud, la falta de niveles de autorización definidos por monto y la inexistencia de un mecanismo ágil de seguimiento del estatus de cotizaciones, concentrando la carga operativa en pocos actores del proceso.",
    "Se determinó que las causas organizativas de los retrasos en el ciclo de adquisición responden a la ausencia de procedimientos escritos simplificados, la dispersión de responsabilidades y la inexistencia de indicadores que permitan medir el desempeño del proceso de compras.",
    "Se diseñó una propuesta de simplificación administrativa que contempla un nuevo flujo de trabajo con menor número de pasos y puntos de control definidos, plantillas estandarizadas de cotización y orden de compra, y una matriz de autorización por monto, herramientas que en conjunto fortalecen el control interno y agilizan el ciclo de adquisición."
]

RECOMENDACIONES = [
    "Implementar el nuevo flujo simplificado de forma gradual, comenzando por la formalización del canal de recepción de requisiciones y la adopción de las plantillas estandarizadas de solicitud de cotización y orden de compra.",
    "Socializar el manual de procedimientos simplificados de procura con todo el personal involucrado en el ciclo de compras, garantizando que cada actor conozca sus responsabilidades y los tiempos máximos de respuesta establecidos para cada fase.",
    "Establecer indicadores de gestión para el proceso de procura, tales como el tiempo promedio de ciclo de compra y el porcentaje de requisiciones tramitadas dentro del plazo, con seguimiento mensual por parte de la gerencia administrativa.",
    "Revisar y actualizar el procedimiento simplificado al menos una vez al año, incorporando las lecciones aprendidas durante su ejecución y los cambios en las condiciones operativas o normativas de la organización."
]

# ================================================================
#  Referencias Bibliográficas
# ================================================================
REFERENCIAS_LISTA = [
    "Arias, F. (2012). El proyecto de investigación: Introducción a la metodología científica (6ta ed.). Episteme, Venezuela.",
    "Chiavenato, I. (2006). Introducción a la teoría general de la administración (7ma ed.). McGraw-Hill, México.",
    "Harrington, H. J. (1993). Mejoramiento de los procesos de la empresa. McGraw-Hill, Colombia.",
    "Mantilla, S. (2005). Control interno: Informe COSO (4ta ed.). Ecoe Ediciones, Colombia.",
    "Monterroso, E. (2002). El proceso de abastecimiento: El aprovisionamiento. Universidad Nacional de Luján, Argentina.",
    "Universidad Pedagógica Experimental Libertador. (2016). Manual de trabajos de grado de especialización y maestría y tesis doctorales (5ta ed.). FEDUPEL, Venezuela."
]

# ================================================================
#  Anexos
# ================================================================
ANEXOS_LISTA = []
