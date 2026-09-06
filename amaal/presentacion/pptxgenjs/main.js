const path = require("path");
const pptxgen = require("pptxgenjs");

const CARPETA = __dirname;
const CARPETA_AMAAL = path.resolve(CARPETA, "../..");
const SALIDA = path.join(CARPETA, "Defensa_Amaal_10_laminas.pptx");
const SALIDA_PUBLICA = path.resolve(CARPETA, "..", "Defensa_Amaal_10_laminas.pptx");

const pptx = new pptxgen();

pptx.layout = "LAYOUT_WIDE";
pptx.author = "Amaal Alrifaai Alrifaaie";
pptx.subject = "Defensa de Pasantías Profesionales";
pptx.title =
"Evaluación del control administrativo aplicado a la gestión de solicitudes de servicios de telecomunicaciones";
pptx.company = "IUTECP";
pptx.lang = "es-VE";

pptx.theme = {
    headFontFace: "Aptos Display",
    bodyFontFace: "Aptos",
    lang: "es-VE"
};

pptx.defineSlideMaster({
    title: "MASTER",
    background: { color: "FCFBFE" },
    objects: [
        {
            line: {
                x: 0.65,
                y: 0.42,
                w: 12.0,
                h: 0,
                line: {
                    color: "5B2A86",
                    width: 3
                }
            }
        },
        {
            text: {
                text: "DEFENSA DE PASANTÍAS · AMAAL ALRIFAAI ALRIFAAIE",
                options: {
                    x: 0.7,
                    y: 0.12,
                    w: 6.5,
                    h: 0.2,
                    fontFace: "Aptos",
                    fontSize: 8,
                    bold: true,
                    color: "6D6373",
                    charSpacing: 1
                }
            }
        }
    ],
    slideNumber: {
        x: 12.25,
        y: 7.05,
        w: 0.35,
        h: 0.2,
        fontFace: "Aptos",
        fontSize: 8,
        color: "5B2A86",
        align: "right"
    }
});

const C = {
    purple: "5B2A86",
    violet: "9B6BC4",
    lavender: "EDE3F7",
    paper: "FCFBFE",
    ink: "24182D",
    muted: "6D6373",
    line: "D9C7E8",
    white: "FFFFFF",
    navy: "080452"
};

const IMG = {
    logo: path.join(CARPETA_AMAAL, "imagenes", "logo.jpg"),
    ishikawa: path.join(CARPETA_AMAAL, "imagenes", "ishikawa_amaal_solicitudes.png"),
    swimlane: path.join(CARPETA_AMAAL, "imagenes", "04_swimlane_gestion_solicitudes.png")
};

function addChapter(slide, text) {
    slide.addText(text.toUpperCase(), {
        x: 0.72,
        y: 0.58,
        w: 7.2,
        h: 0.28,
        fontFace: "Aptos",
        fontSize: 11,
        bold: true,
        color: C.purple,
        charSpacing: 1.3,
        margin: 0
    });
}

function addTitle(slide, text, y = 0.95, size = 27) {
    slide.addText(text, {
        x: 0.72,
        y,
        w: 11.8,
        h: 0.72,
        fontFace: "Aptos Display",
        fontSize: size,
        bold: true,
        color: C.ink,
        margin: 0,
        breakLine: false
    });
}

function addCard(slide, x, y, w, h, title, body, options = {}) {
    slide.addShape(pptx.ShapeType.rect, {
        x,
        y,
        w,
        h,
        fill: { color: options.fill || C.white },
        line: { color: options.line || C.line, width: 1 }
    });

    slide.addShape(pptx.ShapeType.rect, {
        x,
        y,
        w: 0.07,
        h,
        fill: { color: options.accent || C.purple },
        line: { color: options.accent || C.purple }
    });

    slide.addText(title, {
        x: x + 0.2,
        y: y + 0.16,
        w: w - 0.35,
        h: 0.32,
        fontFace: "Aptos",
        fontSize: options.titleSize || 15,
        bold: true,
        color: options.titleColor || C.purple,
        margin: 0
    });

    if (body) {
        slide.addText(body, {
            x: x + 0.2,
            y: y + 0.55,
            w: w - 0.35,
            h: h - 0.68,
            fontFace: "Aptos",
            fontSize: options.bodySize || 11,
            color: options.bodyColor || C.muted,
            margin: 0,
            valign: "mid",
            breakLine: false
        });
    }
}

function addSimpleBox(slide, x, y, w, h, text) {
    slide.addShape(pptx.ShapeType.rect, {
        x,
        y,
        w,
        h,
        fill: { color: C.lavender },
        line: { color: C.lavender }
    });

    slide.addText(text, {
        x: x + 0.12,
        y: y + 0.12,
        w: w - 0.24,
        h: h - 0.24,
        fontFace: "Aptos",
        fontSize: 14,
        bold: true,
        color: C.purple,
        align: "center",
        valign: "mid",
        margin: 0
    });
}

//
// 1. PORTADA
//
{
    const slide = pptx.addSlide();

    slide.background = { color: C.paper };

    slide.addShape(pptx.ShapeType.rect, {
        x: 8.4,
        y: 0,
        w: 4.93,
        h: 7.5,
        fill: { color: C.lavender },
        line: { color: C.lavender }
    });

    slide.addText("DEFENSA DE PASANTÍAS PROFESIONALES", {
        x: 0.75,
        y: 1.05,
        w: 5.8,
        h: 0.35,
        fontFace: "Aptos",
        fontSize: 12,
        bold: true,
        color: C.purple,
        charSpacing: 1.5,
        margin: 0
    });

    slide.addText(
        "Evaluación del control administrativo aplicado a la gestión de solicitudes de servicios de telecomunicaciones en la empresa Ingeniería de Telecomunicaciones, C.A.",
        {
            x: 0.75,
            y: 1.55,
            w: 7.1,
            h: 3.15,
            fontFace: "Aptos Display",
            fontSize: 26,
            bold: true,
            color: C.ink,
            margin: 0,
            valign: "mid",
            breakLine: false
        }
    );

    slide.addText("Amaal Alrifaai Alrifaaie", {
        x: 0.75,
        y: 5.5,
        w: 5.8,
        h: 0.4,
        fontFace: "Aptos",
        fontSize: 20,
        bold: true,
        color: C.purple,
        margin: 0
    });

    slide.addText("Administración · IUTECP · 2026", {
        x: 0.75,
        y: 6.0,
        w: 5.8,
        h: 0.3,
        fontFace: "Aptos",
        fontSize: 13,
        color: C.muted,
        margin: 0
    });

    slide.addShape(pptx.ShapeType.rect, {
        x: 9.2,
        y: 1.2,
        w: 3.3,
        h: 4.9,
        fill: { color: C.white },
        line: { color: C.line, width: 1 }
    });

    slide.addImage({
        path: IMG.logo,
        x: 10.0,
        y: 1.55,
        w: 1.7,
        h: 1.7
    });

    slide.addText("CASO", {
        x: 9.55,
        y: 3.55,
        w: 2.6,
        h: 0.2,
        fontSize: 9,
        bold: true,
        color: C.muted,
        charSpacing: 1
    });

    slide.addText("Solicitud de servicio", {
        x: 9.55,
        y: 3.82,
        w: 2.6,
        h: 0.35,
        fontSize: 16,
        bold: true,
        color: C.ink
    });

    slide.addText("RECORRIDO", {
        x: 9.55,
        y: 4.45,
        w: 2.6,
        h: 0.2,
        fontSize: 9,
        bold: true,
        color: C.muted,
        charSpacing: 1
    });

    slide.addText("Recepción → cierre", {
        x: 9.55,
        y: 4.72,
        w: 2.6,
        h: 0.35,
        fontSize: 16,
        bold: true,
        color: C.ink
    });

    slide.addText("PROPUESTA FORMULADA", {
        x: 9.55,
        y: 5.45,
        w: 2.6,
        h: 0.42,
        fontSize: 12,
        bold: true,
        color: C.purple,
        fill: { color: C.lavender },
        align: "center",
        valign: "mid",
        margin: 0.08
    });

    slide.addNotes(
        "Saludar al jurado y presentar a Amaal Alrifaai Alrifaaie, estudiante de Administración del IUTECP. " +
        "Leer el título oficial e indicar que las pasantías se realizaron en IDETEL. Explicar que la defensa " +
        "seguirá la secuencia de los cinco capítulos del informe."
    );
}

//
// 2. AGENDA
//
{
    const slide = pptx.addSlide("MASTER");

    addChapter(slide, "Agenda");
    addTitle(slide, "Estructura de la socialización");

    const items = [
        ["CAPÍTULO I", "Realidad Organizacional"],
        ["CAPÍTULO II", "Diagnóstico Situacional"],
        ["CAPÍTULO III", "Marco Teórico"],
        ["CAPÍTULO IV", "Actividades Realizadas"],
        ["CAPÍTULO V", "Conclusiones y Recomendaciones"]
    ];

    const x0 = 0.7;
    const gap = 0.15;
    const w = 2.36;

    items.forEach((item, i) => {
        const x = x0 + i * (w + gap);

        slide.addShape(pptx.ShapeType.rect, {
            x,
            y: 2.75,
            w,
            h: 2.5,
            fill: { color: C.lavender },
            line: { color: C.line }
        });

        slide.addShape(pptx.ShapeType.rect, {
            x,
            y: 2.75,
            w,
            h: 0.08,
            fill: { color: C.purple },
            line: { color: C.purple }
        });

        slide.addText(item[0], {
            x: x + 0.16,
            y: 3.12,
            w: w - 0.32,
            h: 0.3,
            fontSize: 10,
            bold: true,
            color: C.violet,
            align: "center",
            margin: 0
        });

        slide.addText(item[1], {
            x: x + 0.18,
            y: 3.6,
            w: w - 0.36,
            h: 1.0,
            fontSize: 16,
            bold: true,
            color: C.ink,
            align: "center",
            valign: "mid",
            margin: 0
        });
    });

    slide.addNotes(
        "Explicar brevemente la agenda. La presentación seguirá la misma secuencia de los cinco capítulos: " +
        "realidad organizacional, diagnóstico situacional, marco teórico, actividades realizadas y " +
        "conclusiones y recomendaciones."
    );
}

//
// 3. CAPÍTULO I
//
{
    const slide = pptx.addSlide("MASTER");

    addChapter(slide, "Capítulo I · Realidad Organizacional");
    addTitle(slide, "Empresa y área de pasantía");

    slide.addShape(pptx.ShapeType.rect, {
        x: 0.8,
        y: 2.2,
        w: 3.7,
        h: 3.9,
        fill: { color: C.navy },
        line: { color: C.navy }
    });

    slide.addImage({
        path: IMG.logo,
        x: 1.75,
        y: 3.15,
        w: 1.8,
        h: 1.8
    });

    const facts = [
        ["EMPRESA", "Ingeniería de Telecomunicaciones, C.A."],
        ["SECTOR", "Telecomunicaciones y automatización"],
        ["SEDE", "El Tigre, estado Anzoátegui"],
        ["ÁREA", "Atención al Cliente · Semanas 1–3"],
        ["ÁREA", "Administración · Semanas 4–10"]
    ];

    facts.forEach((f, i) => {
        addCard(
            slide,
            4.8,
            2.1 + i * 0.88,
            7.5,
            0.72,
            f[0],
            f[1],
            {
                titleSize: 9,
                bodySize: 14,
                fill: i % 2 === 0 ? "FFFFFF" : "F7F2FB"
            }
        );
    });

    slide.addNotes(
        "Presentar a IDETEL como una empresa ubicada en El Tigre con más de cuatro décadas de experiencia " +
        "en telecomunicaciones y automatización. Explicar la rotación: Atención al Cliente durante las " +
        "semanas 1 a 3 y Administración desde la semana 4 hasta la 10. Mencionar recepción, pagos, " +
        "facturación, documentos, seguimiento y reportes."
    );
}

//
// 4. CAPÍTULO II — PROBLEMA + OBJETIVOS
//
{
    const slide = pptx.addSlide("MASTER");

    addChapter(slide, "Capítulo II · Diagnóstico Situacional");
    addTitle(slide, "Situación problemática y objetivos");

    slide.addShape(pptx.ShapeType.rect, {
        x: 0.75,
        y: 2.0,
        w: 11.85,
        h: 0.85,
        fill: { color: C.purple },
        line: { color: C.purple }
    });

    slide.addText(
        "No existía un procedimiento único y formalizado para seguir las solicitudes desde su recepción hasta el cierre.",
        {
            x: 1.0,
            y: 2.2,
            w: 11.3,
            h: 0.42,
            fontSize: 18,
            bold: true,
            color: C.white,
            align: "center",
            valign: "mid",
            margin: 0
        }
    );

    [
        "Formatos no uniformes",
        "Estatus distribuido",
        "Sin tiempos de referencia",
        "Comunicación fragmentada"
    ].forEach((text, i) => {
        addSimpleBox(slide, 0.75 + i * 3.0, 3.2, 2.75, 0.75, text);
    });

    slide.addText(
        "¿Cómo puede evaluarse el control administrativo para identificar debilidades y fortalecer la trazabilidad y el seguimiento?",
        {
            x: 0.95,
            y: 4.2,
            w: 11.5,
            h: 0.65,
            fontSize: 14,
            bold: true,
            italic: true,
            color: C.purple,
            align: "center",
            valign: "mid",
            margin: 0
        }
    );

    const objectives = [
        ["01", "Diagnosticar", "recorrido actual"],
        ["02", "Identificar", "deficiencias y causas"],
        ["03", "Formular", "mejoras procedimentales"]
    ];

    objectives.forEach((o, i) => {
        addCard(
            slide,
            1.05 + i * 4.05,
            5.25,
            3.65,
            1.25,
            `${o[0]} · ${o[1]}`,
            o[2],
            {
                titleSize: 17,
                bodySize: 12
            }
        );
    });

    slide.addNotes(
        "Explicar que la empresa atendía las solicitudes, pero no contaba con un procedimiento único y " +
        "formalizado desde la recepción hasta el cierre. Mencionar las cuatro manifestaciones: formatos " +
        "no uniformes, estatus distribuido, falta de tiempos de referencia y comunicación fragmentada. " +
        "Leer la interrogante y presentar los objetivos en orden: diagnosticar, identificar y formular."
    );
}

//
// 5. CAPÍTULO II — ISHIKAWA
//
{
    const slide = pptx.addSlide("MASTER");

    addChapter(slide, "Capítulo II · Técnica de Diagnóstico");
    addTitle(slide, "Diagrama de Ishikawa");

    const methods = [
        "Observación directa",
        "Revisión de registros",
        "Entrevistas al personal",
        "Diagrama de Ishikawa"
    ];

    methods.forEach((m, i) => {
        addSimpleBox(slide, 0.75, 2.1 + i * 0.82, 3.25, 0.62, m);
    });

    slide.addImage({
        path: IMG.ishikawa,
        x: 4.35,
        y: 1.9,
        w: 8.15,
        h: 4.15
    });

    slide.addShape(pptx.ShapeType.rect, {
        x: 0.8,
        y: 5.9,
        w: 11.65,
        h: 0.7,
        fill: { color: C.purple },
        line: { color: C.purple }
    });

    slide.addText(
        "Hallazgo central: el problema no era recibir la solicitud, sino mantener visible su continuidad hasta el cierre.",
        {
            x: 1.0,
            y: 6.09,
            w: 11.25,
            h: 0.34,
            fontSize: 15,
            bold: true,
            color: C.white,
            align: "center",
            margin: 0
        }
    );

    slide.addNotes(
        "Explicar que el diagnóstico combinó observación, revisión de registros, entrevistas y el Ishikawa. " +
        "Señalar las cuatro dimensiones: procedimiento, comunicación, registro y seguimiento. Cerrar con " +
        "el hallazgo central: el problema no era recibir la solicitud, sino mantener visible su continuidad " +
        "hasta el cierre."
    );
}

//
// 6. CAPÍTULO III
//
{
    const slide = pptx.addSlide("MASTER");

    addChapter(slide, "Capítulo III · Marco Teórico");
    addTitle(slide, "Conceptos disciplinares y bases legales");

    const concepts = [
        ["Control administrativo", "Verificar el proceso y corregir desviaciones."],
        ["Gestión de solicitudes", "Recibir, registrar, procesar, seguir y cerrar."],
        ["Trazabilidad administrativa", "Reconstruir el recorrido completo de un caso."],
        ["Estandarización", "Aplicar criterios, estados y formatos comunes."]
    ];

    concepts.forEach((c, i) => {
        const x = i % 2 === 0 ? 0.8 : 6.7;
        const y = i < 2 ? 2.05 : 3.55;

        addCard(slide, x, y, 5.65, 1.18, c[0], c[1], {
            titleSize: 15,
            bodySize: 11
        });
    });

    addCard(
        slide,
        0.8,
        5.35,
        5.65,
        1.0,
        "Constitución · Artículo 112",
        "Marco general de la actividad económica.",
        { titleSize: 13, bodySize: 10, fill: C.lavender }
    );

    addCard(
        slide,
        6.7,
        5.35,
        5.65,
        1.0,
        "Código de Comercio · Artículo 32",
        "Orden y claridad de los registros.",
        { titleSize: 13, bodySize: 10, fill: C.lavender }
    );

    slide.addNotes(
        "Explicar solamente los cuatro conceptos más relevantes: control administrativo, gestión de " +
        "solicitudes, trazabilidad administrativa y estandarización de procedimientos. Mencionar brevemente " +
        "el artículo 112 de la Constitución y el artículo 32 del Código de Comercio como bases legales."
    );
}

//
// 7. CAPÍTULO IV — ACTIVIDADES
//
{
    const slide = pptx.addSlide("MASTER");

    addChapter(slide, "Capítulo IV · Actividades Realizadas");
    addTitle(slide, "Cuatro actividades principales");

    const activities = [
        ["SEM. 1–3", "Observar el recorrido", "Atención al Cliente y Administración."],
        ["SEM. 4", "Revisar y entrevistar", "Registros, personal e identificación de fallas."],
        ["SEM. 5", "Elaborar el Ishikawa", "Organización de causas relacionadas."],
        ["SEM. 7–9", "Diseñar y validar", "Flujo, formatos, responsables e indicadores."]
    ];

    activities.forEach((a, i) => {
        const x = i % 2 === 0 ? 0.85 : 6.75;
        const y = i < 2 ? 2.45 : 4.5;

        addCard(
            slide,
            x,
            y,
            5.55,
            1.55,
            `${a[0]} · ${a[1]}`,
            a[2],
            {
                titleSize: 16,
                bodySize: 12
            }
        );
    });

    slide.addNotes(
        "No explicar las diez semanas una por una. Resumirlas en cuatro actividades principales: observar " +
        "el recorrido, revisar registros y entrevistar, elaborar el Ishikawa, y diseñar y validar mejoras. " +
        "Mencionar también el apoyo en pagos, facturación, documentación, seguimiento y reportes."
    );
}

//
// 8. CAPÍTULO IV — PROPUESTA
//
{
    const slide = pptx.addSlide("MASTER");

    addChapter(slide, "Capítulo IV · Propuesta de Mejora");
    addTitle(slide, "Un procedimiento visible de principio a fin");

    const proposal = [
        "Flujo estandarizado",
        "Responsables por etapa",
        "Formatos uniformes",
        "Estados definidos",
        "Tiempos de referencia",
        "Indicadores básicos"
    ];

    proposal.forEach((p, i) => {
        const col = i % 3;
        const row = Math.floor(i / 3);

        addSimpleBox(
            slide,
            0.75 + col * 4.08,
            1.75 + row * 1.05,
            3.78,
            0.78,
            p
        );
    });

    slide.addImage({
        path: IMG.swimlane,
        x: 1.15,
        y: 4.0,
        w: 11.0,
        h: 1.75
    });

    slide.addText(
        "Recibida → Registrada → Asignada → En atención → Resuelta → Cerrada",
        {
            x: 1.0,
            y: 5.9,
            w: 11.35,
            h: 0.3,
            fontSize: 12,
            bold: true,
            color: C.purple,
            align: "center",
            margin: 0
        }
    );

    slide.addText("Resuelta ≠ Cerrada", {
        x: 4.95,
        y: 6.3,
        w: 3.4,
        h: 0.32,
        fontSize: 15,
        bold: true,
        color: C.violet,
        align: "center",
        margin: 0
    });

    slide.addNotes(
        "Presentar los seis componentes de la propuesta y señalar el flujo. Explicar que cada transferencia " +
        "deja un responsable y un estado visible. Diferenciar resuelta de cerrada: el cierre exige confirmar " +
        "y registrar el resultado. Primero se organiza y valida el procedimiento; después se evalúa una " +
        "herramienta digital."
    );
}

//
// 9. CAPÍTULO V — CONCLUSIONES Y RECOMENDACIONES
//
{
    const slide = pptx.addSlide("MASTER");

    addChapter(slide, "Capítulo V · Conclusiones y Recomendaciones");
    addTitle(slide, "Resultados principales");

    const conclusions = [
        [
            "1 · DIAGNÓSTICO",
            "El recorrido existía, pero no estaba formalizado como un solo proceso."
        ],
        [
            "2 · DEFICIENCIAS",
            "Formatos, estatus, tiempos y comunicación afectaban la trazabilidad."
        ],
        [
            "3 · APORTE",
            "Flujo, responsables, formatos e indicadores permiten fortalecer el control."
        ]
    ];

    conclusions.forEach((c, i) => {
        addCard(
            slide,
            0.75 + i * 4.08,
            2.0,
            3.78,
            1.55,
            c[0],
            c[1],
            {
                titleSize: 13,
                bodySize: 11
            }
        );
    });

    addCard(
        slide,
        0.75,
        4.0,
        5.8,
        1.7,
        "A IDETEL",
        "Probar flujo → uniformar formatos → medir resultados → evaluar digitalización.",
        {
            titleSize: 16,
            bodySize: 12,
            fill: C.lavender
        }
    );

    addCard(
        slide,
        6.8,
        4.0,
        2.7,
        1.7,
        "Al IUTECP",
        "Fortalecer el acompañamiento académico.",
        {
            titleSize: 14,
            bodySize: 10,
            fill: C.lavender
        }
    );

    addCard(
        slide,
        9.75,
        4.0,
        2.7,
        1.7,
        "A futuros pasantes",
        "Registrar actividades y conservar evidencias.",
        {
            titleSize: 13,
            bodySize: 10,
            fill: C.lavender
        }
    );

    slide.addText(
        "Aprendizaje: control, organización de procesos, gestión documental y atención al usuario.",
        {
            x: 1.05,
            y: 6.1,
            w: 11.15,
            h: 0.4,
            fontSize: 13,
            bold: true,
            color: C.purple,
            align: "center",
            margin: 0
        }
    );

    slide.addNotes(
        "Relacionar cada conclusión con los objetivos específicos: diagnóstico del proceso, deficiencias " +
        "principales y propuesta formulada. Explicar brevemente las recomendaciones dirigidas a IDETEL, " +
        "IUTECP y futuros pasantes. Mencionar los aprendizajes administrativos obtenidos."
    );
}

//
// 10. CIERRE
//
{
    const slide = pptx.addSlide();

    slide.background = { color: C.paper };

    slide.addShape(pptx.ShapeType.rect, {
        x: 8.65,
        y: 0,
        w: 4.68,
        h: 7.5,
        fill: { color: C.lavender },
        line: { color: C.lavender }
    });

    slide.addText("CIERRE", {
        x: 0.85,
        y: 1.45,
        w: 2.2,
        h: 0.3,
        fontSize: 12,
        bold: true,
        color: C.purple,
        charSpacing: 1.3,
        margin: 0
    });

    slide.addText(
        "Una solicitud bien atendida también debe estar bien controlada.",
        {
            x: 0.85,
            y: 2.05,
            w: 7.2,
            h: 2.5,
            fontFace: "Aptos Display",
            fontSize: 32,
            bold: true,
            color: C.ink,
            margin: 0,
            valign: "mid"
        }
    );

    slide.addText("Gracias por su atención.", {
        x: 0.85,
        y: 5.25,
        w: 5.0,
        h: 0.45,
        fontSize: 20,
        bold: true,
        color: C.purple,
        margin: 0
    });

    slide.addText("Quedo atenta a sus preguntas.", {
        x: 0.85,
        y: 5.8,
        w: 5.0,
        h: 0.4,
        fontSize: 15,
        color: C.muted,
        margin: 0
    });

    slide.addImage({
        path: IMG.logo,
        x: 10.1,
        y: 2.55,
        w: 1.8,
        h: 1.8
    });

    slide.addText("AMAAL ALRIFAAI ALRIFAAIE", {
        x: 9.25,
        y: 4.8,
        w: 3.45,
        h: 0.4,
        fontSize: 14,
        bold: true,
        color: C.purple,
        align: "center",
        margin: 0
    });

    slide.addText("Administración · IUTECP", {
        x: 9.25,
        y: 5.3,
        w: 3.45,
        h: 0.3,
        fontSize: 11,
        color: C.muted,
        align: "center",
        margin: 0
    });

    slide.addNotes(
        "Cerrar con la idea principal: no basta con recibir o resolver técnicamente una solicitud; también " +
        "debe conocerse quién la atendió, cuál es su estado, cuánto tiempo lleva y cómo fue cerrada. " +
        "Agradecer al IUTECP, IDETEL, tutoras y personal de la empresa. Mantener esta diapositiva visible " +
        "durante las preguntas."
    );
}

async function main() {
    for (const fileName of [SALIDA, SALIDA_PUBLICA]) {
        await pptx.writeFile({ fileName, compression: true });
        console.log(`Presentación generada: ${fileName}`);
    }
    console.log("Diapositivas: 10");
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
