# Contexto del Proyecto - Juliano
> Archivo de contexto para sesiones con IA. Actualizar a medida que avance el proyecto.

---

## 1. Datos Generales
- **Pasante:** Juliano
- **Carrera:** TSU en Informática — IUTECP (El Tigre, Anzoátegui)
- **Empresa:** Venangocupet, S.A. (empresa mixta adscrita a la CVP)
- **Área de pasantía:** Departamento de Presidencia
- **Tutor industrial:** Ing. Yasmin Sabaneta — C.I. 14.187.924
- **Tutor académico:** Ing. Mejías José — C.I. 4.273.815
- **Duración:** 9 semanas

---

## 2. Proyecto
- **Título:** Por confirmar
- **Modalidad:** Proyecto Factible
- **Objetivo general:** Desarrollar un sistema de escritorio para el
  registro, seguimiento y generación de reportes del flujo documental
  del Departamento de Presidencia de Venangocupet, S.A.

---

## 3. Problema Identificado
- **Situación:** El registro de correspondencia y expedientes se lleva
  manualmente en Excel, con copiado y pegado propenso a errores
- **Deficiencias concretas:**
  - Duplicidad y omisión de datos por entrada manual
  - Tiempo excesivo redactando resúmenes y reportes para la directiva
  - Sin trazabilidad del ciclo de vida de cada expediente
  - Sin capacidad de auditoría en tiempo real ni resúmenes mensuales
    inmediatos
- **Impacto:** Retrasos que paralizan operaciones en otros departamentos
  que dependen de la firma presidencial

---

## 4. Lógica del Negocio
- El departamento solo recibe, revisa, registra, canaliza y despacha.
  No genera documentos propios ni retiene expedientes permanentemente
- **Relación de datos:** 1 proceso → N documentos (ej. un contrato de
  izamiento genera: Acta de Inicio, Decisión Gerencial, Adjudicación)
- **Volumen regular:** ~10 documentos / ~5 procesos concurrentes
- **Volumen alta demanda:** ~20 documentos / ~7 procesos simultáneos
- **Perfil del usuario:** Personal administrativo con buenas competencias
  tecnológicas. La interfaz mantiene paradigmas visuales tipo Excel para
  facilitar la transición

---

## 5. Flujo del Proceso Actual
1. Recepción externa del expediente
2. Revisión de forma (errores tipográficos, ortográficos y de formato)
3. Registro manual en Excel (recepción y estado)
4. Entrega al Presidente para firma
5. Recepción del documento firmado, registro de salida y despacho al
   departamento destino

---

## 6. Solución Desarrollada
- **Stack definitivo:** Wails + WebView2 portable + SQLite
- **Interfaz:** HTML / CSS / JS (visual tipo tabla/Excel)
- **Funciones principales:**
  - Registro de procesos y documentos vinculados
  - Historial interactivo de movimientos por expediente
  - Generación automática de reportes y resúmenes para la directiva

---

## 7. Cronología del Desarrollo
- **Semana 1:** Análisis del flujo. Intentos con MySQL+Python+Rust
  (descartado por permisos) → SQLite + LibreOffice Portable
- **Semanas 2–3:** Formularios en LibreOffice Base → descartado por
  limitaciones en vistas dinámicas → pivote a entorno web + Electron
- **Semana 4:** Interfaz casi lista en Electron → migración a Wails
  (WebView2 portable, más liviano)
- **Semanas 5–9:** Finalización de funciones, pruebas, manuales y
  redacción del informe académico

---

## 8. Restricciones Técnicas (NO mencionar en el informe)
- Prohibición de ingresar laptops personales
- PC corporativa sin permisos de administrador
- Sin instalación de MySQL, drivers ODBC ni librerías nativas
- Drivers de GPU obsoletos (incompatible con Rust/Egui)
- Sin WebView2 nativo en el SO (resuelto con versión portable)
- No mencionar confidencialidad de la información en el informe

---

## 9. Preferencias del Tutor Académico
- Exige árbol del problema
- Revisar planificación integral de objetivos
- Revisar cronograma de actividades (Diagrama de Gantt)
- Misión y Visión: el contenido va en normal, no en cursiva
- Subtítulos en minúscula y alineados a la izquierda, sin numeración
- Entregas del Cap. I y Cap. II son por separado

---

## 10. Pendientes / Notas Activas
- [ ] Confirmar título definitivo del proyecto
- [ ] Árbol del problema
- [ ] Revisar planificación integral de objetivos
- [ ] Revisar cronograma / Diagrama de Gantt
- [ ] Completar redacción del informe académico (semanas 5–9)
