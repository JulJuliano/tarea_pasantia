# -*- coding: utf-8 -*-
# Archivo revisado para informe de pasantías regulares IUTECP.

# ========================================================================
# 1. RUTAS, IMÁGENES Y CUADROS
# ========================================================================
CARPETA_IMAGENES = 'imagenes'

# El logotipo se inserta como gráfico académico antes de la ubicación geográfica.
GRAFICOS = [
    {
        'numero': 1,
        'archivo': 'logo.png',
        'tras': 'logo_empresa',
        'titulo': 'Gráfico 1. Logotipo de la Empresa Mixta Petrolera Venangocupet, S.A.',
        'ancho_cm': 4.2,
        'lista': 'Logotipo de la Empresa Mixta Petrolera Venangocupet, S.A.',
        'pagina': '4',
        'fuente': 'Empresa Mixta Petrolera Venangocupet, S.A. (2026).',},
    {
        'numero': 2,
        'archivo': 'mapa.png',
        'tras': 'ubicacion',
        'titulo': 'Gráfico 2. Referencia cartográfica de la ubicación de las oficinas administrativas de Venangocupet, S.A.',
        'ancho_cm': 11,
        'lista': 'Referencia cartográfica de la ubicación de las oficinas administrativas de Venangocupet, S.A.',
        'pagina': '5',
        'fuente': 'Captura cartográfica de Google Maps (2026). La empresa no aparece rotulada de forma independiente; se emplea como referencia el Centro Comercial San Remo Mall.'
    },
    {
        'numero': 3,
        'archivo': '1.png',
        'tras': 'estructura',
        'titulo': 'Gráfico 3. Organigrama estructural y niveles jerárquicos de Venangocupet, S.A.',
        'ancho_cm': 12,
        'lista': 'Organigrama estructural y niveles jerárquicos de Venangocupet, S.A.',
        'pagina': '7',
        'fuente': 'Empresa Mixta Petrolera Venangocupet, S.A. (2026).'
    },
    {
        'numero': 4,
        'archivo': '2.png',
        'tras': 'estructura',
        'titulo': 'Gráfico 4. Organigrama del Departamento de Presidencia.',
        'ancho_cm': 12,
        'lista': 'Organigrama del Departamento de Presidencia',
        'pagina': '8',
        'fuente': 'Empresa Mixta Petrolera Venangocupet, S.A. (2026).'
    }
]

PLANIFICACION_INTRO_TEXTO = ('La planificación relaciona cada objetivo específico con las actividades técnicas necesarias para el desarrollo '
 'y validación del sistema automatizado:')

CRONOGRAMA_INTRO_TEXTO = ('El cronograma organiza las fases de diagnóstico, diseño, implementación y validación del sistema a lo largo de '
 'las nueve (9) semanas de pasantía:')

CUADRO_CRONOGRAMA_TITULO = 'Cuadro 2. Cronograma de actividades del desarrollo del sistema automatizado.'

CUADROS_INDICE = [('1', 'Planificación integral de objetivos específicos', '8'),
 ('2', 'Cronograma de actividades del desarrollo del sistema automatizado', '9')]

# ========================================================================
# 2. DATOS DE PORTADA
# ========================================================================
MEMBRETE = ['REPÚBLICA BOLIVARIANA DE VENEZUELA',
 'MINISTERIO DEL PODER POPULAR PARA LA EDUCACIÓN UNIVERSITARIA',
 'INSTITUTO UNIVERSITARIO DE TECNOLOGÍA',
 '"ELÍAS CALIXTO POMPA"',
 'EL TIGRE, ESTADO ANZOÁTEGUI']

TITULO_PROYECTO = ('DESARROLLO DE UN PROTOTIPO DE SISTEMA PARA EL CONTROL, TRAZABILIDAD Y REPORTE DOCUMENTAL EN LA '
 'PRESIDENCIA DE VENANGOCUPET, S.A.')

AUTOR_DATOS = ['Autor:',
 'Cardona, Juliano',
 'C.I.: 32.281.199',
 '',
 'Tutor Industrial:',
 'Ing. Sabaneta, Yasmin',
 'C.I.: 14.187.924',
 '',
 'Tutor Académico:',
 'Ing. Mejías, José',
 'C.I.: 4.273.815']

FECHA_LUGAR = 'El Tigre, agosto de 2026'

CIUDAD_FECHA = FECHA_LUGAR

NOMBRE_PASANTE = 'Cardona, Juliano'

CI_PASANTE = '32.281.199'

ESPECIALIDAD = 'Informática'

RAZON_SOCIAL = 'Empresa Mixta Petrolera Venangocupet, S.A.'

# ========================================================================
# 3. PÁGINAS PRELIMINARES
# ========================================================================
DEDICATORIA = 'A mi familia, por su apoyo incondicional en cada paso de mi formación académica y personal.'

AGRADECIMIENTOS = ('A la Empresa Mixta Petrolera Venangocupet, S.A., por abrir las puertas de su organización y brindar la '
 'oportunidad de desarrollar este proyecto técnico de la mano de excelentes profesionales.')

RESUMEN_TEXTO = ('El presente informe expone las actividades realizadas durante nueve (9) semanas de pasantías profesionales en '
 'el Departamento de Presidencia de la Empresa Mixta Petrolera Venangocupet, S.A. La práctica permitió reconocer '
 'el flujo real de recepción, revisión, registro, firma y despacho de expedientes, cuyo control se efectúa '
 'mediante hojas de cálculo y requiere transcripción repetitiva de datos. Esta dinámica puede generar duplicidad '
 'u omisión de registros y dificulta la obtención inmediata de resúmenes sobre documentos ingresados, firmados, '
 'pendientes o despachados. En respuesta a esta situación se planteó como objetivo general desarrollar un sistema '
 'automatizado para el control, trazabilidad y reporte documental del área. Las actividades comprendieron el '
 'diagnóstico del proceso, levantamiento de requerimientos, modelado de una base de datos relacional, diseño de '
 'la interfaz, implementación con SQLite, integración de una aplicación de escritorio y pruebas funcionales de '
 'los módulos de registro, consulta, historial y reportes. Como resultado se obtuvo un prototipo funcional '
 'orientado a reducir tareas repetitivas y mantener un historial verificable del recorrido de los expedientes. Se '
 'concluye que la solución desarrollada responde a los requerimientos esenciales identificados en Presidencia. Se '
 'recomienda realizar una incorporación progresiva de los registros y establecer respaldos periódicos de la base '
 'de datos antes de su utilización continua.')

PALABRAS_CLAVE = 'sistema automatizado, trazabilidad documental, SQLite, Wails, pasantías'

INTRODUCCION_TEXTO = ['La gestión documental constituye una actividad esencial en las organizaciones, pues permite mantener '
 'control sobre la recepción, revisión, circulación y despacho de información necesaria para el '
 'funcionamiento administrativo. En áreas de alta dirección, conocer con rapidez el estado y recorrido de '
 'los expedientes contribuye a responder oportunamente a los requerimientos de las distintas unidades.',
 'En el Departamento de Presidencia de la Empresa Mixta Petrolera Venangocupet, S.A., el control de los '
 'movimientos documentales se apoya en hojas de cálculo. Durante las pasantías se observó que la '
 'transcripción manual y repetitiva de datos puede generar duplicidades, omisiones y demoras para elaborar '
 'resúmenes solicitados por la directiva, lo que hizo pertinente desarrollar una herramienta de escritorio '
 'para organizar la información sin alterar el flujo real del departamento.',
 'El propósito de la pasantía fue desarrollar un sistema automatizado para el control, trazabilidad y '
 'reporte documental, sustentado en fundamentos de sistemas de información, gestión documental, bases de '
 'datos relacionales y automatización de procesos administrativos. El alcance comprendió diagnóstico, '
 'definición de requerimientos, diseño lógico, implementación y validación funcional.',
 'El informe se organiza en cinco capítulos: realidad organizacional; diagnóstico, objetivos y '
 'planificación; fundamentos teóricos; actividades realizadas; y conclusiones y recomendaciones.']

# ========================================================================
# 4. CAPÍTULO I — REALIDAD ORGANIZACIONAL
# ========================================================================
RESENA_HISTORICA = ['Venangocupet, S.A. fue constituida formalmente el 26 de noviembre de 2012, como parte de la estrategia de '
 'alianzas para el desarrollo de la Faja Petrolífera del Orinoco. Inicialmente, su estructura accionaria estaba '
 'compuesta por un 60% correspondiente a Petróleos de Venezuela, S.A. (PDVSA), a través de la CVP, y un 40% '
 'distribuido entre socios internacionales.',
 'El 26 de octubre de 2023, se registró un hito corporativo cuando los socios internacionales cedieron sus '
 'participaciones accionarias, consolidando el 100% del capital bajo el control de la filial de la CVP. Desde '
 'entonces, la empresa enfoca sus esfuerzos en la optimización operativa y la modernización tecnológica en el '
 'estado Anzoátegui.']

MISION = ('Realizar actividades primarias de hidrocarburos aplicando estrategias y tecnologías de calidad, con personal '
 'competente, motivado y con plena conciencia de seguridad ambiental hacia las personas, los bienes y el entorno. '
 'Su propósito es producir el máximo beneficio posible para la nación, en concordancia con el Plan Estratégico '
 'Socialista (P.E.S) de PDVSA.')

VISION = ('Constituirse como una empresa de referencia por excelencia en el negocio de hidrocarburos, caracterizada por '
 'ser productiva, innovadora y oportuna. Aspirar a impulsar el desarrollo sustentable manteniéndose a la '
 'vanguardia tecnológica para minimizar costos operativos y maximizar la recuperación de reservas.')

VALORES = [('Responsabilidad', 'Compromiso inquebrantable con la seguridad operativa y el bienestar del personal.'),
 ('Excelencia', 'Aplicación sistemática de altos estándares de calidad y rigor técnico en cada proceso.'),
 ('Innovación', 'Fomento del uso de tecnologías de punta para optimizar la gestión integral de la empresa.'),
 ('Sentido Social', 'Contribución activa al desarrollo productivo y la sostenibilidad como pilares operativos.')]

OBJETIVOS_ORG = ['Maximizar la recuperación de reservas de hidrocarburos.',
 'Minimizar los costos operativos y optimizar el uso de todos los recursos.',
 'Impulsar el desarrollo sustentable de las comunidades vecinas mediante el fortalecimiento de las '
 'organizaciones de base y la diversificación económica.',
 'Cumplir con las políticas, leyes, normas, procedimientos y lineamientos corporativos.',
 'Conocer y aplicar las resoluciones, decretos y leyes de la industria del petróleo frente a las operaciones '
 'de la empresa en materia laboral.',
 'Incentivar buenas relaciones interpersonales y laborales entre todos los trabajadores.',
 'Mantener un alto nivel de comunicación y apoyo con el personal e informar acerca de los cambios y/o '
 'acciones de interés social y laboral.',
 'Apoyar los objetivos y las metas de la organización en armonía con el desarrollo profesional del empleado.',
 'Mantener el carácter confidencial de la información operativa y administrativa de la empresa.',
 'Brindar los beneficios contractuales y velar por las mejoras de las condiciones laborales y la calidad de '
 'vida de los trabajadores.',
 'Producir el máximo beneficio posible para sus accionistas, trabajadores, comunidades vecinas y clientes.']

OBJETIVO_GENERAL_EMPRESA = 'Maximizar la recuperación de reservas de hidrocarburos.'

OBJETIVOS_ESPECIFICOS_EMPRESA = ['Minimizar los costos operativos y optimizar el uso de todos los recursos.',
 'Impulsar el desarrollo sustentable de las comunidades vecinas mediante el fortalecimiento de las '
 'organizaciones de base y la diversificación económica.',
 'Cumplir con las políticas, leyes, normas, procedimientos y lineamientos corporativos.',
 'Conocer y aplicar las resoluciones, decretos y leyes de la industria del petróleo frente a las operaciones '
 'de la empresa en materia laboral.',
 'Incentivar buenas relaciones interpersonales y laborales entre todos los trabajadores.',
 'Mantener un alto nivel de comunicación y apoyo con el personal e informar acerca de los cambios y/o '
 'acciones de interés social y laboral.',
 'Apoyar los objetivos y las metas de la organización en armonía con el desarrollo profesional del empleado.',
 'Mantener el carácter confidencial de la información operativa y administrativa de la empresa.',
 'Brindar los beneficios contractuales y velar por las mejoras de las condiciones laborales y la calidad de '
 'vida de los trabajadores.',
 'Producir el máximo beneficio posible para sus accionistas, trabajadores, comunidades vecinas y clientes.']

UBICACION = ('La Empresa Mixta Petrolera Venangocupet, S.A. se ubica en la Avenida Jesús Subero (vía El Tigre - San José de '
 'Guanipa), con prolongación de la Calle 19 Sur, sector San Remo, Centro Comercial San Remo Mall, El Tigre, '
 'municipio Simón Rodríguez, estado Anzoátegui. Las oficinas administrativas se encuentran específicamente en la '
 'planta baja del centro comercial, identificadas como Local 89-PB. Para la representación cartográfica se '
 'utiliza como referencia el Centro Comercial San Remo Mall, debido a que la empresa no aparece rotulada de forma '
 'independiente en la plataforma cartográfica consultada.')

POBLACION_TABLA = [('Departamento de Presidencia', 'Presidente', 0, 1, 1),
 ('Departamento de Presidencia', 'Secretaría', 1, 0, 1),
 ('TOTAL GENERAL', '', 1, 1, 2)]

POBLACION_FUENTE = ('Información suministrada por el Departamento de Presidencia de la Empresa Mixta Petrolera Venangocupet, S.A. '
 '(2026).')

POBLACION = ['El Departamento de Presidencia cuenta con una fuerza laboral activa de dos (2) personas: el Presidente, de '
 'género masculino, y una persona responsable de Secretaría, de género femenino. Para el momento de las pasantías '
 'no se reportaron vacantes en esta unidad. Esta población corresponde al departamento donde se ejecutaron las '
 'actividades de pasantía y es la directamente vinculada con el flujo documental analizado.']

ORGANIGRAMA_TEXTO = ('La estructura organizativa de Venangocupet, S.A. responde a un esquema jerárquico-funcional encabezado por la '
 'Junta Directiva y la Presidencia. El Departamento de Presidencia constituye el área donde se desarrollaron las '
 'pasantías y actúa como punto de recepción, revisión, firma y despacho de correspondencia ejecutiva. A '
 'continuación se presentan el organigrama general de la empresa y el organigrama específico del departamento.')

MOSTRAR_NIVELES_DIAGNOSTICO = False

DESCRIPCION_DEPARTAMENTO = ('El Departamento de Presidencia fue el área donde se desarrollaron las pasantías y funciona como punto '
 'de recepción, revisión, firma y despacho de correspondencia ejecutiva. El flujo observado comprende la recepción '
 'externa del documento, la revisión ortográfica y de formato, el registro de ingreso, la entrega al Presidente para '
 'firma, el registro de egreso y el despacho al departamento de destino. La práctica también incluyó el registro y '
 'actualización de expedientes, la revisión y canalización de correspondencia y la elaboración de reportes.')

# ========================================================================
# 5. CAPÍTULO II — DIAGNÓSTICO SITUACIONAL
# ========================================================================
SITUACION_PROBLEMATICA = [{'titulo': 'Nivel macro',
  'parrafos': ['En las organizaciones que movilizan documentos entre distintas unidades, el control oportuno '
               'de cada ingreso, revisión, firma y despacho resulta necesario para conservar la continuidad '
               'de los procesos administrativos. Cuando estos movimientos se registran mediante operaciones '
               'manuales repetitivas, aumenta la posibilidad de inconsistencias y se requiere mayor tiempo '
               'para consolidar información destinada a la toma de decisiones.']},
 {'titulo': 'Nivel meso',
  'parrafos': ['En las unidades administrativas vinculadas con la alta dirección, la gestión documental '
               'exige registrar con precisión el recorrido de expedientes que requieren revisión, '
               'validación, firma y posterior canalización hacia otras dependencias. La ausencia de '
               'herramientas que centralicen el seguimiento puede dificultar la consulta inmediata del '
               'estado de cada documento y la preparación de reportes gerenciales cuando coinciden varios '
               'movimientos en un mismo período.']},
 {'titulo': 'Nivel micro',
  'parrafos': ['Dentro de la Empresa Mixta Petrolera Venangocupet, S.A., el Departamento de Presidencia '
               'funciona como un nodo de tránsito y validación de expedientes. El flujo real comprende la '
               'recepción externa del documento, revisión ortográfica y de formato, registro de ingreso, '
               'entrega al Presidente para firma, registro de egreso y despacho al departamento de destino. '
               'La unidad no genera ni conserva de manera permanente los expedientes que recibe, por lo que '
               'la trazabilidad depende de la calidad del registro de cada movimiento.',
               'Actualmente, este control se realiza mediante hojas de cálculo. En períodos de mayor '
               'concurrencia documental, el copiado y pegado de datos repetitivos ralentiza el procesamiento '
               'y puede originar duplicación de información u omisión de movimientos. Del mismo modo, cuando '
               'la alta dirección solicita un resumen mensual de documentos firmados o el estado de '
               'expedientes pendientes, el personal debe filtrar y consolidar manualmente los registros '
               'existentes.']},
 {'titulo': 'Técnica empleada para el diagnóstico',
  'parrafos': ['Como técnica de análisis de la situación se estructuró un árbol del problema a partir de la '
               'observación directa del flujo documental y de la revisión de los registros utilizados por el '
               'departamento. El problema central se relaciona con la limitada automatización del control '
               'documental; entre sus causas se encuentran la transcripción repetitiva, la ausencia de '
               'validaciones automáticas y la dispersión del seguimiento en hojas de cálculo, mientras que '
               'sus efectos se reflejan en demoras de registro, dificultad para obtener reportes inmediatos '
               'y menor trazabilidad del recorrido de los expedientes.']}]

INTERROGANTE_TITULO = 'Interrogante orientadora'

INTERROGANTE_PROBLEMA = ('¿De qué manera puede desarrollarse un sistema automatizado que mejore el control, la trazabilidad y la '
 'generación de reportes de los movimientos documentales en el Departamento de Presidencia de Venangocupet, S.A.?')

OBJETIVO_GENERAL = ('Desarrollar un prototipo de sistema automatizado para el control, trazabilidad y reporte de movimientos '
 'documentales en la Presidencia de la Empresa Mixta Petrolera Venangocupet, S.A.')

OBJETIVOS_ESPECIFICOS = ['Diagnosticar la situación actual del flujo procedimental de recepción, revisión, firma y despacho de '
 'expedientes en el Departamento de Presidencia.',
 'Determinar los requerimientos técnicos y funcionales necesarios para el registro, trazabilidad y generación de '
 'reportes de los movimientos documentales.',
 'Diseñar la arquitectura lógica de la base de datos y la interfaz gráfica del sistema de acuerdo con el flujo '
 'real del Departamento de Presidencia.',
 'Implementar y validar el prototipo funcional mediante SQLite y una aplicación de escritorio, comprobando los '
 'módulos de registro, consulta, historial y reporte.']

PLANIFICACION_DATOS = [('Diagnosticar la situación actual del flujo procedimental de recepción, revisión, firma y despacho de '
  'expedientes en el Departamento de Presidencia.',
  'Flujo procedimental y trazabilidad de los movimientos documentales.',
  'Observar el ciclo real de los expedientes, describir las etapas y analizar los registros existentes.',
  'Observación directa y análisis documental.',
  'Cuaderno de notas y registros de la hoja de cálculo utilizada en el departamento.'),
 ('Determinar los requerimientos técnicos y funcionales necesarios para el registro, trazabilidad y generación de '
  'reportes de los movimientos documentales.',
  'Requerimientos técnicos y funcionales del sistema.',
  'Levantar los datos requeridos, reglas de validación, consultas y reportes necesarios para el control '
  'documental.',
  'Entrevista no estructurada y revisión documental.',
  'Formato de requerimientos, notas de trabajo y diccionario de datos.'),
 ('Diseñar la arquitectura lógica de la base de datos y la interfaz gráfica del sistema de acuerdo con el flujo '
  'real del Departamento de Presidencia.',
  'Arquitectura lógica e interfaz del sistema documental.',
  'Modelar la relación entre procesos y documentos, normalizar la estructura de datos y diseñar los módulos '
  'visuales.',
  'Modelado de datos y diseño de interfaz.',
  'Herramientas de modelado, editor de código y documentación técnica.'),
 ('Implementar y validar el prototipo funcional mediante SQLite y una aplicación de escritorio, comprobando los '
  'módulos de registro, consulta, historial y reporte.',
  'Prototipo funcional para el control y reporte documental.',
  'Implementar la base de datos en SQLite, integrar la interfaz de escritorio y ejecutar pruebas funcionales de '
  'los módulos.',
  'Desarrollo de software y pruebas funcionales.',
  'SQLite, Wails, editor de código y equipo informático.')]

CRONOGRAMA_DATOS = [('Diagnóstico del flujo documental y levantamiento de requerimientos.',
  [True, False, False, False, False, False, False, False, False]),
 ('Diseño del modelo relacional, normalización y diccionario de datos.',
  [False, True, False, False, False, False, False, False, False]),
 ('Implementación de la base de datos relacional en SQLite.',
  [False, False, True, False, False, False, False, False, False]),
 ('Desarrollo de la interfaz gráfica y módulos de consulta e historial.',
  [False, False, False, True, True, False, False, False, False]),
 ('Empaquetado de la aplicación de escritorio con Wails.',
  [False, False, False, False, False, True, False, False, False]),
 ('Pruebas funcionales y depuración del prototipo.',
  [False, False, False, False, False, False, True, False, False]),
 ('Documentación técnica, manual de usuario e informe académico.',
  [False, False, False, False, False, False, False, True, False]),
 ('Validación final, ajustes y presentación del prototipo.',
  [False, False, False, False, False, False, False, False, True]),
 ('Inducción institucional y capacitación en seguridad (SIAHO).',
  [True, False, False, True, False, False, False, False, False]),
 ('Registro y actualización de expedientes en hoja de cálculo.',
  [False, True, True, False, False, False, False, False, False]),
 ('Revisión y canalización de correspondencia presidencial.',
  [False, False, False, False, True, True, False, False, False]),
 ('Apoyo en generación de reportes y actividades de cierre.',
  [False, False, False, False, False, False, True, True, True])]

# ========================================================================
# 6. CAPÍTULO III — MARCO TEÓRICO
# ========================================================================
BASES_TEORICAS = [{'titulo': 'Sistemas de Información',
  'posicion_autor': 'Desde la perspectiva del autor, el sistema desarrollado debe priorizar información confiable '
                    'y oportuna para apoyar el control de los movimientos documentales de Presidencia.',
  'parrafos': ['Un sistema de información constituye un conjunto organizado de recursos humanos, tecnológicos y '
               'procedimentales orientados a la captura, almacenamiento, procesamiento y distribución de datos '
               'con el propósito de apoyar la toma de decisiones dentro de una organización. Laudon y Laudon '
               '(2016) distinguen entre sistemas de procesamiento de transacciones, sistemas de soporte a la '
               'decisión y sistemas de información gerencial, siendo estos últimos los que transforman datos '
               'operativos en reportes consolidados de utilidad directiva.',
               'En el contexto del presente proyecto, el sistema propuesto se enmarca en la categoría de sistema '
               'de información operacional con capacidad de reporte gerencial, dado que registra cada movimiento '
               'documental de forma transaccional y provee resúmenes inmediatos al nivel de presidencia. Según '
               'Kendall y Kendall (2011), el análisis y diseño de sistemas busca comprender sistemáticamente cómo '
               'interactúan los datos y los usuarios para proponer soluciones tecnológicas que mejoren el flujo '
               'de trabajo de una organización.'],
  'cita_larga': {'texto': 'Los sistemas de información gerencial proporcionan a los administradores informes '
                          'sobre el desempeño actual de la organización. Esta información se utiliza para '
                          'supervisar y controlar el negocio y predecir el desempeño futuro. Los sistemas de '
                          'información gerencial resumen y reportan las operaciones básicas de la empresa usando '
                          'datos suministrados por los sistemas de procesamiento de transacciones.',
                 'autor': '(Laudon y Laudon, 2016, p. 46)'},
  'post_cita': ''},
 {'titulo': 'Gestión Documental',
  'posicion_autor': 'En Venangocupet, la gestión documental debe reflejar el recorrido real de cada expediente, '
                    'desde su recepción hasta su despacho, sin agregar pasos que no correspondan al proceso.',
  'parrafos': ['La gestión documental se define como el conjunto de normas, técnicas y prácticas que regulan el '
               'ciclo de vida de los documentos dentro de una organización, desde su creación o recepción hasta '
               'su disposición final. Cruz Mundet (2011) señala que una gestión documental eficaz garantiza la '
               'autenticidad, integridad, fiabilidad y disponibilidad de la información registrada, constituyendo '
               'un pilar fundamental para la transparencia administrativa y la continuidad operativa.',
               'En el Departamento de Presidencia de Venangocupet, S.A., el flujo documental responde a un ciclo '
               'específico: recepción del expediente externo, revisión de forma, registro de ingreso, firma '
               'presidencial, registro de egreso y despacho al departamento destinatario. La automatización de '
               'este ciclo mediante un sistema digitalizado reduce la propensión al error humano y dota al '
               'departamento de un historial auditable de cada movimiento, en concordancia con los principios de '
               'gestión documental descritos por Cruz Mundet (2011).'],
  'cita_larga': None,
  'post_cita': ''},
 {'titulo': 'Modelo Relacional de Bases de Datos',
  'posicion_autor': 'A juicio de quien suscribe, el modelo relacional resulta adecuado porque representa la '
                    'relación entre procesos y documentos sin duplicar la información que se necesita consultar.',
  'parrafos': ['El modelo relacional, propuesto originalmente por Codd (1970), organiza la información en tablas '
               'bidimensionales denominadas relaciones, cuyos atributos representan las propiedades de las '
               'entidades y cuyas filas corresponden a instancias individuales de datos. La fortaleza de este '
               'modelo radica en la aplicación de reglas de normalización que eliminan la redundancia y preservan '
               'la integridad referencial entre tablas relacionadas mediante claves primarias y foráneas.',
               'Date (2001) establece que un diseño relacional correctamente normalizado garantiza que cada dato '
               'se almacene una sola vez, reduciendo la posibilidad de inconsistencias derivadas de '
               'actualizaciones parciales. En el sistema propuesto, la relación entre procesos administrativos y '
               'documentos sigue una cardinalidad uno a muchos (1:N), permitiendo registrar múltiples expedientes '
               'asociados a un mismo proceso contractual o administrativo sin duplicar los datos maestros del '
               'proceso.'],
  'cita_larga': None,
  'post_cita': ''},
 {'titulo': 'SQLite como Sistema Gestor de Base de Datos',
  'posicion_autor': 'La selección de SQLite se fundamenta en su portabilidad, sencillez de despliegue y capacidad '
                    'para mantener la información del prototipo en un archivo relacional único, características '
                    'adecuadas para una aplicación de escritorio de alcance departamental.',
  'parrafos': ['SQLite es un motor de base de datos relacional de código abierto, autocontenido y sin servidor, '
               'cuya arquitectura embebida lo diferencia de sistemas cliente-servidor convencionales. Su '
               'funcionamiento se basa en un único archivo que aloja el esquema y los registros de la base de '
               'datos, reduciendo la complejidad de administración para aplicaciones locales.',
               'Pressman (2010) señala que la selección de herramientas tecnológicas debe considerar las '
               'características del entorno de despliegue y los requerimientos reales de la solución. Para el '
               'prototipo desarrollado en el Departamento de Presidencia, SQLite permite gestionar las relaciones '
               'entre procesos y documentos, conservar el historial de movimientos y ejecutar consultas sin '
               'incorporar una infraestructura adicional de servidor.'],
  'cita_larga': None,
  'post_cita': ''},
 {'titulo': 'Trazabilidad Documental',
  'posicion_autor': 'Para este proyecto, la trazabilidad es el elemento que permite demostrar qué ocurrió con '
                    'cada expediente y ofrecer respuestas verificables a la dirección de la empresa.',
  'parrafos': ['La trazabilidad documental se entiende como la capacidad de reconstruir el historial completo de '
               'un documento a lo largo de su ciclo de vida, identificando en cada etapa el responsable, la '
               'fecha, la acción ejecutada y el estado resultante. Gómez (2019) señala que la trazabilidad '
               'constituye el mecanismo central de auditoría en los sistemas de gestión documental, dado que '
               'permite verificar la integridad del proceso y detectar cuellos de botella o irregularidades en el '
               'flujo.',
               'En el ámbito de la alta dirección, la trazabilidad cobra especial relevancia porque los '
               'expedientes que transitan por la Presidencia frecuentemente están vinculados a procesos '
               'contractuales y decisiones gerenciales de impacto organizacional. El sistema propuesto registra '
               'automáticamente cada movimiento de ingreso y egreso del expediente, almacenando la fecha, el '
               'estatus y el departamento de origen o destino, lo que permite generar reportes de trazabilidad de '
               'forma inmediata ante cualquier requerimiento directivo.'],
  'cita_larga': {'texto': 'Un sistema de información eficaz proporciona a los administradores de la organización '
                          'datos precisos y oportunos, facilitando la auditoría de cada transacción operativa y '
                          'mejorando sustancialmente la capacidad de respuesta ante requerimientos gerenciales de '
                          'alto nivel. La ausencia de este tipo de herramientas obliga al personal a invertir '
                          'tiempo considerable en la búsqueda y consolidación manual de información que debería '
                          'estar disponible de forma inmediata.',
                 'autor': '(Gómez, 2019, p. 45)'},
  'post_cita': ''},
 {'titulo': 'Automatización de Procesos Administrativos',
  'posicion_autor': 'Desde la posición del autor, automatizar el registro y los reportes permite disminuir tareas '
                    'repetitivas y dedicar mayor atención a la revisión y canalización de los expedientes.',
  'parrafos': ['La automatización de procesos administrativos consiste en la sustitución de tareas manuales '
               'repetitivas por flujos de trabajo controlados por sistemas informáticos, con el objetivo de '
               'reducir los tiempos de ejecución, minimizar el error humano y liberar al personal para '
               'actividades de mayor valor analítico. Laudon y Laudon (2016) plantean que la automatización de '
               'procesos de negocio genera mejoras medibles en la productividad organizacional al estandarizar '
               'los procedimientos y centralizar el control de la información.',
               'En el Departamento de Presidencia de Venangocupet, S.A., la automatización se justifica por la '
               'naturaleza del proceso actual: el personal destina un porcentaje significativo de su tiempo '
               'operativo al copiado y pegado de datos entre documentos y hojas de cálculo, así como a la '
               'redacción manual de resúmenes solicitados por la dirección. La implementación del sistema '
               'automatizado propuesto traslada estas tareas al software, permitiendo que el personal se '
               'concentre en las funciones de revisión y coordinación propias del departamento.'],
  'cita_larga': None,
  'post_cita': ''},
 {'titulo': 'Proyecto Factible como Modalidad de Investigación',
  'posicion_autor': 'La modalidad de proyecto factible resulta compatible con el trabajo realizado porque el '
                    'diagnóstico del flujo documental condujo al diseño, construcción y validación de un '
                    'prototipo orientado a una necesidad concreta del Departamento de Presidencia.',
  'parrafos': ['La Universidad Pedagógica Experimental Libertador (UPEL, 2016) define el proyecto factible como '
               'la investigación, elaboración y desarrollo de una propuesta de un modelo operativo viable para '
               'solucionar problemas, requerimientos o necesidades de organizaciones o grupos sociales. Esta '
               'modalidad exige la comprobación de la viabilidad técnica, económica y operativa de la solución '
               'planteada, sustentada en un diagnóstico de campo que evidencie la situación deficitaria que da '
               'origen a la propuesta.',
               'Arias (2012) complementa esta definición señalando que el proyecto factible no se limita a '
               'diagnosticar un problema, sino que avanza hasta proponer y en muchos casos desarrollar la '
               'solución, demostrando su aplicabilidad en el contexto real. El presente trabajo se enmarca en '
               'esta modalidad al partir de un diagnóstico situacional del flujo documental en Presidencia, '
               'proponer una arquitectura tecnológica específica y materializar un prototipo funcional del '
               'sistema como evidencia de la viabilidad de la propuesta.'],
  'cita_larga': None,
  'post_cita': ''}]

POST_CITA_TEXTO = ''

# ========================================================================
# 7. CAPÍTULO IV — ACTIVIDADES REALIZADAS
# ========================================================================
ACTIVIDADES_DESCRIPCION = ('Durante las nueve (9) semanas de práctica profesional se ejecutaron actividades operativas propias del '
 'Departamento de Presidencia y actividades técnicas vinculadas con el diagnóstico, diseño, implementación y '
 'validación del sistema automatizado:')

ACTIVIDADES_LISTA = [{'semana': 1,
  'operativa': 'Inducción institucional, recorrido por las instalaciones del área administrativa, presentación '
               'del equipo de trabajo y revisión de los lineamientos generales de funcionamiento del Departamento '
               'de Presidencia.',
  'investigacion': 'Observación directa y mapeo del ciclo real de los documentos en Presidencia, identificación '
                   'de fallas en el registro manual y levantamiento inicial de los datos requeridos para la '
                   'trazabilidad.'},
 {'semana': 2,
  'operativa': 'Clasificación y registro manual de expedientes físicos en la hoja de cálculo utilizada por la '
               'oficina, con actualización de los movimientos correspondientes a los documentos recibidos durante '
               'el período.',
  'investigacion': 'Validación de requerimientos con el tutor industrial, construcción del diagrama '
                   'Entidad-Relación, normalización del esquema propuesto y elaboración del diccionario de '
                   'datos.'},
 {'semana': 3,
  'operativa': 'Procesamiento y actualización del estatus de expedientes en el archivo de control de la oficina, '
               'apoyando el seguimiento de los documentos recibidos y despachados durante la semana.',
  'investigacion': 'Implementación de la estructura relacional en SQLite, carga de registros de prueba, '
                   'construcción de formularios de captura y programación de consultas de trazabilidad.'},
 {'semana': 4,
  'operativa': 'Asistencia a la charla técnica sobre Identificación y Notificación de Peligros y Riesgos en '
               'Instalaciones y Puestos de Trabajo dictada por el departamento de SIAHO, junto con labores '
               'regulares de registro documental.',
  'investigacion': 'Programación del entorno visual de escritorio, estructuración de los módulos de la interfaz y '
                   'organización del código fuente del prototipo.'},
 {'semana': 5,
  'operativa': 'Revisión ortográfica y de formato de correspondencia presidencial, y apoyo en la canalización de '
               'expedientes hacia su departamento de destino después de la firma presidencial.',
  'investigacion': 'Desarrollo de los módulos de consulta e historial de movimientos e integración de la '
                   'visualización de expedientes asociados a cada proceso administrativo.'},
 {'semana': 6,
  'operativa': 'Colaboración en la revisión y despacho de correspondencia presidencial y apoyo en el registro de '
               'salida de expedientes firmados durante el período.',
  'investigacion': 'Empaquetado de la aplicación de escritorio mediante Wails, integración del entorno visual y '
                   'generación de un ejecutable autónomo para las pruebas funcionales del prototipo.'},
 {'semana': 7,
  'operativa': 'Apoyo en la elaboración manual de resúmenes de estatus de expedientes solicitados por la alta '
               'dirección a partir de los registros disponibles en la hoja de cálculo.',
  'investigacion': 'Ejecución de pruebas funcionales, depuración de errores y verificación de los módulos de '
                   'registro, trazabilidad, consulta e informes utilizando datos de prueba representativos del '
                   'flujo departamental.'},
 {'semana': 8,
  'operativa': 'Participación en las actividades regulares del Departamento de Presidencia y apoyo en la '
               'organización y seguimiento de los expedientes correspondientes al período.',
  'investigacion': 'Redacción del informe de pasantías, elaboración del manual de usuario y organización técnica '
                   'del código fuente y los entregables del prototipo.'},
 {'semana': 9,
  'operativa': 'Presentación del prototipo funcional ante la tutora industrial para su evaluación, recepción de '
               'observaciones y gestión de los recaudos correspondientes al cierre de la pasantía.',
  'investigacion': 'Consolidación y revisión del informe académico, incorporación de las observaciones recibidas '
                   'y preparación de los anexos definitivos para la entrega institucional.'}]

# ========================================================================
# 8. CAPÍTULO V — CONCLUSIONES Y RECOMENDACIONES
# ========================================================================
CONCLUSIONES = ['Se diagnosticó que el control manual en hojas de cálculo puede generar cuellos de botella cuando aumenta la '
 'concurrencia de expedientes, debido a la repetición de datos y a la ausencia de validaciones automáticas que '
 'faciliten el seguimiento del recorrido documental.',
 'Se determinaron como requerimientos esenciales del sistema el registro de ingreso y egreso de expedientes, la '
 'asociación de múltiples documentos con un mismo proceso, la consulta del historial de movimientos y la '
 'generación de reportes resumidos para la Presidencia.',
 'Se diseñó una arquitectura relacional normalizada con SQLite y una interfaz de escritorio orientada a conservar '
 'una dinámica de uso sencilla, representando la relación uno a muchos entre procesos y documentos sin alterar el '
 'flujo operativo del departamento.',
 'Se implementó y validó un prototipo funcional que integra los módulos de registro, consulta, historial y '
 'reporte, demostrando la viabilidad técnica de automatizar el control documental y reducir la dependencia de '
 'operaciones manuales repetitivas.']

RECOMENDACIONES = ['Incorporar progresivamente al sistema los registros históricos que deban conservarse para consulta, verificando '
 'previamente la integridad de la información antes de su migración.',
 'Capacitar al personal del Departamento de Presidencia en el uso de los módulos de registro, consulta, historial '
 'y generación de reportes, utilizando ejemplos del flujo cotidiano de expedientes.',
 'Establecer una rutina periódica de respaldo del archivo de base de datos en una ubicación segura y definida por '
 'la organización, con el fin de preservar la continuidad del historial documental.',
 'Evaluar en fases posteriores la incorporación de nuevas funciones únicamente cuando respondan a necesidades '
 'reales del flujo de Presidencia, evitando agregar pasos que compliquen el proceso actual.']

# ========================================================================
# 9. REFERENCIAS Y ANEXOS
# ========================================================================
REFERENCIAS_LISTA = ['Arias, F. (2012). El proyecto de investigación: Introducción a la metodología científica (6ta ed.). Episteme, '
 'Venezuela.',
 'Codd, E. F. (1970). A relational model of data for large shared data banks. Communications of the ACM, 13(6), '
 '377-387.',
 'Cruz Mundet, J. R. (2011). Administración de documentos y archivos: Textos fundamentales. Coordinadora de '
 'Asociaciones de Archiveros, España.',
 'Date, C. J. (2001). Introducción a los sistemas de bases de datos (7ma ed.). Pearson Educación, México.',
 'Gómez, R. (2019). Gestión Documental y Sistemas. Editorial Trillas, México.',
 'Kendall, K., y Kendall, J. (2011). Análisis y diseño de sistemas (8va ed.). Pearson Educación, México.',
 'Laudon, K., y Laudon, J. (2016). Sistemas de información gerencial (14va ed.). Pearson Educación, México.',
 'Pressman, R. (2010). Ingeniería de Software: Un enfoque práctico (7ma ed.). McGraw-Hill, México.',
 'Universidad Pedagógica Experimental Libertador. (2016). Manual de trabajos de grado de especialización y '
 'maestría y tesis doctorales (5ta ed.). FEDUPEL, Venezuela.']

ANEXOS_LISTA = [
    ('ANEXO A', 'Árbol del problema del control de movimientos documentales', 3, {'width_cm': 11.0, 'height_cm': 13.5})
]
