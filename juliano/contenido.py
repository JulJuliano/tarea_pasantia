# 1. Rutas y Carpetas
CARPETA_IMAGENES = "imagenes"
# Gráficos del informe: cada uno indica tras qué sección va (anclas: "ubicacion" | "estructura")
# "lista" = descripción corta para el índice (Lista de Gráficos), "pagina" = página estimada
GRAFICOS = [
    { "numero": 1, "tras": "estructura", "titulo": "Gráfico 1. Organigrama estructural y niveles jerárquicos de Venangocupet, S.A.", "ancho_cm": 12, "lista": "Organigrama estructural y niveles jerárquicos de Venangocupet, S.A.", "pagina": "3" },
    { "numero": 2, "tras": "estructura", "titulo": "Gráfico 2. Organigrama del Departamento de Presidencia.", "ancho_cm": 12, "lista": "Organigrama del Departamento de Presidencia.", "pagina": "4" },
]

# Textos introductorios del Capítulo II
PLANIFICACION_INTRO_TEXTO = "La planificación establece la relación entre cada objetivo y las actividades técnicas a ejecutar para el desarrollo del proyecto factible:"
CRONOGRAMA_INTRO_TEXTO = "El cronograma estructura temporalmente las fases de diseño y desarrollo del sistema automatizado, distribuidas a lo largo de las nueve (9) semanas de duración de la pasantía:"

# Título del Cuadro 2 (Cronograma)
CUADRO_CRONOGRAMA_TITULO = "Cuadro 2. Cronograma de actividades del proyecto factible."

# Lista de Cuadros (índice preliminar): (número, descripción, página)
CUADROS_INDICE = [
    ("1", "Planificación integral de objetivos específicos", "5"),
    ("2", "Cronograma de actividades del proyecto factible (9 semanas)", "6"),
]

# 2. Datos de Portada y Datos Personales
MEMBRETE = [
    "REPÚBLICA BOLIVARIANA DE VENEZUELA",
    "MINISTERIO DEL PODER POPULAR PARA LA EDUCACIÓN UNIVERSITARIA",
    "INSTITUTO UNIVERSITARIO DE TECNOLOGÍA",
    "\"ELÍAS CALIXTO POMPA\"",
    "EL TIGRE, ESTADO ANZOÁTEGUI"
]

TITULO_PROYECTO = "DISEÑO DE UN SISTEMA PARA EL CONTROL, TRAZABILIDAD Y REPORTE DE MOVIMIENTOS DOCUMENTALES EN LA PRESIDENCIA DE LA EMPRESA MIXTA PETROLERA VENANGOCUPET, S.A."

AUTOR_DATOS = [
    "Autor:",
    "Juliano Cardona",
    "C.I.: 32.281.199",
    "",
    "Tutor Industrial:",
    "Ing. Yasmin Sabaneta",
    "C.I.: 14.187.924",
    "",
    "Tutor Académico:",
    "Lic. Carlos Mendoza",
    "C.I.: 4.273.815"
]

FECHA_LUGAR = "El Tigre, julio de 2026"
RAZON_SOCIAL = "Empresa Mixta Petrolera Venangocupet, S.A."

# 3. Páginas Preliminares
DEDICATORIA = "A mi familia, por su apoyo incondicional en cada paso de mi formación académica y personal."

AGRADECIMIENTOS = "A la Empresa Mixta Petrolera Venangocupet, S.A., por abrir las puertas de su organización y brindar la oportunidad de desarrollar este proyecto técnico de la mano de excelentes profesionales."

RESUMEN_TEXTO = (
    "El presente informe describe el diseño de un sistema automatizado para el control, trazabilidad y reporte de movimientos documentales en la Presidencia de la Empresa Mixta Petrolera Venangocupet, S.A. La investigación se enmarca en la modalidad de proyecto factible apoyado en un diagnóstico de campo. Durante el estudio se identificaron demoras operativas derivadas de la transcripción manual en hojas de cálculo y deficiencias en la generación de reportes inmediatos ante altos volúmenes de concurrencia. La solución tecnológica abarca el modelado lógico de datos en SQLite y la construcción de una aplicación de escritorio mediante código HTML empaquetado con el framework Wails, optimizando el registro, búsqueda y auditoría del flujo documental para fortalecer la toma de decisiones gerenciales."
)

PALABRAS_CLAVE = "sistema, trazabilidad, automatización, Wails, proyecto factible, pasantías."

INTRODUCCION_TEXTO = (
    "La presente pasantía, desarrollada como requisito para optar al título de Técnico Superior Universitario en Informática, tiene como propósito proponer un sistema automatizado para el control de movimientos documentales en la Presidencia de Venangocupet, S.A. Este desarrollo busca sustituir el registro manual por una herramienta tecnológica de escritorio ágil y moderna, que garantice la trazabilidad de los expedientes, optimizando los tiempos de respuesta y dotando al departamento de un control exacto sobre la entrada y salida de oficios en alta dirección."
)

# 4. CAPÍTULO I - Realidad Organizacional
IDENTIFICACION_EMPRESA = (
    "La práctica profesional se desarrolla en la Empresa Mixta Petrolera Venangocupet, S.A., entidad filial de la Corporación Venezolana de Petróleo (CVP). Su actividad principal se centra en la exploración y producción primaria de hidrocarburos, operando bajo los lineamientos estratégicos de la División Ayacucho de la Faja Petrolífera del Orinoco."
)

RESENA_HISTORICA = [
    "Venangocupet, S.A. fue constituida formalmente el 26 de noviembre de 2012, como parte de la estrategia de alianzas para el desarrollo de la Faja Petrolífera del Orinoco. Inicialmente, su estructura accionaria estaba compuesta por un 60% correspondiente a Petróleos de Venezuela, S.A. (PDVSA), a través de la CVP, y un 40% distribuido entre socios internacionales.",
    "El 26 de octubre de 2023, se registró un hito corporativo cuando los socios internacionales cedieron sus participaciones accionarias, consolidando el 100% del capital bajo el control de la filial de la CVP. Desde entonces, la empresa enfoca sus esfuerzos en la optimización operativa y la modernización tecnológica en el estado Anzoátegui."
]

MISION = (
    "Realizar actividades primarias de hidrocarburos aplicando estrategias y tecnologías de calidad, con personal competente, motivado y con plena conciencia de seguridad ambiental hacia las personas, los bienes y el entorno. Su propósito es producir el máximo beneficio posible para la nación, en concordancia con el Plan Estratégico Socialista (P.E.S) de PDVSA."
)

VISION = (
    "Constituirse como una empresa de referencia por excelencia en el negocio de hidrocarburos, caracterizada por ser productiva, innovadora y oportuna. Aspirar a impulsar el desarrollo sustentable manteniéndose a la vanguardia tecnológica para minimizar costos operativos y maximizar la recuperación de reservas."
)

VALORES = [
    ("Responsabilidad", "Compromiso inquebrantable con la seguridad operativa y el bienestar del personal."),
    ("Excelencia", "Aplicación sistemática de altos estándares de calidad y rigor técnico en cada proceso."),
    ("Innovación", "Fomento del uso de tecnologías de punta para optimizar la gestión integral de la empresa."),
    ("Sentido Social", "Contribución activa al desarrollo productivo y la sostenibilidad como pilares operativos.")
]

OBJETIVOS_ORG = [
    "Maximizar la recuperación eficiente y segura de las reservas de hidrocarburos asignadas.",
    "Minimizar los costos operativos mediante la optimización de recursos tecnológicos y logísticos.",
    "Garantizar la trazabilidad y el reporte oportuno de la información administrativa de la empresa."
]

UBICACION = (
    "La Empresa Mixta Petrolera Venangocupet, S.A. se encuentra ubicada en el sur del estado Anzoátegui, operando geográficamente en los bloques asignados dentro de la División Ayacucho, Faja Petrolífera del Orinoco."
)

POBLACION = [
    "La estructura del talento humano de la organización refleja un equipo multidisciplinario especializado en la gestión administrativa y operativa. La población total del personal directo asciende a 107 trabajadores.",
    "El Departamento de Presidencia, donde se desarrolló la investigación técnica, actúa como el nodo principal de recepción, revisión y canalización de correspondencia ejecutiva. Su operatividad exige un alto nivel de eficiencia en el control de flujos documentales concurrentes."
]

ORGANIGRAMA_TEXTO = (
    "La arquitectura organizativa de Venangocupet, S.A. se fundamenta en un modelo jerárquico-funcional. La empresa está encabezada por la Junta Directiva y la Presidencia. A continuación, se presenta el organigrama general destacando el Área de Presidencia, contexto en el cual se aplicó el desarrollo tecnológico."
)

SITUACION_PROBLEMATICA = [
    "El proceso administrativo en el Departamento de Presidencia funciona estrictamente como un nodo de tránsito y validación. El flujo procedimental consiste en recibir expedientes externos, someterlos a revisión ortográfica y de formato, y registrarlos para su entrega al Presidente de la empresa. Una vez firmados, se registra su salida y se despachan de forma inmediata hacia su departamento de destino, sin retener documentos propios de forma permanente.",
    "Actualmente, el control de este ciclo se ejecuta mediante hojas de cálculo convencionales. El flujo de expedientes es azaroso, alternando entre volúmenes mínimos y escenarios de ingresos masivos concurrentes. En dichos picos de alta demanda, el registro basado en el copiado y pegado manual de datos repetitivos ralentiza severamente el procesamiento y propicia errores humanos, tales como la duplicación de datos o la omisión de movimientos críticos.",
    "Adicionalmente, este mecanismo dificulta la generación de reportes inmediatos. Cuando la alta dirección solicita conocer el resumen de documentos firmados en el mes o el estatus de los expedientes pendientes por firma, el personal debe filtrar, interpretar y redactar la información manualmente. Esto retrasa la respuesta operativa del departamento y evidencia la necesidad inminente de un salto tecnológico hacia la automatización."
]

OBJETIVO_GENERAL = "Proponer el desarrollo de un sistema automatizado para el control, trazabilidad y reporte de movimientos documentales en la Presidencia de la Empresa Mixta Petrolera Venangocupet, S.A., bajo la modalidad de proyecto factible."

OBJETIVOS_ESPECIFICOS = [
    "Diagnosticar la situación actual del flujo procedimental de recepción, firma y derivación de expedientes en el área de Presidencia.",
    "Determinar los requerimientos técnicos y funcionales necesarios para la base de datos de trazabilidad documental.",
    "Diseñar la arquitectura lógica del sistema relacional y la interfaz gráfica de usuario para el entorno de escritorio.",
    "Desarrollar un prototipo funcional del sistema empleando bases de datos y tecnologías de empaquetado para su validación operativa."
]

PLANIFICACION_DATOS = [
    (
        "Diagnosticar el flujo procedimental actual de los movimientos documentales.",
        "Observación directa del ciclo de expedientes y análisis de las fallas en las hojas de cálculo existentes.",
        "Cuaderno de notas, registros de Excel",
        "Diagnóstico con identificación de debilidades en el flujo documental y la trazabilidad."
    ),
    (
        "Determinar los requerimientos técnicos y funcionales del sistema.",
        "Levantamiento de metadatos requeridos (fechas, remitente, estatus) y definición de reglas de validación mediante entrevista no estructurada.",
        "Formatos de requerimientos, diccionario de datos",
        "Documento de especificación de requerimientos funcionales y técnicos."
    ),
    (
        "Diseñar la arquitectura lógica y la interfaz gráfica de usuario.",
        "Modelado del diagrama Entidad-Relación y diseño de los módulos visuales mediante análisis documental.",
        "Herramientas de modelado, editores de código",
        "Diagrama Entidad-Relación y maquetado de la interfaz gráfica aprobados."
    ),
    (
        "Desarrollar un prototipo funcional del sistema para su validación.",
        "Implementación en SQLite, integración de la interfaz con Wails y ejecución de pruebas de escritorio.",
        "Framework Wails, motor SQLite, equipo informático",
        "Prototipo funcional validado con pruebas de escritorio exitosas."
    )
]

# Matriz booleana ajustada a 8 SEMANAS exactas de pasantía
CRONOGRAMA_DATOS = [
    # ── ACTIVIDADES DEL PROYECTO (5) ──────────────────────────────────────────────────────────
    ("Diagnóstico del flujo documental y levantamiento de requerimientos.",    [True,  False, False, False, False, False, False, False, False]),
    ("Diseño del modelo relacional, normalización y diccionario de datos.",    [False, True,  False, False, False, False, False, False, False]),
    ("Implementación de la base de datos relacional en SQLite.",               [False, False, True,  False, False, False, False, False, False]),
    ("Desarrollo de la interfaz gráfica y empaquetado con Wails.",             [False, False, False, True,  True,  False, False, False, False]),
    ("Integración, pruebas funcionales y consolidación del sistema.",          [False, False, False, False, False, False, True,  True,  True ]),
    # ── ACTIVIDADES DE OFICINA (4) ────────────────────────────────────────────────────────────
    ("Inducción institucional y capacitación en seguridad (SIAHO).",           [True,  False, False, True,  False, False, False, False, False]),
    ("Registro y actualización de expedientes en hoja de cálculo.",            [False, True,  True,  False, False, False, False, False, False]),
    ("Revisión y canalización de correspondencia presidencial.",               [False, False, False, False, True,  True,  False, False, False]),
    ("Apoyo en generación de reportes y cierre administrativo.",               [False, False, False, False, False, False, False, True,  True ]),
]

# CAPÍTULO III - Marco Teórico
# Estructura: lista de subsecciones, cada una con título, párrafos
# y opcionalmente una cita larga (>40 palabras, bloque aparte).
# El generador debe iterar sobre BASES_TEORICAS para renderizar
# cada subsección como un encabezado de Nivel 2 + párrafos.

BASES_TEORICAS = [
    {
        "titulo": "Sistemas de Información",
        "parrafos": [
            "Un sistema de información constituye un conjunto organizado de recursos humanos, tecnológicos y procedimentales orientados a la captura, almacenamiento, procesamiento y distribución de datos con el propósito de apoyar la toma de decisiones dentro de una organización. Laudon y Laudon (2016) distinguen entre sistemas de procesamiento de transacciones, sistemas de soporte a la decisión y sistemas de información gerencial, siendo estos últimos los que transforman datos operativos en reportes consolidados de utilidad directiva.",
            "En el contexto del presente proyecto, el sistema propuesto se enmarca en la categoría de sistema de información operacional con capacidad de reporte gerencial, dado que registra cada movimiento documental de forma transaccional y provee resúmenes inmediatos al nivel de presidencia. Según Kendall y Kendall (2011), el análisis y diseño de sistemas busca comprender sistemáticamente cómo interactúan los datos y los usuarios para proponer soluciones tecnológicas que mejoren el flujo de trabajo de una organización."
        ],
        "cita_larga": {
            "texto": "Los sistemas de información gerencial proporcionan a los administradores informes sobre el desempeño actual de la organización. Esta información se utiliza para supervisar y controlar el negocio y predecir el desempeño futuro. Los sistemas de información gerencial resumen y reportan las operaciones básicas de la empresa usando datos suministrados por los sistemas de procesamiento de transacciones.",
            "autor": "(Laudon y Laudon, 2016, p. 46)"
        }
    },
    {
        "titulo": "Gestión Documental",
        "parrafos": [
            "La gestión documental se define como el conjunto de normas, técnicas y prácticas que regulan el ciclo de vida de los documentos dentro de una organización, desde su creación o recepción hasta su disposición final. Cruz Mundet (2011) señala que una gestión documental eficaz garantiza la autenticidad, integridad, fiabilidad y disponibilidad de la información registrada, constituyendo un pilar fundamental para la transparencia administrativa y la continuidad operativa.",
            "En el Departamento de Presidencia de Venangocupet, S.A., el flujo documental responde a un ciclo específico: recepción del expediente externo, revisión de forma, registro de ingreso, firma presidencial, registro de egreso y despacho al departamento destinatario. La automatización de este ciclo mediante un sistema digitalizado reduce la propensión al error humano y dota al departamento de un historial auditable de cada movimiento, en concordancia con los principios de gestión documental descritos por Cruz Mundet (2011)."
        ],
        "cita_larga": None
    },
    {
        "titulo": "Modelo Relacional de Bases de Datos",
        "parrafos": [
            "El modelo relacional, propuesto originalmente por Codd (1970), organiza la información en tablas bidimensionales denominadas relaciones, cuyos atributos representan las propiedades de las entidades y cuyas filas corresponden a instancias individuales de datos. La fortaleza de este modelo radica en la aplicación de reglas de normalización que eliminan la redundancia y preservan la integridad referencial entre tablas relacionadas mediante claves primarias y foráneas.",
            "Date (2001) establece que un diseño relacional correctamente normalizado garantiza que cada dato se almacene una sola vez, reduciendo la posibilidad de inconsistencias derivadas de actualizaciones parciales. En el sistema propuesto, la relación entre procesos administrativos y documentos sigue una cardinalidad uno a muchos (1:N), permitiendo registrar múltiples expedientes asociados a un mismo proceso contractual o administrativo sin duplicar los datos maestros del proceso."
        ],
        "cita_larga": None
    },
    {
        "titulo": "SQLite como Sistema Gestor de Base de Datos",
        "parrafos": [
            "SQLite es un motor de base de datos relacional de código abierto, autocontenido y sin servidor, cuya arquitectura embebida lo diferencia de sistemas cliente-servidor convencionales como MySQL o PostgreSQL. Su funcionamiento se basa en un único archivo portable que aloja el esquema completo de la base de datos, eliminando la necesidad de procesos de servidor independientes o configuraciones de red. Esta característica lo convierte en la opción técnica idónea para entornos corporativos con restricciones de instalación de software.",
            "Pressman (2010) señala que la selección de herramientas tecnológicas debe estar guiada por los atributos del entorno de despliegue y no exclusivamente por las capacidades abstractas del instrumento. En el caso particular del Departamento de Presidencia de Venangocupet, S.A., las restricciones de permisos administrativos sobre los equipos de la organización hacen de SQLite la alternativa técnicamente viable para implementar persistencia de datos sin requerir intervención del departamento de tecnología de la empresa."
        ],
        "cita_larga": None
    },
    {
        "titulo": "Trazabilidad Documental",
        "parrafos": [
            "La trazabilidad documental se entiende como la capacidad de reconstruir el historial completo de un documento a lo largo de su ciclo de vida, identificando en cada etapa el responsable, la fecha, la acción ejecutada y el estado resultante. Gómez (2019) señala que la trazabilidad constituye el mecanismo central de auditoría en los sistemas de gestión documental, dado que permite verificar la integridad del proceso y detectar cuellos de botella o irregularidades en el flujo.",
            "En el ámbito de la alta dirección, la trazabilidad cobra especial relevancia porque los expedientes que transitan por la Presidencia frecuentemente están vinculados a procesos contractuales y decisiones gerenciales de impacto organizacional. El sistema propuesto registra automáticamente cada movimiento de ingreso y egreso del expediente, almacenando la fecha, el estatus y el departamento de origen o destino, lo que permite generar reportes de trazabilidad de forma inmediata ante cualquier requerimiento directivo."
        ],
        "cita_larga": {
            "texto": "Un sistema de información eficaz proporciona a los administradores de la organización datos precisos y oportunos, facilitando la auditoría de cada transacción operativa y mejorando sustancialmente la capacidad de respuesta ante requerimientos gerenciales de alto nivel. La ausencia de este tipo de herramientas obliga al personal a invertir tiempo considerable en la búsqueda y consolidación manual de información que debería estar disponible de forma inmediata.",
            "autor": "(Gómez, 2019, p. 45)"
        }
    },
    {
        "titulo": "Automatización de Procesos Administrativos",
        "parrafos": [
            "La automatización de procesos administrativos consiste en la sustitución de tareas manuales repetitivas por flujos de trabajo controlados por sistemas informáticos, con el objetivo de reducir los tiempos de ejecución, minimizar el error humano y liberar al personal para actividades de mayor valor analítico. Laudon y Laudon (2016) plantean que la automatización de procesos de negocio genera mejoras medibles en la productividad organizacional al estandarizar los procedimientos y centralizar el control de la información.",
            "En el Departamento de Presidencia de Venangocupet, S.A., la automatización se justifica por la naturaleza del proceso actual: el personal destina un porcentaje significativo de su tiempo operativo al copiado y pegado de datos entre documentos y hojas de cálculo, así como a la redacción manual de resúmenes solicitados por la dirección. La implementación del sistema automatizado propuesto traslada estas tareas al software, permitiendo que el personal se concentre en las funciones de revisión y coordinación propias del departamento."
        ],
        "cita_larga": None
    },
    {
        "titulo": "Proyecto Factible como Modalidad de Investigación",
        "parrafos": [
            "La Universidad Pedagógica Experimental Libertador (UPEL, 2016) define el proyecto factible como la investigación, elaboración y desarrollo de una propuesta de un modelo operativo viable para solucionar problemas, requerimientos o necesidades de organizaciones o grupos sociales. Esta modalidad exige la comprobación de la viabilidad técnica, económica y operativa de la solución planteada, sustentada en un diagnóstico de campo que evidencie la situación deficitaria que da origen a la propuesta.",
            "Arias (2012) complementa esta definición señalando que el proyecto factible no se limita a diagnosticar un problema, sino que avanza hasta proponer y en muchos casos desarrollar la solución, demostrando su aplicabilidad en el contexto real. El presente trabajo se enmarca en esta modalidad al partir de un diagnóstico situacional del flujo documental en Presidencia, proponer una arquitectura tecnológica específica y materializar un prototipo funcional del sistema como evidencia de la viabilidad de la propuesta."
        ],
        "cita_larga": None
    }
]

# 7. CAPÍTULO IV - Actividades Realizadas
ACTIVIDADES_DESCRIPCION = "Durante las nueve (9) semanas de práctica profesional, se ejecutaron fases sucesivas de análisis, diseño y desarrollo de software, integrando la operativa departamental con la investigación técnica:"

# Estructura actualizada para separar Operativa e Investigación por semana
ACTIVIDADES_LISTA = [
    {
        "semana": 1,
        "operativa": "Inducción institucional por la Gerencia de Recursos Humanos, recorrido por las instalaciones del área administrativa, presentación del equipo de trabajo y revisión de protocolos de seguridad, confidencialidad y manejo de información.",
        "investigacion": "Observación directa y mapeo del ciclo de vida de los documentos en Presidencia, detección de fallas procedimentales en el registro manual y levantamiento de los campos y atributos requeridos para la base de datos de trazabilidad."
    },
    {
        "semana": 2,
        "operativa": "Transmisión, clasificación y registro manual de expedientes físicos en la hoja de cálculo institucional preexistente, y actualización continua de datos de nuevos documentos recibidos durante el período.",
        "investigacion": "Validación de requerimientos con el tutor industrial, construcción del diagrama Entidad-Relación, aplicación de las formas normales sobre el esquema propuesto y elaboración formal del diccionario de datos."
    },
    {
        "semana": 3,
        "operativa": "Procesamiento y actualización del estatus de expedientes en el archivo Excel de la oficina, con apoyo administrativo en el control de documentos recibidos durante la semana.",
        "investigacion": "Ejecución de la secuencia de comandos estructurales en SQLite, migración de registros históricos validados, construcción de formularios de captura y programación de consultas de trazabilidad con detección de limitaciones técnicas del entorno inicial."
    },
    {
        "semana": 4,
        "operativa": "Asistencia a la charla técnica sobre Identificación y Notificación de Peligros y Riesgos en Instalaciones y Puestos de Trabajo dictada por el departamento de SIAHO, y carga de expedientes recibidos en la hoja de cálculo.",
        "investigacion": "Programación del entorno visual de escritorio mediante tecnologías de marcado y estilos, sincronización del código fuente en plataforma de control de versiones y planificación estructural de los esquemas remanentes."
    },
    {
        "semana": 5,
        "operativa": "Revisión ortográfica y de formato de correspondencia presidencial, y apoyo en la canalización de expedientes hacia su departamento de destino tras la firma presidencial.",
        "investigacion": "Completación de los módulos visuales de consulta e historial de movimientos, integrando la lógica de visualización dinámica de expedientes por proceso administrativo."
    },
    {
        "semana": 6,
        "operativa": "Colaboración en la revisión y despacho de correspondencia presidencial y apoyo en el registro de salida de expedientes firmados durante el período.",
        "investigacion": "Empaquetado de la aplicación de escritorio mediante el framework Wails con integración de WebView2 portable, logrando un ejecutable autónomo sin dependencias de instalación en el equipo corporativo."
    },
    {
        "semana": 7,
        "operativa": "Apoyo en la elaboración manual de resúmenes de estatus de expedientes solicitados por la alta dirección, aplicando los registros de la hoja de cálculo del departamento.",
        "investigacion": "Ejecución de pruebas de validación funcional del sistema, depuración de errores y verificación del correcto funcionamiento de los módulos de registro, trazabilidad y generación de reportes sobre datos reales."
    },
    {
        "semana": 8,
        "operativa": "Participación en las actividades regulares del departamento y apoyo en el cierre administrativo del período, asistiendo en la organización final de expedientes del ciclo.",
        "investigacion": "Redacción del informe técnico de pasantías, elaboración de los manuales de usuario y estructuración definitiva del código fuente para entrega."
    },
    {
        "semana": 9,
        "operativa": "Presentación del prototipo funcional ante la tutora industrial para su evaluación, retroalimentación final y firma de la carta de aprobación del tutor industrial.",
        "investigacion": "Consolidación y revisión final del informe académico, incorporación de observaciones del tutor industrial y preparación de los anexos definitivos para la entrega institucional."
    }
]

# 8. CAPÍTULO V - Conclusiones y Recomendaciones
# Conclusiones actualizadas (una por cada objetivo específico)
CONCLUSIONES = [
    "Se diagnosticó que la dependencia del registro manual en hojas de cálculo genera cuellos de botella en escenarios de alta concurrencia documental, propiciando la duplicación de datos y la omisión de movimientos críticos que comprometen la trazabilidad del flujo en Presidencia.",
    "Se determinó que los requerimientos funcionales del sistema giran en torno a tres módulos esenciales: registro de ingreso y egreso de expedientes, consulta de historial por proceso administrativo y generación automática de reportes gerenciales, todos sustentados en una estructura relacional 1:N entre procesos y documentos.",
    "Se diseñó una arquitectura lógica basada en el modelo relacional normalizado con SQLite como motor de persistencia y una interfaz gráfica desarrollada en código HTML, logrando una solución técnicamente coherente con las restricciones operativas del entorno corporativo.",
    "Se desarrolló un prototipo funcional empaquetado con el framework Wails que demostró la viabilidad técnica de la propuesta, validando los flujos de registro, consulta y reporte sobre datos reales del Departamento de Presidencia."
]

# Recomendaciones actualizadas y ampliadas
RECOMENDACIONES = [
    "Ejecutar la migración progresiva de los registros históricos contenidos en las hojas de cálculo hacia la base de datos del nuevo sistema, preservando la trazabilidad de los expedientes anteriores al período de implementación.",
    "Capacitar al personal administrativo del Departamento de Presidencia en el uso de las interfaces de registro, consulta y generación de reportes del sistema, garantizando la correcta apropiación tecnológica de la herramienta.",
    "Establecer rutinas periódicas de respaldo del archivo de base de datos (.sqlite) en una unidad de almacenamiento alternativa, con el fin de salvaguardar la integridad del historial documental ante eventuales fallas del equipo.",
    "Extender el alcance del sistema en fases posteriores para incorporar notificaciones automáticas a los departamentos destinatarios una vez despachado el expediente firmado, optimizando la comunicación interdepartamental."
]

# 9. Referencias Bibliográficas (orden alfabético estricto, sangría francesa)
REFERENCIAS_LISTA = [
    "Arias, F. (2012). El proyecto de investigación: Introducción a la metodología científica (6ta ed.). Episteme, Venezuela.",
    "Codd, E. F. (1970). A relational model of data for large shared data banks. Communications of the ACM, 13(6), 377-387.",
    "Cruz Mundet, J. R. (2011). Administración de documentos y archivos: Textos fundamentales. Coordinadora de Asociaciones de Archiveros, España.",
    "Date, C. J. (2001). Introducción a los sistemas de bases de datos (7ma ed.). Pearson Educación, México.",
    "Gómez, R. (2019). Gestión Documental y Sistemas. Editorial Trillas, México.",
    "Kendall, K., y Kendall, J. (2011). Análisis y diseño de sistemas (8va ed.). Pearson Educación, México.",
    "Laudon, K., y Laudon, J. (2016). Sistemas de información gerencial (14va ed.). Pearson Educación, México.",
    "Pressman, R. (2010). Ingeniería de Software: Un enfoque práctico (7ma ed.). McGraw-Hill, México.",
    "Universidad Pedagógica Experimental Libertador. (2016). Manual de trabajos de grado de especialización y maestría y tesis doctorales (5ta ed.). FEDUPEL, Venezuela."
]

# 10. Anexos
ANEXOS_LISTA = [
    ("ANEXO A", "Diagrama Entidad-Relación de la Base de Datos"),
    ("ANEXO B", "Capturas de la Interfaz del Sistema (Wails/HTML)"),
    ("ANEXO C", "Memoria Fotográfica del Área de Presidencia")
]
