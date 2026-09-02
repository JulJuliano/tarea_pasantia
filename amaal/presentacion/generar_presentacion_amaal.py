#!/usr/bin/env python3
"""Genera la presentacion autocontenida para la defensa de Amaal Alrifaai.

Uso:
    python3 amaal/presentacion/generar_presentacion_amaal.py

Salida:
    amaal/presentacion/index.html

Controles:
    Flechas / espacio  -> avanzar o retroceder
    F                  -> pantalla completa
    S                  -> mostrar u ocultar notas
    Esc                -> cerrar notas o salir de pantalla completa
"""

from __future__ import annotations

import base64
import mimetypes
from dataclasses import dataclass
from html import escape
from pathlib import Path
from textwrap import dedent


CARPETA = Path(__file__).resolve().parent
CARPETA_IMAGENES = CARPETA.parent / "imagenes"
SALIDA = CARPETA / "index.html"


@dataclass(frozen=True)
class Diapositiva:
    fase: int
    clase: str
    cuerpo: str
    notas: str


def e(texto: str) -> str:
    return escape(texto, quote=True)


def imagen_embebida(nombre: str) -> str:
    ruta = CARPETA_IMAGENES / nombre
    mime = mimetypes.guess_type(ruta.name)[0] or "application/octet-stream"
    datos = base64.b64encode(ruta.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{datos}"


def slide(fase: int, clase: str, cuerpo: str, notas: str) -> Diapositiva:
    return Diapositiva(
        fase=fase,
        clase=clase,
        cuerpo=dedent(cuerpo).strip(),
        notas=dedent(notas).strip(),
    )


LOGO = imagen_embebida("logo.jpg")
ISHIKAWA = imagen_embebida("01_ishikawa_control_solicitudes.png")
SWIMLANE = imagen_embebida("04_swimlane_gestion_solicitudes.png")
ESTADOS = imagen_embebida("05_estados_solicitud.png")
COMPARACION = imagen_embebida("11_comparacion_as_is_to_be.png")


DIAPOSITIVAS: list[Diapositiva] = [
    slide(
        1,
        "cover",
        f"""
        <div class="cover-copy">
          <p class="kicker">DEFENSA DE PASANTÍAS PROFESIONALES</p>
          <h1>Control administrativo de solicitudes de servicio</h1>
          <p class="lead">Evaluación y mejoras procedimentales para IDETEL</p>
          <div class="author-block">
            <strong>Amaal Alrifaai</strong>
            <span>Administración · IUTECP · 2026</span>
          </div>
        </div>
        <div class="cover-ticket" aria-label="Ficha de la defensa">
          <img src="{LOGO}" alt="Logotipo de Ingeniería de Telecomunicaciones, C.A.">
          <div class="ticket-line"><small>CASO</small><b>Solicitud de servicio</b></div>
          <div class="ticket-line"><small>RECORRIDO</small><b>Recepción → cierre</b></div>
          <div class="ticket-status"><i></i> Propuesta formulada</div>
        </div>
        """,
        """
        Saludar al jurado, presentarse y mencionar el título del informe. Explicar que la
        exposición mostrará cómo se evaluó el recorrido administrativo de una solicitud de
        servicio y qué mejoras se formularon para hacerlo trazable.
        """,
    ),
    slide(
        1,
        "route",
        """
        <p class="eyebrow">RUTA DE LA EXPOSICIÓN</p>
        <h2>Seguiremos el recorrido de una solicitud.</h2>
        <div class="route-track">
          <div><b>Contexto</b><span>empresa y área</span></div>
          <div><b>Diagnóstico</b><span>problema y causas</span></div>
          <div><b>Fundamentos</b><span>criterios de control</span></div>
          <div><b>Propuesta</b><span>flujo y seguimiento</span></div>
          <div><b>Cierre</b><span>resultados y recomendaciones</span></div>
        </div>
        """,
        """
        Presentar la ruta sin leer cada palabra. El hilo conductor es el recorrido de una
        solicitud: primero se ubica el contexto, luego se explica el diagnóstico, la base
        conceptual, la propuesta y finalmente los resultados.
        """,
    ),
    slide(
        1,
        "company",
        f"""
        <p class="eyebrow">CONTEXTO ORGANIZACIONAL</p>
        <h2>Ingeniería de Telecomunicaciones, C.A.</h2>
        <div class="company-layout">
          <div class="company-logo"><img src="{LOGO}" alt="Logotipo de IDETEL"></div>
          <div class="fact-stack">
            <div><small>TRAYECTORIA</small><b>Más de cuatro décadas</b></div>
            <div><small>SECTOR</small><b>Telecomunicaciones y automatización</b></div>
            <div><small>SEDE</small><b>El Tigre, Anzoátegui</b></div>
          </div>
        </div>
        """,
        """
        Presentar brevemente a IDETEL como una empresa con trayectoria en telecomunicaciones,
        radiocomunicación, conectividad y automatización. Ubicar la sede y evitar extenderse en
        toda la reseña histórica del informe.
        """,
    ),
    slide(
        1,
        "rotation",
        """
        <p class="eyebrow">ÁREA DE PASANTÍA</p>
        <h2>Dos espacios, un mismo recorrido.</h2>
        <div class="handoff two">
          <article>
            <span class="week-tag">SEMANAS 1–3</span>
            <h3>Atención al Cliente</h3>
            <p>Recepción de solicitudes, registro de pagos y contacto inicial con el suscriptor.</p>
          </article>
          <div class="handoff-arrow">→</div>
          <article>
            <span class="week-tag">SEMANAS 4–10</span>
            <h3>Administración</h3>
            <p>Facturación, documentación, seguimiento de casos y reportes administrativos.</p>
          </article>
        </div>
        <p class="bottom-line">La rotación permitió observar dónde se origina la información y cómo continúa.</p>
        """,
        """
        Explicar la rotación real: tres semanas en Atención al Cliente y siete en Administración.
        Destacar que esta experiencia permitió ver la continuidad del caso entre áreas y no solo
        una tarea aislada.
        """,
    ),
    slide(
        1,
        "journey",
        """
        <p class="eyebrow">RECORRIDO OBSERVADO</p>
        <h2>Una solicitud atraviesa varias áreas.</h2>
        <div class="service-path">
          <div><span>01</span><b>Suscriptor</b><small>presenta el caso</small></div>
          <div><span>02</span><b>Atención</b><small>recibe y registra</small></div>
          <div><span>03</span><b>Administración</b><small>procesa información</small></div>
          <div><span>04</span><b>NOC / Técnicos</b><small>atiende si corresponde</small></div>
          <div><span>05</span><b>Cierre</b><small>comunica el resultado</small></div>
        </div>
        """,
        """
        Describir el recorrido general de una afiliación o incidencia. Señalar que cada transferencia
        requiere información completa y actualización de estatus para evitar que el caso pierda continuidad.
        """,
    ),
    slide(
        2,
        "problem",
        """
        <p class="eyebrow">SITUACIÓN PROBLEMÁTICA</p>
        <div class="problem-statement">
          <h2>No existía un procedimiento único de seguimiento.</h2>
          <div class="case-card">
            <small>CASO ADMINISTRATIVO</small>
            <b>¿Quién lo tiene?</b>
            <b>¿En qué estado está?</b>
            <b>¿Cuándo debe cerrar?</b>
          </div>
        </div>
        """,
        """
        Plantear el problema central: la organización atendía las solicitudes, pero no contaba con
        un procedimiento único y visible desde la recepción hasta el cierre. Eso dificultaba responder
        tres preguntas básicas de control: responsable, estado y tiempo.
        """,
    ),
    slide(
        2,
        "manifestations",
        """
        <p class="eyebrow">MANIFESTACIONES OBSERVADAS</p>
        <h2>Cuatro señales de pérdida de continuidad.</h2>
        <div class="alert-grid">
          <div><span>REGISTRO</span><b>Formatos no uniformes</b></div>
          <div><span>ESTATUS</span><b>Actualización distribuida</b></div>
          <div><span>TIEMPO</span><b>Sin referencia por etapa</b></div>
          <div><span>COMUNICACIÓN</span><b>Transferencia fragmentada</b></div>
        </div>
        """,
        """
        Explicar las cuatro manifestaciones sin convertirlas en causas aisladas. Todas afectan la
        continuidad de la información y obligan al personal a reconstruir manualmente el estado del caso.
        """,
    ),
    slide(
        2,
        "effects",
        """
        <p class="eyebrow">EFECTOS ADMINISTRATIVOS</p>
        <h2>La información dispersa se convierte en demora.</h2>
        <div class="impact-row">
          <div><strong>01</strong><b>Reprocesos</b><p>consultas y verificaciones repetidas</p></div>
          <div><strong>02</strong><b>Mayor respuesta</b><p>más tiempo para ubicar el estatus</p></div>
          <div><strong>03</strong><b>Menor precisión</b><p>información incompleta al suscriptor</p></div>
        </div>
        """,
        """
        Conectar las manifestaciones con sus efectos: reprocesos, aumento del tiempo de respuesta y
        dificultad para informar con precisión al suscriptor. Evitar afirmar que todos los casos fallaban;
        se trata de debilidades que elevan ese riesgo.
        """,
    ),
    slide(
        2,
        "question",
        """
        <p class="eyebrow">INTERROGANTE ORIENTADORA</p>
        <div class="question-box">
          <span>¿</span>
          <h2>Cómo evaluar el control para identificar debilidades y fortalecer la trazabilidad?</h2>
        </div>
        <p class="question-detail">Gestión de solicitudes de servicios de telecomunicaciones en IDETEL</p>
        """,
        """
        Leer la interrogante de forma pausada. Explicar que la pregunta vincula tres acciones: evaluar
        el control existente, identificar debilidades y formular mejoras procedimentales.
        """,
    ),
    slide(
        2,
        "objective-general",
        """
        <p class="eyebrow">OBJETIVO GENERAL</p>
        <div class="objective-focus">
          <span>Evaluar</span>
          <p>el control administrativo aplicado a la gestión de solicitudes de servicios de telecomunicaciones.</p>
        </div>
        <div class="purpose-band">Identificar debilidades <i>+</i> formular mejoras procedimentales</div>
        """,
        """
        Presentar el objetivo general y hacer énfasis en el verbo evaluar. El trabajo no consistió en
        implementar un sistema informático, sino en estudiar el control y formular mejoras viables.
        """,
    ),
    slide(
        2,
        "objectives",
        """
        <p class="eyebrow">OBJETIVOS ESPECÍFICOS</p>
        <h2>Tres etapas de una misma evaluación.</h2>
        <div class="objective-list">
          <article><span>01</span><h3>Diagnosticar</h3><p>el recorrido actual desde la recepción hasta el cierre.</p></article>
          <article><span>02</span><h3>Identificar</h3><p>deficiencias, causas e incidencia sobre tiempos y trazabilidad.</p></article>
          <article><span>03</span><h3>Formular</h3><p>flujo, formatos, responsables e indicadores de seguimiento.</p></article>
        </div>
        """,
        """
        Mostrar la coherencia entre los objetivos: diagnosticar primero, identificar las causas después
        y formular la mejora a partir de los hallazgos. Cada conclusión retomará esta secuencia.
        """,
    ),
    slide(
        2,
        "method",
        """
        <p class="eyebrow">TÉCNICAS DE DIAGNÓSTICO</p>
        <h2>La situación se observó desde cuatro fuentes.</h2>
        <div class="method-grid">
          <div><span>OBS</span><b>Observación directa</b><p>recorrido real de solicitudes</p></div>
          <div><span>DOC</span><b>Revisión de registros</b><p>soportes y casos disponibles</p></div>
          <div><span>ENT</span><b>Entrevistas</b><p>personal de las áreas relacionadas</p></div>
          <div><span>ISH</span><b>Ishikawa</b><p>organización de las causas</p></div>
        </div>
        """,
        """
        Explicar que el diagnóstico combinó observación, revisión documental, entrevistas estructuradas
        y el diagrama de Ishikawa. La combinación evitó depender de una sola percepción.
        """,
    ),
    slide(
        2,
        "diagram-slide",
        f"""
        <p class="eyebrow">DIAGRAMA DE CAUSA–EFECTO</p>
        <h2>Las causas se agruparon en cuatro dimensiones.</h2>
        <figure class="wide-figure">
          <img src="{ISHIKAWA}" alt="Diagrama de Ishikawa del control de solicitudes">
          <figcaption>Procedimiento · comunicación · registro · seguimiento</figcaption>
        </figure>
        """,
        """
        Recorrer el Ishikawa de izquierda a derecha. Resumir cada dimensión con una causa principal y
        cerrar indicando que todas convergen en debilidades de control y trazabilidad.
        """,
    ),
    slide(
        2,
        "findings",
        """
        <p class="eyebrow">HALLAZGO CENTRAL</p>
        <div class="finding-layout">
          <h2>El problema no era recibir el caso.</h2>
          <div class="finding-arrow">→</div>
          <h2>Era mantener visible su continuidad.</h2>
        </div>
        <p class="bottom-line">La mejora debía unir registro, responsable, estatus y tiempo.</p>
        """,
        """
        Sintetizar el diagnóstico con esta idea: la solicitud sí ingresaba, pero su continuidad podía
        perder visibilidad al pasar entre áreas. Esta conclusión orientó directamente la propuesta.
        """,
    ),
    slide(
        3,
        "theory",
        """
        <p class="eyebrow">CONCEPTOS DISCIPLINARES · I</p>
        <h2>Controlar significa hacer visible el proceso.</h2>
        <div class="concept-grid">
          <div><b>Control administrativo</b><p>comparar lo ejecutado con lo esperado</p></div>
          <div><b>Gestión de solicitudes</b><p>recibir, registrar, procesar y cerrar</p></div>
          <div><b>Estandarización</b><p>aplicar criterios y formatos comunes</p></div>
          <div><b>Calidad del servicio</b><p>responder con fiabilidad y oportunidad</p></div>
        </div>
        """,
        """
        Relacionar estos cuatro conceptos con el diagnóstico. El control requiere información; la gestión
        define el ciclo; la estandarización reduce variaciones; y la respuesta administrativa influye en
        la calidad percibida por el suscriptor.
        """,
    ),
    slide(
        3,
        "theory",
        """
        <p class="eyebrow">CONCEPTOS DISCIPLINARES · II</p>
        <h2>La continuidad depende de información compartida.</h2>
        <div class="concept-grid">
          <div><b>Sistemas de información</b><p>centralizar datos para decidir</p></div>
          <div><b>Trazabilidad</b><p>reconstruir el recorrido del caso</p></div>
          <div><b>Comunicación entre áreas</b><p>transferir información completa</p></div>
          <div><b>Indicadores de gestión</b><p>medir tiempos, pendientes y cierres</p></div>
        </div>
        """,
        """
        Explicar el segundo grupo conceptual. La propuesta necesita información disponible, trazabilidad,
        coordinación entre áreas e indicadores que permitan revisar si el procedimiento funciona.
        """,
    ),
    slide(
        3,
        "theory-applied",
        """
        <p class="eyebrow">FUNDAMENTO APLICADO</p>
        <h2>De los conceptos a decisiones concretas.</h2>
        <div class="translation-grid">
          <div><span>CONTROL</span><b>Estados verificables</b></div>
          <div><span>ESTANDARIZACIÓN</span><b>Formatos uniformes</b></div>
          <div><span>TRAZABILIDAD</span><b>Identificación única</b></div>
          <div><span>MEDICIÓN</span><b>Indicadores básicos</b></div>
        </div>
        """,
        """
        No detenerse en definiciones extensas. Mostrar cómo cada concepto se tradujo en una decisión de
        diseño de la propuesta: estados, formatos, identificación e indicadores.
        """,
    ),
    slide(
        3,
        "legal",
        """
        <p class="eyebrow">BASES LEGALES</p>
        <h2>Orden empresarial y claridad documental.</h2>
        <div class="legal-layout">
          <article><span>CONSTITUCIÓN</span><b>Artículo 112</b><p>Fundamento general de la actividad económica privada dentro del ordenamiento jurídico.</p></article>
          <article><span>CÓDIGO DE COMERCIO</span><b>Artículo 32</b><p>Principio de orden y claridad de los registros que acompañan las operaciones mercantiles.</p></article>
        </div>
        <p class="legal-note">Las mejoras complementan el control administrativo; no sustituyen los registros exigidos por la ley.</p>
        """,
        """
        Presentar la base legal con prudencia. El artículo 112 aporta el marco constitucional general y
        el artículo 32 respalda el principio de orden documental. Ninguno regula específicamente el flujo
        de solicitudes estudiado.
        """,
    ),
    slide(
        3,
        "weeks",
        """
        <p class="eyebrow">DIEZ SEMANAS DE PASANTÍA</p>
        <h2>La experiencia avanzó en cuatro momentos.</h2>
        <div class="timeline">
          <article><span>1–3</span><b>Reconocer</b><p>atención, pagos y recorrido inicial</p></article>
          <article><span>4–5</span><b>Diagnosticar</b><p>entrevistas, registros e Ishikawa</p></article>
          <article><span>6–8</span><b>Diseñar</b><p>análisis, flujo y formatos</p></article>
          <article><span>9–10</span><b>Validar</b><p>ajustes, cierre e informe</p></article>
        </div>
        """,
        """
        Resumir las diez semanas por etapas para no leer el cronograma completo. Mencionar que las tareas
        operativas continuaron mientras se desarrollaban las actividades de análisis.
        """,
    ),
    slide(
        3,
        "activities",
        """
        <p class="eyebrow">ACTIVIDADES REALIZADAS</p>
        <h2>Operación y análisis se desarrollaron en paralelo.</h2>
        <div class="activity-split">
          <article>
            <span>APOYO OPERATIVO</span>
            <ul><li>Registro de pagos</li><li>Facturación y documentación</li><li>Seguimiento de casos</li><li>Reportes administrativos</li></ul>
          </article>
          <article>
            <span>TRABAJO DE ANÁLISIS</span>
            <ul><li>Levantamiento del proceso</li><li>Entrevistas y revisión documental</li><li>Diseño de mejoras</li><li>Validación con tutor industrial</li></ul>
          </article>
        </div>
        """,
        """
        Diferenciar las actividades propias del área y las actividades relacionadas con el informe.
        Destacar que ambas se complementaron: la práctica permitió comprender el proceso y el análisis
        permitió formular la mejora.
        """,
    ),
    slide(
        4,
        "proposal",
        """
        <p class="eyebrow">PROPUESTA DE MEJORA</p>
        <h2>Un procedimiento visible de principio a fin.</h2>
        <div class="proposal-grid">
          <div><span>01</span><b>Flujo estandarizado</b></div>
          <div><span>02</span><b>Responsables por etapa</b></div>
          <div><span>03</span><b>Formatos uniformes</b></div>
          <div><span>04</span><b>Estados definidos</b></div>
          <div><span>05</span><b>Tiempos de referencia</b></div>
          <div><span>06</span><b>Indicadores básicos</b></div>
        </div>
        """,
        """
        Presentar la propuesta como un conjunto integrado de seis componentes. Ninguno funciona de forma
        aislada: el flujo define el recorrido, los responsables lo ejecutan y los registros permiten medirlo.
        """,
    ),
    slide(
        4,
        "diagram-slide swimlane",
        f"""
        <p class="eyebrow">FLUJO ESTANDARIZADO</p>
        <h2>Cada transferencia deja un responsable visible.</h2>
        <figure class="wide-figure swimlane-figure">
          <img src="{SWIMLANE}" alt="Swimlane propuesto para la gestión de solicitudes">
          <figcaption>Cliente → Atención al Cliente → Administración → NOC / Técnicos → cierre</figcaption>
        </figure>
        """,
        """
        Explicar el swimlane por áreas. Atención al Cliente recibe, registra y comunica; Administración
        revisa y actualiza; NOC o Técnicos atienden cuando corresponde; finalmente se confirma el cierre
        y el cliente recibe la respuesta.
        """,
    ),
    slide(
        4,
        "states",
        f"""
        <p class="eyebrow">ESTADOS DE LA SOLICITUD</p>
        <h2>El estatus resume dónde está el caso.</h2>
        <figure class="state-figure"><img src="{ESTADOS}" alt="Estados propuestos de una solicitud"></figure>
        <div class="state-benefits">
          <span>Evita términos distintos entre áreas</span>
          <span>Facilita consultas y reportes</span>
          <span>Hace verificable el cierre</span>
        </div>
        """,
        """
        Recorrer los estados: recibida, registrada, asignada, en atención, resuelta y cerrada. Aclarar
        que resuelta y cerrada no son idénticas: el cierre requiere confirmar y registrar el resultado.
        """,
    ),
    slide(
        4,
        "formats",
        """
        <p class="eyebrow">FORMATOS Y RESPONSABILIDADES</p>
        <h2>La misma información acompaña todo el recorrido.</h2>
        <div class="form-preview">
          <div class="form-head"><b>ID DEL CASO</b><b>TIPO</b><b>FECHA</b><b>RESPONSABLE</b></div>
          <div class="form-body"><span>Datos del suscriptor</span><span>Descripción de la solicitud</span><span>Estatus y observaciones</span></div>
          <div class="form-foot"><b>Actualiza:</b> responsable de la etapa <i></i><b>Verifica:</b> supervisión</div>
        </div>
        <p class="bottom-line">Formato común + responsable definido = continuidad verificable</p>
        """,
        """
        Explicar los datos mínimos del formato y la necesidad de identificar quién actualiza cada etapa.
        La finalidad no es añadir formularios, sino evitar registros distintos e información incompleta.
        """,
    ),
    slide(
        4,
        "indicators",
        """
        <p class="eyebrow">INDICADORES BÁSICOS</p>
        <h2>Medir permite detectar dónde se retrasa el proceso.</h2>
        <div class="metric-grid">
          <article><span>TIEMPO</span><b>Promedio de atención</b><p>desde recepción hasta cierre</p></article>
          <article><span>PENDIENTES</span><b>Casos abiertos</b><p>por estado y responsable</p></article>
          <article><span>CUMPLIMIENTO</span><b>Cierres en plazo</b><p>porcentaje dentro de referencia</p></article>
          <article><span>CALIDAD</span><b>Devoluciones</b><p>por información incompleta</p></article>
        </div>
        """,
        """
        Presentar indicadores sencillos y realizables. Señalar que requieren registros uniformes para
        ser comparables y que sirven para detectar retrasos, no para sancionar automáticamente al personal.
        """,
    ),
    slide(
        4,
        "comparison",
        f"""
        <p class="eyebrow">DEL AS–IS AL TO–BE</p>
        <div class="comparison-layout">
          <div>
            <h2>De información dispersa a control verificable.</h2>
            <ul><li>estandarizar</li><li>ordenar</li><li>definir</li><li>medir</li><li>controlar</li></ul>
          </div>
          <figure><img src="{COMPARACION}" alt="Comparación del control actual y propuesto"></figure>
        </div>
        """,
        """
        Usar esta diapositiva para sintetizar el cambio esperado. La propuesta transforma registros no
        unificados y estatus distribuido en formatos uniformes, responsables, estados verificables e indicadores.
        """,
    ),
    slide(
        5,
        "conclusions",
        """
        <p class="eyebrow">CONCLUSIONES · DIAGNÓSTICO</p>
        <h2>El recorrido existía, pero no estaba formalizado como un solo proceso.</h2>
        <div class="conclusion-band">
          <span>Sin flujo único</span><i>→</i><span>responsables poco visibles</span><i>→</i><span>cierre difícil de verificar</span>
        </div>
        """,
        """
        Presentar la primera conclusión vinculada con el objetivo de diagnosticar. El recorrido se
        realizaba entre áreas, pero no estaba formalizado de forma integral desde la recepción hasta el cierre.
        """,
    ),
    slide(
        5,
        "conclusions",
        """
        <p class="eyebrow">CONCLUSIONES · CAUSAS</p>
        <h2>Cuatro debilidades afectaban la trazabilidad.</h2>
        <div class="four-words"><span>formatos</span><span>estatus</span><span>tiempos</span><span>comunicación</span></div>
        <p class="bottom-line">Su efecto conjunto puede prolongar la respuesta al suscriptor.</p>
        """,
        """
        Presentar la segunda conclusión: formatos no uniformes, estatus no centralizado, ausencia de
        tiempos de referencia y comunicación fragmentada. Destacar el efecto conjunto sobre la trazabilidad.
        """,
    ),
    slide(
        5,
        "conclusions",
        """
        <p class="eyebrow">CONCLUSIONES · APORTE</p>
        <h2>La propuesta conecta control, continuidad y servicio.</h2>
        <div class="result-equation">
          <span>flujo</span><i>+</i><span>responsables</span><i>+</i><span>formatos</span><i>+</i><span>indicadores</span><b>= trazabilidad</b>
        </div>
        """,
        """
        Presentar la tercera conclusión vinculada con el objetivo de formular mejoras. Explicar que la
        trazabilidad surge de la combinación de los componentes y no de un único formato o herramienta.
        """,
    ),
    slide(
        5,
        "recommendations",
        """
        <p class="eyebrow">RECOMENDACIONES A IDETEL</p>
        <h2>Implementar primero; digitalizar después.</h2>
        <div class="recommend-grid">
          <article><span>PRIMERO</span><b>Probar el flujo con un grupo controlado.</b></article>
          <article><span>LUEGO</span><b>Uniformar formatos y responsables.</b></article>
          <article><span>REVISAR</span><b>Medir pendientes y tiempos periódicamente.</b></article>
          <article><span>DESPUÉS</span><b>Evaluar una herramienta digital centralizada.</b></article>
        </div>
        """,
        """
        Explicar el orden recomendado. Primero debe formalizarse y probarse el procedimiento; luego se
        miden sus resultados. Una herramienta digital tiene más sentido cuando el flujo ya está validado.
        """,
    ),
    slide(
        5,
        "closing",
        """
        <p class="eyebrow">CIERRE</p>
        <div class="closing-copy">
          <h2>Una solicitud bien atendida también debe estar bien controlada.</h2>
          <p>Gracias por su atención.</p>
          <span>Quedo atenta a sus preguntas.</span>
        </div>
        <div class="closing-status"><i></i><b>CASO PRESENTADO</b><small>Amaal Alrifaai · Administración</small></div>
        """,
        """
        Cerrar con la idea principal, agradecer al jurado y quedar disponible para preguntas. Mantener
        la última diapositiva visible durante la ronda de respuestas.
        """,
    ),
]


FASES = (
    ("01", "Contexto"),
    ("02", "Diagnóstico"),
    ("03", "Fundamentos"),
    ("04", "Propuesta"),
    ("05", "Cierre"),
)


CSS = r"""
:root {
  --paper: #fcfbfe;
  --paper-soft: #faf8fd;
  --lavender: #ede3f7;
  --violet: #9b6bc4;
  --purple: #5b2a86;
  --ink: #24182d;
  --muted: #6d6373;
  --line: #d9c7e8;
  --white: #ffffff;
  --shadow: 0 18px 50px rgba(91, 42, 134, .11);
}

* { box-sizing: border-box; }
html, body { height: 100%; margin: 0; overflow: hidden; width: 100%; }
body {
  background: var(--paper);
  color: var(--ink);
  font-family: Tahoma, "DejaVu Sans", sans-serif;
}
button { font: inherit; }

.deck { height: 100vh; position: relative; width: 100vw; }
.slide {
  background:
    linear-gradient(rgba(91,42,134,.032) 1px, transparent 1px),
    linear-gradient(90deg, rgba(91,42,134,.032) 1px, transparent 1px),
    var(--paper);
  background-size: 32px 32px;
  display: none;
  height: 100vh;
  inset: 0;
  overflow: hidden;
  padding: 7.5vh 6vw 7vh;
  position: absolute;
  width: 100vw;
}
.slide.active {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.slide::before {
  background: var(--purple);
  content: "";
  height: 5px;
  left: 6vw;
  position: absolute;
  right: 6vw;
  top: 4.8vh;
}

.case-meta {
  align-items: center;
  color: var(--muted);
  display: flex;
  font-size: clamp(.62rem, .75vw, .88rem);
  font-weight: 800;
  justify-content: space-between;
  left: 6vw;
  letter-spacing: .08em;
  position: absolute;
  right: 6vw;
  text-transform: uppercase;
  top: 2vh;
}
.case-meta span:last-child { color: var(--purple); }
.page-number {
  bottom: 2.2vh;
  color: var(--purple);
  font-size: clamp(.62rem, .8vw, .9rem);
  font-weight: 900;
  letter-spacing: .1em;
  position: absolute;
  right: 6vw;
}

h1, h2, h3, p { margin: 0; }
h1, h2 {
  font-family: "Trebuchet MS", Tahoma, sans-serif;
  font-weight: 800;
  letter-spacing: -.045em;
}
h1 { font-size: clamp(3.6rem, 5.8vw, 6.7rem); line-height: .97; max-width: 12ch; }
h2 { font-size: clamp(3rem, 4.7vw, 5.5rem); line-height: 1; max-width: 16ch; }
h3 { font-size: clamp(1.7rem, 2.3vw, 2.8rem); line-height: 1.05; }
.eyebrow, .kicker {
  color: var(--purple);
  font-size: clamp(.9rem, 1.15vw, 1.35rem);
  font-weight: 900;
  letter-spacing: .11em;
  margin-bottom: 1.25rem;
  text-transform: uppercase;
}
.lead {
  color: var(--muted);
  font-size: clamp(1.5rem, 2.1vw, 2.5rem);
  line-height: 1.2;
  margin-top: 1.5rem;
  max-width: 31ch;
}
.bottom-line {
  border-left: 5px solid var(--violet);
  color: var(--purple);
  font-size: clamp(1.4rem, 1.9vw, 2.25rem);
  font-weight: 800;
  margin-top: 4vh;
  padding-left: 1.2rem;
}

.cover {
  background:
    radial-gradient(circle at 82% 16%, rgba(155,107,196,.22), transparent 22%),
    linear-gradient(115deg, #fff 0 61%, var(--lavender) 61% 100%);
  display: none;
  grid-template-columns: 1.35fr .65fr;
  gap: 6vw;
  padding-left: 6vw;
  place-items: center;
}
.cover.active { display: grid; }
.cover::before, .cover .case-meta { display: none; }
.cover-copy { padding-top: 1rem; }
.author-block { display: grid; gap: .4rem; margin-top: 4.5vh; }
.author-block strong { color: var(--purple); font-size: clamp(1.8rem, 2.7vw, 3.25rem); }
.author-block span { color: var(--muted); font-size: clamp(1.05rem, 1.4vw, 1.65rem); }
.cover-ticket {
  background: white;
  border: 1px solid var(--line);
  box-shadow: var(--shadow);
  display: grid;
  gap: 1.6rem;
  min-width: 26vw;
  padding: 2.2rem;
  position: relative;
}
.cover-ticket::before {
  background: repeating-linear-gradient(90deg, var(--purple) 0 18px, transparent 18px 28px);
  content: "";
  height: 6px;
  left: 0;
  position: absolute;
  right: 0;
  top: 0;
}
.cover-ticket img { height: 8.5rem; justify-self: center; width: 8.5rem; }
.ticket-line { border-top: 1px solid var(--line); display: grid; gap: .35rem; padding-top: 1rem; }
.ticket-line small { color: var(--muted); font-size: .8rem; font-weight: 900; letter-spacing: .1em; }
.ticket-line b { font-size: clamp(1.15rem, 1.6vw, 1.8rem); }
.ticket-status { align-items: center; background: var(--lavender); color: var(--purple); display: flex; font-weight: 900; gap: .7rem; padding: 1rem; }
.ticket-status i, .closing-status i { background: var(--purple); border-radius: 50%; display: block; height: .75rem; width: .75rem; }

.route h2 { max-width: 12ch; }
.route-track { display: grid; gap: 1.2rem; grid-template-columns: repeat(5, 1fr); margin-top: 9vh; position: relative; }
.route-track::before { background: var(--violet); content: ""; height: 3px; left: 8%; position: absolute; right: 8%; top: 1.05rem; }
.route-track div { padding-top: 3.2rem; position: relative; }
.route-track div::before { background: white; border: 4px solid var(--purple); border-radius: 50%; content: ""; height: 1.55rem; left: .2rem; position: absolute; top: .25rem; width: 1.55rem; z-index: 1; }
.route-track b { display: block; font-size: clamp(1.35rem, 1.8vw, 2.1rem); }
.route-track span { color: var(--muted); display: block; font-size: clamp(.95rem, 1.2vw, 1.4rem); line-height: 1.25; margin-top: .55rem; }

.company-layout { align-items: stretch; display: grid; gap: 4vw; grid-template-columns: .8fr 1.2fr; margin-top: 5vh; }
.company-logo { align-items: center; background: #080452; display: flex; justify-content: center; min-height: 43vh; position: relative; }
.company-logo::after { border: 1px solid rgba(255,255,255,.45); content: ""; inset: 1.1rem; position: absolute; }
.company-logo img { height: 15rem; width: 15rem; }
.fact-stack { display: grid; gap: 1rem; }
.fact-stack div { background: white; border-left: 5px solid var(--purple); box-shadow: 0 8px 25px rgba(91,42,134,.07); display: grid; gap: .55rem; padding: 1.3rem 1.6rem; }
.fact-stack small { color: var(--purple); font-size: .9rem; font-weight: 900; letter-spacing: .1em; }
.fact-stack b { font-size: clamp(1.45rem, 2vw, 2.35rem); }

.handoff { align-items: center; display: grid; margin-top: 7vh; }
.handoff.two { grid-template-columns: 1fr auto 1fr; gap: 2.2rem; }
.handoff article { background: white; border: 1px solid var(--line); box-shadow: var(--shadow); min-height: 31vh; padding: 2rem; }
.handoff article:last-child { border-top: 7px solid var(--purple); }
.handoff article:first-child { border-top: 7px solid var(--violet); }
.week-tag { color: var(--purple); display: block; font-size: .9rem; font-weight: 900; letter-spacing: .1em; margin-bottom: 1.3rem; }
.handoff p { color: var(--muted); font-size: clamp(1rem, 1.35vw, 1.55rem); line-height: 1.45; margin-top: 1rem; }
.handoff-arrow { color: var(--purple); font-size: 3rem; font-weight: 900; }

.service-path { display: grid; gap: 1.1rem; grid-template-columns: repeat(5, 1fr); margin-top: 8vh; }
.service-path div { background: white; border: 1px solid var(--line); min-height: 25vh; padding: 1.4rem; position: relative; }
.service-path div:not(:last-child)::after { color: var(--violet); content: "→"; font-size: 2rem; font-weight: 900; position: absolute; right: -1.5rem; top: 44%; z-index: 3; }
.service-path span { color: var(--violet); display: block; font-size: 1rem; font-weight: 900; margin-bottom: 2.7rem; }
.service-path b { display: block; font-size: clamp(1.25rem, 1.6vw, 1.9rem); line-height: 1.05; }
.service-path small { color: var(--muted); display: block; font-size: clamp(.8rem, 1vw, 1.15rem); line-height: 1.3; margin-top: .7rem; }

.problem { background: linear-gradient(110deg, var(--lavender), white); }
.problem-statement { align-items: end; display: grid; gap: 7vw; grid-template-columns: 1.25fr .75fr; margin-top: 9vh; }
.problem-statement h2 { font-size: clamp(3.3rem, 5.5vw, 6.2rem); }
.case-card { background: white; border: 1px solid var(--line); box-shadow: var(--shadow); display: grid; gap: 1.15rem; padding: 2rem; transform: rotate(1.5deg); }
.case-card small { color: var(--purple); font-weight: 900; letter-spacing: .1em; margin-bottom: .5rem; }
.case-card b { border-bottom: 1px solid var(--line); font-size: clamp(1.15rem, 1.55vw, 1.8rem); padding-bottom: .85rem; }

.alert-grid, .concept-grid, .translation-grid, .metric-grid { display: grid; gap: 1.3rem; grid-template-columns: repeat(2, 1fr); margin-top: 4.5vh; }
.alert-grid div { background: white; border-left: 6px solid var(--violet); min-height: 17vh; padding: 1.5rem; }
.alert-grid span, .translation-grid span { color: var(--purple); display: block; font-size: .8rem; font-weight: 900; letter-spacing: .11em; margin-bottom: 1rem; }
.alert-grid b { font-size: clamp(1.45rem, 2.15vw, 2.5rem); }

.impact-row { display: grid; gap: 2rem; grid-template-columns: repeat(3, 1fr); margin-top: 8vh; }
.impact-row div { border-top: 7px solid var(--purple); padding: 1.5rem .5rem; }
.impact-row strong { color: var(--violet); display: block; font-size: 1rem; letter-spacing: .1em; margin-bottom: 2rem; }
.impact-row b { display: block; font-size: clamp(1.65rem, 2.4vw, 2.8rem); }
.impact-row p { color: var(--muted); font-size: clamp(1rem, 1.25vw, 1.45rem); line-height: 1.3; margin-top: .8rem; }

.question { background: var(--purple); color: white; }
.question::before { background: var(--violet); }
.question .case-meta, .question .page-number { color: white; }
.question .case-meta span:last-child, .question .eyebrow { color: #eadcf5; }
.question-box { align-items: start; display: grid; gap: 1.5rem; grid-template-columns: auto 1fr; margin-top: 6vh; max-width: 88%; }
.question-box > span { color: var(--violet); font-family: Georgia, serif; font-size: clamp(6rem, 10vw, 11rem); line-height: .7; }
.question-box h2 { font-size: clamp(3.1rem, 5vw, 5.8rem); max-width: 17ch; }
.question-detail { border-top: 1px solid rgba(255,255,255,.35); color: #eadcf5; font-size: clamp(1.1rem, 1.55vw, 1.8rem); margin-left: 7rem; margin-top: 5vh; padding-top: 1.3rem; }

.objective-focus { display: grid; gap: 2rem; grid-template-columns: .55fr 1.45fr; margin-top: 7vh; }
.objective-focus span { color: var(--purple); font-family: "Trebuchet MS", Tahoma, sans-serif; font-size: clamp(4rem, 7vw, 8rem); font-weight: 900; letter-spacing: -.06em; line-height: .9; }
.objective-focus p { border-left: 2px solid var(--line); font-size: clamp(1.65rem, 2.4vw, 2.85rem); font-weight: 700; line-height: 1.25; padding-left: 2rem; }
.purpose-band { background: var(--lavender); color: var(--purple); font-size: clamp(1.35rem, 1.85vw, 2.15rem); font-weight: 900; margin-top: 6vh; padding: 1.3rem; text-align: center; }
.purpose-band i { color: var(--violet); font-style: normal; margin: 0 1.4rem; }

.objective-list { display: grid; gap: 1rem; grid-template-columns: repeat(3, 1fr); margin-top: 5vh; }
.objective-list article { background: white; border-bottom: 6px solid var(--purple); min-height: 30vh; padding: 1.5rem; }
.objective-list span { color: var(--violet); display: block; font-size: 1rem; font-weight: 900; margin-bottom: 2rem; }
.objective-list h3 { color: var(--purple); }
.objective-list p { color: var(--muted); font-size: clamp(.95rem, 1.2vw, 1.4rem); line-height: 1.35; margin-top: .8rem; }

.method-grid { display: grid; gap: 1rem; grid-template-columns: repeat(4, 1fr); margin-top: 7vh; }
.method-grid div { background: white; border: 1px solid var(--line); min-height: 29vh; padding: 1.35rem; }
.method-grid span { align-items: center; background: var(--lavender); border-radius: 50%; color: var(--purple); display: flex; font-size: .75rem; font-weight: 900; height: 3.6rem; justify-content: center; margin-bottom: 2.2rem; width: 3.6rem; }
.method-grid b { display: block; font-size: clamp(1.15rem, 1.5vw, 1.75rem); line-height: 1.1; }
.method-grid p { color: var(--muted); font-size: clamp(.85rem, 1vw, 1.2rem); line-height: 1.3; margin-top: .7rem; }

.diagram-slide h2 { max-width: 19ch; }
.wide-figure { background: white; border: 1px solid var(--line); box-shadow: 0 10px 28px rgba(91,42,134,.07); display: grid; margin: 3.5vh 0 0; padding: 1.1rem; place-items: center; }
.wide-figure img { height: 31vh; object-fit: contain; width: 100%; }
.wide-figure figcaption { color: var(--muted); font-size: clamp(.8rem, 1vw, 1.1rem); margin-top: .6rem; }
.swimlane-figure { margin-top: 2vh; }
.swimlane-figure img { height: 42vh; }

.finding-layout { align-items: center; display: grid; gap: 2vw; grid-template-columns: 1fr auto 1fr; margin-top: 9vh; }
.finding-layout h2 { font-size: clamp(2.8rem, 4.3vw, 5rem); }
.finding-layout h2:last-child { color: var(--purple); }
.finding-arrow { color: var(--violet); font-size: 4rem; font-weight: 900; }

.concept-grid div { background: white; border: 1px solid var(--line); min-height: 17vh; padding: 1.35rem 1.5rem; }
.concept-grid b { color: var(--purple); display: block; font-size: clamp(1.25rem, 1.7vw, 2rem); line-height: 1.1; }
.concept-grid p { color: var(--muted); font-size: clamp(.9rem, 1.1vw, 1.25rem); line-height: 1.3; margin-top: .65rem; }

.translation-grid { margin-top: 6vh; }
.translation-grid div { border-bottom: 2px solid var(--line); padding: 1.25rem 0 1.5rem; }
.translation-grid b { display: block; font-size: clamp(1.6rem, 2.2vw, 2.6rem); }

.legal-layout { display: grid; gap: 2rem; grid-template-columns: repeat(2, 1fr); margin-top: 5vh; }
.legal-layout article { background: white; border-top: 7px solid var(--purple); min-height: 26vh; padding: 1.7rem; }
.legal-layout span { color: var(--purple); display: block; font-size: .85rem; font-weight: 900; letter-spacing: .1em; margin-bottom: 1.5rem; }
.legal-layout b { display: block; font-size: clamp(1.5rem, 2vw, 2.35rem); }
.legal-layout p { color: var(--muted); font-size: clamp(.9rem, 1.12vw, 1.3rem); line-height: 1.4; margin-top: .8rem; }
.legal-note { color: var(--purple); font-size: clamp(1rem, 1.3vw, 1.5rem); font-weight: 800; margin-top: 3vh; text-align: center; }

.timeline { display: grid; gap: 1rem; grid-template-columns: repeat(4, 1fr); margin-top: 8vh; position: relative; }
.timeline::before { background: var(--line); content: ""; height: 4px; left: 7%; position: absolute; right: 7%; top: 2.3rem; }
.timeline article { padding-top: 5.5rem; position: relative; }
.timeline span { align-items: center; background: var(--purple); border: 8px solid var(--lavender); border-radius: 50%; color: white; display: flex; font-size: .85rem; font-weight: 900; height: 4.6rem; justify-content: center; left: 0; position: absolute; top: 0; width: 4.6rem; z-index: 2; }
.timeline b { display: block; font-size: clamp(1.4rem, 1.9vw, 2.2rem); }
.timeline p { color: var(--muted); font-size: clamp(.85rem, 1.05vw, 1.2rem); line-height: 1.35; margin-top: .6rem; }

.activity-split { display: grid; gap: 2rem; grid-template-columns: 1fr 1fr; margin-top: 5vh; }
.activity-split article { background: white; border: 1px solid var(--line); padding: 1.7rem; }
.activity-split article:last-child { background: var(--lavender); }
.activity-split span { color: var(--purple); display: block; font-size: .85rem; font-weight: 900; letter-spacing: .1em; margin-bottom: 1.3rem; }
.activity-split ul { list-style: none; margin: 0; padding: 0; }
.activity-split li { border-bottom: 1px solid var(--line); font-size: clamp(1.05rem, 1.4vw, 1.6rem); font-weight: 700; padding: .7rem 0; }

.proposal { background: linear-gradient(120deg, white, var(--lavender)); }
.proposal-grid { display: grid; gap: 1rem; grid-template-columns: repeat(3, 1fr); margin-top: 5vh; }
.proposal-grid div { background: white; border: 1px solid var(--line); min-height: 17vh; padding: 1.2rem; }
.proposal-grid span { color: var(--violet); display: block; font-size: .9rem; font-weight: 900; margin-bottom: 1.5rem; }
.proposal-grid b { display: block; font-size: clamp(1.25rem, 1.65vw, 1.9rem); line-height: 1.1; }

.state-figure { background: white; border: 1px solid var(--line); display: grid; margin: 4vh 0 0; padding: 1.4rem; place-items: center; }
.state-figure img { height: 22vh; object-fit: contain; width: 100%; }
.state-benefits { display: grid; gap: 1rem; grid-template-columns: repeat(3, 1fr); margin-top: 3vh; }
.state-benefits span { background: var(--lavender); color: var(--purple); font-size: clamp(.9rem, 1.15vw, 1.3rem); font-weight: 800; padding: 1rem; text-align: center; }

.form-preview { background: white; border: 1px solid var(--line); box-shadow: var(--shadow); margin-top: 5vh; padding: 1.2rem; }
.form-head { background: var(--purple); color: white; display: grid; gap: 1px; grid-template-columns: 1.3fr 1fr 1fr 1.3fr; }
.form-head b { border-right: 1px solid rgba(255,255,255,.3); font-size: clamp(.75rem, .95vw, 1.1rem); padding: 1rem; }
.form-body { display: grid; gap: 1px; grid-template-columns: 1fr 1.4fr 1fr; }
.form-body span { border: 1px solid var(--line); color: var(--muted); font-size: clamp(.9rem, 1.12vw, 1.3rem); min-height: 14vh; padding: 1rem; }
.form-foot { align-items: center; background: var(--paper-soft); display: flex; font-size: clamp(.8rem, 1vw, 1.15rem); gap: .65rem; padding: 1rem; }
.form-foot i { background: var(--line); height: 1px; margin: 0 1rem; width: 3rem; }

.metric-grid article { background: white; border: 1px solid var(--line); min-height: 17vh; padding: 1.25rem; }
.metric-grid span { color: var(--purple); display: block; font-size: .78rem; font-weight: 900; letter-spacing: .1em; margin-bottom: 1rem; }
.metric-grid b { display: block; font-size: clamp(1.25rem, 1.7vw, 2rem); }
.metric-grid p { color: var(--muted); font-size: clamp(.85rem, 1vw, 1.15rem); margin-top: .5rem; }

.comparison-layout { align-items: center; display: grid; gap: 4vw; grid-template-columns: .8fr 1.2fr; height: 100%; }
.comparison-layout figure { background: white; border: 1px solid var(--line); display: grid; margin: 0; padding: 1rem; place-items: center; }
.comparison-layout img { height: 66vh; object-fit: contain; width: 100%; }
.comparison-layout ul { display: flex; flex-wrap: wrap; gap: .65rem; list-style: none; margin: 3vh 0 0; padding: 0; }
.comparison-layout li { background: var(--lavender); color: var(--purple); font-size: clamp(.85rem, 1.05vw, 1.2rem); font-weight: 900; padding: .65rem .85rem; }

.conclusion-band { align-items: center; display: grid; gap: 1rem; grid-template-columns: 1fr auto 1fr auto 1fr; margin-top: 9vh; }
.conclusion-band span { background: var(--lavender); color: var(--purple); font-size: clamp(1.25rem, 1.8vw, 2.1rem); font-weight: 900; min-height: 14vh; padding: 1.2rem; text-align: center; }
.conclusion-band i { color: var(--violet); font-size: 2.5rem; font-style: normal; font-weight: 900; }
.four-words { display: grid; gap: 1rem; grid-template-columns: repeat(4, 1fr); margin-top: 9vh; }
.four-words span { border-bottom: 7px solid var(--purple); font-size: clamp(1.4rem, 2vw, 2.4rem); font-weight: 900; padding: 1.3rem .4rem; text-align: center; text-transform: uppercase; }
.result-equation { align-items: center; display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 9vh; }
.result-equation span { background: var(--lavender); color: var(--purple); font-size: clamp(1.15rem, 1.55vw, 1.8rem); font-weight: 900; padding: 1rem 1.2rem; }
.result-equation i { color: var(--violet); font-size: 2rem; font-style: normal; font-weight: 900; }
.result-equation b { color: var(--purple); display: block; font-size: clamp(2.3rem, 3.4vw, 4rem); margin-top: 2vh; width: 100%; }

.recommend-grid { display: grid; gap: 1rem; grid-template-columns: repeat(2, 1fr); margin-top: 4vh; }
.recommend-grid article { background: white; border-left: 6px solid var(--purple); min-height: 16vh; padding: 1.25rem; }
.recommend-grid span { color: var(--violet); display: block; font-size: .8rem; font-weight: 900; letter-spacing: .1em; margin-bottom: .8rem; }
.recommend-grid b { display: block; font-size: clamp(1.15rem, 1.55vw, 1.8rem); line-height: 1.2; }

.closing { background: linear-gradient(115deg, white 0 66%, var(--lavender) 66%); }
.closing-copy { margin-top: 9vh; max-width: 67%; }
.closing-copy h2 { font-size: clamp(3.6rem, 5.8vw, 6.6rem); max-width: 14ch; }
.closing-copy p { color: var(--purple); font-size: clamp(1.5rem, 2vw, 2.35rem); font-weight: 900; margin-top: 5vh; }
.closing-copy span { color: var(--muted); display: block; font-size: clamp(1rem, 1.3vw, 1.5rem); margin-top: .5rem; }
.closing-status { background: white; border: 1px solid var(--line); bottom: 10vh; box-shadow: var(--shadow); display: grid; gap: .5rem; padding: 1.5rem; position: absolute; right: 7vw; width: 22vw; }
.closing-status i { margin-bottom: .3rem; }
.closing-status b { color: var(--purple); font-size: clamp(1.05rem, 1.4vw, 1.6rem); letter-spacing: .08em; }
.closing-status small { color: var(--muted); font-size: clamp(.75rem, .9vw, 1rem); }

.controls { bottom: 1.3rem; display: flex; gap: .6rem; left: 2rem; position: fixed; z-index: 20; }
.controls button { background: white; border: 1px solid var(--line); color: var(--purple); cursor: pointer; font-weight: 900; height: 2.4rem; width: 2.8rem; }
.controls button:hover, .controls button:focus-visible { background: var(--purple); color: white; outline: 3px solid rgba(155,107,196,.35); outline-offset: 2px; }
.progress { background: var(--lavender); bottom: 0; height: 7px; left: 0; position: fixed; right: 0; z-index: 30; }
.progress span { background: var(--purple); display: block; height: 100%; transition: width .25s ease; width: 0; }
.notes-panel { background: rgba(36,24,45,.97); bottom: 4rem; color: white; display: none; font-size: 1.15rem; line-height: 1.45; max-width: 48rem; padding: 1.4rem; position: fixed; right: 2rem; z-index: 40; }
.notes-panel.show { display: block; }
.notes-panel b { color: #d9b8f2; display: block; margin-bottom: .5rem; }

@media screen and (max-width: 900px) {
  .slide { padding: 7vh 5vw; }
  .slide::before, .case-meta { left: 5vw; right: 5vw; }
  h1 { font-size: clamp(2.3rem, 8vw, 4rem); }
  h2 { font-size: clamp(2rem, 6.2vw, 3.4rem); }
  .cover { grid-template-columns: 1fr; padding: 6vh 6vw; }
  .cover-ticket { display: none; }
  .route-track, .service-path, .method-grid, .timeline, .four-words { grid-template-columns: repeat(2, 1fr); }
  .route-track::before, .timeline::before { display: none; }
  .route-track div, .timeline article { padding-top: 1.5rem; }
  .route-track div::before, .timeline span { display: none; }
  .company-layout, .problem-statement, .objective-focus, .comparison-layout { grid-template-columns: 1fr; }
  .company-logo { display: none; }
  .handoff p, .service-path small, .objective-list p { font-size: .8rem; }
  .service-path { gap: .4rem; }
  .service-path div { min-height: 7rem; padding: .6rem; }
  .service-path div:not(:last-child)::after { display: none; }
  .objective-list, .impact-row, .proposal-grid, .state-benefits { gap: .6rem; }
  .objective-list article, .impact-row div { min-height: auto; padding: .8rem; }
  .wide-figure img { height: 28vh; }
  .comparison-layout figure { display: none; }
  .closing-copy { max-width: 88%; }
  .closing-status { display: none; }
}

@media (prefers-reduced-motion: reduce) {
  .progress span { transition: none; }
}

@media print {
  @page { size: 16in 9in; margin: 0; }
  html, body { height: auto; overflow: visible; width: auto; }
  body { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
  .deck { height: auto; width: auto; }
  .slide, .slide.active, .cover, .cover.active {
    break-after: page;
    display: flex;
    flex-direction: column;
    height: 9in;
    inset: auto;
    justify-content: center;
    overflow: hidden;
    page-break-after: always;
    position: relative;
    width: 16in;
  }
  .cover, .cover.active { display: grid; }
  .controls, .notes-panel, .progress { display: none !important; }
}
"""


JS = r"""
(() => {
  const slides = Array.from(document.querySelectorAll('.slide'));
  const progress = document.querySelector('.progress span');
  const notes = document.querySelector('.notes-panel');
  const requested = Number(new URLSearchParams(location.search).get('slide'));
  let index = Number.isInteger(requested) && requested > 0
    ? Math.min(requested - 1, slides.length - 1)
    : 0;

  function render(updateUrl = true) {
    slides.forEach((item, position) => item.classList.toggle('active', position === index));
    progress.style.width = `${((index + 1) / slides.length) * 100}%`;
    notes.classList.remove('show');
    notes.innerHTML = `<b>Notas del expositor</b>${slides[index].dataset.notes}`;
    document.title = `Amaal Alrifaai · Diapositiva ${index + 1}`;
    if (updateUrl) history.replaceState(null, '', `?slide=${index + 1}`);
  }

  function next() { if (index < slides.length - 1) { index += 1; render(); } }
  function prev() { if (index > 0) { index -= 1; render(); } }

  document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowRight' || event.key === 'PageDown' || event.key === ' ') next();
    if (event.key === 'ArrowLeft' || event.key === 'PageUp') prev();
    if (event.key === 'Home') { index = 0; render(); }
    if (event.key === 'End') { index = slides.length - 1; render(); }
    if (event.key.toLowerCase() === 's') notes.classList.toggle('show');
    if (event.key.toLowerCase() === 'f') {
      if (!document.fullscreenElement) document.documentElement.requestFullscreen?.();
      else document.exitFullscreen?.();
    }
    if (event.key === 'Escape') notes.classList.remove('show');
  });

  document.querySelector('[data-action="prev"]').addEventListener('click', prev);
  document.querySelector('[data-action="next"]').addEventListener('click', next);
  render(false);
})();
"""


def construir_html() -> str:
    secciones = []
    total = len(DIAPOSITIVAS)
    for numero, diapositiva in enumerate(DIAPOSITIVAS, start=1):
        notas = e(diapositiva.notas).replace("\n", "<br>")
        fase_numero, fase_nombre = FASES[diapositiva.fase - 1]
        secciones.append(
            dedent(
                f"""
                <section class="slide {e(diapositiva.clase)}" data-notes="{notas}" aria-label="Diapositiva {numero} de {total}">
                  <div class="case-meta"><span>IDETEL · CONTROL DE SOLICITUDES</span><span>FASE {fase_numero} · {e(fase_nombre)}</span></div>
                  {diapositiva.cuerpo}
                  <div class="page-number">{numero:02d} / {total:02d}</div>
                </section>
                """
            ).strip()
        )

    return dedent(
        f"""
        <!doctype html>
        <html lang="es">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <meta name="theme-color" content="#fcfbfe">
          <title>Amaal Alrifaai · Control administrativo de solicitudes</title>
          <style>{CSS}</style>
        </head>
        <body>
          <main class="deck">{"".join(secciones)}</main>
          <nav class="controls" aria-label="Controles de diapositivas">
            <button type="button" data-action="prev" aria-label="Diapositiva anterior">←</button>
            <button type="button" data-action="next" aria-label="Diapositiva siguiente">→</button>
          </nav>
          <div class="notes-panel" aria-live="polite"></div>
          <div class="progress" aria-hidden="true"><span></span></div>
          <script>{JS}</script>
        </body>
        </html>
        """
    ).strip() + "\n"


def main() -> None:
    SALIDA.write_text(construir_html(), encoding="utf-8")
    print(f"Presentación generada: {SALIDA}")
    print(f"Diapositivas: {len(DIAPOSITIVAS)}")


if __name__ == "__main__":
    main()
