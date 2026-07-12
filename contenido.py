# contenido.py
# ================================================================
#  MÓDULO DE CONTENIDO ACADÉMICO PARA EL INFORME DE PASANTÍAS
#  (Por defecto: Proyecto de Juliano Cardona - Venangocupet, S.A.)
# ================================================================

# 1. Rutas y Carpetas
CARPETA_IMAGENES = "juliano"  # Se asume que las imágenes del proyecto están en la carpeta juliano

# 2. Datos de Portada y Datos Personales
MEMBRETE = [
    "REPÚBLICA BOLIVARIANA DE VENEZUELA",
    "MINISTERIO DEL PODER POPULAR PARA LA EDUCACIÓN",
    "INSTITUTO UNIVERSITARIO DE TECNOLOGÍA",
    "\"ELÍAS CALIXTO POMPA\" (IUTECP)",
    "EL TIGRE, ESTADO ANZOÁTEGUI"
]

TITULO_PROYECTO = "DISEÑO DE UN SISTEMA PARA EL CONTROL, TRAZABILIDAD Y REPORTE DE MOVIMIENTOS DOCUMENTALES EN LA PRESIDENCIA DE LA EMPRESA MIXTA PETROLERA VENANGOCUPET, S.A."

# Cada elemento de la lista es una línea que aparece en el bloque del autor.
# Las cadenas vacías ('') generan una línea en blanco de separación.
AUTOR_DATOS = [
    "Autor: Cardona, Juliano",
    "C.I.: 32.281.199",
    "",
    "Tutor Industrial: Ing. Yasmin Sabaneta",
    "C.I.: 14.187.924",
    "",
    "Tutor Académico: Lic. Carlos Mendoza"
]

FECHA_LUGAR = "El Tigre, julio de 2026"

RAZON_SOCIAL = "Empresa Mixta Petrolera Venangocupet, S.A."

# 3. Páginas Preliminares
DEDICATORIA = "A mis padres, por su apoyo incondicional en cada paso de mi formación académica y personal."
AGRADECIMIENTOS = "A la Empresa Mixta Petrolera Venangocupet, S.A., por abrirme sus puertas y brindarme la oportunidad de desarrollar este proyecto técnico."
RESUMEN_TEXTO = (
    "El presente informe describe el diseño de un sistema automatizado para el control, trazabilidad "
    "y reporte de movimientos documentales en la presidencia de la Empresa Mixta Petrolera Venangocupet, S.A. "
    "La investigación se enmarca en la modalidad de proyecto tecnológico apoyado en un diagnóstico de campo, "
    "donde se identificaron las demoras operativas, pérdida de trazabilidad y riesgos en la integridad "
    "física de los expedientes. El sistema propuesto incluye modelado lógico de datos, diagramas de "
    "flujo de información y prototipos de interfaces que garantizan un registro inmutable de cada transacción, "
    "optimizando la toma de decisiones por la alta gerencia."
)
PALABRAS_CLAVE = "sistema, trazabilidad, petrolera, IUTECP, pasantías."

INTRODUCCION_TEXTO = (
    "La presente pasantía realizada en la Empresa Mixta Petrolera Venangocupet, S.A., tiene como propósito "
    "diseñar un sistema para el control, trazabilidad y reporte de movimientos documentales en la presidencia "
    "de la empresa, contribuyendo al fortalecimiento de los procesos administrativos y operativos de la organización."
)

# 4. CAPÍTULO I - Realidad Organizacional
IDENTIFICACION_EMPRESA = (
    "La Empresa Mixta Petrolera Venangocupet, S.A., es una organización estratégica encargada de la "
    "exploración, extracción y comercialización de hidrocarburos en la Faja Petrolífera del Orinoco. Como filial "
    "de la corporación nacional, se enfoca en optimizar los recursos energéticos del país."
)

RESENA_HISTORICA = [
    "Fundada en el año 2010 como una alianza estratégica internacional para maximizar la producción petrolera regional, "
    "Venangocupet ha consolidado una infraestructura técnica robusta y un equipo multidisciplinario altamente calificado "
    "en la gestión de hidrocarburos, adaptándose progresivamente a las exigencias normativas del sector.",
    "A lo largo de su evolución institucional, la empresa ha optimizado sus líneas de operaciones de campo y sus procesos "
    "de soporte administrativo, integrando tecnologías avanzadas para asegurar el control de sus operaciones "
    "financieras, técnicas y operativas."
]

MISION = (
    "Contribuir eficazmente al desarrollo energético de la nación mediante operaciones seguras, eficientes "
    "y sustentables en la exploración y producción de crudo, a través del talento humano comprometido con la excelencia."
)

VISION = (
    "Ser la empresa mixta líder y de referencia nacional e internacional en la producción de hidrocarburos, "
    "reconocida por sus altos estándares técnicos, innovación tecnológica y responsabilidad socioambiental."
)

VALORES = [
    ("Responsabilidad", "Garantizar la ejecución oportuna y segura de las operaciones petroleras y administrativas."),
    ("Integridad", "Proceder con ética y transparencia en la administración de los recursos del Estado."),
    ("Calidad", "Asegurar la excelencia operativa y técnica en cada fase del proceso productivo y de gestión."),
    ("Compromiso", "Dedicación plena hacia los objetivos corporativos y el desarrollo sustentable de la región.")
]

OBJETIVOS_ORG = [
    "Maximizar la eficiencia operativa en la producción de crudo de la organización.",
    "Garantizar el cumplimiento riguroso de las normativas de seguridad industrial y protección ambiental.",
    "Optimizar los procesos administrativos internos para asegurar una toma de decisiones gerenciales oportuna."
]

UBICACION = "Av. Intercomunal, Complejo de Oficinas Administrativas Venangocupet, El tigre, Estado Anzoátegui."

POBLACION = [
    "La población laboral del complejo administrativo de Venangocupet, S.A., consta de personal administrativo de presidencia, "
    "analistas de operaciones, planificadores y técnicos de campo, coordinados de manera vertical para garantizar la "
    "continuidad operativa de la corporación.",
    "El área de presidencia actúa como el núcleo de toma de decisiones corporativas y de coordinación interdepartamental, "
    "siendo indispensable una gestión altamente eficiente y trazable de todo su flujo de documentos."
]

ORGANIGRAMA_TEXTO = "La estructura organizativa de la empresa Venangocupet es vertical y se detalla en el organigrama general de la organización:"

# 5. CAPÍTULO II - Diagnóstico Situacional
SITUACION_PROBLEMATICA = [
    "Durante las actividades en la Presidencia de la Empresa Mixta Petrolera Venangocupet, S.A., se detectó que el "
    "control de movimientos documentales (oficios, contratos, memorandos, minutas y correspondencia en general) se "
    "realiza de forma manual y dispersa, utilizando herramientas no centralizadas de oficina.",
    "Esta falta de automatización y centralización genera retrasos considerables en la recuperación de información, "
    "pérdida de trazabilidad en las autorizaciones y riesgo de extravío de documentos críticos, afectando la "
    "eficiencia en la toma de decisiones por parte de la alta gerencia ante entes reguladores."
]

OBJETIVO_GENERAL = (
    "Diseñar un sistema para el control, trazabilidad y reporte de movimientos documentales en la presidencia "
    "de la Empresa Mixta Petrolera Venangocupet, S.A., con el propósito de optimizar la gestión de la información, "
    "garantizar la seguridad de los archivos y mejorar la eficiencia de los procesos administrativos de la organización."
)

OBJETIVOS_ESPECIFICOS = [
    "Diagnosticar el proceso de control de correspondencia actual en el área de presidencia de la empresa para identificar cuellos de botella.",
    "Determinar los requerimientos técnicos y funcionales necesarios para el desarrollo del nuevo sistema de control.",
    "Diseñar la estructura lógica del sistema y modelar la base de datos para la trazabilidad y reportes en tiempo real."
]

PLANIFICACION_DATOS = [
    (
        "Diagnosticar la situación actual de los movimientos documentales en presidencia.",
        "Entrevistas y observación directa de flujos documentales.",
        "Guía de observación, PC, notas.",
        "Mapeo situacional elaborado."
    ),
    (
        "Determinar los requerimientos del nuevo sistema.",
        "Análisis de procesos internos y formatos vigentes.",
        "Plantillas de requerimientos, ERS.",
        "Documento de requerimientos validado."
    ),
    (
        "Diseñar la estructura lógica del sistema y modelar base de datos.",
        "Diseño de diagramas de flujo y modelado de datos.",
        "CASE tools, draw.io, PC.",
        "Diseño de base de datos aprobado."
    )
]

CRONOGRAMA_DATOS = [
    ("Reconocimiento del departamento administrativo.",       [True,  False, False, False, False]),
    ("Levantamiento de información preliminar de procura.",   [True,  True,  False, False, False]),
    ("Entrevistas al personal sobre cuellos de botella.",     [False, True,  True,  False, False]),
    ("Análisis y diagnóstico situacional.",                   [False, False, True,  True,  False]),
    ("Propuesta de optimización y formatos.",                 [False, False, False, True,  True ]),
    ("Presentación final de la propuesta.",                   [False, False, False, False, True ])
]

# 6. CAPÍTULO III - Marco Teórico
BASES_TEORICAS_PARRAFOS = [
    "Según Pérez (2020), la trazabilidad documental es fundamental para el control eficiente de los procesos "
    "administrativos en las organizaciones, permitiendo el rastreo histórico y auditable de cada expediente.",
    "La gestión documental en las organizaciones modernas no solo implica el almacenamiento pasivo de archivos, "
    "sino la garantía activa de que cada movimiento y alteración quede registrada de forma inmutable para auditorías futuras."
]

CITA_LARGA_TEXTO = (
    "La gestión de la información en el entorno petrolero requiere un control estricto de las transacciones "
    "y correspondencia, asegurando la inmutabilidad física y lógica de los expedientes corporativos para "
    "mitigar riesgos legales y mejorar el tiempo de respuesta operativo."
)
CITA_LARGA_AUTOR = "(Gómez, 2019, p. 45)"

# 7. CAPÍTULO IV - Actividades Realizadas
ACTIVIDADES_DESCRIPCION = "Durante las diez semanas de pasantías, se llevaron a cabo actividades de análisis y diseño en la presidencia de la empresa:"
ACTIVIDADES_LISTA = [
    "Semana 1: Inducción institucional y reconocimiento del puesto de trabajo.",
    "Semana 2: Observación del flujo físico de los contratos y correspondencias.",
    "Semana 3: Diseño de cuestionario y entrevistas para el personal administrativo.",
    "Semana 4: Aplicación del cuestionario y tabulación de respuestas de la muestra.",
    "Semana 5: Identificación de los principales problemas y causas de demoras.",
    "Semana 6: Diseño lógico de la base de datos y modelado de tablas.",
    "Semana 7: Definición de flujogramas del nuevo proceso de recepción.",
    "Semana 8: Prototipado rápido de interfaces de usuario.",
    "Semana 9: Pruebas del prototipo y recolección de retroalimentación.",
    "Semana 10: Consolidación del informe final de la propuesta."
]

# 8. CAPÍTULO V - Conclusiones y Recomendaciones
CONCLUSIONES = [
    "Se logró estructurar la propuesta del sistema de movimientos documentales que soluciona los problemas de pérdida de trazabilidad.",
    "La propuesta técnica cumple con los requerimientos de seguridad e inmutabilidad exigidos por las directivas de la empresa."
]

RECOMENDACIONES = [
    "Capacitar formalmente al personal en el uso del nuevo protocolo documental sugerido para la presidencia.",
    "Iniciar el desarrollo de software basándose en el diseño de base de datos y prototipos de interfaces elaborados."
]

# 9. Referencias Bibliográficas
REFERENCIAS_LISTA = [
    "Asamblea Nacional. (1999). Constitución de la República Bolivariana de Venezuela. Caracas, La Torre.",
    "Gómez, R. (2019). Gestión Documental en Empresas Petroleras. Editorial Trillas, México.",
    "Pérez, L. (2020). Trazabilidad de Movimientos. Universidad Pedagógica Experimental Libertador."
]

# 10. Anexos
ANEXOS_LISTA = [
    ("ANEXO A", "Definición de Términos Básicos"),
    ("ANEXO B", "Planes de Trabajo"),
    ("ANEXO C", "Memoria Fotográfica")
]
