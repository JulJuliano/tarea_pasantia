# Guía de anexos generables por código y sistema visual

## 1. Criterio general de trabajo

Esta guía parte de dos insumos:

- `ANEXOS_PROPUESTOS.md`, que ya contiene una propuesta amplia de anexos posibles para Juliano, Keidy y Amaal.
- `CONTEXTO_GENERAL.md`, que fija reglas de coherencia, prioridades y particularidades de cada informe.

La idea es **no hacer anexos en Word o PowerPoint**, sino producirlos con herramientas reproducibles: Mermaid, PlantUML, GraphViz, BPMN, DBML, D2, C4-PlantUML, Structurizr, Vega/Vega-Lite y otros lenguajes compatibles con Kroki, además de Python y HTML/CSS.

## 2. Regla metodológica obligatoria

Todo anexo debe cumplir estas cuatro condiciones:

1. Debe corresponder a una actividad, instrumento, resultado o propuesta **realmente realizada**.
2. Debe ser mencionado antes en el cuerpo del informe.
3. Debe mantener coherencia con la cadena:

   **situación problemática → interrogante → objetivo general → objetivos específicos → planificación integral → Gantt → Capítulo IV → conclusiones → recomendaciones → anexos**
4. No debe agregarse solo porque “se puede dibujar”.

## 3. Revisión rápida del generador actualizado

El `generador_informe(1).py` ya mejoró varios puntos importantes frente a la versión anterior:

- la paginación está mucho mejor planteada, con romanos en preliminares y arábigos desde Introducción;
- el Resumen ya se inserta con formato específico de interlineado sencillo;
- el índice general ya respeta mejor el orden físico del documento;
- se añadió el apartado **“Descripción del departamento donde realizó la pasantía”** después del organigrama;
- la visibilidad de **macro / meso / micro** ya depende de `MOSTRAR_NIVELES_DIAGNOSTICO`.

### Pendientes todavía recomendables

1. Implementar en el generador la lectura de:
   - `CUADRO_PLANIFICACION_FUENTE`
   - `CUADRO_CRONOGRAMA_FUENTE`

   para que aparezca automáticamente la fuente debajo de esos cuadros.

2. Si más adelante quieres separar visualmente las **bases legales** dentro del Capítulo III, conviene introducir una marca o subtítulo específico, porque ahora el generador sigue imprimiendo todo en la misma secuencia de subtítulos.

3. Conviene dejar el generador listo para **insertar anexos SVG o PNG** de forma consistente, manteniendo ancho máximo y espacio para título/fuente.

## 4. Estrategia general para no parecer “plagio”

La clave no es exagerar el diseño, sino dar a cada informe una identidad visual distinta, manteniendo seriedad académica.

### 4.1 Reglas comunes

- Sin emojis.
- Fondo blanco.
- Títulos en negrita.
- Texto oscuro casi negro.
- Diagramas con 2–4 colores como máximo.
- Cajas con bordes limpios y sin sombras recargadas.
- Flechas claras y consistentes.
- Tipografía sans-serif para anexos y diagramas; la familia concreta se define por estudiante y no se intercambia.
- En tablas: zebra suave o encabezado sólido + filas blancas.
- Exportar preferiblemente a **SVG** y, si hace falta para Word/PDF, convertir a PNG de buena resolución.

### 4.2 Convenciones compartidas

- **Títulos de anexos**: siempre en estilo institucional del informe.
- **Fuente del anexo**: usar una de estas fórmulas según el caso:
  - `Fuente: Elaboración propia (2026).`
  - `Fuente: La autora (2026).`
  - `Fuente: El autor (2026).`
  - `Fuente: Información suministrada por la empresa y elaboración propia (2026).`
- **Nombres de archivo**: `anexo_tema_version.svg` o `anexo_tema_version.png`
- **Tamaño sugerido**:
  - Diagramas verticales: ancho útil 11–13 cm
  - Diagramas horizontales: ancho útil 14–16 cm
  - Tablas: intentar 1 sola página, y si no, dividirlas por lógica, no reducirlas agresivamente.

## 5. Sistema visual por estudiante

---

## 5.1 Juliano — Informática / Venangocupet

### Identidad visual

**Identidad:** técnica, sobria y de carácter industrial, orientada a software, control y trazabilidad documental. El color rector es el rojo vino y la tipografía base es Arial; ambos deben mantenerse en sus anexos.

### Paleta

- Rojo vino principal: `#8F1D2C`
- Rojo medio: `#C94F5D`
- Rojo claro auxiliar: `#F7DDE1`
- Texto ciruela oscuro: `#24171A`
- Fondo auxiliar: `#FFF7F8`

### Tipografía

- Preferida: `Arial`
- Respaldo: `Liberation Sans, sans-serif`

### Estética

- Rectángulos con esquinas ligeramente redondeadas.
- Bordes finos en rojo vino y conectores gris oscuro.
- Flujos muy ordenados, con poca decoración.
- Si hay tablas técnicas, usar encabezado rojo vino con texto blanco.
- Si hay arquitectura o base de datos, priorizar líneas limpias y jerarquía clara.

### Herramientas recomendadas por tipo

- Árbol del problema: **GraphViz** o **Mermaid**
- AS-IS / TO-BE: **Mermaid** o **PlantUML Activity**
- ERD: **DBML** o **Mermaid ER**
- Arquitectura: **C4-PlantUML**
- Secuencia: **Mermaid Sequence** o **PlantUML Sequence**
- Estados: **Mermaid stateDiagram**
- Matrices / pruebas: **Python + pandas**

### Anexos prioritarios

1. Árbol del problema.
2. Flujograma AS-IS del proceso documental actual.
3. Flujograma TO-BE con el prototipo.
4. ERD de la base de datos.
5. Arquitectura del prototipo.
6. Secuencia de registro y despacho.
7. Diagrama de estados del expediente.
8. Matriz de trazabilidad requerimiento → módulo → prueba.
9. Matriz de casos de prueba y resultados.

---

## 5.2 Keidy — Administración / Procura

### Identidad visual

**Identidad:** administrativo-procedimental, clara y organizada, enfocada en control interno, procura y simplificación. El color rector es el verde esmeralda, con terracota como acento, y la tipografía base es Verdana; esta combinación debe mantenerse en sus anexos.

### Paleta

- Verde esmeralda principal: `#1F6F5B`
- Verde salvia medio: `#68B398`
- Verde claro auxiliar: `#E5F3EC`
- Texto verde oscuro: `#1C2B24`
- Fondo auxiliar: `#F7FCF9`
- Acento terracota: `#B76D4A`

### Tipografía

- Preferida: `Verdana`
- Respaldo: `DejaVu Sans, sans-serif`

### Estética

- Diagramas más funcionales que técnicos.
- Muy buena legibilidad en swimlanes, SIPOC, RACI y matrices.
- Encabezados de tablas en verde esmeralda con texto blanco.
- Cajas con relleno muy claro y bordes discretos.
- Ideal para anexos de flujo y formatos administrativos.

### Herramientas recomendadas por tipo

- Ishikawa: **GraphViz**, **PlantUML** o **Mermaid adaptado**
- AS-IS / TO-BE: **BPMN** o **Mermaid**
- Swimlane: **BPMN** o **PlantUML Activity**
- SIPOC: **Python/pandas** o **GraphViz**
- RACI: **Python/pandas**
- Matriz de autorización: **Python/pandas**
- Formatos (requisición, cotización, OC, seguimiento): **HTML/CSS** o **Python → HTML/PDF/PNG**
- Indicadores: **Python/pandas**

### Anexos prioritarios

1. Ishikawa.
2. Flujograma AS-IS del proceso de procura.
3. Flujograma TO-BE del proceso simplificado.
4. Swimlane del proceso propuesto.
5. SIPOC.
6. Matriz RACI.
7. Matriz de autorización por monto.
8. Formato de requisición.
9. Formato de solicitud de cotización.
10. Formato de orden de compra.
11. Formato de seguimiento de cotizaciones.
12. Ficha de indicadores del proceso.

---

## 5.3 Amaal — Administración / IDETEL

### Identidad visual

**Identidad:** de servicio, cercana pero formal, enfocada en atención al cliente, seguimiento de solicitudes y coordinación entre áreas. El color rector es el morado, con lavanda como apoyo, y la tipografía base es Tahoma; esta combinación debe mantenerse en sus anexos.

### Paleta

- Morado profundo principal: `#5B2A86`
- Morado medio: `#9B6BC4`
- Lavanda clara auxiliar: `#EDE3F7`
- Texto ciruela oscuro: `#24182D`
- Fondo auxiliar: `#FAF8FD`

### Tipografía

- Preferida: `Tahoma`
- Respaldo: `DejaVu Sans, sans-serif`

### Estética

- Flujos con énfasis en continuidad del caso.
- Buen uso de carriles por área.
- Encabezados de tablas en morado profundo con texto blanco.
- Visualmente más orientado al servicio que Keidy, pero igual de formal.
- Excelente para estados de solicitudes, flujo de afiliaciones/incidencias y coordinación interdepartamental.

### Herramientas recomendadas por tipo

- Ishikawa: **GraphViz** o **Mermaid adaptado**
- AS-IS / TO-BE: **BPMN** o **Mermaid**
- Swimlane Cliente → Atención al Cliente → Administración → NOC/Técnicos → cierre: **BPMN** o **PlantUML Activity**
- Diagrama de estados: **Mermaid stateDiagram**
- RACI: **Python/pandas**
- Indicadores: **Python/pandas**
- Formatos unificados: **HTML/CSS**
- Comunicación interdepartamental: **Mermaid** o **PlantUML**

### Anexos prioritarios

1. Ishikawa.
2. Flujograma AS-IS de afiliaciones e incidencias.
3. Flujograma TO-BE del proceso estandarizado.
4. Swimlane interdepartamental.
5. Diagrama de estados de la solicitud.
6. Matriz RACI.
7. Formato unificado de afiliación.
8. Formato unificado de incidencias.
9. Ficha de indicadores.
10. Diagrama de comunicación interdepartamental.

### 5.4 Separación visual obligatoria

Para evitar que los anexos parezcan copiados entre informes, cada estudiante debe conservar su propia combinación de color, tipografía y tratamiento de componentes:

| Estudiante | Identidad cromática | Tipografía base | Tratamiento visual |
|---|---|---|---|
| Juliano | Rojo vino, rojo medio y rojo claro | Arial | Técnico, lineal, compacto y orientado a trazabilidad |
| Keidy | Verde esmeralda, verde salvia y terracota | Verdana | Procedimental, matricial y orientado a control interno; Ishikawa horizontal de espina continua |
| Amaal | Morado profundo, morado medio y lavanda | Tahoma | De servicio, continuo y orientado a coordinación; causa-efecto vertical por agrupaciones |

Los códigos hexadecimales definidos en cada apartado son canónicos: no deben sustituirse por equivalentes visuales ni mezclarse entre estudiantes.

Reglas de aplicación:

- No reutilizar la misma paleta en dos estudiantes.
- Si un archivo fuente existente utiliza otra paleta, debe considerarse pendiente de normalización antes de incorporar su salida; no debe mezclarse con la identidad de este apartado.
- No copiar la misma distribución, jerarquía de cajas o combinación de estilos en diagramas equivalentes.
- En los Ishikawa, Keidy usa una espina horizontal con ramas sobre el flujo de procura y Amaal usa una composición vertical con agrupaciones de causas; no deben volver a la misma plantilla.
- No copiar un archivo fuente completo para cambiar únicamente los textos, los colores o la tipografía.
- En anexos equivalentes, adaptar también la estructura, la secuencia, los roles, las etiquetas y los datos propios del proceso de cada estudiante.
- No trasladar entre informes nombres de empresas, cargos, cifras, procesos, resultados, conclusiones ni textos.
- Cada fuente debe aplicar desde el inicio la identidad de su estudiante: nombre, tipografía y paleta correspondiente.
- Mantener el color principal en títulos de bloques, nodos centrales y encabezados de tablas.
- Usar el color medio para decisiones, estados o funciones destacadas.
- Reservar el color claro para fondos auxiliares y carriles.
- Mantener el texto en tonos oscuros, nunca en colores saturados.
- Antes de exportar, comprobar que el título, el contenido, la fuente, el nombre de archivo, la paleta y la tipografía correspondan al mismo estudiante.
- La diferenciación visual no debe sacrificar legibilidad ni inventar información académica.

## 6. Stack mínimo recomendado para no complicarse

Para reducir trabajo y no dispersarse entre demasiados lenguajes, recomiendo este stack base:

### Juliano
- **Mermaid**: flujos, secuencia, estados.
- **DBML**: modelo de datos.
- **C4-PlantUML**: arquitectura.
- **Python/pandas**: matrices y tablas.

### Keidy
- **Mermaid o BPMN**: flujos.
- **GraphViz**: Ishikawa.
- **Python/pandas**: RACI, autorización, indicadores.
- **HTML/CSS**: formatos administrativos.

### Amaal
- **Mermaid o BPMN**: flujos y swimlanes.
- **GraphViz**: Ishikawa.
- **Mermaid stateDiagram**: estados.
- **Python/pandas**: RACI e indicadores.
- **HTML/CSS**: formatos.

## 7. Plantilla estética resumida por tipo de anexo

### 7.1 Diagramas de flujo / BPMN / Mermaid

- Título fuera del diagrama, en el informe.
- Nodos principales con color sólido suave.
- Todo color de relleno debe pertenecer a la paleta asignada al estudiante; no usar colores por defecto del motor.
- Texto siempre oscuro.
- No usar más de dos colores de relleno por diagrama.
- Flechas negras o gris oscuro.
- En swimlanes, usar carriles muy claros para no saturar.

### 7.2 Tablas / matrices

- Encabezado sólido.
- Fuente 10–11 pt.
- Filas blancas + alternado muy suave si hace falta.
- Evitar bordes excesivamente gruesos.
- Columnas compactas, pero legibles.

### 7.3 Formatos administrativos

- Encabezado con nombre de empresa.
- Tabla base o celdas bien delimitadas.
- Espacios de firma claramente señalados.
- Códigos o versiones solo si existen realmente.
- Si es un formato propuesto, debe indicarse como **propuesto**.

## 8. Orden práctico de producción

### Primera ronda

- Juliano: árbol del problema + AS-IS + ERD.
- Keidy: Ishikawa + AS-IS + TO-BE.
- Amaal: Ishikawa + AS-IS + TO-BE.

### Segunda ronda

- Juliano: arquitectura + secuencia + estados.
- Keidy: swimlane + RACI + autorización.
- Amaal: swimlane + estados + RACI.

### Tercera ronda

- Keidy y Amaal: formatos + indicadores.
- Juliano: matrices de trazabilidad y pruebas.

## 9. Convención para el repositorio

### Carpeta sugerida

- `anexos/juliano/`
- `anexos/keidy/`
- `anexos/amaal/`

### Dentro de cada una

- `src/` → código fuente de diagramas
- `out/` → SVG/PNG finales
- `README.md` → explicación breve de qué es cada anexo

### Ejemplo de nombres

#### Juliano
- `src/anexo_arbol_problema.mmd`
- `src/anexo_erd.dbml`
- `out/anexo_arbol_problema.svg`
- `out/anexo_erd.svg`

#### Keidy
- `src/anexo_ishikawa.dot`
- `src/anexo_procura_asis.mmd`
- `src/anexo_raci.py`
- `out/anexo_ishikawa.svg`

#### Amaal
- `src/anexo_ishikawa.dot`
- `src/anexo_solicitudes_tobe.mmd`
- `src/anexo_estados_solicitud.mmd`
- `out/anexo_estados_solicitud.svg`

## 10. Decisión final recomendada

Si quieres avanzar rápido y sin cansarte con Word/PowerPoint, mi recomendación concreta es esta:

1. **Mantener `ANEXOS_PROPUESTOS.md` como inventario general.**
2. Crear luego un archivo operativo por estudiante con:
   - anexos aprobados;
   - lenguaje elegido;
   - nombre del archivo fuente;
   - nombre del archivo final;
   - estado (`pendiente`, `en_proceso`, `listo`).
3. Trabajar con un stack corto y repetible.
4. Aplicar las paletas anteriores para que:
   - **Juliano** se vea técnico;
   - **Keidy** se vea administrativo-procedimental;
   - **Amaal** se vea administrativo-operativo y orientado al servicio.

## 11. Siguiente paso recomendado

El siguiente paso ideal no es generar todos los anexos de una vez, sino definir:

- cuáles van a entrar realmente en cada informe;
- cuál será la **letra definitiva** de cada anexo;
- y con qué lenguaje exacto se hará cada uno.

Después de eso, se puede preparar:

1. un **plan de producción de anexos por estudiante**; o
2. directamente los **archivos fuente listos para Kroki**.
