# Sistema Multi-Compilador de Informes de Pasantías (IUTECP)

Este proyecto implementa una solución automatizada para la generación de informes y cronogramas de pasantía conformes a la **Normativa de Transcripción de Trabajos e Informes Escritos del IUTECP**. Permite compilar y organizar de manera inteligente los documentos de múltiples estudiantes (**Juliano, Keidy y Amaal**) de forma individual y modular.

---

## 📁 Estructura del Proyecto

El repositorio está organizado con una arquitectura modular y simétrica. Cada estudiante posee su propio directorio aislado, con sus respectivos contenidos, configuraciones e insumos gráficos:

```text
tarea_pasantia/
│
├── generador_informe.py     # Script principal (motor de generación de plantillas DOCX y conversión PDF)
├── selector.py              # Panel de control intercativo y automatizado por CLI
├── .gitignore               # Exclusiones de Git (entornos virtuales, temporales y bloqueos de oficina)
│
├── juliano/                 # Directorio del Proyecto de Juliano (TSU Informática)
│   ├── contenido.py         # Textos, tablas, objetivos y variables de Juliano
│   ├── contexto.md          # Diagnóstico situacional, flujo de correspondencias de Presidencia y metas
│   ├── cronograma.py        # Generador de cronogramas semanales de Juliano
│   ├── reportes/            # Salida del Informe de Pasantías (Generado)
│   │   ├── Informe_Pasantia_IUTECP.docx
│   │   └── Informe_Pasantia_IUTECP.pdf
│   ├── cronogramas/         # Salida de Cronogramas Semanales (Generados)
│   │   ├── Cronograma_Semana1_IUTECP.pdf
│   │   └── ...
│   └── imagenes/            # Insumos gráficos (1.png = Mapa, 2.png = Organigrama)
│
├── keidy/                   # Directorio del Proyecto de Keidy (TSU Informática)
│   ├── contenido.py         # Textos, tablas y variables de Keidy
│   ├── cronograma.py        # Generador de cronogramas semanales de Keidy
│   ├── reportes/            # Salida del Informe de Pasantías (Generado)
│   ├── cronogramas/         # Salida de Cronogramas Semanales (Generados)
│   └── imagenes/            # Insumos gráficos (1.png = Mapa, 2.png = Organigrama)
│
└── amaal/                   # Directorio del Proyecto de Amaal (TSU Administración)
    ├── cronograma.py        # Generador de cronogramas semanales de Amaal
    ├── reportes/            # Salida del Informe de Pasantías (Vacío hasta definir contenido.py)
    ├── cronogramas/         # Salida de Cronogramas Semanales (Generados)
    └── imagenes/            # Insumos gráficos del reporte
```

---

## ⚙️ Panel de Control (`selector.py`)

El script `selector.py` en la raíz del proyecto es el orquestador principal. Cuenta con dos modos de ejecución:

### 1. Modo Interactivo (TUI)
Si lo ejecutas directamente desde una terminal interactiva:
```bash
python selector.py
# o bien:
./selector.py
```
* **Navegación:** Flechas `↑` y `↓` para desplazarte por las opciones.
* **Selección:** Barra espaciadora (`Espacio`) para marcar o desmarcar acciones y estudiantes.
* **Ejecución:** Tecla `Enter` para comenzar el procesamiento.
* **Salida:** Tecla `Q` o `Ctrl+C` para cancelar.

### 2. Modo Directo por Línea de Comandos (CLI / Scripts)
Puedes automatizar las tareas usando argumentos, lo cual es ideal si ejecutas compilaciones desde scripts externos o terminales no interactivas:
```bash
./selector.py --estudiantes <estudiante_id> --acciones <accion_id>
```
* **Argumento `--estudiantes`:** Permite especificar qué estudiantes compilar separados por comas (`juliano`, `keidy`, `amaal`, `all`).
* **Argumento `--acciones`:** Permite especificar qué tareas realizar separadas por comas (`informe`, `cronogramas`, `all`).

**Ejemplos prácticos:**
* Compilar solo el informe de Keidy:
  ```bash
  ./selector.py --estudiantes keidy --acciones informe
  ```
* Compilar todo (informe y cronogramas) para Juliano y Amaal:
  ```bash
  ./selector.py --estudiantes juliano,amaal --acciones all
  ```

---

## 🧠 Funcionamiento Inteligente del Compilador

El selector realiza un proceso de "montaje y desmontaje" dinámico en la raíz del proyecto para que no tengas que modificar código:

1. **Copia de Insumos:** Copia temporalmente el archivo `<carpeta_estudiante>/contenido.py` a la raíz como `contenido.py`.
2. **Montaje de Imágenes:** Copia la carpeta `<carpeta_estudiante>/imagenes/` a la raíz como `imagenes/` de forma temporal.
3. **Ejecución y Tolerancia a Fallos:** Lanza `generador_informe.py` utilizando de manera prioritaria el entorno virtual (`venv`) del proyecto para evitar errores de dependencias (`python-docx`). El motor del informe cuenta con fallback seguro (usa `getattr`), lo que significa que si el `contenido.py` de un estudiante no está completo, el informe se compilará con campos vacíos sin colapsar.
4. **Organización de Salidas:** Mueve los reportes resultantes a la carpeta `reportes/` del estudiante respectivo.
5. **Ejecución de Cronogramas:** Cambia el directorio de trabajo (`CWD`) a la carpeta del estudiante, ejecuta su script local `cronograma.py` (si existe), recopila recursivamente todos los documentos PDF y Word generados y los organiza limpiamente dentro de su subcarpeta `cronogramas/`.
6. **Limpieza Absoluta:** Limpia y elimina todos los archivos temporales y directorios de bloqueo de la raíz y subcarpetas (como `cronogramas generados/`), garantizando que tu repositorio se mantenga ordenado y libre de archivos huérfanos.

---

## 🎨 Insumos y Gráficos por Estudiante
Para garantizar que las imágenes del informe pertenezcan al estudiante que estás compilando, coloca los archivos gráficos en su respectiva carpeta `imagenes/` utilizando los siguientes nombres estándar:
* **`1.png`:** Representación cartográfica / ubicación espacial de la empresa.
* **`2.png`:** Organigrama estructural y niveles jerárquicos de la empresa.

---

## 🛠️ Requisitos Técnicos
* **Python 3.10+**
* Dependencias instaladas en el entorno virtual (`python-docx` para manipulación de XML de Word).
* **LibreOffice** instalado en el sistema (el script lo llama con `--headless` para renderizar y exportar los archivos PDF con la tipografía e índices alineados de forma nativa).
