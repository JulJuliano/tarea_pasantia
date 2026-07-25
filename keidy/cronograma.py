import os
import subprocess
from docx import Document
from docx.shared import Cm, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

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
    add_label_value(doc, "EMPRESA: ", "Lubricantes y Equipos Varyna, C.A.")
    add_label_value(doc, "DEPARTAMENTO: ", "Departamento Administrativo / Área de Procura")
    add_label_value(doc, "ESPECIALIDAD: ", "Administración / Ciencias Comerciales")
    add_label_value(doc, "SEMANA N°: ", datos["num_semana"])
    add_label_value(doc, "PERÍODO: ", datos["periodo"])
    add_label_value(doc, "PASANTE: ", "Keidy Guzmán |  C.I.: 28.706.352")
    add_label_value(doc, "TUTOR INDUSTRIAL: ", "Martina Rondón | C.I.: 12.208.768")

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

    # 6. Observaciones del Tutor Industrial (Espacio para llenar a mano)
    p_obs_t = doc.add_paragraph()
    p_obs_t.paragraph_format.space_after = Pt(4)
    run_ot2 = p_obs_t.add_run("OBSERVACIONES DEL TUTOR INDUSTRIAL:")
    run_ot2.font.name = 'Times New Roman'
    run_ot2.font.size = Pt(12)
    run_ot2.font.bold = True

    p_obs = doc.add_paragraph()
    p_obs.paragraph_format.line_spacing = 1.5
    run_obs = p_obs.add_run("(Espacio reservado para la evaluación cualitativa del tutor sobre control de procesos, puntualidad, manejo de solicitudes y cumplimiento de directrices contables)")
    run_obs.font.name = 'Times New Roman'
    run_obs.font.size = Pt(11)
    run_obs.font.italic = True

    for _ in range(4):
        p_line = doc.add_paragraph()
        p_line.paragraph_format.space_before = Pt(8)
        p_line.paragraph_format.space_after = Pt(0)
        run_line = p_line.add_run("_" * 75)
        run_line.font.name = 'Times New Roman'
        run_line.font.bold = True

    doc.add_paragraph()
    doc.add_paragraph()

    # 7. Firmas (Estructura de Tabla Invisible)
    sign_table = doc.add_table(rows=2, cols=2)
    remove_table_borders(sign_table)
    sign_table.allow_autofit = False
    for row in sign_table.rows:
        row.cells[0].width = Cm(7.29)
        row.cells[1].width = Cm(7.30)

    set_cell_format(sign_table.rows[0].cells[0], "", size=12, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell_format(sign_table.rows[0].cells[1], "", size=12, align=WD_ALIGN_PARAGRAPH.CENTER)

    # Insertar firma del pasante si existe
    ruta_firma_keidy = os.path.join("imagenes", "firma_keidy.png")
    if os.path.exists(ruta_firma_keidy):
        cell_fk = sign_table.rows[0].cells[0]
        cell_fk.text = ""
        cell_fk.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        run_fk = cell_fk.paragraphs[0].add_run()
        run_fk.add_picture(ruta_firma_keidy, width=Cm(3.5))
    else:
        set_cell_format(sign_table.rows[0].cells[0], "_________________________", size=12, align=WD_ALIGN_PARAGRAPH.CENTER)

    ruta_firma_tutor = os.path.join("imagenes", "firma_tutor_keidy.png")
    if os.path.exists(ruta_firma_tutor):
        cell_ft = sign_table.rows[0].cells[1]
        cell_ft.text = ""
        cell_ft.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        run_ft = cell_ft.paragraphs[0].add_run()
        run_ft.add_picture(ruta_firma_tutor, width=Cm(3.5))
    else:
        set_cell_format(sign_table.rows[0].cells[1], "_________________________", size=12, align=WD_ALIGN_PARAGRAPH.CENTER)

    set_cell_format(sign_table.rows[1].cells[0], "Firma del Pasante:\nKeidy Guzmán |  C.I.: 28.706.352", size=9, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell_format(sign_table.rows[1].cells[1], "Firma del Tutor Industrial:\nMartina Rondón | C.I.: 12.208.768", size=9, align=WD_ALIGN_PARAGRAPH.CENTER)

    doc.add_paragraph()

    # 8. Bloque Sello Corporativo
    ruta_sello = os.path.join("imagenes", "sello_keidy.jpg")
    if os.path.exists(ruta_sello):
        p_sello = doc.add_paragraph()
        p_sello.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_sello.paragraph_format.space_before = Pt(12)
        run_s = p_sello.add_run()
        run_s.add_picture(ruta_sello, width=Cm(4))
    else:
        p_sello = doc.add_paragraph()
        p_sello.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_sello.paragraph_format.space_before = Pt(12)
        run_s = p_sello.add_run("SELLO DE LA EMPRESA")
        run_s.font.name = 'Times New Roman'
        run_s.font.size = Pt(10)
        run_s.font.bold = True

    output_dir = "cronogramas generados"
    os.makedirs(output_dir, exist_ok=True)
    fn_word = os.path.join(output_dir, f"Cronograma_Procura_Semana{datos['num_semana']}_IUTECP.docx")
    doc.save(fn_word)
    print(f"✔ Generado Word: {fn_word}")

    try:
        subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', '--outdir', output_dir, fn_word], check=True, stdout=subprocess.DEVNULL)
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
        "periodo": "Del 08 al 12 de junio de 2026",
        "objetivo": "Formalizar el inicio de las pasantías y observar el flujo procedimental de las solicitudes de compra del departamento.",
        "entregables": "Acta de inicio de pasantías visada por la empresa y registro inicial del flujo observado de requisiciones.",
        "actividades": [
            ("1", "Formalización del inicio", "Reunión con la gerencia y el tutor industrial para consignar los formatos institucionales del IUTECP.", "Cartas de postulación, plan institucional"),
            ("2", "Recorrido por las instalaciones", "Conocer las áreas físicas del departamento administrativo y los actores clave del proceso de procura.", "Agenda, cuaderno de apuntes"),
            ("3", "Presentación ante el equipo", "Integrarse formalmente al equipo del departamento administrativo y al área de procura.", "Documentos de presentación"),
            ("4", "Observación del flujo de requisiciones", "Observar el recorrido de una solicitud de compra desde su recepción hasta su procesamiento inicial.", "Cuaderno de campo, lápiz"),
            ("5", "Formulación de la situación problemática", "Registrar las primeras observaciones sobre la complejidad procedimental identificada en el área.", "Libreta de notas, papelería")
        ]
    },
    # ── SEMANA 2 ────────────────────────────────────────────────
    {
        "num_semana": "2",
        "periodo": "Del 15 al 19 de junio de 2026",
        "objetivo": "Apoyar en la recepción de solicitudes de compra y levantar el flujo secuencial del proceso de adquisición.",
        "entregables": "Registro de solicitudes recibidas y mapeo situacional preliminar del proceso actual de procura.",
        "actividades": [
            ("1", "Recepción de solicitudes", "Apoyar en la recepción y clasificación de las solicitudes de compra pendientes del período.", "Formatos de requisición, archiveros"),
            ("2", "Registro de documentos", "Anotar la correspondencia de compras entrante en el libro de control diario del departamento.", "Libro diario, PC de oficina"),
            ("3", "Entrevistas informales al personal", "Conversar con el personal encargado para levantar el flujo secuencial del proceso de adquisición.", "Cuaderno de apuntes, lápiz"),
            ("4", "Familiarización con el sistema de cotizaciones", "Revisar el sistema de seguimiento de cotizaciones vigente y su funcionamiento en el área.", "Expedientes, archivos físicos"),
            ("5", "Elaboración del mapeo situacional", "Documentar el flujo secuencial de las adquisiciones con base en las observaciones y entrevistas realizadas.", "Papel, lápiz, procesador de textos")
        ]
    },
    # ── SEMANA 3 ────────────────────────────────────────────────
    {
        "num_semana": "3",
        "periodo": "Del 22 al 26 de junio de 2026",
        "objetivo": "Tramitar requisiciones del departamento y aplicar la guía de entrevista estructurada al personal de compras.",
        "entregables": "Requisiciones tramitadas del período y guía de entrevista aplicada con respuestas registradas.",
        "actividades": [
            ("1", "Tramitación de requisiciones", "Colaborar en la tramitación de requisiciones de materiales e insumos recibidas durante la semana.", "Formatos de requisición, archivos"),
            ("2", "Comunicación con proveedores", "Apoyar en el contacto con proveedores para el seguimiento de cotizaciones en proceso.", "Teléfono, correo de oficina"),
            ("3", "Actualización del registro de cotizaciones", "Registrar el estado actual de las cotizaciones activas en el sistema de control del departamento.", "PC de oficina, hojas de seguimiento"),
            ("4", "Aplicación de la guía de entrevista", "Aplicar la guía de entrevista estructurada al personal de compras y administración.", "Guía de entrevista impresa, lápiz"),
            ("5", "Identificación de cuellos de botella", "Registrar los hallazgos sobre los pasos que generan mayor demora en las fases de seguimiento y aprobación.", "Cuaderno de campo, notas de entrevista")
        ]
    },
    # ── SEMANA 4 ────────────────────────────────────────────────
    {
        "num_semana": "4",
        "periodo": "Del 29 de junio al 03 de julio de 2026",
        "objetivo": "Dar seguimiento a órdenes de compra abiertas y revisar expedientes históricos para medir tiempos de respuesta.",
        "entregables": "Registro actualizado de órdenes de compra abiertas y tabla de tiempos promedio históricos por fase.",
        "actividades": [
            ("1", "Seguimiento de órdenes abiertas", "Verificar el estatus de las órdenes de compra en proceso y actualizar el registro del departamento.", "Expedientes activos, PC de oficina"),
            ("2", "Verificación de cotizaciones pendientes", "Revisar las cotizaciones sin respuesta e identificar las de mayor antigüedad en el sistema.", "Hojas de seguimiento, archiveros"),
            ("3", "Actualización del registro de proveedores", "Depurar y actualizar la base de datos de proveedores activos del departamento.", "PC de oficina, software de oficina"),
            ("4", "Revisión de expedientes históricos", "Acceder a los expedientes de compras anteriores para calcular los tiempos promedio de respuesta por fase.", "Archivo histórico, hojas de cálculo"),
            ("5", "Identificación de etapas críticas", "Determinar cuáles fases del ciclo concentran los mayores retrasos a partir del análisis de los expedientes.", "Excel, cuaderno de notas")
        ]
    },
    # ── SEMANA 5 ────────────────────────────────────────────────
    {
        "num_semana": "5",
        "periodo": "Del 06 al 10 de julio de 2026",
        "objetivo": "Tramitar solicitudes de compra de la semana y analizar las causas organizativas de los retrasos identificados.",
        "entregables": "Solicitudes tramitadas del período y diagrama causa-efecto con clasificación jerárquica de factores de demora.",
        "actividades": [
            ("1", "Tramitación de solicitudes", "Procesar las solicitudes de compra recibidas durante la semana y gestionar su trámite correspondiente.", "Formatos de requisición, archivos"),
            ("2", "Elaboración de cuadros comparativos", "Apoyar en la preparación de cuadros comparativos de cotizaciones de proveedores activos.", "Excel, hojas de comparación"),
            ("3", "Actualización de la base de proveedores", "Incorporar nuevos datos de contacto y condiciones de proveedores al registro del departamento.", "PC de oficina, base de datos"),
            ("4", "Elaboración del diagrama causa-efecto", "Construir el diagrama de Ishikawa con las causas organizativas de los retrasos identificadas en semanas anteriores.", "Papel, lápiz, procesador de textos"),
            ("5", "Jerarquización de factores", "Clasificar jerárquicamente las causas de demora según su impacto en el ciclo de adquisición.", "Cuaderno de notas, software de oficina")
        ]
    },
    # ── SEMANA 6 ────────────────────────────────────────────────
    {
        "num_semana": "6",
        "periodo": "Del 13 al 17 de julio de 2026",
        "objetivo": "Dar seguimiento a cotizaciones pendientes y diseñar el nuevo flujo de trabajo simplificado de la procura.",
        "entregables": "Expedientes de cotizaciones actualizados y esquema del nuevo flujo simplificado con puntos de control definidos.",
        "actividades": [
            ("1", "Seguimiento a cotizaciones", "Verificar el estatus de las cotizaciones pendientes de aprobación gerencial y actualizar los expedientes.", "Hojas de seguimiento, PC de oficina"),
            ("2", "Actualización de expedientes activos", "Registrar los avances de las compras en proceso en los expedientes del período.", "Archiveros, formatos de control"),
            ("3", "Diseño del flujo simplificado", "Redactar el nuevo flujo de trabajo con reducción de pasos y definición de puntos de control.", "Procesador de textos, papel"),
            ("4", "Asignación de responsables por etapa", "Definir el responsable de cada fase del nuevo procedimiento simplificado de procura.", "Organigrama, procesador de textos"),
            ("5", "Definición de tiempos máximos por fase", "Establecer los tiempos máximos de respuesta aceptables para cada etapa del nuevo circuito de compras.", "Cuaderno de notas, software de oficina")
        ]
    },
    # ── SEMANA 7 ────────────────────────────────────────────────
    {
        "num_semana": "7",
        "periodo": "Del 20 al 24 de julio de 2026",
        "objetivo": "Procesar requisiciones urgentes del período y diseñar las plantillas estandarizadas de cotización y orden de compra.",
        "entregables": "Requisiciones urgentes tramitadas y plantillas estandarizadas de solicitud de cotización y orden de compra diseñadas.",
        "actividades": [
            ("1", "Recepción de requisiciones urgentes", "Procesar las solicitudes de compra urgentes recibidas durante la semana con prioridad operativa.", "Formatos de requisición, archivos"),
            ("2", "Verificación presupuestaria", "Colaborar en la verificación de disponibilidad presupuestaria para las compras urgentes en trámite.", "Sistema contable, hojas de control"),
            ("3", "Diseño de plantilla de cotización", "Elaborar el formato estandarizado de solicitud de cotización adaptado a los requerimientos del departamento.", "PC de oficina, procesador de textos"),
            ("4", "Diseño de plantilla de orden de compra", "Elaborar el formato estandarizado de orden de compra con los campos esenciales del proceso.", "PC de oficina, procesador de textos"),
            ("5", "Diseño de plantilla de seguimiento de estatus", "Crear el formato de control de estatus de cotizaciones para el monitoreo del ciclo de adquisición.", "Excel, PC de oficina")
        ]
    },
    # ── SEMANA 8 ────────────────────────────────────────────────
    {
        "num_semana": "8",
        "periodo": "Del 27 al 31 de julio de 2026",
        "objetivo": "Actualizar registros de proveedores del período y redactar el documento de propuesta de simplificación administrativa.",
        "entregables": "Registros de proveedores actualizados y borrador del documento de propuesta de simplificación administrativa.",
        "actividades": [
            ("1", "Seguimiento a órdenes en proceso", "Verificar el avance de las órdenes de compra activas y actualizar su estatus en el sistema.", "Expedientes activos, PC de oficina"),
            ("2", "Actualización de registros de proveedores", "Incorporar datos actualizados de proveedores y condiciones de entrega al registro del departamento.", "Base de datos, PC de oficina"),
            ("3", "Redacción del documento de propuesta", "Redactar el cuerpo principal de la propuesta de simplificación administrativa integrando el nuevo flujo.", "Procesador de textos, notas de campo"),
            ("4", "Integración de formatos diseñados", "Incorporar las plantillas estandarizadas diseñadas como componentes formales de la propuesta.", "Archivos digitales, procesador de textos"),
            ("5", "Redacción de recomendaciones de control interno", "Documentar las recomendaciones de mejora de control interno derivadas del diagnóstico realizado.", "Procesador de textos, cuaderno de notas")
        ]
    },
    # ── SEMANA 9 ────────────────────────────────────────────────
    {
        "num_semana": "9",
        "periodo": "Del 03 al 07 de agosto de 2026",
        "objetivo": "Apoyar el cierre administrativo del período y validar la propuesta de simplificación con el tutor industrial.",
        "entregables": "Órdenes de compra del período archivadas y propuesta de simplificación validada con observaciones incorporadas.",
        "actividades": [
            ("1", "Cierre administrativo del ciclo", "Apoyar en el cierre del ciclo de compras del período y la organización de los expedientes pendientes.", "Archiveros, formatos de cierre"),
            ("2", "Archivo de órdenes de compra", "Organizar y archivar ordenadamente las órdenes de compra gestionadas durante la pasantía.", "Carpetas físicas, archiveros"),
            ("3", "Presentación de la propuesta al tutor", "Presentar el documento de simplificación administrativa al tutor industrial para su revisión.", "Documento impreso, PC de oficina"),
            ("4", "Registro de observaciones", "Anotar las observaciones y correcciones indicadas por el tutor industrial sobre la propuesta.", "Libreta de notas, lápiz"),
            ("5", "Ajustes al documento final", "Incorporar las observaciones recibidas y realizar los ajustes al documento final de la propuesta.", "Procesador de textos, PC de oficina")
        ]
    },
    # ── SEMANA 10 ───────────────────────────────────────────────
    {
        "num_semana": "10",
        "periodo": "Del 10 al 14 de agosto de 2026",
        "objetivo": "Presentar formalmente la propuesta de simplificación ante la gerencia y consolidar el informe académico de pasantías.",
        "entregables": "Carta de aprobación del tutor industrial firmada e informe académico final listo para entrega institucional.",
        "actividades": [
            ("1", "Presentación ante la gerencia", "Exponer formalmente la propuesta de simplificación administrativa ante la gerencia del departamento.", "Documento final, oficina de gerencia"),
            ("2", "Firma de la carta de aprobación", "Gestionar la firma de la carta de aprobación del tutor industrial para el expediente académico.", "Formato institucional, bolígrafo"),
            ("3", "Consolidación del informe académico", "Integrar todos los capítulos, anexos y formatos en el documento académico definitivo.", "PC de oficina, procesador de textos"),
            ("4", "Revisión final del informe", "Verificar ortografía, referencias bibliográficas, márgenes y normas de presentación del informe.", "Normativa IUTECP, PC de oficina"),
            ("5", "Preparación para entrega institucional", "Organizar los archivos digitales e impresos del informe final para su consignación ante el IUTECP.", "Pendrive, impresora, carpeta de entrega")
        ]
    }
]

# ================================================================
#  EJECUCIÓN GENERAL
# ================================================================

if __name__ == "__main__":
    print("🚀 Iniciando motor de automatización de cronogramas para Procura (Keidy)...")
    for idx, reporte in enumerate(reportes_pasantias):
        print(f"\n[Compilando {idx+1}/{len(reportes_pasantias)}] Semana {reporte['num_semana']}...")
        generar_documento_semana(reporte)
    print("\n✨ ¡Proceso culminado con éxito! Se han generado los 10 archivos independientes en Word y PDF.")
