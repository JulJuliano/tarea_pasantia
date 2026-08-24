#!/usr/bin/env python3
"""Genera la presentación web de defensa para el informe de Juliano."""

from html import escape
from pathlib import Path
from textwrap import dedent


CARPETA = Path(__file__).resolve().parent
CARPETA_IMAGENES = CARPETA.parent / "imagenes"
SALIDA = CARPETA / "index.html"

ETAPAS = (
    ("01", "OBSERVAR"),
    ("02", "MODELAR"),
    ("03", "IMPLEMENTAR"),
    ("04", "VALIDAR"),
)


def imagen(nombre, alt, clase=""):
    """Devuelve una imagen local con una ruta relativa al HTML generado."""
    ruta = Path("../imagenes") / nombre
    clase_html = f' class="{escape(clase)}"' if clase else ""
    return (
        f'<img src="{escape(ruta.as_posix())}" alt="{escape(alt)}"'
        f'{clase_html} loading="eager">'
    )


def ruta_expediente(etapa):
    """Crea la línea lateral que representa las fases reales del proyecto."""
    pasos = []
    for codigo, nombre in ETAPAS:
        activo = " is-active" if nombre.lower() == etapa else ""
        pasos.append(f'<span class="rail-step{activo}"><b>{codigo}</b>{nombre}</span>')
    return dedent(
        f"""
        <aside class="dossier-rail" aria-label="Fases del proyecto">
          <div class="rail-brand">BASE<br><span>ACCESS</span></div>
          <div class="rail-rule"></div>
          <div class="rail-steps">{''.join(pasos)}</div>
          <div class="rail-foot">INFORME<br>JULIANO<br><span>2026</span></div>
        </aside>
        """
    )


def diapositiva(cuerpo, notas="", clase="", transicion="fade", etapa="observar"):
    atributos = [f'data-transition="{escape(transicion)}"']
    if clase:
        atributos.append(f'class="{escape(clase)}"')
    notas_html = f'<aside class="notes">{escape(notas)}</aside>' if notas else ""
    return (
        f'<section {" ".join(atributos)}>'
        f'<div class="slide-shell">{ruta_expediente(etapa)}'
        f'<div class="slide-body">{cuerpo}</div></div>{notas_html}</section>'
    )


def construir_diapositivas():
    return [
        diapositiva(
            dedent(
                """
                <div class="title-layout">
                  <div class="title-copy">
                    <div class="kicker">INFORME DE PASANTÍA · 2026</div>
                    <h1>Del expediente<br><span>al dato trazable</span></h1>
                    <p class="title-subtitle">Prototipo de sistema para el control, trazabilidad y reporte documental en la Presidencia de Venangocupet, S.A.</p>
                    <div class="author-line"><strong>JULIANO CARDONA</strong><span>INFORMÁTICA</span><span>9 SEMANAS</span></div>
                  </div>
                  <div class="hero-seal" aria-label="La ruta del expediente">
                    <span class="seal-label">LA RUTA</span>
                    <div class="seal-track"><i></i><i></i><i></i><i></i></div>
                    <strong>REGISTRAR<br>SEGUIR<br>REPORTAR</strong>
                    <small>Un recorrido visible<br>de principio a fin.</small>
                  </div>
                </div>
                """
            ),
            "Abrir con la tesis: el proyecto toma un flujo documental manual y lo convierte en un recorrido que puede registrarse, seguirse y reportarse.",
            clase="title-slide",
            transicion="zoom",
            etapa="observar",
        ),
        diapositiva(
            dedent(
                """
                <div class="kicker">EL PROBLEMA OPERATIVO</div>
                <div class="claim-layout">
                  <div class="claim-index">01</div>
                  <div>
                    <h2>Una pregunta sencilla no tenía una respuesta inmediata.</h2>
                    <p class="lead">¿Dónde está cada expediente y qué ocurrió con él?</p>
                    <div class="question-strip">
                      <span>¿RECIBIDO?</span><span>¿FIRMADO?</span><span>¿DESPACHADO?</span>
                    </div>
                  </div>
                </div>
                <div class="bottom-note"><b>Observación de campo</b><span>La información estaba distribuida entre hojas, transcripciones y revisiones manuales.</span></div>
                """
            ),
            "En Presidencia, responder sobre el estado de un documento exigía revisar registros y consolidar información repetitiva. La dificultad no era solo guardar datos: era conservar el recorrido.",
            clase="paper-slide",
            transicion="fade",
            etapa="observar",
        ),
        diapositiva(
            dedent(
                f"""
                <div class="kicker light-kicker">ANTES · FLUJO OBSERVADO</div>
                <div class="visual-heading"><h2>El documento se mueve;<br><em>el control se fragmenta.</em></h2><span class="visual-code">AS-IS / PRESIDENCIA</span></div>
                <div class="large-diagram">{imagen("02_flujo_as_is_presidencia.png", "Flujo actual de recepción, firma y despacho de expedientes")}</div>
                <div class="three-labels"><span>TRANSCRIBIR</span><span>CONFIRMAR</span><span>RESUMIR</span></div>
                """
            ),
            "Explicar el flujo real sin dramatizarlo: recepción, revisión, registro, firma y despacho dependían de controles dispersos. El costo aparecía cuando había que reconstruir la historia.",
            clase="dark-slide",
            transicion="slide",
            etapa="observar",
        ),
        diapositiva(
            dedent(
                f"""
                <div class="kicker light-kicker">DESPUÉS · PROPUESTA</div>
                <div class="visual-heading"><h2>El mismo proceso,<br><em>con memoria.</em></h2><span class="visual-code">TO-BE / PROTOTIPO</span></div>
                <div class="large-diagram solution-diagram">{imagen("03_flujo_to_be_sistema_automatizado.png", "Flujo propuesto con el prototipo BaseAccess")}</div>
                <div class="promise-row"><span><b>VALIDAR</b> datos antes de guardar</span><span><b>RASTREAR</b> movimientos e historial</span><span><b>REPORTAR</b> sin transcribir de nuevo</span></div>
                """
            ),
            "La propuesta no cambia las responsabilidades del departamento. Agrega una capa de registro estructurado, validación, historial, consulta y reportes.",
            clase="wine-slide",
            transicion="slide",
            etapa="modelar",
        ),
        diapositiva(
            dedent(
                f"""
                <div class="kicker">EL PROTOTIPO EN UNA MIRADA</div>
                <div class="visual-heading paper-heading"><h2>La interfaz convierte el flujo<br>en decisiones visibles.</h2><span class="visual-code">BASEACCESS / UI</span></div>
                <div class="interface-layout">
                  <div class="interface-shot">{imagen("captura-registro-nuevo-contexto.png", "Vista general de BaseAccess con navegación modular y registros")}</div>
                  <div class="proof-list">
                    <div><b>01</b><span>Navegar por módulos y hojas activas.</span></div>
                    <div><b>02</b><span>Registrar documentos, estatus y relaciones.</span></div>
                    <div><b>03</b><span>Consultar el recorrido sin abandonar la vista.</span></div>
                  </div>
                </div>
                """
            ),
            "Aquí se muestra el resultado visible del modelado: una interfaz de escritorio que concentra módulos, registros, hojas y acciones sin perder el contexto del usuario.",
            clase="paper-slide interface-slide",
            transicion="fade",
            etapa="implementar",
        ),
        diapositiva(
            dedent(
                f"""
                <div class="kicker light-kicker">CÓMO SE CONSTRUYÓ</div>
                <div class="visual-heading"><h2>Una aplicación pequeña<br>para un problema concreto.</h2><span class="visual-code">WAILS / SQLITE</span></div>
                <div class="architecture-layout">
                  <div class="architecture-shot">{imagen("06_arquitectura_prototipo.png", "Arquitectura del prototipo: interfaz, Wails, lógica y SQLite")}</div>
                  <div class="layer-stack"><span><b>INTERFAZ</b> WebView2</span><span><b>APLICACIÓN</b> Wails + Go</span><span><b>DATOS</b> SQLite local</span></div>
                </div>
                <p class="dark-caption">Las capas se separan para que el registro, la consulta y el historial puedan evolucionar sin perder el modelo documental.</p>
                """
            ),
            "No presentar la arquitectura como una lista de tecnologías. Explicar qué responsabilidad queda en cada capa y por qué SQLite encaja con un prototipo de escritorio local.",
            clase="dark-slide architecture-slide",
            transicion="fade",
            etapa="implementar",
        ),
        diapositiva(
            dedent(
                f"""
                <div class="kicker">LA LÓGICA ANTES DEL CÓDIGO</div>
                <div class="visual-heading paper-heading"><h2>El sistema decide en un orden<br>que se puede explicar.</h2><span class="visual-code">ANEXO H</span></div>
                <div class="pseudo-layout">
                  <div class="pseudo-shot">{imagen("05_pseudocodigo_general_baseaccess.png", "Pseudocódigo general de operación de BaseAccess")}</div>
                  <div class="pseudo-note"><b>Entrada</b><span>Archivo SQLite, formulario y acción del usuario.</span><b>Control</b><span>Validación, transacción, historial y filtros.</span><b>Salida</b><span>Registro trazable, consulta y XLSX.</span></div>
                </div>
                """
            ),
            "El pseudocódigo resume la operación completa: abrir y validar la base, cargar el contexto, procesar una acción con validaciones y transacción, consultar o exportar y cerrar con respaldo.",
            clase="paper-slide pseudo-slide",
            transicion="fade",
            etapa="implementar",
        ),
        diapositiva(
            dedent(
                f"""
                <div class="kicker">REGLAS DE NEGOCIO VISIBLES</div>
                <div class="visual-heading paper-heading"><h2>La pantalla cambia cuando<br>cambia el expediente.</h2><span class="visual-code">EVIDENCIA / INTERFAZ</span></div>
                <div class="evidence-grid">
                  <figure>{imagen("captura-formulario-general.png", "Formulario general de registro documental")}<figcaption>Captura estructurada</figcaption></figure>
                  <figure>{imagen("captura-expedientes-frentes.png", "Formulario de expedientes con múltiples frentes")}<figcaption>Frentes dinámicos</figcaption></figure>
                  <figure>{imagen("captura-catalogos-validaciones.png", "Gestión de catálogos y validaciones")}<figcaption>Datos maestros</figcaption></figure>
                </div>
                <p class="micro-caption">La configuración se expresa en la interfaz; la validación protege el dato antes de la transacción.</p>
                """
            ),
            "Usar tres ejemplos concretos: el formulario común, la generación de frentes adicionales y la administración de catálogos. No enumerar todos los módulos.",
            clase="paper-slide evidence-slide",
            transicion="slide",
            etapa="implementar",
        ),
        diapositiva(
            dedent(
                f"""
                <div class="kicker light-kicker">USAR LA INFORMACIÓN</div>
                <div class="visual-heading"><h2>Registrar es el inicio.<br><em>Seguir y reportar es el resultado.</em></h2><span class="visual-code">OPERACIÓN / SALIDA</span></div>
                <div class="operations-layout">
                  <figure class="operation-shot wide-shot">{imagen("captura-ruta-seleccion-multiple.png", "Ruta de procesos con selección múltiple")}</figure>
                  <figure class="operation-shot">{imagen("captura-exportacion-filtros-columnas.png", "Exportación de información con filtros y columnas")}</figure>
                </div>
                <div class="operations-footer"><span>PLANIFICAR ACTIVIDADES</span><span>EXPORTAR INFORMACIÓN</span></div>
                """
            ),
            "La trazabilidad se vuelve útil cuando permite actuar: seleccionar actividades en una ruta, aplicar filtros y exportar una salida para revisión.",
            clase="wine-slide operations-slide",
            transicion="slide",
            etapa="validar",
        ),
        diapositiva(
            dedent(
                f"""
                <div class="kicker">EVIDENCIA DEL PROCESO</div>
                <div class="visual-heading paper-heading"><h2>El prototipo también tiene<br>una historia de construcción.</h2><span class="visual-code">ANEXO I</span></div>
                <div class="workbench-layout">
                  <div class="workbench-main">{imagen("foto-desarrollo-opencode-laptop.jpg", "Desarrollo del prototipo desde un portátil")}</div>
                  <div class="workbench-side"><figure>{imagen("foto-github-repositorio.png", "Repositorio de BaseAccess en GitHub")}<figcaption>Control de versiones</figcaption></figure><figure>{imagen("foto-opencode.png", "Uso de OpenCode durante el desarrollo")}<figcaption>Asistencia técnica</figcaption></figure></div>
                </div>
                <p class="micro-caption">Diseñar · implementar · probar · corregir · documentar</p>
                """
            ),
            "Las fotografías funcionan como evidencia de proceso, no como decoración: diseño inicial, trabajo de desarrollo, repositorio y herramientas utilizadas.",
            clase="paper-slide workbench-slide",
            transicion="fade",
            etapa="validar",
        ),
        diapositiva(
            dedent(
                f"""
                <div class="kicker light-kicker">VALIDACIÓN DEL PROTOTIPO</div>
                <div class="claim-layout validation-claim">
                  <div class="claim-index">04</div>
                  <div><h2>La prueba no termina en “abre”.</h2><p class="lead light-lead">Termina cuando el dato puede registrarse, consultarse y volver a encontrarse.</p></div>
                </div>
                <div class="validation-grid"><div><b>REGISTRO</b><span>Campos y catálogos controlados.</span></div><div><b>HISTORIAL</b><span>Movimientos conservados.</span></div><div><b>SALIDA</b><span>Filtros y reportes exportables.</span></div></div>
                <div class="validation-line"><span>PRUEBAS FUNCIONALES</span><i></i><span>AJUSTES</span><i></i><span>PRESENTACIÓN</span></div>
                """
            ),
            "En la defensa, conectar la validación con las actividades de las semanas 7 a 9: pruebas funcionales, depuración, ajustes, manual y presentación del prototipo.",
            clase="dark-slide validation-slide",
            transicion="fade",
            etapa="validar",
        ),
        diapositiva(
            dedent(
                f"""
                <div class="kicker">RESULTADO</div>
                <div class="result-layout"><div><h2>El expediente deja de ser<br><span>una fila aislada.</span></h2><p class="lead">Se convierte en una historia que la oficina puede consultar y explicar.</p></div><div class="result-stamp"><strong>BASE<br>ACCESS</strong><span>PROTOTIPO<br>FUNCIONAL</span></div></div>
                <div class="result-grid"><div><b>REGISTRAR</b><span>Ingreso y egreso.</span></div><div><b>SEGUIR</b><span>Estados e historial.</span></div><div><b>REPORTAR</b><span>Resúmenes verificables.</span></div></div>
                <p class="closing-line">Una solución orientada a reducir tareas repetitivas y conservar el recorrido documental.</p>
                """
            ),
            "Cerrar la parte técnica con el aporte principal. No prometer una transformación total: presentar el prototipo como una solución viable y orientada a una necesidad concreta.",
            clase="paper-slide result-slide",
            transicion="zoom",
            etapa="validar",
        ),
        diapositiva(
            dedent(
                """
                <div class="closing-layout">
                  <div class="kicker">CIERRE</div>
                  <h2>Del control manual<br><span>a una trazabilidad defendible.</span></h2>
                  <p class="closing-copy">El siguiente paso no es agregar más pantallas: es llevar el prototipo al flujo cotidiano, capacitar al personal y proteger la información con respaldos.</p>
                  <div class="closing-signature"><strong>JULIANO CARDONA</strong><span>Desarrollo de un prototipo de sistema para el control, trazabilidad y reporte documental</span></div>
                </div>
                """
            ),
            "Agradecer y dejar tres ideas: el problema fue observado, la solución fue construida y el prototipo queda listo para seguir validándose en el contexto real.",
            clase="title-slide closing-slide",
            transicion="zoom",
            etapa="validar",
        ),
    ]


CSS = dedent(
    """
    :root {
      --wine: #8f1d2c;
      --wine-deep: #54131d;
      --rose: #f7dde1;
      --rose-soft: #fff7f8;
      --ink: #24171a;
      --paper: #fffdfb;
      --muted: #715d61;
      --gold: #d9a84d;
      --line: rgba(143, 29, 44, .24);
    }

    html, body { background: var(--paper); margin: 0; }
    .reveal {
      background: var(--paper);
      color: var(--ink);
      font-family: Arial, "Liberation Sans", sans-serif;
      font-size: 30px;
    }
    .reveal .slides section { box-sizing: border-box; height: 100%; text-align: left; }
    .slide-shell { display: grid; grid-template-columns: 7.4rem 1fr; height: 100%; min-height: 100%; }
    .slide-body { min-width: 0; overflow: hidden; padding: 5.7vh 6vw 5vh 5.2vw; position: relative; }
    .dossier-rail {
      background: var(--wine-deep);
      color: #fff7f8;
      display: flex;
      flex-direction: column;
      min-height: 100%;
      padding: 2rem 1rem 1.5rem;
      position: relative;
    }
    .rail-brand { font-size: .68em; font-weight: 900; letter-spacing: .14em; line-height: .9; }
    .rail-brand span { color: #e8b0b8; }
    .rail-rule { background: #c94f5d; height: 2px; margin: 1.7rem 0 1.25rem; width: 2rem; }
    .rail-steps { display: flex; flex-direction: column; gap: .95rem; }
    .rail-step { color: rgba(255, 247, 248, .48); display: flex; flex-direction: column; font-size: .32em; font-weight: 800; gap: .12rem; letter-spacing: .12em; line-height: 1.05; }
    .rail-step b { color: rgba(255, 247, 248, .42); font-size: 1.25em; }
    .rail-step.is-active { color: #fff; }
    .rail-step.is-active b { color: #f2b7be; }
    .rail-foot { bottom: 1.4rem; color: rgba(255, 247, 248, .55); font-size: .28em; font-weight: 800; letter-spacing: .12em; line-height: 1.4; position: absolute; }
    .rail-foot span { color: #f2b7be; }
    .kicker { color: var(--wine); font-size: .43em; font-weight: 900; letter-spacing: .22em; margin-bottom: 1.5em; text-transform: uppercase; }
    .light-kicker { color: #f2b7be; }
    h1, h2, p { margin: 0; }
    h1, h2 { font-weight: 900; letter-spacing: -.045em; line-height: .96; }
    h1 { font-size: 3.2em; max-width: 10em; }
    h1 span, h2 span, h2 em { color: var(--wine); font-style: normal; }
    h2 { font-size: 1.75em; max-width: 18em; }
    .lead { color: var(--muted); font-size: .73em; line-height: 1.35; margin-top: 1.3em; max-width: 26em; }
    .dark-slide, .wine-slide { color: #fff7f8; }
    .dark-slide h2, .wine-slide h2, .dark-slide .lead, .wine-slide .lead { color: #fff7f8; }
    .dark-slide h2 em, .wine-slide h2 em { color: #f2b7be; }
    .dark-slide { background: #24171a; }
    .wine-slide { background: var(--wine); }
    .paper-slide { background: var(--paper); }
    .title-slide { background: radial-gradient(circle at 78% 20%, rgba(217, 168, 77, .22), transparent 24%), var(--rose-soft); }
    .title-layout { align-items: center; display: grid; gap: 5vw; grid-template-columns: minmax(0, 1fr) minmax(13rem, 20rem); height: 100%; }
    .title-subtitle { color: var(--muted); font-size: .7em; line-height: 1.35; margin-top: 1.4em; max-width: 25em; }
    .author-line { border-top: 1px solid var(--line); color: var(--muted); display: flex; flex-wrap: wrap; font-size: .38em; font-weight: 800; gap: 1.4em; letter-spacing: .13em; margin-top: 3.2em; padding-top: 1em; }
    .author-line strong { color: var(--wine); }
    .hero-seal { align-items: center; border: 1px solid var(--wine); color: var(--wine); display: flex; flex-direction: column; justify-content: center; min-height: 18rem; padding: 1.5rem; position: relative; text-align: center; }
    .hero-seal::before, .hero-seal::after { border: 1px solid var(--wine); content: ""; inset: .45rem; pointer-events: none; position: absolute; }
    .hero-seal::after { inset: .72rem; opacity: .25; }
    .seal-label, .visual-code { font-size: .36em; font-weight: 900; letter-spacing: .19em; }
    .seal-track { display: flex; flex-direction: column; gap: .5rem; margin: 1rem 0; }
    .seal-track i { background: var(--wine); border-radius: 50%; display: block; height: .55rem; position: relative; width: .55rem; }
    .seal-track i:not(:last-child)::after { background: var(--wine); content: ""; height: .5rem; left: .22rem; opacity: .4; position: absolute; top: .55rem; width: 1px; }
    .hero-seal strong { font-size: .5em; letter-spacing: .16em; line-height: 1.5; }
    .hero-seal small { color: var(--muted); font-size: .38em; line-height: 1.35; margin-top: 1rem; }
    .claim-layout { align-items: center; display: grid; gap: 2.5vw; grid-template-columns: 6rem minmax(0, 1fr); margin-top: 9vh; }
    .claim-index { color: var(--wine); font-family: "Arial Narrow", Arial, sans-serif; font-size: 4.6em; font-weight: 900; letter-spacing: -.1em; line-height: .8; }
    .question-strip { display: flex; flex-wrap: wrap; gap: .7em; margin-top: 2em; }
    .question-strip span, .three-labels span, .promise-row span, .operations-footer span { border-bottom: 2px solid var(--wine); color: var(--wine); font-size: .4em; font-weight: 900; letter-spacing: .14em; padding-bottom: .45em; }
    .bottom-note { border-top: 1px solid var(--line); bottom: 5vh; color: var(--muted); display: flex; font-size: .46em; gap: 1.2em; left: 5.2vw; line-height: 1.3; padding-top: .8em; position: absolute; right: 6vw; }
    .bottom-note b { color: var(--wine); flex: 0 0 auto; letter-spacing: .05em; }
    .visual-heading { align-items: end; display: flex; gap: 2em; justify-content: space-between; }
    .paper-heading h2 { color: var(--ink); }
    .visual-code { color: inherit; opacity: .68; white-space: nowrap; }
    .large-diagram { align-items: center; display: flex; justify-content: center; margin: 1.5vh auto 1vh; min-height: 0; }
    .large-diagram img { background: #fff; border: 1px solid rgba(255,255,255,.35); max-height: 62vh; max-width: 82vw; object-fit: contain; padding: .4rem; }
    .wine-slide .large-diagram img { border-color: rgba(255,255,255,.55); }
    .three-labels, .promise-row, .operations-footer { display: flex; flex-wrap: wrap; gap: 1.4em; }
    .dark-slide .three-labels span, .wine-slide .promise-row span, .operations-footer span { border-color: #f2b7be; color: #fff7f8; }
    .promise-row { justify-content: space-between; margin-top: .5em; }
    .promise-row span { border: 0; font-size: .4em; padding: 0; }
    .promise-row b { color: #f2b7be; display: block; font-size: 1.15em; letter-spacing: .12em; }
    .interface-layout { align-items: center; display: grid; gap: 4vw; grid-template-columns: minmax(0, 1.6fr) minmax(12rem, .8fr); margin-top: 4vh; }
    .interface-shot img { border: 1px solid var(--line); box-shadow: 10px 10px 0 var(--rose); display: block; max-height: 55vh; max-width: 100%; object-fit: contain; }
    .proof-list { display: flex; flex-direction: column; gap: 1.2rem; }
    .proof-list div { border-top: 1px solid var(--line); display: grid; gap: .7em; grid-template-columns: 2.3em 1fr; padding-top: .8em; }
    .proof-list b { color: var(--wine); font-size: .48em; }
    .proof-list span { color: var(--muted); font-size: .52em; line-height: 1.35; }
    .architecture-layout { align-items: center; display: grid; gap: 4vw; grid-template-columns: minmax(0, 1fr) minmax(10rem, .7fr); margin-top: 5vh; }
    .architecture-shot img { background: #fff; border: 1px solid rgba(255,255,255,.5); max-width: 100%; padding: 1rem; }
    .layer-stack { display: flex; flex-direction: column; gap: .8rem; }
    .layer-stack span { border-left: 3px solid #f2b7be; color: rgba(255,247,248,.72); display: flex; flex-direction: column; font-size: .5em; gap: .2em; padding: .55em .8em; }
    .layer-stack b { color: #fff; letter-spacing: .12em; }
    .dark-caption, .micro-caption { color: var(--muted); font-size: .43em; letter-spacing: .05em; margin-top: 1.3em; }
    .dark-caption { color: rgba(255,247,248,.65); }
    .pseudo-layout { align-items: center; display: grid; gap: 3vw; grid-template-columns: minmax(0, 1fr) minmax(11rem, .45fr); margin-top: 2.5vh; }
    .pseudo-shot { align-items: center; display: flex; justify-content: center; }
    .pseudo-shot img { border: 1px solid var(--line); max-height: 62vh; max-width: 100%; object-fit: contain; }
    .pseudo-note { border-left: 3px solid var(--wine); display: flex; flex-direction: column; gap: .35em; padding-left: 1em; }
    .pseudo-note b { color: var(--wine); font-size: .4em; letter-spacing: .15em; }
    .pseudo-note span { color: var(--muted); font-size: .5em; line-height: 1.3; margin-bottom: .9em; }
    .evidence-grid { display: grid; gap: 1.1em; grid-template-columns: repeat(3, 1fr); margin-top: 5vh; }
    figure { margin: 0; }
    .evidence-grid figure { border-top: 3px solid var(--wine); padding-top: .7em; }
    .evidence-grid img { display: block; height: 29vh; max-width: 100%; object-fit: contain; width: 100%; }
    figcaption { color: var(--muted); font-size: .4em; font-weight: 800; letter-spacing: .06em; margin-top: .8em; }
    .operations-layout { align-items: center; display: grid; gap: 2vw; grid-template-columns: 1.5fr 1fr; margin-top: 4vh; }
    .operation-shot { background: #fff; border: 1px solid rgba(255,255,255,.52); padding: .45rem; }
    .operation-shot img { display: block; height: 34vh; max-width: 100%; object-fit: contain; width: 100%; }
    .wide-shot img { height: 21vh; }
    .operations-footer { justify-content: space-between; margin-top: 1em; }
    .operations-footer span { border: 0; font-size: .4em; padding: 0; }
    .workbench-layout { display: grid; gap: 1.1em; grid-template-columns: 1.45fr .8fr; margin-top: 4vh; }
    .workbench-main img { display: block; height: 46vh; max-width: 100%; object-fit: cover; width: 100%; }
    .workbench-side { display: grid; gap: 1.1em; grid-template-rows: 1fr 1fr; }
    .workbench-side figure { border-left: 3px solid var(--wine); padding-left: .7em; }
    .workbench-side img { display: block; height: 20vh; max-width: 100%; object-fit: contain; width: 100%; }
    .validation-claim { margin-top: 5vh; }
    .light-lead { color: rgba(255,247,248,.76); }
    .validation-grid { display: grid; gap: 1.3em; grid-template-columns: repeat(3, 1fr); margin-top: 7vh; }
    .validation-grid div { border-top: 2px solid #f2b7be; display: flex; flex-direction: column; gap: .45em; padding-top: .8em; }
    .validation-grid b { color: #f2b7be; font-size: .44em; letter-spacing: .13em; }
    .validation-grid span { color: rgba(255,247,248,.78); font-size: .53em; line-height: 1.3; }
    .validation-line { align-items: center; color: #f2b7be; display: flex; font-size: .38em; font-weight: 800; gap: 1em; letter-spacing: .14em; margin-top: 7vh; }
    .validation-line i { background: #f2b7be; height: 1px; opacity: .6; width: 3rem; }
    .result-layout { align-items: center; display: grid; gap: 4vw; grid-template-columns: 1fr 13rem; margin-top: 9vh; }
    .result-stamp { align-items: center; border: 1px solid var(--wine); color: var(--wine); display: flex; flex-direction: column; gap: .8em; justify-content: center; min-height: 10rem; padding: 1rem; text-align: center; transform: rotate(3deg); }
    .result-stamp strong { font-size: .7em; letter-spacing: .12em; line-height: .95; }
    .result-stamp span { border-top: 1px solid var(--wine); font-size: .34em; font-weight: 900; letter-spacing: .13em; padding-top: .65em; }
    .result-grid { display: grid; gap: 1.2em; grid-template-columns: repeat(3, 1fr); margin-top: 6vh; max-width: 30em; }
    .result-grid div { background: var(--rose); border-top: 4px solid var(--wine); display: flex; flex-direction: column; gap: .35em; padding: .8em; }
    .result-grid b { color: var(--wine); font-size: .48em; letter-spacing: .14em; }
    .result-grid span { color: var(--muted); font-size: .5em; }
    .closing-line { color: var(--wine); font-size: .65em; font-weight: 800; margin-top: 2em; max-width: 27em; }
    .closing-slide .slide-body { background: linear-gradient(135deg, var(--rose-soft), #fff); }
    .closing-layout { align-self: center; max-width: 48rem; }
    .closing-layout h2 { font-size: 2.5em; }
    .closing-layout h2 span { color: var(--wine); }
    .closing-copy { color: var(--muted); font-size: .7em; line-height: 1.4; margin-top: 1.5em; max-width: 27em; }
    .closing-signature { border-top: 1px solid var(--line); display: flex; flex-direction: column; font-size: .4em; gap: .5em; margin-top: 4em; padding-top: 1em; }
    .closing-signature strong { color: var(--wine); letter-spacing: .14em; }
    .closing-signature span { color: var(--muted); max-width: 37em; }
    .reveal .progress { color: var(--wine); }
    .reveal .slide-number { background: transparent; color: var(--muted); }
    .reveal .controls { color: var(--wine); }

    @media (max-width: 700px) {
      .reveal { font-size: 23px; }
      .slide-shell { grid-template-columns: 1fr; grid-template-rows: 4.2rem 1fr; }
      .dossier-rail { align-items: center; flex-direction: row; min-height: 0; padding: .7rem 1rem; }
      .rail-brand { font-size: .5em; line-height: .9; }
      .rail-rule { height: 1.4rem; margin: 0 .8rem; width: 1px; }
      .rail-steps { flex: 1; flex-direction: row; justify-content: space-between; }
      .rail-step { align-items: center; font-size: .26em; text-align: center; }
      .rail-foot { display: none; }
      .slide-body { padding: 7vh 7vw 5vh; }
      h1 { font-size: 2.45em; }
      h2 { font-size: 1.45em; }
      .title-layout, .interface-layout, .architecture-layout, .pseudo-layout, .workbench-layout, .result-layout { display: flex; flex-direction: column; gap: 1.2rem; justify-content: center; }
      .hero-seal { min-height: 9rem; width: 8rem; }
      .title-subtitle { font-size: .62em; }
      .author-line { font-size: .31em; margin-top: 1.7em; }
      .claim-layout { gap: 1rem; grid-template-columns: 3.5rem 1fr; margin-top: 4vh; }
      .claim-index { font-size: 3.6em; }
      .question-strip { gap: .45em; margin-top: 1.2em; }
      .bottom-note { bottom: 3vh; display: block; font-size: .4em; }
      .bottom-note span { display: block; margin-top: .4em; }
      .visual-heading { align-items: start; flex-direction: column; gap: .6em; }
      .large-diagram { margin-top: 2vh; }
      .large-diagram img { max-height: 53vh; max-width: 86vw; }
      .interface-shot img { max-height: 41vh; }
      .proof-list { gap: .55rem; }
      .proof-list div { padding-top: .45em; }
      .architecture-shot img { max-height: 18vh; }
      .pseudo-shot img { max-height: 43vh; }
      .evidence-grid { gap: .5em; margin-top: 2vh; }
      .evidence-grid img { height: 21vh; }
      .operations-layout { gap: .6em; grid-template-columns: 1fr; margin-top: 2vh; }
      .operation-shot img, .wide-shot img { height: 22vh; }
      .workbench-main img { height: 27vh; }
      .workbench-side { display: flex; gap: .6em; }
      .workbench-side img { height: 14vh; }
      .validation-grid, .result-grid { gap: .6em; grid-template-columns: 1fr; margin-top: 3vh; }
      .validation-line { flex-wrap: wrap; margin-top: 3vh; }
      .result-stamp { min-height: 6rem; width: 7rem; }
      .closing-layout h2 { font-size: 2em; }
    }

    @media (prefers-reduced-motion: reduce) {
      .reveal .slides section, .reveal .fragment { transition: none !important; }
    }
    """
)


def construir_html():
    imagenes_requeridas = {
        "02_flujo_as_is_presidencia.png",
        "03_flujo_to_be_sistema_automatizado.png",
        "05_pseudocodigo_general_baseaccess.png",
        "06_arquitectura_prototipo.png",
        "captura-registro-nuevo-contexto.png",
        "captura-formulario-general.png",
        "captura-expedientes-frentes.png",
        "captura-catalogos-validaciones.png",
        "captura-ruta-seleccion-multiple.png",
        "captura-exportacion-filtros-columnas.png",
        "foto-desarrollo-opencode-laptop.jpg",
        "foto-github-repositorio.png",
        "foto-opencode.png",
    }
    faltantes = sorted(nombre for nombre in imagenes_requeridas if not (CARPETA_IMAGENES / nombre).is_file())
    if faltantes:
        raise FileNotFoundError(f"No se encontraron imágenes de Juliano: {', '.join(faltantes)}")

    contenido = "\n".join(construir_diapositivas())
    return dedent(
        """
        <!doctype html>
        <html lang="es">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <meta name="theme-color" content="#8f1d2c">
          <title>Del expediente al dato trazable | Juliano Cardona</title>
          <link rel="preconnect" href="https://cdn.jsdelivr.net">
          <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css">
          <style>
        """
    ) + CSS + dedent(
        f"""
          </style>
        </head>
        <body>
          <div class="reveal">
            <div class="slides">
        {contenido}
            </div>
          </div>
          <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
          <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/notes/notes.js"></script>
          <script>
            const vistaMovil = window.innerWidth < 700;
            Reveal.initialize({{
              hash: true,
              controls: true,
              progress: true,
              slideNumber: "c/t",
              center: false,
              width: vistaMovil ? 390 : 1280,
              height: vistaMovil ? 844 : 720,
              margin: vistaMovil ? 0.04 : 0.03,
              minScale: 0.2,
              maxScale: 2.0,
              transition: "fade",
              backgroundTransition: "fade",
              plugins: [RevealNotes]
            }});
          </script>
        </body>
        </html>
        """
    )


def main():
    SALIDA.write_text(construir_html(), encoding="utf-8")
    print(f"Presentación generada en: {SALIDA} ({len(construir_diapositivas())} diapositivas)")


if __name__ == "__main__":
    main()
