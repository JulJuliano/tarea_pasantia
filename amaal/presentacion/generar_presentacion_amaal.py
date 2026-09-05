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
    capitulo: int
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


def slide(capitulo: int, clase: str, cuerpo: str, notas: str) -> Diapositiva:
    return Diapositiva(
        capitulo=capitulo,
        clase=clase,
        cuerpo=dedent(cuerpo).strip(),
        notas=dedent(notas).strip(),
    )


LOGO = imagen_embebida("logo.jpg")
ISHIKAWA = imagen_embebida("ishikawa_amaal_solicitudes.png")
SWIMLANE = imagen_embebida("04_swimlane_gestion_solicitudes.png")
COMPARACION = imagen_embebida("11_comparacion_as_is_to_be.png")


DIAPOSITIVAS: list[Diapositiva] = [
    slide(
        1,
        "cover",
        f"""
        <div class="cover-copy">
          <p class="kicker">DEFENSA DE PASANTÍAS PROFESIONALES</p>
          <h1 class="official-title">Evaluación del control administrativo aplicado a la gestión de solicitudes de servicios de telecomunicaciones en la empresa Ingeniería de Telecomunicaciones, C.A.</h1>
          <div class="author-block">
            <strong>Amaal Alrifaai Alrifaaie</strong>
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
        Saludar al jurado, a las tutoras y a las personas presentes. Presentarse como Amaal
        Alrifaai Alrifaaie, estudiante de Administración del IUTECP, y leer el título oficial
        del informe. Indicar que las pasantías se realizaron en IDETEL.
        """,
    ),
    slide(
        1,
        "route",
        """
        <p class="eyebrow">ESTRUCTURA DE LA PRESENTACIÓN</p>
        <h2>Cinco capítulos, una misma secuencia.</h2>
        <div class="route-track">
          <div><small>CAPÍTULO I</small><b>Realidad Organizacional</b></div>
          <div><small>CAPÍTULO II</small><b>Diagnóstico Situacional</b></div>
          <div><small>CAPÍTULO III</small><b>Marco Teórico</b></div>
          <div><small>CAPÍTULO IV</small><b>Actividades Realizadas</b></div>
          <div><small>CAPÍTULO V</small><b>Conclusiones y Recomendaciones</b></div>
        </div>
        """,
        """
        Explicar que la exposición seguirá la misma secuencia de los cinco capítulos del informe:
        realidad organizacional, diagnóstico situacional, marco teórico, actividades realizadas
        y conclusiones y recomendaciones.
        """,
    ),
    slide(
        1,
        "company",
        f"""
        <p class="eyebrow">CAPÍTULO I · REALIDAD ORGANIZACIONAL</p>
        <h2>Empresa y área de pasantía.</h2>
        <div class="company-layout">
          <div class="company-logo"><img src="{LOGO}" alt="Logotipo de IDETEL"></div>
          <div class="fact-stack">
            <div><small>EMPRESA</small><b>Ingeniería de Telecomunicaciones, C.A.</b></div>
            <div><small>SECTOR</small><b>Telecomunicaciones y automatización</b></div>
            <div><small>SEDE</small><b>El Tigre, Anzoátegui</b></div>
            <div><small>ÁREA DE PASANTÍA</small><b>Atención al Cliente <i>Sem. 1–3</i> → Administración <i>Sem. 4–10</i></b></div>
          </div>
        </div>
        """,
        """
        Presentar a IDETEL como una empresa ubicada en El Tigre con más de cuatro décadas de
        experiencia en telecomunicaciones y automatización. Explicar la rotación: Atención al
        Cliente durante las semanas 1 a 3 y Administración desde la semana 4 hasta la 10.
        Mencionar recepción, pagos, facturación, documentos, seguimiento y reportes.
        """,
    ),
    slide(
        1,
        "journey",
        """
        <p class="eyebrow">CAPÍTULO I · REALIDAD ORGANIZACIONAL</p>
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
        Explicar que una solicitud comienza en Atención al Cliente, puede pasar por Administración
        y, según el caso, por el NOC o el personal técnico antes de cerrarse. Destacar que el proceso
        depende de que la información pase claramente entre áreas y conserve su continuidad.
        """,
    ),
    slide(
        2,
        "problem problem-compact",
        """
        <p class="eyebrow">CAPÍTULO II · SITUACIÓN PROBLEMÁTICA</p>
        <h2>No existía un procedimiento único de seguimiento.</h2>
        <div class="problem-layout">
          <div class="case-card">
            <small>PREGUNTAS DE CONTROL</small>
            <b>¿Quién lo tiene?</b>
            <b>¿En qué estado está?</b>
            <b>¿Cuándo debe cerrar?</b>
          </div>
          <div class="signal-list">
            <div><span>01</span><b>Formatos no uniformes</b></div>
            <div><span>02</span><b>Estatus distribuido</b></div>
            <div><span>03</span><b>Sin tiempos de referencia</b></div>
            <div><span>04</span><b>Comunicación fragmentada</b></div>
          </div>
        </div>
        """,
        """
        Explicar que la empresa atendía los casos, pero no contaba con un procedimiento único y
        formalizado desde la entrada hasta el cierre. Describir las cuatro manifestaciones: formatos
        no uniformes, estatus distribuido, falta de tiempos de referencia y comunicación fragmentada.
        Aclarar que esto describe una necesidad del proceso, no un incumplimiento del personal.
        """,
    ),
    slide(
        2,
        "effects effects-question",
        """
        <p class="eyebrow">CAPÍTULO II · DIAGNÓSTICO SITUACIONAL</p>
        <h2>Efectos administrativos.</h2>
        <div class="impact-row">
          <div><strong>01</strong><b>Reprocesos</b></div>
          <div><strong>02</strong><b>Mayor tiempo de respuesta</b></div>
          <div><strong>03</strong><b>Menor precisión</b></div>
        </div>
        <div class="question-strip"><b>INTERROGANTE</b><p>¿Cómo puede evaluarse el control administrativo aplicado a la gestión de solicitudes de servicios de telecomunicaciones en IDETEL para identificar sus principales debilidades y formular mejoras procedimentales que fortalezcan la trazabilidad y el seguimiento de los casos?</p></div>
        """,
        """
        Relacionar las manifestaciones con los reprocesos, la demora y la dificultad para informar con
        precisión al suscriptor. Leer la interrogante de forma pausada y explicar que vincula evaluar
        el control, identificar debilidades y formular mejoras para la trazabilidad y el seguimiento.
        """,
    ),
    slide(
        2,
        "objectives objectives-combined",
        """
        <p class="eyebrow">CAPÍTULO II · OBJETIVOS</p>
        <div class="objective-summary">
          <span>OBJETIVO GENERAL</span>
          <b>EVALUAR</b>
          <p>el control administrativo para identificar debilidades y formular mejoras procedimentales.</p>
        </div>
        <div class="objective-list">
          <article><span>01</span><h3>Diagnosticar</h3><p>recorrido actual</p></article>
          <article><span>02</span><h3>Identificar</h3><p>deficiencias y causas</p></article>
          <article><span>03</span><h3>Formular</h3><p>mejoras procedimentales</p></article>
        </div>
        <p class="objective-sequence">Diagnosticar <i>→</i> Identificar <i>→</i> Formular</p>
        """,
        """
        Enfatizar el verbo evaluar. Luego presentar la secuencia de los tres objetivos específicos:
        diagnosticar el recorrido actual, identificar las deficiencias y sus causas, y formular mejoras
        mediante flujo, formatos, responsables e indicadores. Recordar: conocer, identificar y mejorar.
        """,
    ),
    slide(
        2,
        "method",
        """
        <p class="eyebrow">CAPÍTULO II · TÉCNICAS DE DIAGNÓSTICO</p>
        <h2>La situación se observó desde cuatro fuentes.</h2>
        <div class="method-grid">
          <div><span>OBS</span><b>Observación directa</b><p>recorrido real de solicitudes</p></div>
          <div><span>DOC</span><b>Revisión de registros</b><p>soportes y casos disponibles</p></div>
          <div><span>ENT</span><b>Entrevistas</b><p>personal de las áreas relacionadas</p></div>
          <div><span>ISH</span><b>Ishikawa</b><p>organización de las causas</p></div>
        </div>
        """,
        """
        Mencionar brevemente observación directa, revisión de registros, entrevistas al personal e
        Ishikawa. Explicar que la combinación permitió comparar el recorrido cotidiano, los soportes
        disponibles y la experiencia de quienes participan en el proceso.
        """,
    ),
    slide(
        2,
        "diagram-slide ishikawa-slide",
        f"""
        <p class="eyebrow">CAPÍTULO II · DIAGRAMA DE CAUSA–EFECTO</p>
        <h2>Las causas se agruparon en cuatro dimensiones.</h2>
        <figure class="wide-figure ishikawa-figure">
          <img src="{ISHIKAWA}" alt="Diagrama de Ishikawa del control de solicitudes">
          <figcaption>Procedimiento · comunicación · registro · seguimiento</figcaption>
        </figure>
        <p class="finding-line">Hallazgo central: el problema no era recibir el caso, sino mantener visible su continuidad.</p>
        """,
        """
        Explicar que el Ishikawa organizó causas relacionadas en procedimiento, comunicación, registro
        y seguimiento. Dar un ejemplo breve por dimensión. Cerrar con el hallazgo principal: el problema
        no era recibir la solicitud, sino mantener visible su continuidad hasta el cierre.
        """,
    ),
    slide(
        3,
        "theory",
        """
        <p class="eyebrow">CAPÍTULO III · MARCO TEÓRICO</p>
        <h2>Cuatro conceptos disciplinares.</h2>
        <div class="concept-grid">
          <div><b>Control administrativo</b><p>Verificar el proceso y corregir desviaciones.</p></div>
          <div><b>Gestión de solicitudes</b><p>Recibir, registrar, procesar, seguir y cerrar.</p></div>
          <div><b>Trazabilidad administrativa</b><p>Poder reconstruir el recorrido de un caso.</p></div>
          <div><b>Estandarización de procedimientos</b><p>Aplicar criterios y formatos comunes.</p></div>
        </div>
        """,
        """
        Explicar solamente los cuatro conceptos más relacionados con el problema. Controlar es verificar
        y corregir; gestionar es completar el ciclo de la solicitud; la trazabilidad permite reconstruir
        su recorrido; y la estandarización establece criterios comunes. Relacionarlos oralmente con la propuesta.
        """,
    ),
    slide(
        3,
        "legal",
        """
        <p class="eyebrow">CAPÍTULO III · MARCO TEÓRICO</p>
        <h2>Bases legales.</h2>
        <div class="legal-layout">
          <article><span>CONSTITUCIÓN</span><b>Artículo 112</b><p>Fundamento general de la actividad económica privada dentro del ordenamiento jurídico.</p></article>
          <article><span>CÓDIGO DE COMERCIO</span><b>Artículo 32</b><p>Principio de orden y claridad de los registros que acompañan las operaciones mercantiles.</p></article>
        </div>
        <p class="legal-note">Estas normas aportan un fundamento general; no regulan directamente el flujo de solicitudes estudiado.</p>
        """,
        """
        Mencionar el artículo 112 de la Constitución como marco general de la actividad empresarial y el
        artículo 32 del Código de Comercio como referencia para el orden y la claridad de los registros.
        Aclarar que ninguno regula directamente el flujo de solicitudes estudiado.
        """,
    ),
    slide(
        4,
        "activities",
        """
        <p class="eyebrow">CAPÍTULO IV · ACTIVIDADES REALIZADAS</p>
        <h2>Cuatro actividades principales.</h2>
        <div class="activity-grid">
          <article><span>SEM. 1–3</span><b>Observar el recorrido</b><p>Atención al Cliente y Administración</p></article>
          <article><span>SEM. 4</span><b>Revisar y entrevistar</b><p>Registros, personal e identificación de fallas</p></article>
          <article><span>SEM. 5</span><b>Elaborar el Ishikawa</b><p>Organización de causas relacionadas</p></article>
          <article><span>SEM. 7–9</span><b>Diseñar y validar</b><p>Flujo, formatos, responsables e indicadores</p></article>
        </div>
        """,
        """
        Resumir las diez semanas en cuatro actividades: observar el recorrido; revisar registros y
        entrevistar al personal; elaborar el Ishikawa; y diseñar y validar las mejoras. Mencionar que
        también se apoyaron pagos, facturación, documentos, casos y reportes administrativos.
        """,
    ),
    slide(
        4,
        "proposal",
        """
        <p class="eyebrow">CAPÍTULO IV · ACTIVIDADES REALIZADAS</p>
        <p class="section-label">RESULTADO PRINCIPAL · PROPUESTA DE MEJORA</p>
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
        Presentar la propuesta como el principal resultado del Capítulo IV. Explicar sus seis componentes:
        flujo estandarizado, responsables, formatos, estados, tiempos e indicadores. Aclarar que funcionan
        de manera integrada y que la propuesta busca simplificar el control, no aumentar la burocracia.
        """,
    ),
    slide(
        4,
        "diagram-slide swimlane flow-states",
        f"""
        <p class="eyebrow">CAPÍTULO IV · FLUJO ESTANDARIZADO</p>
        <h2>Cada transferencia deja un responsable visible.</h2>
        <figure class="wide-figure swimlane-figure">
          <img src="{SWIMLANE}" alt="Swimlane propuesto para la gestión de solicitudes">
        </figure>
        <div class="state-flow" aria-label="Estados de una solicitud">
          <span>Recibida</span><i>→</i><span>Registrada</span><i>→</i><span>Asignada</span><i>→</i><span>En atención</span><i>→</i><span>Resuelta</span><i>→</i><span>Cerrada</span>
        </div>
        <p class="resolution-note">Resuelta ≠ Cerrada</p>
        """,
        """
        Explicar el swimlane por áreas. Atención al Cliente recibe, registra y comunica; Administración
        revisa y actualiza; NOC o Técnicos atienden cuando corresponde. Recorrer los seis estados y
        enfatizar que resuelta no equivale a cerrada: el cierre exige registrar y confirmar el resultado.
        """,
    ),
    slide(
        4,
        "formats control-tools",
        """
        <p class="eyebrow">CAPÍTULO IV · REGISTRO Y MEDICIÓN</p>
        <h2>Información común para controlar el proceso.</h2>
        <div class="tools-layout">
          <article class="format-card">
            <span>FORMATO COMÚN</span>
            <div class="field-cloud"><b>ID</b><b>Tipo</b><b>Fecha</b><b>Responsable</b><b>Estatus</b><b>Observaciones</b></div>
          </article>
          <article class="indicator-card">
            <span>INDICADORES</span>
            <ul><li>Tiempo promedio</li><li>Casos pendientes</li><li>Cierres en plazo</li><li>Devoluciones</li></ul>
          </article>
        </div>
        <p class="bottom-line">Primero organizar el proceso; después medirlo y digitalizarlo.</p>
        """,
        """
        Explicar que cada caso conservaría ID, tipo, fecha, responsable, estatus y observaciones. Presentar
        los cuatro indicadores sencillos: tiempo promedio, pendientes, cierres en plazo y devoluciones.
        Su función es detectar retrasos, no sancionar. Primero se organiza y prueba; luego se digitaliza.
        """,
    ),
    slide(
        4,
        "comparison",
        f"""
        <p class="eyebrow">CAPÍTULO IV · COMPARACIÓN DEL PROCESO</p>
        <div class="comparison-layout">
          <div>
            <h2>De información dispersa a control verificable.</h2>
            <div class="comparison-labels"><span><small>ANTES · AS–IS</small><b>Información dispersa</b></span><i>→</i><span><small>PROPUESTA · TO–BE</small><b>Control verificable</b></span></div>
          </div>
          <figure><img src="{COMPARACION}" alt="Comparación del control actual y propuesto"></figure>
        </div>
        """,
        """
        Sintetizar el cambio esperado: de registros no unificados, comunicación fragmentada y estatus
        distribuido a formatos uniformes, flujo común, responsables visibles, estados verificables e
        indicadores. Recordar que se trata de una propuesta formulada, no de resultados ya implementados.
        """,
    ),
    slide(
        5,
        "conclusions conclusions-combined",
        """
        <p class="eyebrow">CAPÍTULO V · CONCLUSIONES</p>
        <h2>Tres objetivos, tres resultados.</h2>
        <div class="conclusion-grid">
          <article><span>1 · DIAGNÓSTICO</span><p>El recorrido existía, pero no estaba formalizado como un solo proceso.</p></article>
          <article><span>2 · DEFICIENCIAS</span><p>Formatos, estatus, tiempos y comunicación afectaban la trazabilidad.</p></article>
          <article><span>3 · APORTE</span><p>Flujo + responsables + formatos + indicadores = mayor trazabilidad.</p></article>
        </div>
        <p class="learning-line"><b>Aprendizaje:</b> control, organización de procesos, gestión documental y atención al usuario.</p>
        """,
        """
        Relacionar cada conclusión con un objetivo: el recorrido existe, pero no como un proceso integral;
        las cuatro debilidades afectan la trazabilidad; y la propuesta combina flujo, responsables, formatos
        e indicadores. Mencionar los aprendizajes administrativos obtenidos durante la experiencia.
        """,
    ),
    slide(
        5,
        "recommendations",
        """
        <p class="eyebrow">CAPÍTULO V · RECOMENDACIONES</p>
        <h2>Implementar primero; digitalizar después.</h2>
        <div class="recommend-layout">
          <article class="idetel-recommendation"><span>A IDETEL</span><b>Probar flujo <i>→</i> uniformar <i>→</i> medir <i>→</i> evaluar digitalización</b></article>
          <div class="secondary-recommendations">
            <article><span>AL IUTECP</span><b>Fortalecer el acompañamiento académico.</b></article>
            <article><span>A FUTUROS PASANTES</span><b>Registrar actividades y conservar evidencias.</b></article>
          </div>
        </div>
        """,
        """
        Recomendar a IDETEL una implementación gradual: probar el flujo, uniformar los formatos, definir
        quién actualiza, medir periódicamente y solo entonces evaluar una herramienta centralizada. Al
        IUTECP, fortalecer el acompañamiento; a futuros pasantes, registrar actividades y evidencias.
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
        <div class="closing-status"><i></i><b>CASO PRESENTADO</b><small>Amaal Alrifaai Alrifaaie · Administración</small></div>
        """,
        """
        Explicar que no basta con recibir o resolver técnicamente un caso: también debe conocerse quién
        lo atendió, su estado, su tiempo y su cierre. Agradecer al IUTECP, IDETEL, tutores y personal.
        Dar las gracias por la atención y quedar disponible para preguntas.
        """,
    ),
]


CAPITULOS = (
    ("I", "Realidad Organizacional"),
    ("II", "Diagnóstico Situacional"),
    ("III", "Marco Teórico"),
    ("IV", "Actividades Realizadas"),
    ("V", "Conclusiones y Recomendaciones"),
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
.official-title { font-size: clamp(2.15rem, 3.05vw, 3.65rem); line-height: 1.03; max-width: 24ch; }
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
.route-track small { color: var(--violet); display: block; font-size: clamp(.66rem, .8vw, .9rem); font-weight: 900; letter-spacing: .08em; margin-bottom: .6rem; }
.route-track b { display: block; font-size: clamp(1.05rem, 1.4vw, 1.6rem); line-height: 1.15; }
.route-track span { color: var(--muted); display: block; font-size: clamp(.95rem, 1.2vw, 1.4rem); line-height: 1.25; margin-top: .55rem; }

.company-layout { align-items: stretch; display: grid; gap: 4vw; grid-template-columns: .8fr 1.2fr; margin-top: 5vh; }
.company-logo { align-items: center; background: #080452; display: flex; justify-content: center; min-height: 43vh; position: relative; }
.company-logo::after { border: 1px solid rgba(255,255,255,.45); content: ""; inset: 1.1rem; position: absolute; }
.company-logo img { height: 15rem; width: 15rem; }
.fact-stack { display: grid; gap: 1rem; }
.fact-stack div { background: white; border-left: 5px solid var(--purple); box-shadow: 0 8px 25px rgba(91,42,134,.07); display: grid; gap: .55rem; padding: 1.3rem 1.6rem; }
.fact-stack small { color: var(--purple); font-size: .9rem; font-weight: 900; letter-spacing: .1em; }
.fact-stack b { font-size: clamp(1.45rem, 2vw, 2.35rem); }
.company .company-layout { margin-top: 3vh; }
.company .company-logo { min-height: 44vh; }
.company .fact-stack { gap: .7rem; }
.company .fact-stack div { gap: .3rem; padding: .85rem 1.2rem; }
.company .fact-stack b { font-size: clamp(1.05rem, 1.45vw, 1.65rem); line-height: 1.18; }
.company .fact-stack i { color: var(--violet); font-size: .72em; font-style: normal; white-space: nowrap; }

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
.problem-compact h2 { font-size: clamp(2.65rem, 4.2vw, 4.8rem); max-width: 22ch; }
.problem-layout { align-items: stretch; display: grid; gap: 2.5vw; grid-template-columns: .8fr 1.2fr; margin-top: 4vh; }
.problem-layout .case-card { gap: .7rem; padding: 1.35rem; transform: rotate(-1deg); }
.problem-layout .case-card small { margin-bottom: .15rem; }
.problem-layout .case-card b { font-size: clamp(1rem, 1.3vw, 1.5rem); padding-bottom: .55rem; }
.signal-list { display: grid; gap: .65rem; grid-template-columns: repeat(2, 1fr); }
.signal-list div { align-items: center; background: white; border-left: 5px solid var(--violet); display: grid; gap: .35rem; padding: .85rem 1rem; }
.signal-list span { color: var(--violet); font-size: .75rem; font-weight: 900; }
.signal-list b { font-size: clamp(.95rem, 1.25vw, 1.45rem); line-height: 1.15; }

.alert-grid, .concept-grid, .translation-grid, .metric-grid { display: grid; gap: 1.3rem; grid-template-columns: repeat(2, 1fr); margin-top: 4.5vh; }
.alert-grid div { background: white; border-left: 6px solid var(--violet); min-height: 17vh; padding: 1.5rem; }
.alert-grid span, .translation-grid span { color: var(--purple); display: block; font-size: .8rem; font-weight: 900; letter-spacing: .11em; margin-bottom: 1rem; }
.alert-grid b { font-size: clamp(1.45rem, 2.15vw, 2.5rem); }

.impact-row { display: grid; gap: 2rem; grid-template-columns: repeat(3, 1fr); margin-top: 8vh; }
.impact-row div { border-top: 7px solid var(--purple); padding: 1.5rem .5rem; }
.impact-row strong { color: var(--violet); display: block; font-size: 1rem; letter-spacing: .1em; margin-bottom: 2rem; }
.impact-row b { display: block; font-size: clamp(1.65rem, 2.4vw, 2.8rem); }
.impact-row p { color: var(--muted); font-size: clamp(1rem, 1.25vw, 1.45rem); line-height: 1.3; margin-top: .8rem; }
.effects-question .impact-row { margin-top: 3vh; }
.effects-question .impact-row div { min-height: 13vh; padding: 1rem .5rem; }
.effects-question .impact-row strong { margin-bottom: .7rem; }
.effects-question .impact-row b { font-size: clamp(1.25rem, 1.85vw, 2.15rem); }
.question-strip { background: var(--purple); color: white; display: grid; gap: .65rem; margin-top: 3.5vh; padding: 1.15rem 1.4rem; }
.question-strip > b { color: #e7d3f5; font-size: .75rem; letter-spacing: .12em; }
.question-strip p { font-size: clamp(.9rem, 1.14vw, 1.3rem); line-height: 1.4; }

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
.objective-summary { align-items: center; display: grid; gap: .7rem 1.5rem; grid-template-columns: auto 1fr; }
.objective-summary > span { color: var(--purple); font-size: .8rem; font-weight: 900; grid-column: 1 / -1; letter-spacing: .11em; }
.objective-summary > b { color: var(--purple); font-family: "Trebuchet MS", Tahoma, sans-serif; font-size: clamp(3.2rem, 5vw, 5.8rem); letter-spacing: -.05em; line-height: .85; }
.objective-summary p { border-left: 2px solid var(--line); font-size: clamp(1.2rem, 1.65vw, 1.9rem); font-weight: 700; line-height: 1.25; max-width: 36ch; padding-left: 1.4rem; }
.objectives-combined .objective-list { margin-top: 3vh; }
.objectives-combined .objective-list article { min-height: 19vh; padding: 1rem 1.25rem; }
.objectives-combined .objective-list span { margin-bottom: .65rem; }
.objectives-combined .objective-list h3 { font-size: clamp(1.35rem, 1.8vw, 2.1rem); }
.objectives-combined .objective-list p { margin-top: .35rem; }
.objective-sequence { color: var(--purple); font-size: clamp(1rem, 1.3vw, 1.5rem); font-weight: 900; margin-top: 2vh; text-align: center; }
.objective-sequence i { color: var(--violet); font-style: normal; margin: 0 .8rem; }

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
.ishikawa-slide h2 { font-size: clamp(2.2rem, 3.35vw, 3.85rem); }
.ishikawa-figure { margin-top: 1.5vh; padding: .65rem; }
.ishikawa-figure img { height: 43vh; }
.ishikawa-figure figcaption { margin-top: .3rem; }
.finding-line { background: var(--purple); color: white; font-size: clamp(1rem, 1.35vw, 1.55rem); font-weight: 900; margin-top: 1.5vh; padding: .9rem 1.2rem; text-align: center; }

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

.activity-grid { display: grid; gap: 1rem; grid-template-columns: repeat(2, 1fr); margin-top: 4vh; }
.activity-grid article { background: white; border: 1px solid var(--line); border-left: 6px solid var(--purple); min-height: 16vh; padding: 1.2rem 1.4rem; }
.activity-grid span { color: var(--violet); display: block; font-size: .78rem; font-weight: 900; letter-spacing: .1em; margin-bottom: .65rem; }
.activity-grid b { display: block; font-size: clamp(1.25rem, 1.75vw, 2rem); line-height: 1.1; }
.activity-grid p { color: var(--muted); font-size: clamp(.85rem, 1.05vw, 1.2rem); line-height: 1.3; margin-top: .45rem; }

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
.section-label { color: var(--violet); font-size: clamp(.78rem, .95vw, 1.05rem); font-weight: 900; letter-spacing: .12em; margin-bottom: .8rem; }

.state-figure { background: white; border: 1px solid var(--line); display: grid; margin: 4vh 0 0; padding: 1.4rem; place-items: center; }
.state-figure img { height: 22vh; object-fit: contain; width: 100%; }
.state-benefits { display: grid; gap: 1rem; grid-template-columns: repeat(3, 1fr); margin-top: 3vh; }
.state-benefits span { background: var(--lavender); color: var(--purple); font-size: clamp(.9rem, 1.15vw, 1.3rem); font-weight: 800; padding: 1rem; text-align: center; }
.flow-states h2 { font-size: clamp(2.1rem, 3.15vw, 3.65rem); }
.flow-states .swimlane-figure { margin-top: 1.2vh; padding: .65rem; }
.flow-states .swimlane-figure img { height: 34vh; }
.state-flow { align-items: center; display: grid; gap: .45rem; grid-template-columns: repeat(11, auto); justify-content: center; margin-top: 1.7vh; }
.state-flow span { background: var(--lavender); color: var(--purple); font-size: clamp(.72rem, .9vw, 1.05rem); font-weight: 900; padding: .65rem .8rem; white-space: nowrap; }
.state-flow i { color: var(--violet); font-size: 1.2rem; font-style: normal; font-weight: 900; }
.resolution-note { color: var(--purple); font-size: clamp(.9rem, 1.05vw, 1.2rem); font-weight: 900; margin-top: 1vh; text-align: center; }

.form-preview { background: white; border: 1px solid var(--line); box-shadow: var(--shadow); margin-top: 5vh; padding: 1.2rem; }
.form-head { background: var(--purple); color: white; display: grid; gap: 1px; grid-template-columns: 1.3fr 1fr 1fr 1.3fr; }
.form-head b { border-right: 1px solid rgba(255,255,255,.3); font-size: clamp(.75rem, .95vw, 1.1rem); padding: 1rem; }
.form-body { display: grid; gap: 1px; grid-template-columns: 1fr 1.4fr 1fr; }
.form-body span { border: 1px solid var(--line); color: var(--muted); font-size: clamp(.9rem, 1.12vw, 1.3rem); min-height: 14vh; padding: 1rem; }
.form-foot { align-items: center; background: var(--paper-soft); display: flex; font-size: clamp(.8rem, 1vw, 1.15rem); gap: .65rem; padding: 1rem; }
.form-foot i { background: var(--line); height: 1px; margin: 0 1rem; width: 3rem; }

.tools-layout { display: grid; gap: 2vw; grid-template-columns: 1fr 1fr; margin-top: 4vh; }
.tools-layout article { background: white; border: 1px solid var(--line); min-height: 27vh; padding: 1.4rem; }
.tools-layout article > span { color: var(--purple); display: block; font-size: .82rem; font-weight: 900; letter-spacing: .12em; margin-bottom: 1.2rem; }
.field-cloud { display: grid; gap: .65rem; grid-template-columns: repeat(2, 1fr); }
.field-cloud b { background: var(--lavender); color: var(--purple); font-size: clamp(1rem, 1.25vw, 1.45rem); padding: .65rem .8rem; }
.indicator-card { border-top: 6px solid var(--purple) !important; }
.indicator-card ul { display: grid; gap: .45rem; list-style: none; margin: 0; padding: 0; }
.indicator-card li { border-bottom: 1px solid var(--line); font-size: clamp(1rem, 1.25vw, 1.45rem); font-weight: 800; padding: .45rem 0; }
.control-tools .bottom-line { font-size: clamp(1.15rem, 1.55vw, 1.8rem); margin-top: 3vh; }

.metric-grid article { background: white; border: 1px solid var(--line); min-height: 17vh; padding: 1.25rem; }
.metric-grid span { color: var(--purple); display: block; font-size: .78rem; font-weight: 900; letter-spacing: .1em; margin-bottom: 1rem; }
.metric-grid b { display: block; font-size: clamp(1.25rem, 1.7vw, 2rem); }
.metric-grid p { color: var(--muted); font-size: clamp(.85rem, 1vw, 1.15rem); margin-top: .5rem; }

.comparison-layout { align-items: center; display: grid; gap: 4vw; grid-template-columns: .8fr 1.2fr; height: 100%; }
.comparison-layout figure { background: white; border: 1px solid var(--line); display: grid; margin: 0; padding: 1rem; place-items: center; }
.comparison-layout img { height: 66vh; object-fit: contain; width: 100%; }
.comparison-layout ul { display: flex; flex-wrap: wrap; gap: .65rem; list-style: none; margin: 3vh 0 0; padding: 0; }
.comparison-layout li { background: var(--lavender); color: var(--purple); font-size: clamp(.85rem, 1.05vw, 1.2rem); font-weight: 900; padding: .65rem .85rem; }
.comparison-labels { display: grid; gap: .8rem; margin-top: 4vh; }
.comparison-labels span { background: white; border-left: 5px solid var(--violet); display: grid; gap: .35rem; padding: 1rem; }
.comparison-labels span:last-child { border-left-color: var(--purple); }
.comparison-labels small { color: var(--violet); font-size: .7rem; font-weight: 900; letter-spacing: .1em; }
.comparison-labels b { color: var(--ink); font-size: clamp(1.05rem, 1.4vw, 1.6rem); }
.comparison-labels > i { color: var(--purple); font-size: 1.5rem; font-style: normal; font-weight: 900; margin-left: 1rem; }

.conclusion-band { align-items: center; display: grid; gap: 1rem; grid-template-columns: 1fr auto 1fr auto 1fr; margin-top: 9vh; }
.conclusion-band span { background: var(--lavender); color: var(--purple); font-size: clamp(1.25rem, 1.8vw, 2.1rem); font-weight: 900; min-height: 14vh; padding: 1.2rem; text-align: center; }
.conclusion-band i { color: var(--violet); font-size: 2.5rem; font-style: normal; font-weight: 900; }
.four-words { display: grid; gap: 1rem; grid-template-columns: repeat(4, 1fr); margin-top: 9vh; }
.four-words span { border-bottom: 7px solid var(--purple); font-size: clamp(1.4rem, 2vw, 2.4rem); font-weight: 900; padding: 1.3rem .4rem; text-align: center; text-transform: uppercase; }
.result-equation { align-items: center; display: flex; flex-wrap: wrap; gap: 1rem; margin-top: 9vh; }
.result-equation span { background: var(--lavender); color: var(--purple); font-size: clamp(1.15rem, 1.55vw, 1.8rem); font-weight: 900; padding: 1rem 1.2rem; }
.result-equation i { color: var(--violet); font-size: 2rem; font-style: normal; font-weight: 900; }
.result-equation b { color: var(--purple); display: block; font-size: clamp(2.3rem, 3.4vw, 4rem); margin-top: 2vh; width: 100%; }

.conclusion-grid { display: grid; gap: 1.2rem; grid-template-columns: repeat(3, 1fr); margin-top: 4.5vh; }
.conclusion-grid article { background: white; border-top: 7px solid var(--purple); min-height: 24vh; padding: 1.35rem; }
.conclusion-grid span { color: var(--violet); display: block; font-size: .78rem; font-weight: 900; letter-spacing: .09em; margin-bottom: 1.2rem; }
.conclusion-grid p { font-size: clamp(1rem, 1.3vw, 1.5rem); font-weight: 800; line-height: 1.3; }
.learning-line { background: var(--lavender); color: var(--purple); font-size: clamp(.95rem, 1.18vw, 1.35rem); margin-top: 3vh; padding: 1rem; text-align: center; }

.recommend-grid { display: grid; gap: 1rem; grid-template-columns: repeat(2, 1fr); margin-top: 4vh; }
.recommend-grid article { background: white; border-left: 6px solid var(--purple); min-height: 16vh; padding: 1.25rem; }
.recommend-grid span { color: var(--violet); display: block; font-size: .8rem; font-weight: 900; letter-spacing: .1em; margin-bottom: .8rem; }
.recommend-grid b { display: block; font-size: clamp(1.15rem, 1.55vw, 1.8rem); line-height: 1.2; }
.recommend-layout { display: grid; gap: 1.1rem; margin-top: 4vh; }
.recommend-layout article { background: white; border-left: 6px solid var(--purple); padding: 1.2rem 1.4rem; }
.recommend-layout span { color: var(--violet); display: block; font-size: .78rem; font-weight: 900; letter-spacing: .11em; margin-bottom: .75rem; }
.recommend-layout b { display: block; font-size: clamp(1rem, 1.35vw, 1.55rem); line-height: 1.25; }
.idetel-recommendation { background: var(--lavender) !important; min-height: 15vh; }
.idetel-recommendation b { color: var(--purple); font-size: clamp(1.35rem, 2vw, 2.3rem); }
.idetel-recommendation i { color: var(--violet); font-style: normal; margin: 0 .3rem; }
.secondary-recommendations { display: grid; gap: 1.1rem; grid-template-columns: repeat(2, 1fr); }

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
  .company-layout, .problem-statement, .problem-layout, .objective-focus, .comparison-layout { grid-template-columns: 1fr; }
  .company-logo { display: none; }
  .handoff p, .service-path small, .objective-list p { font-size: .8rem; }
  .service-path { gap: .4rem; }
  .service-path div { min-height: 7rem; padding: .6rem; }
  .service-path div:not(:last-child)::after { display: none; }
  .objective-list, .impact-row, .proposal-grid, .state-benefits { gap: .6rem; }
  .objective-list article, .impact-row div { min-height: auto; padding: .8rem; }
  .wide-figure img { height: 28vh; }
  .comparison-layout figure { display: none; }
  .official-title { font-size: clamp(1.7rem, 6vw, 3rem); }
  .route-track { margin-top: 3vh; }
  .signal-list, .activity-grid, .tools-layout, .secondary-recommendations { grid-template-columns: 1fr 1fr; }
  .problem-layout .case-card { display: none; }
  .state-flow { display: flex; flex-wrap: wrap; }
  .flow-states .swimlane-figure img { height: 28vh; }
  .conclusion-grid { gap: .5rem; }
  .conclusion-grid article { min-height: auto; padding: .7rem; }
  .conclusion-grid p { font-size: .8rem; }
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
        capitulo_numero, capitulo_nombre = CAPITULOS[diapositiva.capitulo - 1]
        secciones.append(
            dedent(
                f"""
                <section class="slide {e(diapositiva.clase)}" data-notes="{notas}" aria-label="Diapositiva {numero} de {total}">
                  <div class="case-meta"><span>IDETEL · CONTROL DE SOLICITUDES</span><span>CAPÍTULO {capitulo_numero} · {e(capitulo_nombre)}</span></div>
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
          <title>Amaal Alrifaai Alrifaaie · Control administrativo de solicitudes</title>
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
