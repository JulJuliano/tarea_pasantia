#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import shutil
import glob
import subprocess
import argparse
import socket
import tempfile

# Intentamos importar módulos de terminal interactiva (solo Linux/Unix)
try:
    import termios
    import tty
    SOPORTE_TTY = True
except ImportError:
    SOPORTE_TTY = False

# Configuración de carpetas y archivos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GENERATOR_SCRIPT = os.path.join(BASE_DIR, "generador_informe.py")
ARCHIVO_CONTENIDO = "contenido.py"
ARCHIVO_CRONOGRAMA = "cronograma.py"
CARPETA_REPORTES = "reportes"
CARPETA_IMAGENES = "imagenes"
CARPETA_CRONOGRAMAS = "cronogramas"
PATRON_CRONOGRAMAS = "Cronograma_*.*"
NOMBRE_DOCX_SALIDA = "Informe_Pasantia_IUTECP.docx"
NOMBRE_PDF_SALIDA = "Informe_Pasantia_IUTECP.pdf"

CONFIGURACIONES_COMBINACION = {
    "juliano": {
        "patron": "Cronograma_Informatica_Semana{semana}_IUTECP.docx",
        "semanas": 9,
    },
    "keidy": {
        "patron": "Cronograma_Procura_Semana{semana}_IUTECP.docx",
        "semanas": 10,
    },
    "amaal": {
        "patron": "Cronograma_Administracion_Semana{semana}_IUTECP.docx",
        "semanas": 10,
    },
}

# Excluir del escaneo de estudiantes: carpetas especiales del repositorio
CARPETAS_EXCLUIDAS = {"venv", "compartido", "__pycache__", ".git", ".venv", "env"}

# Buscar el ejecutable de Python del venv de forma prioritaria para evitar ModuleNotFoundError
PYTHON_EXEC = sys.executable
for vp in [
    os.path.join(BASE_DIR, "venv", "bin", "python"),
    *[os.path.join(BASE_DIR, d, "venv", "bin", "python") for d in os.listdir(BASE_DIR)
      if os.path.isdir(os.path.join(BASE_DIR, d))],
]:
    if os.path.exists(vp):
        PYTHON_EXEC = vp
        break

# Estudiantes: se detectan dinámicamente como toda subcarpeta con contenido.py o cronograma.py
def _detectar_estudiantes():
    """Escanea BASE_DIR y devuelve la lista de estudiantes con contenido.py o cronograma.py."""
    estudiantes = []
    for nombre in sorted(os.listdir(BASE_DIR)):
        ruta = os.path.join(BASE_DIR, nombre)
        if not os.path.isdir(ruta) or nombre in CARPETAS_EXCLUIDAS or nombre.startswith('.'):
            continue
        contenido = os.path.join(ruta, ARCHIVO_CONTENIDO)
        cronograma = os.path.join(ruta, ARCHIVO_CRONOGRAMA)
        if os.path.exists(contenido) or os.path.exists(cronograma):
            estudiantes.append({
                "id": nombre.lower(),
                "nombre": nombre.capitalize(),
                "dir": ruta,
                "source_content": contenido,
                "cronograma_script": cronograma,
            })
    return estudiantes

ESTUDIANTES = _detectar_estudiantes()

# Acciones globales
ACCIONES = [
    {"id": "informe", "nombre": "Compilar Informe de Pasantía (.docx y .pdf)", "def": True},
    {"id": "borrador1", "nombre": "Compilar Borrador 1 (solo Cap I)", "def": False},
    {"id": "borrador2", "nombre": "Compilar Borrador 2 (Cap I + II)", "def": False},
    {"id": "borrador3", "nombre": "Compilar Borrador 3 (Cap I + II + III)", "def": False},
    {"id": "borrador4", "nombre": "Compilar Borrador 4 (Cap I + II + III + IV)", "def": False},
    {"id": "cronogramas", "nombre": "Compilar Cronogramas Semanales (.docx y .pdf)", "def": True},
    {"id": "combinar_documentos", "nombre": "Combinar informe + cronogramas (.docx y .pdf)", "def": False}
]

# Códigos de escape ANSI para colores y formato
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[38;2;46;204;113m"
BLUE = "\033[38;2;52;152;219m"
YELLOW = "\033[38;2;241;196;15m"
RED = "\033[38;2;231;76;60m"
CYAN = "\033[38;2;26;188;156m"
GRAY = "\033[38;2;127;140;141m"

def obtener_tecla():
    """Lee una tecla del teclado en modo raw para interactividad instantánea."""
    if not SOPORTE_TTY or not sys.stdin.isatty():
        return '\n' # Retorno de nueva línea por defecto si no es TTY
        
    fd = sys.stdin.fileno()
    try:
        old_settings = termios.tcgetattr(fd)
    except Exception:
        return '\n'
        
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
        if ch == '\x1b':
            ch2 = sys.stdin.read(1)
            if ch2 == '[':
                ch3 = sys.stdin.read(1)
                if ch3 == 'A':
                    return 'UP'
                elif ch3 == 'B':
                    return 'DOWN'
        return ch
    finally:
        try:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        except Exception:
            pass

def dibujar_interfaz(indice_cursor, sel_acciones, sel_estudiantes):
    """Renderiza el menú interactivo con selección de acciones y estudiantes."""
    os.system("clear")
    print(f"{BOLD}{BLUE}================================================================{RESET}")
    print(f"{BOLD}{CYAN}             IUTECP - PANEL DE CONTROL MULTI-COMPILACIÓN         {RESET}")
    print(f"{BOLD}{BLUE}================================================================{RESET}")
    print(f"{GRAY}Usa las flechas {BOLD}↑ / ↓{RESET}{GRAY} para moverte, {BOLD}Espacio{RESET}{GRAY} para marcar/desmarcar y {BOLD}Enter{RESET}{GRAY} para iniciar.{RESET}")
    print()

    # RENDERIZADO DE ACCIONES
    print(f"{BOLD}{YELLOW}1. Seleccione las acciones a realizar:{RESET}")
    total_acciones = len(ACCIONES)
    for i, acc in enumerate(ACCIONES):
        is_cursor = i == indice_cursor
        cursor = f"{BLUE}➔{RESET} " if is_cursor else "  "
        check = f"[{GREEN}✔{RESET}]" if sel_acciones[i] else "[ ]"
        lbl_color = f"{BOLD}{CYAN if sel_acciones[i] else RESET}{acc['nombre']}{RESET}"
        print(f"{cursor}{check} {lbl_color}")
    print()

    # RENDERIZADO DE ESTUDIANTES
    print(f"{BOLD}{YELLOW}2. Seleccione los estudiantes a procesar:{RESET}")
    # Mapa id_accion -> índice en sel_acciones para evitar hardcodeo de [0]/[1]
    idx_accion = {ACCIONES[i]["id"]: i for i in range(len(ACCIONES))}
    for i, est in enumerate(ESTUDIANTES):
        global_idx = total_acciones + i
        is_cursor = global_idx == indice_cursor
        cursor = f"{BLUE}➔{RESET} " if is_cursor else "  "
        check = f"[{GREEN}✔{RESET}]" if sel_estudiantes[i] else "[ ]"
        
        # Estado de archivos: muestra advertencia si la acción activa no encuentra el archivo
        has_content = os.path.exists(est["source_content"])
        has_crono = os.path.exists(est["cronograma_script"])
        
        status_lbl = ""
        if not has_content and sel_acciones[idx_accion.get("informe", -1)]:
            status_lbl += f" {RED}(Sin contenido.py){RESET}"
        if not has_crono and sel_acciones[idx_accion.get("cronogramas", -1)]:
            status_lbl += f" {RED}(Sin cronograma.py){RESET}"
        if sel_acciones[idx_accion.get("combinar_documentos", -1)] and est["id"] not in CONFIGURACIONES_COMBINACION:
            status_lbl += f" {GRAY}(Combinación no configurada){RESET}"

        nombre_color = f"{BOLD}{GREEN if sel_estudiantes[i] else RESET}{est['nombre']}{RESET}"
        print(f"{cursor}{check} {nombre_color}{status_lbl}")
        print()

    print(f"{BOLD}{BLUE}================================================================{RESET}")
    print(f"{GRAY}Presiona {BOLD}Q{RESET}{GRAY} para salir.{RESET}")

def compilar_informe_estudiante(est, modo="completo"):
    """Genera el informe de un estudiante y lo mueve a su carpeta de reportes.
    
    modo: "completo" | "borrador1" (solo Cap I) | "borrador2" (Cap I+II) |
          "borrador3" (Cap I+II+III) | "borrador4" (Cap I+II+III+IV)
    """
    modo_label = {"completo": "Informe Completo", "borrador1": "Borrador 1 (Cap I)", "borrador2": "Borrador 2 (Cap I+II)", "borrador3": "Borrador 3 (Cap I+II+III)", "borrador4": "Borrador 4 (Cap I+II+III+IV)"}.get(modo, modo)
    print(f"\n{BOLD}{CYAN}» Generando {modo_label} para {est['nombre']}...{RESET}")
    
    if not os.path.exists(est["source_content"]):
        print(f"{RED}⚠ Omitido: No se encontró contenido.py para {est['nombre']} en:{RESET}")
        print(f"  {est['source_content']}")
        return False

    raiz_content = os.path.join(BASE_DIR, ARCHIVO_CONTENIDO)
    respaldo_content = os.path.join(BASE_DIR, ".contenido_respaldo_temp.py")
    tiene_respaldo = False
    
    raiz_imagenes = os.path.join(BASE_DIR, CARPETA_IMAGENES)
    respaldo_imagenes = os.path.join(BASE_DIR, ".imagenes_respaldo_temp")
    est_imagenes = os.path.join(est["dir"], CARPETA_IMAGENES)
    copio_imagenes = False
    tiene_respaldo_imagenes = False
    
    if os.path.exists(raiz_content):
        shutil.copy2(raiz_content, respaldo_content)
        tiene_respaldo = True

    # Respaldar carpeta imagenes de la raíz si existe
    if os.path.exists(raiz_imagenes):
        shutil.move(raiz_imagenes, respaldo_imagenes)
        tiene_respaldo_imagenes = True

    try:
        # Copiar contenido.py a la raíz
        shutil.copy2(est["source_content"], raiz_content)
        
        # Copiar carpeta imagenes del estudiante a la raíz si existe
        if os.path.exists(est_imagenes):
            shutil.copytree(est_imagenes, raiz_imagenes)
            copio_imagenes = True
        
        # Ejecutar generador_informe.py
        print(f"{GRAY}Ejecutando generador_informe.py...{RESET}")
        cmd = [PYTHON_EXEC, GENERATOR_SCRIPT]
        if modo == "borrador1":
            cmd.extend(["--modo", "borrador1"])
        elif modo == "borrador2":
            cmd.extend(["--modo", "borrador2"])
        elif modo == "borrador3":
            cmd.extend(["--modo", "borrador3"])
        elif modo == "borrador4":
            cmd.extend(["--modo", "borrador4"])
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        for line in proc.stdout:
            print(f"  {GRAY}{line.strip()}{RESET}")
        proc.wait()
        
        if proc.returncode != 0:
            print(f"{RED}⚠ Error durante la compilación del informe de {est['nombre']}.{RESET}")
            return False

        # Asegurar directorio de destino
        dest_reportes = os.path.join(est["dir"], CARPETA_REPORTES)
        os.makedirs(dest_reportes, exist_ok=True)

        # Mover archivos generados
        if modo == "borrador1":
            sufijo = "_BORRADOR1"
        elif modo == "borrador2":
            sufijo = "_BORRADOR2"
        elif modo == "borrador3":
            sufijo = "_BORRADOR3"
        elif modo == "borrador4":
            sufijo = "_BORRADOR4"
        else:
            sufijo = ""
        docx_name = f"Informe_Pasantia_IUTECP{sufijo}.docx"
        pdf_name = f"Informe_Pasantia_IUTECP{sufijo}.pdf"
        docx_src = os.path.join(BASE_DIR, docx_name)
        pdf_src = os.path.join(BASE_DIR, pdf_name)
        modo_label = {"completo": "Informe", "borrador": "Borrador"}.get(modo, "Informe")
        
        docx_dest = os.path.join(dest_reportes, docx_name)
        pdf_dest = os.path.join(dest_reportes, pdf_name)
        
        if os.path.exists(docx_src):
            shutil.move(docx_src, docx_dest)
            print(f"{GREEN}✔ {modo_label} Word guardado en: {docx_dest}{RESET}")
        if os.path.exists(pdf_src):
            shutil.move(pdf_src, pdf_dest)
            print(f"{GREEN}✔ {modo_label} PDF guardado en: {pdf_dest}{RESET}")
            
        return True
        
    finally:
        # Restaurar respaldo de contenido.py
        if tiene_respaldo:
            shutil.move(respaldo_content, raiz_content)
        elif os.path.exists(raiz_content):
            os.remove(raiz_content)
            
        # Limpiar carpeta imagenes copiada a la raíz
        if copio_imagenes and os.path.exists(raiz_imagenes):
            shutil.rmtree(raiz_imagenes)
            
        # Restaurar la carpeta imagenes original si existía
        if tiene_respaldo_imagenes:
            shutil.move(respaldo_imagenes, raiz_imagenes)

def compilar_cronogramas_estudiante(est):
    """Ejecuta el script de cronograma de un estudiante y organiza los archivos resultantes."""
    print(f"\n{BOLD}{CYAN}» Generando Cronogramas para {est['nombre']}...{RESET}")
    
    if not os.path.exists(est["cronograma_script"]):
        print(f"{RED}⚠ Omitido: No se encontró cronograma.py para {est['nombre']}.{RESET}")
        return False

    crono_dir = est["dir"]
    script_name = os.path.basename(est["cronograma_script"])

    # Ejecutar en el subdirectorio del estudiante
    print(f"{GRAY}Ejecutando {script_name} en {crono_dir}...{RESET}")
    try:
        proc = subprocess.Popen(
            [PYTHON_EXEC, script_name],
            cwd=crono_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        for line in proc.stdout:
            print(f"  {GRAY}{line.strip()}{RESET}")
        proc.wait()

        if proc.returncode != 0:
            print(f"{RED}⚠ Error en la ejecución de {script_name}.{RESET}")
            return False

        # Asegurar directorio de destino para cronogramas
        dest_cronos = os.path.join(crono_dir, CARPETA_CRONOGRAMAS)
        os.makedirs(dest_cronos, exist_ok=True)

        # Buscar todos los archivos generados en cualquier subcarpeta de forma recursiva
        archivos_generados = glob.glob(os.path.join(crono_dir, "**", PATRON_CRONOGRAMAS), recursive=True)
        
        movidos = 0
        for src in archivos_generados:
            basename = os.path.basename(src)
            dest = os.path.join(dest_cronos, basename)
            
            # Evitar procesar archivos que ya están en la carpeta de destino final
            rel_path = src.replace(crono_dir + "/", "")
            if rel_path.startswith(CARPETA_CRONOGRAMAS + "/"):
                continue
                
            shutil.move(src, dest)
            movidos += 1

        # Limpiar la carpeta temporal 'cronogramas generados' si quedó vacía
        crono_gen_dir = os.path.join(crono_dir, "cronogramas generados")
        if os.path.exists(crono_gen_dir) and not os.listdir(crono_gen_dir):
            os.rmdir(crono_gen_dir)

        print(f"{GREEN}✔ Se procesaron y organizaron {movidos} archivos de cronogramas en: {dest_cronos}{RESET}")
        return True

    except Exception as e:
        print(f"{RED}⚠ Error ejecutando cronogramas: {e}{RESET}")
        return False

def _buscar_python_con_uno():
    """Busca un Python del sistema con el puente UNO de LibreOffice."""
    candidatos = ["/usr/bin/python3", shutil.which("python3"), sys.executable]
    revisados = set()
    for candidato in candidatos:
        if not candidato or candidato in revisados or not os.path.exists(candidato):
            continue
        revisados.add(candidato)
        prueba = subprocess.run(
            [candidato, "-c", "import uno"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if prueba.returncode == 0:
            return candidato
    return None

def combinar_informe_cronogramas(est):
    """Combina el informe y los cronogramas configurados del estudiante."""
    configuracion = CONFIGURACIONES_COMBINACION.get(est["id"])
    if configuracion is None:
        print(f"{GRAY}» Combinación omitida para {est['nombre']}: no está configurada.{RESET}")
        return None

    patron_cronograma = configuracion["patron"]
    total_semanas = configuracion["semanas"]

    informe = os.path.join(est["dir"], CARPETA_REPORTES, NOMBRE_DOCX_SALIDA)
    cronogramas = [
        os.path.join(
            est["dir"],
            CARPETA_CRONOGRAMAS,
            patron_cronograma.format(semana=semana),
        )
        for semana in range(1, total_semanas + 1)
    ]
    fuentes = [informe, *cronogramas]
    faltantes = [ruta for ruta in fuentes if not os.path.isfile(ruta)]
    if faltantes:
        print(f"{RED}⚠ No se puede crear el Word combinado. Faltan estos archivos:{RESET}")
        for ruta in faltantes:
            print(f"  {ruta}")
        return False

    python_uno = _buscar_python_con_uno()
    soffice = shutil.which("libreoffice") or shutil.which("soffice")
    if not python_uno or not soffice:
        print(f"{RED}⚠ Se requiere LibreOffice y un Python del sistema con el módulo UNO.{RESET}")
        return False

    salida_docx = os.path.join(
        est["dir"],
        CARPETA_REPORTES,
        "Informe_Pasantia_IUTECP_con_Cronogramas.docx",
    )
    salida_pdf = os.path.join(
        est["dir"],
        CARPETA_REPORTES,
        "Informe_Pasantia_IUTECP_con_Cronogramas.pdf",
    )

    with socket.socket() as servidor:
        servidor.bind(("127.0.0.1", 0))
        puerto = servidor.getsockname()[1]

    perfil = tempfile.mkdtemp(prefix="selector_libreoffice_")
    perfil_url = "file://" + perfil
    office_proc = subprocess.Popen(
        [
            soffice,
            "--headless",
            "--nologo",
            "--nodefault",
            "--nofirststartwizard",
            "--norestore",
            f"-env:UserInstallation={perfil_url}",
            f"--accept=socket,host=127.0.0.1,port={puerto};urp;StarOffice.ComponentContext",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    script_uno = r'''
import os
import sys
import time
import uno
from com.sun.star.beans import PropertyValue
from com.sun.star.style.BreakType import PAGE_BEFORE
from com.sun.star.text.ControlCharacter import PARAGRAPH_BREAK

def propiedad(nombre, valor):
    prop = PropertyValue()
    prop.Name = nombre
    prop.Value = valor
    return prop

puerto = int(sys.argv[1])
salida_docx = os.path.abspath(sys.argv[2])
salida_pdf = os.path.abspath(sys.argv[3])
fuentes = [os.path.abspath(ruta) for ruta in sys.argv[4:]]
contexto_local = uno.getComponentContext()
resolver = contexto_local.ServiceManager.createInstanceWithContext(
    "com.sun.star.bridge.UnoUrlResolver", contexto_local
)

contexto = None
for _ in range(60):
    try:
        contexto = resolver.resolve(
            f"uno:socket,host=127.0.0.1,port={puerto};urp;StarOffice.ComponentContext"
        )
        break
    except Exception:
        time.sleep(0.25)
if contexto is None:
    raise RuntimeError("No se pudo conectar con LibreOffice.")

desktop = contexto.ServiceManager.createInstanceWithContext(
    "com.sun.star.frame.Desktop", contexto
)
documento = desktop.loadComponentFromURL(
    uno.systemPathToFileUrl(fuentes[0]),
    "_blank",
    0,
    (propiedad("Hidden", True),),
)
if documento is None:
    raise RuntimeError("No se pudo abrir el informe del estudiante.")

try:
    texto = documento.Text
    for fuente in fuentes[1:]:
        cursor = texto.createTextCursor()
        cursor.gotoEnd(False)
        texto.insertControlCharacter(cursor, PARAGRAPH_BREAK, False)
        cursor.gotoEnd(False)
        cursor.BreakType = PAGE_BEFORE
        cursor.insertDocumentFromURL(uno.systemPathToFileUrl(fuente), ())

    documento.storeAsURL(
        uno.systemPathToFileUrl(salida_docx),
        (
            propiedad("FilterName", "Office Open XML Text"),
            propiedad("Overwrite", True),
        ),
    )
    documento.storeToURL(
        uno.systemPathToFileUrl(salida_pdf),
        (
            propiedad("FilterName", "writer_pdf_Export"),
            propiedad("Overwrite", True),
        ),
    )
finally:
    documento.close(True)
'''

    print(f"\n{BOLD}{CYAN}» Combinando informe y cronogramas de {est['nombre']}...{RESET}")
    try:
        resultado = subprocess.run(
            [python_uno, "-c", script_uno, str(puerto), salida_docx, salida_pdf, *fuentes],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=240,
        )
        if resultado.returncode != 0 or not os.path.isfile(salida_docx) or not os.path.isfile(salida_pdf):
            detalle = resultado.stdout.strip()
            print(f"{RED}⚠ No se pudieron crear los documentos combinados.{RESET}")
            if detalle:
                print(f"  {detalle}")
            return False
        print(f"{GREEN}✔ Word combinado guardado en: {salida_docx}{RESET}")
        print(f"{GREEN}✔ PDF combinado guardado en: {salida_pdf}{RESET}")
        return True
    except subprocess.TimeoutExpired:
        print(f"{RED}⚠ LibreOffice excedió el tiempo límite al combinar los documentos.{RESET}")
        return False
    finally:
        office_proc.terminate()
        try:
            office_proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            office_proc.kill()
        shutil.rmtree(perfil, ignore_errors=True)

def main():
    # Procesamiento de argumentos
    parser = argparse.ArgumentParser(description="Selector y compilador de informes IUTECP.")
    parser.add_argument("--estudiantes", type=str, help="Estudiantes a procesar separados por comas (juliano, keidy, amaal, all)")
    parser.add_argument("--acciones", type=str, help="Acciones separadas por comas (informe, cronogramas, combinar_documentos, all)")
    args = parser.parse_args()

    # Determinar si usamos modo interactivo o directo
    usar_interactivo = sys.stdin.isatty() and not (args.estudiantes or args.acciones)

    # Estado de selecciones por defecto
    sel_acciones = [acc["def"] for acc in ACCIONES]
    sel_estudiantes = [False] * len(ESTUDIANTES)
    sel_estudiantes[0] = True # Juliano por defecto

    if usar_interactivo:
        # Modo interactivo TTY
        total_opciones = len(ACCIONES) + len(ESTUDIANTES)
        indice_cursor = 0

        while True:
            dibujar_interfaz(indice_cursor, sel_acciones, sel_estudiantes)
            tecla = obtener_tecla()
            
            if tecla == 'UP':
                indice_cursor = (indice_cursor - 1) % total_opciones
            elif tecla == 'DOWN':
                indice_cursor = (indice_cursor + 1) % total_opciones
            elif tecla == ' ':
                if indice_cursor < len(ACCIONES):
                    sel_acciones[indice_cursor] = not sel_acciones[indice_cursor]
                else:
                    est_idx = indice_cursor - len(ACCIONES)
                    sel_estudiantes[est_idx] = not sel_estudiantes[est_idx]
            elif tecla in ('\r', '\n'):
                break
            elif tecla in ('q', 'Q', '\x03'):
                print("\nSaliendo del selector...")
                sys.exit(0)
    else:
        # Modo automático / Argumentos de consola
        if args.acciones:
            acts = args.acciones.lower().split(",")
            if "all" in acts:
                sel_acciones = [True] * len(ACCIONES)
            else:
                for idx, acc in enumerate(ACCIONES):
                    sel_acciones[idx] = acc["id"] in acts
        
        if args.estudiantes:
            ests = args.estudiantes.lower().split(",")
            if "all" in ests:
                sel_estudiantes = [True] * len(ESTUDIANTES)
            else:
                for idx, est_cfg in enumerate(ESTUDIANTES):
                    sel_estudiantes[idx] = est_cfg["id"] in ests
        # Si no es interactiva y no se pasan argumentos, compila el primer estudiante por defecto

    # Resolver listas finales
    acciones_a_ejecutar = [ACCIONES[i]["id"] for i, sel in enumerate(sel_acciones) if sel]
    estudiantes_a_procesar = [ESTUDIANTES[i] for i, sel in enumerate(sel_estudiantes) if sel]

    if not acciones_a_ejecutar:
        print(f"\n{YELLOW}No se seleccionó ninguna acción a realizar.{RESET}")
        sys.exit(0)
    if not estudiantes_a_procesar:
        print(f"\n{YELLOW}No se seleccionó ningún estudiante para procesar.{RESET}")
        sys.exit(0)

    # Procesar
    print(f"\n{BOLD}{BLUE}================================================================{RESET}")
    print(f"{BOLD}{CYAN}INICIANDO PROCESAMIENTO MULTI-COMPILACIÓN{RESET}")
    print(f"{BOLD}{BLUE}================================================================{RESET}")
    
    exito_total = 0
    errores_totales = 0

    for est in estudiantes_a_procesar:
        print(f"\n{BOLD}{YELLOW}➔ PROCESANDO GRUPO: {est['nombre'].upper()}{RESET}")
        
        # 1. Compilar informe completo si aplica
        if "informe" in acciones_a_ejecutar:
            if compilar_informe_estudiante(est, modo="completo"):
                exito_total += 1
            else:
                errores_totales += 1

        # 2. Compilar borradores si aplica
        for bid, bnombre in [("borrador1", "borrador1"), ("borrador2", "borrador2"), ("borrador3", "borrador3"), ("borrador4", "borrador4")]:
            if bid in acciones_a_ejecutar:
                if compilar_informe_estudiante(est, modo=bnombre):
                    exito_total += 1
                else:
                    errores_totales += 1
                
        # 3. Compilar cronogramas si aplica
        if "cronogramas" in acciones_a_ejecutar:
            if compilar_cronogramas_estudiante(est):
                exito_total += 1
            else:
                errores_totales += 1

        # 4. Combinar informe y cronogramas del estudiante si aplica
        if "combinar_documentos" in acciones_a_ejecutar:
            resultado_combinacion = combinar_informe_cronogramas(est)
            if resultado_combinacion is True:
                exito_total += 1
            elif resultado_combinacion is False:
                errores_totales += 1

    print(f"\n{BOLD}{BLUE}================================================================{RESET}")
    print(f"{BOLD}{GREEN}PROCESO COMPLETADO{RESET}")
    print(f"  Tareas exitosas: {GREEN}{exito_total}{RESET}")
    if errores_totales > 0:
        print(f"  Tareas fallidas: {RED}{errores_totales}{RESET}")
    print(f"{BOLD}{BLUE}================================================================{RESET}")

if __name__ == "__main__":
    main()
