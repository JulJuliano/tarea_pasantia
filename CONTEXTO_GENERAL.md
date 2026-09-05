# Contexto General — Proyectos de Pasantías IUTECP

> **Documento maestro de contexto para Juliano, Keidy y Amaal.**
>
> Este archivo sustituye los antiguos `contexto.md` individuales. Su finalidad es conservar en un solo lugar la información que debe conocer una persona o una IA antes de revisar, redactar o modificar cualquiera de los tres informes.
>
> **Importante:** los tres estudiantes cursan la misma asignatura de **Pasantías Profesionales** en el IUTECP y comparten el mismo entorno académico/Moodle, la misma normativa institucional y la misma estructura general de informe. Sin embargo, **no todos tienen el mismo tutor académico**, por lo que deben respetarse tanto las reglas comunes como las observaciones particulares de cada tutor.

---

# 1. Contexto académico común

## 1.1 Institución y asignatura

- **Institución:** Instituto Universitario de Tecnología “Elías Calixto Pompa” (IUTECP).
- **Sede de referencia:** El Tigre, estado Anzoátegui.
- **Asignatura / componente:** Pasantías Profesionales.
- **Modalidad de estos tres casos:** pasantías profesionales regulares.
- **No corresponde utilizar como base las disposiciones exclusivas de acreditación por experiencia laboral.**
- Los tres estudiantes cursan la misma materia y utilizan el mismo espacio institucional/Moodle, por lo cual:
  - comparten las mismas normas de transcripción;
  - comparten la estructura general de capítulos;
  - comparten los criterios institucionales de evaluación;
  - pueden recibir indicaciones generales comunes;
  - las correcciones particulares del tutor de cada estudiante tienen que conservarse por separado.

## 1.2 Estructura general del informe

La estructura de trabajo utilizada para los tres informes es:

1. Portada.
2. Contraportada.
3. Aprobación del Tutor Industrial.
4. Aprobación del Tutor Académico.
5. Agradecimiento, si se utiliza.
6. Dedicatoria, si se utiliza.
7. Índice de contenido.
8. Lista de cuadros, si aplica.
9. Lista de figuras, **solo si existen figuras reales**.
10. Lista de gráficos, si aplica.
11. Lista de anexos.
12. Resumen.
13. Introducción.
14. **Capítulo I — Realidad Organizacional.**
15. **Capítulo II — Diagnóstico Situacional.**
16. **Capítulo III — Marco Teórico.**
17. **Capítulo IV — Actividades Realizadas.**
18. **Capítulo V — Conclusiones y Recomendaciones.**
19. Referencias.
20. Anexos.

## 1.3 Regla de coherencia metodológica

Para cualquiera de los tres proyectos debe mantenerse la siguiente correspondencia:

**situación problemática → interrogante → objetivo general → objetivos específicos → planificación integral → Gantt → planes semanales → Capítulo IV → conclusiones → recomendaciones → anexos**

No debe modificarse una parte de esta cadena sin revisar las demás.

## 1.4 Criterios de formato comunes

El generador está diseñado para trabajar, entre otros, con:

- papel carta;
- margen izquierdo de 4 cm;
- márgenes superior, derecho e inferior de 3 cm;
- Times New Roman de 12 pt como texto general;
- 10 pt en cuadros/gráficos cuando corresponde;
- interlineado de 1,5 en el cuerpo general;
- títulos de capítulos en página nueva;
- subtítulos alineados a la izquierda y sin numeración;
- preliminares con números romanos minúsculos;
- numeración arábiga desde la Introducción;
- primera página de Introducción/capítulo/referencias contada pero sin número visible;
- contraportada con la frase:
  **“Informe de pasantías para obtener el título de Técnico Superior Universitario en la especialidad de: …”**
- `LISTA DE FIGURAS` únicamente cuando realmente existen elementos clasificados como figuras;
- `LISTA DE GRÁFICOS` para los elementos visuales que actualmente se están registrando como gráficos.

Siempre debe revisarse visualmente el PDF final porque el código no puede garantizar por sí solo todos los saltos de página.

## 1.5 Archivos comunes del proyecto

- `generador_informe.py`: motor de generación de informes.
- `selector.py`: selector/compilador.
- `revisiones_tutor.md`: historial acumulativo de observaciones y estado de cada corrección.
- `ANEXOS_PROPUESTOS.md`: banco de anexos y diagramas posibles.
- normativa institucional en Markdown/PDF/DOCX.

Antes de modificar contenido académico conviene consultar `revisiones_tutor.md`.

---

# 2. Juliano Cardona — TSU en Informática

## 2.1 Datos generales

- **Pasante:** Cardona, Juliano.
- **C.I.:** 32.281.199.
- **Carrera:** TSU en Informática.
- **Empresa:** Empresa Mixta Petrolera Venangocupet, S.A.
- **Área de pasantía:** Departamento de Presidencia.
- **Tutor industrial:** Ing. Sabaneta, Yasmin — C.I. 14.187.924.
- **Tutor académico:** Ing. Mejías, José — C.I. 4.273.815.
- **Duración documentada:** **9 semanas**.
- La duración de nueve semanas debe mantenerse de forma uniforme en todos sus documentos. No agregar una décima semana para “normalizar” el informe.

## 2.2 Título actual del proyecto

**DESARROLLO DE UN PROTOTIPO DE SISTEMA AUTOMATIZADO PARA EL CONTROL, TRAZABILIDAD Y REPORTE DOCUMENTAL EN LA PRESIDENCIA DE VENANGOCUPET, S.A.**

Este título se adoptó para que el alcance sea coherente con lo realmente ejecutado: análisis, modelado, desarrollo, empaquetado y pruebas de un prototipo.

## 2.3 Objetivo general del proyecto

**Desarrollar un prototipo de sistema automatizado para el control, trazabilidad y reporte de movimientos documentales en la Presidencia de la Empresa Mixta Petrolera Venangocupet, S.A.**

## 2.4 Objetivos específicos actuales

1. **Diagnosticar** la situación actual del flujo procedimental de recepción, revisión, firma y despacho de expedientes en el Departamento de Presidencia.
2. **Determinar** los requerimientos técnicos y funcionales necesarios para el registro, trazabilidad y generación de reportes de los movimientos documentales.
3. **Diseñar** la arquitectura lógica de la base de datos y la interfaz gráfica del sistema de acuerdo con el flujo real del Departamento de Presidencia.
4. **Implementar y validar** el prototipo funcional mediante SQLite y una aplicación de escritorio, comprobando los módulos de registro, consulta, historial y reporte.

## 2.5 Problema identificado

El Departamento de Presidencia funciona como un punto de tránsito y control de expedientes. El proceso real debe describirse de esta forma:

1. recepción del expediente;
2. revisión ortográfica y de formato;
3. registro de ingreso;
4. remisión para firma presidencial;
5. recepción del documento firmado;
6. registro de egreso;
7. despacho al departamento de destino.

**Presidencia no debe describirse como un archivo permanente de expedientes.**

La situación problemática se relaciona con:

- uso de hojas de cálculo para el control;
- transcripción manual y repetitiva;
- riesgo de duplicidad u omisión de registros;
- dificultad para conocer rápidamente el estado/recorrido;
- tiempo adicional para preparar reportes y resúmenes.

## 2.6 Técnica de diagnóstico

- **Árbol del problema.**
- Se encuentra configurado como anexo.
- Imagen prevista: `juliano/imagenes/3.png`.
- Debe coincidir con las causas, problema central y efectos explicados en el Capítulo II.

## 2.7 Solución técnica desarrollada

Stack de referencia:

- Wails;
- interfaz HTML/CSS/JS;
- WebView2 portable;
- SQLite.

Funciones centrales:

- registro de procesos/documentos;
- consulta;
- historial de movimientos;
- trazabilidad;
- reportes/resúmenes.

## 2.8 Restricciones que NO deben aparecer en el informe

Estas notas pueden servir internamente para comprender decisiones técnicas, pero **no deben incorporarse como justificación explícita en el informe**:

- prohibición de ingresar laptop personal;
- ausencia de permisos de administrador;
- imposibilidad de instalar MySQL/ODBC u otras dependencias;
- limitaciones de drivers/GPU;
- ausencia inicial de WebView2;
- no mencionar confidencialidad como condición técnica del proyecto.

La elección de SQLite debe justificarse académicamente por portabilidad, sencillez, arquitectura embebida y adecuación al prototipo, no por restricciones internas de los equipos.

## 2.9 Información institucional de Venangocupet incorporada

La reseña histórica se apoya en material institucional suministrado:

- negociaciones desde 2009;
- aprobación de creación de la empresa mixta en 2010;
- transferencia/entrega durante 2013;
- inicio efectivo de operaciones en marzo de 2014.

### Misión y visión

Se utilizan versiones tomadas del material institucional proporcionado.

### Objetivos organizacionales

Para adaptar el material institucional al esquema IUTECP se conserva:

**Objetivo general de la empresa:**
- Maximizar la recuperación de reservas de hidrocarburos.

**Objetivos específicos / estratégicos:**
- Minimizar los costos operativos y optimizar el uso de todos los recursos.
- Impulsar el desarrollo sustentable de las comunidades vecinas mediante el fortalecimiento de las organizaciones de base y la diversificación económica.
- Cumplir con las políticas, leyes, normas, procedimientos y lineamientos corporativos.
- Conocer y aplicar las resoluciones, decretos y leyes de la industria del petróleo frente a las operaciones de la empresa en materia laboral.
- Incentivar buenas relaciones interpersonales y laborales entre los trabajadores.
- Mantener un alto nivel de comunicación y apoyo con el personal e informar sobre cambios o acciones de interés social y laboral.
- Apoyar los objetivos y metas de la organización en armonía con el desarrollo profesional del empleado.
- Mantener el carácter confidencial de la información operativa y administrativa de la empresa.
- Brindar los beneficios contractuales y velar por las mejoras de las condiciones laborales y calidad de vida de los trabajadores.
- Producir el máximo beneficio posible a accionistas, trabajadores, comunidades vecinas y clientes.

## 2.10 Ubicación y población

### Oficinas administrativas

Las oficinas administrativas utilizadas para la pasantía se describen en:

**Avenida Jesús Subero (vía El Tigre–San José de Guanipa), prolongación de la Calle 19 Sur, sector San Remo, Centro Comercial San Remo Mall, planta baja, Local 89-PB, El Tigre, Municipio Simón Rodríguez, estado Anzoátegui.**

La captura cartográfica usa el Centro Comercial San Remo Mall como referencia porque la empresa no aparece rotulada independientemente en la plataforma cartográfica consultada.

### Población del Departamento de Presidencia

| Cargo | Femenino | Masculino | Total |
|---|---:|---:|---:|
| Presidente | 0 | 1 | 1 |
| Secretaría | 1 | 0 | 1 |
| **TOTAL** | **1** | **1** | **2** |

Para el período documentado no se reportan vacantes en esta unidad.

## 2.11 Imágenes esperadas

Dentro de `juliano/imagenes/`:

- `logo.png` — logotipo de Venangocupet.
- `mapa.png` — ubicación administrativa.
- `1.png` — organigrama general.
- `2.png` — organigrama del Departamento de Presidencia.
- `3.png` — árbol del problema / Anexo A.

El logo debe ir **inmediatamente antes de “Ubicación geográfica”**, acompañado únicamente de título del gráfico y fuente, sin párrafo descriptivo adicional.

## 2.12 Estado actual / pendientes

### Corregido

- título/alcance;
- objetivo general y objetivos específicos;
- árbol del problema;
- planificación integral;
- Gantt interno del informe;
- misión y visión en texto normal;
- introducción ampliada y luego compactada;
- logo;
- mapa;
- cuadro de población;
- ubicación;
- reseña histórica;
- objetivos organizacionales;
- contraportada;
- eliminación de lista de figuras vacía.

### Pendiente

- Juliano realizará personalmente correcciones a las **semanas 8 y 9 de su `cronograma.py`**.
- Después de esas correcciones debe volver a comprobarse:
  - Gantt;
  - Capítulo IV;
  - resumen;
  - conclusiones;
  - anexos.
- Revisar visualmente `3.png` en el PDF final.

---

# 3. Keidy Guzmán — TSU en Administración

## 3.1 Datos generales

- **Pasante:** Guzmán, Keidy.
- **C.I.:** 28.706.352.
- **Carrera:** TSU en Administración.
- **Empresa:** Lubricantes y Equipos Varyna, C.A.
- **Área:** Departamento Administrativo / área de Procura.
- **Cargo de referencia durante la pasantía:** Asistente Administrativo.
- **Tutor industrial:** Rondón, Martina — C.I. 12.208.768.
- **Tutor académico:** Dra. Álvarez, Carmen — C.I. 14.452.956.
- **Duración:** 10 semanas.

## 3.2 Título actual

**PROPUESTA DE SIMPLIFICACIÓN ADMINISTRATIVA DE LA PROCURA EN LUBRICANTES Y EQUIPOS VARYNA, C.A.**

Este título proviene de una corrección expresa de la tutora académica y sustituye el enfoque anterior de “optimización”.

## 3.3 Objetivo general

**Proponer la simplificación administrativa del proceso de procura en el Departamento Administrativo de Lubricantes y Equipos Varyna, C.A., con la finalidad de agilizar el ciclo de adquisición y fortalecer el control interno.**

## 3.4 Objetivos específicos obligatorios

Por instrucción expresa de la tutora deben mantenerse **solo tres**:

1. **Diagnosticar** el proceso actual de procura.
2. **Identificar** las deficiencias, redundancias y causas que generan retrasos o pérdida de trazabilidad.
3. **Formular** la propuesta de simplificación administrativa.

No volver a introducir un cuarto objetivo sin una nueva instrucción de la tutora.

## 3.5 Problema identificado

Aspectos centrales:

- ausencia de canal único/formalizado para recepción de requisiciones;
- formatos no uniformes;
- dificultades de seguimiento de cotizaciones;
- criterios de autorización susceptibles de formalización;
- falta de indicadores básicos;
- cuellos de botella y carga manual de seguimiento.

El diagnóstico está estructurado en:

- **Nivel macro**;
- **Nivel meso**;
- **Nivel micro**.

En el caso de Keidy estos rótulos deben conservarse porque la tutora los solicitó expresamente en su revisión del 06/08/2026.

## 3.6 Técnica del diagnóstico

- **Diagrama causa-efecto / Ishikawa.**
- Complementado con:
  - observación directa;
  - entrevistas;
  - revisión documental/expedientes.

Debe incorporarse su representación gráfica en anexos cuando esté lista.

## 3.7 Propuesta

La propuesta se orienta a:

- flujo simplificado;
- responsables definidos;
- formatos estandarizados;
- criterios/niveles de autorización;
- seguimiento del estatus;
- indicadores de gestión.

Los productos propuestos deben coincidir con lo que finalmente se muestre en los anexos.

## 3.8 Información organizacional

- Empresa con más de 36 años de trayectoria.
- Sector: petrolero, industrial y construcción.
- Vinculada al Grupo Corporativo VTC.
- Población registrada en el informe: **42 trabajadores**.
- Distribución general utilizada:
  - 14 mujeres;
  - 28 hombres.
- El cuadro de población incluye cargos y el área donde se desarrolla la pasantía.

## 3.9 Cronología general

- **Semanas 1–2:** inducción, observación y levantamiento del flujo.
- **Semanas 3–5:** requisiciones, entrevistas, revisión documental y diagnóstico.
- **Semanas 6–7:** diseño del flujo y formatos.
- **Semanas 8–9:** redacción/validación de la propuesta.
- **Semana 10:** presentación/cierre.

El `cronograma.py` fue reajustado para corresponder con los tres objetivos.

## 3.10 Particularidades impuestas por la tutora

- El resumen no debe presentarse como tesis.
- Evitar en el resumen lenguaje como:
  - “investigación”;
  - “estudio”;
  - “proyecto factible”.
- El resumen debe:
  - indicar el objetivo general;
  - resumir la problemática;
  - incluir resultado/conclusión;
  - indicar cómo se atiende la problemática;
  - mantenerse dentro del rango acordado para la entrega.
- Usar **Nivel macro, meso y micro**.
- Incorporar la técnica utilizada.
- Incorporar interrogante que conduzca al objetivo general.
- Mantener solo tres objetivos específicos.
- Incluir bases teóricas sustentadas con autores.
- Incluir bases legales relacionadas y analizar el aporte de cada artículo utilizado.
- El cuadro de planificación debe procurar quedar en una sola hoja y llevar fuente.
- Entregas de Capítulo I y II pueden solicitarse por separado.

## 3.11 Imágenes esperadas

Dentro de `keidy/imagenes/`:

- `logo.jpg` — logotipo de la empresa.
- `1.png` — mapa/ubicación.
- `2.png` — organigrama.
- imagen adicional del Ishikawa cuando sea generada.

El logo debe mostrarse con título y fuente, **sin párrafo descriptivo del logotipo**.

## 3.12 Observaciones del cronograma

Las observaciones semanales fueron restauradas como apoyo porque la estudiante no dispone de tiempo para redactarlas junto con la tutora.

Deben considerarse **texto precargado de apoyo**, especialmente en la semana final, y no una certificación independiente de que la tutora haya emitido literalmente esas frases.

## 3.13 Estado actual / pendientes

### Corregido

- portada/contraportada;
- preliminares;
- introducción;
- título;
- Capítulo I;
- población;
- estructura organizacional;
- resumen;
- macro/meso/micro;
- Ishikawa;
- interrogante;
- tres objetivos;
- planificación;
- Gantt;
- bases teóricas;
- bases legales;
- coherencia con Capítulo IV y conclusiones;
- lista de figuras vacía eliminada.

### Pendiente

- revisar comentarios que la tutora haya insertado directamente en el documento anotado, porque no todos están transcritos en `revisiones_tutor.md`;
- generar/insertar la imagen definitiva del Ishikawa;
- revisión visual del PDF final.

---

# 4. Amaal Alrifaaie — TSU en Administración

## 4.1 Datos generales

- **Pasante:** Alrifaai Alrifaaie, Amaal.
- **C.I.:** 31.985.792.
- **Carrera:** TSU en Administración.
- **Empresa:** Ingeniería de Telecomunicaciones, C.A. (IDETEL / INTELCA).
- **Tutor industrial:** Mata, Lenny — C.I. 8.969.750.
- **Tutor académico:** Dra. Álvarez, Carmen — C.I. 14.452.956.
- **Duración:** 10 semanas.

Keidy y Amaal comparten tutor académico; Juliano tiene tutor académico diferente.

## 4.2 Título actual

**EVALUACIÓN DEL CONTROL ADMINISTRATIVO APLICADO A LA GESTIÓN DE SOLICITUDES DE SERVICIOS DE TELECOMUNICACIONES EN LA EMPRESA INGENIERÍA DE TELECOMUNICACIONES, C.A.**

## 4.3 Objetivo general

**Evaluar el control administrativo aplicado a la gestión de solicitudes de servicios de telecomunicaciones en Ingeniería de Telecomunicaciones, C.A. (IDETEL), con el propósito de identificar sus debilidades y formular mejoras procedimentales.**

## 4.4 Objetivos específicos

1. **Describir** el proceso administrativo actual de recepción, registro, seguimiento y cierre de solicitudes de afiliación e incidencias.
2. **Identificar** las deficiencias presentes en los mecanismos de control.
3. **Analizar** el impacto de las debilidades sobre tiempos de respuesta, trazabilidad y atención al suscriptor.
4. **Proponer** mejoras mediante un flujo estandarizado, formatos y mecanismos básicos de seguimiento.

## 4.5 Contexto real de las actividades

Esta parte debe tomarse como referencia prioritaria porque procede de la explicación suministrada por Amaal:

- **Semanas 1–3:** rotación/apoyo en **Atención al Cliente**.
- **Semanas 4–10:** actividades vinculadas con **Administración**.

La redacción del Capítulo IV y del cronograma debe reflejar esa transición y no presentar toda la pasantía como si se hubiera ejecutado exclusivamente en Administración desde el primer día.

## 4.6 Problema identificado

La problemática se relaciona con:

- ausencia de un procedimiento único formalizado para el seguimiento;
- registros no estandarizados;
- comunicación fragmentada entre áreas;
- dificultad para conocer responsables/estado;
- tiempos de respuesta;
- carencia de indicadores básicos.

La lógica del diagnóstico sigue:

- nivel general/macro;
- nivel intermedio/meso;
- realidad específica/micro.

Se decidió mantener los rótulos macro/meso/micro de forma uniforme con los otros informes, aunque la instrucción expresa más fuerte sobre esos rótulos provino de la tutora de Keidy.

## 4.7 Técnica e instrumentos

- **Técnica de análisis:** diagrama de Ishikawa.
- **Recolección:** observación directa, revisión documental/registros y entrevistas estructuradas.

Debe mantenerse la misma denominación de los instrumentos en:

- planificación integral;
- cronograma semanal;
- Capítulo IV.

No alternar sin explicación entre cuestionario, entrevista no estructurada, entrevista estructurada y guía de observación.

## 4.8 Propuesta

- flujo estandarizado;
- formatos unificados;
- responsables/etapas definidos;
- mecanismos de seguimiento;
- indicadores básicos.

## 4.9 Empresa y población

- Empresa pequeña, con estructura reducida y ajustes recientes de personal.
- Población total indicada: **8 trabajadores**.
- Durante las pasantías se identifican funciones relacionadas con:
  - Supervisión de Administración, Contabilidad y Tributos;
  - Compras y Facturación;
  - Atención al Cliente.
- Amaal apoyó funciones de forma rotativa.

## 4.10 Elementos visuales

El material preparado incluye:

- ubicación;
- organigrama general;
- organigrama del área;
- flujograma del proceso;
- propuesta de Ishikawa.

Dentro de `amaal/imagenes/` se espera:

- `logo.jpg` — logotipo.
- `1.png` — ubicación.
- `2.png` — organigrama general.
- `3.png` — organigrama del departamento.
- `4.png` — Anexo A / flujograma propuesto.

El generador limita proporcionalmente el tamaño de los anexos para que el gráfico no exceda el área útil de la página y deje espacio suficiente para el título.

El logo debe aparecer con título y fuente, **sin descripción textual adicional**.

## 4.11 Observaciones del tutor

- subtítulos en minúscula y alineados a la izquierda;
- preliminares e índices;
- revisión del Capítulo II;
- incorporación de flujograma para visualizar los procesos;
- contenido ajustado a la realidad de la empresa;
- preferencia por apoyo visual.

## 4.12 Estado actual / pendientes

### Corregido

- formato de subtítulos;
- preliminares;
- contraportada;
- diagnóstico;
- flujograma;
- rotación Atención al Cliente → Administración;
- coherencia básica de instrumentos;
- Gantt/actividades reajustados;
- lista de figuras vacía eliminada;
- tamaño máximo de anexos ajustado.

### Pendiente

- generar/insertar Ishikawa definitivo si se decide conservarlo como anexo adicional;
- comprobar en el PDF final que el flujograma se lea con claridad;
- verificar que cronograma y Capítulo IV reflejen exactamente las actividades realmente realizadas.

---

# 5. Tutores y relación entre los tres estudiantes

| Estudiante | Tutor académico | Tutor industrial |
|---|---|---|
| Juliano | Ing. José Mejías | Ing. Yasmin Sabaneta |
| Keidy | Dra. Carmen J. Álvarez | Martina Rondón |
| Amaal | Dra. Carmen J. Álvarez | Lenny Mata |

Esto explica por qué varias reglas y observaciones se parecen entre los tres, pero no deben copiarse automáticamente las correcciones particulares de un tutor al informe de otro estudiante.

## Regla práctica

Cuando una corrección proviene de:

### Normativa / Moodle / instrucciones comunes de la asignatura
Aplicarla a los tres cuando corresponda.

### Tutor académico particular
Aplicarla primero al estudiante al que fue dirigida. Solo extenderla a los otros si:
- coincide con la normativa institucional;
- mejora la coherencia;
- o existe una indicación común equivalente.

---

# 6. Convenciones de trabajo para futuras sesiones

1. **Consultar este archivo primero** para conocer el contexto general.
2. Revisar `revisiones_tutor.md` para saber qué observaciones fueron hechas y cuáles están resueltas.
3. Usar `contenido.py` de cada estudiante como fuente del estado textual actual.
4. Usar `cronograma.py` como fuente de la secuencia semanal actual.
5. No asumir que los antiguos `contexto.md` individuales siguen vigentes.
6. No recuperar automáticamente expresiones antiguas como “Proyecto Factible” si fueron eliminadas por correcciones posteriores.
7. Antes de cambiar objetivos, comprobar la cadena completa de coherencia.
8. No inventar actividades ya realizadas, datos empresariales, leyes, resultados, indicadores o comentarios de tutores.
9. Distinguir entre:
   - **actividad planificada**;
   - **actividad efectivamente realizada**;
   - **producto propuesto**.
10. Toda imagen/anexo debe ser mencionada en el cuerpo del informe antes de presentarse en anexos.

---

# Correo enviado por el profesor recientemente

Buenos días, gusto en saludarlos.

La finalidad de las presentaciones que les hice llegar, es para que ustedes tengan una idea y tengan como comenzar.

La presentación, hacer uso de cualquier herramienta: Power Point, Canva, Prezi, entre otros.

Realmente no es la secuencia de los ejemplos que envíe, la secuencia de la presentación está relacionada con los cinco capítulos del Informe final.

Del capítulo III las bases teóricas más relevantes (3 o 4).

Capítulo IV las actividades semanales las 3 o 4 más importantes.

Capítulo V los más relevante en cada caso.

Igual deben estar preparados:

1. Evaluación del tutor industrial, indispensable.

2. Pago del arancel (75$) y estar solventes. Adjunto envío una información relacionada con el pago en dos partes.

3. Actitud positiva.

En caso de incumplimiento parcial o total de los puntos 1 y 2 no se puede dar la calificación de la presentación.

Como pudieron observar los intervalos de tiempo son de 30 minutos.

20 minutos para hacer la presentación y 10 minutos para las posibles preguntas.

Cualquier información adicional, por favor me escriben por esta vía o WhatsApp en privado.

José Mejías
