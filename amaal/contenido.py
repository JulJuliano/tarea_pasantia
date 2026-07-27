# contenido.py
# ================================================================
#  MÓDULO DE CONTENIDO ACADÉMICO PARA EL INFORME DE PASANTÍAS
#  Proyecto de Amaal Alrifaaie - TSU en Administración
# ================================================================

# 1. Rutas y Carpetas
CARPETA_IMAGENES = "imagenes"

# Gráficos del informe: cada uno indica tras qué sección va (anclas: "ubicacion" | "estructura")
GRAFICOS = [
    {"numero": 1, "tras": "ubicacion", "titulo": "Gráfico 1. Representación cartográfica y ubicación espacial de Ingeniería de Telecomunicaciones, C.A.", "ancho_cm": 5, "lista": "Representación cartográfica y ubicación espacial de Ingeniería de Telecomunicaciones, C.A.", "pagina": "3"},
    {"numero": 2, "tras": "estructura", "titulo": "Gráfico 2. Organigrama estructural y niveles jerárquicos de Ingeniería de Telecomunicaciones, C.A.", "ancho_cm": 12, "lista": "Organigrama estructural y niveles jerárquicos de Ingeniería de Telecomunicaciones, C.A.", "pagina": "4"},
    {"numero": 3, "tras": "estructura", "titulo": "Gráfico 3. Organigrama del Departamento de Administración.", "ancho_cm": 12, "lista": "Organigrama del Departamento de Administración.", "pagina": "5"},
]

# Textos introductorios del Capítulo II
PLANIFICACION_INTRO_TEXTO = "La planificación establece la relación entre cada objetivo específico y las actividades técnicas a ejecutar para el desarrollo de la evaluación del control administrativo:"
CRONOGRAMA_INTRO_TEXTO = "El cronograma estructura temporalmente las fases de diagnóstico, análisis y propuesta de mejora, distribuidas a lo largo de las diez (10) semanas de duración de la pasantía:"

# Título del Cuadro 2 (Cronograma)
CUADRO_CRONOGRAMA_TITULO = "Cuadro 2. Cronograma de actividades del proyecto."

# Lista de Cuadros (índice preliminar): (número, descripción, página)
CUADROS_INDICE = [
    ("1", "Planificación integral de objetivos específicos", "5"),
    ("2", "Cronograma de actividades del proyecto", "6"),
]

# 2. Datos de Portada y Datos Personales
MEMBRETE = [
    "REPÚBLICA BOLIVARIANA DE VENEZUELA",
    "MINISTERIO DEL PODER POPULAR PARA LA EDUCACIÓN",
    "INSTITUTO UNIVERSITARIO DE TECNOLOGÍA",
    "\"ELÍAS CALIXTO POMPA\"",
    "EL TIGRE, ESTADO ANZOÁTEGUI"
]

TITULO_PROYECTO = "EVALUACIÓN DEL CONTROL ADMINISTRATIVO APLICADO A LA GESTIÓN DE SOLICITUDES DE SERVICIOS DE TELECOMUNICACIONES EN LA EMPRESA INGENIERÍA DE TELECOMUNICACIONES, C.A."

AUTOR_DATOS = [
    "Autor:",
    "Alrifaai Alrifaaie Amaal",
    "C.I.: 31.985.792",
    "",
    "Tutor Industrial:",
    "Lenny Mata",
    "C.I.: 8969750",
    "",
    "Tutor Académico:",
    "Lic. Carlos Mendoza",
    "C.I.: 4.273.815"
]

FECHA_LUGAR = "El Tigre, julio de 2026"
CIUDAD_FECHA = FECHA_LUGAR
NOMBRE_PASANTE = "Alrifaai Alrifaaie Amaal"
CI_PASANTE = "31.985.792"
ESPECIALIDAD = "Administración"

RAZON_SOCIAL = "Ingeniería de Telecomunicaciones, C.A. (IDETEL / INTELCA)"

# 3. Páginas Preliminares
DEDICATORIA = ""

AGRADECIMIENTOS = ""

RESUMEN_TEXTO = (
    "El presente informe describe la evaluación del control administrativo aplicado a la gestión de solicitudes "
    "de servicios de telecomunicaciones en la empresa Ingeniería de Telecomunicaciones, C.A. (IDETEL). La "
    "investigación se enmarca en la modalidad de proyecto factible apoyado en un diagnóstico de campo. Durante "
    "el estudio se identificó la ausencia de procedimientos formalizados para el seguimiento de solicitudes de "
    "afiliación e incidencias, la falta de formatos estandarizados de registro y la inexistencia de indicadores "
    "de gestión que permitan evaluar el desempeño del proceso de atención al suscriptor. La propuesta contempla "
    "un nuevo flujo de trabajo estandarizado, formatos unificados de control y un conjunto de indicadores de "
    "gestión orientados a fortalecer el control administrativo y optimizar la calidad del servicio prestado."
)

PALABRAS_CLAVE = "control administrativo, solicitudes de servicios, telecomunicaciones, proyecto factible, pasantías."

INTRODUCCION_TEXTO = (
    "La presente pasantía, desarrollada como requisito para optar al título de Técnico Superior Universitario "
    "en Administración, tiene como propósito evaluar el control administrativo aplicado a la gestión de "
    "solicitudes de servicios de telecomunicaciones en la empresa Ingeniería de Telecomunicaciones, C.A. "
    "(IDETEL), con sede en la ciudad de El Tigre, estado Anzoátegui. El estudio parte del diagnóstico de las "
    "deficiencias presentes en el proceso de atención al suscriptor para proponer mejoras procedimentales "
    "que optimicen el control interno del departamento. El informe se organiza en cinco capítulos: el Capítulo "
    "I presenta la realidad organizacional de IDETEL; el Capítulo II desarrolla el diagnóstico situacional y "
    "la planificación del proyecto; el Capítulo III sustenta las bases teóricas que orientan la propuesta; "
    "el Capítulo IV describe las actividades ejecutadas durante las diez semanas de pasantía; y el Capítulo "
    "V presenta las conclusiones y recomendaciones derivadas del proceso investigativo."
)

# 4. CAPÍTULO I - Realidad Organizacional

RESENA_HISTORICA = [
    "Ingeniería de Telecomunicaciones, C.A. se consolidó en la ciudad de El Tigre, estado Anzoátegui, "
    "acumulando una trayectoria de más de cuatro (4) décadas en el mercado tecnológico de la región oriental "
    "de Venezuela. Un hito fundamental en su evolución histórica se remonta al año 1983, cuando la organización "
    "se convirtió en el primer Distribuidor Autorizado Motorola para sistemas de radio de dos vías en el oriente "
    "del país, alianza estratégica que se ha mantenido vigente e ininterrumpida a lo largo de las décadas.",
    "A través de los años, impulsada por las demandas operativas de la Faja Petrolífera del Orinoco y las "
    "necesidades de conectividad comercial, la empresa expandió sus líneas tecnológicas progresivamente. Pasó "
    "de suministrar sistemas de radiocomunicación analógica convencional en bandas VHF/UHF y sistemas Trunking "
    "analógicos (800 MHz), a liderar el mercado regional con tecnologías de radiocomunicación digital de gama "
    "alta como los estándares TETRA (europeo) y P25 (americano), esenciales para operaciones industriales de "
    "misión crítica.",
    "Con la maduración del sector tecnológico, IDETEL incorporó a su portafolio soluciones de ampliación de "
    "cobertura inalámbrica, enlaces de microondas en bandas licenciadas y no licenciadas, redes de telemetría "
    "y telecomunicaciones alámbricas, consolidando su modelo de negocios en torno a Proyectos IPC (Ingeniería, "
    "Procura y Construcción), respaldado por un laboratorio técnico especializado y personal altamente calificado."
]

MISION = (
    "Brindar soluciones con altos estándares de confiabilidad en servicios de radiocomunicación y datos al "
    "segmento de mercado PyME, así como la entrega de servicios de calidad en el sector petrolero, asociados "
    "a los esfuerzos en ingeniería (integración multidisciplinaria), planificación y ejecución de proyectos de "
    "telecomunicaciones y automatización."
)

VISION = (
    "Ser reconocidos por los clientes como un proveedor de servicios altamente confiable y con altos estándares "
    "técnicos y de ingeniería, con capacidad de brindar soluciones multidisciplinarias en el área de automatización "
    "y telecomunicaciones, fortaleciendo continuamente el capital humano mediante capacitación y mejora progresiva "
    "de las instalaciones, con el fin de obtener la innovación, competitividad y liderazgo necesarios para "
    "sobresalir en el mercado de nuevas tecnologías."
)

VALORES = [
    ("Confiabilidad", "Compromiso de entregar soluciones tecnológicas robustas que cumplan con los más altos estándares técnicos y de ingeniería para garantizar operaciones continuas y seguras."),
    ("Innovación y Competitividad", "Búsqueda constante de actualización y adopción de tecnologías de última generación para sobresalir y liderar el mercado de soluciones inalámbricas y ópticas."),
    ("Seguridad Laboral e Higiene Ocupacional", "Aplicación rigurosa de normas de protección e integridad física del personal en cada obra, instalación en campo o infraestructura crítica atendida."),
    ("Excelencia Técnica", "Orientación hacia la precisión en los procesos de diseño, empalme por fusión, certificación de redes y asesoría en laboratorio.")
]

OBJETIVOS_ORG = [
    "Ejecutar todo género de actividad o prestación de servicios relacionados directa o indirectamente con el ramo de las comunicaciones, computación y la electrónica en general.",
    "Prestar servicios de importación, manufacturación, asesoría, ventas, instalaciones, arrendamientos, supervisión y mantenimiento en el área de telecomunicaciones.",
    "Representar total o parcialmente cualquier producto comercial relacionado con sus operaciones mercantiles."
]

OBJETIVO_GENERAL_EMPRESA = "Ejecutar todo género de actividad o prestación de servicios relacionados directa o indirectamente con el ramo de las comunicaciones, computación y la electrónica en general."

OBJETIVOS_ESPECIFICOS_EMPRESA = [
    "Prestar servicios de importación, manufacturación, asesoría, ventas, instalaciones, arrendamientos, supervisión y mantenimiento en el área de telecomunicaciones.",
    "Representar total o parcialmente cualquier producto comercial relacionado con sus operaciones mercantiles."
]

UBICACION = (
    "La sede administrativa y operativa de Ingeniería de Telecomunicaciones, C.A. se encuentra ubicada en la "
    "Calle Bolívar, Edificio La Suiza, Piso 1, Oficina Nro. 28, ciudad de El Tigre, Municipio Simón Rodríguez, "
    "estado Anzoátegui, Venezuela."
)

POBLACION = [
    "La estructura del talento humano de Ingeniería de Telecomunicaciones, C.A. está conformada por personal "
    "multidisciplinario distribuido en las distintas áreas operativas y administrativas, con un total de ocho (8) "
    "trabajadores. La pasantía profesional se desarrolló en el Departamento de Administración, que dado el reducido "
    "tamaño del equipo tras un proceso de reestructuración de personal, opera con una estructura simplificada. "
    "Las funciones administrativas se concentran en dos (2) cargos activos: Supervisión de Administración, "
    "Contabilidad y Tributos, y Analista de Compras y Facturación, además del Analista de Atención al Cliente."
]

ORGANIGRAMA_TEXTO = (
    "La estructura organizativa de Ingeniería de Telecomunicaciones, C.A. es de tipo vertical, diseñada para "
    "garantizar una comunicación fluida entre los niveles directivos y operativos. A la cabeza se encuentra la "
    "Presidencia, seguida de la Gerencia General y Operaciones, de la cual se desprenden los departamentos de "
    "Supervisión de Administración, Contabilidad y Tributos, Supervisión Comercial, Área de Internet, Supervisión "
    "del NOC (Network Operations Center) y Mantenimiento de Radiocomunicación. Se presenta a continuación el "
    "organigrama general de la empresa y del Departamento de Administración."
)

# 5. CAPÍTULO II - Diagnóstico Situacional
SITUACION_PROBLEMATICA = [
    "En el contexto global actual, la gestión eficiente de los procesos administrativos constituye un factor "
    "determinante para la competitividad y sostenibilidad de las organizaciones del sector tecnológico. Las "
    "empresas proveedoras de servicios de telecomunicaciones enfrentan, de manera creciente, la necesidad de "
    "articular sus procedimientos internos con las exigencias de un mercado que demanda respuestas ágiles, "
    "trazabilidad en la atención al cliente y control riguroso sobre el ciclo de vida de cada solicitud de servicio.",
    "A nivel nacional, el sector de telecomunicaciones en Venezuela ha experimentado una expansión sostenida, "
    "impulsada por la demanda de conectividad tanto en el segmento PyME como en el sector industrial y petrolero. "
    "Sin embargo, esta expansión ha puesto en evidencia debilidades estructurales en los sistemas de control "
    "administrativo de diversas organizaciones del ramo, particularmente en la gestión de solicitudes de servicio, "
    "donde la ausencia de procesos estandarizados genera retrasos, duplicidad de funciones y dificultades en la "
    "trazabilidad operativa.",
    "En el caso específico de Ingeniería de Telecomunicaciones, C.A. (IDETEL), empresa con más de cuatro décadas "
    "de trayectoria en la región oriental del país, se identificó durante el período de pasantías que el "
    "Departamento de Administración presenta deficiencias en el control administrativo aplicado a la gestión de "
    "solicitudes de servicios. Concretamente, se observó que los procesos de afiliación de nuevos suscriptores "
    "e incidencias reportadas no cuentan con un sistema de seguimiento unificado que permita verificar en tiempo "
    "real el estado de cada solicitud, lo que genera inconsistencias entre los departamentos involucrados.",
    "Las principales manifestaciones de la problemática identificada son las siguientes: (a) ausencia de registros "
    "estandarizados para el control de solicitudes de instalación y atención de incidencias, (b) comunicación "
    "fragmentada entre el área comercial, el NOC y las cuadrillas técnicas de campo, (c) retrasos en la "
    "actualización del sistema de tickets que dificultan el cierre oportuno de los casos, y (d) carencia de "
    "indicadores de gestión que permitan evaluar el desempeño del proceso de atención al suscriptor.",
    "Las causas de esta situación se atribuyen principalmente a la falta de un protocolo administrativo formal "
    "que regule el flujo de las solicitudes desde su recepción hasta su cierre definitivo, así como a la "
    "dependencia de canales informales de comunicación entre las áreas involucradas. Como consecuencia, se generan "
    "reprocesos, insatisfacción en los clientes y sobrecarga operativa en los supervisores, comprometiendo la "
    "calidad del servicio prestado y la imagen institucional de la organización."
]

OBJETIVO_GENERAL = (
    "Evaluar el control administrativo aplicado a la gestión de solicitudes de servicios de telecomunicaciones "
    "en la empresa Ingeniería de Telecomunicaciones, C.A., con el propósito de identificar las debilidades del "
    "proceso y proponer mejoras que optimicen la atención al suscriptor desde el Departamento de Administración."
)

OBJETIVOS_ESPECIFICOS = [
    "Describir los procesos administrativos actuales aplicados a la gestión de solicitudes de afiliación de nuevos suscriptores e incidencias en Ingeniería de Telecomunicaciones, C.A.",
    "Identificar las deficiencias presentes en el sistema de control administrativo utilizado para el seguimiento de solicitudes de servicios de telecomunicaciones.",
    "Analizar el impacto de las debilidades detectadas en el control administrativo sobre la calidad del servicio prestado a los suscriptores de la empresa.",
    "Proponer mejoras al proceso de control administrativo de solicitudes de servicios que contribuyan a la optimización operativa y a la satisfacción del cliente en Ingeniería de Telecomunicaciones, C.A."
]

PLANIFICACION_DATOS = [
    (
        "Describir los procesos administrativos actuales de solicitudes de servicio.",
        "Procesos administrativos de gestión de solicitudes de servicio.",
        "Observación directa y revisión documental del flujo de solicitudes.",
        "Observación directa y análisis documental.",
        "Guía de observación, documentos internos y computadora."
    ),
    (
        "Identificar las deficiencias en el control administrativo de solicitudes.",
        "Deficiencias del control administrativo de solicitudes.",
        "Entrevistas al personal administrativo y revisión de registros históricos.",
        "Entrevista no estructurada y análisis documental.",
        "Guía de entrevista, registros históricos de tickets y computadora."
    ),
    (
        "Analizar el impacto de las debilidades en la calidad del servicio.",
        "Impacto del control administrativo en la calidad del servicio.",
        "Análisis de tiempos de respuesta y correlación con quejas de suscriptores.",
        "Análisis estadístico y revisión de registros.",
        "Base de datos de incidencias y hojas de cálculo."
    ),
    (
        "Proponer mejoras al proceso de control administrativo.",
        "Mejoras al proceso de control administrativo de solicitudes.",
        "Diseño de procedimientos estandarizados y formatos de control.",
        "Diseño procedimental y estandarización de formatos.",
        "Procesador de texto y normativas internas."
    ),
]

CRONOGRAMA_DATOS = [
    ("Inducción y reconocimiento del área de trabajo.", [True, False, False, False, False, False, False, False, False, False]),
    ("Levantamiento de información sobre procesos administrativos.", [True, True, False, False, False, False, False, False, False, False]),
    ("Observación y análisis del proceso de solicitudes de servicio.", [False, True, True, False, False, False, False, False, False, False]),
    ("Diseño y aplicación de instrumentos de recolección de datos.", [False, False, True, True, False, False, False, False, False, False]),
    ("Diagnóstico de la situación problemática.", [False, False, False, True, True, False, False, False, False, False]),
    ("Revisión y elaboración del Marco Teórico.", [False, False, False, False, True, True, False, False, False, False]),
    ("Ejecución de actividades asignadas en el área administrativa.", [False, False, False, False, False, True, True, True, False, False]),
    ("Registro semanal de actividades realizadas.", [False, False, False, False, False, False, True, True, True, False]),
    ("Redacción de conclusiones y recomendaciones.", [False, False, False, False, False, False, False, False, True, True]),
    ("Revisión final y presentación del informe.", [False, False, False, False, False, False, False, False, False, True]),
]

# 6. CAPÍTULO III - Marco Teórico
BASES_TEORICAS = [
    {
        "titulo": "Control Administrativo",
        "parrafos": [
            "El control administrativo constituye una de las funciones fundamentales del proceso administrativo y se define como el mecanismo mediante el cual la organización verifica que las actividades ejecutadas se correspondan con lo planificado, detectando desviaciones y aplicando las medidas correctivas necesarias. Robbins y Coulter (2010) señalan que el control eficaz no solo identifica fallas, sino que proporciona información oportuna para la toma de decisiones gerenciales, convirtiéndose en un instrumento de mejora continua y no únicamente de fiscalización.",
            "En el contexto del Departamento de Administración de Ingeniería de Telecomunicaciones, C.A., el control administrativo se aplica sobre el ciclo de gestión de solicitudes de servicio, abarcando desde la recepción de la solicitud del suscriptor hasta el cierre definitivo del caso. La ausencia de mecanismos formales de control en este ciclo genera inconsistencias entre los departamentos involucrados y dificulta la evaluación del desempeño del proceso de atención."
        ],
        "cita_larga": {
            "texto": "El control es el proceso de monitorear las actividades para asegurarse de que se lleven a cabo según lo planeado y para corregir cualquier desviación significativa. Los gerentes no pueden saber realmente si sus unidades están desempeñándose adecuadamente hasta que evalúan qué actividades se han llevado a cabo y comparan el desempeño real con el estándar deseado.",
            "autor": "(Robbins y Coulter, 2010, p. 398)"
        }
    },
    {
        "titulo": "Gestión de Solicitudes de Servicio",
        "parrafos": [
            "La gestión de solicitudes de servicio comprende el conjunto de procedimientos administrativos orientados a recepcionar, registrar, procesar y dar seguimiento a los requerimientos presentados por los clientes o suscriptores de una organización. Zeithaml, Parasuraman y Berry (1993) establecen que la calidad del servicio percibida por el cliente está directamente vinculada a la capacidad de la organización para gestionar sus solicitudes de forma ágil, transparente y con comunicación fluida en cada etapa del proceso.",
            "En empresas de telecomunicaciones como IDETEL, la gestión de solicitudes abarca dos categorías principales: las solicitudes de afiliación de nuevos suscriptores, que implican la coordinación entre las áreas comercial, técnica y administrativa; y las incidencias reportadas por suscriptores activos, que requieren diagnóstico, despacho de cuadrillas y cierre verificado del caso. La ausencia de un sistema unificado de seguimiento para ambas categorías genera retrasos y reprocesos que impactan directamente en la satisfacción del cliente."
        ],
        "cita_larga": None
    },
    {
        "titulo": "Procesos Administrativos y Estandarización de Procedimientos",
        "parrafos": [
            "El proceso administrativo constituye el marco conceptual que rige el funcionamiento de las organizaciones modernas. Chiavenato (2006) lo describe como el conjunto secuencial e interrelacionado de funciones de planificación, organización, dirección y control, orientadas al logro eficiente de los objetivos organizacionales. La estandarización de los procedimientos dentro de este marco garantiza que las actividades se ejecuten de manera uniforme, reduciendo la variabilidad y los errores derivados de la discrecionalidad individual.",
            "La formalización de los procedimientos mediante manuales, flujogramas y formatos estandarizados constituye una herramienta esencial para el control administrativo. Según Harrington (1993), un proceso estandarizado es medible, controlable y mejorable, condiciones que permiten a la organización identificar con precisión los puntos de falla y aplicar acciones correctivas focalizadas. En el caso de IDETEL, la ausencia de procedimientos escritos para la gestión de solicitudes es una de las causas raíz de las deficiencias identificadas."
        ],
        "cita_larga": None
    },
    {
        "titulo": "Calidad del Servicio en Empresas de Telecomunicaciones",
        "parrafos": [
            "La calidad del servicio se define como el grado en que las características del servicio prestado satisfacen o superan las expectativas del cliente. Parasuraman, Zeithaml y Berry (1988) desarrollaron el modelo SERVQUAL, que identifica cinco dimensiones de la calidad del servicio: fiabilidad, capacidad de respuesta, seguridad, empatía y elementos tangibles. En el sector de telecomunicaciones, la fiabilidad y la capacidad de respuesta son las dimensiones con mayor peso en la percepción del cliente.",
            "Las deficiencias en el control administrativo del proceso de solicitudes de servicio impactan directamente sobre la fiabilidad y la capacidad de respuesta de IDETEL. Cuando una solicitud no es gestionada dentro de los tiempos establecidos o su estatus no puede ser verificado en tiempo real, el cliente percibe una falla en la calidad del servicio que deteriora su confianza en la organización y puede derivar en la cancelación del contrato o en la difusión de experiencias negativas."
        ],
        "cita_larga": None
    },
    {
        "titulo": "Sistemas de Información para el Control Administrativo",
        "parrafos": [
            "Un sistema de información constituye un conjunto organizado de recursos tecnológicos y procedimentales orientados a la captura, almacenamiento, procesamiento y distribución de datos con el propósito de apoyar la toma de decisiones. Laudon y Laudon (2016) distinguen los sistemas de procesamiento de transacciones como la categoría que registra y gestiona las operaciones rutinarias de la organización, siendo esta la tipología más pertinente para el control de solicitudes de servicio en una empresa de telecomunicaciones.",
            "La implementación de un sistema de tickets o plataforma de seguimiento de solicitudes en IDETEL permitiría centralizar el registro de cada caso, asignar responsables, definir tiempos de atención y generar alertas ante incumplimientos. Esta herramienta transformaría el control administrativo de reactivo a proactivo, dotando a la supervisión de información en tiempo real para la toma de decisiones y la evaluación continua del desempeño del proceso."
        ],
        "cita_larga": None
    },
    {
        "titulo": "Proyecto Factible como Modalidad de Investigación",
        "parrafos": [
            "La Universidad Pedagógica Experimental Libertador (UPEL, 2016) define el proyecto factible como la investigación, elaboración y desarrollo de una propuesta de un modelo operativo viable para solucionar problemas, requerimientos o necesidades de organizaciones o grupos sociales. Esta modalidad exige un diagnóstico de campo que evidencie la situación deficitaria y la comprobación de la viabilidad técnica y operativa de la solución planteada.",
            "Arias (2012) señala que el proyecto factible avanza hasta proponer y en muchos casos desarrollar la solución, demostrando su aplicabilidad en el contexto real. El presente trabajo se enmarca en esta modalidad al partir de la evaluación del control administrativo de IDETEL para proponer mejoras procedimentales cuya implementación es viable dentro de la estructura organizativa y los recursos disponibles de la empresa."
        ],
        "cita_larga": None
    }
]

POST_CITA_TEXTO = "El control administrativo, como lo señalan los autores referidos, no se limita a una función de fiscalización, sino que se constituye en un mecanismo de retroalimentación continua que permite a la organización detectar desviaciones a tiempo y ajustar sus procesos para garantizar la calidad del servicio prestado al suscriptor."

# 7. CAPÍTULO IV - Actividades Realizadas
ACTIVIDADES_DESCRIPCION = "Durante las diez (10) semanas de pasantías, se llevaron a cabo actividades de evaluación y análisis en el Departamento de Administración de Ingeniería de Telecomunicaciones, C.A.:"
ACTIVIDADES_LISTA = [
    {
        "semana": 1,
        "operativa": "Inducción institucional, recorrido por las instalaciones, presentación ante el equipo del Departamento de Administración y familiarización con los sistemas de registro y los procedimientos generales de la empresa.",
        "investigacion": "Observación directa del flujo de recepción y procesamiento de solicitudes de servicio, identificación preliminar de los actores involucrados en el proceso y formulación inicial de la situación problemática."
    },
    {
        "semana": 2,
        "operativa": "Apoyo en la recepción y registro de solicitudes de afiliación de nuevos suscriptores, verificación de documentación requerida y actualización del sistema de control de casos activos.",
        "investigacion": "Levantamiento detallado del flujo procedimental de solicitudes de instalación e incidencias mediante la revisión de registros históricos y la documentación interna disponible en el departamento."
    },
    {
        "semana": 3,
        "operativa": "Colaboración en el seguimiento de solicitudes de servicio activas, actualización del estatus de los casos en el sistema de registro del departamento y apoyo en la coordinación con el área técnica.",
        "investigacion": "Diseño y aplicación de guía de observación directa sobre el proceso de gestión de solicitudes, registrando los tiempos de respuesta por etapa y los puntos de interrupción del flujo."
    },
    {
        "semana": 4,
        "operativa": "Apoyo en la atención al suscriptor vía telefónica y presencial, registro de incidencias reportadas y coordinación con el NOC para el despacho de cuadrillas técnicas de campo.",
        "investigacion": "Aplicación de entrevistas no estructuradas al personal administrativo, comercial y técnico para identificar las deficiencias percibidas en el sistema de control de solicitudes de servicio."
    },
    {
        "semana": 5,
        "operativa": "Colaboración en la actualización del registro de suscriptores activos, verificación del cierre de casos pendientes y apoyo en la elaboración de reportes de incidencias del período.",
        "investigacion": "Diagnóstico situacional de las deficiencias del control administrativo, elaboración de la matriz de fallas identificadas y análisis de los tiempos promedio de atención por tipo de solicitud."
    },
    {
        "semana": 6,
        "operativa": "Apoyo en la tramitación de contratos de nuevos suscriptores, verificación de la documentación requerida y actualización del registro de afiliaciones del período en el sistema del departamento.",
        "investigacion": "Análisis del impacto de las deficiencias detectadas sobre la calidad del servicio percibida por los suscriptores, mediante correlación entre tiempos de atención y quejas registradas."
    },
    {
        "semana": 7,
        "operativa": "Colaboración en la revisión y archivo de expedientes administrativos del ciclo, apoyo en la conciliación de pagos de suscriptores y actualización de la base de datos de clientes.",
        "investigacion": "Diseño del nuevo flujo de trabajo estandarizado para la gestión de solicitudes, con definición de etapas, responsables, tiempos máximos de respuesta y puntos de control por fase."
    },
    {
        "semana": 8,
        "operativa": "Apoyo en la generación de reportes de incidencias y solicitudes del período para la supervisión administrativa, y colaboración en la atención de requerimientos de suscriptores activos.",
        "investigacion": "Diseño de los formatos estandarizados de registro de solicitudes de afiliación y de incidencias, y elaboración del procedimiento escrito para la gestión unificada de casos en el departamento."
    },
    {
        "semana": 9,
        "operativa": "Participación en las actividades regulares del departamento y apoyo en el cierre administrativo del ciclo de atención al suscriptor correspondiente al período de pasantías.",
        "investigacion": "Redacción y validación de la propuesta de mejora al control administrativo de solicitudes de servicio, incorporando las observaciones del tutor industrial y ajustando los procedimientos al contexto operativo de IDETEL."
    },
    {
        "semana": 10,
        "operativa": "Presentación formal de la propuesta de mejora ante la supervisión del Departamento de Administración y firma de la carta de aprobación del tutor industrial.",
        "investigacion": "Consolidación y revisión final del informe académico de pasantías, incorporación de los anexos definitivos y preparación del documento para la entrega institucional al IUTECP."
    }
]

# 8. CAPÍTULO V - Conclusiones y Recomendaciones
CONCLUSIONES = [
    "Se describió el proceso administrativo actual de gestión de solicitudes de IDETEL, identificando un flujo de cuatro etapas (recepción, asignación, ejecución y cierre) que opera sin procedimientos escritos formales, dependiendo de canales informales de comunicación entre las áreas comercial, administrativa y técnica.",
    "Se identificaron como principales deficiencias del control administrativo la ausencia de un sistema unificado de seguimiento de casos, la falta de formatos estandarizados de registro, la inexistencia de tiempos de respuesta definidos por etapa y la carencia de indicadores de gestión que permitan evaluar el desempeño del proceso.",
    "Se determinó que las debilidades detectadas en el control administrativo generan impactos directos sobre la calidad del servicio percibida por los suscriptores, manifestados en tiempos de atención prolongados, falta de trazabilidad en el estatus de los casos y dificultades en la coordinación interdepartamental que derivan en reprocesos y quejas reiteradas.",
    "Se formuló una propuesta de mejora al control administrativo que contempla un nuevo flujo de trabajo estandarizado con etapas y responsables definidos, formatos unificados de registro de solicitudes e incidencias, y un conjunto de indicadores de gestión para el monitoreo continuo del proceso de atención al suscriptor."
]

RECOMENDACIONES = [
    "Implementar el nuevo flujo de trabajo estandarizado propuesto, comenzando por la formalización del canal de recepción de solicitudes y la adopción de los formatos unificados de registro de afiliaciones e incidencias en todos los departamentos involucrados.",
    "Socializar el manual de procedimientos de gestión de solicitudes con el personal de las áreas administrativa, comercial y técnica, garantizando que cada actor conozca su rol, sus responsabilidades y los tiempos máximos de respuesta establecidos para cada fase del proceso.",
    "Establecer indicadores de gestión para el proceso de atención al suscriptor, tales como el tiempo promedio de resolución de incidencias, el porcentaje de solicitudes cerradas dentro del plazo y el índice de reincidencias por caso, con seguimiento mensual por parte de la supervisión.",
    "Evaluar la incorporación de una plataforma de gestión de tickets de código abierto que centralice el registro y seguimiento de solicitudes en tiempo real, eliminando la dependencia de canales informales de comunicación y dotando a la organización de trazabilidad completa sobre el ciclo de vida de cada caso."
]

# 9. Referencias Bibliográficas
REFERENCIAS_LISTA = [
    "Arias, F. (2012). El proyecto de investigación: Introducción a la metodología científica (6ta ed.). Episteme, Venezuela.",
    "Chiavenato, I. (2006). Introducción a la teoría general de la administración (7ma ed.). McGraw-Hill, México.",
    "Harrington, H. J. (1993). Mejoramiento de los procesos de la empresa. McGraw-Hill, Colombia.",
    "Laudon, K., y Laudon, J. (2016). Sistemas de información gerencial (14va ed.). Pearson Educación, México.",
    "Parasuraman, A., Zeithaml, V., y Berry, L. (1988). SERVQUAL: A multiple-item scale for measuring consumer perceptions of service quality. Journal of Retailing, 64(1), 12-40.",
    "Robbins, S., y Coulter, M. (2010). Administración (10ma ed.). Pearson Educación, México.",
    "Universidad Pedagógica Experimental Libertador. (2016). Manual de trabajos de grado de especialización y maestría y tesis doctorales (5ta ed.). FEDUPEL, Venezuela.",
    "Zeithaml, V., Parasuraman, A., y Berry, L. (1993). Calidad total en la gestión de servicios. Díaz de Santos, España."
]

# 10. Anexos
ANEXOS_LISTA = [
    ("ANEXO A", "Flujograma del proceso de gestión de solicitudes de servicios", 4, 17)
]
