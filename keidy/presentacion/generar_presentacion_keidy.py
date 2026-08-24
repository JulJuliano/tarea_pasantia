#!/usr/bin/env python3
"""Genera una presentación web clara y legible para la defensa de Keidy Guzmán.

Uso:
    python3 generar_presentacion_keidy.py

Salida:
    index.html en la misma carpeta del script.

Controles en la presentación:
    Flechas / espacio  -> avanzar o retroceder
    F                  -> pantalla completa
    S                  -> mostrar/ocultar notas de la diapositiva
    Esc                -> cerrar notas o salir de pantalla completa

La presentación es autocontenida: no depende de internet ni de Reveal.js.
Si prefieres usar Reveal.js, puedes conservar la narrativa y el CSS y montar cada
<section> dentro de Reveal; la estructura está pensada para migrarse fácil.
"""

from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path
from textwrap import dedent

CARPETA = Path(__file__).resolve().parent
SALIDA = CARPETA / "index.html"
SALIDA_COPIA = CARPETA / "index(1).html"


@dataclass(frozen=True)
class Diapositiva:
    clase: str
    cuerpo: str
    notas: str


def e(texto: str) -> str:
    return escape(texto, quote=True)


def slide(clase: str, cuerpo: str, notas: str) -> Diapositiva:
    return Diapositiva(
        clase=clase,
        cuerpo=dedent(cuerpo).strip(),
        notas=dedent(notas).strip(),
    )


DIAPOSITIVAS: list[Diapositiva] = [
    slide(
        "cover",
        """
        <div class="cover-mark">DEFENSA DE PASANTÍAS PROFESIONALES</div>
        <div class="cover-grid">
            <div>
                <h1>Simplificación administrativa de la procura</h1>
                <p class="subtitle">Lubricantes y Equipos Varyna, C.A.</p>
                <div class="student">
                    <strong>Keidy Guzmán</strong>
                    <span>Administración · IUTECP</span>
                </div>
            </div>
            <div class="cover-figure" aria-label="Ruta de la exposición">
                <div class="mini-flow vertical">
                    <span><b>01</b> Diagnóstico</span>
                    <span><b>02</b> Propuesta</span>
                    <span><b>03</b> Cierre</span>
                </div>
            </div>
        </div>
        """,
        """
        Saludar al jurado, decir el título del informe y presentar el objetivo de la exposición:
        mostrar cómo se pasó de un proceso de procura disperso a una propuesta con recorrido
        claro, controlable y trazable.
        """,
    ),
    slide(
        "route",
        """
        <p class="eyebrow">RUTA DE LA EXPOSICIÓN</p>
        <h2>Del proceso disperso a un recorrido controlado.</h2>
        <div class="route-line five">
            <div><b>01</b><span>Empresa</span></div>
            <div><b>02</b><span>Problema</span></div>
            <div><b>03</b><span>Diagnóstico</span></div>
            <div><b>04</b><span>Propuesta</span></div>
            <div><b>05</b><span>Cierre</span></div>
        </div>
        """,
        """
        Anticipar el orden: primero se presenta la empresa y el área; luego el problema, el
        diagnóstico, la propuesta y finalmente conclusiones y recomendaciones. No leer la ruta:
        explicarla como hilo narrativo.
        """,
    ),
    slide(
        "company",
        """
        <p class="eyebrow">KEIDY GUZMÁN · ADMINISTRACIÓN</p>
        <h2>La empresa y el área de pasantía</h2>
        <p class="subtitle">Lubricantes y Equipos Varyna, C.A.</p>
        <div class="company-layout">
            <div class="big-number"><strong>36+</strong><span>años de trayectoria industrial</span></div>
            <div class="fact"><small>SECTOR</small><b>Petrolero · industrial · construcción</b></div>
            <div class="fact"><small>ÁREA</small><b>Departamento Administrativo</b></div>
            <div class="fact"><small>FOCO</small><b>Procura de insumos</b></div>
        </div>
        """,
        """
        Presentar la empresa como organización venezolana con trayectoria en sectores petrolero,
        industrial y de construcción. Señalar que la pasantía se desarrolló en el Departamento
        Administrativo, especialmente en actividades de procura.
        """,
    ),
    slide(
        "path",
        """
        <p class="eyebrow">PROCURA</p>
        <h2>¿Qué recorrido sigue una compra?</h2>
        <p class="subtitle">Necesidad · cotización · autorización · seguimiento</p>
        <div class="process-strip five">
            <div><b>01</b><span>Requisición</span></div>
            <div><b>02</b><span>Cotización</span></div>
            <div><b>03</b><span>Autorización</span></div>
            <div><b>04</b><span>Orden de compra</span></div>
            <div><b>05</b><span>Seguimiento</span></div>
        </div>
        <p class="bottom-claim">El problema aparece cuando ese recorrido no está formalizado.</p>
        """,
        """
        Explicar que la procura no es solo comprar. Es una cadena que empieza con una necesidad,
        pasa por cotizaciones, autorizaciones y orden de compra, y requiere seguimiento hasta el cierre.
        """,
    ),
    slide(
        "problem hero-split",
        """
        <div>
            <p class="eyebrow">SITUACIÓN PROBLEMÁTICA</p>
            <h2>Proceso de procura con flujo disperso.</h2>
        </div>
        <div class="three-terms">
            <div><small>CANAL</small><b>no único</b></div>
            <div><small>FORMATOS</small><b>no uniformes</b></div>
            <div><small>SEGUIMIENTO</small><b>manual</b></div>
        </div>
        """,
        """
        Describir la situación problemática: no existía un canal único formalizado, algunos formatos
        no eran uniformes y el seguimiento dependía demasiado del trabajo manual. Esto dificulta saber
        en qué estado está cada solicitud.
        """,
    ),
    slide(
        "list-light",
        """
        <p class="eyebrow">KEIDY GUZMÁN · ADMINISTRACIÓN</p>
        <h2>Manifestaciones observadas</h2>
        <ol class="statement-list">
            <li><b>01</b><span>Cuellos de botella en aprobaciones.</span></li>
            <li><b>02</b><span>Estatus de cotizaciones poco visible.</span></li>
            <li><b>03</b><span>Autorización por monto sin criterio claro.</span></li>
            <li><b>04</b><span>Indicadores de seguimiento ausentes.</span></li>
        </ol>
        """,
        """
        Explicar que los retrasos no dependen de un único error; se distribuyen entre recepción,
        cotización, aprobación y seguimiento. Detenerse en cada punto con un ejemplo breve.
        """,
    ),
    slide(
        "effects",
        """
        <p class="eyebrow">EFECTOS</p>
        <h2>Cuando el proceso no se ve, el control se vuelve manual.</h2>
        <div class="impact-grid">
            <div><small>DEMORAS</small><b>más tiempo de respuesta</b></div>
            <div><small>TRAZABILIDAD</small><b>menor claridad documental</b></div>
            <div><small>CARGA MANUAL</small><b>seguimiento repetitivo</b></div>
        </div>
        """,
        """
        Explicar los efectos administrativos: se invierte más tiempo en responder, se pierde claridad
        documental y el personal debe hacer más seguimiento manual. Aclarar que la propuesta busca
        ordenar el control, no eliminarlo.
        """,
    ),
    slide(
        "question",
        """
        <p class="eyebrow">INTERROGANTE ORIENTADORA</p>
        <h2>¿Cómo reducir la dispersión y fortalecer el seguimiento?</h2>
        <div class="rule"></div>
        <p class="eyebrow">OBJETIVO GENERAL</p>
        <p class="objective">Proponer la simplificación administrativa del proceso de procura.</p>
        <p class="subtitle">Agilizar el ciclo de adquisición y fortalecer el control interno.</p>
        """,
        """
        Presentar la pregunta orientadora y el objetivo general. Recalcar las dos finalidades: agilizar
        el ciclo de adquisición y fortalecer el control interno.
        """,
    ),
    slide(
        "objectives",
        """
        <h2>Tres objetivos específicos</h2>
        <div class="triad">
            <div><small>DIAGNOSTICAR</small><b>proceso actual</b></div>
            <div><small>IDENTIFICAR</small><b>causas de demora</b></div>
            <div><small>FORMULAR</small><b>propuesta de mejora</b></div>
        </div>
        <p class="bottom-claim">La cadena debía mantenerse coherente.</p>
        """,
        """
        Explicar que los tres objetivos siguen una secuencia lógica: primero conocer el proceso,
        luego identificar deficiencias y causas, y finalmente formular una propuesta relacionada con
        lo diagnosticado.
        """,
    ),
    slide(
        "diagnosis-method",
        """
        <p class="eyebrow">KEIDY GUZMÁN · ADMINISTRACIÓN</p>
        <h2>Cómo se realizó el diagnóstico</h2>
        <p class="subtitle">Técnicas de campo y análisis documental.</p>
        <div class="process-strip four">
            <div><b>01</b><span>Observación directa</span></div>
            <div><b>02</b><span>Entrevista estructurada</span></div>
            <div><b>03</b><span>Revisión documental</span></div>
            <div><b>04</b><span>Ishikawa</span></div>
        </div>
        """,
        """
        Explicar que no se trabajó solo con opiniones: se combinó observación directa, entrevistas,
        revisión de expedientes y diagrama de Ishikawa para organizar las causas.
        """,
    ),
    slide(
        "diagnosis-findings",
        """
        <p class="eyebrow">HALLAZGOS DEL DIAGNÓSTICO</p>
        <h2>El problema estaba distribuido en varias fases.</h2>
        <ol class="statement-list compact">
            <li><b>01</b><span>Recepción sin canal único.</span></li>
            <li><b>02</b><span>Cotizaciones con seguimiento disperso.</span></li>
            <li><b>03</b><span>Aprobaciones con criterios poco visibles.</span></li>
            <li><b>04</b><span>Cierre administrativo difícil de verificar.</span></li>
        </ol>
        """,
        """
        Resumir los hallazgos: el proceso tenía oportunidades de mejora en varias fases. Conectar
        esto con la necesidad de una propuesta integral y no de una solución aislada.
        """,
    ),
    slide(
        "theory",
        """
        <p class="eyebrow">KEIDY GUZMÁN · ADMINISTRACIÓN</p>
        <h2>Fundamentos teóricos</h2>
        <p class="subtitle">El marco teórico sostuvo la propuesta.</p>
        <div class="theory-map">
            <div><span>01</span><b>Procura y compras</b></div>
            <div><span>02</span><b>Proceso administrativo</b></div>
            <div><span>03</span><b>Control interno</b></div>
            <div><span>04</span><b>Simplificación administrativa</b></div>
        </div>
        <p class="quote-line">Comprar mejor no es comprar más rápido: es controlar mejor.</p>
        """,
        """
        Relacionar los conceptos teóricos. La procura define la cadena de compras; el proceso
        administrativo ordena planificación, organización, dirección y control; el control interno
        protege la trazabilidad; y la simplificación reduce redundancias sin quitar controles.
        """,
    ),
    slide(
        "weeks",
        """
        <p class="eyebrow">KEIDY GUZMÁN · ADMINISTRACIÓN</p>
        <h2>Diez semanas de pasantía</h2>
        <p class="subtitle">Actividades operativas y de análisis.</p>
        <div class="process-strip four tall">
            <div><b>01</b><span>Conocer el área</span></div>
            <div><b>02</b><span>Diagnosticar el proceso</span></div>
            <div><b>03</b><span>Diseñar la propuesta</span></div>
            <div><b>04</b><span>Validar y cerrar</span></div>
        </div>
        <p class="bottom-claim small">Apoyo continuo: requisiciones · cotizaciones · proveedores · expedientes</p>
        """,
        """
        Sintetizar las diez semanas en cuatro momentos: inducción y reconocimiento, diagnóstico,
        diseño de la propuesta y validación/cierre. Mencionar que en paralelo se apoyaron tareas
        operativas de procura.
        """,
    ),
    slide(
        "proposal",
        """
        <p class="eyebrow">PROPUESTA DE SIMPLIFICACIÓN</p>
        <h2>Ordenar el recorrido sin eliminar controles.</h2>
        <div class="proposal-layout">
            <div><b>01</b><span>Flujo definido.</span></div>
            <div><b>02</b><span>Responsables por etapa.</span></div>
            <div><b>03</b><span>Formatos estandarizados.</span></div>
            <div><b>04</b><span>Matriz de autorización.</span></div>
            <div><b>05</b><span>Indicadores de seguimiento.</span></div>
        </div>
        """,
        """
        Presentar los cinco componentes de la propuesta. Recalcar que simplificar no significa quitar
        controles, sino hacer que el recorrido sea claro, verificable y menos dependiente del seguimiento manual.
        """,
    ),
    slide(
        "flow",
        """
        <p class="eyebrow">KEIDY GUZMÁN · ADMINISTRACIÓN</p>
        <h2>Flujo propuesto</h2>
        <p class="subtitle">Un recorrido claro para cada requisición.</p>
        <div class="process-strip six">
            <div><b>01</b><span>Recibir</span></div>
            <div><b>02</b><span>Registrar</span></div>
            <div><b>03</b><span>Cotizar</span></div>
            <div><b>04</b><span>Autorizar</span></div>
            <div><b>05</b><span>Comprar</span></div>
            <div><b>06</b><span>Cerrar</span></div>
        </div>
        <p class="bottom-claim">Cada etapa tiene responsable y evidencia.</p>
        """,
        """
        Explicar el flujo propuesto. Cada requisición debe pasar por etapas reconocibles, con responsable
        y evidencia. Eso facilita saber dónde se encuentra una solicitud y qué falta para cerrar.
        """,
    ),
    slide(
        "formats",
        """
        <p class="eyebrow">KEIDY GUZMÁN · ADMINISTRACIÓN</p>
        <h2>Formatos y autorización</h2>
        <p class="subtitle">Estandarizar para decidir con claridad.</p>
        <div class="split-cards">
            <div><small>FORMATO ÚNICO</small><b>la solicitud contiene los mismos datos clave</b></div>
            <div><small>MATRIZ POR MONTO</small><b>cada compra sabe quién debe autorizar</b></div>
        </div>
        <p class="bottom-claim">Menos ambigüedad · más trazabilidad</p>
        """,
        """
        Aclarar que los formatos estandarizados no agregan burocracia innecesaria: permiten que las
        solicitudes tengan los mismos datos mínimos. La matriz por monto evita dudas sobre la autorización.
        """,
    ),
    slide(
        "indicators",
        """
        <p class="eyebrow">INDICADORES BÁSICOS</p>
        <h2>Medir para revisar y ajustar.</h2>
        <div class="metric-grid">
            <div><small>TIEMPO CICLO</small><b>días por compra</b></div>
            <div><small>PENDIENTES</small><b>solicitudes abiertas</b></div>
            <div><small>EN PLAZO</small><b>requisiciones atendidas</b></div>
        </div>
        """,
        """
        Explicar los indicadores: tiempo promedio del ciclo de compra, solicitudes pendientes y
        requisiciones atendidas dentro del plazo. Medir permite revisar si la propuesta funciona y ajustar.
        """,
    ),
    slide(
        "conclusions",
        """
        <p class="eyebrow">KEIDY GUZMÁN · ADMINISTRACIÓN</p>
        <h2>Conclusiones</h2>
        <p class="subtitle">Cada conclusión responde a un objetivo.</p>
        <ol class="statement-list compact">
            <li><b>01</b><span>El proceso requiere un canal único.</span></li>
            <li><b>02</b><span>Las demoras nacen de controles dispersos.</span></li>
            <li><b>03</b><span>La propuesta mejora trazabilidad y control.</span></li>
        </ol>
        """,
        """
        Presentar las conclusiones conectadas con los objetivos: se diagnosticó el proceso, se
        identificaron causas y se formuló una propuesta. Cerrar esta parte diciendo que los objetivos
        fueron cumplidos.
        """,
    ),
    slide(
        "recommendations",
        """
        <h2>Recomendaciones</h2>
        <ol class="statement-list compact">
            <li><b>01</b><span>Implementar de forma gradual.</span></li>
            <li><b>02</b><span>Socializar el flujo con el personal.</span></li>
            <li><b>03</b><span>Registrar indicadores mensuales.</span></li>
            <li><b>04</b><span>Revisar y ajustar el procedimiento.</span></li>
        </ol>
        <p class="thanks">Gracias. Quedo atenta a sus preguntas.</p>
        """,
        """
        Dar las recomendaciones y cerrar con agradecimiento. Frase final sugerida: Muchas gracias por
        su atención, quedo atenta a sus preguntas.
        """,
    ),
]


CSS = r"""
:root {
  --paper: #f6efe5;
  --paper-2: #fbf6ee;
  --ink: #201817;
  --muted: #6f625c;
  --accent: #a33a2e;
  --accent-2: #d97961;
  --clay: #ead0c6;
  --sand: #e5c48b;
  --sage: #8f9b83;
  --line: rgba(163, 58, 46, .32);
}

* { box-sizing: border-box; }
html, body { margin: 0; width: 100%; height: 100%; overflow: hidden; }
body {
  background: var(--paper);
  color: var(--ink);
  font-family: Arial, Helvetica, sans-serif;
}
button { font: inherit; }

.deck { width: 100vw; height: 100vh; position: relative; }
.slide {
  display: none;
  height: 100vh;
  overflow: hidden;
  padding: 6.5vh 5.6vw;
  position: absolute;
  inset: 0;
  width: 100vw;
}
.slide.active { display: block; }
.slide.hero-split { display: none; }
.slide.hero-split.active { display: flex; }

.slide::before {
  content: "";
  position: absolute;
  inset: 1.8rem;
  border: 1px solid rgba(163, 58, 46, .12);
  pointer-events: none;
}
.slide::after {
  content: "";
  position: absolute;
  right: 5.6vw;
  top: 6.5vh;
  width: 6.5rem;
  height: .55rem;
  background: linear-gradient(90deg, var(--accent), var(--sand));
  border-radius: 999px;
  opacity: .86;
}

h1, h2 {
  font-family: Georgia, 'Times New Roman', serif;
  font-weight: 800;
  letter-spacing: -.055em;
  margin: 0;
}
h1 { font-size: clamp(4.7rem, 8vw, 8.8rem); line-height: .93; max-width: 10ch; }
h2 { font-size: clamp(3.7rem, 6.4vw, 7.1rem); line-height: .96; max-width: 13.8ch; }
p { margin: 0; }
.subtitle {
  color: var(--muted);
  font-size: clamp(1.75rem, 3vw, 3rem);
  line-height: 1.15;
  margin-top: 1.5rem;
  max-width: 36ch;
}
.eyebrow {
  color: var(--accent);
  font-size: clamp(1.1rem, 1.75vw, 1.75rem);
  font-weight: 900;
  letter-spacing: .08em;
  margin-bottom: 1.35rem;
  text-transform: uppercase;
}

.cover { background: radial-gradient(circle at 84% 28%, rgba(217, 121, 97, .22), transparent 21rem), var(--paper-2); }
.cover::before { border-color: rgba(163, 58, 46, .18); }
.cover-grid { display: grid; grid-template-columns: minmax(0, 1.1fr) 31rem; gap: 5vw; align-items: center; height: 100%; }
.cover-mark { color: var(--accent); font-size: 1.65rem; font-weight: 900; letter-spacing: .08em; position: absolute; top: 6.5vh; left: 5.6vw; }
.cover h1 { margin-top: 4rem; }
.student { margin-top: 5.5rem; display: grid; gap: .55rem; }
.student strong { color: var(--accent); font-family: Georgia, 'Times New Roman', serif; font-size: 3.3rem; }
.student span { color: var(--muted); font-size: 2rem; }
.cover-figure {
  align-items: center;
  background: var(--clay);
  border: 2px solid var(--accent);
  display: flex;
  justify-content: center;
  min-height: 72vh;
  padding: 3rem;
  position: relative;
}
.cover-figure::before { content: ""; position: absolute; inset: 1.25rem; border: 1px solid var(--accent); opacity: .5; }
.mini-flow { display: flex; gap: 1rem; position: relative; z-index: 1; }
.mini-flow.vertical { flex-direction: column; }
.mini-flow span {
  align-items: center;
  background: var(--paper-2);
  border: 2px solid var(--accent);
  color: var(--accent);
  display: flex;
  flex-direction: column;
  font-size: 1.55rem;
  font-weight: 900;
  justify-content: center;
  min-height: 7rem;
  padding: 1rem;
  text-align: center;
}
.mini-flow b { color: var(--accent); display: block; font-size: 1.25rem; margin-bottom: .3rem; }

.route, .effects, .indicators { background: linear-gradient(135deg, var(--paper-2), #f2e6d7); }
.route-line, .process-strip { display: grid; gap: 1rem; margin-top: 7.2rem; position: relative; }
.route-line.five, .process-strip.five { grid-template-columns: repeat(5, 1fr); }
.process-strip.four { grid-template-columns: repeat(4, 1fr); }
.process-strip.six { grid-template-columns: repeat(6, 1fr); }
.route-line div, .process-strip div {
  align-items: center;
  background: rgba(255,255,255,.45);
  border: 2px solid var(--accent);
  color: var(--accent);
  display: flex;
  flex-direction: column;
  justify-content: center;
  min-height: 10.2rem;
  padding: 1rem;
  position: relative;
  text-align: center;
}
.route-line div:not(:last-child)::after, .process-strip div:not(:last-child)::after {
  content: "→";
  color: var(--accent);
  font-size: 2.2rem;
  font-weight: 800;
  position: absolute;
  right: -1.45rem;
  top: 50%;
  transform: translateY(-50%);
  z-index: 5;
}
.route-line b, .process-strip b { font-size: 2rem; margin-bottom: .55rem; }
.route-line span, .process-strip span { color: var(--ink); font-size: 2.1rem; font-weight: 900; line-height: 1.05; }
.process-strip.six { gap: .74rem; }
.process-strip.six div { min-height: 8.7rem; padding: .72rem; }
.process-strip.six span { font-size: 1.75rem; }
.process-strip.tall div { min-height: 11.5rem; }
.path .process-strip { margin-top: 5.2rem; }
.path .bottom-claim { margin-top: 3.1rem; font-size: clamp(2.2rem, 4.25vw, 4.6rem); }
.bottom-claim {
  font-family: Georgia, 'Times New Roman', serif;
  font-size: clamp(2.5rem, 4.8vw, 5.1rem);
  font-weight: 800;
  letter-spacing: -.045em;
  line-height: 1.02;
  margin-top: 5.4rem;
  text-align: center;
}
.bottom-claim.small { color: var(--muted); font-family: Arial, Helvetica, sans-serif; font-size: 2.35rem; font-weight: 400; letter-spacing: 0; }

.company-layout { display: grid; grid-template-columns: 1.15fr 1fr 1fr 1fr; gap: 2rem; margin-top: 4.8rem; align-items: stretch; }
.big-number, .fact {
  background: rgba(255,255,255,.42);
  border-top: 8px solid var(--accent);
  min-height: 21rem;
  padding: 2rem;
}
.big-number strong { color: var(--accent); display: block; font-family: Georgia, 'Times New Roman', serif; font-size: 7rem; letter-spacing: -.08em; line-height: .85; }
.big-number span { color: var(--muted); display: block; font-size: 2.2rem; line-height: 1.1; margin-top: 1.5rem; }
.fact small, .impact-grid small, .metric-grid small, .split-cards small, .triad small {
  color: var(--accent);
  display: block;
  font-size: 1.55rem;
  font-weight: 900;
  letter-spacing: .08em;
  margin-bottom: 2.3rem;
}
.fact b { display: block; font-family: Georgia, 'Times New Roman', serif; font-size: 3rem; letter-spacing: -.04em; line-height: 1; }

.problem { background: #f1d8d2; }
.slide.hero-split { flex-direction: column; justify-content: space-between; }
.three-terms, .impact-grid, .metric-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; margin-bottom: 3.5rem; }
.three-terms div, .impact-grid div, .metric-grid div {
  border-top: 5px solid var(--accent);
  padding: 2rem 1.2rem;
  text-align: center;
}
.three-terms small { color: var(--accent); display: block; font-size: 1.65rem; font-weight: 900; letter-spacing: .08em; margin-bottom: 2rem; }
.three-terms b, .impact-grid b, .metric-grid b { display: block; font-family: Georgia, 'Times New Roman', serif; font-size: 3.25rem; letter-spacing: -.04em; line-height: 1.05; }

.statement-list { list-style: none; margin: 5rem 0 0; padding: 0; max-width: 95rem; }
.statement-list li { display: grid; grid-template-columns: 6rem 1fr; gap: 1.5rem; align-items: start; margin: 1.35rem 0; }
.statement-list b { color: var(--accent); font-size: 2.05rem; line-height: 1.1; }
.statement-list span { font-family: Georgia, 'Times New Roman', serif; font-size: clamp(2.4rem, 3.65vw, 4.5rem); font-weight: 800; letter-spacing: -.045em; line-height: 1.05; }
.statement-list.compact { margin-top: 2.8rem; }
.statement-list.compact li { margin: 1.1rem 0; }
.statement-list.compact span { font-size: clamp(2.25rem, 3.25vw, 4.1rem); }
.list-light .statement-list { margin-top: 3.2rem; }

.effects h2, .indicators h2 { max-width: 16ch; }
.impact-grid, .metric-grid { margin-top: 7.8rem; margin-bottom: 0; }
.impact-grid div, .metric-grid div { min-height: 16rem; }

.rule { height: 2px; background: var(--line); margin: 4.6rem 0 3.8rem; width: 100%; }
.objective { color: var(--accent); font-family: Georgia, 'Times New Roman', serif; font-size: clamp(3.2rem, 5.8vw, 6.3rem); font-weight: 800; letter-spacing: -.055em; line-height: .98; max-width: 18ch; }
.question h2 { max-width: 17ch; font-size: clamp(3.2rem, 5.65vw, 6.25rem); }
.question .rule { margin: 3.3rem 0 2.8rem; }
.question .objective { font-size: clamp(2.85rem, 5vw, 5.5rem); }
.question .subtitle { font-size: clamp(1.45rem, 2.5vw, 2.5rem); margin-top: 1rem; }

.objectives { background: #f1d8d2; }
.triad { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; margin-top: 9rem; text-align: center; }
.triad div { border-top: 5px solid var(--accent); padding-top: 2rem; }
.triad b { font-family: Georgia, 'Times New Roman', serif; font-size: 3.45rem; letter-spacing: -.04em; line-height: 1; }

.theory-map { display: grid; grid-template-columns: repeat(2, 1fr); gap: 2rem; margin-top: 4rem; }
.theory-map div { background: rgba(255,255,255,.48); border-left: 8px solid var(--accent); min-height: 9rem; padding: 1.5rem 2rem; }
.theory-map span { color: var(--accent); display: block; font-size: 1.4rem; font-weight: 900; margin-bottom: .7rem; }
.theory-map b { font-family: Georgia, 'Times New Roman', serif; font-size: 3.3rem; letter-spacing: -.045em; line-height: 1; }
.quote-line { color: var(--accent); font-family: Georgia, 'Times New Roman', serif; font-size: 3.7rem; font-weight: 800; letter-spacing: -.04em; margin-top: 3.4rem; text-align: center; }

.proposal { background: linear-gradient(135deg, var(--paper-2), #f3e4d2); }
.proposal-layout { display: grid; grid-template-columns: 1fr 1fr; gap: 2.1rem 4rem; margin-top: 4.5rem; max-width: 90rem; }
.proposal-layout div { display: grid; grid-template-columns: 5rem 1fr; align-items: start; }
.proposal-layout b { color: var(--accent); font-size: 1.9rem; }
.proposal-layout span { font-family: Georgia, 'Times New Roman', serif; font-size: 3.6rem; font-weight: 800; letter-spacing: -.045em; line-height: 1; }

.split-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 6rem; margin-top: 5rem; }
.split-cards div { background: rgba(255,255,255,.45); border-top: 8px solid var(--accent); min-height: 18rem; padding: 2rem; }
.split-cards b { font-family: Georgia, 'Times New Roman', serif; font-size: 3.8rem; letter-spacing: -.045em; line-height: 1.02; }

.thanks { color: var(--accent); font-family: Georgia, 'Times New Roman', serif; font-size: 3.3rem; font-weight: 800; letter-spacing: -.035em; margin-top: 3.3rem; text-align: center; }

.progress { position: fixed; left: 0; right: 0; bottom: 0; height: 8px; background: rgba(163, 58, 46, .15); z-index: 50; }
.progress span { display: block; height: 100%; background: var(--accent); width: 0%; transition: width .25s ease; }
.counter { position: fixed; right: 2rem; bottom: 1.45rem; color: var(--muted); font-size: 1rem; font-weight: 800; letter-spacing: .08em; z-index: 51; }
.notes-panel {
  background: rgba(32,24,23,.96);
  color: #fff8ef;
  display: none;
  font-size: 1.6rem;
  line-height: 1.38;
  max-width: 64rem;
  padding: 2rem;
  position: fixed;
  right: 2rem;
  bottom: 3.2rem;
  z-index: 60;
  border-radius: 1rem;
  box-shadow: 0 1.4rem 4rem rgba(0,0,0,.28);
}
.notes-panel.show { display: block; }
.notes-panel b { color: #f4c08d; display: block; margin-bottom: .65rem; }

@media (min-width: 901px) and (max-width: 1500px) {
  .slide { padding-top: 5.5vh; padding-bottom: 5vh; }
  .cover-grid { grid-template-columns: minmax(0, 1fr) 24rem; gap: 3vw; }
  .cover h1 { font-size: clamp(3.8rem, 7vw, 6.8rem); margin-top: 2.5rem; }
  .cover .subtitle { font-size: clamp(1.4rem, 2.3vw, 2.4rem); margin-top: 1rem; }
  .student { margin-top: 2.8rem; }
  .student strong { font-size: 2.5rem; }
  .student span { font-size: 1.5rem; }
  .cover-figure { min-height: 68vh; padding: 2rem; }
  .mini-flow span { min-height: 5.5rem; padding: .7rem; font-size: 1.25rem; }
  .route-line, .process-strip { margin-top: 5.2rem; }
  .bottom-claim { margin-top: 3.8rem; font-size: clamp(2.1rem, 4.2vw, 4.6rem); }
  .path .bottom-claim { margin-top: 1.4rem; font-size: clamp(1.8rem, 2.8vw, 3rem); }
  .company-layout { margin-top: 3.6rem; gap: 1.2rem; }
  .big-number, .fact { min-height: 17rem; padding: 1.3rem; }
  .fact b { font-size: 2.4rem; }
  .triad { margin-top: 6rem; }
  .impact-grid, .metric-grid { margin-top: 5.5rem; }
  .impact-grid { margin-top: 4.2rem; }
  .impact-grid div { min-height: 13rem; }
  .impact-grid b, .metric-grid b { font-size: 2.65rem; }
  .question .rule { margin: 2.2rem 0 1.7rem; }
  .question .objective { max-width: 20ch; font-size: clamp(2.4rem, 4.1vw, 4.6rem); }
  .question .subtitle { font-size: clamp(1.25rem, 2.1vw, 2.1rem); }
  .theory-map { gap: 1.2rem; margin-top: 2.8rem; }
  .theory-map div { min-height: 7rem; padding: 1rem 1.2rem; border-left-width: 5px; }
  .theory-map span { font-size: 1.1rem; margin-bottom: .45rem; }
  .theory-map b { font-size: 2.5rem; }
  .quote-line { font-size: clamp(1.8rem, 2.4vw, 2.8rem); margin-top: 1rem; }
  .proposal-layout { gap: 1rem 2rem; margin-top: 2.8rem; }
  .proposal-layout div { grid-template-columns: 4rem 1fr; }
  .proposal-layout span { font-size: 2.8rem; line-height: 1.02; }
  .split-cards { gap: 3rem; margin-top: 3rem; }
  .split-cards div { min-height: 13rem; padding: 1.3rem; }
  .split-cards b { font-size: 2.7rem; }
  .formats .bottom-claim { margin-top: 2rem; font-size: clamp(1.9rem, 3.5vw, 3.8rem); }
  .weeks .bottom-claim.small { margin-top: 2rem; font-size: 2.1rem; }
}

@media (max-width: 900px) {
  .slide { padding: 3.8vh 5vw; }
  .slide::before { inset: .85rem; }
  .slide::after { right: 5vw; top: 3.8vh; width: 4rem; height: .35rem; }
  .cover-grid { grid-template-columns: 1fr; }
  .cover-figure { display: none; }
  .cover h1 { margin-top: 2rem; }
  .cover-mark { left: 5vw; top: 3.8vh; font-size: .85rem; }
  .student { margin-top: 2rem; }
  .student strong { font-size: 1.9rem; }
  .student span { font-size: 1.1rem; }
  h1 { font-size: clamp(2.2rem, 7.5vw, 4.2rem); }
  h2 { font-size: clamp(2rem, 6vw, 3.4rem); max-width: 16ch; }
  .eyebrow { font-size: clamp(.7rem, 1.7vw, 1.1rem); margin-bottom: .65rem; }
  .subtitle { font-size: clamp(1rem, 2.8vw, 1.75rem); margin-top: .7rem; }
  .route-line.five, .process-strip.five { grid-template-columns: repeat(5, minmax(0, 1fr)); }
  .process-strip.four { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .process-strip.six { grid-template-columns: repeat(6, minmax(0, 1fr)); }
  .route-line, .process-strip { gap: .35rem; margin-top: 2.2rem; }
  .route-line div, .process-strip div { border-width: 1px; min-height: 5.2rem; padding: .45rem .25rem; }
  .route-line div:not(:last-child)::after, .process-strip div:not(:last-child)::after { display: none; }
  .route-line b, .process-strip b { font-size: .85rem; margin-bottom: .25rem; }
  .route-line span, .process-strip span { font-size: clamp(.65rem, 1.7vw, 1.1rem); overflow-wrap: anywhere; }
  .process-strip.six { gap: .25rem; }
  .process-strip.six div { min-height: 4.6rem; padding: .35rem .18rem; }
  .process-strip.six span { font-size: clamp(.6rem, 1.45vw, 1rem); }
  .process-strip.tall div { min-height: 5.5rem; }
  .path .process-strip { margin-top: 2.2rem; }
  .path .bottom-claim { margin-top: 1.8rem; font-size: clamp(1.35rem, 4vw, 2.3rem); }
  .bottom-claim { font-size: clamp(1.35rem, 4vw, 2.3rem); margin-top: 2rem; }
  .bottom-claim.small { font-size: clamp(.8rem, 2vw, 1.25rem); margin-top: 1.4rem; }
  .company-layout, .three-terms, .impact-grid, .metric-grid, .triad, .theory-map, .proposal-layout, .split-cards { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .company-layout { gap: .7rem; margin-top: 2.2rem; }
  .big-number, .fact { min-height: 7.5rem; padding: .8rem; border-top-width: 3px; }
  .big-number strong { font-size: 3.2rem; }
  .big-number span { font-size: 1rem; margin-top: .6rem; }
  .fact small, .impact-grid small, .metric-grid small, .split-cards small, .triad small { font-size: .65rem; margin-bottom: .6rem; }
  .fact b { font-size: 1.3rem; }
  .three-terms, .impact-grid, .metric-grid { gap: .7rem; margin-bottom: 1.2rem; }
  .three-terms div, .impact-grid div, .metric-grid div { border-top-width: 2px; padding: .7rem .35rem; }
  .three-terms small { font-size: .65rem; margin-bottom: .6rem; }
  .three-terms b, .impact-grid b, .metric-grid b { font-size: 1.35rem; }
  .impact-grid, .metric-grid { margin-top: 2.5rem; }
  .impact-grid div, .metric-grid div { min-height: 6.5rem; }
  .statement-list { margin-top: 2rem; }
  .statement-list li { grid-template-columns: 2.4rem 1fr; gap: .55rem; margin: .65rem 0; }
  .statement-list b { font-size: .85rem; }
  .statement-list span, .statement-list.compact span { font-size: clamp(1.3rem, 3.5vw, 2.2rem); }
  .statement-list.compact { margin-top: 1.8rem; }
  .statement-list.compact li { margin: .55rem 0; }
  .rule { margin: 2rem 0 1.6rem; }
  .objective, .question .objective { font-size: clamp(1.8rem, 5vw, 3rem); }
  .question h2 { font-size: clamp(2rem, 5.5vw, 3.3rem); max-width: 18ch; }
  .question .rule { margin: 1.8rem 0 1.4rem; }
  .question .subtitle { font-size: clamp(1rem, 2.5vw, 1.4rem); margin-top: .7rem; }
  .triad { gap: .7rem; margin-top: 2.5rem; }
  .triad div { border-top-width: 2px; padding-top: .7rem; }
  .triad b { font-size: 1.35rem; }
  .theory-map { gap: .7rem; margin-top: 2rem; }
  .theory-map div { min-height: 5rem; padding: .7rem; border-left-width: 3px; }
  .theory-map span { font-size: .7rem; margin-bottom: .3rem; }
  .theory-map b { font-size: 1.3rem; }
  .quote-line { font-size: 1.4rem; margin-top: 1.5rem; }
  .proposal-layout { gap: .9rem 1.2rem; margin-top: 2.2rem; }
  .proposal-layout div { grid-template-columns: 2rem 1fr; }
  .proposal-layout b { font-size: .8rem; }
  .proposal-layout span { font-size: 1.45rem; }
  .split-cards { gap: .7rem; margin-top: 2.2rem; }
  .split-cards div { min-height: 8rem; padding: .8rem; border-top-width: 3px; }
  .split-cards b { font-size: 1.45rem; }
  .thanks { font-size: 1.4rem; margin-top: 1.6rem; }
}

@media (max-width: 900px) and (orientation: landscape) {
  .company-layout { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .three-terms, .impact-grid, .metric-grid, .triad { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .theory-map, .proposal-layout, .split-cards { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
"""


JS = r"""
(() => {
  const slides = Array.from(document.querySelectorAll('.slide'));
  const progress = document.querySelector('.progress span');
  const counter = document.querySelector('.counter');
  const notes = document.querySelector('.notes-panel');
  let index = 0;

  function render() {
    slides.forEach((s, i) => s.classList.toggle('active', i === index));
    progress.style.width = `${((index + 1) / slides.length) * 100}%`;
    counter.textContent = `${String(index + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')}`;
    notes.classList.remove('show');
    notes.innerHTML = `<b>Notas del expositor</b>${slides[index].dataset.notes}`;
    document.title = `Keidy Guzmán · Diapositiva ${index + 1}`;
  }

  function next() { if (index < slides.length - 1) { index += 1; render(); } }
  function prev() { if (index > 0) { index -= 1; render(); } }

  document.addEventListener('keydown', (ev) => {
    if (ev.key === 'ArrowRight' || ev.key === 'PageDown' || ev.key === ' ') next();
    if (ev.key === 'ArrowLeft' || ev.key === 'PageUp') prev();
    if (ev.key === 'Home') { index = 0; render(); }
    if (ev.key === 'End') { index = slides.length - 1; render(); }
    if (ev.key.toLowerCase() === 's') notes.classList.toggle('show');
    if (ev.key.toLowerCase() === 'f') {
      if (!document.fullscreenElement) document.documentElement.requestFullscreen?.();
      else document.exitFullscreen?.();
    }
    if (ev.key === 'Escape') notes.classList.remove('show');
  });

  document.addEventListener('click', (ev) => {
    if (ev.target.closest('.notes-panel')) return;
    next();
  });

  render();
})();
"""


def construir_html() -> str:
    slides_html = []
    total = len(DIAPOSITIVAS)
    for i, s in enumerate(DIAPOSITIVAS, start=1):
        notas = e(s.notas).replace("\n", "<br>")
        slides_html.append(
            f'<section class="slide {e(s.clase)}" data-notes="{notas}" aria-label="Diapositiva {i} de {total}">\n{s.cuerpo}\n</section>'
        )

    return dedent(
        f"""
        <!doctype html>
        <html lang="es">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <meta name="theme-color" content="#f6efe5">
          <title>Keidy Guzmán · Simplificación administrativa de la procura</title>
          <style>{CSS}</style>
        </head>
        <body>
          <main class="deck">
            {''.join(slides_html)}
          </main>
          <div class="notes-panel" aria-live="polite"></div>
          <div class="counter"></div>
          <div class="progress"><span></span></div>
          <script>{JS}</script>
        </body>
        </html>
        """
    ).strip() + "\n"


def main() -> None:
    html = construir_html()
    for salida in (SALIDA, SALIDA_COPIA):
        salida.write_text(html, encoding="utf-8")
    print(f"Presentación generada: {SALIDA}")
    print(f"Diapositivas: {len(DIAPOSITIVAS)}")


if __name__ == "__main__":
    main()
