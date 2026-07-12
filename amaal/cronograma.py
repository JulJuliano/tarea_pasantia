import os
import subprocess
from docx import Document
from docx.shared import Cm, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

# ================================================================
#  DATOS DEL PASANTE (MODIFIQUE ESTOS VALORES CON SUS DATOS)
# ================================================================
PASANTE_NOMBRE = "Alrifaaie Amaal"
PASANTE_CI = "31.985.792"

# ================================================================
#  FUNCIONES DE CONFIGURACIÓN Y FORMATO (ESTÁTICAS - NORMA IUTECP)
# ================================================================

def setup_page(doc):
    """Márgenes Art. 6 (4cm Izquierdo para encuadernación, 3cm los demás)"""
    section = doc.sections[0]
    section.page_width = Cm(21.59)
    section.page_height = Cm(27.94)
    section.left_margin = Cm(4)
    section.right_margin = Cm(3)
    section.top_margin = Cm(3)
    section.bottom_margin = Cm(3)

def add_paragraph_normado(doc, text, bold=False, size=12):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(0)

    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(size)
    run.font.bold = bold
    return p

def add_label_value(doc, label, value):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(2)

    run_l = p.add_run(label)
    run_l.font.name = 'Times New Roman'
    run_l.font.size = Pt(12)
    run_l.font.bold = True

    run_v = p.add_run(value)
    run_v.font.name = 'Times New Roman'
    run_v.font.size = Pt(12)
    return p

def set_cell_format(cell, text, bold=False, size=10, align=WD_ALIGN_PARAGRAPH.LEFT):
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = align
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)

    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(size)
    run.font.bold = bold
    cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER

def remove_table_borders(table):
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else OxmlElement('w:tblPr')
    borders = OxmlElement('w:tblBorders')
    for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'none')
        border.set(qn('w:sz'), '0')
        borders.append(border)
    tblPr.append(borders)

# ================================================================
#  PROCESADOR CORE: COMPILA UNA SEMANA ESPECÍFICA
# ================================================================

def generar_documento_semana(datos):
    doc = Document()
    setup_page(doc)

    # 1. Título Centralizado
    p_titulo = doc.add_paragraph()
    p_titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_titulo.paragraph_format.space_after = Pt(12)
    run_t = p_titulo.add_run("PLAN SEMANAL DE PASANTÍAS")
    run_t.font.name = 'Times New Roman'
    run_t.font.size = Pt(14)
    run_t.font.bold = True

    # 2. Datos Informativos de la Empresa y la Pasante
    add_label_value(doc, "EMPRESA: ", "Ingeniería de Telecomunicaciones, C.A.")
    add_label_value(doc, "DEPARTAMENTO: ", "Departamento de Administración")
    add_label_value(doc, "ESPECIALIDAD: ", "Administración")
    add_label_value(doc, "SEMANA N°: ", datos["num_semana"])
    add_label_value(doc, "PERÍODO: ", datos["periodo"])
    add_label_value(doc, "PASANTE: ", f"{PASANTE_NOMBRE} |  C.I.: {PASANTE_CI}")
#    add_label_value(doc, "TUTOR INDUSTRIAL: ", "[Nombre del Tutor]  |  C.I.: [Cédula]")

    doc.add_paragraph()

    # 3. Objetivo de la semana
    p_obj_t = doc.add_paragraph()
    p_obj_t.paragraph_format.space_after = Pt(4)
    run_ot = p_obj_t.add_run("OBJETIVO DE LA SEMANA:")
    run_ot.font.name = 'Times New Roman'
    run_ot.font.size = Pt(12)
    run_ot.font.bold = True

    add_paragraph_normado(doc, datos["objetivo"])

    doc.add_paragraph()

    # 4. Tabla de Actividades Planificadas (Dimensiones fijas para evitar desbordes)
    p_cuarto_t = doc.add_paragraph()
    p_cuarto_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cuarto_t.paragraph_format.space_after = Pt(6)
    run_ct = p_cuarto_t.add_run(f"CUADRO 1. Actividades Planificadas de la Semana {datos['num_semana']}")
    run_ct.font.name = 'Times New Roman'
    run_ct.font.size = Pt(10)
    run_ct.font.bold = True

    table = doc.add_table(rows=1, cols=4)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.allow_autofit = False

    tblLayout = OxmlElement('w:tblLayout')
    tblLayout.set(qn('w:type'), 'fixed')
    table._tbl.tblPr.append(tblLayout)

    # Encabezados con Sombreado Azul Pastel
    headers = ["Nro", "Actividad", "Descripción", "Recursos"]
    for i, h in enumerate(headers):
        set_cell_format(table.rows[0].cells[i], h, bold=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER)
        shading_elm = OxmlElement('w:shd')
        shading_elm.set(qn('w:fill'), "D9E2F3")
        table.rows[0].cells[i]._tc.get_or_add_tcPr().append(shading_elm)

    # Inyección de actividades semanales
    for nro, act, desc, rec in datos["actividades"]:
        row = table.add_row()
        set_cell_format(row.cells[0], nro, size=10, align=WD_ALIGN_PARAGRAPH.CENTER)
        set_cell_format(row.cells[1], act, size=10, align=WD_ALIGN_PARAGRAPH.LEFT)
        set_cell_format(row.cells[2], desc, size=10, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
        set_cell_format(row.cells[3], rec, size=10, align=WD_ALIGN_PARAGRAPH.LEFT)

    # Ancho total útil: 14.59 cm
    widths = [Cm(1.2), Cm(3.5), Cm(6.5), Cm(3.39)]
    for idx, width in enumerate(widths):
        table.columns[idx].width = width
    for row in table.rows:
        for idx, width in enumerate(widths):
            row.cells[idx].width = width

    doc.add_paragraph()

    # 5. Entregables
    p_ent_t = doc.add_paragraph()
    p_ent_t.paragraph_format.space_after = Pt(4)
    run_et = p_ent_t.add_run("ENTREGABLES DE LA SEMANA:")
    run_et.font.name = 'Times New Roman'
    run_et.font.size = Pt(12)
    run_et.font.bold = True

    add_paragraph_normado(doc, datos["entregables"])

    doc.add_paragraph()

    # 6. Observaciones del Tutor Industrial (Inyección cualitativa real)
    p_obs_t = doc.add_paragraph()
    p_obs_t.paragraph_format.space_after = Pt(4)
    run_ot2 = p_obs_t.add_run("OBSERVACIONES DEL TUTOR INDUSTRIAL:")
    run_ot2.font.name = 'Times New Roman'
    run_ot2.font.size = Pt(12)
    run_ot2.font.bold = True

    add_paragraph_normado(doc, datos["observaciones_tutor"])

#    p_obs = doc.add_paragraph()
#    p_obs.paragraph_format.line_spacing = 1.5
#    run_obs = p_obs.add_run("(Espacio reservado para la evaluación cualitativa del tutor sobre control de procesos, puntualidad, manejo de solicitudes y cumplimiento de directrices contables)")
#    run_obs.font.name = 'Times New Roman'
#    run_obs.font.size = Pt(11)
#    run_obs.font.italic = True

#    for _ in range(4):
#        p_line = doc.add_paragraph()
#        p_line.paragraph_format.space_before = Pt(8)
#        p_line.paragraph_format.space_after = Pt(0)
#        run_line = p_line.add_run("_" * 75)
#        run_line.font.name = 'Times New Roman'
#        run_line.font.bold = True

    doc.add_paragraph()
    doc.add_paragraph()

    # 7. Firmas (Estructura de Tabla Invisible)
    sign_table = doc.add_table(rows=2, cols=2)
    remove_table_borders(sign_table)
    sign_table.allow_autofit = False
    for row in sign_table.rows:
        row.cells[0].width = Cm(7.29)
        row.cells[1].width = Cm(7.30)

    set_cell_format(sign_table.rows[0].cells[0], "_________________________", size=12, align=WD_ALIGN_PARAGRAPH.CENTER)
#    set_cell_format(sign_table.rows[0].cells[1], "_________________________", size=12, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell_format(sign_table.rows[1].cells[0], f"Firma del Pasante:\n{PASANTE_NOMBRE} |  C.I.: {PASANTE_CI}", size=9, align=WD_ALIGN_PARAGRAPH.CENTER)
#    set_cell_format(sign_table.rows[1].cells[1], "Firma del Tutor Industrial:\n[Nombre del Tutor] | C.I.: [Cédula]", size=9, align=WD_ALIGN_PARAGRAPH.CENTER)

    doc.add_paragraph()

    # 8. Bloque Sello Corporativo
#    p_sello = doc.add_paragraph()
#    p_sello.alignment = WD_ALIGN_PARAGRAPH.CENTER
#    p_sello.paragraph_format.space_before = Pt(12)
#    run_s = p_sello.add_run("SELLO DE LA EMPRESA")
#    run_s.font.name = 'Times New Roman'
#    run_s.font.size = Pt(10)
#    run_s.font.bold = True

    fn_word = f"Cronograma_Administracion_Semana{datos['num_semana']}_IUTECP.docx"
    doc.save(fn_word)
    print(f"✔ Generado Word: {fn_word}")

    try:
        subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', fn_word], check=True, stdout=subprocess.DEVNULL)
        print(f"✔ Convertido PDF: {fn_word.replace('.docx', '.pdf')}")
    except Exception:
        print(f"⚠️ Word creado. LibreOffice headless no se ejecutó.")

# ================================================================
#  COLECCIÓN DE DATOS MAESTRA (CRONOGRAMA ADAPTADO A TSU - 10 SEMANAS)
# ================================================================

reportes_pasantias = [
    # ── SEMANA 1 ────────────────────────────────────────────────
    {
        "num_semana": "1",
        "periodo": "Del 01 al 05 de junio de 2026",
        "objetivo": "Formalizar el inicio de las pasantías y reconocer el área administrativa de la empresa para iniciar el levantamiento de información de sus procesos.",
        "entregables": "Acta de inicio firmada, esquema de inducción y primer registro de observaciones de campo.",
        "observaciones_tutor": "La pasante formalizó su ingreso al Departamento de Administración de IDETEL. Mostró puntualidad y disposición para el reconocimiento de los procesos internos.",
        "actividades": [
            ("1", "Inducción y recorrido", "Recorrido por las instalaciones de Ingeniería de Telecomunicaciones, C.A. y presentación al personal administrativo, comercial y de soporte técnico.", "Guía de inducción, planos"),
            ("2", "Reconocimiento de puestos", "Identificación de las estaciones de trabajo y asignación de herramientas y recursos en el Departamento de Administración.", "PC, escritorio, papelería"),
            ("3", "Levantamiento preliminar", "Reunión con el tutor industrial para coordinar el acceso a los registros físicos e informáticos de la empresa.", "Hojas de control, PC"),
            ("4", "Recolección de normativas", "Compilación de los lineamientos internos de trabajo y regulaciones operativas aplicadas en la organización.", "Manuales de procedimiento"),
            ("5", "Diagnóstico inicial de archivos", "Inspección general de la forma en que se custodian los expedientes de nuevos suscriptores e incidencias.", "Archivos físicos, cuaderno")
        ]
    },
    # ── SEMANA 2 ────────────────────────────────────────────────
    {
        "num_semana": "2",
        "periodo": "Del 08 al 12 de junio de 2026",
        "objetivo": "Recopilar y analizar la información sobre la recepción y control de las solicitudes de servicio (nuevos suscriptores e incidencias).",
        "entregables": "Resumen de los flujos de recepción de solicitudes de servicio y registro de observaciones en el cuaderno de campo.",
        "observaciones_tutor": "La pasante ha recolectado información detallada sobre cómo manejamos las solicitudes en el Departamento. Demuestra buen sentido de organización y capacidad analítica.",
        "actividades": [
            ("1", "Entrevistas exploratorias", "Conversación informal con la Supervisora de Administración para entender el flujo documental de la empresa.", "Cuaderno de notas"),
            ("2", "Mapeo de flujos", "Observación directa del camino que siguen las solicitudes de afiliación de nuevos clientes desde el área comercial.", "Hojas de flujo, lápiz"),
            ("3", "Revisión de solicitudes", "Inspección física de las carpetas de nuevos suscriptores para verificar los datos exigidos para la afiliación.", "Carpetas de clientes, PC"),
            ("4", "Clasificación documental", "Organizar de forma preliminar las solicitudes de afiliación y las incidencias técnicas reportadas.", "Expedientes de servicio"),
            ("5", "Registro en bitácora", "Documentar las tareas ejecutadas y los cuellos de botella detectados en la recepción de solicitudes.", "Libreta de apuntes")
        ]
    },
    # ── SEMANA 3 ────────────────────────────────────────────────
    {
        "num_semana": "3",
        "periodo": "Del 15 al 19 de junio de 2026",
        "objetivo": "Analizar detalladamente las fallas en el seguimiento de servicios y diseñar los cuestionarios de recolección de datos.",
        "entregables": "Guía de entrevista estructurada y aprobada por el tutor industrial para diagnosticar el control administrativo.",
        "observaciones_tutor": "La pasante diseñó una guía de entrevista muy pertinente para evaluar la trazabilidad de los reportes e inscripciones. Excelente iniciativa.",
        "actividades": [
            ("1", "Análisis de incidencias", "Examinar cómo se registran y procesan los reportes de fallas o incidencias de los clientes del servicio de internet.", "Tickets de soporte, PC"),
            ("2", "Diseño de guías", "Diseñar el cuestionario de preguntas a aplicar al personal del departamento de administración, NOC y comercial.", "Procesador de textos, PC"),
            ("3", "Validación de cuestionarios", "Someter las preguntas diseñadas a la aprobación del tutor industrial para asegurar su idoneidad.", "Formato borrador de encuesta"),
            ("4", "Planificación de entrevistas", "Establecer el cronograma y horarios para aplicar los cuestionarios sin interferir con las operaciones.", "Agenda, calendario de oficina"),
            ("5", "Selección de muestra", "Definir los cargos específicos a entrevistar (Supervisora de Administración, Analista de Ventas, Analista de Atención).", "Estructura organizativa")
        ]
    },
    # ── SEMANA 4 ────────────────────────────────────────────────
    {
        "num_semana": "4",
        "periodo": "Del 22 al 26 de junio de 2026",
        "objetivo": "Aplicar las entrevistas al personal para diagnosticar los factores críticos que afectan el control de las solicitudes.",
        "entregables": "Cuestionarios completados y matriz de tabulación de las respuestas del personal entrevistado.",
        "observaciones_tutor": "La aplicación del instrumento se realizó ordenadamente. La pasante logró obtener la opinión sincera del personal sobre las fallas de comunicación y demoras.",
        "actividades": [
            ("1", "Aplicación de entrevistas", "Realizar las entrevistas al personal de Administración, Comercialización y Soporte Técnico sobre el flujo de servicios.", "Cuestionarios impresos"),
            ("2", "Recopilación de respuestas", "Sistematizar las respuestas de los cuestionarios aplicados y las observaciones recopiladas en campo.", "Hojas de respuestas, lápiz"),
            ("3", "Identificación de fallas", "Detectar los puntos críticos donde las solicitudes de servicio se retrasan o pierden trazabilidad.", "Expedientes de control"),
            ("4", "Análisis de comunicación", "Evaluar cómo fluye la información sobre las solicitudes entre la administración, el NOC y las cuadrillas de campo.", "Registros de mensajería, PC"),
            ("5", "Tabulación de datos", "Elaborar tablas resumen con los datos de las entrevistas y el porcentaje de inconformidades observadas.", "Hojas de cálculo, PC")
        ]
    },
    # ── SEMANA 5 ────────────────────────────────────────────────
    {
        "num_semana": "5",
        "periodo": "Del 29 de junio al 03 de julio de 2026",
        "objetivo": "Culminar el diagnóstico situacional estructurando el diagrama de Ishikawa y fundamentar la investigación teóricamente.",
        "entregables": "Sección del Diagnóstico Situacional (Capítulo II), diagrama de Ishikawa causa-efecto digital y primer borrador del marco teórico.",
        "observaciones_tutor": "La pasante estructuró de manera excelente el diagnóstico. El diagrama de Ishikawa refleja claramente los vacíos que tenemos en el control de tickets y el canal comercial.",
        "actividades": [
            ("1", "Redacción del diagnóstico", "Elaborar el análisis formal de la situación problemática identificada en el Departamento de Administración.", "PC de oficina, Word"),
            ("2", "Diagramación de Ishikawa", "Construir el diagrama de espina de pescado (causa-efecto) para representar las causas de la pérdida de trazabilidad.", "Herramientas de dibujo, PC"),
            ("3", "Revisión de antecedentes", "Buscar investigaciones previas relacionadas con el control administrativo y la gestión de servicios en telecomunicaciones.", "Buscadores web, biblioteca"),
            ("4", "Definición de bases teóricas", "Redactar los conceptos clave sobre control interno administrativo, procesos, trazabilidad y sistemas de tickets.", "Libros digitales de administración"),
            ("5", "Compilación del marco teórico", "Estructurar el Capítulo II y las bases teóricas del informe final de pasantías según la norma IUTECP.", "Procesador de textos, PC")
        ]
    },
    # ── SEMANA 6 ────────────────────────────────────────────────
    {
        "num_semana": "6",
        "periodo": "Del 06 al 10 de julio de 2026",
        "objetivo": "Concluir los aspectos teóricos del informe y ejecutar tareas de apoyo administrativo en el control diario de clientes.",
        "entregables": "Marco teórico consolidado y registro de asistencia y apoyo en las operaciones contables y de archivo del departamento.",
        "observaciones_tutor": "La pasante brinda un valioso apoyo en el archivo y control diario. Demuestra alto compromiso con el cumplimiento de las tareas operativas asignadas.",
        "actividades": [
            ("1", "Finalización del Marco Teórico", "Revisar la redacción y referencias bibliográficas de los conceptos administrativos de soporte.", "Word, PC de oficina"),
            ("2", "Control de facturas", "Apoyar en la verificación y conciliación de facturas de cobro de servicios mensuales con el listado de abonados.", "Facturas, hojas de cálculo"),
            ("3", "Revisión de contratos", "Colaborar en el cotejo de las firmas y recaudos de los contratos de servicio archivados durante la semana.", "Expedientes de clientes"),
            ("4", "Atención telefónica", "Apoyar en la atención telefónica a suscriptores comerciales para registrar reportes administrativos y de cobros.", "Teléfono de oficina, libreta"),
            ("5", "Organización del archivo", "Colaborar en el ordenamiento físico de los expedientes de clientes corporativos en los archivadores.", "Archivadores de metal, carpetas")
        ]
    },
    # ── SEMANA 7 ────────────────────────────────────────────────
    {
        "num_semana": "7",
        "periodo": "Del 13 al 17 de julio de 2026",
        "objetivo": "Ejecutar las tareas operativas y contables programadas en el departamento y documentar el registro diario de actividades.",
        "entregables": "Planilla de control de incidencias diarias procesadas y reporte de bitácora semanal validado.",
        "observaciones_tutor": "Excelente desempeño en las tareas de soporte comercial-administrativo. Las conciliaciones de cobros fueron realizadas con precisión.",
        "actividades": [
            ("1", "Registro de incidencias", "Llenar el registro diario de incidencias reportadas por los suscriptores y remitir al área de NOC.", "Base de datos local, PC"),
            ("2", "Conciliación de cuentas", "Participar en el proceso de verificación de pagos bancarios contra el listado de clientes activos.", "Estados de cuenta, Excel"),
            ("3", "Documentación en bitácora", "Registrar en el cuaderno de campo las tareas de soporte realizadas y observaciones sobre la atención al cliente.", "Cuaderno de campo, bolígrafo"),
            ("4", "Redacción de actas", "Elaborar borradores de minutas o actas de reuniones semanales de control administrativo.", "Word, plantilla de minuta"),
            ("5", "Archivo de cobranzas", "Organizar y archivar los soportes de transferencia y depósitos de las mensualidades del servicio de internet.", "Carpetas de cobranza, grapadora")
        ]
    },
    # ── SEMANA 8 ────────────────────────────────────────────────
    {
        "num_semana": "8",
        "periodo": "Del 20 al 24 de julio de 2026",
        "objetivo": "Continuar con las labores de soporte administrativo y depurar la correspondencia y archivos de incidencias cerradas.",
        "entregables": "Reporte de control de correspondencia enviada e incidencias depuradas del departamento.",
        "observaciones_tutor": "La pasante ha mostrado mucha madurez profesional. Su labor de depuración de registros nos ha ayudado a ver cuentas pendientes de manera rápida.",
        "actividades": [
            ("1", "Apoyo en auditoría física", "Revisar de forma aleatoria el estado de activación de 20 clientes contra el expediente físico administrativo.", "Carpetas, PC de oficina"),
            ("2", "Control de reportes de campo", "Clasificar y archivar los reportes de culminación de trabajos entregados por las cuadrillas de campo.", "Informes técnicos, archivador"),
            ("3", "Actualización de bases", "Digitar la información de cierre de casos de incidencias administrativas en la base de datos local de control.", "Software de control, PC"),
            ("4", "Redacción de correspondencia", "Elaborar cartas de notificación de saldos pendientes y comunicaciones dirigidas a los suscriptores.", "Word, impresora"),
            ("5", "Reporte de actividades", "Sintetizar las tareas administrativas y los avances en la revisión del archivo de expedientes para la gerencia.", "Procesador de textos, PC")
        ]
    },
    # ── SEMANA 9 ────────────────────────────────────────────────
    {
        "num_semana": "9",
        "periodo": "Del 27 al 31 de julio de 2026",
        "objetivo": "Diseñar la propuesta de mejora del control administrativo y redactar las conclusiones y recomendaciones del informe.",
        "entregables": "Propuesta metodológica de control administrativo, flujograma del nuevo proceso y borradores de conclusiones y recomendaciones.",
        "observaciones_tutor": "Las recomendaciones presentadas por la pasante son muy viables. El nuevo protocolo propuesto reduciría los tiempos de atención de incidencias significativamente.",
        "actividades": [
            ("1", "Elaboración de propuesta", "Diseñar la propuesta de mejoras (nuevo protocolo de recepción de solicitudes de servicios de telecomunicaciones).", "Word, PC de oficina"),
            ("2", "Redacción de Conclusiones", "Escribir las conclusiones del trabajo basándose en los hallazgos y análisis del control administrativo de la empresa.", "Word, PC"),
            ("3", "Redacción de Recomendaciones", "Formular las recomendaciones prácticas dirigidas a la gerencia para optimizar la trazabilidad y la atención.", "Word, PC"),
            ("4", "Flujograma propuesto", "Dibujar el diagrama de flujo del nuevo proceso administrativo propuesto para la gestión de solicitudes.", "Herramientas de diagramación, PC"),
            ("5", "Registro final en bitácora", "Completar las últimas anotaciones y bitácoras del período de ejecución del proyecto.", "Cuaderno de apuntes")
        ]
    },
    # ── SEMANA 10 ───────────────────────────────────────────────
    {
        "num_semana": "10",
        "periodo": "Del 03 al 07 de agosto de 2026",
        "objetivo": "Consolidar y revisar el informe final de pasantías bajo las normas IUTECP para su presentación y firma de cierre.",
        "entregables": "Informe final de pasantías impreso/digitalizado con firmas de aprobación y carta de culminación de actividades.",
        "observaciones_tutor": "La pasante Amaal culminó con éxito sus actividades de pasantía. El informe presentado cumple con los estándares requeridos y aporta soluciones aplicables a IDETEL.",
        "actividades": [
            ("1", "Consolidación del informe", "Unir los capítulos I, II y III, junto con las conclusiones, recomendaciones y anexos en el formato final.", "PC, Word"),
            ("2", "Formateo bajo normas", "Adecuar el espaciado, márgenes, tipo de letra e índices de acuerdo a la normativa de transcripción del IUTECP.", "Word, plantilla IUTECP"),
            ("3", "Revisión de ortografía", "Realizar la lectura final del texto para corregir la sintaxis y asegurar la coherencia técnica del documento.", "Word, corrector ortográfico"),
            ("4", "Reunión de cierre", "Presentar los resultados y formatos propuestos a la Supervisora de Administración y al Tutor Industrial.", "Presentación en PDF, laptop"),
            ("5", "Firma y aval", "Obtener las firmas del tutor industrial y el sello de la empresa en el informe de pasantías definitivo.", "Documento impreso, bolígrafos, sello")
        ]
    }
]

# ================================================================
#  EJECUCIÓN GENERAL
# ================================================================

if __name__ == "__main__":
    print("🚀 Iniciando motor de automatización de cronogramas para Administración (Amaal)...")
    for idx, reporte in enumerate(reportes_pasantias):
        print(f"\n[Compilando {idx+1}/{len(reportes_pasantias)}] Semana {reporte['num_semana']}...")
        generar_documento_semana(reporte)
    print("\n✨ ¡Proceso culminado con éxito! Se han generado los 10 archivos independientes en Word.")
