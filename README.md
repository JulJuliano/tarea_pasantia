# Sistema Multi-Compilador de Informes de Pasantías (IUTECP)

Este repositorio implementa una solución automatizada para generar, organizar y revisar los **informes de pasantías** y **cronogramas semanales** de tres estudiantes del IUTECP: **Juliano, Keidy y Amaal**.

Los tres cursan la misma asignatura de **Pasantías Profesionales**, comparten la normativa institucional y el entorno académico/Moodle, pero sus empresas, proyectos, tutores y actividades son diferentes. Por ello, el sistema mantiene un generador común y contenidos separados por estudiante.

> [!IMPORTANT]
> **Instrucción para asistentes IA y para futuras modificaciones**
>
> Antes de modificar `generador_informe.py`, `selector.py`, cualquier `contenido.py` o cualquier `cronograma.py`:
>
> 1. leer `CONTEXTO_GENERAL.md`;
> 2. leer `revisiones_tutor.md`;
> 3. consultar la normativa vigente dentro de `compartido/normativa/`;
> 4. contrastar cualquier cambio de actividades con el `cronograma.py` del estudiante;
> 5. mantener la cadena de coherencia:
>
> **problema → interrogante → objetivo general → objetivos específicos → planificación integral → Gantt → cronogramas semanales → Capítulo IV → conclusiones → recomendaciones → anexos**.
>
> No se deben recuperar automáticamente versiones antiguas de contenidos, objetivos o enfoques metodológicos que ya hayan sido corregidos.

---

## 1. Fuentes normativas del proyecto

La normativa común está centralizada en:

```text
compartido/normativa/
├── 00_LEEME_GUIA_PASANTIAS_REGULARES_IUTECP.md
├── 01_FORMATO_TRANSCRIPCION_Y_REDACCION_IUTECP.md
├── 02_ESTRUCTURA_Y_CONTENIDO_DEL_INFORME_IUTECP.md
├── 03_PROCESO_EVALUACION_Y_PRESENTACION_ORAL_IUTECP.md
└── opcional/
```

Uso recomendado:

| Archivo | Función |
|---|---|
| `00_LEEME...` | Explica cómo usar el conjunto normativo y qué corresponde a las pasantías regulares. |
| `01_FORMATO...` | Fuente, márgenes, interlineado, sangrías, citas, cuadros, gráficos, paginación y referencias. |
| `02_ESTRUCTURA...` | Qué debe contener el informe: preliminares, capítulos I–V, planificación, Gantt y anexos. |
| `03_PROCESO...` | Proceso de pasantías, responsabilidades, evaluación y presentación oral. |
| `opcional/` | Material institucional complementario que no constituye por sí solo la guía principal. |

Los tres casos corresponden a **pasantías profesionales regulares**. Las disposiciones exclusivas de acreditación por experiencia laboral no deben aplicarse a estos informes.

---

## 2. Contexto y revisiones

### `CONTEXTO_GENERAL.md`

Es la **fuente maestra de contexto** del proyecto y sustituye los antiguos `contexto.md` separados.

Incluye:

- contexto académico común;
- datos de Juliano, Keidy y Amaal;
- empresas y áreas de pasantía;
- títulos y objetivos actuales;
- problemas identificados;
- técnicas e instrumentos;
- imágenes esperadas;
- decisiones ya tomadas;
- restricciones que no deben aparecer en algunos informes;
- estado actual y pendientes.

### `revisiones_tutor.md`

Es un registro acumulativo de observaciones. **No se eliminan las correcciones antiguas** aunque ya hayan sido atendidas, porque sirven como referencia futura.

Convención:

- `[x]` corregido;
- `[~]` corregido, pero requiere comprobación visual/final;
- `[ ]` pendiente;
- `[i]` nota o instrucción de referencia.

### `ANEXOS_PROPUESTOS.md`

Contiene el banco de anexos y diagramas que pueden producirse mediante Mermaid, PlantUML, GraphViz, DBML, Kroki u otras herramientas.

---

## 3. Estructura actual del repositorio

```text
tarea_pasantia/
│
├── amaal/
│   ├── contenido.py
│   ├── cronograma.py
│   ├── cronogramas/
│   │   └── combinados/
│   ├── imagenes/
│   ├── reportes/
│   └── varios/
│       └── mermaids.txt
│
├── ANEXOS_PROPUESTOS.md
│
├── compartido/
│   └── normativa/
│       ├── 00_LEEME_GUIA_PASANTIAS_REGULARES_IUTECP.md
│       ├── 01_FORMATO_TRANSCRIPCION_Y_REDACCION_IUTECP.md
│       ├── 02_ESTRUCTURA_Y_CONTENIDO_DEL_INFORME_IUTECP.md
│       ├── 03_PROCESO_EVALUACION_Y_PRESENTACION_ORAL_IUTECP.md
│       └── opcional/
│
├── CONTEXTO_GENERAL.md
├── generador_informe.py
├── .gitignore
│
├── juliano/
│   ├── contenido.py
│   ├── cronograma.py
│   ├── cronogramas/
│   ├── imagenes/
│   ├── reportes/
│   └── varios/
│       └── mermaids.txt
│
├── keidy/
│   ├── contenido.py
│   ├── cronograma.py
│   ├── cronogramas/
│   │   └── combinados/
│   ├── imagenes/
│   ├── reportes/
│   └── varios/
│
├── README.md
├── revisiones_tutor.md
└── selector.py
```

### Elementos principales

| Elemento | Descripción |
|---|---|
| `generador_informe.py` | Motor común que genera los informes DOCX/PDF según la normativa IUTECP. |
| `selector.py` | Orquestador para seleccionar estudiantes y acciones de compilación. |
| `CONTEXTO_GENERAL.md` | Contexto académico y particular de los tres estudiantes. |
| `revisiones_tutor.md` | Historial acumulativo de observaciones y correcciones. |
| `ANEXOS_PROPUESTOS.md` | Banco de anexos técnicos y académicos. |
| `<estudiante>/contenido.py` | Datos académicos y contenido de los capítulos I–V. |
| `<estudiante>/cronograma.py` | Generador de planes/cronogramas semanales del estudiante. |
| `<estudiante>/imagenes/` | Logos, mapas, organigramas, diagramas y anexos gráficos. |
| `<estudiante>/reportes/` | Informes generados. |
| `<estudiante>/cronogramas/` | Cronogramas generados. |
| `<estudiante>/cronogramas/combinados/` | Versiones combinadas, cuando se utilicen. |
| `<estudiante>/varios/` | Material de apoyo y referencias específicas del estudiante. |

---

## 4. Estudiantes

| Estudiante | Carrera | Empresa / área principal | Tutor académico |
|---|---|---|---|
| **Juliano** | TSU en Informática | Venangocupet, S.A. — Presidencia | Ing. José Mejías |
| **Keidy** | TSU en Administración | Lubricantes y Equipos Varyna, C.A. — Administración/Procura | Dra. Carmen J. Álvarez |
| **Amaal** | TSU en Administración | Ingeniería de Telecomunicaciones, C.A. — Atención al Cliente/Administración | Dra. Carmen J. Álvarez |

Keidy y Amaal comparten tutora académica. Juliano tiene un tutor académico diferente.

Una observación particular de un tutor **no debe copiarse automáticamente** al otro proyecto, salvo que también esté respaldada por la normativa institucional o por una instrucción común de la asignatura.

---

## 5. Panel de control (`selector.py`)

`selector.py` funciona como orquestador principal del proyecto.

### Modo interactivo

```bash
python selector.py
```

o:

```bash
./selector.py
```

Controles habituales:

- `↑` / `↓`: navegar;
- `Espacio`: marcar/desmarcar;
- `Enter`: ejecutar;
- `Q` o `Ctrl+C`: salir/cancelar.

### Modo CLI

```bash
./selector.py --estudiantes <estudiante_id> --acciones <accion_id>
```

Ejemplos:

```bash
./selector.py --estudiantes keidy --acciones informe
```

```bash
./selector.py --estudiantes juliano,amaal --acciones all
```

```bash
./selector.py --acciones borrador2
```

```bash
./selector.py --estudiantes juliano --acciones combinar_documentos
```

La acción `combinar_documentos` une el informe completo con los cronogramas semanales disponibles: nueve para Juliano y diez para Keidy y Amaal.

### Modos de informe

| Modo | Acción | Capítulos incluidos | Sufijo |
|---|---|---|---|
| completo | `informe` | I, II, III, IV, V | — |
| borrador 1 | `borrador1` | I | `_BORRADOR1` |
| borrador 2 | `borrador2` | I + II | `_BORRADOR2` |
| borrador 3 | `borrador3` | I + II + III | `_BORRADOR3` |
| borrador 4 | `borrador4` | I + II + III + IV | `_BORRADOR4` |

Los borradores conservan las páginas preliminares necesarias y generan un índice acorde con los capítulos incluidos.

---

## 6. Funcionamiento del compilador

El flujo general del selector es:

1. toma el `contenido.py` del estudiante seleccionado;
2. monta temporalmente sus imágenes;
3. ejecuta `generador_informe.py`;
4. genera DOCX y, cuando LibreOffice está disponible, PDF;
5. mueve los resultados a `reportes/`;
6. ejecuta `cronograma.py` cuando se solicita;
7. organiza los archivos producidos dentro de `cronogramas/`;
8. limpia archivos temporales.

El contenido de un estudiante debe permanecer aislado del de los otros.

---

## 7. Formato general implementado

El generador se ha ajustado para reflejar, entre otras, estas reglas:

- papel carta;
- margen izquierdo de 4 cm;
- márgenes superior, derecho e inferior de 3 cm;
- Times New Roman de 12 pt para texto general;
- 10 pt en cuadros/gráficos cuando corresponde;
- interlineado 1,5 en el cuerpo;
- capítulos en página nueva;
- subtítulos alineados a la izquierda y sin numeración;
- preliminares con números romanos minúsculos;
- numeración arábiga desde la Introducción;
- primera página de Introducción, capítulos y referencias contada pero sin número visible;
- contraportada con la frase:
  **“Informe de pasantías para obtener el título de Técnico Superior Universitario en la especialidad de: …”**;
- referencias con orden alfabético y sangría francesa;
- anexos ajustados al área útil de la página.

> El cumplimiento final siempre debe verificarse sobre el **PDF renderizado**, porque algunos saltos de página, tamaños de imágenes y longitud de párrafos dependen del contenido real.

---

## 8. Portada y contraportada

### Portada

Incluye:

- membrete institucional;
- logo IUTECP;
- título del informe;
- datos del autor;
- ciudad y fecha.

### Contraportada

Incluye:

- membrete;
- título;
- texto institucional:
  **“Informe de pasantías para obtener el título de Técnico Superior Universitario en la especialidad de: …”**;
- Tutor Industrial;
- Autor;
- Tutor Académico;
- ciudad, mes y año.

Debe mantenerse dentro de **una sola página**.

---

## 9. Páginas preliminares

Orden general utilizado:

1. Aprobación del Tutor Industrial.
2. Aprobación del Tutor Académico.
3. Agradecimiento, si aplica.
4. Dedicatoria, si aplica.
5. Índice de contenido.
6. Lista de cuadros, si aplica.
7. Lista de figuras, **solo si existen figuras**.
8. Lista de gráficos, si aplica.
9. Lista de anexos.
10. Resumen.
11. Introducción.

### Figuras y gráficos

La normativa contempla ambas listas, pero son condicionales.

Actualmente los tres informes trabajan sus elementos visuales principalmente como **gráficos**. Por eso el generador no debe crear una página vacía de `LISTA DE FIGURAS` cuando no exista ninguna figura declarada.

---

## 10. Capítulo I y recursos gráficos

`contenido.py` define los elementos académicos del Capítulo I:

- identificación de la empresa;
- razón social;
- reseña histórica;
- misión;
- visión;
- valores;
- objetivos organizacionales;
- objetivo general de la empresa;
- objetivos específicos de la empresa;
- logotipo;
- ubicación geográfica;
- población;
- estructura organizacional;
- descripción del departamento donde se realizó la pasantía.

Los objetivos organizacionales de la empresa son **diferentes** de los objetivos del proyecto, que pertenecen al Capítulo II.

### Logos

Los logos empresariales se ubican antes de la sección de ubicación geográfica siguiendo el modelo utilizado por el profesor:

```text
[LOGO]

Gráfico N. Logotipo de la empresa.
Fuente: Empresa X (2026).

Ubicación geográfica
...
```

No se agrega actualmente un párrafo de interpretación/descripción del logo.

### Gráficos

Los gráficos se configuran desde `contenido.py`, por ejemplo:

```python
GRAFICOS = [
    {
        "numero": 2,
        "tras": "ubicacion",
        "titulo": "Gráfico 2. Referencia cartográfica...",
        "ancho_cm": 10,
        "lista": "Referencia cartográfica...",
    },
]
```

Las imágenes deben existir dentro de `<estudiante>/imagenes/`.

---

## 11. Imágenes actuales por estudiante

### Juliano

```text
juliano/imagenes/
├── logo.png
├── mapa.png
├── 1.png
├── 2.png
└── 3.png
```

Referencia actual:

- `logo.png`: logotipo de Venangocupet;
- `mapa.png`: mapa/referencia de las oficinas administrativas;
- `1.png`: organigrama general;
- `2.png`: organigrama del Departamento de Presidencia;
- `3.png`: árbol del problema — Anexo A.

### Keidy

```text
keidy/imagenes/
├── logo.jpg
├── 1.png
└── 2.png
```

Además puede incorporarse una imagen adicional del **diagrama de Ishikawa** cuando se genere.

### Amaal

```text
amaal/imagenes/
├── logo.jpg
├── 1.png
├── 2.png
├── 3.png
└── 4.png
```

Referencia actual:

- `logo.jpg`: logotipo;
- `1.png`: ubicación;
- `2.png`: organigrama general;
- `3.png`: organigrama del departamento;
- `4.png`: flujograma utilizado como anexo.

Las imágenes de anexos se escalan proporcionalmente para respetar el tamaño carta, los márgenes y el espacio destinado al título.

---

## 12. Capítulo II y coherencia metodológica

El diagnóstico debe estar conectado con el resto del informe.

Elementos esperados:

- situación problemática;
- desarrollo desde contexto amplio hasta realidad específica;
- técnica utilizada para representar/analizar el problema;
- interrogante;
- objetivo general;
- objetivos específicos;
- planificación integral;
- cronograma/Gantt.

Actualmente se trabaja con la lógica **macro → meso → micro**. Las instrucciones particulares sobre la presentación de esos rótulos deben revisarse en `revisiones_tutor.md`, porque han existido observaciones de tutor que requieren conservarse como referencia.

---

## 13. Capítulo III — Marco Teórico

El generador admite contenido estructurado mediante `BASES_TEORICAS`.

Una entrada típica puede contener:

```python
{
    "titulo": "Control Administrativo",
    "parrafos": [
        "...",
        "..."
    ],
    "cita_larga": {
        "texto": "...",
        "autor": "(Autor, año, p. X)"
    }
}
```

También puede incorporarse, cuando corresponde, una posición o análisis del autor.

Las bases teóricas deben guardar relación real con:

- el problema;
- los objetivos;
- el área de pasantía;
- la solución/propuesta.

No deben agregarse conceptos únicamente para aumentar extensión.

---

## 14. Capítulo IV — Actividades realizadas

`ACTIVIDADES_LISTA` puede organizarse por semana:

```python
{
    "semana": 1,
    "operativa": "...",
    "investigacion": "..."
}
```

La palabra `investigacion` es una **clave interna del código**; su redacción visible debe ajustarse al enfoque académico que corresponda a cada estudiante y a las observaciones de su tutor.

El contenido del Capítulo IV debe coincidir con los planes semanales reales.

No deben presentarse como realizadas actividades futuras o actividades que no aparezcan en el cronograma real.

---

## 15. Conclusiones y recomendaciones

Las conclusiones deben responder a los objetivos específicos.

Regla práctica:

```text
Objetivo específico 1 → Conclusión 1
Objetivo específico 2 → Conclusión 2
...
```

Las recomendaciones deben derivarse de los resultados y conclusiones, y pueden dirigirse a:

- la empresa;
- el IUTECP;
- futuros pasantes;
- responsables del proceso evaluado.

---

## 16. Anexos

Los anexos deben:

- estar mencionados previamente en el cuerpo del informe;
- tener relación directa con actividades, diagnóstico o propuesta;
- evitar contenido decorativo o redundante;
- mantener legibilidad dentro del área útil de la página.

`ANEXOS_PROPUESTOS.md` contiene opciones como:

- árboles del problema;
- Ishikawa;
- flujogramas AS-IS / TO-BE;
- diagramas de estados;
- swimlanes;
- diagramas entidad-relación;
- arquitecturas de software;
- secuencias;
- matrices RACI;
- SIPOC;
- matrices de pruebas;
- formatos propuestos.

Muchos pueden generarse mediante **Kroki** usando Mermaid, GraphViz, PlantUML, DBML, C4, D2 u otros lenguajes.

---

## 17. Cronogramas

Patrón histórico de nombres:

```text
Cronograma_<Area>_Semana<N>_IUTECP.{docx,pdf}
```

Áreas:

| Estudiante | Área |
|---|---|
| Juliano | `Informatica` |
| Keidy | `Procura` |
| Amaal | `Administracion` |

Al modificar un cronograma semanal se debe revisar inmediatamente:

- Gantt del informe;
- Capítulo IV;
- resumen, si menciona actividades;
- conclusiones, si cambian los productos/resultados;
- anexos relacionados.

---

## 18. Estado particular importante

### Juliano

- duración documentada: **9 semanas**;
- no agregar una décima semana automáticamente;
- el `cronograma.py` de Juliano es mantenido/corregido directamente por Juliano cuando así se indique;
- después de cambios de semanas 8 y 9 debe revisarse la coherencia con el informe.

### Keidy

- la tutora exige actualmente **tres objetivos específicos**;
- las observaciones del cronograma fueron restauradas como texto de apoyo;
- verificar las observaciones directas realizadas por la tutora dentro de versiones comentadas del documento.

### Amaal

- el contexto real distingue:
  - semanas 1–3: Atención al Cliente;
  - semanas 4–10: Administración;
- cronograma y Capítulo IV deben conservar esa transición.

Para detalles completos consultar `CONTEXTO_GENERAL.md`.

---

## 19. Requisitos técnicos

- Python 3.10+.
- `python-docx`.
- LibreOffice para conversión headless a PDF.
- Sistema capaz de ejecutar los scripts desde la raíz del repositorio.

Ejemplo de dependencia:

```bash
pip install python-docx
```

---

## 20. Flujo recomendado de trabajo

Antes de efectuar cambios:

```text
1. CONTEXTO_GENERAL.md
        ↓
2. revisiones_tutor.md
        ↓
3. normativa aplicable
        ↓
4. contenido.py
        ↓
5. cronograma.py (si el cambio afecta actividades)
        ↓
6. generador_informe.py (solo si el cambio es estructural/formato)
        ↓
7. generar DOCX/PDF
        ↓
8. inspección visual final
```

### Lista de control antes de una entrega

- [ ] Portada en una página.
- [ ] Contraportada en una página y con la frase institucional.
- [ ] Preliminares completos.
- [ ] Lista de figuras omitida si no aplica.
- [ ] Índices actualizados.
- [ ] Logo, mapa y organigramas legibles.
- [ ] Problema coherente con objetivos.
- [ ] Técnica del problema incluida y anexada.
- [ ] Planificación y Gantt coherentes.
- [ ] Cronograma semanal coherente con Capítulo IV.
- [ ] Bases teóricas y legales sustentadas cuando correspondan.
- [ ] Conclusiones vinculadas uno a uno con objetivos.
- [ ] Recomendaciones derivadas de conclusiones.
- [ ] Referencias citadas correctamente.
- [ ] Anexos mencionados dentro del cuerpo.
- [ ] PDF revisado visualmente.

---

## 21. Principio de mantenimiento

Este repositorio no debe tratarse solamente como un generador de Word.

La prioridad es conservar **coherencia académica y trazabilidad de las decisiones**. Por ello:

- `CONTEXTO_GENERAL.md` documenta el estado real;
- `revisiones_tutor.md` conserva el historial de cambios;
- la normativa define las reglas;
- `contenido.py` representa el informe;
- `cronograma.py` representa lo planificado/realizado;
- `generador_informe.py` se limita a convertir esas decisiones académicas en un documento con el formato institucional.
