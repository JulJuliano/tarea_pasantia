### Contexto Institucional y Académico
* **Autor:** Juliano.
* **Título a optar:** Técnico Superior Universitario (TSU) en Informática.
* **Institución:** Instituto Universitario de Tecnología "Elías Calixto Pompa" (IUTECP).
* **Modalidad del Proyecto:** Proyecto Factible.
* **Duración de las pasantías:** 8 semanas.

### Contexto Corporativo
* **Organización:** Venangocupet, S.A. (empresa mixta adscrita a la CVP).
* **Área de aplicación:** Departamento de Presidencia.
* **Rol del departamento:** Funciona estrictamente como un nodo de revisión, registro y canalización de correspondencia/expedientes presidenciales. No genera documentos propios y su objetivo operativo es no retener ningún expediente de forma permanente.

### Situación Actual y Problemática (Diagnóstico)
* **Proceso actual:**
  1. Recepción externa del expediente.
  2. Revisión de forma (errores tipográficos, ortográficos y de formato).
  3. Registro manual de recepción y estado en una hoja de cálculo (Excel).
  4. Entrega al Presidente para su respectiva firma.
  5. Recepción del documento firmado, registro manual de salida y despacho inmediato al departamento destino.
* **Naturaleza del Flujo Documental (Lógica de Negocio):** Los expedientes no son elementos aislados; pertenecen a procesos administrativos o contratos mayores (ej. contrataciones de servicios de izamiento) que tienen un ciclo de vida secuencial (ej. Acta de Inicio, Decisión Gerencial, Adjudicación). Por tanto, la relación de datos es de 1 a N (Un proceso -> Muchos documentos).
* **Métricas de Volumen:** En escenarios regulares, se procesan aproximadamente 10 documentos vinculados a unos 5 procesos concurrentes. En escenarios de alta demanda, la cifra se duplica a 20 documentos asociados a 7 procesos simultáneos.
* **Deficiencias del Excel actual:**
  * Copiado y pegado manual propenso a errores (duplicidad, omisión).
  * El verdadero cuello de botella radica en la estructuración y formateo visual de la información. Al solicitarse estatus o historiales, el personal invierte demasiado tiempo redactando y organizando la respuesta para la directiva.
* **Riesgos Operativos:** El retraso en el registro o revisión paraliza operaciones críticas en otros departamentos que dependen de la firma presidencial. Falta capacidad de auditoría en tiempo real para generar resúmenes mensuales inmediatos.
* **Perfil del Usuario:** Operado por personal administrativo (ej. Tutora Industrial) con sólidas competencias tecnológicas. Para suavizar la transición, el nuevo sistema mantendrá paradigmas visuales familiares (similares a tablas/Excel) pero automatizando la lógica de reportes.

### 🚫 Restricciones Operativas (Contexto Interno - NO incluir en el informe)
* **Equipos personales:** Prohibición estricta de ingresar o trabajar con laptops personales.
* **Permisos de red e instalación:** La PC corporativa tiene usuario restringido (sin permisos de administrador), impidiendo instalar motores como MySQL, drivers ODBC o librerías nativas del sistema.
* **Hardware y Software desactualizado:** Drivers de GPU obsoletos (rompiendo frameworks como Rust/Egui) y ausencia de WebView2 nativo en el sistema operativo.
* **Confidencialidad:** Queda estrictamente excluido abordar o mencionar temas de confidencialidad de la información en el informe.

### Evolución Técnica y Cronológica (El camino del desarrollo)
* **Semana 1 (Análisis y Pruebas Iniciales):**
  * Bienvenida, presentación del flujo de procesos y debilidades del Excel.
  * *Intento 1:* MySQL + Python + Rust (Egui) -> Descartado por falta de permisos de admin y drivers de GPU.
  * *Intento 2:* Adopción de **SQLite** (portable) y **LibreOffice Portable**. Creación del esquema inicial.
  * Solución a problemas de conexión (driver JDBC, fallo ODBC) mediante script CMD portable, resolviendo un bug de codificación (tildes).
* **Semana 2 y mitad de la Semana 3 (LibreOffice y Pivot Tecnológico):**
  * Configuración de formularios y mejoras del esquema SQLite (integrando la lógica de Procesos vs. Documentos).
  * *Requerimiento clave:* Se solicita desplegar el historial de movimientos interactivo al tocar la fila de un expediente.
  * *Intento 3:* LibreOffice Base resulta limitante para vistas anidadas/dinámicas. Se pivota hacia un entorno web (HTML, CSS, JS) a mitad de la semana 3.
  * Uso temporal de **Electron** al fallar Tauri (por falta de WebView2 en la PC).
* **Semana 4 (Consolidación de la Interfaz):**
  * Desarrollo intensivo de la app con Electron. Interfaz gráfica y funciones principales casi listas.
  * *Intento 4 (Definitivo, fin sem. 4 / inicio sem. 5):* Se logra integrar WebView2 de forma portable (evadiendo la restricción de admin). Se abandona Electron (muy pesado) y se migra a **Wails**.
* **Semanas 5 a 8 (Proyección actual):**
  * Finalización de funciones pendientes, integración definitiva con Wails/SQLite, depuración, pruebas funcionales, redacción de manuales y consolidación del informe académico.
