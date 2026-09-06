const path = require("path");
const PptxGenJS = require("pptxgenjs");

const pptxgen = new PptxGenJS();

const CARPETA_PRESENTACION = path.resolve(__dirname, "..");
const CARPETA_KEIDY = path.resolve(CARPETA_PRESENTACION, "..");
const CARPETA_RAIZ = path.resolve(CARPETA_KEIDY, "..");

const SALIDA_OFICIAL = path.join(CARPETA_PRESENTACION, "Defensa_Keidy_10_laminas.pptx");
const SALIDA_ESTUDIO = path.join(CARPETA_PRESENTACION, "Estudio_Keidy_17_laminas.pptx");

const C = {
    paper: "F6EFE5",
    paperLight: "FBF6EE",
    white: "FFFFFF",
    ink: "201817",
    muted: "6F625C",
    oxide: "A33A2E",
    copper: "D97961",
    clay: "EAD0C6",
    sand: "E5C48B",
    green: "1F6F5B",
    greenLight: "E5F3EC",
    line: "D9B8AA"
};

const IMG = {
    varyna: {
        path: path.join(CARPETA_KEIDY, "imagenes", "logo.jpg"),
        width: 447,
        height: 447
    },
    iutecp: {
        path: path.join(CARPETA_RAIZ, "compartido", "iutecp.png"),
        width: 2578,
        height: 830
    },
    ishikawa: {
        path: path.join(CARPETA_KEIDY, "imagenes", "ishikawa_keidy_procura.png"),
        width: 1729,
        height: 523
    },
    asIs: {
        path: path.join(CARPETA_KEIDY, "imagenes", "02_flujo_as_is_procura.png"),
        width: 584,
        height: 1141
    },
    toBe: {
        path: path.join(CARPETA_KEIDY, "imagenes", "03_flujo_to_be_procura.png"),
        width: 640,
        height: 1567
    },
    swimlane: {
        path: path.join(CARPETA_KEIDY, "imagenes", "04_swimlane_procura.png"),
        width: 1199,
        height: 1081
    },
    sipoc: {
        path: path.join(CARPETA_KEIDY, "imagenes", "05_sipoc_procura.png"),
        width: 637,
        height: 730
    },
    raci: {
        path: path.join(CARPETA_KEIDY, "imagenes", "06_matriz_raci_propuesta.png"),
        width: 519,
        height: 139
    }
};

const CHAPTERS = ["I", "II", "III", "IV", "V"];

function createDeck(title) {
    const pptx = new PptxGenJS();
    pptx.layout = "LAYOUT_WIDE";
    pptx.author = "Keidy Guzmán";
    pptx.company = "IUTECP";
    pptx.subject = "Defensa de Pasantías Profesionales";
    pptx.title = title;
    pptx.lang = "es-VE";
    pptx.theme = {
        headFontFace: "Georgia",
        bodyFontFace: "Verdana",
        lang: "es-VE"
    };
    return pptx;
}

function addContainedImage(slide, image, box) {
    const imageRatio = image.width / image.height;
    const boxRatio = box.w / box.h;
    const w = imageRatio > boxRatio ? box.w : box.h * imageRatio;
    const h = imageRatio > boxRatio ? box.w / imageRatio : box.h;

    slide.addImage({
        path: image.path,
        x: box.x + (box.w - w) / 2,
        y: box.y + (box.h - h) / 2,
        w,
        h
    });
}

function addChrome(slide, number, chapter = null, study = false) {
    slide.background = { color: C.paper };
    slide.addShape(pptxgen.ShapeType.rect, {
        x: 0.28,
        y: 0.24,
        w: 12.77,
        h: 7.02,
        fill: { color: C.paper, transparency: 100 },
        line: { color: C.line, transparency: 45, width: 0.8 }
    });
    slide.addText(study ? "GUÍA DE ESTUDIO · KEIDY GUZMÁN" : "DEFENSA DE PASANTÍAS · KEIDY GUZMÁN", {
        x: 0.72,
        y: 0.38,
        w: 5.6,
        h: 0.2,
        fontFace: "Verdana",
        fontSize: 8,
        bold: true,
        color: C.oxide,
        charSpacing: 1.2,
        margin: 0
    });
    slide.addShape(pptxgen.ShapeType.rect, {
        x: 11.3,
        y: 0.42,
        w: 0.82,
        h: 0.06,
        fill: { color: C.oxide },
        line: { color: C.oxide }
    });
    slide.addShape(pptxgen.ShapeType.rect, {
        x: 12.12,
        y: 0.42,
        w: 0.45,
        h: 0.06,
        fill: { color: C.sand },
        line: { color: C.sand }
    });
    slide.addText(String(number).padStart(2, "0"), {
        x: 12.2,
        y: 7.02,
        w: 0.4,
        h: 0.15,
        fontFace: "Verdana",
        fontSize: 7,
        color: C.muted,
        align: "right",
        margin: 0
    });

    if (!study) {
        CHAPTERS.forEach((label, index) => {
            const active = chapter === index;
            const x = 0.72 + index * 1.06;
            slide.addText(label, {
                x,
                y: 6.88,
                w: 0.92,
                h: 0.13,
                fontFace: "Verdana",
                fontSize: 6.5,
                bold: active,
                color: active ? C.oxide : C.muted,
                align: "center",
                margin: 0
            });
            slide.addShape(pptxgen.ShapeType.rect, {
                x,
                y: 7.07,
                w: 0.92,
                h: active ? 0.07 : 0.035,
                fill: { color: active ? C.oxide : C.line },
                line: { color: active ? C.oxide : C.line }
            });
        });
    }
}

function addHeading(slide, eyebrow, title, subtitle = "", options = {}) {
    slide.addText(eyebrow.toUpperCase(), {
        x: 0.72,
        y: options.eyebrowY || 0.72,
        w: 8.8,
        h: 0.24,
        fontFace: "Verdana",
        fontSize: 9,
        bold: true,
        color: options.eyebrowColor || C.oxide,
        charSpacing: 1.1,
        margin: 0
    });
    slide.addText(title, {
        x: 0.72,
        y: options.titleY || 1.05,
        w: options.titleW || 11.6,
        h: options.titleH || 0.78,
        fontFace: "Georgia",
        fontSize: options.titleSize || 28,
        bold: true,
        color: C.ink,
        margin: 0,
        valign: "mid",
        breakLine: false
    });
    if (subtitle) {
        slide.addText(subtitle, {
            x: 0.74,
            y: options.subtitleY || 1.82,
            w: options.subtitleW || 10.8,
            h: options.subtitleH || 0.34,
            fontFace: "Verdana",
            fontSize: options.subtitleSize || 11,
            color: C.muted,
            margin: 0,
            valign: "mid"
        });
    }
}

function addCard(slide, config) {
    const {
        x,
        y,
        w,
        h,
        label = "",
        title,
        body = "",
        fill = C.paperLight,
        accent = C.oxide,
        titleSize = 16,
        bodySize = 9.5,
        align = "left",
        topAccent = true
    } = config;

    slide.addShape(pptxgen.ShapeType.rect, {
        x,
        y,
        w,
        h,
        fill: { color: fill },
        line: { color: C.line, width: 0.8 }
    });
    slide.addShape(pptxgen.ShapeType.rect, {
        x,
        y,
        w: topAccent ? w : 0.07,
        h: topAccent ? 0.06 : h,
        fill: { color: accent },
        line: { color: accent }
    });

    const runs = [];
    if (label) {
        runs.push({
            text: label.toUpperCase(),
            options: {
                fontFace: "Verdana",
                fontSize: 7.5,
                bold: true,
                color: accent,
                charSpacing: 0.8,
                breakLine: true,
                paraSpaceAfterPt: 5
            }
        });
    }
    runs.push({
        text: title,
        options: {
            fontFace: "Georgia",
            fontSize: titleSize,
            bold: true,
            color: C.ink,
            breakLine: Boolean(body),
            paraSpaceAfterPt: body ? 5 : 0
        }
    });
    if (body) {
        runs.push({
            text: body,
            options: {
                fontFace: "Verdana",
                fontSize: bodySize,
                color: C.muted
            }
        });
    }
    slide.addText(runs, {
        x: x + 0.16,
        y: y + 0.12,
        w: w - 0.32,
        h: h - 0.24,
        margin: 0,
        align,
        valign: "mid",
        breakLine: false
    });
}

function addPill(slide, text, x, y, w, h = 0.46, options = {}) {
    slide.addShape(pptxgen.ShapeType.rect, {
        x,
        y,
        w,
        h,
        fill: { color: options.fill || C.clay },
        line: { color: options.line || C.clay }
    });
    slide.addText(text, {
        x: x + 0.1,
        y: y + 0.08,
        w: w - 0.2,
        h: h - 0.16,
        fontFace: "Verdana",
        fontSize: options.fontSize || 9.5,
        bold: true,
        color: options.color || C.oxide,
        align: "center",
        valign: "mid",
        margin: 0
    });
}

function addProcess(slide, steps, box) {
    const gap = box.gap || 0.12;
    const w = (box.w - gap * (steps.length - 1)) / steps.length;
    steps.forEach((step, index) => {
        const x = box.x + index * (w + gap);
        slide.addShape(pptxgen.ShapeType.rect, {
            x,
            y: box.y,
            w,
            h: box.h,
            fill: { color: box.fill || C.paperLight },
            line: { color: box.line || C.oxide, width: 0.8 }
        });
        slide.addText([
            {
                text: String(index + 1).padStart(2, "0"),
                options: {
                    fontFace: "Verdana",
                    fontSize: 7,
                    bold: true,
                    color: box.accent || C.oxide,
                    breakLine: true,
                    paraSpaceAfterPt: 4
                }
            },
            {
                text: step,
                options: {
                    fontFace: "Georgia",
                    fontSize: box.fontSize || 13,
                    bold: true,
                    color: C.ink
                }
            }
        ], {
            x: x + 0.08,
            y: box.y + 0.08,
            w: w - 0.16,
            h: box.h - 0.16,
            align: "center",
            valign: "mid",
            margin: 0,
            breakLine: false
        });
        if (index < steps.length - 1) {
            slide.addText("→", {
                x: x + w - 0.01,
                y: box.y + box.h / 2 - 0.12,
                w: gap + 0.02,
                h: 0.24,
                fontFace: "Verdana",
                fontSize: 11,
                bold: true,
                color: box.accent || C.oxide,
                align: "center",
                margin: 0
            });
        }
    });
}

function addNotes(slide, text) {
    slide.addNotes(text.replace(/\s+/g, " ").trim());
}

function addCover(pptx, study = false) {
    const slide = pptx.addSlide();
    slide.background = { color: C.paperLight };
    slide.addShape(pptxgen.ShapeType.rect, {
        x: 0.28,
        y: 0.24,
        w: 12.77,
        h: 7.02,
        fill: { color: C.paperLight, transparency: 100 },
        line: { color: C.line, transparency: 30, width: 0.8 }
    });
    slide.addText(study ? "GUÍA PERSONAL DE ESTUDIO" : "DEFENSA DE PASANTÍAS PROFESIONALES", {
        x: 0.72,
        y: 0.58,
        w: 6.3,
        h: 0.3,
        fontFace: "Verdana",
        fontSize: 9,
        bold: true,
        color: C.oxide,
        charSpacing: 1.2,
        margin: 0
    });
    slide.addText("PROPUESTA DE SIMPLIFICACIÓN ADMINISTRATIVA DE LA PROCURA EN LUBRICANTES Y EQUIPOS VARYNA, C.A.", {
        x: 0.72,
        y: 1.18,
        w: 7.1,
        h: 3.15,
        fontFace: "Georgia",
        fontSize: study ? 25 : 27,
        bold: true,
        color: C.ink,
        margin: 0,
        valign: "mid",
        breakLine: false
    });
    slide.addText("Keidy Guzmán", {
        x: 0.72,
        y: 5.15,
        w: 5.8,
        h: 0.42,
        fontFace: "Georgia",
        fontSize: 20,
        bold: true,
        color: C.oxide,
        margin: 0
    });
    slide.addText("Administración · IUTECP · 2026", {
        x: 0.72,
        y: 5.65,
        w: 5.8,
        h: 0.3,
        fontFace: "Verdana",
        fontSize: 11,
        color: C.muted,
        margin: 0
    });

    slide.addShape(pptxgen.ShapeType.rect, {
        x: 8.5,
        y: 0.58,
        w: 4.08,
        h: 6.32,
        fill: { color: C.clay },
        line: { color: C.oxide, width: 1.2 }
    });
    slide.addShape(pptxgen.ShapeType.rect, {
        x: 8.72,
        y: 0.8,
        w: 3.64,
        h: 5.88,
        fill: { color: C.clay, transparency: 100 },
        line: { color: C.oxide, transparency: 45, width: 0.8 }
    });
    slide.addShape(pptxgen.ShapeType.rect, {
        x: 9.05,
        y: 1.08,
        w: 2.98,
        h: 1.02,
        fill: { color: C.white },
        line: { color: C.white }
    });
    addContainedImage(slide, IMG.iutecp, { x: 9.18, y: 1.2, w: 2.72, h: 0.76 });
    slide.addShape(pptxgen.ShapeType.rect, {
        x: 9.67,
        y: 2.35,
        w: 1.78,
        h: 1.78,
        fill: { color: C.white },
        line: { color: C.line, width: 0.7 }
    });
    addContainedImage(slide, IMG.varyna, { x: 9.82, y: 2.5, w: 1.48, h: 1.48 });
    ["DIAGNÓSTICO", "PROPUESTA", "CONTROL"].forEach((text, index) => {
        addPill(slide, text, 9.35, 4.46 + index * 0.58, 2.38, 0.4, {
            fill: index === 1 ? C.greenLight : C.paperLight,
            line: index === 1 ? C.green : C.oxide,
            color: index === 1 ? C.green : C.oxide,
            fontSize: 8
        });
    });
    addNotes(slide, study
        ? "Usar esta portada para iniciar el repaso. Decir el título completo, el nombre de la empresa y recordar que la procura abarca desde la necesidad hasta el cierre de la adquisición."
        : "Saludar al jurado, a las tutoras y a las personas presentes. Presentarse como Keidy Guzmán, estudiante de Administración del IUTECP. Leer el título oficial e indicar que las pasantías se realizaron en Lubricantes y Equipos Varyna, C.A. Explicar que el tema central es la simplificación administrativa del proceso de procura.");
}

function buildOfficialDeck() {
    const pptx = createDeck("Propuesta de simplificación administrativa de la procura en Lubricantes y Equipos Varyna, C.A.");
    addCover(pptx, false);

    // 2. Agenda
    {
        const slide = pptx.addSlide();
        addChrome(slide, 2);
        addHeading(slide, "Agenda", "Estructura de la socialización", "", {
            titleY: 1.7,
            titleH: 0.7
        });
        const items = [
            ["CAPÍTULO I", "Realidad organizacional"],
            ["CAPÍTULO II", "Diagnóstico situacional"],
            ["CAPÍTULO III", "Marco teórico"],
            ["CAPÍTULO IV", "Actividades realizadas"],
            ["CAPÍTULO V", "Conclusiones y recomendaciones"]
        ];
        items.forEach(([label, title], index) => {
            addCard(slide, {
                x: 0.72 + index * 2.5,
                y: 3.33,
                w: 2.3,
                h: 2.22,
                label,
                title,
                titleSize: 15,
                align: "center",
                fill: index % 2 === 0 ? C.paperLight : "F2E3D8"
            });
        });
        addNotes(slide, "Explicar brevemente que la presentación seguirá los cinco capítulos del informe: realidad organizacional, diagnóstico situacional, marco teórico, actividades realizadas y conclusiones con recomendaciones. No leer cada tarjeta; presentarlas como el recorrido de la defensa.");
    }

    // 3. Empresa y área
    {
        const slide = pptx.addSlide();
        addChrome(slide, 3, 0);
        addHeading(slide, "Capítulo I · Realidad organizacional", "Empresa y área de pasantía");
        slide.addShape(pptxgen.ShapeType.rect, {
            x: 0.78,
            y: 2.0,
            w: 3.1,
            h: 3.98,
            fill: { color: C.clay },
            line: { color: C.oxide, width: 0.9 }
        });
        slide.addShape(pptxgen.ShapeType.rect, {
            x: 1.36,
            y: 2.38,
            w: 1.94,
            h: 1.94,
            fill: { color: C.white },
            line: { color: C.white }
        });
        addContainedImage(slide, IMG.varyna, { x: 1.5, y: 2.52, w: 1.66, h: 1.66 });
        slide.addText("15 años", {
            x: 1.0,
            y: 4.65,
            w: 2.65,
            h: 0.45,
            fontFace: "Georgia",
            fontSize: 22,
            bold: true,
            color: C.oxide,
            align: "center",
            margin: 0
        });
        slide.addText("de trayectoria", {
            x: 1.0,
            y: 5.12,
            w: 2.65,
            h: 0.28,
            fontFace: "Verdana",
            fontSize: 9,
            color: C.muted,
            align: "center",
            margin: 0
        });
        [
            ["EMPRESA", "Lubricantes y Equipos Varyna, C.A."],
            ["SECTOR", "Petrolero · Industrial · Construcción"],
            ["ÁREA", "Departamento Administrativo"],
            ["FOCO", "Procura de bienes, materiales e insumos"]
        ].forEach(([label, title], index) => {
            addCard(slide, {
                x: index % 2 === 0 ? 4.2 : 8.35,
                y: index < 2 ? 2.0 : 3.34,
                w: 3.75,
                h: 1.08,
                label,
                title,
                titleSize: 14,
                topAccent: false
            });
        });
        addProcess(slide, ["Requisición", "Cotización", "Aprobación", "Compra", "Seguimiento"], {
            x: 4.2,
            y: 4.92,
            w: 7.9,
            h: 0.9,
            fontSize: 10,
            gap: 0.1
        });
        addNotes(slide, "Presentar a Lubricantes y Equipos Varyna, C.A. como una empresa venezolana con aproximadamente quince años de trayectoria en los sectores petrolero, industrial y de construcción. Explicar que la pasantía se desarrolló en el Departamento Administrativo, especialmente en procura. Señalar que el proceso incluye requisición, cotización, aprobación, compra y seguimiento.");
    }

    // 4. Problema y objetivos
    {
        const slide = pptx.addSlide();
        addChrome(slide, 4, 1);
        addHeading(slide, "Capítulo II · Diagnóstico situacional", "Proceso realizado, pero con oportunidades de organización", "", {
            titleH: 1.02,
            titleSize: 26,
            titleW: 11.8
        });
        [
            "Canal de recepción no único",
            "Formatos no uniformes",
            "Cuellos de botella en aprobaciones",
            "Seguimiento e indicadores limitados"
        ].forEach((title, index) => {
            addCard(slide, {
                x: 0.72 + index * 3.03,
                y: 2.3,
                w: 2.78,
                h: 1.18,
                label: `HALLAZGO ${index + 1}`,
                title,
                titleSize: 13.5,
                align: "center",
                fill: index === 2 ? C.clay : C.paperLight
            });
        });
        slide.addText("“El proceso no estaba mal, pero podía estar mejor organizado.”", {
            x: 1.05,
            y: 3.83,
            w: 11.15,
            h: 0.58,
            fontFace: "Georgia",
            fontSize: 19,
            bold: true,
            italic: true,
            color: C.oxide,
            align: "center",
            valign: "mid",
            margin: 0
        });
        slide.addText("OBJETIVOS", {
            x: 0.78,
            y: 4.72,
            w: 1.45,
            h: 0.25,
            fontFace: "Verdana",
            fontSize: 8,
            bold: true,
            color: C.muted,
            charSpacing: 1,
            margin: 0
        });
        addProcess(slide, ["Diagnosticar", "Identificar", "Formular"], {
            x: 2.15,
            y: 4.55,
            w: 9.55,
            h: 1.05,
            fontSize: 15,
            gap: 0.18,
            fill: C.clay
        });
        addNotes(slide, "Explicar que la situación se relacionó con la dispersión del flujo administrativo: solicitudes sin un canal único, formatos no uniformes, posibles cuellos de botella en aprobaciones y seguimiento limitado. Aclarar que el personal realizaba el proceso; la oportunidad estaba en organizarlo mejor. Presentar la secuencia de objetivos: diagnosticar, identificar y formular.");
    }

    // 5. Diagnóstico e Ishikawa
    {
        const slide = pptx.addSlide();
        addChrome(slide, 5, 1);
        addHeading(slide, "Capítulo II · Técnica de diagnóstico", "Diagnóstico e Ishikawa");
        ["Observación directa", "Entrevista estructurada", "Revisión documental", "Análisis de tiempos"].forEach((text, index) => {
            addPill(slide, text, 0.78, 2.05 + index * 0.76, 3.1, 0.58, {
                fill: index % 2 === 0 ? C.clay : C.paperLight,
                line: C.line,
                color: C.oxide,
                fontSize: 10
            });
        });
        slide.addText("TÉCNICAS", {
            x: 0.8,
            y: 5.18,
            w: 3.05,
            h: 0.2,
            fontFace: "Verdana",
            fontSize: 7,
            bold: true,
            color: C.muted,
            align: "center",
            charSpacing: 1,
            margin: 0
        });
        slide.addShape(pptxgen.ShapeType.rect, {
            x: 4.18,
            y: 1.98,
            w: 8.38,
            h: 3.25,
            fill: { color: C.white },
            line: { color: C.line, width: 0.8 }
        });
        addContainedImage(slide, IMG.ishikawa, { x: 4.36, y: 2.15, w: 8.02, h: 2.9 });
        ["Procedimientos", "Responsabilidades", "Documentación", "Seguimiento"].forEach((text, index) => {
            addPill(slide, text, 4.18 + index * 2.1, 5.42, 1.92, 0.42, {
                fill: C.greenLight,
                line: C.green,
                color: C.green,
                fontSize: 8
            });
        });
        slide.addText("Ishikawa = herramienta para organizar causas", {
            x: 1.0,
            y: 6.02,
            w: 11.3,
            h: 0.42,
            fontFace: "Georgia",
            fontSize: 17,
            bold: true,
            color: C.oxide,
            align: "center",
            margin: 0
        });
        addNotes(slide, "Explicar que el diagnóstico combinó observación directa, entrevista estructurada, revisión documental y análisis de tiempos. Presentar el Ishikawa como una herramienta para organizar causas, no como una solución ni como un cuello de botella. Las causas se agruparon en procedimientos, responsabilidades, documentación y seguimiento.");
    }

    // 6. Marco teórico
    {
        const slide = pptx.addSlide();
        addChrome(slide, 6, 2);
        addHeading(slide, "Capítulo III · Marco teórico", "Cuatro conceptos que sostienen la propuesta");
        [
            ["01", "Procura y gestión de compras", "Gestionar necesidades, proveedores y adquisiciones."],
            ["02", "Control interno", "Mantener verificaciones, documentos y responsabilidades."],
            ["03", "Simplificación administrativa", "Reducir demoras y organizar el proceso."],
            ["04", "Trazabilidad documental", "Seguir el recorrido completo de cada solicitud."]
        ].forEach(([label, title, body], index) => {
            addCard(slide, {
                x: index % 2 === 0 ? 0.78 : 6.72,
                y: index < 2 ? 2.08 : 3.7,
                w: 5.55,
                h: 1.34,
                label,
                title,
                body,
                titleSize: 16,
                bodySize: 9.5,
                topAccent: false
            });
        });
        slide.addShape(pptxgen.ShapeType.rect, {
            x: 0.78,
            y: 5.52,
            w: 11.5,
            h: 0.72,
            fill: { color: C.clay },
            line: { color: C.line, width: 0.8 }
        });
        slide.addText("BASES LEGALES", {
            x: 1.0,
            y: 5.73,
            w: 1.4,
            h: 0.2,
            fontFace: "Verdana",
            fontSize: 7.5,
            bold: true,
            color: C.oxide,
            charSpacing: 0.9,
            margin: 0
        });
        slide.addText("Constitución, Art. 112  ·  Código de Comercio, Art. 32", {
            x: 2.55,
            y: 5.65,
            w: 8.9,
            h: 0.32,
            fontFace: "Georgia",
            fontSize: 15,
            bold: true,
            color: C.ink,
            align: "center",
            margin: 0
        });
        addNotes(slide, "Destacar cuatro conceptos: procura y gestión de compras, control interno, simplificación administrativa y trazabilidad documental. Aclarar que simplificar no significa eliminar controles, sino organizar el proceso. Mencionar brevemente el artículo 112 de la Constitución y el artículo 32 del Código de Comercio como fundamentos generales.");
    }

    // 7. Actividades
    {
        const slide = pptx.addSlide();
        addChrome(slide, 7, 3);
        addHeading(slide, "Capítulo IV · Actividades realizadas", "Cuatro actividades principales");
        [
            ["SEMANAS 1–2", "Observar y levantar el proceso", "Recepción de solicitudes y recorrido de requisiciones."],
            ["SEMANAS 3–4", "Entrevistar, revisar y analizar tiempos", "Personal, expedientes y etapas con posibles retrasos."],
            ["SEMANA 5", "Elaborar el Ishikawa", "Organización de causas relacionadas con la problemática."],
            ["SEMANAS 6–9", "Diseñar y validar la propuesta", "Flujo, formatos, autorizaciones e indicadores."]
        ].forEach(([label, title, body], index) => {
            addCard(slide, {
                x: index % 2 === 0 ? 0.82 : 6.72,
                y: index < 2 ? 2.12 : 4.0,
                w: 5.55,
                h: 1.48,
                label,
                title,
                body,
                titleSize: 16,
                bodySize: 9.2,
                topAccent: false,
                fill: index === 3 ? C.greenLight : C.paperLight,
                accent: index === 3 ? C.green : C.oxide
            });
        });
        addPill(slide, "SEMANA 10  →  cierre y consolidación del informe", 3.42, 5.88, 6.5, 0.48, {
            fill: C.clay,
            line: C.oxide,
            color: C.oxide,
            fontSize: 9.5
        });
        addNotes(slide, "Resumir las diez semanas en cuatro actividades: observar y levantar el proceso, entrevistar y revisar documentos con análisis de tiempos, elaborar el Ishikawa, y diseñar y validar la propuesta. Añadir que la semana diez se dedicó al cierre y consolidación del informe.");
    }

    // 8. Propuesta
    {
        const slide = pptx.addSlide();
        addChrome(slide, 8, 3);
        addHeading(slide, "Capítulo IV · Propuesta", "Simplificar sin perder el control", "El TO-BE organiza el recorrido y deja visibles las verificaciones.");
        slide.addText("TO-BE PROPUESTO", {
            x: 0.92,
            y: 2.13,
            w: 2.85,
            h: 0.2,
            fontFace: "Verdana",
            fontSize: 7.5,
            bold: true,
            color: C.green,
            charSpacing: 0.8,
            align: "center",
            margin: 0
        });
        slide.addShape(pptxgen.ShapeType.rect, {
            x: 0.82,
            y: 2.38,
            w: 3.05,
            h: 3.94,
            fill: { color: C.white },
            line: { color: C.green, width: 0.8 }
        });
        addContainedImage(slide, IMG.toBe, { x: 1.0, y: 2.52, w: 2.69, h: 3.66 });
        [
            ["01", "Flujo simplificado"],
            ["02", "Responsables definidos"],
            ["03", "Formatos estandarizados"],
            ["04", "Matriz de autorización por monto"],
            ["05", "Indicadores de seguimiento"]
        ].forEach(([label, title], index) => {
            const last = index === 4;
            addCard(slide, {
                x: last ? 4.38 : index % 2 === 0 ? 4.38 : 8.48,
                y: last ? 4.85 : index < 2 ? 2.22 : 3.53,
                w: last ? 8.18 : 3.78,
                h: last ? 0.88 : 1.05,
                label,
                title,
                titleSize: last ? 15 : 14.5,
                align: last ? "center" : "left",
                fill: last ? C.greenLight : C.paperLight,
                accent: last ? C.green : C.oxide,
                topAccent: false
            });
        });
        slide.addText([
            { text: "Simplificar ≠ eliminar controles", options: { breakLine: true } },
            { text: "Simplificar = organizar mejor el proceso", options: { color: C.green } }
        ], {
            x: 4.4,
            y: 5.98,
            w: 8.1,
            h: 0.55,
            fontFace: "Georgia",
            fontSize: 16,
            bold: true,
            color: C.oxide,
            align: "center",
            margin: 0,
            breakLine: false
        });
        addNotes(slide, "Presentar la propuesta como un flujo simplificado con responsables por etapa, formatos estandarizados, una matriz de autorización por monto e indicadores. Explicar que los niveles y montos deben definirse y aprobarse con la empresa. Recalcar que simplificar no es eliminar controles, sino ordenar el proceso para hacerlo más claro y fácil de seguir.");
    }

    // 9. Conclusiones y recomendaciones
    {
        const slide = pptx.addSlide();
        addChrome(slide, 9, 4);
        addHeading(slide, "Capítulo V · Conclusiones y recomendaciones", "Resultados principales");
        [
            ["1 · DIAGNÓSTICO", "El recorrido puede simplificarse."],
            ["2 · HALLAZGOS", "Formatos, autorizaciones, seguimiento e indicadores requieren mejora."],
            ["3 · PROPUESTA", "Flujo + responsables + formatos + autorizaciones + indicadores."]
        ].forEach(([label, title], index) => {
            addCard(slide, {
                x: 0.72 + index * 4.08,
                y: 1.92,
                w: 3.8,
                h: 1.55,
                label,
                title,
                titleSize: 14.5,
                topAccent: false
            });
        });
        slide.addText("RECOMENDACIONES", {
            x: 0.75,
            y: 3.78,
            w: 2.0,
            h: 0.22,
            fontFace: "Verdana",
            fontSize: 8,
            bold: true,
            color: C.oxide,
            charSpacing: 1,
            margin: 0
        });
        [
            ["EMPRESA", "Implementación gradual y revisión de indicadores."],
            ["IUTECP", "Mantener el acompañamiento académico."],
            ["FUTUROS PASANTES", "Registrar actividades y evidencias."]
        ].forEach(([label, title], index) => {
            addCard(slide, {
                x: 0.72 + index * 4.08,
                y: 4.15,
                w: 3.8,
                h: 1.45,
                label,
                title,
                titleSize: 14,
                topAccent: false,
                fill: C.clay
            });
        });
        addPill(slide, "Aprendizaje: planificación · organización · control · análisis de procesos", 2.15, 5.95, 9.0, 0.46, {
            fill: C.paperLight,
            line: C.line,
            color: C.oxide,
            fontSize: 9
        });
        addNotes(slide, "Relacionar cada conclusión con un objetivo: el diagnóstico mostró un recorrido simplificable; los hallazgos señalaron formatos, autorizaciones, seguimiento e indicadores; y la propuesta integró esos elementos. Recomendar implementación gradual, acompañamiento académico y registro de evidencias. Mencionar el aprendizaje profesional en planificación, organización, control y análisis de procesos.");
    }

    // 10. Cierre
    {
        const slide = pptx.addSlide();
        slide.background = { color: C.paperLight };
        slide.addShape(pptxgen.ShapeType.rect, {
            x: 8.55,
            y: 0,
            w: 4.78,
            h: 7.5,
            fill: { color: C.clay },
            line: { color: C.clay }
        });
        slide.addText("CIERRE", {
            x: 0.82,
            y: 1.15,
            w: 2.0,
            h: 0.25,
            fontFace: "Verdana",
            fontSize: 9,
            bold: true,
            color: C.oxide,
            charSpacing: 1.2,
            margin: 0
        });
        slide.addText("“El proceso no estaba mal; podía estar mejor organizado, ser más fácil de seguir y mantener controles más claros.”", {
            x: 0.82,
            y: 1.78,
            w: 7.1,
            h: 2.65,
            fontFace: "Georgia",
            fontSize: 27,
            bold: true,
            color: C.ink,
            margin: 0,
            valign: "mid"
        });
        slide.addText("Gracias por su atención.", {
            x: 0.82,
            y: 5.15,
            w: 5.8,
            h: 0.42,
            fontFace: "Georgia",
            fontSize: 19,
            bold: true,
            color: C.oxide,
            margin: 0
        });
        slide.addText("Quedo atenta a sus preguntas.", {
            x: 0.82,
            y: 5.68,
            w: 5.8,
            h: 0.3,
            fontFace: "Verdana",
            fontSize: 11,
            color: C.muted,
            margin: 0
        });
        slide.addShape(pptxgen.ShapeType.rect, {
            x: 9.25,
            y: 1.25,
            w: 3.35,
            h: 1.08,
            fill: { color: C.white },
            line: { color: C.white }
        });
        addContainedImage(slide, IMG.iutecp, { x: 9.42, y: 1.42, w: 3.0, h: 0.74 });
        slide.addShape(pptxgen.ShapeType.rect, {
            x: 10.1,
            y: 2.82,
            w: 1.65,
            h: 1.65,
            fill: { color: C.white },
            line: { color: C.line }
        });
        addContainedImage(slide, IMG.varyna, { x: 10.24, y: 2.96, w: 1.37, h: 1.37 });
        slide.addText("KEIDY GUZMÁN", {
            x: 9.15,
            y: 5.05,
            w: 3.5,
            h: 0.3,
            fontFace: "Georgia",
            fontSize: 14,
            bold: true,
            color: C.oxide,
            align: "center",
            margin: 0
        });
        slide.addText("Administración · IUTECP", {
            x: 9.15,
            y: 5.48,
            w: 3.5,
            h: 0.22,
            fontFace: "Verdana",
            fontSize: 8.5,
            color: C.muted,
            align: "center",
            margin: 0
        });
        addNotes(slide, "Cerrar recordando que el objetivo no fue afirmar que el proceso estaba mal, sino demostrar que podía organizarse mejor, ser más fácil de seguir y mantener controles más claros. Agradecer al jurado, al IUTECP, a las tutoras y a la empresa. Mantener esta lámina durante las preguntas.");
    }

    return pptx;
}

function addStudyHeading(slide, number, eyebrow, title, subtitle = "") {
    addChrome(slide, number, null, true);
    addHeading(slide, eyebrow, title, subtitle, {
        titleSize: 27,
        titleH: 0.9,
        subtitleY: 1.88
    });
}

function buildStudyDeck() {
    const pptx = createDeck("Guía de estudio para la defensa de Keidy Guzmán");
    addCover(pptx, true);

    // 2. Mapa
    {
        const slide = pptx.addSlide();
        addStudyHeading(slide, 2, "Mapa completo del proyecto", "La cadena que organiza la defensa");
        addProcess(slide, ["Empresa", "Problema", "Diagnóstico", "Ishikawa", "Propuesta", "Conclusión"], {
            x: 0.72,
            y: 3.0,
            w: 11.85,
            h: 1.55,
            fontSize: 14,
            gap: 0.12
        });
        slide.addText("PROBLEMA → DIAGNÓSTICO → ISHIKAWA → HALLAZGOS → PROPUESTA → CONCLUSIÓN", {
            x: 1.1,
            y: 5.25,
            w: 11.1,
            h: 0.5,
            fontFace: "Georgia",
            fontSize: 17,
            bold: true,
            color: C.oxide,
            align: "center",
            margin: 0
        });
        addNotes(slide, "Memorizar esta cadena. Si se pierde el hilo, volver al problema, explicar cómo se diagnosticó y conectar los hallazgos con la propuesta.");
    }

    // 3. Empresa
    {
        const slide = pptx.addSlide();
        addStudyHeading(slide, 3, "Capítulo I", "¿Qué es Varyna y dónde se realizó la pasantía?");
        slide.addShape(pptxgen.ShapeType.rect, {
            x: 0.82,
            y: 2.2,
            w: 3.3,
            h: 3.75,
            fill: { color: C.clay },
            line: { color: C.oxide }
        });
        addContainedImage(slide, IMG.varyna, { x: 1.5, y: 2.65, w: 1.95, h: 1.95 });
        slide.addText("15 años de trayectoria", {
            x: 1.0,
            y: 4.95,
            w: 2.95,
            h: 0.4,
            fontFace: "Georgia",
            fontSize: 17,
            bold: true,
            color: C.oxide,
            align: "center",
            margin: 0
        });
        [
            ["SECTOR", "Petrolero · industrial · construcción"],
            ["ÁREA", "Departamento Administrativo"],
            ["FOCO", "Procura de bienes, materiales e insumos"]
        ].forEach(([label, title], index) => {
            addCard(slide, {
                x: 4.65,
                y: 2.2 + index * 1.28,
                w: 7.6,
                h: 1.0,
                label,
                title,
                titleSize: 16,
                topAccent: false
            });
        });
        addNotes(slide, "Respuesta corta: Varyna es una empresa venezolana vinculada con los sectores petrolero, industrial y de construcción. La pasantía se realizó en el Departamento Administrativo, en actividades de procura.");
    }

    // 4. Procura
    {
        const slide = pptx.addSlide();
        addStudyHeading(slide, 4, "Concepto clave", "¿Qué es la procura?", "Procura no es solamente comprar.");
        addProcess(slide, ["Necesidad", "Requisición", "Cotización", "Aprobación", "Orden", "Seguimiento", "Cierre"], {
            x: 0.65,
            y: 2.85,
            w: 12.0,
            h: 1.48,
            fontSize: 12,
            gap: 0.08
        });
        slide.addText("Gestiona necesidades, proveedores, documentos, autorizaciones y adquisiciones.", {
            x: 1.15,
            y: 5.05,
            w: 11.0,
            h: 0.6,
            fontFace: "Georgia",
            fontSize: 20,
            bold: true,
            color: C.oxide,
            align: "center",
            margin: 0
        });
        addNotes(slide, "Definir procura como el proceso completo que parte de una necesidad, solicita y compara cotizaciones, obtiene aprobaciones, formaliza la compra y mantiene seguimiento hasta el cierre.");
    }

    // 5. Problema
    {
        const slide = pptx.addSlide();
        addStudyHeading(slide, 5, "Situación problemática", "El proceso se realizaba, pero estaba disperso");
        [
            "Canal no único",
            "Formatos diferentes",
            "Seguimiento manual",
            "Aprobaciones demoradas",
            "Indicadores ausentes"
        ].forEach((title, index) => {
            addCard(slide, {
                x: index < 3 ? 0.75 + index * 4.05 : 2.78 + (index - 3) * 4.05,
                y: index < 3 ? 2.25 : 3.88,
                w: 3.75,
                h: 1.18,
                label: `SEÑAL ${index + 1}`,
                title,
                titleSize: 15,
                align: "center",
                fill: index === 3 ? C.clay : C.paperLight
            });
        });
        slide.addText("“No estaba mal, pero podía estar mejor organizado.”", {
            x: 1.2,
            y: 5.55,
            w: 10.9,
            h: 0.5,
            fontFace: "Georgia",
            fontSize: 18,
            bold: true,
            italic: true,
            color: C.oxide,
            align: "center",
            margin: 0
        });
        addNotes(slide, "Frase de rescate: el proceso se realizaba, pero presentaba oportunidades de mejora en su organización y seguimiento.");
    }

    // 6. Interrogante y objetivos
    {
        const slide = pptx.addSlide();
        addStudyHeading(slide, 6, "Orientación del proyecto", "Interrogante y objetivos");
        slide.addText("¿Cómo reducir la dispersión procedimental y fortalecer el seguimiento de las adquisiciones?", {
            x: 1.0,
            y: 2.12,
            w: 11.3,
            h: 1.0,
            fontFace: "Georgia",
            fontSize: 22,
            bold: true,
            color: C.oxide,
            align: "center",
            valign: "mid",
            margin: 0
        });
        addProcess(slide, ["Diagnosticar", "Identificar", "Formular"], {
            x: 1.25,
            y: 3.62,
            w: 10.8,
            h: 1.35,
            fontSize: 16,
            gap: 0.18,
            fill: C.clay
        });
        slide.addText("Primero conocer · después analizar · finalmente proponer", {
            x: 1.5,
            y: 5.55,
            w: 10.3,
            h: 0.4,
            fontFace: "Verdana",
            fontSize: 11,
            bold: true,
            color: C.muted,
            align: "center",
            margin: 0
        });
        addNotes(slide, "Recordar los tres verbos en orden: diagnosticar el proceso actual, identificar deficiencias y causas, y formular una propuesta de simplificación.");
    }

    // 7. Técnicas
    {
        const slide = pptx.addSlide();
        addStudyHeading(slide, 7, "Diagnóstico", "¿Cómo se estudió el proceso?");
        [
            ["01", "Observación directa", "Ver el recorrido real."],
            ["02", "Entrevista estructurada", "Conocer la experiencia del personal."],
            ["03", "Revisión documental", "Examinar requisiciones, cotizaciones y expedientes."],
            ["04", "Análisis de tiempos", "Ubicar etapas con posibles retrasos."]
        ].forEach(([label, title, body], index) => {
            addCard(slide, {
                x: index % 2 === 0 ? 0.82 : 6.75,
                y: index < 2 ? 2.15 : 4.02,
                w: 5.5,
                h: 1.45,
                label,
                title,
                body,
                titleSize: 17,
                bodySize: 9.5,
                topAccent: false
            });
        });
        addNotes(slide, "Explicar que el diagnóstico no se basó en una sola opinión: combinó observación, entrevista, documentos y tiempos.");
    }

    // 8. Ishikawa
    {
        const slide = pptx.addSlide();
        addStudyHeading(slide, 8, "Herramienta de diagnóstico", "¿Qué es el diagrama de Ishikawa?", "Organiza las posibles causas relacionadas con un problema.");
        slide.addShape(pptxgen.ShapeType.rect, {
            x: 0.75,
            y: 2.35,
            w: 11.85,
            h: 3.15,
            fill: { color: C.white },
            line: { color: C.green, width: 0.8 }
        });
        addContainedImage(slide, IMG.ishikawa, { x: 0.98, y: 2.58, w: 11.4, h: 2.68 });
        slide.addText("No es la solución: es la herramienta que organiza las causas.", {
            x: 1.1,
            y: 5.82,
            w: 11.1,
            h: 0.42,
            fontFace: "Georgia",
            fontSize: 17,
            bold: true,
            color: C.green,
            align: "center",
            margin: 0
        });
        addNotes(slide, "Definición corta: el Ishikawa es una herramienta que organiza las posibles causas de un problema. En este proyecto organizó causas relacionadas con recepción, documentación, autorización, responsabilidades y seguimiento.");
    }

    // 9. Ishikawa vs cuello de botella
    {
        const slide = pptx.addSlide();
        addStudyHeading(slide, 9, "Distinción importante", "Ishikawa no es lo mismo que cuello de botella");
        addCard(slide, {
            x: 0.82,
            y: 2.2,
            w: 5.55,
            h: 2.0,
            label: "ISHIKAWA",
            title: "Herramienta de análisis",
            body: "Organiza causas posibles y muestra cómo pueden relacionarse.",
            titleSize: 19,
            bodySize: 10.5,
            topAccent: false,
            fill: C.greenLight,
            accent: C.green
        });
        addCard(slide, {
            x: 6.75,
            y: 2.2,
            w: 5.55,
            h: 2.0,
            label: "CUELLO DE BOTELLA",
            title: "Etapa donde el trabajo se retrasa",
            body: "Ejemplo: una requisición queda detenida durante la aprobación.",
            titleSize: 18,
            bodySize: 10.5,
            topAccent: false,
            fill: C.clay
        });
        addProcess(slide, ["Requisición", "Cotización", "APROBACIÓN DETENIDA", "Compra"], {
            x: 1.12,
            y: 4.8,
            w: 11.05,
            h: 1.0,
            fontSize: 12,
            gap: 0.15,
            fill: C.paperLight
        });
        addNotes(slide, "Responder sin confundir: Ishikawa es la herramienta de análisis; un cuello de botella es una etapa concreta donde el trabajo se acumula o se retrasa.");
    }

    // 10. Hallazgos
    {
        const slide = pptx.addSlide();
        addStudyHeading(slide, 10, "Resultados del diagnóstico", "¿Qué se descubrió?");
        [
            "Canal no único",
            "Formatos no uniformes",
            "Cotizaciones poco visibles",
            "Aprobaciones con retrasos",
            "Autorización por monto",
            "Indicadores ausentes"
        ].forEach((title, index) => {
            addCard(slide, {
                x: 0.75 + (index % 3) * 4.08,
                y: index < 3 ? 2.2 : 4.02,
                w: 3.8,
                h: 1.42,
                label: String(index + 1).padStart(2, "0"),
                title,
                titleSize: 15.5,
                align: "center",
                topAccent: false,
                fill: index === 3 ? C.clay : C.paperLight
            });
        });
        addNotes(slide, "Enumerar los seis hallazgos sin inventar porcentajes ni mejoras medidas. Hablar de oportunidades observadas y beneficios esperados.");
    }

    // 11. Marco teórico
    {
        const slide = pptx.addSlide();
        addStudyHeading(slide, 11, "Capítulo III", "Las cuatro bases teóricas");
        [
            ["PROCURA", "Gestionar necesidades y adquisiciones."],
            ["CONTROL INTERNO", "Conservar verificaciones y responsabilidades."],
            ["SIMPLIFICACIÓN", "Reducir demoras y ordenar pasos."],
            ["TRAZABILIDAD", "Reconstruir el recorrido documental."]
        ].forEach(([title, body], index) => {
            addCard(slide, {
                x: index % 2 === 0 ? 0.82 : 6.75,
                y: index < 2 ? 2.15 : 4.0,
                w: 5.5,
                h: 1.48,
                label: `BASE ${index + 1}`,
                title,
                body,
                titleSize: 17,
                bodySize: 10,
                topAccent: false
            });
        });
        addNotes(slide, "Relacionar cada concepto con el proyecto. Simplificación y control interno no se contradicen: la propuesta intenta hacer el proceso más ágil sin perder verificaciones.");
    }

    // 12. Bases legales
    {
        const slide = pptx.addSlide();
        addStudyHeading(slide, 12, "Bases legales", "¿Qué aportan al informe?");
        addCard(slide, {
            x: 0.82,
            y: 2.35,
            w: 5.55,
            h: 2.35,
            label: "CONSTITUCIÓN · ARTÍCULO 112",
            title: "Actividad económica dentro del marco legal",
            body: "Fundamento general para el desarrollo de la actividad empresarial.",
            titleSize: 19,
            bodySize: 10.5,
            topAccent: false
        });
        addCard(slide, {
            x: 6.75,
            y: 2.35,
            w: 5.55,
            h: 2.35,
            label: "CÓDIGO DE COMERCIO · ARTÍCULO 32",
            title: "Orden y claridad de los registros",
            body: "Fundamento general para una gestión empresarial organizada y documentada.",
            titleSize: 19,
            bodySize: 10.5,
            topAccent: false
        });
        slide.addText("No regulan directamente la procura de Varyna; aportan un marco general.", {
            x: 1.0,
            y: 5.35,
            w: 11.3,
            h: 0.45,
            fontFace: "Georgia",
            fontSize: 17,
            bold: true,
            color: C.oxide,
            align: "center",
            margin: 0
        });
        addNotes(slide, "No recitar los artículos. Explicar su relación general con la actividad económica y el orden de los registros.");
    }

    // 13. Actividades
    {
        const slide = pptx.addSlide();
        addStudyHeading(slide, 13, "Capítulo IV", "Actividades principales de las semanas 1–5");
        addProcess(slide, ["Conocer el área", "Observar el proceso", "Entrevistar", "Revisar documentos", "Elaborar Ishikawa"], {
            x: 0.72,
            y: 2.65,
            w: 11.85,
            h: 1.55,
            fontSize: 13,
            gap: 0.12
        });
        slide.addText("Apoyo continuo: requisiciones · cotizaciones · proveedores · expedientes", {
            x: 1.0,
            y: 4.9,
            w: 11.3,
            h: 0.42,
            fontFace: "Verdana",
            fontSize: 11,
            bold: true,
            color: C.muted,
            align: "center",
            margin: 0
        });
        slide.addText("Semana 5: las observaciones se convierten en un mapa de causas.", {
            x: 1.1,
            y: 5.55,
            w: 11.1,
            h: 0.45,
            fontFace: "Georgia",
            fontSize: 17,
            bold: true,
            color: C.oxide,
            align: "center",
            margin: 0
        });
        addNotes(slide, "Contar las actividades como secuencia y no como una lista de diez semanas. Conectar el trabajo operativo con el diagnóstico.");
    }

    // 14. Diseño de propuesta
    {
        const slide = pptx.addSlide();
        addStudyHeading(slide, 14, "Semanas 6–9", "Cómo se diseñó la propuesta", "TO-BE · swimlane · SIPOC · RACI");
        const panels = [
            [IMG.toBe, "TO-BE", 0.72, 2.25, 2.75, 3.7],
            [IMG.swimlane, "SWIMLANE", 3.65, 2.25, 3.0, 3.7],
            [IMG.sipoc, "SIPOC", 6.83, 2.25, 2.45, 3.7],
            [IMG.raci, "RACI", 9.46, 2.25, 3.1, 3.7]
        ];
        panels.forEach(([image, label, x, y, w, h]) => {
            slide.addShape(pptxgen.ShapeType.rect, {
                x,
                y,
                w,
                h,
                fill: { color: C.white },
                line: { color: C.line, width: 0.7 }
            });
            slide.addText(label, {
                x: x + 0.08,
                y: y + 0.12,
                w: w - 0.16,
                h: 0.2,
                fontFace: "Verdana",
                fontSize: 7,
                bold: true,
                color: C.green,
                align: "center",
                charSpacing: 0.8,
                margin: 0
            });
            addContainedImage(slide, image, { x: x + 0.15, y: y + 0.45, w: w - 0.3, h: h - 0.62 });
        });
        addNotes(slide, "Nombrar los cuatro recursos de diseño. Presentarlos como propuestas: flujo TO-BE, responsabilidades por carriles, visión SIPOC y matriz RACI.");
    }

    // 15. Elementos
    {
        const slide = pptx.addSlide();
        addStudyHeading(slide, 15, "Propuesta", "Cinco elementos que debe recordar");
        [
            ["01", "Flujo simplificado"],
            ["02", "Responsables definidos"],
            ["03", "Formatos estandarizados"],
            ["04", "Matriz de autorización"],
            ["05", "Indicadores de seguimiento"]
        ].forEach(([label, title], index) => {
            addCard(slide, {
                x: index < 3 ? 0.75 + index * 4.05 : 2.78 + (index - 3) * 4.05,
                y: index < 3 ? 2.2 : 3.92,
                w: 3.75,
                h: 1.25,
                label,
                title,
                titleSize: 15.5,
                align: "center",
                topAccent: false,
                fill: index === 4 ? C.greenLight : C.paperLight,
                accent: index === 4 ? C.green : C.oxide
            });
        });
        slide.addText("Simplificar = organizar mejor sin quitar controles necesarios.", {
            x: 1.0,
            y: 5.58,
            w: 11.3,
            h: 0.48,
            fontFace: "Georgia",
            fontSize: 18,
            bold: true,
            color: C.oxide,
            align: "center",
            margin: 0
        });
        addNotes(slide, "Memorizar los cinco elementos. No inventar montos para la matriz; explicar que los rangos deben definirse y aprobarse con la empresa.");
    }

    // 16. Conclusiones
    {
        const slide = pptx.addSlide();
        addStudyHeading(slide, 16, "Capítulo V", "Cada conclusión responde a un objetivo");
        [
            ["OBJETIVO 1", "Diagnóstico", "El recorrido puede simplificarse."],
            ["OBJETIVO 2", "Hallazgos", "La dispersión afecta seguimiento y trazabilidad."],
            ["OBJETIVO 3", "Propuesta", "Flujo, responsables, formatos, autorizaciones e indicadores."]
        ].forEach(([label, title, body], index) => {
            addCard(slide, {
                x: 0.72 + index * 4.08,
                y: 2.15,
                w: 3.8,
                h: 2.0,
                label,
                title,
                body,
                titleSize: 18,
                bodySize: 10,
                topAccent: false
            });
        });
        addCard(slide, {
            x: 2.1,
            y: 4.75,
            w: 9.1,
            h: 1.05,
            label: "APRENDIZAJE PROFESIONAL",
            title: "Planificación · organización · control · gestión documental",
            titleSize: 15.5,
            align: "center",
            topAccent: false,
            fill: C.clay
        });
        addNotes(slide, "Mantener la correspondencia entre objetivos y conclusiones. Añadir el aprendizaje profesional como resultado de la experiencia, no como un cuarto objetivo.");
    }

    // 17. Preguntas
    {
        const slide = pptx.addSlide();
        addStudyHeading(slide, 17, "Práctica final", "Preguntas que debe dominar", "Responderlas sin leer demuestra dominio del proyecto.");
        const questions = [
            "¿Qué es procura?",
            "¿Qué problema encontró?",
            "¿Qué es Ishikawa?",
            "¿Ishikawa o cuello de botella?",
            "¿Cuáles fueron sus objetivos?",
            "¿Qué descubrió?",
            "¿Qué propone?",
            "¿Qué es trazabilidad?",
            "¿Qué es simplificación?",
            "¿Simplificar quita controles?",
            "¿Qué es la matriz por monto?",
            "¿Qué indicadores propone?",
            "¿Cuál fue el aporte?"
        ];
        questions.forEach((text, index) => {
            const column = index < 7 ? 0 : 1;
            const row = column === 0 ? index : index - 7;
            slide.addText([
                { text: String(index + 1).padStart(2, "0"), options: { bold: true, color: C.oxide } },
                { text: `  ${text}`, options: { color: C.ink } }
            ], {
                x: column === 0 ? 0.85 : 6.8,
                y: 2.18 + row * 0.47,
                w: 5.55,
                h: 0.3,
                fontFace: "Verdana",
                fontSize: 10.5,
                margin: 0,
                valign: "mid"
            });
        });
        slide.addShape(pptxgen.ShapeType.rect, {
            x: 0.82,
            y: 5.72,
            w: 11.7,
            h: 0.78,
            fill: { color: C.clay },
            line: { color: C.oxide, width: 0.8 }
        });
        slide.addText("Frase de rescate: primero diagnostiqué el proceso, después identifiqué las causas y finalmente formulé una propuesta de simplificación.", {
            x: 1.05,
            y: 5.88,
            w: 11.25,
            h: 0.42,
            fontFace: "Georgia",
            fontSize: 13.5,
            bold: true,
            color: C.oxide,
            align: "center",
            valign: "mid",
            margin: 0
        });
        addNotes(slide, "Practicar cada pregunta en voz alta. Si una respuesta se bloquea, usar la frase de rescate y regresar a la cadena problema, diagnóstico, Ishikawa, hallazgos, propuesta y conclusión.");
    }

    return pptx;
}

async function main() {
    const official = buildOfficialDeck();
    const study = buildStudyDeck();
    await official.writeFile({ fileName: SALIDA_OFICIAL, compression: true });
    await study.writeFile({ fileName: SALIDA_ESTUDIO, compression: true });
    console.log(`Presentación oficial generada: ${SALIDA_OFICIAL}`);
    console.log(`Presentación de estudio generada: ${SALIDA_ESTUDIO}`);
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
