# Propuesta de anexos generables por código

> No asignar letras definitivas hasta cerrar el orden de anexos institucionales (técnica del problema, términos básicos, planes semanales y memoria fotográfica). Los anexos siguientes son complementarios y deben incorporarse solo si corresponden a actividades o productos realmente realizados.

## Juliano — Informática / Venangocupet

1. Árbol del problema del control documental — Mermaid o GraphViz.
2. Flujograma AS-IS del proceso documental actual de Presidencia — Mermaid, PlantUML Activity o BPMN.
3. Flujograma TO-BE del proceso con el sistema automatizado — Mermaid, PlantUML Activity o BPMN.
4. Diagrama Entidad-Relación de la base de datos — Mermaid ER, PlantUML ER o DBML/Kroki.
5. Diccionario de datos generado desde el esquema SQLite — Python + sqlite3 → tabla Markdown/HTML/PNG.
6. Diagrama de arquitectura del prototipo — C4-PlantUML o Structurizr.
7. Diagrama de secuencia: registro y despacho de un expediente — Mermaid Sequence o PlantUML Sequence.
8. Diagrama de estados del expediente — Mermaid stateDiagram o PlantUML State.
9. Matriz de trazabilidad requerimiento → módulo → prueba — Python/pandas → tabla.
10. Matriz de casos de prueba y resultados funcionales — Python/pandas → tabla.
11. Mapa de módulos de la interfaz — Mermaid flowchart o C4 Component.
12. Esquema del proceso de respaldo de la base de datos — Mermaid flowchart.

## Keidy — Administración / Procura

1. Diagrama de Ishikawa de causas de demoras y pérdida de trazabilidad — PlantUML/GraphViz o Mermaid adaptado.
2. Flujograma AS-IS del proceso de procura — Mermaid o BPMN.
3. Flujograma TO-BE del proceso simplificado — Mermaid o BPMN.
4. Diagrama tipo swimlane con solicitante, procura, administración, gerencia y proveedor — PlantUML Activity/BPMN.
5. SIPOC del proceso de procura — GraphViz/PlantUML o tabla generada por Python.
6. Matriz RACI del proceso propuesto — Python/pandas → tabla o PlantUML Salt.
7. Matriz de autorización por monto — Python/pandas → tabla; completar solo con rangos reales aprobados por la empresa.
8. Formato propuesto de requisición / solicitud de compra — HTML/CSS o Python → PDF/PNG.
9. Formato de solicitud de cotización — HTML/CSS o Python → PDF/PNG.
10. Formato de orden de compra — HTML/CSS o Python → PDF/PNG.
11. Formato de seguimiento de cotizaciones — Python/pandas → tabla/hoja modelo.
12. Ficha de indicadores del proceso (fórmula, fuente, frecuencia, responsable) — Python/pandas.
13. Comparación AS-IS vs TO-BE por número de pasos/responsables/puntos de control — Python; no usar datos de tiempos si no fueron medidos.

## Amaal — Administración / IDETEL

1. Diagrama de Ishikawa del control de solicitudes — PlantUML/GraphViz o Mermaid adaptado.
2. Flujograma AS-IS de afiliaciones e incidencias — Mermaid/BPMN.
3. Flujograma TO-BE del proceso estandarizado — Mermaid/BPMN.
4. Swimlane Cliente → Atención al Cliente → Administración → NOC/Técnicos → cierre — PlantUML Activity/BPMN.
5. Diagrama de estados de una solicitud: recibida, registrada, asignada, en atención, resuelta, cerrada — Mermaid State/PlantUML State.
6. Matriz RACI de gestión de solicitudes — Python/pandas.
7. Formato unificado de registro de afiliación — HTML/CSS o Python → PDF/PNG.
8. Formato unificado de registro de incidencias — HTML/CSS o Python → PDF/PNG.
9. Ficha de indicadores de atención: tiempo de respuesta, cierre dentro de plazo, reincidencia — Python/pandas; usar fórmulas y datos reales únicamente.
10. Diagrama de comunicación interdepartamental — Mermaid flowchart o PlantUML.
11. Comparación AS-IS vs TO-BE del flujo de solicitudes — Python/GraphViz.
12. Organigrama del departamento y organigrama general — ya existen en Mermaid; mantener en Capítulo I salvo que por tamaño deban pasar a anexos.

## Orden de prioridad sugerido

### Juliano
Árbol del problema → AS-IS → ERD → arquitectura → secuencia → estados → matriz de pruebas.

### Keidy
Ishikawa → AS-IS → TO-BE → swimlane → RACI → matriz de autorización → formatos → indicadores.

### Amaal
Ishikawa → AS-IS → TO-BE → swimlane → estados → RACI → formatos → indicadores.

## Regla de contenido

No agregar un anexo solo porque puede generarse. Cada anexo debe estar mencionado o analizado en el cuerpo del informe y corresponder a una actividad, instrumento, resultado o propuesta realmente elaborada durante la pasantía.
