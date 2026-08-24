# Anexos y diapositivas — Informe de Juliano

## Propósito

Este documento reúne los hallazgos y decisiones de trabajo para ampliar el
informe de pasantía de Juliano con:

- un pseudocódigo general y defendible de BaseAccess;
- fotografías del proceso de diseño, desarrollo, depuración y control de
  versiones;
- capturas claras del funcionamiento del prototipo;
- una estructura de anexos reutilizable luego en la presentación oral.

La fuente académica de verdad sigue siendo
`juliano/contenido.py`. El informe se genera con
`generador_informe.py` mediante `selector.py`.

## Fuentes Autoritativas

- Informe de Juliano: `juliano/contenido.py`.
- Generador: `generador_informe.py`.
- Orquestador: `selector.py`.
- Diagramas y fuentes técnicas: `anexos_codigo_iutecp_estilos/juliano/`.
- Imágenes incorporadas al informe: `juliano/imagenes/`.
- Propuesta académica: `ANEXOS_PROPUESTOS.md`.
- Reglas visuales y normativas: `GUIA_ANEXOS_CODIGO_Y_ESTETICA_IUTECP.md`.
- Aplicación documentada: `/home/user/Documentos/proyecto/baseaccess/`.

Comando principal de regeneración:

```bash
./selector.py --estudiantes juliano --acciones informe
```

El informe completo se copia en:

- `juliano/reportes/Informe_Pasantia_IUTECP.docx`
- `juliano/reportes/Informe_Pasantia_IUTECP.pdf`

## Generación con Kroki

Los diagramas técnicos existentes se generaron con Kroki ejecutado mediante
Docker. La configuración está en:

- `anexos_codigo_iutecp_estilos/compose.yaml`;
- `anexos_codigo_iutecp_estilos/generar_png.sh`;
- `anexos_codigo_iutecp_estilos/juliano/`.

El servicio se publica localmente en `http://127.0.0.1:8000`. Para levantarlo
solo durante la sesión, sin habilitarlo al inicio del sistema:

```bash
cd /home/user/Documentos/tarea_pasantia/anexos_codigo_iutecp_estilos
sudo systemctl start docker
docker compose -f compose.yaml up -d
```

El script general recorre los tres estudiantes y puede regenerar todos los
PNG:

```bash
./generar_png.sh
```

Para el Anexo H se usó una solicitud individual a
`http://127.0.0.1:8000/graphviz/png`, evitando sobrescribir los PNG existentes.
La fuente reproducible quedó en
`juliano/05_pseudocodigo_general_baseaccess.dot` y el resultado en
`juliano/png/05_pseudocodigo_general_baseaccess.png`.

## Estado Inicial

El informe vigente tenía 48 páginas físicas y nueve anexos:

| Anexo | Contenido | Archivo |
|---|---|---|
| A | Árbol del problema | `3.png` |
| B | Flujograma AS-IS | `02_flujo_as_is_presidencia.png` |
| C | Flujograma TO-BE | `03_flujo_to_be_sistema_automatizado.png` |
| D | Modelo relacional | `04_modelo_relacional_documental.png` |
| E | Arquitectura lógica | `06_arquitectura_prototipo.png` |
| F | Secuencia de registro y despacho | `07_secuencia_registro_despacho.png` |
| G | Estados del expediente | `08_estados_expediente.png` |
| H | Mapa de módulos | `11_mapa_modulos_interfaz.png` |
| I | Respaldo periódico SQLite | `12_proceso_respaldo_sqlite.png` |

La propuesta revisada considera redundantes los anexos H e I. Se reemplazan,
no se acumulan, para evitar un informe innecesariamente largo.

## Estructura Final

Se conservarán los anexos técnicos A–G y se añadirán tres anexos temáticos:

| Anexo | Nuevo contenido | Evidencia |
|---|---|---|
| A–G | Diagramas técnicos existentes | Fuentes Mermaid/PlantUML y PNG existentes |
| H | Pseudocódigo general de operación de BaseAccess | `05_pseudocodigo_general_baseaccess.png` |
| I | Memoria fotográfica del desarrollo | Seis imágenes de `/home/user/Imágenes/anexos/` |
| J | Evidencias visuales del prototipo | Siete capturas claras del manual |

Cada fotografía o captura del anexo I/J ocupa una página propia cuando sea
necesario para conservar legibilidad. El generador ya escribe automáticamente
una página nueva para cada imagen adicional, conservando el título individual
de cada fotografía o captura.

## Resultado Actual

La regeneración posterior a la integración produjo:

- `juliano/reportes/Informe_Pasantia_IUTECP.docx`;
- `juliano/reportes/Informe_Pasantia_IUTECP.pdf`;
- 60 páginas físicas en papel carta después de eliminar el salto vacío del
  Anexo I;
- anexos correlativos A–J;
- seis páginas de memoria fotográfica y siete páginas de capturas del sistema;
- una página legible para el pseudocódigo, con el límite de imagen ajustado a
  `17 cm` de alto para evitar una página en blanco antes del gráfico.

## Anexo H: Pseudocódigo

El pseudocódigo debe representar el flujo general, no cada función del código
actual. La versión académica debe ser comprensible para un lector que no vaya
a revisar el repositorio.

### Secuencia conceptual

1. Iniciar la aplicación y recuperar o solicitar una base SQLite.
2. Validar el archivo, la versión del esquema y los permisos.
3. Abrir SQLite con claves foráneas, WAL y tiempo de espera.
4. Crear el esquema o ejecutar migraciones pendientes dentro de transacciones.
5. Cargar módulos, catálogos, hoja activa y registros paginados.
6. Recibir acciones del usuario: registrar, editar, consultar, filtrar,
   historial, exportar o respaldar.
7. Normalizar y validar fechas, números, catálogos, documentos y frentes.
8. Detectar duplicados en los identificadores configurados.
9. Guardar inserciones o actualizaciones, asociaciones y vínculos en una
   transacción con `COMMIT` o `ROLLBACK`.
10. Generar instantáneas de historial y actualizar la consulta visible.
11. Exportar XLSX cuando existan resultados y filtros válidos.
12. Crear y rotar respaldos, cerrar SQLite y limpiar el estado al salir.

### Correspondencia con la implementación

- Inicio Wails: `baseaccess/main_wails.go`, `baseaccess/app.go`.
- Apertura y migraciones: `baseaccess/app.go`, funciones
  `AbrirBaseDatos`, `initializeDatabaseSchema` y `applySchemaMigrations`.
- Esquema: `baseaccess/data/sql/01_master_control_docs_presidencia.sql` y
  `02_modulos_adicionales.sql`.
- Guardado transaccional: `GuardarFila` y `withTx` en `baseaccess/app.go`.
- Validación del formulario: `baseaccess/handler.go` y `baseaccess/app.go`.
- Historial: `ObtenerHistorialFila`, vistas y triggers SQL.
- Consulta y paginación: `baseaccess/app.go` y `baseaccess/handler.go`.
- Exportación: `baseaccess/handler_export.go`.
- Interfaz: `baseaccess/web/templates/` y
  `baseaccess/web/static/vendor/`.

El pseudocódigo no debe afirmar que todos los módulos actuales existían al
inicio de la pasantía. Debe hablar del prototipo desarrollado para registro,
consulta, historial, trazabilidad y reportes.

## Anexo I: Fotografías del Desarrollo

El usuario autorizó incorporar las seis imágenes completas, sin recorte ni
redacción adicional. Se conservarán con nombres simples y ordenados:

| Orden | Archivo en `juliano/imagenes/` | Descripción |
|---|---|---|
| I-1 | `foto-borrador-diseno-interfaz.jpg` | Borrador de diseño de la interfaz |
| I-2 | `foto-desarrollo-opencode-laptop.jpg` | Desarrollo y verificación desde el portátil |
| I-3 | `foto-desarrollo-telefono.jpg` | Desarrollo y seguimiento desde el teléfono |
| I-4 | `foto-error-antiguo-programa.jpg` | Error de una versión anterior del programa |
| I-5 | `foto-github-repositorio.png` | Repositorio y control de versiones |
| I-6 | `foto-opencode.png` | Uso de OpenCode durante el desarrollo |

Fuentes originales:

- `/home/user/Imágenes/anexos/borrador_de_diseño_interfaz.jpg`
- `/home/user/Imágenes/anexos/desarrollo_en_opencode_laptop.jpg`
- `/home/user/Imágenes/anexos/desarrollo_usando_el_telefono.jpg`
- `/home/user/Imágenes/anexos/error_antiguo_en_el_programa.jpg`
- `/home/user/Imágenes/anexos/github.png`
- `/home/user/Imágenes/anexos/opencode.png`

Las imágenes muestran pantallas, URLs, rutas, repositorios y herramientas de
desarrollo. Se incorporan completas por decisión expresa, pero deben revisarse
una última vez antes de la entrega institucional para confirmar que no revelan
información que deba permanecer privada.

## Anexo J: Capturas del Prototipo

Se utilizarán las variantes claras del manual, adecuadas para impresión:

| Orden | Archivo fuente | Título formal |
|---|---|---|
| J-1 | `registro-nuevo-contexto.png` | Vista general de la interfaz y navegación modular de BaseAccess |
| J-2 | `registro-formulario-general.png` | Formulario estructurado para el registro de información documental |
| J-3 | `modulo-expedientes-frentes.png` | Adaptación dinámica del formulario para procesos con múltiples frentes |
| J-4 | `catalogos-gestion-validaciones.png` | Administración centralizada de catálogos y reglas de validación |
| J-5 | `ruta-seleccion-multiple.png` | Cronograma interactivo de procesos con selección múltiple de actividades |
| J-6 | `exportacion-filtros-columnas.png` | Configuración de filtros y columnas para la exportación de información |
| J-7 | `registro-papelera-restaurar.png` | Recuperación y eliminación definitiva de registros mediante la papelera |

Origen de las capturas claras:

`/home/user/Documentos/proyecto/baseaccess/docs/manual/img/light/`

No se incluirán las 38 capturas: las siete elegidas cubren interfaz, captura,
reglas de negocio, catálogos, Ruta, exportación y protección de datos sin
repetir formularios equivalentes.

## Identidad Visual

Los anexos técnicos de Juliano conservan una identidad sobria e industrial:

- rojo vino principal: `#8F1D2C`;
- rojo medio: `#C94F5D`;
- rojo claro: `#F7DDE1`;
- texto oscuro: `#24171A`;
- fondo de diagramas: preferiblemente blanco para impresión;
- tipografía: Arial, con Liberation Sans como respaldo;
- bordes finos, conectores oscuros y ausencia de sombras.

El generador institucional mantiene títulos y fuentes en Times New Roman. La
identidad sans-serif se reserva para el contenido gráfico.

## Referencias en el Cuerpo

Los anexos deben aparecer explicados antes de la sección de referencias. Las
actividades de Juliano ya mencionan diseño, SQLite, interfaz, pruebas,
depuración, Wails, manual y preparación de anexos. Las referencias nuevas deben
reforzar esa cadena:

- Semana 2: diseño relacional y pseudocódigo de la solución.
- Semana 3: implementación de SQLite, formularios y consultas.
- Semana 4: interfaz y organización del código fuente.
- Semana 6: empaquetado Wails y ejecutable.
- Semana 7: pruebas funcionales y depuración.
- Semana 8: manual y organización de entregables.
- Semana 9: consolidación del informe y anexos definitivos.

Las frases añadidas deben ser breves y no inventar métricas, usuarios,
resultados de rendimiento ni responsabilidades empresariales.

## Validación

Después de modificar `contenido.py` y copiar los recursos:

```bash
cd /home/user/Documentos/tarea_pasantia
python3 -m py_compile juliano/contenido.py generador_informe.py selector.py
./selector.py --estudiantes juliano --acciones informe
pdfinfo juliano/reportes/Informe_Pasantia_IUTECP.pdf
```

Comprobar manualmente:

- anexos correlativos A–J;
- lista de anexos y páginas actualizada;
- una portadilla `ANEXOS` independiente;
- títulos `ANEXO X` y pies individuales legibles;
- fuente debajo de cada anexo/fotografía;
- imágenes sin deformación ni recorte accidental;
- capturas claras y fotografías completas;
- ausencia de páginas en blanco inesperadas;
- referencias a anexos en el Capítulo IV;
- DOCX y PDF generados en la misma ejecución.

## Preparación de Diapositivas

La presentación oral se implementa como un deck de **20 diapositivas** en
`juliano/presentacion/index.html`. El generador de referencia es
`juliano/presentacion/generar_presentacion.py`.

El deck cumple estas decisiones de alcance:

- no contiene barra lateral, rail ni navegación visual lateral;
- no utiliza encabezado, pie, numeración, barra de progreso, controles visuales
  ni metadata ornamental;
- construye rutas, flujos, tarjetas, matrices, expediente, arquitectura e
  interfaz mediante HTML y CSS nativos;
- no contiene etiquetas `<img>` ni depende de las imágenes de los anexos para
  regenerarse;
- conserva Reveal.js, controles de teclado, notas del expositor con `S` y
  `prefers-reduced-motion`;
- mantiene una diapositiva de pausa titulada **“Demostración del prototipo”**
  para cambiar al portátil.

## Guion Exacto de la Presentación

La fuente ejecutable del guion es
`juliano/presentacion/generar_presentacion.py`; el archivo generado es
`juliano/presentacion/index.html`. Cada sección incluye una nota concisa de
25–40 segundos, con lenguaje académico y sin métricas inventadas.

| Nº | Título o idea central | Visual nativo | Idea oral |
|---|---|---|---|
| 1 | Del expediente al dato trazable | Ruta `registrar / seguir / reportar` | Presentar la transformación del flujo documental en un recorrido visible. |
| 2 | Presidencia funciona como un nodo de tránsito documental. | Nodo central con origen y destino | Explicar la posición intermedia de Presidencia en el movimiento de expedientes. |
| 3 | Cada expediente atraviesa seis movimientos. | Secuencia CSS de seis pasos | Recorrer recepción, revisión, ingreso, firma, egreso y despacho. |
| 4 | ¿Cómo mejorar el control, la trazabilidad y los reportes documentales? | Pregunta central y tres necesidades | Introducir la interrogante que ordena el diagnóstico y la solución. |
| 5 | El control se apoyaba en hojas de cálculo. | Hoja conceptual con registros dispersos | Explicar la transcripción manual necesaria para registrar y resumir. |
| 6 | El problema no era almacenar datos. | Fila aislada frente a secuencia conectada | Diferenciar una fila informativa de un recorrido reconstruible. |
| 7 | Tres efectos operativos. | Repetición conectada con tres impactos | Presentar duplicidad, omisión y demora en reportes como riesgos operativos. |
| 8 | Trazabilidad es poder demostrar qué ocurrió. | Expediente con cuatro evidencias | Relacionar responsable, fecha, acción y estado con Gómez (2019). |
| 9 | Objetivo general | Tipografía que destaca controlar, trazar y reportar | Exponer el alcance del prototipo sin prometer resultados medidos. |
| 10 | El proyecto avanzó del diagnóstico a una solución viable. | Camino de cuatro etapas | Ubicar el trabajo como proyecto factible: diagnosticar, determinar, diseñar, implementar y validar. |
| 11 | La solución debía responder a tres necesidades. | Módulos de registro, historial y reporte | Vincular el alcance con las necesidades identificadas. |
| 12 | El proceso se conserva; la información se estructura. | Flujo real y flujo estructurado | Mostrar que la propuesta conserva la secuencia y organiza sus datos. |
| 13 | El expediente es la unidad central del modelo. | Expediente conectado con cuatro entidades | Explicar relaciones con catálogos, documentos, frentes e historial. |
| 14 | Tres capas, una responsabilidad por nivel. | WebView2, Wails/Go y SQLite | Presentar la arquitectura por responsabilidad, no como inventario tecnológico. |
| 15 | Cada cambio se procesa como una transacción. | Flujo de validación con COMMIT/ROLLBACK | Explicar cómo se protege la consistencia del registro y su historial. |
| 16 | La interfaz traduce el modelo al trabajo cotidiano. | Ventana nativa con navegación, formulario y tabla | Mostrar cómo el modelo se convierte en acciones concretas. |
| 17 | La información registrada vuelve como seguimiento y reporte. | Consulta, historial y exportación XLSX | Conectar el registro con las salidas que puede utilizar el área. |
| 18 | La validación comprobó el recorrido completo. | Matriz de cuatro pruebas funcionales | Relacionar registro, consulta, historial y reporte con datos representativos. |
| 19 | Demostración del prototipo | Ruta de tres acciones para la demostración | Cambiar al portátil y ejecutar registrar, consultar historial y exportar reporte. |
| 20 | Resultado: un prototipo funcional y técnicamente viable. | Expediente final con sello `TRAZABLE` | Cerrar con adopción progresiva, capacitación y respaldos periódicos. |

### Regla de exposición

Cada diapositiva debe responder una sola pregunta. No leer los textos de las
capturas ni explicar cada función. La secuencia oral es:

`problema observado → proceso modelado → solución construida → evidencia validada → aporte y siguiente paso`.

### Diseño de la presentación

- Paleta: rojo vino `#8F1D2C`, vino profundo `#54131D`, rosa claro
  `#F3D6D8`, papel cálido `#F7F0E7`, texto ciruela `#24191B`, dorado
  auxiliar `#D6A252` y verde sobrio para estados verificados.
- Tipografía: Georgia/Times New Roman para tesis y títulos; Arial/Liberation
  Sans para datos y etiquetas estrictamente necesarias.
- Firma visual: expediente, líneas de recorrido y sello final `TRAZABLE`,
  integrados como bloques CSS y no como anexos pegados.
- Composición: lienzo completo, sin sidebar, header, footer, numeración,
  controles visibles ni elementos de relleno fuera del argumento de cada
  diapositiva.
- Movimiento: transiciones suaves de Reveal.js y desactivación efectiva cuando
  el usuario solicita `prefers-reduced-motion`.
- Formato de exposición: 1280x720 en escritorio y 390x844 en móvil.

### Regeneración y presentación

```bash
cd /home/user/Documentos/tarea_pasantia
python3 juliano/presentacion/generar_presentacion.py
python3 -m http.server 8000
```

Abrir `http://localhost:8000/juliano/presentacion/`. Las notas del expositor
están dentro de cada diapositiva y se abren con `S`; `F` activa pantalla
completa y las flechas cambian de diapositiva.

### Publicación en GitHub Pages

El workflow `.github/workflows/deploy-pages.yml` publica el HTML generado en
cada push a `main`, sin copiar las imágenes de los anexos. La URL esperada es:

`https://juljuliano.github.io/tarea_pasantia/`

### Comprobaciones de Aceptación

Desde `/home/user/Documentos/tarea_pasantia`:

```bash
python3 -m py_compile juliano/presentacion/generar_presentacion.py
python3 juliano/presentacion/generar_presentacion.py
python3 - <<'PY'
from pathlib import Path

html = Path("juliano/presentacion/index.html").read_text(encoding="utf-8")
assert html.count("<section ") == 20
assert html.count('<aside class="notes">') == 20
assert html.count("<img") == 0
assert "../imagenes" not in html
assert "dossier-rail" not in html
assert "rail-step" not in html
assert "meta-line" not in html
assert "progress-line" not in html
PY
git diff --check
```

La revisión visual debe confirmar que el deck carga en 1280x720 y 390x844 sin
desplazamiento horizontal, que no aparece una barra lateral, que el texto
principal conserva legibilidad y que la diapositiva 19 deja una pausa clara
para la demostración en vivo.

## Pendientes Posteriores

- Revisar el texto final de cada pie de fotografía.
- Confirmar con el tutor que las seis imágenes completas pueden divulgarse.
- Revisar si el diagrama de estados debe llamarse “Etapas del flujo documental”
  para no confundirlo con los valores reales del catálogo de estatus.
- Preparar el guion oral a partir de la secuencia de diapositivas.
- No añadir anexos solo para aumentar la cantidad: cada uno debe respaldar una
  actividad, técnica, resultado o producto mencionado en el informe.
