# -*- coding: utf-8 -*-
# Archivo revisado para informe de pasantías regulares IUTECP.

# ========================================================================
# 1. RUTAS, IMÁGENES Y CUADROS
# ========================================================================
CARPETA_IMAGENES = 'imagenes'

FIRMA_TUTOR_INDUSTRIAL = 'firma_tutor_amaal.png'
FIRMA_TUTOR_ACADEMICO = 'firma_tutor_academico.png'
TEXTO_FECHA_APROBACION_TUTOR_INDUSTRIAL = 'a los 14 días del mes de agosto de 2026'


GRAFICOS = [
    {
        'numero': 1,
        'archivo': 'logo.jpg',
        'tras': 'logo_empresa',
        'titulo': 'Gráfico 1. Logotipo de Ingeniería de Telecomunicaciones, C.A.',
        'ancho_cm': 4.2,
        'lista': 'Logotipo de Ingeniería de Telecomunicaciones, C.A.',
        'pagina': '3',
        'fuente': 'Ingeniería de Telecomunicaciones, C.A. (2026).',},
    {
        'numero': 2,
        'archivo': '1.png',
        'tras': 'ubicacion',
        'titulo': 'Gráfico 2. Representación cartográfica y ubicación espacial de Ingeniería de Telecomunicaciones, C.A.',
        'ancho_cm': 5,
        'lista': 'Representación cartográfica y ubicación espacial de Ingeniería de Telecomunicaciones, C.A.',
        'pagina': '4',
        'fuente': 'Google Maps (2026).'
    },
    {
        'numero': 3,
        'archivo': '2.png',
        'tras': 'estructura',
        'titulo': 'Gráfico 3. Organigrama estructural y niveles jerárquicos de Ingeniería de Telecomunicaciones, C.A.',
        'ancho_cm': 12,
        'lista': 'Organigrama estructural y niveles jerárquicos de Ingeniería de Telecomunicaciones, C.A.',
        'pagina': '5',
        'fuente': 'Ingeniería de Telecomunicaciones, C.A. (2026).'
    },
    {
        'numero': 4,
        'archivo': '3.png',
        'tras': 'estructura',
        'titulo': 'Gráfico 4. Organigrama del Departamento de Administración.',
        'ancho_cm': 12,
        'lista': 'Organigrama del Departamento de Administración.',
        'pagina': '6',
        'fuente': 'Ingeniería de Telecomunicaciones, C.A. (2026).'
    },
    {
        'numero': 5,
        'archivo': 'ishikawa_amaal_solicitudes.png',
        'tras': 'diagnostico_tecnica',
        'titulo': 'Gráfico 5. Diagrama de Ishikawa del control y trazabilidad de las solicitudes de servicio.',
        'ancho_cm': 12.5,
        'lista': 'Diagrama de Ishikawa del control y trazabilidad de las solicitudes de servicio',
        'pagina': '',
        'fuente': 'Alrifaai A. (2026).'
    }
]

FIGURAS = []

PLANIFICACION_INTRO_TEXTO = ('La planificación relaciona cada objetivo específico con las actividades de observación, diagnóstico, análisis y '
 'formulación de mejoras al control administrativo:')

CRONOGRAMA_INTRO_TEXTO = ('El cronograma organiza las actividades operativas y de análisis durante las diez (10) semanas de pasantía, '
 'considerando la rotación inicial por Atención al Cliente y la posterior incorporación al área de '
 'Administración:')

CUADRO_POBLACION_TITULO = 'Cuadro 1. Población de los trabajadores de la empresa.'
CUADRO_PLANIFICACION_TITULO = 'Cuadro 2. Planificación integral de objetivos específicos.'
CUADRO_CRONOGRAMA_TITULO = 'Cuadro 3. Cronograma de actividades de la pasantía.'

CUADRO_PLANIFICACION_FUENTE = 'Alrifaai A. (2026).'

CUADRO_CRONOGRAMA_FUENTE = 'Alrifaai A. (2026).'

FORMATO_APROBACION_DESTACADO = True
ESTRUCTURA_ORGANIZATIVA_TITULO = 'Estructura organizativa de la empresa (Organigrama)'
CRONOGRAMA_SECCION_TITULO = 'CRONOGRAMA DE ACTIVIDADES (DIAGRAMA DE GANTT)'

ETIQUETA_ACTIVIDAD_ANALISIS = 'Actividad de análisis'

# ========================================================================
# 2. DATOS DE PORTADA
# ========================================================================
MEMBRETE = ['REPÚBLICA BOLIVARIANA DE VENEZUELA',
 'MINISTERIO DEL PODER POPULAR PARA LA EDUCACIÓN UNIVERSITARIA',
 'INSTITUTO UNIVERSITARIO DE TECNOLOGÍA',
 '"ELÍAS CALIXTO POMPA"',
 'EL TIGRE, ESTADO ANZOÁTEGUI']

TITULO_PROYECTO = ('EVALUACIÓN DEL CONTROL ADMINISTRATIVO APLICADO A LA GESTIÓN DE SOLICITUDES DE SERVICIOS DE TELECOMUNICACIONES '
 'EN LA EMPRESA INGENIERÍA DE TELECOMUNICACIONES, C.A.')

AUTOR_DATOS = ['Autor:',
 'Alrifaai Alrifaaie, Amaal',
 'C.I.: 31.985.792',
 '',
 'Tutor Industrial:',
 'Lic. Lenny Mata',
 'C.I.: 8969750',
 '',
 'Tutor Académico:',
 'Dra. Carmen J. Álvarez',
 'C.I.: 14.452.956']

FECHA_LUGAR = 'El Tigre, agosto de 2026'

CIUDAD_FECHA = FECHA_LUGAR

NOMBRE_PASANTE = 'Alrifaai Alrifaaie, Amaal'

CI_PASANTE = '31.985.792'

ESPECIALIDAD = 'Administración'

RAZON_SOCIAL = 'Ingeniería de Telecomunicaciones, C.A. (IDETEL / INTELCA)'

# ========================================================================
# 3. PÁGINAS PRELIMINARES
# ========================================================================
DEDICATORIA = ('A mi familia, por su apoyo constante, comprensión y motivación durante mi formación académica y en el desarrollo '
 'de esta etapa profesional.')

AGRADECIMIENTOS = ('Al Instituto Universitario de Tecnología “Elías Calixto Pompa” (IUTECP), por la formación recibida; a Ingeniería '
 'de Telecomunicaciones, C.A. (IDETEL), por permitirme desarrollar las pasantías y conocer de manera directa sus '
 'procesos de atención y administración; a mis tutores, por sus orientaciones y observaciones durante la elaboración '
 'del informe; y al personal de la empresa, por su disposición, acompañamiento y colaboración durante las '
 'actividades realizadas.')

RESUMEN_TEXTO = ('El presente informe recoge las actividades desarrolladas durante diez (10) semanas de pasantías profesionales en '
 'Ingeniería de Telecomunicaciones, C.A. (IDETEL), con una primera etapa de rotación por Atención al Cliente y una '
 'segunda etapa de apoyo en el área de Administración. Durante la práctica se observó el recorrido de solicitudes de '
 'afiliación e incidencias, el registro de pagos, la facturación, el seguimiento de casos y la elaboración de '
 'reportes administrativos. La situación problemática se relaciona con la ausencia de un procedimiento formalizado y '
 'unificado para controlar las solicitudes desde su recepción hasta el cierre, lo que dificulta conocer de manera '
 'oportuna los responsables, tiempos de respuesta y estatus de cada caso. El objetivo general fue evaluar el control '
 'administrativo aplicado a la gestión de solicitudes de servicios de telecomunicaciones, con el propósito de '
 'identificar sus debilidades y formular mejoras procedimentales. Para ello se realizaron observaciones directas, '
 'revisión de registros, entrevistas estructuradas al personal y un diagrama de causa-efecto para organizar los '
 'factores vinculados con las fallas detectadas. A partir de los hallazgos se formularon mejoras orientadas a '
 'establecer un flujo estandarizado, definir responsables por etapa, utilizar formatos uniformes y aplicar '
 'indicadores básicos para el seguimiento de las solicitudes. Como resultado, se determinó que la formalización del '
 'recorrido y la centralización de la información pueden facilitar la trazabilidad y reducir los reprocesos '
 'administrativos. Se concluye que el fortalecimiento del control depende principalmente de establecer criterios '
 'comunes de registro, actualización y cierre de los casos. Se recomienda implementar progresivamente el '
 'procedimiento propuesto, comunicarlo al personal involucrado y revisar periódicamente los tiempos de respuesta y '
 'solicitudes pendientes para detectar desviaciones y oportunidades de mejora.')

PALABRAS_CLAVE = 'control administrativo, solicitudes de servicio, trazabilidad, telecomunicaciones, pasantías'

INTRODUCCION_TEXTO = ['La atención de solicitudes de servicio exige coordinación entre las áreas que reciben el requerimiento, '
 'registran la información, procesan pagos o documentación y ejecutan las acciones técnicas necesarias para '
 'cerrar cada caso. En una empresa de telecomunicaciones, el control administrativo de ese recorrido permite '
 'conocer el estado de las afiliaciones e incidencias y facilita la comunicación con el suscriptor.',
 'Las pasantías en Ingeniería de Telecomunicaciones, C.A. (IDETEL) permitieron observar esta dinámica desde dos '
 'espacios vinculados: durante las primeras semanas se apoyaron tareas de Atención al Cliente y posteriormente se '
 'desarrollaron actividades en Administración. La rotación permitió identificar cómo la información originada en '
 'la atención inicial debe continuar hacia los procesos administrativos, comerciales y técnicos hasta alcanzar el '
 'cierre de la solicitud.',
 'El propósito del informe es evaluar el control administrativo aplicado a la gestión de solicitudes de servicios '
 'para determinar las principales debilidades y formular mejoras procedimentales. El trabajo se apoya en '
 'fundamentos de control administrativo, gestión de solicitudes, estandarización de procedimientos, calidad del '
 'servicio y sistemas de información, relacionándolos con las actividades realizadas durante la pasantía.',
 'El informe se organiza en cinco capítulos. El Capítulo I presenta la realidad organizacional de IDETEL; el '
 'Capítulo II desarrolla el diagnóstico situacional, los objetivos, la planificación y el cronograma; el Capítulo '
 'III expone las bases teóricas; el Capítulo IV describe las actividades ejecutadas durante las diez semanas; y '
 'el Capítulo V presenta las conclusiones y recomendaciones derivadas de la experiencia.']

# ========================================================================
# 4. CAPÍTULO I — REALIDAD ORGANIZACIONAL
# ========================================================================
RESENA_HISTORICA = ['Ingeniería de Telecomunicaciones, C.A. se consolidó en la ciudad de El Tigre, estado Anzoátegui, acumulando una '
 'trayectoria de más de cuatro (4) décadas en el mercado tecnológico de la región oriental de Venezuela. Un hito '
 'fundamental en su evolución histórica se remonta al año 1983, cuando la organización se convirtió en el primer '
 'Distribuidor Autorizado Motorola para sistemas de radio de dos vías en el oriente del país, alianza estratégica '
 'que se ha mantenido vigente e ininterrumpida a lo largo de las décadas.',
 'A través de los años, impulsada por las demandas operativas de la Faja Petrolífera del Orinoco y las '
 'necesidades de conectividad comercial, la empresa expandió sus líneas tecnológicas progresivamente. Pasó de '
 'suministrar sistemas de radiocomunicación analógica convencional en bandas VHF/UHF y sistemas Trunking '
 'analógicos (800 MHz), a liderar el mercado regional con tecnologías de radiocomunicación digital de gama alta '
 'como los estándares TETRA (europeo) y P25 (americano), esenciales para operaciones industriales de misión '
 'crítica.',
 'Con la maduración del sector tecnológico, IDETEL incorporó a su portafolio soluciones de ampliación de '
 'cobertura inalámbrica, enlaces de microondas en bandas licenciadas y no licenciadas, redes de telemetría y '
 'telecomunicaciones alámbricas, consolidando su modelo de negocios en torno a Proyectos IPC (Ingeniería, Procura '
 'y Construcción), respaldado por un laboratorio técnico especializado y personal altamente calificado.']

MISION = ('Brindar soluciones con altos estándares de confiabilidad en servicios de radiocomunicación y datos al segmento '
 'de mercado PyME, así como la entrega de servicios de calidad en el sector petrolero, asociados a los esfuerzos '
 'en ingeniería (integración multidisciplinaria), planificación y ejecución de proyectos de telecomunicaciones y '
 'automatización.')

VISION = ('Ser reconocidos por los clientes como un proveedor de servicios altamente confiable y con altos estándares '
 'técnicos y de ingeniería, con capacidad de brindar soluciones multidisciplinarias en el área de automatización '
 'y telecomunicaciones, fortaleciendo continuamente el capital humano mediante capacitación y mejora progresiva '
 'de las instalaciones, con el fin de obtener la innovación, competitividad y liderazgo necesarios para '
 'sobresalir en el mercado de nuevas tecnologías.')

VALORES = [('Confiabilidad',
  'Compromiso de entregar soluciones tecnológicas robustas que cumplan con los más altos estándares técnicos y de '
  'ingeniería para garantizar operaciones continuas y seguras.'),
 ('Innovación y Competitividad',
  'Búsqueda constante de actualización y adopción de tecnologías de última generación para sobresalir y liderar '
  'el mercado de soluciones inalámbricas y ópticas.'),
 ('Seguridad Laboral e Higiene Ocupacional',
  'Aplicación rigurosa de normas de protección e integridad física del personal en cada obra, instalación en '
  'campo o infraestructura crítica atendida.'),
 ('Excelencia Técnica',
  'Orientación hacia la precisión en los procesos de diseño, empalme por fusión, certificación de redes y '
  'asesoría en laboratorio.')]

OBJETIVOS_ORG = ['Ejecutar todo género de actividad o prestación de servicios relacionados directa o indirectamente con el ramo '
 'de las comunicaciones, computación y la electrónica en general.',
 'Prestar servicios de importación, manufacturación, asesoría, ventas, instalaciones, arrendamientos, supervisión '
 'y mantenimiento en el área de telecomunicaciones.',
 'Representar total o parcialmente cualquier producto comercial relacionado con sus operaciones mercantiles.']

OBJETIVO_GENERAL_EMPRESA = ('Ejecutar todo género de actividad o prestación de servicios relacionados directa o indirectamente con el ramo '
 'de las comunicaciones, computación y la electrónica en general.')

OBJETIVOS_ESPECIFICOS_EMPRESA = ['Prestar servicios de importación, manufacturación, asesoría, ventas, instalaciones, arrendamientos, supervisión '
 'y mantenimiento en el área de telecomunicaciones.',
 'Representar total o parcialmente cualquier producto comercial relacionado con sus operaciones mercantiles.']

UBICACION = ('La sede administrativa y operativa de Ingeniería de Telecomunicaciones, C.A. se encuentra ubicada en la Calle '
 'Bolívar, Edificio La Suiza, Piso 1, Oficina Nro. 28, ciudad de El Tigre, Municipio Simón Rodríguez, estado '
 'Anzoátegui, Venezuela.')

POBLACION_TABLA = [
 ('Empresa', 'Personal activo en los cargos de la estructura organizativa', '-', '-', 8),
 ('TOTAL GENERAL', '', '-', '-', 8),
]

POBLACION_FUENTE = 'Información suministrada por Ingeniería de Telecomunicaciones, C.A. (2026).'

POBLACION = ['Ingeniería de Telecomunicaciones, C.A. cuenta con una población total de ocho (8) trabajadores. Debido a '
 'ajustes recientes de personal, varias funciones se concentran en una estructura reducida y algunos puestos '
 'permanecen vacantes. Durante las pasantías se realizó una rotación funcional que permitió apoyar tareas '
 'correspondientes a Atención al Cliente y, posteriormente, al área de Administración.',
 'Dentro de la Supervisión de Administración se reconocen tres funciones directamente relacionadas con la '
 'experiencia de la pasante: Supervisión de Administración, Contabilidad y Tributos; Compras y Facturación; y '
 'Atención al Cliente. La pasante apoyó actividades asociadas a estas funciones de manera rotativa, lo que '
 'facilitó observar el recorrido de la información desde la atención inicial hasta el seguimiento administrativo '
 'de los casos.']

ORGANIGRAMA_TEXTO = ('La estructura organizativa de Ingeniería de Telecomunicaciones, C.A. es de tipo vertical, diseñada para '
 'garantizar una comunicación fluida entre los niveles directivos y operativos. A la cabeza se encuentra la '
 'Presidencia, seguida de la Gerencia General y Operaciones, de la cual se desprenden los departamentos de '
 'Supervisión de Administración, Contabilidad y Tributos, Supervisión Comercial, Área de Internet, Supervisión '
 'del NOC (Network Operations Center) y Mantenimiento de Radiocomunicación. Se presenta a continuación el '
 'organigrama general de la empresa y del Departamento de Administración.')

MOSTRAR_NIVELES_DIAGNOSTICO = True

DESCRIPCION_DEPARTAMENTO = ('La pasantía se realizó en la Supervisión de Administración, donde se reconocen las funciones de '
 'Supervisión de Administración, Contabilidad y Tributos; Compras y Facturación; y Atención al Cliente. La práctica '
 'incluyó una rotación inicial por Atención al Cliente y una etapa posterior de apoyo en Administración, con '
 'actividades de registro de pagos, facturación, seguimiento de solicitudes y elaboración de reportes administrativos.')

# ========================================================================
# 5. CAPÍTULO II — DIAGNÓSTICO SITUACIONAL
# ========================================================================
SITUACION_PROBLEMATICA = [{'parrafos': ['La identificación de la situación problemática permite analizar las condiciones que afectan el '
                                        'control administrativo aplicado a la gestión de solicitudes de servicios en Ingeniería de '
                                        'Telecomunicaciones, C.A. Para comprender la problemática de manera progresiva, se consideran '
                                        'aspectos generales relacionados con las organizaciones de servicio, las características propias '
                                        'del sector de telecomunicaciones y, finalmente, las condiciones observadas directamente en la '
                                        'empresa durante el período de pasantías.']},
 {'titulo': 'Nivel macro',
  'parrafos': ['En las organizaciones de servicios, el control administrativo permite verificar que las '
               'solicitudes recibidas avancen por etapas definidas, cuenten con responsables identificados y '
               'dispongan de información suficiente para conocer su estado. Cuando ese recorrido depende de '
               'canales informales o registros no unificados, se incrementa la posibilidad de reprocesos y '
               'se dificulta responder oportunamente al usuario.']},
 {'titulo': 'Nivel meso',
  'parrafos': ['En el sector de telecomunicaciones, las solicitudes pueden involucrar atención al cliente, '
               'administración, comercialización, soporte y personal técnico. Por ello, la continuidad del '
               'servicio depende no solo de la ejecución técnica, sino también de que la información '
               'administrativa se transfiera de manera ordenada entre las áreas involucradas, especialmente '
               'en afiliaciones, pagos, incidencias y cierres de casos.']},
 {'titulo': 'Nivel micro',
  'parrafos': ['En Ingeniería de Telecomunicaciones, C.A. (IDETEL), la rotación realizada durante las '
               'pasantías permitió observar que las solicitudes de afiliación e incidencias no cuentan con '
               'un procedimiento único y formalizado de seguimiento desde su recepción hasta el cierre. Se '
               'identificaron registros no estandarizados, actualización desigual del estatus de los casos y '
               'dificultades para conocer en un mismo punto la información manejada por Atención al Cliente, '
               'Administración y las áreas técnicas.',
               'Las principales manifestaciones se relacionan con demoras en la actualización de casos, '
               'comunicación fragmentada entre áreas, ausencia de tiempos de referencia por etapa y carencia '
               'de indicadores básicos de seguimiento. Como consecuencias pueden generarse reprocesos, mayor '
               'tiempo de respuesta y dificultades para ofrecer al suscriptor información precisa sobre el '
               'estado de su solicitud.']},
  {'parrafos': ['El recorrido actual de afiliaciones e incidencias se representa en el flujograma AS-IS incorporado como '
                'Anexo B, el cual permite visualizar la transición de la información entre las áreas involucradas.',
               'Para organizar las causas de la situación se empleó un diagrama de Ishikawa, complementado '
               'con observación directa, revisión de registros y entrevistas estructuradas al personal. La '
               'técnica permitió relacionar factores de procedimiento, comunicación, registro y seguimiento '
                'con las demoras e inconsistencias identificadas. La representación gráfica de esta técnica se presenta a continuación.']}]

INTERROGANTE_TITULO = 'Interrogante orientadora'

INTERROGANTE_PROBLEMA = ('¿Cómo puede evaluarse el control administrativo aplicado a la gestión de solicitudes de servicios de '
 'telecomunicaciones en IDETEL para identificar sus principales debilidades y formular mejoras procedimentales que '
 'fortalezcan la trazabilidad y el seguimiento de los casos?')

OBJETIVO_GENERAL = ('Evaluar el control administrativo aplicado a la gestión de solicitudes de servicios de telecomunicaciones en '
 'Ingeniería de Telecomunicaciones, C.A. (IDETEL), con el propósito de identificar sus debilidades y formular '
 'mejoras procedimentales.')

OBJETIVOS_ESPECIFICOS = ['Diagnosticar el proceso administrativo actual de recepción, registro, seguimiento y cierre de solicitudes de '
 'afiliación e incidencias en Ingeniería de Telecomunicaciones, C.A., considerando la transición de la información '
 'entre Atención al Cliente, Administración y las áreas relacionadas.',
 'Identificar las deficiencias y causas presentes en los mecanismos de control de las solicitudes de servicio, '
 'considerando su incidencia en los tiempos de respuesta, la trazabilidad de los casos y la atención al suscriptor.',
 'Formular mejoras al control administrativo de las solicitudes mediante un flujo estandarizado, formatos de '
 'registro, responsables por etapa e indicadores básicos de seguimiento.']

PLANIFICACION_DATOS = [('Diagnosticar el proceso administrativo actual de recepción, registro, seguimiento y cierre de solicitudes de '
  'afiliación e incidencias en Ingeniería de Telecomunicaciones, C.A., considerando la transición de la información '
  'entre Atención al Cliente, Administración y las áreas relacionadas.',
  'Proceso administrativo de gestión de solicitudes de servicio.',
  'Observar el recorrido de afiliaciones e incidencias desde Atención al Cliente hasta su seguimiento '
  'administrativo, describir las etapas y revisar la documentación utilizada.',
  'Observación directa y análisis documental.',
  'Guía de observación, registros de solicitudes, comprobantes y documentos internos.'),
 ('Identificar las deficiencias y causas presentes en los mecanismos de control de las solicitudes de servicio, '
  'considerando su incidencia en los tiempos de respuesta, la trazabilidad de los casos y la atención al suscriptor.',
  'Deficiencias y causas que afectan el control administrativo de solicitudes.',
  'Aplicar entrevistas estructuradas al personal, revisar casos históricos, comparar tiempos de respuesta y elaborar '
  'un diagrama de Ishikawa con las causas identificadas.',
  'Entrevista estructurada, análisis documental, comparación de tiempos y diagrama causa-efecto.',
  'Guía de entrevista, registros históricos, reportes internos, hoja de cálculo y matriz de causas.'),
 ('Formular mejoras al control administrativo de las solicitudes mediante un flujo estandarizado, formatos de '
  'registro, responsables por etapa e indicadores básicos de seguimiento.',
  'Mejoras al control administrativo de solicitudes.',
  'Diseñar el flujo estandarizado, formatos de registro, responsables por etapa e indicadores básicos de '
  'seguimiento; validar la propuesta con el tutor industrial.',
  'Diseño procedimental y validación técnica.',
  'Procesador de textos, herramientas de diagramación, hoja de cálculo y formato de validación.')]

CRONOGRAMA_DATOS = [('Inducción y reconocimiento de Atención al Cliente y del flujo de solicitudes.',
  [True, False, False, False, False, False, False, False, False, False]),
 ('Apoyo en Atención al Cliente: registro de pagos, recepción de solicitudes y observación del proceso.',
  [True, True, True, False, False, False, False, False, False, False]),
 ('Levantamiento y descripción del proceso administrativo de afiliaciones e incidencias.',
  [True, True, True, False, False, False, False, False, False, False]),
 ('Diseño y aplicación de entrevistas estructuradas al personal relacionado con las solicitudes.',
  [False, False, True, True, False, False, False, False, False, False]),
 ('Diagnóstico de deficiencias y elaboración del diagrama de Ishikawa.',
  [False, False, False, True, True, False, False, False, False, False]),
 ('Revisión y desarrollo de las bases teóricas relacionadas con el control administrativo.',
  [False, False, False, False, True, True, False, False, False, False]),
 ('Análisis del impacto de las debilidades sobre tiempos, trazabilidad y atención al suscriptor.',
  [False, False, False, False, False, True, False, False, False, False]),
 ('Diseño del flujo estandarizado y de los formatos de control de solicitudes.',
  [False, False, False, False, False, False, True, True, False, False]),
 ('Formulación y validación de la propuesta de mejora.',
  [False, False, False, False, False, False, False, False, True, False]),
 ('Consolidación, revisión y presentación del informe de pasantías.',
  [False, False, False, False, False, False, False, False, False, True]),
 ('Apoyo operativo en pagos, facturación, seguimiento de casos y reportes administrativos.',
  [False, False, False, True, True, True, True, True, True, True])]

# ========================================================================
# 6. CAPÍTULO III — MARCO TEÓRICO
# ========================================================================
BASES_TEORICAS = [{'titulo': 'Control Administrativo',
  'posicion_autor': 'Desde la perspectiva de quien desarrolla este informe, el control administrativo en IDETEL debe '
                    'convertirse en una herramienta de seguimiento continuo y no limitarse a la revisión posterior '
                    'de los casos.',
  'parrafos': ['El control administrativo constituye una de las funciones fundamentales del proceso administrativo y '
               'se define como el mecanismo mediante el cual la organización verifica que las actividades ejecutadas '
               'se correspondan con lo planificado, detectando desviaciones y aplicando las medidas correctivas '
               'necesarias. Robbins y Coulter (2010) señalan que el control eficaz no solo identifica fallas, sino '
               'que proporciona información oportuna para la toma de decisiones gerenciales, convirtiéndose en un '
               'instrumento de mejora continua y no únicamente de fiscalización.',
               'En el contexto del Departamento de Administración de Ingeniería de Telecomunicaciones, C.A., el '
               'control administrativo se aplica sobre el ciclo de gestión de solicitudes de servicio, abarcando '
               'desde la recepción de la solicitud del suscriptor hasta el cierre definitivo del caso. La ausencia '
               'de mecanismos formales de control en este ciclo genera inconsistencias entre los departamentos '
               'involucrados y dificulta la evaluación del desempeño del proceso de atención.'],
  'cita_larga': {'texto': 'El control es el proceso de monitorear las actividades para asegurarse de que se lleven a '
                          'cabo según lo planeado y para corregir cualquier desviación significativa. Los gerentes '
                          'no pueden saber realmente si sus unidades están desempeñándose adecuadamente hasta que '
                          'evalúan qué actividades se han llevado a cabo y comparan el desempeño real con el '
                          'estándar deseado.',
                 'autor': '(Robbins y Coulter, 2010, p. 398)'},
  'post_cita': ''},
 {'titulo': 'Gestión de Solicitudes de Servicio',
  'posicion_autor': 'En el contexto de IDETEL, la gestión de solicitudes requiere un flujo único que permita conocer '
                    'el responsable, el estado y el tiempo de atención de cada caso.',
  'parrafos': ['La gestión de solicitudes de servicio comprende el conjunto de procedimientos administrativos '
               'orientados a recepcionar, registrar, procesar y dar seguimiento a los requerimientos presentados por '
               'los clientes o suscriptores de una organización. Zeithaml, Parasuraman y Berry (1993) establecen que '
               'la calidad del servicio percibida por el cliente está directamente vinculada a la capacidad de la '
               'organización para gestionar sus solicitudes de forma ágil, transparente y con comunicación fluida en '
               'cada etapa del proceso.',
               'En empresas de telecomunicaciones como IDETEL, la gestión de solicitudes abarca dos categorías '
               'principales: las solicitudes de afiliación de nuevos suscriptores, que implican la coordinación '
               'entre las áreas comercial, técnica y administrativa; y las incidencias reportadas por suscriptores '
               'activos, que requieren diagnóstico, despacho de cuadrillas y cierre verificado del caso. La ausencia '
               'de un sistema unificado de seguimiento para ambas categorías genera retrasos y reprocesos que '
               'impactan directamente en la satisfacción del cliente.'],
  'cita_larga': None,
  'post_cita': ''},
 {'titulo': 'Procesos Administrativos y Estandarización de Procedimientos',
  'posicion_autor': 'A juicio de quien suscribe, la estandarización propuesta no busca aumentar la carga '
                    'administrativa, sino eliminar ambigüedades y hacer verificable cada etapa del proceso.',
  'parrafos': ['El proceso administrativo constituye el marco conceptual que rige el funcionamiento de las '
               'organizaciones modernas. Chiavenato (2006) lo describe como el conjunto secuencial e '
               'interrelacionado de funciones de planificación, organización, dirección y control, orientadas al '
               'logro eficiente de los objetivos organizacionales. La estandarización de los procedimientos dentro '
               'de este marco garantiza que las actividades se ejecuten de manera uniforme, reduciendo la '
               'variabilidad y los errores derivados de la discrecionalidad individual.',
               'La formalización de los procedimientos mediante manuales, flujogramas y formatos estandarizados '
               'constituye una herramienta esencial para el control administrativo. Según Harrington (1993), un '
               'proceso estandarizado es medible, controlable y mejorable, condiciones que permiten a la '
               'organización identificar con precisión los puntos de falla y aplicar acciones correctivas '
               'focalizadas. En el caso de IDETEL, la ausencia de procedimientos escritos para la gestión de '
               'solicitudes es una de las causas raíz de las deficiencias identificadas.'],
  'cita_larga': None,
  'post_cita': ''},
 {'titulo': 'Calidad del Servicio en Empresas de Telecomunicaciones',
  'posicion_autor': 'En el contexto de estas pasantías, la calidad del servicio se relaciona directamente con la '
                    'capacidad administrativa de IDETEL para responder y dar seguimiento oportuno a las solicitudes '
                    'del suscriptor.',
  'parrafos': ['La calidad del servicio se define como el grado en que las características del servicio prestado '
               'satisfacen o superan las expectativas del cliente. Parasuraman, Zeithaml y Berry (1988) '
               'desarrollaron el modelo SERVQUAL, que identifica cinco dimensiones de la calidad del servicio: '
               'fiabilidad, capacidad de respuesta, seguridad, empatía y elementos tangibles. En el sector de '
               'telecomunicaciones, la fiabilidad y la capacidad de respuesta son las dimensiones con mayor peso en '
               'la percepción del cliente.',
               'Las deficiencias en el control administrativo del proceso de solicitudes de servicio impactan '
               'directamente sobre la fiabilidad y la capacidad de respuesta de IDETEL. Cuando una solicitud no es '
               'gestionada dentro de los tiempos establecidos o su estatus no puede ser verificado en tiempo real, '
               'el cliente percibe una falla en la calidad del servicio que deteriora su confianza en la '
               'organización y puede derivar en la cancelación del contrato o en la difusión de experiencias '
               'negativas.'],
  'cita_larga': None,
  'post_cita': ''},
 {'titulo': 'Sistemas de Información para el Control Administrativo',
  'posicion_autor': 'Desde la posición del autor, una herramienta de seguimiento centralizada es viable para IDETEL '
                    'porque permite mejorar la trazabilidad sin modificar la naturaleza de los servicios que presta '
                    'la empresa.',
  'parrafos': ['Un sistema de información constituye un conjunto organizado de recursos tecnológicos y '
               'procedimentales orientados a la captura, almacenamiento, procesamiento y distribución de datos con '
               'el propósito de apoyar la toma de decisiones. Laudon y Laudon (2016) distinguen los sistemas de '
               'procesamiento de transacciones como la categoría que registra y gestiona las operaciones rutinarias '
               'de la organización, siendo esta la tipología más pertinente para el control de solicitudes de '
               'servicio en una empresa de telecomunicaciones.',
               'La implementación de un sistema de tickets o plataforma de seguimiento de solicitudes en IDETEL '
               'permitiría centralizar el registro de cada caso, asignar responsables, definir tiempos de atención y '
               'generar alertas ante incumplimientos. Esta herramienta transformaría el control administrativo de '
               'reactivo a proactivo, dotando a la supervisión de información en tiempo real para la toma de '
               'decisiones y la evaluación continua del desempeño del proceso.'],
  'cita_larga': None,
  'post_cita': ''},
 {'titulo': 'Base Legal: Constitución de la República Bolivariana de Venezuela — Artículo 112',
  'espaciado_titulo_compacto': True,
  'parrafos': ['Como marco general de la actividad económica privada, la Constitución reconoce la iniciativa '
               'empresarial dentro de los límites establecidos por el ordenamiento jurídico.'],
  'cita_larga': {'texto': 'Todas las personas pueden dedicarse libremente a la actividad económica de su '
                          'preferencia, sin más limitaciones que las previstas en esta Constitución y las que '
                          'establezcan las leyes, por razones de desarrollo humano, seguridad, sanidad, protección '
                          'del ambiente u otras de interés social. El Estado promoverá la iniciativa privada, '
                          'garantizando la creación y justa distribución de la riqueza, así como la producción de '
                          'bienes y servicios que satisfagan las necesidades de la población, la libertad de '
                          'trabajo, empresa, comercio, industria, sin perjuicio de su facultad para dictar medidas '
                          'para planificar, racionalizar y regular la economía e impulsar el desarrollo integral del '
                          'país.',
                 'autor': '(Constitución de la República Bolivariana de Venezuela, 1999, art. 112)'},
  'post_cita': '',
  'posicion_autor': 'El aporte de este artículo al informe es de carácter general, porque reconoce el ejercicio de '
                    'la actividad empresarial y permite ubicar la prestación de servicios de IDETEL dentro de una '
                    'actividad económica sujeta al ordenamiento jurídico. Su relación con el informe se limita a '
                    'este fundamento general y no establece por sí mismo el procedimiento administrativo de '
                    'seguimiento de solicitudes.'},
 {'titulo': 'Base Legal: Código de Comercio — Artículo 32',
  'espaciado_titulo_compacto': True,
  'parrafos': ['El Código de Comercio establece obligaciones vinculadas con el orden y claridad de los registros de '
               'los comerciantes, aspecto relacionado con la necesidad de conservar información organizada y '
               'verificable en los procesos administrativos.'],
  'cita_larga': {'texto': 'Todo comerciante debe llevar en idioma castellano su contabilidad, la cual comprenderá, '
                          'obligatoriamente, el libro Diario, el libro Mayor y el de Inventarios. Podrá llevar, '
                          'además, todos los libros auxiliares que estimara conveniente para el mayor orden y '
                          'claridad de sus operaciones.',
                 'autor': '(Código de Comercio, 1955, art. 32)'},
  'post_cita': '',
  'posicion_autor': 'La relación con el informe se encuentra en el principio de orden y claridad de las operaciones '
                    'mercantiles. Los formatos y mecanismos de seguimiento propuestos no sustituyen los libros '
                    'contables exigidos por la ley, pero complementan el control administrativo al organizar '
                    'información asociada con solicitudes, pagos, facturación y seguimiento de casos.'}]

POST_CITA_TEXTO = ''

# ========================================================================
# 7. CAPÍTULO IV — ACTIVIDADES REALIZADAS
# ========================================================================
ACTIVIDADES_DESCRIPCION = ('Durante las diez (10) semanas de pasantías se desarrollaron actividades operativas y de análisis mediante una '
  'rotación inicial por Atención al Cliente y una segunda etapa de apoyo en Administración. Algunas actividades y espacios observados '
  'se documentan en la memoria fotográfica incorporada como Anexo G:')

ACTIVIDADES_LISTA = [{'semana': 1,
  'operativa': 'Inducción institucional y rotación inicial por Atención al Cliente, reconocimiento de los tipos '
               'de solicitudes recibidas, revisión del proceso de registro de pagos y familiarización con la '
               'información utilizada para atender a los suscriptores.',
  'investigacion': 'Observación directa del punto de inicio de las solicitudes de afiliación e incidencias, '
                   'identificando los datos que se generan en Atención al Cliente y la forma en que son '
                   'comunicados a otras áreas.'},
 {'semana': 2,
  'operativa': 'Apoyo en Atención al Cliente mediante recepción y registro de pagos, verificación de datos '
               'básicos de suscriptores y orientación inicial sobre solicitudes e incidencias reportadas.',
  'investigacion': 'Levantamiento del recorrido de las solicitudes desde su recepción, revisión de registros '
                   'disponibles y elaboración de un esquema preliminar de las etapas y áreas que intervienen en '
                   'cada tipo de caso.'},
 {'semana': 3,
  'operativa': 'Continuación del apoyo en Atención al Cliente, registro de pagos y solicitudes, actualización de '
               'información básica y seguimiento inicial de casos remitidos a otras áreas.',
  'investigacion': 'Diseño de una guía de entrevista estructurada y revisión del flujo observado para precisar '
                   'los puntos donde se pierde continuidad o se dificulta conocer el estatus de las solicitudes.'},
 {'semana': 4,
  'operativa': 'Inicio de la rotación por Administración con apoyo en procesamiento de pagos, facturación, '
               'revisión de documentación y seguimiento administrativo de solicitudes activas.',
  'investigacion': 'Aplicación de entrevistas estructuradas al personal vinculado con Administración, Atención al '
                   'Cliente y áreas relacionadas, registrando las principales fallas percibidas en comunicación, '
                   'control y seguimiento.'},
  {'semana': 5,
  'operativa': 'Apoyo en tareas administrativas de facturación, actualización de registros y verificación del '
               'cierre de solicitudes e incidencias correspondientes al período.',
   'investigacion': 'Organización de los hallazgos del diagnóstico y elaboración del diagrama de Ishikawa para '
                    'representar las causas relacionadas con procedimiento, comunicación, registro y seguimiento; '
                    'inicio de la revisión de bases teóricas.'},
 {'semana': 6,
  'operativa': 'Procesamiento de pagos y documentos administrativos, apoyo en facturación y elaboración de '
               'reportes básicos requeridos por la supervisión.',
  'investigacion': 'Análisis del impacto de las deficiencias identificadas sobre los tiempos de respuesta, la '
                   'trazabilidad y la atención al suscriptor, complementando el desarrollo del marco teórico.'},
 {'semana': 7,
  'operativa': 'Apoyo en seguimiento de casos, actualización de registros administrativos y organización de '
               'documentación vinculada con solicitudes de servicio.',
  'investigacion': 'Diseño del nuevo flujo estandarizado para la gestión de solicitudes, estableciendo etapas, '
                    'responsables, tiempos de referencia y puntos de control desde la recepción hasta el cierre; '
                    'la propuesta y su distribución interdepartamental se presentan en los Anexos A y C.'},
 {'semana': 8,
  'operativa': 'Colaboración en facturación, seguimiento de incidencias y preparación de reportes administrativos '
               'del período.',
  'investigacion': 'Diseño de formatos estandarizados para afiliaciones e incidencias y redacción del '
                   'procedimiento de control que acompaña al flujo propuesto.'},
 {'semana': 9,
  'operativa': 'Participación en las actividades regulares de Administración y apoyo en el cierre y seguimiento '
               'de casos correspondientes al período de pasantías.',
  'investigacion': 'Redacción y validación de la propuesta de mejora con el tutor industrial, incorporación de '
                   'observaciones y preparación del flujograma definitivo del proceso propuesto (véase Anexo A).'},
 {'semana': 10,
  'operativa': 'Presentación de los resultados y de la propuesta ante la supervisión del área, gestión de los '
               'recaudos de cierre y organización final de la documentación de pasantías.',
  'investigacion': 'Consolidación del informe académico, revisión de la normativa IUTECP, incorporación de anexos '
                   'y correcciones finales para la entrega institucional.'}]

# ========================================================================
# 8. CAPÍTULO V — CONCLUSIONES Y RECOMENDACIONES
# ========================================================================
CONCLUSIONES = ['Se diagnosticó que la gestión de solicitudes de IDETEL se inicia en Atención al Cliente y continúa hacia '
 'Administración y las áreas relacionadas, sin contar con un procedimiento único que establezca de forma visible el '
 'recorrido completo, los responsables y los criterios de cierre de cada caso.',
 'Se identificaron como principales deficiencias la falta de formatos uniformes, la actualización no centralizada '
 'del estatus, la ausencia de tiempos de referencia por etapa y las dificultades de comunicación entre las áreas; '
 'estas condiciones afectan la trazabilidad y pueden prolongar los tiempos de respuesta al suscriptor.',
 'Se formularon mejoras al control administrativo mediante un flujo estandarizado, responsables por etapa, formatos '
 'de registro e indicadores básicos de seguimiento, orientados a facilitar la continuidad de la información y el '
 'control de las solicitudes desde su recepción hasta el cierre.',
 'La experiencia de pasantía permitió aplicar conocimientos y competencias de Administración vinculados con control, '
 'organización de procesos, gestión documental, seguimiento y atención al usuario, fortaleciendo la relación entre '
 'la formación académica y las situaciones reales observadas en la empresa.']

RECOMENDACIONES = [
 {'destinatario': 'A la empresa Ingeniería de Telecomunicaciones, C.A.',
  'recomendaciones': ['Implementar progresivamente el flujo estandarizado propuesto y verificar su funcionamiento con un grupo '
                      'controlado de solicitudes antes de aplicarlo a todos los casos.',
                      'Utilizar de manera uniforme los formatos de registro de afiliaciones e incidencias y definir claramente el '
                      'responsable de actualizar el estatus en cada etapa.',
                      'Registrar y revisar periódicamente tiempos de respuesta, solicitudes pendientes y casos cerrados para '
                      'identificar retrasos recurrentes y aplicar acciones correctivas.',
                      'Evaluar posteriormente una herramienta digital centralizada de seguimiento cuando el procedimiento '
                      'administrativo ya se encuentre formalizado y validado por las áreas involucradas.']},
 {'destinatario': 'Al Instituto Universitario de Tecnología “Elías Calixto Pompa” (IUTECP).',
  'recomendaciones': ['Continuar fortaleciendo el acompañamiento académico durante las pasantías y la articulación entre los '
                      'conocimientos adquiridos en la carrera y las situaciones administrativas observadas en las empresas.']},
 {'destinatario': 'A futuros pasantes.',
  'recomendaciones': ['Llevar un registro sistemático de las actividades desde las primeras semanas, observar los procesos '
                      'administrativos, conservar las evidencias pertinentes y relacionar las tareas realizadas con los objetivos '
                      'establecidos en el informe.']}
]

# ========================================================================
# 9. REFERENCIAS Y ANEXOS
# ========================================================================
REFERENCIAS_LISTA = ['Asamblea Nacional Constituyente. (1999). Constitución de la República Bolivariana de Venezuela. Gaceta Oficial de '
 'la República Bolivariana de Venezuela.',
 'Chiavenato, I. (2006). Introducción a la teoría general de la administración (7ma ed.). McGraw-Hill, México.',
 'Congreso de la República de Venezuela. (1955). Código de Comercio. Gaceta Oficial Extraordinaria N.º 475.',
 'Harrington, H. J. (1993). Mejoramiento de los procesos de la empresa. McGraw-Hill, Colombia.',
 'Laudon, K., y Laudon, J. (2016). Sistemas de información gerencial (14va ed.). Pearson Educación, México.',
 'Parasuraman, A., Zeithaml, V., y Berry, L. (1988). SERVQUAL: A multiple-item scale for measuring consumer '
 'perceptions of service quality. Journal of Retailing, 64(1), 12-40.',
 'Robbins, S., y Coulter, M. (2010). Administración (10ma ed.). Pearson Educación, México.',
 'Zeithaml, V., Parasuraman, A., y Berry, L. (1993). Calidad total en la gestión de servicios. Díaz de Santos, '
 'España.']

ANEXOS_LISTA = [
    ('ANEXO A', 'Flujograma del proceso propuesto de gestión de solicitudes de servicios', 4, {'width_cm': 11.0, 'height_cm': 13.5}, ['Fuente: Alrifaai A. (2026).']),
    ('ANEXO B', 'Flujograma AS-IS de afiliaciones e incidencias', '02_flujo_as_is_solicitudes.png', {'width_cm': 10.0, 'height_cm': 15.0}, ['Fuente: Alrifaai A. (2026).']),
    ('ANEXO C', 'Swimlane interdepartamental de gestión de solicitudes', '04_swimlane_gestion_solicitudes.png', {'width_cm': 14.0, 'height_cm': 10.0}, ['Fuente: Alrifaai A. (2026).']),
    ('ANEXO D', 'Estados de una solicitud de servicio', '05_estados_solicitud.png', {'width_cm': 13.0, 'height_cm': 8.0}, ['Fuente: Alrifaai A. (2026).']),
    ('ANEXO E', 'Comunicación interdepartamental', '10_comunicacion_interdepartamental.png', {'width_cm': 13.0, 'height_cm': 13.0}, ['Fuente: Alrifaai A. (2026).']),
    ('ANEXO F', 'Comparación AS-IS y TO-BE del control de solicitudes', '11_comparacion_as_is_to_be.png', {'width_cm': 13.0, 'height_cm': 13.0}, ['Fuente: Alrifaai A. (2026).']),
    (
        'ANEXO G',
        'Memoria fotográfica de las actividades realizadas',
        [
            {
                'archivo': 'adjuntos/IMG-20260818-WA0007.jpg',
                'titulo': 'Fotografía 1. Registro de actividades administrativas frente al equipo de trabajo.',
                'configuracion': {'width_cm': 13.5, 'height_cm': 10.5},
            },
            {
                'archivo': 'adjuntos/IMG-20260818-WA0008.jpg',
                'titulo': 'Fotografía 2. Vista general del espacio de trabajo del área administrativa.',
                'configuracion': {'width_cm': 13.5, 'height_cm': 10.5},
            },
            {
                'archivo': 'adjuntos/IMG-20260818-WA0009.jpg',
                'titulo': 'Fotografía 3. Verificación de información en los registros administrativos del área.',
                'configuracion': {'width_cm': 10.5, 'height_cm': 15.0},
            },
            {
                'archivo': 'adjuntos/IMG-20260818-WA0010.jpg',
                'titulo': 'Fotografía 4. Puesto de trabajo utilizado para la gestión de información administrativa.',
                'configuracion': {'width_cm': 13.5, 'height_cm': 10.5},
            },
            {
                'archivo': 'adjuntos/IMG-20260818-WA0011.jpg',
                'titulo': 'Fotografía 5. Revisión de registros y documentos desde el puesto de trabajo.',
                'configuracion': {'width_cm': 10.5, 'height_cm': 15.0},
            },
            {
                'archivo': 'adjuntos/IMG-20260818-WA0012.jpg',
                'titulo': 'Fotografía 6. Revisión de información de pagos y soportes documentales.',
                'configuracion': {'width_cm': 10.5, 'height_cm': 15.0},
            },
            {
                'archivo': 'adjuntos/IMG-20260818-WA0015.jpg',
                'titulo': 'Fotografía 7. Puesto de trabajo del área administrativa.',
                'configuracion': {'width_cm': 10.5, 'height_cm': 15.0},
            },
            {
                'archivo': 'adjuntos/IMG-20260818-WA0016.jpg',
                'titulo': 'Fotografía 8. Puesto de trabajo y equipo utilizado durante la pasantía.',
                'configuracion': {'width_cm': 10.5, 'height_cm': 15.0},
            },
        ],
        None,
        ['Fuente: Registro fotográfico suministrado por la autora (2026).'],
    ),
]
