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
    "\"ELÍAS CALIXTO POMPA\" (IUTECP)",
    "EL TIGRE, ESTADO ANZOÁTEGUI"
]

TITULO_PROYECTO = "EVALUACIÓN DEL CONTROL ADMINISTRATIVO APLICADO A LA GESTIÓN DE SOLICITUDES DE SERVICIOS DE TELECOMUNICACIONES EN LA EMPRESA INGENIERÍA DE TELECOMUNICACIONES, C.A."

AUTOR_DATOS = [
    "Autor: Alrifaai Alrifaaie Amaal",
    "C.I.: 31.985.792",
    "",
    "Tutor Industrial: [Nombre del Tutor Industrial]",
    "C.I.: [Cédula del Tutor Industrial]",
    "",
    "Tutor Académico: [Nombre del Tutor Académico]",
    "C.I.: [Cédula del Tutor Académico]"
]

FECHA_LUGAR = "El Tigre, julio de 2026"

RAZON_SOCIAL = "Ingeniería de Telecomunicaciones, C.A. (IDETEL / INTELCA)"

# 3. Páginas Preliminares
DEDICATORIA = "Aquí va la dedicatoria."

AGRADECIMIENTOS = "Aquí van los agradecimientos."

RESUMEN_TEXTO = (
    "Aquí va el resumen del informe. El presente informe describe la evaluación del control administrativo "
    "aplicado a la gestión de solicitudes de servicios de telecomunicaciones en la empresa Ingeniería de "
    "Telecomunicaciones, C.A. (IDETEL). La investigación se enmarca en la modalidad de proyecto factible "
    "apoyado en un diagnóstico de campo. [Completar con el resto del resumen: objetivo general, metodología, "
    "resultados y conclusiones principales.]"
)

PALABRAS_CLAVE = "control administrativo, solicitudes de servicios, telecomunicaciones, proyecto factible, pasantías."

INTRODUCCION_TEXTO = (
    "Aquí va la introducción. La presente pasantía, desarrollada como requisito para optar al título de Técnico "
    "Superior Universitario en Administración, tiene como propósito evaluar el control administrativo aplicado "
    "a la gestión de solicitudes de servicios de telecomunicaciones en la empresa Ingeniería de "
    "Telecomunicaciones, C.A. [Completar con la estructura del informe: capítulos, enfoque metodológico y alcance.]"
)

# 4. CAPÍTULO I - Realidad Organizacional
IDENTIFICACION_EMPRESA = (
    "La pasantía profesional se llevó a cabo en Ingeniería de Telecomunicaciones, C.A., empresa del sector "
    "tecnológico conocida comercialmente bajo las siglas IDETEL o INTELCA, registrada bajo el Registro de "
    "Información Fiscal (RIF) N° J-08011691-7. La organización actúa como operador autorizado por la Comisión "
    "Nacional de Telecomunicaciones (CONATEL) y se desempeña como Distribuidor Autorizado de la marca Motorola "
    "en la región oriental del país."
)

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
        "Observación directa y revisión documental de los procedimientos internos.",
        "Guía de observación, documentos de la empresa, PC.",
        "Mapeo del flujo actual de solicitudes."
    ),
    (
        "Identificar las deficiencias en el control administrativo de solicitudes.",
        "Entrevistas al personal administrativo y revisión de registros históricos.",
        "Guía de entrevista, históricos de tickets, PC.",
        "Matriz de deficiencias identificadas."
    ),
    (
        "Analizar el impacto de las debilidades en la calidad del servicio.",
        "Análisis de tiempos de respuesta y correlación con quejas de suscriptores.",
        "Base de datos de incidencias, hojas de cálculo.",
        "Informe analítico de impacto."
    ),
    (
        "Proponer mejoras al proceso de control administrativo.",
        "Diseño de procedimientos estandarizados y formatos de control.",
        "Procesador de texto, normativas internas.",
        "Propuesta de mejora procedimental formulada."
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

# 7. CAPÍTULO IV - Actividades Realizadas
ACTIVIDADES_DESCRIPCION = "Durante las diez (10) semanas de pasantías, se llevaron a cabo actividades de evaluación y análisis en el Departamento de Administración de Ingeniería de Telecomunicaciones, C.A.:"
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
    },
    {
        "semana": 7,
        "operativa": "Aquí va la actividad operativa de la semana 7. [Completar con la tarea realizada en la empresa.]",
        "investigacion": "Aquí va la actividad de investigación de la semana 7. [Completar con la tarea académica realizada.]"
    },
    {
        "semana": 8,
        "operativa": "Aquí va la actividad operativa de la semana 8. [Completar con la tarea realizada en la empresa.]",
        "investigacion": "Aquí va la actividad de investigación de la semana 8. [Completar con la tarea académica realizada.]"
    },
    {
        "semana": 9,
        "operativa": "Aquí va la actividad operativa de la semana 9. [Completar con la tarea realizada en la empresa.]",
        "investigacion": "Aquí va la actividad de investigación de la semana 9. [Completar con la tarea académica realizada.]"
    },
    {
        "semana": 10,
        "operativa": "Aquí va la actividad operativa de la semana 10. [Completar con la tarea realizada en la empresa.]",
        "investigacion": "Aquí va la actividad de investigación de la semana 10. [Completar con la tarea académica realizada.]"
    }
]

# 8. CAPÍTULO V - Conclusiones y Recomendaciones
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

# 9. Referencias Bibliográficas
REFERENCIAS_LISTA = [
    "Aquí va la primera referencia bibliográfica en formato APA. [Completar con autor, año, título, editorial y ciudad.]",
    "Aquí va la segunda referencia bibliográfica en formato APA. [Completar con autor, año, título, editorial y ciudad.]",
    "Aquí va la tercera referencia bibliográfica en formato APA. [Completar con autor, año, título, editorial y ciudad.]"
]

# 10. Anexos
ANEXOS_LISTA = [
    ("ANEXO A", "Aquí va la descripción del Anexo A"),
    ("ANEXO B", "Aquí va la descripción del Anexo B"),
    ("ANEXO C", "Aquí va la descripción del Anexo C")
]
