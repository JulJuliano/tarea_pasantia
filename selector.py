#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import shutil
import subprocess
import termios
import tty

# Configuración de carpetas y archivos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GENERATOR_SCRIPT = os.path.join(BASE_DIR, "generador_informe.py")
PYTHON_EXEC = sys.executable  # Usa el intérprete actual (incluyendo venv si está activo)

OPCIONES = [
    {
        "id": "juliano",
        "nombre": "Juliano",
        "desc": "Informe de Pasantía en Venangocupet (SQLite/TUI)",
        "source_content": os.path.join(BASE_DIR, "juliano", "contenido.py"),
        "dest_dir": os.path.join(BASE_DIR, "juliano")
    },
    {
        "id": "amaal",
        "nombre": "Amaal",
        "desc": "Informe de Pasantía en Administración (Pendiente contenido.py)",
        "source_content": os.path.join(BASE_DIR, "amaal", "contenido.py"),
        "dest_dir": os.path.join(BASE_DIR, "amaal")
    },
    {
        "id": "keidy",
        "nombre": "Keidy",
        "desc": "Informe de Pasantía sobre Manuales Administrativos",
        "source_content": os.path.join(BASE_DIR, "keidy", "contenido.py"),
        "dest_dir": os.path.join(BASE_DIR, "keidy")
    }
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
DARK_GRAY = "\033[38;2;44;62;80m"

def obtener_tecla():
    """Lee una tecla del teclado en modo raw para interactividad instantánea."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
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
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def dibujar_interfaz(indice_cursor, seleccionados):
    """Renderiza el menú interactivo en la terminal con una estética premium."""
    os.system("clear")
    print(f"{BOLD}{BLUE}================================================================{RESET}")
    print(f"{BOLD}{CYAN}             IUTECP - SELECTOR MULTI-COMPILACIÓN                {RESET}")
    print(f"{BOLD}{BLUE}================================================================{RESET}")
    print(f"{GRAY}Usa las flechas {BOLD}↑ / ↓{RESET}{GRAY} para moverte, {BOLD}Espacio{RESET}{GRAY} para seleccionar y {BOLD}Enter{RESET}{GRAY} para compilar.{RESET}")
    print()

    for i, opc in enumerate(OPCIONES):
        cursor = f"{BLUE}➔{RESET} " if i == indice_cursor else "  "
        check = f"[{GREEN}✔{RESET}]" if seleccionados[i] else "[ ]"
        
        # Validación de si existe contenido.py para la opción
        existe_src = os.path.exists(opc["source_content"])
        status_lbl = ""
        if not existe_src:
            status_lbl = f" {RED}(Falta contenido.py){RESET}"
            
        nombre_color = f"{BOLD}{GREEN if seleccionados[i] else RESET}{opc['nombre']}{RESET}"
        
        print(f"{cursor}{check} {nombre_color} {status_lbl}")
        print(f"    {GRAY}{opc['desc']}{RESET}")
        print()

    print(f"{BOLD}{BLUE}================================================================{RESET}")
    print(f"{GRAY}Presiona {BOLD}Q{RESET}{GRAY} para salir.{RESET}")

def compilar_proyecto(opcion):
    """Copia el contenido, ejecuta la compilación y mueve los archivos generados."""
    print(f"\n{BOLD}{BLUE}» Iniciando compilación de {opcion['nombre']}...{RESET}")
    
    # 1. Verificar si existe el archivo fuente
    if not os.path.exists(opcion["source_content"]):
        print(f"{RED}⚠ Error: No se encontró el archivo de contenido para {opcion['nombre']} en:{RESET}")
        print(f"  {opcion['source_content']}")
        return False

    # 2. Hacer respaldo del contenido.py raíz si existe
    raiz_content = os.path.join(BASE_DIR, "contenido.py")
    respaldo_content = os.path.join(BASE_DIR, ".contenido_respaldo_temp.py")
    tiene_respaldo = False
    
    if os.path.exists(raiz_content):
        shutil.copy2(raiz_content, respaldo_content)
        tiene_respaldo = True

    try:
        # 3. Copiar el contenido del proyecto a la raíz
        shutil.copy2(opcion["source_content"], raiz_content)
        
        # 4. Ejecutar el compilador
        print(f"{GRAY}Ejecutando generador_informe.py...{RESET}")
        proc = subprocess.Popen(
            [PYTHON_EXEC, GENERATOR_SCRIPT],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        
        # Mostrar el progreso en vivo de la compilación
        for line in proc.stdout:
            print(f"  {GRAY}{line.strip()}{RESET}")
            
        proc.wait()
        
        if proc.returncode != 0:
            print(f"{RED}⚠ Error durante la compilación.{RESET}")
            return False

        # 5. Mover los archivos resultantes a la carpeta destino
        docx_source = os.path.join(BASE_DIR, "Informe_Pasantia_IUTECP.docx")
        pdf_source = os.path.join(BASE_DIR, "Informe_Pasantia_IUTECP.pdf")
        
        docx_dest = os.path.join(opcion["dest_dir"], "Informe_Pasantia_IUTECP.docx")
        pdf_dest = os.path.join(opcion["dest_dir"], "Informe_Pasantia_IUTECP.pdf")
        
        if os.path.exists(docx_source):
            shutil.move(docx_source, docx_dest)
            print(f"{GREEN}✔ Archivo Word guardado en: {docx_dest}{RESET}")
            
        if os.path.exists(pdf_source):
            shutil.move(pdf_source, pdf_dest)
            print(f"{GREEN}✔ Archivo PDF guardado en: {pdf_dest}{RESET}")
            
        return True
        
    finally:
        # 6. Restaurar el contenido.py raíz original
        if tiene_respaldo:
            shutil.move(respaldo_content, raiz_content)
        elif os.path.exists(raiz_content):
            os.remove(raiz_content)

def main():
    # Inicializar estado
    indice_cursor = 0
    seleccionados = [False] * len(OPCIONES)
    
    # Por defecto, si el usuario está corriendo esto, marcar a Juliano
    seleccionados[0] = True

    while True:
        dibujar_interfaz(indice_cursor, seleccionados)
        tecla = obtener_tecla()
        
        if tecla == 'UP':
            indice_cursor = (indice_cursor - 1) % len(OPCIONES)
        elif tecla == 'DOWN':
            indice_cursor = (indice_cursor + 1) % len(OPCIONES)
        elif tecla == ' ':
            seleccionados[indice_cursor] = not seleccionados[indice_cursor]
        elif tecla in ('\r', '\n'):
            break
        elif tecla in ('q', 'Q', '\x03'):  # q, Q o Ctrl+C
            print("\nSaliendo del selector...")
            sys.exit(0)

    # Validar que al menos haya uno seleccionado
    proyectos_a_compilar = [OPCIONES[i] for i, sel in enumerate(seleccionados) if sel]
    if not proyectos_a_compilar:
        print(f"\n{YELLOW}No seleccionaste ningún proyecto para compilar.{RESET}")
        sys.exit(0)

    # Ejecutar compilaciones
    completados = 0
    fallidos = 0
    
    print(f"\n{BOLD}{CYAN}Comenzando compilación de {len(proyectos_a_compilar)} proyectos...{RESET}")
    
    for opc in proyectos_a_compilar:
        exito = compilar_proyecto(opc)
        if exito:
            completados += 1
        else:
            fallidos += 1

    print(f"\n{BOLD}{BLUE}================================================================{RESET}")
    print(f"{BOLD}{GREEN}Compilación finalizada:{RESET}")
    print(f"  Procesados con éxito: {GREEN}{completados}{RESET}")
    if fallidos > 0:
        print(f"  Fallidos/Omitidos: {RED}{fallidos}{RESET}")
    print(f"{BOLD}{BLUE}================================================================{RESET}")

if __name__ == "__main__":
    main()
