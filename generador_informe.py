import os
import math
import subprocess
import platform
from docx import Document
from docx.shared import Cm, Pt, Emu, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.section import WD_SECTION_START
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

# Importamos el contenido
import contenido as c

# ================================================================
#  FUNCIONES AUXILIARES DE FORMATO (NORMATIVA IUTECP 2025)
# ================================================================

def setup_iutecp_document():
    """Configura el documento base: Tamaño Carta, Márgenes Art. 6, Fuente Art. 5"""
    doc = Document()

    section = doc.sections[0]
    section.page_width = Cm(21.59)
    section.page_height = Cm(27.94)
    section.top_margin = Cm(3)
    section.bottom_margin = Cm(3)
    section.left_margin = Cm(4)      # Encuadernación
    section.right_margin = Cm(3)

    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(12)
    style.paragraph_format.line_spacing = 1.5
    style.paragraph_format.space_after = Pt(0)

    return doc

def agregar_parrafo_normado(doc, texto, cursiva=False, sangria=True):
    """Párrafo justificado, 1.5 interlineado, sangría 1.25cm (Art. 7, 8)"""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_format = p.paragraph_format
    p_format.line_spacing = 1.5
    p_format.first_line_indent = Cm(1.25) if sangria else Cm(0)
    p_format.space_after = Pt(0)
    p_format.space_before = Pt(0)

    run = p.add_run(texto)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.italic = cursiva
    return p

def agregar_item_lista(doc, numero, texto, negrita_inicio=""):
    """Agrega un elemento enumerado con sangría de primera línea (Art. 10)"""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_format = p.paragraph_format
    p_format.line_spacing = 1.5
    p_format.first_line_indent = Cm(1.25)

    run_num = p.add_run(f"{numero}. ")
    run_num.font.name = 'Times New Roman'
    run_num.font.size = Pt(12)

    if negrita_inicio:
        run_bold = p.add_run(f"{negrita_inicio}: ")
        run_bold.font.name = 'Times New Roman'
        run_bold.font.size = Pt(12)
        run_bold.font.bold = True

    run_text = p.add_run(texto)
    run_text.font.name = 'Times New Roman'
    run_text.font.size = Pt(12)
    return p

def agregar_titulo_nivel2(doc, texto):
    """Nivel 2: Alineado a la izquierda, Negrita (Art. 9 - IUTECP)"""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(24)
    p.paragraph_format.space_after = Pt(24)
    p.paragraph_format.line_spacing = 1.5

    run = p.add_run(texto)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.bold = True
    return p

def agregar_titulo_nivel3(doc, texto):
    """Nivel 3: Alineado a la izquierda, Negrita y Cursiva (Art. 9 - IUTECP)"""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(12)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.first_line_indent = Cm(1.25)

    run = p.add_run(texto)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.italic = True
    return p

def agregar_titulo_nivel4(doc, texto, texto_parrafo=''):
    """
    Nivel 4: Izquierda · Negrita · Sangría ½ pulgada (1.27 cm) · Punto final
    El encabezado termina en punto y el texto del párrafo continúa en la misma línea.
    (Art. 9 - IUTECP)
    Parámetros:
        texto         : El título del nivel 4 (sin punto, se agrega automáticamente).
        texto_parrafo : Texto que continúa en la misma línea después del título.
    """
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(12)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.left_indent = Cm(1.27)
    p.paragraph_format.first_line_indent = Pt(0)

    # Encabezado en negrita con punto final
    run_header = p.add_run(texto.rstrip('.') + '. ')
    run_header.font.name = 'Times New Roman'
    run_header.font.size = Pt(12)
    run_header.font.bold = True

    # Texto del párrafo en la misma línea (formato normal)
    if texto_parrafo:
        run_body = p.add_run(texto_parrafo)
        run_body.font.name = 'Times New Roman'
        run_body.font.size = Pt(12)
    return p

def agregar_titulo_nivel5(doc, texto, texto_parrafo=''):
    """
    Nivel 5: Izquierda · Negrita · Cursiva · Sangría ½ pulgada (1.27 cm) · Punto final
    El encabezado termina en punto y el texto del párrafo continúa en la misma línea.
    (Art. 9 - IUTECP)
    Parámetros:
        texto         : El título del nivel 5 (sin punto, se agrega automáticamente).
        texto_parrafo : Texto que continúa en la misma línea después del título.
    """
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(12)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.left_indent = Cm(1.27)
    p.paragraph_format.first_line_indent = Pt(0)

    # Encabezado en negrita + cursiva con punto final
    run_header = p.add_run(texto.rstrip('.') + '. ')
    run_header.font.name = 'Times New Roman'
    run_header.font.size = Pt(12)
    run_header.font.bold = True
    run_header.font.italic = True

    # Texto del párrafo en la misma línea (formato normal)
    if texto_parrafo:
        run_body = p.add_run(texto_parrafo)
        run_body.font.name = 'Times New Roman'
        run_body.font.size = Pt(12)
    return p

def iniciar_capitulo(doc, numero_romano, titulo):
    """
    Crea un nuevo capítulo con margen superior de 5cm en la primera página (Art. 6),
    centrado, negrita, mayúsculas (Art. 9) y sección continua para volver a 3cm.
    """
    sec = doc.add_section(WD_SECTION_START.NEW_PAGE)
    sec.top_margin = Cm(5)
    sec.bottom_margin = Cm(3)
    sec.left_margin = Cm(4)
    sec.right_margin = Cm(3)
    sec.different_first_page_header_footer = True

    # Título CAPÍTULO X
    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.space_after = Pt(24)
    r1 = p1.add_run(f"CAPÍTULO {numero_romano}")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(12)
    r1.font.bold = True

    # Título del Capítulo
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.space_before = Pt(24)
    r2 = p2.add_run(titulo.upper())
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(12)
    r2.font.bold = True

    # Salto continuo para restaurar margen superior a 3cm en el resto de la página
    sec2 = doc.add_section(WD_SECTION_START.CONTINUOUS)
    sec2.top_margin = Cm(3)
    sec2.bottom_margin = Cm(3)
    sec2.left_margin = Cm(4)
    sec2.right_margin = Cm(3)

def iniciar_seccion_preliminar(doc, titulo):
    """Para secciones preliminares que inician en página nueva (Art. 9, 12)"""
    sec = doc.add_section(WD_SECTION_START.NEW_PAGE)
    sec.top_margin = Cm(5)
    sec.bottom_margin = Cm(3)
    sec.left_margin = Cm(4)
    sec.right_margin = Cm(3)
    sec.different_first_page_header_footer = True

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(24)
    r = p.add_run(titulo.upper())
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.bold = True

    sec2 = doc.add_section(WD_SECTION_START.CONTINUOUS)
    sec2.top_margin = Cm(3)
    sec2.bottom_margin = Cm(3)
    sec2.left_margin = Cm(4)
    sec2.right_margin = Cm(3)

def agregar_cita_larga(doc, texto, cita):
    """
    Citas textuales de más de 40 palabras:
    Párrafo separado, sangría 1.25cm (5 espacios) a ambos lados, interlineado sencillo,
    sin comillas, distancia de 3 espacios de separación del párrafo anterior (Art. 7, 22).
    """
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Cm(1.25)
    p.paragraph_format.right_indent = Cm(1.25)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_before = Pt(36)
    p.paragraph_format.space_after = Pt(12)

    run_t = p.add_run(texto)
    run_t.font.name = 'Times New Roman'
    run_t.font.size = Pt(12)

    run_c = p.add_run(f" {cita}")
    run_c.font.name = 'Times New Roman'
    run_c.font.size = Pt(12)

def agregar_referencia(doc, texto):
    """
    Entrada en referencias bibliográficas (Art. 7, 25 IUTECP):
    - Interlineado sencillo dentro de cada entrada.
    - Sangría francesa de 3 espacios (~0.75cm) hacia la derecha.
    - Entre una referencia y otra: dos (2) espacios sencillos de separación.
    """
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Cm(0.75)
    p.paragraph_format.first_line_indent = Cm(-0.75)
    p.paragraph_format.line_spacing = 1.0
    # 2 espacios sencillos de separación entre referencias (Art. 25)
    p.paragraph_format.space_after = Pt(24)
    p.paragraph_format.space_before = Pt(0)

    run = p.add_run(texto)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)

def set_cell_border(cell, **kwargs):
    """Permite definir bordes de celda personalizados mediante XML"""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for side in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        val = kwargs.get(side, {'val': 'single', 'sz': '4', 'color': '000000'})
        el = OxmlElement(f'w:{side}')
        el.set(qn('w:val'),   val.get('val', 'single'))
        el.set(qn('w:sz'),    val.get('sz', '4'))
        el.set(qn('w:color'), val.get('color', '000000'))
        tcBorders.append(el)
    tcPr.append(tcBorders)

def set_cell_shading(cell, fill='4472C4'):
    """Establece el color de fondo de una celda mediante XML"""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'),   'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'),  fill)
    tcPr.append(shd)

def set_table_fixed_layout(tabla):
    """Establece layout de tabla fijo en XML"""
    tbl = tabla._tbl
    tblPr = tbl.tblPr
    if tblPr is None:
        tblPr = OxmlElement('w:tblPr')
        tbl.insert(0, tblPr)
    for existing in tblPr.findall(qn('w:tblLayout')):
        tblPr.remove(existing)
    tblLayout = OxmlElement('w:tblLayout')
    tblLayout.set(qn('w:type'), 'fixed')
    tblPr.append(tblLayout)

def set_cell_width(cell, width_cm):
    """Establece el ancho de una celda en XML (en dxa/twips)"""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    for existing in tcPr.findall(qn('w:tcW')):
        tcPr.remove(existing)
    tcW = OxmlElement('w:tcW')
    twips = int(width_cm * 567)
    tcW.set(qn('w:w'), str(twips))
    tcW.set(qn('w:type'), 'dxa')
    tcPr.append(tcW)

def set_table_grid_widths_xml(tabla, lista_anchos_cm):
    """Aplica el gridCol XML para garantizar renderizado exacto en LibreOffice/Word"""
    tbl = tabla._tbl
    tblGrid = tbl.tblGrid
    if tblGrid is None:
        tblGrid = OxmlElement('w:tblGrid')
        tbl.append(tblGrid)
    else:
        for existing in tblGrid.findall(qn('w:gridCol')):
            tblGrid.remove(existing)

    for ancho_cm in lista_anchos_cm:
        gridCol = OxmlElement('w:gridCol')
        twips = int(ancho_cm * 567)
        gridCol.set(qn('w:w'), str(twips))
        tblGrid.append(gridCol)

def aplicar_formato_tabla_xml(tabla, lista_anchos_cm):
    """Aplica el ancho fijo a la tabla y a cada celda de forma inmutable"""
    set_table_fixed_layout(tabla)
    set_table_grid_widths_xml(tabla, lista_anchos_cm)
    for fila in tabla.rows:
        for col_idx, ancho in enumerate(lista_anchos_cm):
            set_cell_width(fila.cells[col_idx], ancho)

def _celda(cell, texto, negrita=False, centrado=False, tamaño=Pt(10), color_texto='000000'):
    """Inserta texto formateado en una celda de tabla limpiando párrafos vacíos"""
    for p in cell.paragraphs:
        p._element.getparent().remove(p._element)
    p = cell.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if centrado else WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after  = Pt(3)
    p.paragraph_format.line_spacing = 1.0

    run = p.add_run(texto)
    run.font.name  = 'Times New Roman'
    run.font.size  = tamaño
    run.font.bold  = negrita
    run.font.color.rgb = RGBColor(
        int(color_texto[0:2], 16), int(color_texto[2:4], 16), int(color_texto[4:6], 16)
    )

def agregar_titulo_cuadro(doc, texto):
    """
    Inserta el título de un cuadro ANTES de la tabla (Art. 6, 8, 13 IUTECP).
    - Título arriba del cuadro.
    - El número del cuadro va en negrita, la descripción en cursiva (Art. 6).
    - Espacio doble antes y después (Art. 8).
    Formato esperado del texto: 'Cuadro X. Descripción del cuadro'
    """
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    # Espacio doble antes y después de cuadros titulados (Art. 8)
    p.paragraph_format.space_before = Pt(24)
    p.paragraph_format.space_after = Pt(12)
    p.paragraph_format.line_spacing = 1.5

    # Separar 'Cuadro X' de la descripción para aplicar formatos distintos
    partes = texto.split('. ', 1)
    if len(partes) == 2:
        # "Cuadro X" en negrita
        run_num = p.add_run(partes[0] + '. ')
        run_num.font.name = 'Times New Roman'
        run_num.font.size = Pt(12)
        run_num.font.bold = True
        # Descripción en cursiva (Art. 6)
        run_desc = p.add_run(partes[1])
        run_desc.font.name = 'Times New Roman'
        run_desc.font.size = Pt(12)
        run_desc.font.italic = True
    else:
        run = p.add_run(texto)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.font.bold = True

def agregar_tabla_planificacion(doc, datos, titulo_cuadro=None):
    """Genera la tabla de planificación de objetivos con anchos y estilos fijos"""
    if titulo_cuadro:
        agregar_titulo_cuadro(doc, titulo_cuadro)

    ENCABEZADOS = ['Objetivo Específico', 'Actividades', 'Recursos', 'Indicadores de Logro']
    ANCHOS_CM   = [4.5, 4.5, 3.0, 3.5]
    AZUL, GRIS  = '4472C4', 'D9E1F2'

    tabla = doc.add_table(rows=1 + len(datos), cols=4)
    tabla.style = 'Table Grid'
    aplicar_formato_tabla_xml(tabla, ANCHOS_CM)

    for col, enc in enumerate(ENCABEZADOS):
        cell = tabla.cell(0, col)
        set_cell_shading(cell, AZUL)
        _celda(cell, enc, negrita=True, centrado=True, tamaño=Pt(10), color_texto='FFFFFF')

    for fila, (obj, act, rec, ind) in enumerate(datos, start=1):
        contenidos = [obj, act, rec, ind]
        fondo = GRIS if fila % 2 == 0 else 'FFFFFF'
        for col, texto in enumerate(contenidos):
            cell = tabla.cell(fila, col)
            set_cell_shading(cell, fondo)
            _celda(cell, texto, tamaño=Pt(10))

def agregar_gantt(doc, semanas, titulo_cuadro=None):
    """Genera la tabla Gantt de actividades con cálculo dinámico del ancho útil"""
    if titulo_cuadro:
        agregar_titulo_cuadro(doc, titulo_cuadro)

    num_sem = max(len(s[1]) for s in semanas)
    AZUL, VERDE, GRIS = '4472C4', '70AD47', 'D9E1F2'

    COL_ACT_CM = 9.5
    section = doc.sections[-1]
    ancho_util_emu = section.page_width - section.left_margin - section.right_margin
    ancho_util_cm = Emu(ancho_util_emu).cm
    espacio_restante = max(ancho_util_cm - COL_ACT_CM, 1.0)
    COL_SEM_CM = espacio_restante / num_sem if num_sem > 0 else 1.0

    tabla = doc.add_table(rows=1 + len(semanas), cols=1 + num_sem)
    tabla.style = 'Table Grid'

    anchos_gantt = [COL_ACT_CM] + [COL_SEM_CM] * num_sem
    aplicar_formato_tabla_xml(tabla, anchos_gantt)

    cell_h = tabla.cell(0, 0)
    set_cell_shading(cell_h, AZUL)
    _celda(cell_h, 'Actividades Administrativas', negrita=True, centrado=True, tamaño=Pt(10), color_texto='FFFFFF')

    for s in range(num_sem):
        cell_s = tabla.cell(0, s + 1)
        set_cell_shading(cell_s, AZUL)
        _celda(cell_s, f'S{s+1}', negrita=True, centrado=True, tamaño=Pt(9), color_texto='FFFFFF')

    for fila, (desc, activas) in enumerate(semanas, start=1):
        fondo_fila = GRIS if fila % 2 == 0 else 'FFFFFF'
        cell_a = tabla.cell(fila, 0)
        set_cell_shading(cell_a, fondo_fila)
        _celda(cell_a, desc, tamaño=Pt(10))

        for s in range(num_sem):
            cell_s = tabla.cell(fila, s + 1)
            activa = activas[s] if s < len(activas) else False
            set_cell_shading(cell_s, VERDE if activa else fondo_fila)
            _celda(cell_s, '✓' if activa else '', centrado=True, tamaño=Pt(9), color_texto='FFFFFF' if activa else '000000')

def _insertar_campo_pagina(run, formato_pagina='PAGE'):
    """Inserta un campo de número de página con el formato especificado en un run."""
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set(qn('w:fldCharType'), 'begin')
    instrText = OxmlElement('w:instrText')
    instrText.set(qn('xml:space'), 'preserve')
    instrText.text = formato_pagina
    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'separate')
    fldChar3 = OxmlElement('w:fldChar')
    fldChar3.set(qn('w:fldCharType'), 'end')
    run._r.extend([fldChar1, instrText, fldChar2, fldChar3])
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)

def agregar_numeracion_pie(doc, idx_inicio_cuerpo=None):
    """
    Numeración de páginas según norma IUTECP:
    - Portada y contraportada (secciones 0 y 1): SIN número.
    - Preliminares (Dedicatoria..Introducción): Romanos en minúsculas (i, ii, iii...)
      Se cuentan desde la portada pero no se imprimen en la primera página
      de cada sección preliminar gracias a different_first_page_header_footer.
    - Cuerpo (Capítulos I..V, Referencias, Anexos): Arábigos (1, 2, 3...)
      No se imprime en la primera página de cada capítulo/sección
      gracias a different_first_page_header_footer.
    idx_inicio_cuerpo: índice de la sección donde empieza el Capítulo I.
    """
    # 1. Desactivar numeración en portada y contraportada (secciones 0 y 1)
    for sec_idx in range(min(2, len(doc.sections))):
        section = doc.sections[sec_idx]
        footer = section.footer
        footer.is_linked_to_previous = False
        # Dejar el pie vacío

    # 2. Si no se proporcionó el índice de inicio del cuerpo, detectarlo
    #    buscando la primera sección cuyo primer párrafo contenga "CAPÍTULO"
    if idx_inicio_cuerpo is None:
        for i, sec in enumerate(doc.sections):
            # Buscar si algún párrafo del cuerpo de esta sección dice CAPÍTULO
            body_elem = sec._sectPr.getparent()
            # Simplemente iteramos las secciones y buscamos
            pass
        # Valor por defecto seguro: la Introducción es la última preliminar.
        # Las preliminares producen 2 secciones cada una (NEW_PAGE + CONTINUOUS).
        # Contamos: portada(0), contraportada(1), dedicatoria(2,3),
        # agradecimientos(4,5), resumen(6,7), introducción(8,9) => cap I empieza en 10
        idx_inicio_cuerpo = 10

    # 3. Preliminares: romanos en minúsculas (desde sección 2 hasta idx_inicio_cuerpo - 1)
    for sec_idx in range(2, min(idx_inicio_cuerpo, len(doc.sections))):
        section = doc.sections[sec_idx]
        footer = section.footer
        footer.is_linked_to_previous = False
        p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        # PAGE \\* roman → romanos en minúsculas
        _insertar_campo_pagina(run, ' PAGE \\* roman ')

    # 4. Cuerpo: arábigos (desde idx_inicio_cuerpo en adelante)
    for sec_idx in range(idx_inicio_cuerpo, len(doc.sections)):
        section = doc.sections[sec_idx]
        footer = section.footer
        footer.is_linked_to_previous = False
        p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        _insertar_campo_pagina(run, ' PAGE ')

def buscar_imagen_por_numero(carpeta, numero, extensiones=None):
    """Busca una imagen por su nombre numérico en una carpeta específica"""
    if extensiones is None:
        extensiones = ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff', 'webp']
    if not os.path.exists(carpeta):
        print(f"⚠ Advertencia: La carpeta '{carpeta}' no existe")
        return None
    numero_str = str(numero)
    for archivo in os.listdir(carpeta):
        nombre, ext = os.path.splitext(archivo)
        if nombre == numero_str and ext.lower()[1:] in extensiones:
            ruta_completa = os.path.join(carpeta, archivo)
            print(f"✓ Imagen encontrada: {ruta_completa}")
            return ruta_completa
    print(f"⚠ No se encontró imagen con número {numero} en {carpeta}")
    return None

def agregar_imagen(doc, ruta_imagen, titulo, ancho=Cm(12), fuente=None):
    """
    Agrega una imagen (gráfico) y su título descriptivo DEBAJO (Art. 13 IUTECP).
    - Espacio doble antes y después de gráficos titulados (Art. 8).
    - El número del gráfico en cursiva, la descripción en negrita (Art. 6).
    - Opcionalmente agrega la línea 'Fuente:' (Art. 13).
    Formato esperado del titulo: 'Gráfico X. Descripción del gráfico'
    """
    if not ruta_imagen or not os.path.exists(ruta_imagen):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(f"[IMAGEN NO ENCONTRADA: {titulo}]")
        run.font.italic = True
        run.font.color.rgb = RGBColor(255, 0, 0)
        return

    section = doc.sections[-1]
    max_width = Emu(section.page_width - section.left_margin - section.right_margin)
    if ancho > max_width:
        ancho = max_width

    # Espacio doble antes del gráfico (Art. 8)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(24)
    run = p.add_run()
    try:
        run.add_picture(ruta_imagen, width=ancho)
    except Exception as e:
        print(f"❌ Error al agregar imagen {ruta_imagen}: {e}")
        return

    # Título del gráfico debajo de la imagen (Art. 13)
    p_titulo = doc.add_paragraph()
    p_titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_titulo.paragraph_format.space_before = Pt(6)
    p_titulo.paragraph_format.space_after = Pt(24)

    # Separar 'Gráfico X' de la descripción para formatos distintos
    partes = titulo.split('. ', 1)
    if len(partes) == 2:
        # "Gráfico X." en cursiva
        run_num = p_titulo.add_run(partes[0] + '. ')
        run_num.font.name = 'Times New Roman'
        run_num.font.size = Pt(12)
        run_num.font.italic = True
        # Descripción en negrita
        run_desc = p_titulo.add_run(partes[1])
        run_desc.font.name = 'Times New Roman'
        run_desc.font.size = Pt(12)
        run_desc.font.bold = True
    else:
        run_titulo = p_titulo.add_run(titulo)
        run_titulo.font.name = 'Times New Roman'
        run_titulo.font.size = Pt(12)
        run_titulo.font.bold = True

    # Línea de Fuente opcional (Art. 13)
    if fuente:
        p_fuente = doc.add_paragraph()
        p_fuente.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_fuente.paragraph_format.space_before = Pt(0)
        p_fuente.paragraph_format.space_after = Pt(12)
        run_f_label = p_fuente.add_run('Fuente: ')
        run_f_label.font.name = 'Times New Roman'
        run_f_label.font.size = Pt(12)
        run_f_label.font.italic = True
        run_f_text = p_fuente.add_run(fuente)
        run_f_text.font.name = 'Times New Roman'
        run_f_text.font.size = Pt(12)

# ================================================================
# CONSTRUCCIÓN DEL DOCUMENTO (PORTADA COMPATIBLE LIBREOFFICE)
# ================================================================
def construir_portada(doc):
    """
    Construye la portada distribuyendo los 4 bloques de forma proporcional
    al área útil de la página, sin valores fijos de puntos.

    Las posiciones de cada bloque se definen como porcentajes del área útil:
      POS_TITULO: dónde empieza el título (defecto 42% = ligeramente sobre el centro)
      POS_AUTOR : dónde empiezan los datos del autor (defecto 67% = tercio inferior)
      POS_FECHA : dónde empieza la fecha (defecto 90% = cerca del margen inferior)
    """
    # ------------------------------------------------------------------
    # 1. Leer dimensiones reales de la página (en puntos, 1 pt = 1/72 in)
    # ------------------------------------------------------------------
    section = doc.sections[0]
    EMU_PER_PT = 12700  # 1 pt = 12700 EMU

    usable_h = (section.page_height - section.top_margin - section.bottom_margin) / EMU_PER_PT
    usable_w = (section.page_width  - section.left_margin - section.right_margin ) / EMU_PER_PT

    # ------------------------------------------------------------------
    # 2. Estimar la altura de cada bloque en puntos
    #    (fuente 12pt × interlineado 1.15 = ~13.8pt por línea)
    # ------------------------------------------------------------------
    LINE_PT = 12 * 1.15

    membrete_lines = len(c.MEMBRETE)

    lineas_autor = c.AUTOR_DATOS if isinstance(c.AUTOR_DATOS, list) else [c.AUTOR_DATOS]
    autor_lines  = len(lineas_autor)

    # Times New Roman 12pt: ancho promedio ~6pt por carácter
    chars_per_line = max(1, int(usable_w / 6.0))
    titulo_lines   = max(1, math.ceil(len(c.TITULO_PROYECTO) / chars_per_line))

    h_membrete = membrete_lines * LINE_PT
    h_titulo   = titulo_lines   * LINE_PT
    h_autor    = autor_lines    * LINE_PT
    h_fecha    = LINE_PT

    # ------------------------------------------------------------------
    # 3. Posiciones objetivo como porcentaje del área útil
    #    (ajusta estos valores para mover los bloques)
    # ------------------------------------------------------------------
    POS_TITULO = 0.42   # El título empieza al 42% del área útil
    POS_AUTOR  = 0.67   # El autor empieza al 67%
    POS_FECHA  = 0.90   # La fecha empieza al 90%

    # Espaciado calculado: posición absoluta menos lo ya consumido
    before_titulo = max(6.0, usable_h * POS_TITULO - h_membrete)
    before_autor  = max(6.0, usable_h * POS_AUTOR  - usable_h * POS_TITULO - h_titulo)
    before_fecha  = max(6.0, usable_h * POS_FECHA  - usable_h * POS_AUTOR  - h_autor)

    # ------------------------------------------------------------------
    # 4. Renderizar cada bloque
    # ------------------------------------------------------------------

    # BLOQUE 1: MEMBRETE (Alineado al margen superior)
    p_memb = doc.add_paragraph()
    p_memb.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_memb.paragraph_format.line_spacing = 1.15
    p_memb.paragraph_format.space_before = Pt(0)
    p_memb.paragraph_format.space_after  = Pt(0)
    for i, linea in enumerate(c.MEMBRETE):
        r = p_memb.add_run(linea)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        r.font.bold = True
        if i < len(c.MEMBRETE) - 1:
            r.add_break()

    # BLOQUE 2: TÍTULO DEL PROYECTO (Centrado proporcionalmente)
    p_titulo = doc.add_paragraph()
    p_titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_titulo.paragraph_format.line_spacing = 1.15
    p_titulo.paragraph_format.space_before = Pt(before_titulo)
    p_titulo.paragraph_format.space_after  = Pt(0)
    r_title = p_titulo.add_run(c.TITULO_PROYECTO)
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(12)
    r_title.font.bold = True

    # BLOQUE 3: DATOS DEL AUTOR (Tercio inferior, alineado a la derecha)
    p_datos = doc.add_paragraph()
    p_datos.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_datos.paragraph_format.line_spacing = 1.15
    p_datos.paragraph_format.space_before = Pt(before_autor)
    p_datos.paragraph_format.space_after  = Pt(0)
    for i, linea in enumerate(lineas_autor):
        r = p_datos.add_run(linea)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        r.font.bold = True
        if i < len(lineas_autor) - 1:
            r.add_break()

    # BLOQUE 4: CIUDAD Y FECHA (Proporcional al margen inferior)
    p_pie = doc.add_paragraph()
    p_pie.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_pie.paragraph_format.line_spacing = 1.15
    p_pie.paragraph_format.space_before = Pt(before_fecha)
    p_pie.paragraph_format.space_after  = Pt(0)
    r_pie = p_pie.add_run(c.FECHA_LUGAR)
    r_pie.font.name = 'Times New Roman'
    r_pie.font.size = Pt(12)

def agregar_parada_tabulacion_puntos(parrafo, posicion_emu):
    """Agrega una parada de tabulación derecha con puntos de relleno usando la API oficial de python-docx."""
    parrafo.paragraph_format.tab_stops.add_tab_stop(
        Emu(posicion_emu),
        alignment=WD_TAB_ALIGNMENT.RIGHT,
        leader=WD_TAB_LEADER.DOTS
    )

def agregar_tabulaciones_lista(parrafo, pos_tab_texto_emu, pos_tab_pag_emu):
    """Agrega dos paradas de tabulación oficiales: izquierda (texto) y derecha con puntos (página)."""
    parrafo.paragraph_format.tab_stops.add_tab_stop(
        Emu(pos_tab_texto_emu),
        alignment=WD_TAB_ALIGNMENT.LEFT
    )
    parrafo.paragraph_format.tab_stops.add_tab_stop(
        Emu(pos_tab_pag_emu),
        alignment=WD_TAB_ALIGNMENT.RIGHT,
        leader=WD_TAB_LEADER.DOTS
    )

def agregar_tabulacion_derecha(parrafo, pos_tab_pag_emu):
    """Agrega una única parada de tabulación derecha oficial (para alinear pp. en la cabecera)."""
    parrafo.paragraph_format.tab_stops.add_tab_stop(
        Emu(pos_tab_pag_emu),
        alignment=WD_TAB_ALIGNMENT.RIGHT
    )

def agregar_fila_indice_general_nativa(doc, titulo, pagina, sangria_cm=0, negrita=False):
    """Agrega una línea del índice general usando tabulaciones nativas de Word para alinear al extremo derecho de forma absoluta."""
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.left_indent = Cm(sangria_cm)
    
    section = doc.sections[-1]
    ancho_util_emu = section.page_width - section.left_margin - section.right_margin
    # La posición del tabulador en Word es absoluta respecto a los márgenes, por lo que usamos directamente ancho_util_emu
    agregar_parada_tabulacion_puntos(p, ancho_util_emu)
    
    run_desc = p.add_run(f"{titulo}\t")
    run_desc.font.name = 'Times New Roman'
    run_desc.font.size = Pt(12)
    run_desc.font.bold = negrita
    
    run_pag = p.add_run(pagina)
    run_pag.font.name = 'Times New Roman'
    run_pag.font.size = Pt(12)
    run_pag.font.bold = negrita
    return p

def agregar_fila_lista_preliminar_nativa(doc, col1_text, col2_text, col3_text):
    """Agrega una entrada a una lista descriptiva (cuadro/gráfico/anexo) con sangría colgante y tabulación nativa absoluta."""
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.left_indent = Cm(1.8)
    p.paragraph_format.first_line_indent = Cm(-1.8)
    
    section = doc.sections[-1]
    ancho_util_emu = section.page_width - section.left_margin - section.right_margin
    # La posición del tabulador en Word es absoluta respecto a los márgenes, por lo que usamos directamente ancho_util_emu
    agregar_tabulaciones_lista(p, Cm(1.8).emu, ancho_util_emu)
    
    # Escribir con formato
    run = p.add_run(f"{col1_text}\t{col2_text}\t{col3_text}")
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    return p

def construir_cuerpo_documento(doc):
    """Escribe secuencialmente todas las secciones del informe de pasantía"""

    # --- CÁLCULO DINÁMICO DE PÁGINAS PRELIMINARES ---
    pag_actual_romana = 3  # Dedicatoria empieza en iii (portada=i, contraportada=ii)
    romanos = {1: 'i', 2: 'ii', 3: 'iii', 4: 'iv', 5: 'v', 6: 'vi', 7: 'vii', 8: 'viii', 9: 'ix', 10: 'x', 11: 'xi', 12: 'xii'}
    
    pag_dedicatoria = ""
    pag_agradecimientos = ""
    pag_resumen = ""
    
    if hasattr(c, 'DEDICATORIA') and c.DEDICATORIA:
        pag_dedicatoria = romanos.get(pag_actual_romana, str(pag_actual_romana))
        pag_actual_romana += 1
        
    if hasattr(c, 'AGRADECIMIENTOS') and c.AGRADECIMIENTOS:
        pag_agradecimientos = romanos.get(pag_actual_romana, str(pag_actual_romana))
        pag_actual_romana += 1
        
    if hasattr(c, 'RESUMEN_TEXTO') and c.RESUMEN_TEXTO:
        pag_resumen = romanos.get(pag_actual_romana, str(pag_actual_romana))
        pag_actual_romana += 1
        
    pag_indice = romanos.get(pag_actual_romana, str(pag_actual_romana))
    pag_actual_romana += 1
    
    pag_lista_cuadros = romanos.get(pag_actual_romana, str(pag_actual_romana))
    pag_actual_romana += 1
    
    pag_lista_graficos = romanos.get(pag_actual_romana, str(pag_actual_romana))
    pag_actual_romana += 1
    
    pag_lista_anexos = ""
    if hasattr(c, 'ANEXOS_LISTA') and c.ANEXOS_LISTA:
        pag_lista_anexos = romanos.get(pag_actual_romana, str(pag_actual_romana))
        pag_actual_romana += 1

    # --- PÁGINAS PRELIMINARES ---
    if hasattr(c, 'DEDICATORIA') and c.DEDICATORIA:
        iniciar_seccion_preliminar(doc, "DEDICATORIA")
        agregar_parrafo_normado(doc, c.DEDICATORIA)

    if hasattr(c, 'AGRADECIMIENTOS') and c.AGRADECIMIENTOS:
        iniciar_seccion_preliminar(doc, "AGRADECIMIENTOS")
        agregar_parrafo_normado(doc, c.AGRADECIMIENTOS)

    if hasattr(c, 'RESUMEN_TEXTO') and c.RESUMEN_TEXTO:
        iniciar_seccion_preliminar(doc, "RESUMEN")
        agregar_parrafo_normado(doc, c.RESUMEN_TEXTO)
        doc.add_paragraph()
        p_kw = doc.add_paragraph()
        p_kw.paragraph_format.first_line_indent = Cm(1.25)
        run_kw_label = p_kw.add_run("Palabras claves: ")
        run_kw_label.font.bold = True
        p_kw.add_run(c.PALABRAS_CLAVE)

    # --- ÍNDICE DE CONTENIDO ---
    iniciar_seccion_preliminar(doc, "ÍNDICE DE CONTENIDO")
    p_header_ind = doc.add_paragraph()
    p_header_ind.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_header_ind.paragraph_format.space_after = Pt(12)
    run_h_ind = p_header_ind.add_run("pp.")
    run_h_ind.font.name = 'Times New Roman'
    run_h_ind.font.size = Pt(12)
    run_h_ind.font.bold = True
    
    if pag_dedicatoria:
        agregar_fila_indice_general_nativa(doc, "DEDICATORIA", pag_dedicatoria)
    if pag_agradecimientos:
        agregar_fila_indice_general_nativa(doc, "AGRADECIMIENTOS", pag_agradecimientos)
    if pag_resumen:
        agregar_fila_indice_general_nativa(doc, "RESUMEN", pag_resumen)
        
    agregar_fila_indice_general_nativa(doc, "LISTA DE CUADROS", pag_lista_cuadros)
    agregar_fila_indice_general_nativa(doc, "LISTA DE GRÁFICOS", pag_lista_graficos)
    if pag_lista_anexos:
        agregar_fila_indice_general_nativa(doc, "LISTA DE ANEXOS", pag_lista_anexos)
        
    agregar_fila_indice_general_nativa(doc, "INTRODUCCIÓN", "1")
    
    # Capítulos
    p_cap_lbl = doc.add_paragraph()
    p_cap_lbl.paragraph_format.space_before = Pt(12)
    p_cap_lbl.paragraph_format.space_after = Pt(6)
    p_cap_lbl.add_run("CAPÍTULOS").font.bold = True
    
    # Capítulo I
    agregar_fila_indice_general_nativa(doc, "I REALIDAD ORGANIZACIONAL", "2", sangria_cm=0, negrita=True)
    agregar_fila_indice_general_nativa(doc, "Identificación de la empresa", "2", sangria_cm=0.5)
    agregar_fila_indice_general_nativa(doc, "Reseña histórica", "2", sangria_cm=0.5)
    agregar_fila_indice_general_nativa(doc, "Misión", "2", sangria_cm=0.5)
    agregar_fila_indice_general_nativa(doc, "Visión", "3", sangria_cm=0.5)
    agregar_fila_indice_general_nativa(doc, "Valores", "3", sangria_cm=0.5)
    agregar_fila_indice_general_nativa(doc, "Objetivos Organizacionales", "3", sangria_cm=0.5)
    agregar_fila_indice_general_nativa(doc, "Ubicación geográfica", "3", sangria_cm=0.5)
    agregar_fila_indice_general_nativa(doc, "Población de los trabajadores de la empresa", "3", sangria_cm=0.5)
    agregar_fila_indice_general_nativa(doc, "Estructura organizacional de la empresa (organigrama)", "4", sangria_cm=0.5)
    
    # Capítulo II
    agregar_fila_indice_general_nativa(doc, "II DIAGNÓSTICO SITUACIONAL", "5", sangria_cm=0, negrita=True)
    agregar_fila_indice_general_nativa(doc, "Identificación de la situación problemática", "5", sangria_cm=0.5)
    agregar_fila_indice_general_nativa(doc, "Objetivo General", "5", sangria_cm=0.5)
    agregar_fila_indice_general_nativa(doc, "Objetivos Específicos", "5", sangria_cm=0.5)
    agregar_fila_indice_general_nativa(doc, "Planificación integral de objetivos", "5", sangria_cm=0.5)
    agregar_fila_indice_general_nativa(doc, "Cronograma de actividades", "6", sangria_cm=0.5)
    
    # Capítulo III
    agregar_fila_indice_general_nativa(doc, "III MARCO TEÓRICO", "7", sangria_cm=0, negrita=True)
    agregar_fila_indice_general_nativa(doc, "Bases teóricas referenciales", "7", sangria_cm=0.5)
    
    # Capítulo IV
    agregar_fila_indice_general_nativa(doc, "IV ACTIVIDADES REALIZADAS", "8", sangria_cm=0, negrita=True)
    agregar_fila_indice_general_nativa(doc, "Descripción de actividades ejecutadas por semana", "8", sangria_cm=0.5)
    
    # Capítulo V
    agregar_fila_indice_general_nativa(doc, "V CONCLUSIONES Y RECOMENDACIONES", "10", sangria_cm=0, negrita=True)
    agregar_fila_indice_general_nativa(doc, "Conclusiones", "10", sangria_cm=0.5)
    agregar_fila_indice_general_nativa(doc, "Recomendaciones", "10", sangria_cm=0.5)
    
    # Referencias y Anexos
    agregar_fila_indice_general_nativa(doc, "REFERENCIAS", "11", sangria_cm=0, negrita=True)
    agregar_fila_indice_general_nativa(doc, "ANEXOS", "12", sangria_cm=0, negrita=True)

    # --- LISTA DE CUADROS ---
    iniciar_seccion_preliminar(doc, "LISTA DE CUADROS")
    p_header_c = doc.add_paragraph()
    p_header_c.paragraph_format.space_before = Pt(12)
    p_header_c.paragraph_format.space_after = Pt(12)
    
    section_c = doc.sections[-1]
    ancho_c_emu = section_c.page_width - section_c.left_margin - section_c.right_margin
    agregar_tabulacion_derecha(p_header_c, ancho_c_emu)
    
    run_c_lbl = p_header_c.add_run("CUADRO")
    run_c_lbl.font.name = 'Times New Roman'
    run_c_lbl.font.size = Pt(12)
    run_c_lbl.font.bold = True
    
    p_header_c.add_run("\t")  # Salto de tabulador explícito para OXML
    
    run_pp_c = p_header_c.add_run("pp.")
    run_pp_c.font.name = 'Times New Roman'
    run_pp_c.font.size = Pt(12)
    run_pp_c.font.bold = True
    
    agregar_fila_lista_preliminar_nativa(doc, "1", "Planificación integral de objetivos específicos", "5")
    agregar_fila_lista_preliminar_nativa(doc, "2", "Cronograma de actividades administrativas", "6")

    # --- LISTA DE GRÁFICOS ---
    iniciar_seccion_preliminar(doc, "LISTA DE GRÁFICOS")
    p_header_g = doc.add_paragraph()
    p_header_g.paragraph_format.space_before = Pt(12)
    p_header_g.paragraph_format.space_after = Pt(12)
    
    section_g = doc.sections[-1]
    ancho_g_emu = section_g.page_width - section_g.left_margin - section_g.right_margin
    agregar_tabulacion_derecha(p_header_g, ancho_g_emu)
    
    run_g_lbl = p_header_g.add_run("GRÁFICO")
    run_g_lbl.font.name = 'Times New Roman'
    run_g_lbl.font.size = Pt(12)
    run_g_lbl.font.bold = True
    
    p_header_g.add_run("\t")  # Salto de tabulador explícito para OXML
    
    run_pp_g = p_header_g.add_run("pp.")
    run_pp_g.font.name = 'Times New Roman'
    run_pp_g.font.size = Pt(12)
    run_pp_g.font.bold = True
    
    agregar_fila_lista_preliminar_nativa(doc, "1", "Representación cartográfica y ubicación espacial de la empresa", "3")
    agregar_fila_lista_preliminar_nativa(doc, "2", "Organigrama estructural y niveles jerárquicos de la organización", "4")

    # --- LISTA DE ANEXOS ---
    if hasattr(c, 'ANEXOS_LISTA') and c.ANEXOS_LISTA:
        iniciar_seccion_preliminar(doc, "LISTA DE ANEXOS")
        p_header_a = doc.add_paragraph()
        p_header_a.paragraph_format.space_before = Pt(12)
        p_header_a.paragraph_format.space_after = Pt(12)
        
        section_a = doc.sections[-1]
        ancho_a_emu = section_a.page_width - section_a.left_margin - section_a.right_margin
        agregar_tabulacion_derecha(p_header_a, ancho_a_emu)
        
        run_a_lbl = p_header_a.add_run("ANEXOS")
        run_a_lbl.font.name = 'Times New Roman'
        run_a_lbl.font.size = Pt(12)
        run_a_lbl.font.bold = True
        
        p_header_a.add_run("\t")  # Salto de tabulador explícito para OXML
        
        run_pp_a = p_header_a.add_run("pp.")
        run_pp_a.font.name = 'Times New Roman'
        run_pp_a.font.size = Pt(12)
        run_pp_a.font.bold = True
        
        anexos_lista = getattr(c, 'ANEXOS_LISTA', [])
        for idx, (cod, desc) in enumerate(anexos_lista):
            letra = cod.split(" ")[-1]
            pag_est = str(13 + idx)
            agregar_fila_lista_preliminar_nativa(doc, letra, desc, pag_est)

    # --- REGISTRO DEL INICIO DEL CUERPO ---
    iniciar_seccion_preliminar(doc, "INTRODUCCIÓN")
    agregar_parrafo_normado(doc, getattr(c, 'INTRODUCCION_TEXTO', 'Texto de introducción no proporcionado.'))
    
    # Retornamos el índice de la sección que se va a crear para el Capítulo I (que es la actual longitud de doc.sections)
    idx_cap1 = len(doc.sections)

    # --- CAPÍTULO I: REALIDAD ORGANIZACIONAL ---
    iniciar_capitulo(doc, "I", "REALIDAD ORGANIZACIONAL")
    agregar_titulo_nivel2(doc, "IDENTIFICACIÓN DE LA EMPRESA")
    identificacion_empresa = getattr(c, 'IDENTIFICACION_EMPRESA', '')
    if identificacion_empresa:
        agregar_parrafo_normado(doc, identificacion_empresa)

    agregar_titulo_nivel3(doc, "1.1.1 Razón social")
    agregar_parrafo_normado(doc, getattr(c, 'RAZON_SOCIAL', 'Razón Social no proporcionada.'), sangria=False)

    agregar_titulo_nivel3(doc, "1.1.2 Reseña histórica")
    resena_data = getattr(c, 'RESENA_HISTORICA', [])
    if isinstance(resena_data, str):
        agregar_parrafo_normado(doc, resena_data)
    else:
        for parrafo in resena_data:
            agregar_parrafo_normado(doc, parrafo)

    agregar_titulo_nivel3(doc, "1.1.3 Misión")
    agregar_parrafo_normado(doc, getattr(c, 'MISION', 'Misión no proporcionada.'), cursiva=True)

    agregar_titulo_nivel3(doc, "1.1.4 Visión")
    agregar_parrafo_normado(doc, getattr(c, 'VISION', 'Visión no proporcionada.'), cursiva=True)

    agregar_titulo_nivel3(doc, "1.1.5 Valores")
    agregar_parrafo_normado(doc, "Los valores que orientan las actividades de la organización destacan:")
    valores_data = getattr(c, 'VALORES', [])
    for i, (valor, descripcion) in enumerate(valores_data, 1):
        agregar_item_lista(doc, i, descripcion, valor)

    agregar_titulo_nivel3(doc, "1.1.6 Objetivos Organizacionales")
    agregar_parrafo_normado(doc, "Entre sus objetivos organizacionales se encuentran:")
    objs_org = getattr(c, 'OBJETIVOS_ORG', [])
    for i, objetivo in enumerate(objs_org, 1):
        agregar_item_lista(doc, i, objetivo)

    agregar_titulo_nivel3(doc, "1.1.7 Ubicación geográfica")
    agregar_parrafo_normado(doc, getattr(c, 'UBICACION', 'Ubicación no proporcionada.'), sangria=False)

    carpeta_imagenes = getattr(c, 'CARPETA_IMAGENES', 'imagenes')
    ruta_imagen_1 = buscar_imagen_por_numero(carpeta_imagenes, 1)
    agregar_imagen(doc, ruta_imagen_1, "Gráfico 1. Representación cartográfica y ubicación espacial de la empresa.", ancho=Cm(5))

    agregar_titulo_nivel3(doc, "1.1.8 Población de los trabajadores de la empresa")
    poblacion_data = getattr(c, 'POBLACION', '')
    if isinstance(poblacion_data, str):
        agregar_parrafo_normado(doc, poblacion_data)
    else:
        for parrafo in poblacion_data:
            agregar_parrafo_normado(doc, parrafo)

    agregar_titulo_nivel3(doc, "1.1.9 Estructura Organizativa")
    agregar_parrafo_normado(doc, getattr(c, 'ORGANIGRAMA_TEXTO', 'Estructura organizativa.'))

    ruta_imagen_2 = buscar_imagen_por_numero(carpeta_imagenes, 2)
    agregar_imagen(doc, ruta_imagen_2, "Gráfico 2. Organigrama estructural y niveles jerárquicos de la organización.", ancho=Cm(12))

    # --- CAPÍTULO II: DIAGNÓSTICO SITUACIONAL ---
    iniciar_capitulo(doc, "II", "DIAGNÓSTICO SITUACIONAL")
    agregar_titulo_nivel2(doc, "Identificación de la Situación Problemática")
    situacion_problematica = getattr(c, 'SITUACION_PROBLEMATICA', [])
    if isinstance(situacion_problematica, str):
        agregar_parrafo_normado(doc, situacion_problematica)
    else:
        for parrafo in situacion_problematica:
            agregar_parrafo_normado(doc, parrafo)

    agregar_titulo_nivel2(doc, "Objetivo General")
    agregar_parrafo_normado(doc, getattr(c, 'OBJETIVO_GENERAL', 'Objetivo general no proporcionado.'))

    agregar_titulo_nivel2(doc, "Objetivos Específicos")
    objs_especificos = getattr(c, 'OBJETIVOS_ESPECIFICOS', [])
    for i, obj in enumerate(objs_especificos, 1):
        agregar_item_lista(doc, i, obj)

    agregar_titulo_nivel2(doc, "Planificación integral de objetivos")
    agregar_parrafo_normado(doc, "La planificación establece la relación entre cada objetivo y las actividades administrativas a ejecutar:")
    agregar_tabla_planificacion(doc, getattr(c, 'PLANIFICACION_DATOS', []), titulo_cuadro="Cuadro 1. Planificación integral de objetivos específicos.")
    doc.add_paragraph()

    agregar_titulo_nivel2(doc, "Cronograma de actividades")
    agregar_parrafo_normado(doc, "El cronograma estructura temporalmente las tareas administrativas garantizando el cumplimiento del manual documental propuesto:")
    agregar_gantt(doc, getattr(c, 'CRONOGRAMA_DATOS', []), titulo_cuadro="Cuadro 2. Cronograma de actividades administrativas.")
    doc.add_paragraph()

    # --- CAPÍTULO III: MARCO TEÓRICO ---
    iniciar_capitulo(doc, "III", "MARCO TEÓRICO")
    agregar_titulo_nivel2(doc, "Bases Teóricas Referenciales")
    bases_teoricas = getattr(c, 'BASES_TEORICAS_PARRAFOS', ['Bases teóricas referenciales.'])
    for parrafo in bases_teoricas:
        agregar_parrafo_normado(doc, parrafo)

    if hasattr(c, 'CITA_LARGA_TEXTO') and c.CITA_LARGA_TEXTO:
        agregar_cita_larga(doc, c.CITA_LARGA_TEXTO, getattr(c, 'CITA_LARGA_AUTOR', ''))
        agregar_parrafo_normado(doc, "De acuerdo a la cita previa, se comprende la relevancia del control sistemático y la inmutabilidad de los registros en los departamentos estratégicos de la empresa.", sangria=True)

    # --- CAPÍTULO IV: ACTIVIDADES REALIZADAS ---
    iniciar_capitulo(doc, "IV", "ACTIVIDADES REALIZADAS")
    agregar_titulo_nivel2(doc, "Descripción de Actividades Ejecutadas por Semana")
    agregar_parrafo_normado(doc, getattr(c, 'ACTIVIDADES_DESCRIPCION', 'Descripción de actividades ejecutadas.'))
    actividades_lista = getattr(c, 'ACTIVIDADES_LISTA', [])
    for i, actividad in enumerate(actividades_lista, 1):
        agregar_item_lista(doc, i, actividad)

    # --- CAPÍTULO V: CONCLUSIONES Y RECOMENDACIONES ---
    iniciar_capitulo(doc, "V", "CONCLUSIONES Y RECOMENDACIONES")
    agregar_titulo_nivel2(doc, "Conclusiones")
    conclusiones = getattr(c, 'CONCLUSIONES', [])
    for i, conclusion in enumerate(conclusiones, 1):
        agregar_item_lista(doc, i, conclusion)

    agregar_titulo_nivel2(doc, "Recomendaciones")
    recomendaciones = getattr(c, 'RECOMENDACIONES', [])
    for i, recomendacion in enumerate(recomendaciones, 1):
        agregar_item_lista(doc, i, recomendacion)

    # --- REFERENCIAS BIBLIOGRÁFICAS ---
    iniciar_seccion_preliminar(doc, "REFERENCIAS")
    p_sep = doc.add_paragraph()
    p_sep.paragraph_format.space_before = Pt(24)
    p_sep.paragraph_format.space_after = Pt(0)
    referencias_lista = getattr(c, 'REFERENCIAS_LISTA', [])
    for ref in referencias_lista:
        agregar_referencia(doc, ref)

    # --- ANEXOS ---
    if hasattr(c, 'ANEXOS_LISTA') and c.ANEXOS_LISTA:
        # Portadilla de ANEXOS (Art. 26: una hoja sola con la palabra ANEXOS centrada y en negrita)
        sec_portadilla = doc.add_section(WD_SECTION_START.NEW_PAGE)
        sec_portadilla.top_margin = Cm(5) # Centrado verticalmente aproximado usando margen
        sec_portadilla.bottom_margin = Cm(3)
        sec_portadilla.left_margin = Cm(4)
        sec_portadilla.right_margin = Cm(3)
        sec_portadilla.different_first_page_header_footer = True
        
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        # Empujar hacia el centro vertical aproximado de la página
        p.paragraph_format.space_before = Pt(180)
        run_anexos_tit = p.add_run("ANEXOS")
        run_anexos_tit.font.name = 'Times New Roman'
        run_anexos_tit.font.size = Pt(16) # Un poco más grande para portadilla
        run_anexos_tit.font.bold = True

        # Anexos individuales (Art. 15: cada uno en página nueva, arriba y centrado, subtítulo entre corchetes)
        for cod, desc in c.ANEXOS_LISTA:
            sec_anexo = doc.add_section(WD_SECTION_START.NEW_PAGE)
            sec_anexo.top_margin = Cm(5) # Margen de 5cm para inicio de parte/capítulo/sección nueva
            sec_anexo.bottom_margin = Cm(3)
            sec_anexo.left_margin = Cm(4)
            sec_anexo.right_margin = Cm(3)
            sec_anexo.different_first_page_header_footer = True
            
            p_anexo = doc.add_paragraph()
            p_anexo.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_anexo.paragraph_format.space_before = Pt(0)
            p_anexo.paragraph_format.space_after = Pt(24)
            
            # Nombre del Anexo (ej: ANEXO A)
            run_cod = p_anexo.add_run(cod.upper())
            run_cod.font.name = 'Times New Roman'
            run_cod.font.size = Pt(12)
            run_cod.font.bold = True
            
            # Subtítulo del contenido centrado entre corchetes [ ]
            p_sub = doc.add_paragraph()
            p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_sub.paragraph_format.space_before = Pt(12)
            p_sub.paragraph_format.space_after = Pt(24)
            
            run_desc = p_sub.add_run(f"[{desc}]")
            run_desc.font.name = 'Times New Roman'
            run_desc.font.size = Pt(12)
            run_desc.font.bold = True
            
            # Párrafo de demostración vacío para cumplir la estructura visual
            p_demo = doc.add_paragraph()
            p_demo.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run_demo = p_demo.add_run("(Contenido elaborado por el estudiante)")
            run_demo.font.name = 'Times New Roman'
            run_demo.font.size = Pt(10)
            run_demo.font.italic = True

    return idx_cap1

# ================================================================
#  EJECUCIÓN PRINCIPAL
# ================================================================

def generar_reporte_completo():
    print("» Inicializando documento...")
    doc = setup_iutecp_document()
    
    # 1. Portada (Sección 0)
    construir_portada(doc)
    
    # 2. Contraportada (Sección 1)
    sec_contra = doc.add_section(WD_SECTION_START.NEW_PAGE)
    sec_contra.top_margin = Cm(3)
    sec_contra.bottom_margin = Cm(3)
    sec_contra.left_margin = Cm(4)
    sec_contra.right_margin = Cm(3)
    sec_contra.different_first_page_header_footer = True
    construir_portada(doc)
    
    # 3. Cuerpo (Sección 2 en adelante)
    idx_cap1 = construir_cuerpo_documento(doc)
    
    # Aplicar la numeración de página correcta en base al índice dinámico del Capítulo I
    agregar_numeracion_pie(doc, idx_inicio_cuerpo=idx_cap1)

    docx_output = "Informe_Pasantia_IUTECP.docx"
    doc.save(docx_output)
    print(f"✔ Archivo Word generado: {docx_output}")

    print("» Renderizando PDF usando LibreOffice...")
    soffice_cmd = 'libreoffice'
    if platform.system() == 'Windows':
        possible_paths = [
            r"C:\Program Files\LibreOffice\program\soffice.exe",
            r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
        ]
        for path in possible_paths:
            if os.path.exists(path):
                soffice_cmd = path
                break

    try:
        subprocess.run([soffice_cmd, '--headless', '--convert-to', 'pdf', docx_output], check=True, stdout=subprocess.DEVNULL)
        print("✔ ¡PDF generado con éxito!")
    except FileNotFoundError:
        print("❌ Error: LibreOffice no está instalado o no se encontró en el PATH.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en la conversión a PDF: {e}")

if __name__ == "__main__":
    generar_reporte_completo()
