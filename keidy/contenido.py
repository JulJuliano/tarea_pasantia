# -*- coding: utf-8 -*-
# Archivo revisado para informe de pasantías regulares IUTECP.

# ========================================================================
# 1. RUTAS, IMÁGENES Y CUADROS
# ========================================================================
CARPETA_IMAGENES = 'imagenes'


GRAFICOS = [
    {
        'numero': 1,
        'archivo': 'logo.jpg',
        'tras': 'logo_empresa',
        'titulo': 'Gráfico 1. Logotipo de Lubricantes y Equipos Varyna, C.A.',
        'ancho_cm': 4.2,
        'lista': 'Logotipo de Lubricantes y Equipos Varyna, C.A.',
        'pagina': '3',
        'fuente': 'Lubricantes y Equipos Varyna, C.A. (2026).',},
    {
        'numero': 2,
        'archivo': '1.png',
        'tras': 'ubicacion',
        'titulo': 'Gráfico 2. Representación cartográfica y ubicación espacial de la empresa.',
        'ancho_cm': 5,
        'lista': 'Representación cartográfica y ubicación espacial de la empresa',
        'pagina': '4'
    },
    {
        'numero': 3,
        'archivo': '2.png',
        'tras': 'estructura',
        'titulo': 'Gráfico 3. Organigrama estructural y niveles jerárquicos de la organización.',
        'ancho_cm': 12,
        'lista': 'Organigrama estructural y niveles jerárquicos de la organización',
        'pagina': '5'
    }
]

PLANIFICACION_INTRO_TEXTO = ('La planificación relaciona los tres objetivos específicos con las actividades, técnicas e instrumentos '
 'necesarios para diagnosticar el proceso, identificar sus deficiencias y formular la propuesta de simplificación '
 'administrativa:')

CRONOGRAMA_INTRO_TEXTO = ('El cronograma distribuye las actividades operativas y de análisis durante las diez (10) semanas de pasantía, '
 'manteniendo correspondencia con los objetivos específicos:')

CUADRO_CRONOGRAMA_TITULO = 'Cuadro 2. Cronograma de actividades de la pasantía.'

CUADROS_INDICE = [('1', 'Planificación integral de objetivos específicos', '7'),
 ('2', 'Cronograma de actividades de la pasantía', '8')]

# Configuración particular indicada por la tutora académica (06/08/2026).
MOSTRAR_NIVELES_DIAGNOSTICO = True
ETIQUETA_ACTIVIDAD_ANALISIS = 'Actividad de análisis'
CUADRO_PLANIFICACION_FUENTE = 'La autora (2026).'
CUADRO_CRONOGRAMA_FUENTE = 'La autora (2026).'

# ========================================================================
# 2. DATOS DE PORTADA
# ========================================================================
MEMBRETE = ['REPÚBLICA BOLIVARIANA DE VENEZUELA',
 'MINISTERIO DEL PODER POPULAR PARA LA EDUCACIÓN UNIVERSITARIA',
 'INSTITUTO UNIVERSITARIO DE TECNOLOGÍA',
 '"ELÍAS CALIXTO POMPA"',
 'EL TIGRE, ESTADO ANZOÁTEGUI']

TITULO_PROYECTO = 'PROPUESTA DE SIMPLIFICACIÓN ADMINISTRATIVA DE LA PROCURA EN LUBRICANTES Y EQUIPOS VARYNA, C.A.'

AUTOR_DATOS = ['Autor:',
 'Guzmán, Keidy',
 'C.I.: 28.706.352',
 '',
 'Tutor Industrial:',
 'Rondón, Martina',
 'C.I.: 12.208.768',
 '',
 'Tutor Académico:',
 'Dra. Carmen J. Álvarez',
 'C.I.: 14.452.956']

FECHA_LUGAR = 'El Tigre, agosto de 2026'

CIUDAD_FECHA = FECHA_LUGAR

NOMBRE_PASANTE = 'Guzmán, Keidy'

CI_PASANTE = '28.706.352'

ESPECIALIDAD = 'Administración'

# ========================================================================
# 3. PÁGINAS PRELIMINARES
# ========================================================================
DEDICATORIA = ('A mi familia, por acompañarme con paciencia, apoyo y motivación durante mi formación académica y en cada etapa de estas pasantías. '
                'Dedico especialmente este logro a quienes han confiado en mí y me han impulsado a continuar creciendo personal y profesionalmente.')

AGRADECIMIENTOS = ('Agradezco al Instituto Universitario de Tecnología "Elías Calixto Pompa" (IUTECP) por los conocimientos y orientaciones brindados durante mi formación; '
                      'a Lubricantes y Equipos Varyna, C.A., por permitirme realizar las pasantías profesionales en su Departamento Administrativo y conocer de manera directa sus procesos de procura; '
                      'a mi tutora académica, Dra. Carmen J. Álvarez, y a mi tutora industrial, Martina Rondón, por sus observaciones, acompañamiento y disposición durante el desarrollo del informe; '
                      'y a todas las personas que colaboraron conmigo durante este período, por su apoyo y por los aprendizajes compartidos.')

RESUMEN_TEXTO = ('El presente informe corresponde a las pasantías profesionales realizadas durante diez (10) semanas en el '
 'Departamento Administrativo de Lubricantes y Equipos Varyna, C.A., con participación directa en actividades '
 'relacionadas con la procura de materiales e insumos. Durante la práctica se observó que las requisiciones de '
 'compra no siempre siguen un canal único y formalizado desde su recepción hasta la emisión y seguimiento de la '
 'orden de compra. También se evidenció la ausencia de formatos uniformes para algunas solicitudes, dificultades '
 'para conocer oportunamente el estado de las cotizaciones y falta de criterios visibles que faciliten el '
 'seguimiento de las aprobaciones. Estas condiciones pueden producir demoras, pérdida de trazabilidad y mayor '
 'carga administrativa para el personal encargado. El objetivo general fue proponer la simplificación '
 'administrativa del proceso de procura en el departamento, con la finalidad de reducir pasos innecesarios, '
 'agilizar los tiempos de adquisición y fortalecer el control interno. Para ello se realizaron observaciones del '
 'flujo de compras, entrevistas al personal, revisión de expedientes históricos, análisis de tiempos y un '
 'diagrama de causa-efecto para organizar los factores asociados a los retrasos. Como resultado se formuló una '
 'propuesta compuesta por un flujo simplificado con responsables definidos, formatos estandarizados de solicitud '
 'de cotización y orden de compra, una matriz de autorización por monto y criterios de seguimiento mediante '
 'indicadores de gestión. Se concluye que la formalización de estas herramientas puede facilitar el control y '
 'reducir la dispersión del proceso. Se recomienda implementar la propuesta de manera gradual, socializarla con '
 'el personal involucrado y revisar periódicamente sus resultados para realizar los ajustes necesarios.')

PALABRAS_CLAVE = 'procura, simplificación administrativa, control interno, requisiciones, pasantías'

INTRODUCCION_TEXTO = ['Las pasantías profesionales permiten vincular los conocimientos adquiridos durante la formación en '
 'Administración con situaciones reales de funcionamiento organizacional. En el área administrativa, la procura '
 'representa un proceso de apoyo indispensable porque articula la recepción de requerimientos, búsqueda de '
 'cotizaciones, evaluación de alternativas, aprobación y adquisición de bienes o servicios necesarios para la '
 'continuidad de las operaciones.',
 'En Lubricantes y Equipos Varyna, C.A., las actividades de pasantía se desarrollaron en el Departamento '
 'Administrativo con énfasis en el área de procura. Durante la práctica se identificaron oportunidades de mejora '
 'relacionadas con la recepción de requisiciones, el seguimiento de cotizaciones, la estandarización de formatos '
 'y la definición del recorrido que debe seguir cada solicitud de compra. Estas condiciones justificaron la '
 'formulación de una propuesta de simplificación administrativa adaptada a la dinámica del departamento.',
 'El propósito del informe es presentar el diagnóstico realizado, los objetivos definidos, la planificación de '
 'las actividades y la propuesta formulada. Como soporte conceptual se abordan la procura, el proceso '
 'administrativo, el control interno y la simplificación de procedimientos, complementados con un marco legal '
 'general relacionado con la actividad económica y el orden de los registros mercantiles.',
 'El informe se organiza en cinco capítulos. El Capítulo I describe la realidad organizacional de Lubricantes y '
 'Equipos Varyna, C.A.; el Capítulo II presenta la situación problemática, los objetivos, la planificación '
 'integral y el cronograma; el Capítulo III desarrolla los fundamentos teóricos y legales; el Capítulo IV '
 'describe las actividades operativas y de análisis realizadas durante las diez semanas; y el Capítulo V contiene '
 'las conclusiones y recomendaciones derivadas de la experiencia de pasantía.']

# ========================================================================
# 4. CAPÍTULO I — REALIDAD ORGANIZACIONAL
# ========================================================================
RAZON_SOCIAL = 'Lubricantes y Equipos Varyna, C.A.'

RESENA_HISTORICA = ['Lubricantes y Equipos Varyna, C.A. es una empresa venezolana fundada con la visión de responder a las '
 'crecientes demandas operativas e industriales del país. A lo largo de más de treinta y seis (36) años de '
 'trayectoria ininterrumpida, la organización se ha consolidado en el sector petrolero, industrial y de '
 'construcción, posicionándose como un aliado estratégico de alta confiabilidad en el mercado nacional gracias a '
 'su capacidad de respuesta y solvencia técnica.',
 'Desde sus primeros años de operaciones, la empresa enfocó su estrategia en la diversificación técnica de sus '
 'servicios, pasando de ser un proveedor local de insumos a una estructura corporativa especializada en el '
 'procesamiento y suministro de productos químicos de alto rendimiento, tratamiento químico de crudo y provisión '
 'de maquinaria pesada para proyectos de gran escala. Este desarrollo progresivo le permitió establecer '
 'estándares operacionales alineados con las exigencias de la industria energética regional y nacional.',
 'Su integración como parte fundamental del Grupo Corporativo VTC marcó un hito en su madurez organizacional, '
 'impulsando un crecimiento sostenido mediante la profesionalización de sus procesos, la adopción de tecnologías '
 'de vanguardia y la consolidación de alianzas comerciales de largo alcance. Hoy en día, Lubricantes y Equipos '
 'Varyna, C.A. mantiene su compromiso con el desarrollo productivo del país, sustentando su liderazgo en la '
 'innovación continua, la calidad de servicio y el fortalecimiento constante de su capital humano y capacidad '
 'logística.']

MISION = ('Brindar a nuestros clientes objetivos, soluciones de calidad en las áreas en las cuales nos desempeñamos, para '
 'contribuir de manera significativa en sus resultados. Aportando valor con nuestras respuestas a sus '
 'requerimientos. En la búsqueda de un mejor país y de una mejor humanidad.')

VISION = ('Ser el conglomerado de empresas líderes en cada una de las categorías en las que participamos, generando '
 'modelos de negocios altamente competitivos, atendiendo a nuestros distintos beneficiarios con productos y '
 'servicios de calidad.')

VALORES = [('Planificación',
  'Estructuración anticipada de las adquisiciones para optimizar los recursos financieros de la organización.'),
 ('Responsabilidad',
  'Cumplimiento eficiente de los compromisos adquiridos con clientes, proveedores y trabajadores.'),
 ('Integridad', 'Actuar con honestidad, ética y transparencia en todas las operaciones de la empresa.'),
 ('Transparencia',
  'Garantizar la trazabilidad y la claridad en los procesos de selección y adjudicación de compras.')]

OBJETIVO_GENERAL_EMPRESA = ('Posicionarse como una empresa líder en el sector petrolero, industrial y de construcción a nivel nacional, '
 'garantizando la provisión oportuna de productos químicos especializados, tratamiento de crudo y maquinaria '
 'pesada, mediante una gestión administrativa, operacional y de procura transparente, eficiente y orientada a la '
 'calidad total.')

OBJETIVOS_ESPECIFICOS_EMPRESA = ['Proporcionar soluciones eficientes y oportunas a las necesidades de sus clientes.',
 'Mantener altos estándares de calidad en los productos y servicios ofrecidos.',
 'Asegurar el abastecimiento continuo y eficiente de insumos mediante una gestión administrativa transparente.']

UBICACION = ('Calle 23 de enero entre calle principal el palomar y calle la paz sector vista al sol, San José de Guanipa Edo. '
 'Anzoátegui.')

POBLACION_TABLA = [('Alta Dirección', 'Gerente General', 0, 1, 1),
 ('Dirección Operativa', 'Gerente de Operaciones', 0, 1, 1),
 ('Control y Avance', 'Gerente / Operaciones Morichal', 1, 1, 2),
 ('Administración (Área de Pasantía)', 'Administración / Asistentes Administrativos', 2, 1, 3),
 ('', 'Control de Avance, Logística y Compras (Procura)', 1, 1, 2),
 ('', 'Operarios, Sup. Patio, Mantenimiento y Logística', 0, 2, 2),
 ('Contratación y Adm. Contratos', 'Gerente / Estimadores, Administradores, Planificadores', 2, 1, 3),
 ('Recursos Humanos', 'Gerente de RRHH-Laborales / Asistentes', 2, 1, 3),
 ('Proyectos y Producción', 'Gerentes de Proyecto, Optimización y Servicios', 1, 2, 3),
 ('', 'Gerente Metalmecánico', 0, 1, 1),
 ('Ingeniería y Campo', 'Ingenieros Residentes / Coordinadores (SIHO-A, Calidad)', 2, 3, 5),
 ('', 'Inspectores (SIHO, Ambiente, Paramédicos, Calidad)', 2, 2, 4),
 ('', 'Supervisor de Obras, Operadores, Chóferes, Soldadores, Obreros', 1, 10, 11),
 ('TOTAL GENERAL', '', 14, 28, 42)]

POBLACION_FUENTE = 'Información suministrada por Lubricantes y Equipos Varyna, C.A. (2026).'

POBLACION = []

ORGANIGRAMA_TEXTO = ('La estructura organizativa de Lubricantes y Equipos Varyna, C.A. es de tipo jerárquico-funcional y está integrada por '
 'la Gerencia General, Gerencia de Operaciones, Gerencia de Control y Avance, Departamento Administrativo, Gerencia de '
 'Contratación y Administración de Contratos, Recursos Humanos, gerencias técnicas y coordinaciones de SIHO-A y Calidad. '
 'A continuación, se presenta el organigrama general de la organización y las unidades vinculadas con el área donde se '
 'desarrollaron las pasantías.')

MOSTRAR_NIVELES_DIAGNOSTICO = True

DESCRIPCION_DEPARTAMENTO = ('El Departamento Administrativo fue el área en la que se desarrollaron las pasantías profesionales. '
 'Dentro de esta unidad se realizan actividades relacionadas con administración, control de documentación, logística y procura. '
 'En lo relativo al proceso de compras, el departamento recibe requerimientos, gestiona solicitudes de cotización, mantiene '
 'comunicación con proveedores, prepara y tramita documentación de compra y realiza seguimiento a las adquisiciones hasta su '
 'correspondiente cierre administrativo. La pasantía se concentró especialmente en estas actividades de procura, lo que permitió '
 'observar el recorrido de las requisiciones, identificar oportunidades de simplificación y formular una propuesta ajustada a '
 'las necesidades operativas del área.')

# ========================================================================
# 5. CAPÍTULO II — DIAGNÓSTICO SITUACIONAL
# ========================================================================
SITUACION_PROBLEMATICA = [{'titulo': 'Nivel macro',
  'parrafos': ['En las organizaciones, los procesos de procura requieren coordinación entre las unidades que '
               'solicitan bienes o servicios, el personal encargado de compras, los responsables de autorización '
               'y los proveedores. Cuando las etapas no están claramente definidas, pueden presentarse '
               'duplicidades, retrasos y dificultades para conocer el estado de una solicitud, por lo que la '
               'simplificación administrativa debe orientarse a ordenar el recorrido documental sin eliminar los '
               'controles necesarios.',
               'Desde la perspectiva administrativa, un procedimiento de compras resulta más controlable cuando '
               'dispone de canales de recepción definidos, formatos uniformes, responsables identificados y '
               'mecanismos de seguimiento. Estos elementos permiten disminuir la dependencia de acuerdos '
               'informales y facilitan que la información necesaria para cada adquisición se encuentre disponible '
               'durante las distintas fases del proceso.']},
 {'titulo': 'Nivel meso',
  'parrafos': ['En empresas vinculadas con actividades petroleras, industriales y de construcción, la '
               'disponibilidad oportuna de materiales e insumos influye directamente en la continuidad de las '
               'operaciones. Por esta razón, el departamento administrativo debe mantener coordinación con las '
               'áreas solicitantes y con los proveedores, procurando que las requisiciones, cotizaciones y '
               'aprobaciones avancen mediante una secuencia comprensible y verificable.',
               'Cuando el proceso de procura depende de formatos diferentes, canales dispersos de recepción o '
               'aprobaciones sin criterios previamente definidos, el personal debe invertir tiempo adicional en '
               'ubicar información, verificar solicitudes y determinar el estado de cada compra. Esta situación '
               'puede trasladar demoras administrativas hacia las actividades operativas que dependen de los '
               'suministros requeridos.']},
 {'titulo': 'Nivel micro',
  'parrafos': ['En el Departamento Administrativo de Lubricantes y Equipos Varyna, C.A., se identificó una '
               'situación desfavorable relacionada con la dispersión del flujo procedimental de la procura. Las '
               'solicitudes de compra no cuentan con un canal único formalizado de recepción y se observaron '
               'oportunidades de mejora en la estandarización de los formatos utilizados para solicitar '
               'cotizaciones, emitir órdenes de compra y efectuar el seguimiento de cada adquisición.',
               'Entre las manifestaciones observadas se encuentran cuellos de botella en las aprobaciones, '
               'dificultad para conocer el estatus de algunas cotizaciones, ausencia de niveles de autorización '
               'claramente definidos por monto y limitada disponibilidad de indicadores que permitan valorar el '
               'desempeño del ciclo de compras. Como consecuencia, se prolongan los tiempos de respuesta, se '
               'reduce la trazabilidad documental y aumenta la carga de seguimiento manual sobre el personal del '
               'área.',
               'La situación descrita evidencia la necesidad de formular una propuesta de simplificación '
               'administrativa que organice el recorrido de las requisiciones, defina responsables, estandarice '
               'documentos y establezca mecanismos de seguimiento compatibles con el control interno del '
               'departamento.']},
 {'titulo': 'Técnica empleada para el diagnóstico',
  'parrafos': ['Para organizar las causas de la problemática se utilizó el diagrama de causa-efecto o diagrama de '
               'Ishikawa, complementado con observación directa del flujo de procura, entrevistas estructuradas '
               'al personal y revisión de expedientes de compras. La técnica permitió agrupar factores asociados '
               'a procedimientos, responsabilidades, documentación y seguimiento, facilitando la identificación '
               'de los puntos que debían atenderse en la propuesta.']}]

INTERROGANTE_TITULO = 'Interrogante orientadora'

INTERROGANTE_PROBLEMA = ('¿Cómo puede formularse una propuesta de simplificación administrativa del proceso de procura en el Departamento '
 'Administrativo de Lubricantes y Equipos Varyna, C.A., que reduzca la dispersión procedimental y fortalezca el '
 'seguimiento de las adquisiciones?')

OBJETIVO_GENERAL = ('Proponer la simplificación administrativa del proceso de procura en el Departamento Administrativo de '
 'Lubricantes y Equipos Varyna, C.A., con la finalidad de agilizar el ciclo de adquisición y fortalecer el '
 'control interno.')

OBJETIVOS_ESPECIFICOS = ['Diagnosticar el proceso actual de procura en el Departamento Administrativo de Lubricantes y Equipos Varyna, '
 'C.A., para conocer el recorrido de las requisiciones y los mecanismos de control utilizados.',
 'Identificar las deficiencias, redundancias y causas que generan retrasos o pérdida de trazabilidad en las fases '
 'de recepción, cotización, aprobación y seguimiento de las adquisiciones.',
 'Formular una propuesta de simplificación administrativa del proceso de procura que integre un flujo definido, '
 'responsables, formatos estandarizados, criterios de autorización y mecanismos de seguimiento.']

PLANIFICACION_DATOS = [('Diagnosticar el proceso actual de procura en el Departamento Administrativo de Lubricantes y Equipos Varyna, '
  'C.A., para conocer el recorrido de las requisiciones y los mecanismos de control utilizados.',
  'Proceso actual de procura y recorrido de las requisiciones.',
  'Observar el ciclo de compras, levantar el flujo existente y aplicar una entrevista estructurada al personal '
  'relacionado con la procura.',
  'Observación directa, entrevista estructurada y revisión documental.',
  'Guía de observación, guía de entrevista, cuaderno de notas y expedientes de compra.'),
 ('Identificar las deficiencias, redundancias y causas que generan retrasos o pérdida de trazabilidad en las '
  'fases de recepción, cotización, aprobación y seguimiento de las adquisiciones.',
  'Deficiencias, redundancias y causas de demora del proceso.',
  'Revisar expedientes históricos, comparar tiempos por fase, identificar cuellos de botella y elaborar el '
  'diagrama de Ishikawa.',
  'Análisis documental, análisis de tiempos y diagrama causa-efecto.',
  'Hojas de registro, expedientes históricos, hoja de cálculo y matriz de causas.'),
 ('Formular una propuesta de simplificación administrativa del proceso de procura que integre un flujo definido, '
  'responsables, formatos estandarizados, criterios de autorización y mecanismos de seguimiento.',
  'Propuesta de simplificación administrativa de la procura.',
  'Diseñar el flujo simplificado, formatos de solicitud y orden de compra, matriz de autorización por monto e '
  'indicadores básicos de seguimiento; validar la propuesta con el tutor industrial.',
  'Diseño procedimental, estandarización de formatos y validación técnica.',
  'Procesador de textos, hoja de cálculo, herramientas de diagramación y formato de validación.')]

CRONOGRAMA_DATOS = [('Inducción y reconocimiento del Departamento Administrativo y del área de procura.',
  [True, False, False, False, False, False, False, False, False, False]),
 ('Levantamiento del flujo actual de requisiciones y compras.',
  [True, True, False, False, False, False, False, False, False, False]),
 ('Aplicación de entrevista estructurada y revisión de expedientes de compras.',
  [False, False, True, True, False, False, False, False, False, False]),
 ('Análisis de tiempos, cuellos de botella y elaboración del diagrama de Ishikawa.',
  [False, False, False, True, True, False, False, False, False, False]),
 ('Diseño del flujo simplificado y definición de responsables y puntos de control.',
  [False, False, False, False, False, True, False, False, False, False]),
 ('Diseño de formatos, matriz de autorización por monto e indicadores de seguimiento.',
  [False, False, False, False, False, False, True, False, False, False]),
 ('Redacción de la propuesta de simplificación administrativa.',
  [False, False, False, False, False, False, True, True, False, False]),
 ('Validación de la propuesta e incorporación de observaciones.',
  [False, False, False, False, False, False, False, False, True, False]),
 ('Presentación de la propuesta y consolidación del informe de pasantías.',
  [False, False, False, False, False, False, False, False, False, True]),
 ('Apoyo operativo en requisiciones, cotizaciones, proveedores y archivo de compras.',
  [False, True, True, True, True, True, True, True, True, False])]

# ========================================================================
# 6. CAPÍTULO III — MARCO TEÓRICO Y LEGAL
# ========================================================================
BASES_TEORICAS_TITULOS = [
    'Procura y Gestión de Compras',
    'Proceso Administrativo',
    'Control Interno en los Procesos de Compras',
    'Simplificación Administrativa de Procesos',
]
BASES_LEGALES_TITULOS = [
    'Base Legal: Constitución de la República Bolivariana de Venezuela — Artículo 112',
    'Base Legal: Código de Comercio — Artículo 32',
]

BASES_TEORICAS = [{'titulo': 'Procura y Gestión de Compras',
  'categoria': 'teorica',
  'parrafos': ['La procura se define como el conjunto de actividades orientadas a la adquisición de bienes, '
               'materiales e insumos necesarios para el funcionamiento continuo de una organización. Monterroso '
               '(2002) establece que la gestión de abastecimiento eficiente no se limita a la ejecución de '
               'compras, sino que abarca la planificación de necesidades, la selección de proveedores, la '
               'negociación de condiciones y el control del cumplimiento de los requerimientos en tiempo, calidad '
               'y costo.',
               'Lo anterior cobra especial relevancia en el contexto de Lubricantes y Equipos Varyna, C.A., donde '
               'la procura constituye una función crítica para sostener las operaciones industriales y de campo. '
               'Durante el diagnóstico realizado, se pudo constatar que el departamento administrativo no cuenta '
               'con un canal formalizado de recepción de requisiciones, lo que impide que el proceso de '
               'abastecimiento se desarrolle de forma planificada y controlada tal como lo exige la teoría. En '
               'criterio de quien suscribe, esta ausencia de estructura procedimental es la causa raíz de los '
               'retrasos identificados, por encima incluso de factores humanos o tecnológicos.',
               'Comprender la procura desde esta perspectiva teórica es el punto de partida indispensable para '
               'cualquier propuesta de mejora, pues permite identificar con precisión en cuáles fases del ciclo '
               'se concentran las ineficiencias. Para ello, resulta igualmente necesario examinar el marco '
               'administrativo general que debe regir la gestión de cualquier proceso organizacional, tal como se '
               'desarrolla en el apartado siguiente.'],
  'cita_larga': {'texto': 'La gestión de compras y abastecimiento comprende un conjunto de actividades que '
                          'permiten identificar las necesidades de materiales e insumos de la organización, '
                          'seleccionar adecuadamente a los proveedores, negociar las condiciones de adquisición '
                          'más convenientes y asegurar que los bienes requeridos lleguen en las cantidades '
                          'correctas, en el momento oportuno y al menor costo posible, contribuyendo directamente '
                          'a la eficiencia operativa de la empresa.',
                 'autor': '(Monterroso, 2002, p. 3)'},
  'posicion_autor': '',
  'post_cita': ''},
 {'titulo': 'Proceso Administrativo',
  'categoria': 'teorica',
  'parrafos': ['El proceso administrativo constituye el marco conceptual fundamental que rige el funcionamiento '
               'de las organizaciones modernas. Chiavenato (2006) lo describe como el conjunto secuencial e '
               'interrelacionado de funciones de planificación, organización, dirección y control, orientadas al '
               'logro eficiente de los objetivos organizacionales mediante el uso racional de los recursos '
               'disponibles.',
               'Aplicado al contexto de la procura, el proceso administrativo provee la estructura metodológica '
               'necesaria para formalizar cada etapa del ciclo de compras. La planificación define las '
               'necesidades y tiempos de adquisición; la organización asigna responsabilidades claras a cada '
               'actor del proceso; la dirección asegura la ejecución coordinada de las actividades; y el control '
               'verifica el cumplimiento de los procedimientos y detecta desviaciones que requieren corrección.',
               'Durante la observación directa realizada en Lubricantes y Equipos Varyna, C.A., se evidenció que '
               'ninguna de estas cuatro funciones se ejecuta de manera formal dentro del ciclo de compras. Las '
               'requisiciones se reciben sin planificación previa, las responsabilidades no están escritas ni '
               'asignadas con claridad, y no existe un mecanismo de control que permita detectar en qué fase se '
               'detiene cada expediente. Desde la perspectiva de quien elabora este trabajo, la ausencia del '
               'proceso administrativo como eje rector es lo que convierte un procedimiento que debería ser '
               'simple en una secuencia compleja y propensa a errores. La propuesta de simplificación '
               'desarrollada en los capítulos siguientes busca precisamente instaurar estas cuatro funciones de '
               'forma explícita dentro del nuevo flujo de procura. Para que dicho control sea efectivo, es '
               'necesario además comprender los mecanismos de control interno aplicables específicamente al área '
               'de compras, como se expone a continuación.'],
  'cita_larga': None,
  'posicion_autor': '',
  'post_cita': ''},
 {'titulo': 'Control Interno en los Procesos de Compras',
  'categoria': 'teorica',
  'parrafos': ['El control interno se define como el proceso diseñado e implementado por la dirección de una '
               'organización para proporcionar una seguridad razonable sobre la consecución de los objetivos en '
               'las categorías de eficiencia operativa, confiabilidad de la información financiera y cumplimiento '
               'de las normas aplicables. Mantilla (2005) señala que un sistema de control interno robusto en el '
               'área de compras minimiza los riesgos de fraude, duplicidad de pagos y adquisiciones no '
               'autorizadas.',
               'En el proceso de procura de Lubricantes y Equipos Varyna, C.A., el fortalecimiento del control '
               'interno implica la definición de niveles de autorización por monto de compra, la implementación '
               'de formularios estandarizados de solicitud y la trazabilidad documental de cada expediente desde '
               'la requisición hasta la orden de compra cerrada. Estas medidas reducen la discrecionalidad en las '
               'decisiones de adquisición y aumentan la transparencia del proceso.',
               'A juicio de quien suscribe, el control interno no debe entenderse como una carga burocrática '
               'adicional, sino como la garantía de que cada paso del proceso de compras tiene un propósito '
               'definido y un responsable identificable. En Lubricantes y Equipos Varyna, C.A., la inexistencia '
               'de niveles de autorización formales ha generado que decisiones de adquisición recaigan de manera '
               'discrecional sobre el personal disponible en el momento, sin criterios objetivos ni registros '
               'verificables. Incorporar mecanismos de control interno dentro del nuevo procedimiento '
               'simplificado no agrega complejidad al proceso, sino que le otorga la transparencia y trazabilidad '
               'que actualmente le faltan. Este enfoque de control se articula directamente con la noción de '
               'simplificación administrativa que fundamenta la propuesta, concepto que se desarrolla en el '
               'siguiente apartado.'],
  'cita_larga': None,
  'posicion_autor': '',
  'post_cita': ''},
 {'titulo': 'Simplificación Administrativa de Procesos',
  'categoria': 'teorica',
  'parrafos': ['La simplificación administrativa consiste en la revisión sistemática y el rediseño de los '
               'procedimientos organizacionales con el propósito de eliminar pasos innecesarios, reducir la '
               'burocracia interna y facilitar la ejecución ágil de las operaciones. Según Harrington (1993), un '
               'proceso simplificado debe ser comprensible para todos los actores involucrados, ejecutable con el '
               'menor número de pasos posible y orientado a resultados medibles y verificables.',
               'En el ámbito de la administración de compras, la simplificación procedimental se traduce en la '
               'reducción de los ciclos de aprobación, la unificación de los formatos de cotización y la '
               'clarificación de los roles y responsabilidades de cada actor. El resultado esperado es una '
               'disminución verificable de los tiempos de respuesta en la adquisición de insumos y una mayor '
               'capacidad de la organización para atender sus necesidades de abastecimiento de forma oportuna y '
               'transparente.',
               'Esta definición describe con precisión la situación identificada en Lubricantes y Equipos Varyna, '
               'C.A.: un proceso que ha crecido en pasos y actores sin que todos esos añadidos respondan a una '
               'secuencia formalmente definida. Quien elabora este trabajo considera que la simplificación no '
               'implica eliminar controles, sino reducir redundancias y clarificar responsabilidades. La propuesta '
               'formulada durante las pasantías parte de este principio y organiza los pasos necesarios para que '
               'una requisición avance de manera comprensible desde su recepción hasta el cierre de la orden de '
               'compra, manteniendo responsables, criterios de autorización y mecanismos de seguimiento que '
               'favorezcan el control administrativo del proceso.'],
  'cita_larga': None,
  'posicion_autor': '',
  'post_cita': ''},
 {'titulo': 'Base Legal: Constitución de la República Bolivariana de Venezuela — Artículo 112',
  'categoria': 'legal',
  'parrafos': ['Como marco general de la actividad económica privada, la Constitución reconoce la iniciativa '
               'empresarial dentro de los límites establecidos por el ordenamiento jurídico.'],
  'cita_larga': {'texto': 'Todas las personas pueden dedicarse libremente a la actividad económica de su '
                          'preferencia, sin más limitaciones que las previstas en esta Constitución y las que '
                          'establezcan las leyes, por razones de desarrollo humano, seguridad, sanidad, '
                          'protección del ambiente u otras de interés social. El Estado promoverá la iniciativa '
                          'privada, garantizando la creación y justa distribución de la riqueza, así como la '
                          'producción de bienes y servicios que satisfagan las necesidades de la población, la '
                          'libertad de trabajo, empresa, comercio, industria, sin perjuicio de su facultad para '
                          'dictar medidas para planificar, racionalizar y regular la economía e impulsar el '
                          'desarrollo integral del país.',
                 'autor': '(Constitución de la República Bolivariana de Venezuela, 1999, art. 112)'},
  'post_cita': '',
  'posicion_autor': 'El aporte de este artículo al informe es de carácter general: reconoce el ejercicio de la '
                    'actividad empresarial y permite ubicar la propuesta dentro de la necesidad de organizar '
                    'racionalmente los procesos internos de una empresa privada. No establece un procedimiento '
                    'específico de procura, por lo que su función es servir como fundamento constitucional amplio '
                    'y no como regla operativa de compras.'},
 {'titulo': 'Base Legal: Código de Comercio — Artículo 32',
  'categoria': 'legal',
  'parrafos': ['El Código de Comercio establece obligaciones vinculadas con el orden y claridad de los registros '
               'de los comerciantes, aspecto que guarda relación con la necesidad de mantener información '
               'organizada y verificable en los procesos administrativos.'],
  'cita_larga': {'texto': 'Todo comerciante debe llevar en idioma castellano su contabilidad, la cual '
                          'comprenderá, obligatoriamente, el libro Diario, el libro Mayor y el de Inventarios. '
                          'Podrá llevar, además, todos los libros auxiliares que estimara conveniente para el '
                          'mayor orden y claridad de sus operaciones.',
                 'autor': '(Código de Comercio, 1955, art. 32)'},
  'post_cita': '',
  'posicion_autor': 'La relación con la propuesta se encuentra en el principio de orden y claridad de las '
                    'operaciones mercantiles. Los formatos y mecanismos de seguimiento diseñados para la procura '
                    'no sustituyen los libros contables exigidos por la ley, pero complementan el control '
                    'administrativo al organizar la documentación que antecede y acompaña las compras de la '
                    'empresa.'}]

POST_CITA_TEXTO = ''

# ========================================================================
# 7. CAPÍTULO IV — ACTIVIDADES REALIZADAS
# ========================================================================
ACTIVIDADES_DESCRIPCION = ('Durante las diez (10) semanas de práctica profesional se desarrollaron actividades operativas de apoyo a la '
 'procura y actividades de diagnóstico, análisis y formulación de la propuesta de simplificación administrativa:')

ACTIVIDADES_LISTA = [{'semana': 1,
  'operativa': 'Inducción institucional, recorrido por las instalaciones, presentación ante el equipo del '
               'Departamento Administrativo y familiarización con los procedimientos generales de la empresa y '
               'del área de procura.',
  'investigacion': 'Observación directa del flujo de requisiciones y registro de las primeras situaciones '
                   'relacionadas con la recepción, seguimiento y control de las solicitudes de compra.'},
 {'semana': 2,
  'operativa': 'Apoyo en la recepción, clasificación y registro de solicitudes de compra, además de la '
               'familiarización con los expedientes y mecanismos de seguimiento de cotizaciones del departamento.',
  'investigacion': 'Levantamiento del flujo secuencial del proceso de procura mediante observación directa y '
                   'conversaciones de reconocimiento con el personal encargado.'},
 {'semana': 3,
  'operativa': 'Colaboración en la tramitación de requisiciones, comunicación con proveedores y actualización del '
               'registro de cotizaciones en proceso.',
  'investigacion': 'Aplicación de una guía de entrevista estructurada al personal relacionado con compras y '
                   'administración para identificar demoras, duplicidades y dificultades de seguimiento.'},
 {'semana': 4,
  'operativa': 'Seguimiento de órdenes de compra abiertas, verificación del estatus de cotizaciones pendientes y '
               'actualización del registro de proveedores activos.',
  'investigacion': 'Revisión de expedientes históricos y análisis de tiempos de respuesta por fase con el '
                   'propósito de determinar las etapas donde se concentran los mayores retrasos.'},
 {'semana': 5,
  'operativa': 'Tramitación de solicitudes de compra, apoyo en cuadros comparativos de cotizaciones y '
               'actualización de información de proveedores.',
  'investigacion': 'Elaboración del diagrama de Ishikawa y jerarquización de las causas asociadas con retrasos, '
                   'redundancias, falta de estandarización y dificultades de trazabilidad en la procura.'},
 {'semana': 6,
  'operativa': 'Seguimiento de cotizaciones pendientes de aprobación y actualización de los expedientes de '
               'compras activos del período.',
  'investigacion': 'Diseño del nuevo flujo simplificado del proceso de procura, definiendo etapas, responsables, '
                   'puntos de control y tiempos de referencia para el seguimiento administrativo.'},
 {'semana': 7,
  'operativa': 'Apoyo en el procesamiento de requisiciones y verificación de información necesaria para compras '
               'en trámite.',
  'investigacion': 'Diseño de los formatos estandarizados de solicitud de cotización y orden de compra, '
                   'elaboración de la matriz de autorización por monto y definición de indicadores básicos para '
                   'el seguimiento del proceso.'},
 {'semana': 8,
  'operativa': 'Seguimiento de órdenes en proceso y actualización de registros de proveedores y expedientes de '
               'adquisiciones.',
  'investigacion': 'Redacción de la propuesta de simplificación administrativa integrando el flujo diseñado, los '
                   'formatos, la matriz de autorización y los mecanismos de seguimiento.'},
 {'semana': 9,
  'operativa': 'Apoyo en el cierre administrativo del ciclo de compras y organización de las órdenes de compra '
               'gestionadas durante el período.',
  'investigacion': 'Presentación de la propuesta al tutor industrial, registro de observaciones e incorporación '
                   'de ajustes al documento final.'},
 {'semana': 10,
  'operativa': 'Presentación formal de la propuesta ante la gerencia del área y gestión de los recaudos '
               'institucionales correspondientes al cierre de las pasantías.',
  'investigacion': 'Consolidación del informe de pasantías, revisión de la normativa de presentación e '
                   'incorporación de los anexos y correcciones finales antes de la entrega institucional.'}]

# ========================================================================
# 8. CAPÍTULO V — CONCLUSIONES Y RECOMENDACIONES
# ========================================================================
CONCLUSIONES = ['Se diagnosticó que el proceso de procura presenta un recorrido administrativo susceptible de simplificación, '
 'debido a la ausencia de un canal único de recepción de requisiciones y a la dispersión de algunos mecanismos de '
 'seguimiento utilizados durante las fases de compra.',
 'Se identificaron como principales factores de demora la falta de formatos uniformes, la limitada definición de '
 'criterios de autorización, el seguimiento manual del estatus de cotizaciones y la inexistencia de indicadores '
 'sencillos que permitan valorar el comportamiento del ciclo de adquisición.',
 'Se formuló una propuesta de simplificación administrativa que integra un flujo de trabajo con responsables '
 'definidos, formatos estandarizados, una matriz de autorización por monto e indicadores de seguimiento, '
 'orientados a mejorar la trazabilidad y facilitar el control interno del proceso de procura.']

RECOMENDACIONES = ['Implementar la propuesta de manera gradual, iniciando con la formalización del canal de recepción de '
 'requisiciones y la utilización uniforme de los formatos diseñados.',
 'Socializar el flujo simplificado, los responsables y los criterios de autorización con el personal involucrado '
 'en la procura antes de su aplicación general.',
 'Registrar mensualmente indicadores básicos, como tiempo promedio del ciclo de compra, solicitudes pendientes y '
 'requisiciones tramitadas dentro del plazo definido, para valorar los resultados de la simplificación.',
 'Revisar periódicamente el procedimiento y los formatos con el personal del Departamento Administrativo, '
 'incorporando ajustes cuando cambien las necesidades operativas de la empresa.']

# ========================================================================
# 9. REFERENCIAS Y ANEXOS
# ========================================================================
REFERENCIAS_LISTA = [ 'Asamblea Nacional Constituyente. (1999). Constitución de la República Bolivariana de Venezuela. Gaceta Oficial '
 'de la República Bolivariana de Venezuela.',
 'Chiavenato, I. (2006). Introducción a la teoría general de la administración (7ma ed.). McGraw-Hill, México.',
 'Congreso de la República de Venezuela. (1955). Código de Comercio. Gaceta Oficial Extraordinaria N.º 475.',
 'Harrington, H. J. (1993). Mejoramiento de los procesos de la empresa. McGraw-Hill, Colombia.',
 'Mantilla, S. (2005). Control interno: Informe COSO (4ta ed.). Ecoe Ediciones, Colombia.',
 'Monterroso, E. (2002). El proceso de abastecimiento: El aprovisionamiento. Universidad Nacional de Luján, '
 'Argentina.']

ANEXOS_LISTA = [
    ('ANEXO A', 'Diagrama de Ishikawa de las causas asociadas a las demoras del proceso de procura', '01_ishikawa_demoras_procura.png', {'width_cm': 13.0, 'height_cm': 13.0}, ['Fuente: Elaboración propia (2026).']),
    ('ANEXO B', 'Flujograma AS-IS del proceso actual de procura', '02_flujo_as_is_procura.png', {'width_cm': 10.0, 'height_cm': 15.0}, ['Fuente: Elaboración propia (2026).']),
    ('ANEXO C', 'Flujograma TO-BE del proceso simplificado propuesto', '03_flujo_to_be_procura.png', {'width_cm': 10.0, 'height_cm': 15.0}, ['Fuente: Elaboración propia (2026).']),
    ('ANEXO D', 'Swimlane del proceso propuesto de procura', '04_swimlane_procura.png', {'width_cm': 14.0, 'height_cm': 13.0}, ['Fuente: Elaboración propia (2026).']),
    ('ANEXO E', 'SIPOC del proceso de procura', '05_sipoc_procura.png', {'width_cm': 13.0, 'height_cm': 14.0}, ['Fuente: Elaboración propia (2026).']),
    ('ANEXO F', 'Matriz RACI propuesta del proceso de procura', '06_matriz_raci_propuesta.png', {'width_cm': 14.0, 'height_cm': 5.0}, ['Fuente: Elaboración propia (2026).']),
    ('ANEXO G', 'Diagrama de Ishikawa definitivo de las causas asociadas a las demoras y pérdida de trazabilidad del proceso de procura', 'ishikawa_keidy_procura.png', {'width_cm': 14.0, 'height_cm': 6.0}, ['Fuente: Elaboración propia (2026).'])
]
