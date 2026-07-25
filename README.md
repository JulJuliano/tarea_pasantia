# Sistema Multi-Compilador de Informes de Pasantías (IUTECP)

Este proyecto implementa una solución automatizada para la generación de informes y cronogramas de pasantía conformes a la **Normativa de Transcripción de Trabajos e Informes Escritos del IUTECP**. Permite compilar y organizar de manera inteligente los documentos de múltiples estudiantes (**Juliano, Keidy y Amaal**) de forma individual y modular.

> **🤖 Instrucción para asistentes IA:** Antes de modificar `generador_informe.py` o cualquier `contenido.py`, lee obligatoriamente los archivos de normativa en `compartido/normativa/`:
> - `Reglas_1.md` — reglas generales de presentación y transcripción.
> - `Reglas_2_resumido.md` — resumen de reglas de formato, márgenes, sangrías y citas.
> - `Reglas_3.md` — reglas de referencias, anexos y tabla de contenido.
>
> Estos documentos definen las restricciones de formato (fuente, márgenes, interlineado, sangrías, citas, índices) que el generador implementa. Cualquier cambio al generador o a los contenidos debe respetar lo allí establecido.

---

## 📁 Estructura del Proyecto

El repositorio está organizado con una arquitectura modular y **simétrica**: cada estudiante posee exactamente la misma estructura interna de archivos y carpetas, de forma aislada y consistente.

```text
tarea_pasantia/
│
├── generador_informe.py     # Script principal (motor de generación de plantillas DOCX y conversión PDF)
├── selector.py              # Panel de control interactivo y automatizado por CLI
├── revisiones_tutor.md      # Registro de observaciones y retroalimentación del tutor académico
├── .gitignore               # Exclusiones de Git (entornos virtuales, temporales y bloqueos de oficina)
│
├── compartido/              # Recursos transversales a todos los estudiantes
│   ├── iutecp.png           # Logo del IUTECP (portada)
│   └── normativa/           # Normativa oficial de transcripción del IUTECP
│       ├── Reglas_1.md
│       ├── reglas_1.docx
│       ├── Reglas_2.md
│       ├── Reglas_2_resumido.md
│       └── Reglas_3.md
│
├── juliano/                 # Proyecto de Juliano (TSU en Informática)
│   ├── contenido.py         # Textos, tablas, objetivos y variables de Juliano
│   ├── contexto.md          # Diagnóstico situacional, flujo de correspondencias y metas
│   ├── cronograma.py        # Generador de cronogramas semanales de Juliano
│   ├── reportes/            # Salida del Informe de Pasantías (DOCX + PDF)
│   ├── cronogramas/         # Salida de Cronogramas Semanales (Cronograma_Informatica_SemanaN_IUTECP.*)
│   ├── imagenes/            # Insumos gráficos (1.png = Organigrama general, 2.png = Organigrama del depa)
│   └── varios/              # Documentos de referencia del pasante (JulianoCardona.docx)
│
├── keidy/                   # Proyecto de Keidy (TSU en Administración)
│   ├── contenido.py         # Textos, tablas y variables de Keidy
│   ├── contexto.md          # Diagnóstico situacional de Keidy
│   ├── cronograma.py        # Generador de cronogramas semanales de Keidy
│   ├── reportes/            # Salida del Informe de Pasantías (DOCX + PDF)
│   ├── cronogramas/         # Salida de Cronogramas Semanales (Cronograma_Procura_SemanaN_IUTECP.*)
│   ├── imagenes/            # Insumos gráficos (1.png = Mapa, 2.png = Organigrama)
│   └── varios/              # Documentos de referencia del pasante
│
└── amaal/                   # Proyecto de Amaal (TSU en Administración)
    ├── contenido.py         # Capítulos I y II completados con datos reales de IDETEL
    ├── contexto.md          # Diagnóstico situacional de Amaal
    ├── cronograma.py        # Generador de cronogramas semanales de Amaal
    ├── reportes/            # Salida del Informe de Pasantías (vacío, en desarrollo)
    ├── cronogramas/         # Salida de Cronogramas Semanales (Cronograma_Administracion_SemanaN_IUTECP.*)
    ├── imagenes/            # Insumos gráficos (1.png = Ubicación, 2.png = Organigrama general, 3.png = Organigrama del depa)
    └── varios/              # Documentos de referencia del pasante
```

### Convenciones internas (idénticas en cada carpeta de estudiante)

Cada subcarpeta de estudiante contiene **exactamente** los mismos 7 elementos, garantizando consistencia:

| Elemento         | Descripción                                                                       |
| ---------------- | --------------------------------------------------------------------------------- |
| `contenido.py`   | Variables académicas del informe (portada, capítulos I-V, referencias, anexos).  |
| `contexto.md`    | Diagnóstico situacional, flujo del proceso, enfoque metodológico y datos académicos. |
| `cronograma.py`  | Generador local de cronogramas semanales (DOCX + PDF).                            |
| `reportes/`      | Salida del Informe de Pasantías compilado por `generador_informe.py`.              |
| `cronogramas/`   | Salida de los cronogramas semanales compilados por `cronograma.py`.               |
| `imagenes/`      | Insumos gráficos numerados (`1.png`, `2.png`, ...) definidos en `GRAFICOS`.    |
| `varios/`        | Documentos de referencia del pasante (puede estar vacío).                         |

### Patrón de nombres de cronogramas

Todos los cronogramas siguen el patrón uniforme:

```
Cronograma_<Area>_Semana<N>_IUTECP.{docx,pdf}
```

| Estudiante | `<Area>`         |
| ---------- | ---------------- |
| Juliano    | `Informatica`    |
| Keidy      | `Procura`        |
| Amaal      | `Administracion`|

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
* **Argumento `--acciones`:** Permite especificar qué tareas realizar separadas por comas (`informe`, `borrador`, `borrador2`, `cronogramas`, `all`).

**Ejemplos prácticos:**
* Compilar solo el informe de Keidy:
  ```bash
  ./selector.py --estudiantes keidy --acciones informe
  ```
* Compilar todo (informe y cronogramas) para Juliano y Amaal:
  ```bash
  ./selector.py --estudiantes juliano,amaal --acciones all
  ```
* Compilar borrador2 (todo excepto Cap IV + V) para todos:
  ```bash
  ./selector.py --acciones borrador2
  ```

### Modos de generación de informe

| Modo | Acción | Capítulos incluidos | Suffix archivo |
|---|---|---|---|
| **completo** | `informe` | I, II, III, IV, V | — |
| **borrador 1** | `borrador1` | Solo Cap I | `_BORRADOR1` |
| **borrador 2** | `borrador2` | Cap I + II | `_BORRADOR2` |
| **borrador 3** | `borrador3` | Cap I + II + III | `_BORRADOR3` |
| **borrador 4** | `borrador4` | Cap I + II + III + IV | `_BORRADOR4` |

Todos los modos incluyen portada, contraportada, páginas preliminares, referencias y anexos. El índice solo muestra los capítulos presentes en cada modo.

### Portada y Contraportada

- **Portada**: Membrete centrado → Logo IUTECP (`compartido/iutecp.png`) en el primer cuarto del gap → Título del proyecto → Datos del autor (nombre + CI, alineado derecha) → Ciudad y fecha
- **Contraportada**: Membrete → Título → Tabla invisible de 2 columnas (tutores a la izquierda, autor a la derecha, TOP alignment) → Ciudad y fecha pegada al margen inferior
- Los gaps entre bloques se calculan en puntos (no porcentajes), distribuidos equitativamente: `gap_mt = 1.2×` (membrete–título), `gap_td = 1×` (título–datos), `gap_df = 0.5×` (datos–fecha). Todos los márgenes de sección son 3cm; el efecto de 5cm en primera página de capítulo se logra con `space_before`.

### Páginas de Aprobación

Dos páginas con membrete, título "APROBACIÓN DEL TUTOR INDUSTRIAL" / "APROBACIÓN DEL TUTOR ACADÉMICO", párrafo justificado con datos del pasante, fecha, línea de firma y nombre + C.I. del tutor extraídos automáticamente de `AUTOR_DATOS`.

### Orden de páginas preliminares

1. Aprobación del Tutor Industrial
2. Aprobación del Tutor Académico
3. Agradecimientos
4. Dedicatoria
5. Índice de Contenido (sin numeración de página visible, aunque ocupe 2+ páginas)
6. Lista de Cuadros
7. Lista de Figuras
8. Lista de Gráficos
9. Lista de Anexos
10. Resumen (con palabras clave)
11. Introducción

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

Los gráficos del informe se configuran **data-driven** desde cada `contenido.py` mediante una lista `GRAFICOS`. Cada entrada define el número de imagen, la sección tras la cual se inserta (`tras`), el título y el ancho:

```python
GRAFICOS = [
    {"numero": 1, "tras": "ubicacion",  "titulo": "Gráfico 1. Mapa de ubicación...",  "ancho_cm": 5},
    {"numero": 2, "tras": "estructura", "titulo": "Gráfico 2. Organigrama general...", "ancho_cm": 12},
    {"numero": 3, "tras": "estructura", "titulo": "Gráfico 3. Organigrama del depa...", "ancho_cm": 12},
]
```

**Anclas válidas para `tras`:**
| Ancla         | Se inserta después de                          |
| ------------- | ---------------------------------------------- |
| `"ubicacion"` | Sección 1.1.7 Ubicación geográfica             |
| `"estructura"`| Sección 1.1.9 Estructura Organizativa          |

Los archivos gráficos se colocan en `<estudiante>/imagenes/` con nombres numéricos (`1.png`, `2.png`, `3.png`, ...). El selector los copia temporalmente a la raíz antes de compilar.

---

## 📚 Formatos de Contenido Soportados (refactor del generador)

El generador (`generador_informe.py`) soporta dos formatos alternativos para ciertos bloques de contenido, detectándolos dinámicamente:

### Capítulo I — Realidad Organizacional

Los subtítulos del Capítulo I (Identificación de la empresa, Razón social, Reseña histórica, Misión, Visión, Valores, Objetivos Organizacionales, Ubicación, Población, Estructura Organizativa) se renderizan con `agregar_titulo_nivel2`: **sin numeración**, alineados a la izquierda, negrita. El contenido de Misión y Visión va en redonda (sin cursiva).

"Identificación de la empresa" se muestra centrado y sin texto de entrada asociado.

**Objetivos Organizacionales** incluye:
- "Objetivo General" (de la empresa) → texto desde `OBJETIVO_GENERAL_EMPRESA`
- "Objetivos Específicos" (de la empresa) → lista numerada desde `OBJETIVOS_ESPECIFICOS_EMPRESA`

*(Estos son distintos del Objetivo General y Objetivos Específicos del proyecto, que aparecen en Capítulo II).*

### Marco Teórico (Cap. III)

Se reconoce automáticamente si el estudiante usa el formato enriquecido o el formato plano:

- **Enriquecido (`BASES_TEORICAS`)**: lista de dicts, cada uno con `titulo`, `parrafos` (lista de strings) y `cita_larga` opcional (dict con `texto` y `autor`). El generador renderiza cada subsección con un encabezado Nivel 2, sus párrafos normados y, si existe la cita larga, la inserta con post-cita sangrada.
- **Plano (`BASES_TEORICAS_PARRAFOS`)**: lista simple de strings. Se renderiza bajo un único encabezado "Bases Teóricas Referenciales", con una cita larga global opcional (`CITA_LARGA_TEXTO` + `CITA_LARGA_AUTOR`).

### Actividades Realizadas (Cap. IV)

`ACTIVIDADES_LISTA` admite dos formatos:

- **Strings**: cada elemento es un texto enumerado (formato Amaal/Keidy).
- **Dicts por semana**: cada elemento es un dict con `semana` (int), `operativa` e `investigacion` (strings). El generador produce un subtítulo "Semana N" por cada entrada y dos ítems numerados con etiquetas en negrita "Actividad operativa" e "Actividad de investigación".

---

## 🛠️ Requisitos Técnicos
* **Python 3.10+**
* Dependencias instaladas en el entorno virtual (`python-docx` para manipulación de XML de Word).
* **LibreOffice** instalado en el sistema (el script lo llama con `--headless` para renderizar y exportar los archivos PDF con la tipografía e índices alineados de forma nativa).
