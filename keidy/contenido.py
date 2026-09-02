# -*- coding: utf-8 -*-
# Archivo revisado para informe de pasantías regulares IUTECP.

# ========================================================================
# 1. RUTAS, IMÁGENES Y CUADROS
# ========================================================================
CARPETA_IMAGENES = 'imagenes'

FIRMA_TUTOR_INDUSTRIAL = 'firma_tutor_keidy.png'
FIRMA_TUTOR_ACADEMICO = 'firma_tutor_academico.png'
TEXTO_FECHA_APROBACION_TUTOR_INDUSTRIAL = 'a los 14 días del mes de agosto de 2026'


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
        'pagina': '4',
        'fuente': 'Google Maps (2026).'
    },
    {
        'numero': 3,
        'archivo': '2.png',
        'tras': 'estructura',
        'titulo': 'Gráfico 3. Organigrama estructural y niveles jerárquicos de la organización.',
        'ancho_cm': 12,
        'lista': 'Organigrama estructural y niveles jerárquicos de la organización',
        'pagina': '5',
        'fuente': 'Lubricantes y Equipos Varyna, C.A. (2026).'
    },
    {
        'numero': 4,
        'archivo': 'ishikawa_keidy_procura.png',
        'tras': 'diagnostico_tecnica',
        'titulo': 'Gráfico 4. Diagrama de Ishikawa de las causas asociadas a las demoras y pérdida de trazabilidad del proceso de procura.',
        'ancho_cm': 12.5,
        'lista': 'Diagrama de Ishikawa de las causas asociadas a las demoras y pérdida de trazabilidad del proceso de procura',
        'pagina': '',
        'fuente': 'Guzmán K. (2026).'
    }
]

FIGURAS = []

PLANIFICACION_INTRO_TEXTO = ('La planificación relaciona los tres objetivos específicos con las actividades, técnicas e instrumentos '
 'necesarios para diagnosticar el proceso, identificar sus deficiencias y formular la propuesta de simplificación '
 'administrativa:')

CRONOGRAMA_INTRO_TEXTO = ('El cronograma distribuye las actividades operativas y de análisis durante las diez (10) semanas de pasantía, '
 'manteniendo correspondencia con los objetivos específicos:')

CUADRO_POBLACION_TITULO = 'Cuadro 1. Población de los trabajadores de la empresa.'
CUADRO_PLANIFICACION_TITULO = 'Cuadro 2. Planificación integral de objetivos específicos.'
CUADRO_CRONOGRAMA_TITULO = 'Cuadro 3. Cronograma de actividades de la pasantía.'

# Configuración particular indicada por la tutora académica (06/08/2026).
MOSTRAR_NIVELES_DIAGNOSTICO = True
ETIQUETA_ACTIVIDAD_ANALISIS = 'Actividad de análisis'
CUADRO_PLANIFICACION_FUENTE = 'Guzmán K. (2026).'
CUADRO_CRONOGRAMA_FUENTE = 'Guzmán K. (2026).'

FORMATO_APROBACION_DESTACADO = True
ESTRUCTURA_ORGANIZATIVA_TITULO = 'Estructura organizativa de la empresa (Organigrama)'
CRONOGRAMA_SECCION_TITULO = 'CRONOGRAMA DE ACTIVIDADES (DIAGRAMA DE GANTT)'

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
 'crecientes demandas operativas e industriales del país. A lo largo de quince (15) años de '
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
SITUACION_PROBLEMATICA = [{'parrafos': ['La identificación de la situación problemática permite analizar las condiciones que afectan el '
                                        'proceso administrativo de procura en el Departamento Administrativo de Lubricantes y Equipos '
                                        'Varyna, C.A. Para comprender la problemática de manera progresiva, se consideran aspectos '
                                        'generales relacionados con la gestión de compras en las organizaciones, las exigencias propias '
                                        'del sector industrial y, finalmente, las condiciones observadas directamente en la empresa '
                                        'durante el período de pasantías.']},
 {'titulo': 'Nivel macro',
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
  {'parrafos': ['El recorrido observado del proceso se sintetiza en el flujograma AS-IS incorporado como Anexo A, '
               'donde se muestran las etapas de recepción, cotización, aprobación, orden de compra, seguimiento y cierre, '
               'junto con los principales puntos críticos identificados.',
               'Para organizar las causas de la problemática se utilizó el diagrama de causa-efecto o diagrama de '
               'Ishikawa, complementado con observación directa del flujo de procura, entrevistas estructuradas '
               'al personal y revisión de expedientes de compras. La técnica permitió agrupar factores asociados '
               'a procedimientos, responsabilidades, documentación y seguimiento, facilitando la identificación '
                'de los puntos que debían atenderse en la propuesta. La representación gráfica de esta técnica se presenta a continuación.']}]

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
# 6. CAPÍTULO III — MARCO TEÓRICO
# ========================================================================
CONCEPTOS_DISCIPLINARES_TITULO = 'Conceptos disciplinares'
BASES_LEGALES_SECCION_TITULO = 'Bases legales'

BASES_TEORICAS_TITULOS = [
    'Procura y Gestión de Compras',
    'Proceso Administrativo',
    'Control Interno en los Procesos de Compras',
    'Simplificación Administrativa de Procesos',
    'Gestión de Proveedores',
    'Trazabilidad Documental en la Procura',
    'Estandarización de Procedimientos',
    'Indicadores de Gestión Aplicados a Compras',
]

BASES_LEGALES_TITULOS = [
    'Constitución de la República Bolivariana de Venezuela',
    'Código de Comercio',
]

BASES_TEORICAS = [
 {'titulo': 'Procura y Gestión de Compras',
  'categoria': 'teorica',
  'parrafos': [
      'La procura se define como el conjunto de actividades orientadas a la adquisición de bienes, materiales e insumos necesarios para el funcionamiento continuo de una organización. Monterroso (2002) explica que la gestión de abastecimiento no se limita al acto de comprar, sino que comprende la identificación de necesidades, la búsqueda y evaluación de proveedores, la negociación de condiciones y el seguimiento del cumplimiento en tiempo, calidad y costo.',
      'Dentro de un proceso administrativo, la procura conecta las necesidades internas de la organización con el mercado proveedor. Por ello, una gestión de compras ordenada requiere que cada requisición sea recibida, revisada, cotizada, autorizada, procesada y cerrada mediante una secuencia conocida por quienes participan en ella.',
      'En Lubricantes y Equipos Varyna, C.A., la procura constituye una función de apoyo relevante para la continuidad de las operaciones industriales y de campo. La ausencia de un canal formalizado de recepción y seguimiento de requisiciones justifica analizar el proceso desde una perspectiva administrativa que permita identificar oportunidades de simplificación sin debilitar los controles necesarios.'
  ],
  'cita_larga': {'texto': 'La gestión de compras y abastecimiento comprende un conjunto de actividades que permiten identificar las necesidades de materiales e insumos de la organización, seleccionar adecuadamente a los proveedores, negociar las condiciones de adquisición más convenientes y asegurar que los bienes requeridos lleguen en las cantidades correctas, en el momento oportuno y al menor costo posible, contribuyendo directamente a la eficiencia operativa de la empresa.',
                 'autor': '(Monterroso, 2002, p. 3)'},
  'posicion_autor': '',
  'post_cita': ''},

 {'titulo': 'Proceso Administrativo',
  'categoria': 'teorica',
  'parrafos': [
      'El proceso administrativo constituye un marco conceptual para coordinar los recursos y las actividades de una organización. Chiavenato (2006) lo desarrolla a partir de las funciones de planificación, organización, dirección y control, las cuales se relacionan entre sí y orientan el cumplimiento de los objetivos institucionales.',
      'Aplicado a la procura, la planificación permite prever requerimientos y tiempos de adquisición; la organización distribuye responsabilidades; la dirección coordina la ejecución de las actividades; y el control verifica que las requisiciones, cotizaciones, autorizaciones y órdenes de compra avancen conforme a criterios previamente definidos.',
      'La propuesta de simplificación formulada en este informe se vincula con el proceso administrativo porque procura ordenar el recorrido de las solicitudes de compra, definir responsables y establecer mecanismos de seguimiento. De esta manera, la reducción de pasos innecesarios se combina con una estructura que permite conservar control sobre cada etapa.'
  ],
  'cita_larga': None,
  'posicion_autor': '',
  'post_cita': ''},

 {'titulo': 'Control Interno en los Procesos de Compras',
  'categoria': 'teorica',
  'parrafos': [
      'El control interno comprende políticas, procedimientos y actividades orientadas a proporcionar seguridad razonable sobre la eficiencia de las operaciones, la confiabilidad de la información y el cumplimiento de las disposiciones aplicables. Mantilla (2005) destaca que el control debe formar parte de los procesos y no funcionar como una actividad aislada.',
      'En el área de compras, el control interno se relaciona con la autorización de las adquisiciones, la existencia de soportes documentales, la separación de responsabilidades, la verificación de condiciones y el seguimiento de las operaciones. Estos elementos reducen la posibilidad de omisiones, duplicidades y decisiones sin respaldo suficiente.',
      'Para el proceso de procura analizado, la simplificación propuesta no supone eliminar controles, sino organizarlos dentro de un flujo más claro. La definición de responsables, formatos uniformes y criterios de autorización permite que cada solicitud pueda ser revisada y seguida durante su recorrido administrativo.'
  ],
  'cita_larga': None,
  'posicion_autor': '',
  'post_cita': ''},

 {'titulo': 'Simplificación Administrativa de Procesos',
  'categoria': 'teorica',
  'parrafos': [
      'La simplificación administrativa consiste en revisar un procedimiento para identificar actividades redundantes, demoras, duplicidades y pasos que no aportan valor al resultado esperado. Harrington (1993) plantea el mejoramiento de procesos como una revisión sistemática destinada a hacerlos más efectivos, eficientes y adaptables.',
      'En los procesos de compras, simplificar implica procurar que las requisiciones recorran una secuencia comprensible, con documentos definidos, responsables identificados y controles ubicados en puntos pertinentes. La simplificación no debe confundirse con la eliminación indiscriminada de etapas, ya que un proceso puede ser más ágil y mantener las verificaciones necesarias.',
      'Esta perspectiva se relaciona directamente con el título del informe, debido a que la propuesta busca ordenar el proceso de procura de Lubricantes y Equipos Varyna, C.A., reducir la dispersión procedimental y facilitar el seguimiento de cada adquisición desde la solicitud hasta su cierre administrativo.'
  ],
  'cita_larga': None,
  'posicion_autor': '',
  'post_cita': ''},

 {'titulo': 'Gestión de Proveedores',
  'categoria': 'teorica',
  'parrafos': [
      'La gestión de proveedores forma parte del proceso de abastecimiento porque permite identificar fuentes de suministro, solicitar cotizaciones, comparar condiciones y mantener información útil para futuras adquisiciones. Monterroso (2002) relaciona la gestión de abastecimiento con la selección de proveedores y con la capacidad de asegurar materiales e insumos en condiciones convenientes para la organización.',
      'Una gestión ordenada de proveedores requiere conservar información actualizada sobre ofertas, tiempos de respuesta, condiciones comerciales y cumplimiento de los requerimientos. Esto facilita la comparación de alternativas y reduce la dependencia de búsquedas improvisadas cada vez que surge una necesidad de compra.',
      'En el proceso estudiado, la comunicación con proveedores y el seguimiento de cotizaciones constituyen actividades recurrentes. Por ello, la propuesta de simplificación debe favorecer registros consistentes que permitan conocer qué proveedor fue consultado, qué condiciones ofreció y cuál es el estado de cada cotización.'
  ],
  'cita_larga': None,
  'posicion_autor': '',
  'post_cita': ''},

 {'titulo': 'Trazabilidad Documental en la Procura',
  'categoria': 'teorica',
  'parrafos': [
      'La trazabilidad documental puede entenderse como la posibilidad de reconstruir el recorrido de una operación mediante registros y evidencias que permitan conocer su origen, estado, responsables y resultado. En un proceso de procura, esta capacidad depende de que requisiciones, cotizaciones, autorizaciones y órdenes de compra mantengan una relación identificable durante todo el ciclo.',
      'Desde la perspectiva del control interno desarrollada por Mantilla (2005), la documentación y la disponibilidad de información confiable respaldan la supervisión de las operaciones. Cuando los soportes están dispersos o el estatus de una solicitud depende únicamente del conocimiento informal del personal, aumenta la dificultad para verificar oportunamente el proceso.',
      'La trazabilidad es un elemento central del diagnóstico de este informe, debido a que una de las situaciones observadas fue la dificultad para conocer con rapidez el estado de algunas adquisiciones. La estandarización de registros y la definición de responsables contribuyen a que el recorrido de cada solicitud pueda ser consultado y verificado.'
  ],
  'cita_larga': None,
  'posicion_autor': '',
  'post_cita': ''},

 {'titulo': 'Estandarización de Procedimientos',
  'categoria': 'teorica',
  'parrafos': [
      'La estandarización de procedimientos consiste en definir una forma común y documentada de ejecutar actividades que se repiten dentro de una organización. Harrington (1993) vincula el mejoramiento de procesos con la necesidad de comprender, documentar y controlar las actividades para reducir variaciones que afecten los resultados.',
      'En la procura, la utilización de formatos uniformes para requisiciones, solicitudes de cotización y órdenes de compra facilita que los participantes dispongan de la misma información básica. Asimismo, una secuencia documentada permite establecer qué actividad corresponde a cada responsable y qué condición debe cumplirse antes de avanzar a la fase siguiente.',
      'La propuesta desarrollada para Lubricantes y Equipos Varyna, C.A. incorpora este principio mediante formatos estandarizados, responsables definidos y criterios de autorización. La finalidad es disminuir la dispersión procedimental y facilitar que el personal pueda aplicar el proceso de manera uniforme.'
  ],
  'cita_larga': None,
  'posicion_autor': '',
  'post_cita': ''},

 {'titulo': 'Indicadores de Gestión Aplicados a Compras',
  'categoria': 'teorica',
  'parrafos': [
      'Los indicadores de gestión permiten observar el comportamiento de un proceso mediante datos que facilitan su seguimiento y evaluación. Dentro del proceso administrativo, Chiavenato (2006) relaciona la función de control con la comparación de los resultados obtenidos frente a criterios que permitan identificar desviaciones y aplicar acciones correctivas.',
      'En un proceso de compras pueden emplearse indicadores sencillos vinculados con el tiempo del ciclo de adquisición, el número de solicitudes pendientes, la cantidad de requisiciones procesadas y el cumplimiento de los plazos definidos. Su utilidad depende de que los datos sean registrados de manera consistente y puedan compararse a lo largo del tiempo.',
      'La incorporación de indicadores básicos en la propuesta permite que la simplificación administrativa no se limite a modificar un flujo, sino que pueda ser evaluada después de su aplicación. De esta manera, la empresa podrá identificar si los cambios contribuyen efectivamente a reducir demoras y fortalecer el seguimiento de las adquisiciones.'
  ],
  'cita_larga': None,
  'posicion_autor': '',
  'post_cita': ''}
]

BASES_LEGALES = [
 {
  'norma': 'Constitución de la República Bolivariana de Venezuela',
  'articulo': 'Artículo 112',
  'texto': 'Todas las personas pueden dedicarse libremente a la actividad económica de su preferencia, sin más limitaciones que las previstas en esta Constitución y las que establezcan las leyes, por razones de desarrollo humano, seguridad, sanidad, protección del ambiente u otras de interés social. El Estado promoverá la iniciativa privada, garantizando la creación y justa distribución de la riqueza, así como la producción de bienes y servicios que satisfagan las necesidades de la población, la libertad de trabajo, empresa, comercio, industria, sin perjuicio de su facultad para dictar medidas para planificar, racionalizar y regular la economía e impulsar el desarrollo integral del país.',
  'referencia': '(Asamblea Nacional Constituyente, 1999)',
  'analisis': 'El artículo reconoce la libertad para desarrollar actividades económicas dentro del marco constitucional y legal, al mismo tiempo que atribuye al Estado facultades de regulación y planificación. Desde la perspectiva administrativa, su contenido evidencia que la actividad empresarial debe desarrollarse de manera organizada y compatible con las disposiciones que regulan la operación económica.',
  'aporte': 'Su aporte al informe es servir como fundamento constitucional general para la actividad de Lubricantes y Equipos Varyna, C.A. La propuesta de simplificación administrativa se desarrolla dentro de una empresa privada que ejerce actividad económica y requiere organizar racionalmente sus procesos internos. El artículo no establece un procedimiento específico de procura, por lo que su relación con el trabajo es de carácter general.'
 },
 {
  'norma': 'Código de Comercio',
  'articulo': 'Artículo 32',
  'texto': 'Todo comerciante debe llevar en idioma castellano su contabilidad, la cual comprenderá, obligatoriamente, el libro Diario, el libro Mayor y el de Inventarios. Podrá llevar, además, todos los libros auxiliares que estimara conveniente para el mayor orden y claridad de sus operaciones.',
  'referencia': '(Congreso de la República de Venezuela, 1955)',
  'analisis': 'El artículo establece la obligación de mantener registros contables y permite utilizar libros auxiliares que favorezcan el orden y la claridad de las operaciones. Aunque la disposición se refiere específicamente a la contabilidad mercantil, expresa la importancia jurídica de conservar información organizada y verificable dentro de la actividad comercial.',
  'aporte': 'Su aporte al informe se relaciona con el principio de orden documental que debe acompañar las operaciones de compra. Los formatos, registros y mecanismos de seguimiento propuestos para la procura no sustituyen los libros contables exigidos por la ley, pero complementan el control administrativo de la documentación que antecede y acompaña las adquisiciones de la empresa.'
 }
]

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
                    'puntos de control y tiempos de referencia para el seguimiento administrativo; el flujo TO-BE y su '
                    'distribución por responsables se presentan en los Anexos B y C.'},
 {'semana': 7,
  'operativa': 'Apoyo en el procesamiento de requisiciones y verificación de información necesaria para compras '
               'en trámite.',
  'investigacion': 'Diseño de los formatos estandarizados de solicitud de cotización y orden de compra, '
                   'elaboración de la matriz de autorización por monto y definición de indicadores básicos para '
                    'el seguimiento del proceso. Como apoyos de organización y asignación de responsabilidades se '
                    'incorporan el SIPOC y la matriz RACI en los Anexos D y E.'},
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
 'orientados a mejorar la trazabilidad y facilitar el control interno del proceso de procura.',
 'La experiencia de pasantía permitió aplicar conocimientos y competencias de Administración relacionados con '
 'planificación, organización, control, análisis de procesos y gestión documental, fortaleciendo la capacidad para '
 'relacionar la formación académica con situaciones reales del funcionamiento organizacional.']

RECOMENDACIONES = [
 {'destinatario': 'A la empresa Lubricantes y Equipos Varyna, C.A.',
  'recomendaciones': ['Implementar la propuesta de manera gradual, iniciando con la formalización del canal de recepción de '
                      'requisiciones y la utilización uniforme de los formatos diseñados.',
                      'Socializar el flujo simplificado, los responsables y los criterios de autorización con el personal involucrado '
                      'en la procura antes de su aplicación general.',
                      'Registrar mensualmente indicadores básicos, como tiempo promedio del ciclo de compra, solicitudes pendientes y '
                      'requisiciones tramitadas dentro del plazo definido, para valorar los resultados de la simplificación.',
                      'Revisar periódicamente el procedimiento y los formatos con el personal del Departamento Administrativo, '
                      'incorporando ajustes cuando cambien las necesidades operativas de la empresa.']},
 {'destinatario': 'Al Instituto Universitario de Tecnología “Elías Calixto Pompa” (IUTECP).',
  'recomendaciones': ['Continuar fortaleciendo el acompañamiento académico durante las pasantías, promoviendo la aplicación '
                      'de conocimientos de planificación, organización, control y análisis de procesos frente a situaciones '
                      'administrativas reales de las empresas.']},
 {'destinatario': 'A futuros pasantes.',
  'recomendaciones': ['Llevar un registro sistemático de las actividades desde las primeras semanas, observar los procesos '
                      'administrativos, conservar las evidencias pertinentes y relacionar las tareas realizadas con los objetivos '
                      'establecidos en el informe.']}
]

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
    ('ANEXO A', 'Flujograma AS-IS del proceso actual de procura', '02_flujo_as_is_procura.png', {'width_cm': 10.0, 'height_cm': 15.0}, ['Fuente: Guzmán K. (2026).']),
    ('ANEXO B', 'Flujograma TO-BE del proceso simplificado propuesto', '03_flujo_to_be_procura.png', {'width_cm': 10.0, 'height_cm': 15.0}, ['Fuente: Guzmán K. (2026).']),
    ('ANEXO C', 'Swimlane del proceso propuesto de procura', '04_swimlane_procura.png', {'width_cm': 14.0, 'height_cm': 13.0}, ['Fuente: Guzmán K. (2026).']),
    ('ANEXO D', 'SIPOC del proceso de procura', '05_sipoc_procura.png', {'width_cm': 13.0, 'height_cm': 14.0}, ['Fuente: Guzmán K. (2026).']),
    ('ANEXO E', 'Matriz RACI propuesta del proceso de procura', '06_matriz_raci_propuesta.png', {'width_cm': 14.0, 'height_cm': 5.0}, ['Fuente: Guzmán K. (2026).'])
]
