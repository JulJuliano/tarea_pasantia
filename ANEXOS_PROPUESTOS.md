# ANEXOS PROPUESTOS — VERSIÓN REVISADA Y FACTIBLE

> Esta versión sustituye el inventario amplio como propuesta operativa.
> No asigna letras definitivas. Las letras deben cerrarse después de ordenar los anexos institucionales.
> Solo se incluyen anexos que son viables con la información y productos actualmente disponibles o claramente respaldados por las actividades descritas en los informes.

## Criterios de selección

1. El anexo debe corresponder a una actividad, técnica, resultado o producto mencionado en el informe.
2. No se incorpora un anexo solo porque pueda generarse por código.
3. No se inventan cifras, rangos monetarios, responsables, indicadores medidos ni estructuras internas no confirmadas.
4. Se evita duplicar información entre anexos.
5. Los anexos ya existentes no se rediseñan cuando cumplen su función.
6. Los organigramas permanecen en el Capítulo I, salvo que posteriormente deban moverse por razones de espacio.
7. Los códigos fuente deben conservar la identidad visual definida para cada estudiante.

---

# 1. Juliano — Informática / Venangocupet

## Conjunto recomendado

### 1. Árbol del problema del control documental
- Estado: existente.
- Acción: conservar el anexo actual.
- No rediseñar.
- Función: evidencia de la técnica utilizada para diagnosticar la problemática.

### 2. Flujograma AS-IS del proceso documental de Presidencia
- Lenguaje sugerido: Mermaid.
- Función: representar el proceso real observado antes del prototipo.
- Debe mostrar recepción, revisión, registro de ingreso, firma, registro de egreso y despacho.

### 3. Flujograma TO-BE con apoyo del prototipo
- Lenguaje sugerido: Mermaid.
- Función: mostrar cómo el prototipo apoya el mismo proceso sin modificar las responsabilidades reales del Departamento de Presidencia.

### 4. Diagrama Entidad-Relación de la base de datos
- Lenguaje sugerido: DBML o PlantUML ER.
- Función: evidenciar el diseño lógico de la base de datos.
- Debe mantener únicamente relaciones y campos respaldados por el esquema real del prototipo.

### 5. Arquitectura del prototipo
- Lenguaje sugerido: C4-PlantUML.
- Función: mostrar de forma académica la relación entre interfaz, Wails, lógica de aplicación y SQLite.

### 6. Diagrama de secuencia de registro y despacho
- Lenguaje sugerido: PlantUML Sequence o Mermaid Sequence.
- Función: evidenciar la interacción entre el usuario, prototipo, base de datos y actores del proceso.

### 7. Diagrama de estados del expediente
- Lenguaje sugerido: Mermaid stateDiagram.
- Función: representar la evolución del expediente dentro del flujo documental.

### 8. Matriz de casos de prueba y resultados funcionales
- Incluir solo si se dispone de los casos realmente ejecutados durante la validación del prototipo.
- Función: demostrar la actividad de pruebas descrita en las pasantías.
- No inventar resultados.

## Opcionales, solo si existe información real suficiente

### 9. Diccionario de datos
- Incluir únicamente si puede extraerse del esquema SQLite real.

### 10. Matriz de trazabilidad requerimiento → módulo → prueba
- Útil académicamente, pero secundaria frente a la matriz de pruebas.
- Incluir solo si se pueden relacionar requisitos reales con módulos y pruebas realmente ejecutadas.

## Se eliminan de la propuesta principal

- Mapa de módulos de interfaz: puede resultar redundante con arquitectura y flujo TO-BE.
- Proceso de respaldo SQLite: es una recomendación útil, pero no constituye uno de los productos centrales del proyecto.
- Ishikawa adicional: no incorporarlo mientras el informe mantenga el árbol del problema como técnica diagnóstica principal.

---

# 2. Keidy — Administración / Procura

## Conjunto recomendado

### 1. Diagrama de Ishikawa de las causas asociadas a demoras y pérdida de trazabilidad
- Lenguaje sugerido: GraphViz.
- Función: evidenciar la técnica de análisis de causas.
- Mantener identidad visual propia de Keidy.

### 2. Flujograma AS-IS del proceso de procura
- Lenguaje sugerido: Mermaid.
- Función: representar la situación observada antes de la propuesta.

### 3. Flujograma TO-BE del proceso simplificado
- Lenguaje sugerido: Mermaid.
- Función: representar la simplificación administrativa propuesta.

### 4. Swimlane del proceso propuesto
- Lenguaje sugerido: PlantUML Activity.
- Función: mostrar la participación de solicitante, procura, administración, gerencia y proveedor.
- Debe presentarse como propuesta y no como estructura oficial si las responsabilidades no han sido formalmente aprobadas.

### 5. SIPOC del proceso de procura
- Lenguaje sugerido: GraphViz o Mermaid.
- Función: sintetizar proveedores, entradas, proceso, salidas y clientes internos.
- Es útil como visión global, pero puede retirarse si el informe queda demasiado cargado.

### 6. Formato propuesto de requisición / solicitud de compra
- Función: demostrar uno de los productos concretos de la simplificación administrativa.
- Debe identificarse claramente como formato propuesto.
- No agregar códigos, firmas, responsables o campos que la empresa no haya validado.

### 7. Formato de orden de compra o seguimiento de cotizaciones
- Elegir uno de los dos según el producto que realmente haya sido elaborado durante la pasantía.
- Evitar generar ambos únicamente para aumentar la cantidad de anexos.

### 8. Comparación cualitativa AS-IS vs TO-BE
- Puede elaborarse sin tiempos numéricos.
- Comparar únicamente aspectos verificables: uniformidad de formatos, seguimiento, puntos de control, responsabilidades visibles y organización del flujo.

## Opcionales, sujetos a validación

### 9. Matriz RACI
- Solo mantener si los roles asignados pueden defenderse como parte explícita de la propuesta.
- No presentarla como distribución oficial de responsabilidades de la empresa.

### 10. Ficha de indicadores
- Incluir solo cuando estén definidos fórmula, fuente, frecuencia y responsable.
- Puede ser una ficha de indicadores propuestos; no debe presentar valores históricos inexistentes.

## No incluir por ahora

### Matriz de autorización por monto
- No incorporar mientras no existan rangos monetarios reales y niveles de autorización confirmados por la empresa.

### Formato independiente de solicitud de cotización
- No es imprescindible si ya existe un formato de requisición y un formato de orden/seguimiento que demuestren suficientemente la propuesta.

---

# 3. Amaal — Administración / IDETEL

## Conjunto recomendado

### 1. Diagrama de Ishikawa del control de solicitudes
- Lenguaje sugerido: GraphViz.
- Función: evidenciar las causas asociadas a las debilidades de control y trazabilidad.
- Mantener composición e identidad visual propias de Amaal.

### 2. Flujograma AS-IS de afiliaciones e incidencias
- Lenguaje sugerido: Mermaid.
- Función: representar la situación observada antes de la mejora.

### 3. Flujograma TO-BE del proceso estandarizado
- Estado: existente.
- Acción: conservar el flujograma actual.
- No rediseñar.

### 4. Swimlane interdepartamental
- Lenguaje sugerido: PlantUML Activity.
- Función: mostrar la interacción Cliente → Atención al Cliente → Administración → NOC/Técnicos → cierre.

### 5. Diagrama de estados de la solicitud
- Lenguaje sugerido: Mermaid stateDiagram.
- Estados base: recibida, registrada, asignada, en atención, resuelta y cerrada.
- Función: reforzar la idea de continuidad y trazabilidad del caso.

### 6. Formato unificado de registro de afiliación
- Función: evidenciar uno de los productos concretos de la propuesta.
- Debe identificarse como formato propuesto.

### 7. Formato unificado de registro de incidencias
- Función: demostrar la estandarización propuesta para la atención de incidencias.
- No inventar campos empresariales no respaldados.

### 8. Diagrama de comunicación interdepartamental
- Lenguaje sugerido: Mermaid.
- Función: mostrar cómo debe circular la información mínima entre las áreas relacionadas con una solicitud.

### 9. Comparación cualitativa AS-IS vs TO-BE
- Lenguaje sugerido: GraphViz.
- No utilizar cifras de tiempo si no fueron medidas.
- Comparar únicamente cambios procedimentales verificables.

## Opcionales, sujetos a validación

### 10. Matriz RACI
- Incluir solamente si las responsabilidades propuestas pueden sustentarse con el contenido del informe y validación correspondiente.

### 11. Ficha de indicadores de atención
- Incluir solo cuando fórmula, fuente, frecuencia y responsable estén realmente definidos.
- No presentar resultados históricos inexistentes.

## Se mantienen fuera de los anexos complementarios

- Organigrama general.
- Organigrama departamental.

Ambos permanecen en el Capítulo I salvo que posteriormente deban trasladarse por limitaciones de espacio.

---

# 4. Cantidad recomendada

La cantidad final no tiene que ser igual para los tres estudiantes.

## Juliano
- Recomendados: 8.
- Mínimo sólido: 7 si todavía no existe matriz de pruebas real.
- Máximo razonable: 10 con diccionario y trazabilidad.

## Keidy
- Recomendados: 8.
- Puede reducirse a 7 retirando el SIPOC si existe redundancia.
- RACI e indicadores quedan sujetos a validación.

## Amaal
- Recomendados: 9.
- Puede reducirse a 8 si la comparación AS-IS vs TO-BE resulta redundante con los dos flujos.
- RACI e indicadores quedan sujetos a validación.

---

# 5. Prioridad de producción

## Juliano
1. Árbol existente.
2. AS-IS.
3. TO-BE.
4. ERD.
5. Arquitectura.
6. Secuencia.
7. Estados.
8. Matriz de pruebas, cuando estén disponibles los resultados reales.

## Keidy
1. Ishikawa.
2. AS-IS.
3. TO-BE.
4. Swimlane.
5. Formato de requisición.
6. Formato de orden de compra o seguimiento.
7. Comparación AS-IS vs TO-BE.
8. SIPOC, si aporta valor adicional.

## Amaal
1. Ishikawa.
2. AS-IS.
3. TO-BE existente.
4. Swimlane.
5. Estados.
6. Formato de afiliación.
7. Formato de incidencias.
8. Comunicación interdepartamental.
9. Comparación AS-IS vs TO-BE.

---

# 6. Regla final

La selección definitiva debe hacerse después de revisar el cuerpo de cada informe.

Si un anexo no aparece explicado, mencionado o utilizado como evidencia de una actividad, resultado o propuesta, debe retirarse aunque técnicamente pueda generarse.

El objetivo no es tener la mayor cantidad de anexos, sino que cada anexo ayude a demostrar lo que el informe afirma que el pasante diagnosticó, diseñó, ejecutó o propuso.
