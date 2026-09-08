const path = require("path");
const PptxGenJS = require("pptxgenjs");

const shapeSource = new PptxGenJS();
const ShapeType = shapeSource.ShapeType;

const CARPETA_PRESENTACION = path.resolve(__dirname, "..");
const CARPETA_JULIANO = path.resolve(CARPETA_PRESENTACION, "..");
const CARPETA_RAIZ = path.resolve(CARPETA_JULIANO, "..");
const SALIDA = path.join(CARPETA_PRESENTACION, "Defensa_Juliano_10_laminas.pptx");

const C = {
    skyPale: "DFF6FF",
    sky: "B8E2F8",
    skyDeep: "76B5E3",
    blue: "1F84D0",
    blueBright: "42ABF5",
    navy: "194C6C",
    ink: "17384D",
    muted: "5B7382",
    white: "FFFFFF",
    glass: "EDF9FF",
    inset: "D7EEFA",
    line: "9ED0EC",
    green: "72C81D",
    greenDark: "438C0D",
    wine: "8F1D2C",
    redLight: "F7DDE1",
    pdvsa: "E30613",
    yellow: "F6CA45"
};

const IMG = {
    iutecp: {
        path: path.join(CARPETA_RAIZ, "compartido", "iutecp.png"),
        width: 2578,
        height: 830
    },
    venangocupet: {
        path: path.join(CARPETA_JULIANO, "imagenes", "logo.png"),
        width: 1024,
        height: 1024
    },
    problemTree: {
        path: path.join(CARPETA_JULIANO, "imagenes", "3.png"),
        width: 3055,
        height: 1788
    },
    architecture: {
        path: path.join(CARPETA_JULIANO, "imagenes", "06_arquitectura_prototipo.png"),
        width: 989,
        height: 158
    },
    relational: {
        path: path.join(CARPETA_JULIANO, "imagenes", "04_modelo_relacional_documental.png"),
        width: 1466,
        height: 1295
    },
    form: {
        path: path.join(CARPETA_JULIANO, "imagenes", "captura-formulario-general.png"),
        width: 882,
        height: 529
    },
    fronts: {
        path: path.join(CARPETA_JULIANO, "imagenes", "captura-expedientes-frentes.png"),
        width: 882,
        height: 565
    },
    reports: {
        path: path.join(CARPETA_JULIANO, "imagenes", "captura-exportacion-filtros-columnas.png"),
        width: 1432,
        height: 828
    }
};

const CHAPTERS = [
    ["I", "Empresa"],
    ["II", "Diagnóstico"],
    ["III", "Fundamentos"],
    ["IV", "Desarrollo"],
    ["V", "Resultados"]
];

const pptx = new PptxGenJS();
pptx.layout = "LAYOUT_WIDE";
pptx.author = "Juliano Cardona";
pptx.company = "IUTECP";
pptx.subject = "Defensa de Pasantías Profesionales";
pptx.title = "Desarrollo de un prototipo de sistema para el control, trazabilidad y reporte documental en la Presidencia de Venangocupet, S.A.";
pptx.lang = "es-VE";
pptx.theme = {
    headFontFace: "Trebuchet MS",
    bodyFontFace: "Noto Sans",
    lang: "es-VE"
};

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

function addWindowBackground(slide) {
    slide.background = { color: C.skyDeep };
    slide.addShape(ShapeType.ellipse, {
        x: -1.1,
        y: -1.4,
        w: 7.2,
        h: 5.2,
        fill: { color: C.skyPale, transparency: 18 },
        line: { color: C.skyPale, transparency: 100 }
    });
    slide.addShape(ShapeType.ellipse, {
        x: 8.7,
        y: 4.4,
        w: 5.8,
        h: 4.0,
        fill: { color: C.sky, transparency: 22 },
        line: { color: C.sky, transparency: 100 }
    });
    slide.addShape(ShapeType.roundRect, {
        x: 0.28,
        y: 0.26,
        w: 12.77,
        h: 6.98,
        rectRadius: 0.08,
        fill: { color: C.glass, transparency: 4 },
        line: { color: C.white, width: 1.4 }
    });
}

function addTitleBar(slide, address) {
    slide.addShape(ShapeType.roundRect, {
        x: 0.42,
        y: 0.39,
        w: 12.48,
        h: 0.58,
        rectRadius: 0.06,
        fill: { color: C.blue },
        line: { color: "146EA9", width: 0.9 }
    });
    slide.addShape(ShapeType.roundRect, {
        x: 0.53,
        y: 0.45,
        w: 12.25,
        h: 0.13,
        rectRadius: 0.04,
        fill: { color: C.white, transparency: 62 },
        line: { color: C.white, transparency: 100 }
    });
    slide.addShape(ShapeType.ellipse, {
        x: 0.61,
        y: 0.51,
        w: 0.28,
        h: 0.28,
        fill: { color: C.blueBright },
        line: { color: C.white, width: 0.7 }
    });
    ["‹", "›"].forEach((symbol, index) => {
        slide.addShape(ShapeType.roundRect, {
            x: 0.99 + index * 0.32,
            y: 0.52,
            w: 0.25,
            h: 0.26,
            rectRadius: 0.03,
            fill: { color: C.white, transparency: 73 },
            line: { color: C.white, transparency: 35, width: 0.6 }
        });
        slide.addText(symbol, {
            x: 0.99 + index * 0.32,
            y: 0.5,
            w: 0.25,
            h: 0.23,
            fontFace: "Trebuchet MS",
            fontSize: 12,
            bold: true,
            color: C.white,
            align: "center",
            margin: 0
        });
    });
    slide.addShape(ShapeType.roundRect, {
        x: 1.72,
        y: 0.52,
        w: 8.55,
        h: 0.27,
        rectRadius: 0.04,
        fill: { color: C.white, transparency: 7 },
        line: { color: C.line, width: 0.6 }
    });
    slide.addText(address, {
        x: 1.92,
        y: 0.555,
        w: 8.15,
        h: 0.14,
        fontFace: "Noto Sans Mono",
        fontSize: 7.3,
        color: C.navy,
        charSpacing: 0.8,
        margin: 0
    });
    [C.yellow, C.green, "F06A78"].forEach((color, index) => {
        slide.addShape(ShapeType.ellipse, {
            x: 11.78 + index * 0.31,
            y: 0.55,
            w: 0.18,
            h: 0.18,
            fill: { color },
            line: { color: C.white, width: 0.5 }
        });
    });
}

function addTabs(slide, activeChapter) {
    CHAPTERS.forEach(([roman, title], index) => {
        const active = activeChapter === index;
        const x = 0.64 + index * 2.42;
        slide.addShape(ShapeType.roundRect, {
            x,
            y: 1.02,
            w: 2.2,
            h: 0.38,
            rectRadius: 0.04,
            fill: { color: active ? C.white : C.inset, transparency: active ? 2 : 15 },
            line: { color: active ? C.white : C.line, width: 0.7 }
        });
        slide.addText(`${roman}  ${title}`, {
            x: x + 0.08,
            y: 1.115,
            w: 2.04,
            h: 0.15,
            fontFace: "Noto Sans Mono",
            fontSize: 7.2,
            bold: active,
            color: active ? C.navy : C.muted,
            align: "center",
            margin: 0
        });
    });
}

function addStatusBar(slide, number, status) {
    slide.addShape(ShapeType.roundRect, {
        x: 0.44,
        y: 6.82,
        w: 12.45,
        h: 0.27,
        rectRadius: 0.035,
        fill: { color: C.inset, transparency: 12 },
        line: { color: C.line, width: 0.6 }
    });
    slide.addShape(ShapeType.ellipse, {
        x: 0.63,
        y: 6.895,
        w: 0.12,
        h: 0.12,
        fill: { color: C.green },
        line: { color: C.greenDark, width: 0.5 }
    });
    slide.addText(status, {
        x: 0.84,
        y: 6.875,
        w: 9.8,
        h: 0.13,
        fontFace: "Noto Sans Mono",
        fontSize: 6.8,
        color: C.navy,
        margin: 0
    });
    slide.addText(`${String(number).padStart(2, "0")} / 10`, {
        x: 11.65,
        y: 6.87,
        w: 0.9,
        h: 0.14,
        fontFace: "Noto Sans Mono",
        fontSize: 6.8,
        bold: true,
        color: C.navy,
        align: "right",
        margin: 0
    });
}

function addChrome(slide, number, chapter, address, status) {
    addWindowBackground(slide);
    addTitleBar(slide, address);
    addTabs(slide, chapter);
    addStatusBar(slide, number, status);
}

function addHeading(slide, eyebrow, title, subtitle = "", options = {}) {
    slide.addText(eyebrow.toUpperCase(), {
        x: 0.72,
        y: options.eyebrowY || 1.55,
        w: 7.8,
        h: 0.2,
        fontFace: "Noto Sans Mono",
        fontSize: 8,
        bold: true,
        color: options.accent || C.blue,
        charSpacing: 0.9,
        margin: 0
    });
    slide.addText(title, {
        x: 0.72,
        y: options.titleY || 1.78,
        w: options.titleW || 11.85,
        h: options.titleH || 0.64,
        fontFace: "Trebuchet MS",
        fontSize: options.titleSize || 29,
        bold: true,
        color: C.ink,
        margin: 0,
        valign: "mid",
        breakLine: false
    });
    if (subtitle) {
        slide.addText(subtitle, {
            x: 0.74,
            y: options.subtitleY || 2.42,
            w: options.subtitleW || 11.5,
            h: options.subtitleH || 0.28,
            fontFace: "Noto Sans",
            fontSize: options.subtitleSize || 10.5,
            color: C.muted,
            margin: 0,
            valign: "mid"
        });
    }
}

function addGlassCard(slide, config) {
    const {
        x,
        y,
        w,
        h,
        label = "",
        title,
        body = "",
        accent = C.blue,
        fill = C.white,
        titleSize = 15,
        bodySize = 9.5,
        align = "left"
    } = config;
    slide.addShape(ShapeType.roundRect, {
        x,
        y,
        w,
        h,
        rectRadius: 0.05,
        fill: { color: fill, transparency: 4 },
        line: { color: C.white, width: 1.1 }
    });
    slide.addShape(ShapeType.roundRect, {
        x: x + 0.02,
        y: y + 0.02,
        w: w - 0.04,
        h: 0.14,
        rectRadius: 0.04,
        fill: { color: C.white, transparency: 48 },
        line: { color: C.white, transparency: 100 }
    });
    slide.addShape(ShapeType.rect, {
        x,
        y,
        w: 0.07,
        h,
        fill: { color: accent },
        line: { color: accent }
    });
    const runs = [];
    if (label) {
        runs.push({
            text: label.toUpperCase(),
            options: {
                fontFace: "Noto Sans Mono",
                fontSize: 7,
                bold: true,
                color: accent,
                charSpacing: 0.8,
                breakLine: true,
                paraSpaceAfterPt: 4
            }
        });
    }
    runs.push({
        text: title,
        options: {
            fontFace: "Trebuchet MS",
            fontSize: titleSize,
            bold: true,
            color: C.ink,
            breakLine: Boolean(body),
            paraSpaceAfterPt: body ? 4 : 0
        }
    });
    if (body) {
        runs.push({
            text: body,
            options: {
                fontFace: "Noto Sans",
                fontSize: bodySize,
                color: C.muted
            }
        });
    }
    slide.addText(runs, {
        x: x + 0.2,
        y: y + 0.12,
        w: w - 0.36,
        h: h - 0.24,
        margin: 0,
        align,
        valign: "mid",
        breakLine: false
    });
}

function addGelPill(slide, text, x, y, w, options = {}) {
    const h = options.h || 0.42;
    const color = options.color || C.blue;
    slide.addShape(ShapeType.roundRect, {
        x,
        y,
        w,
        h,
        rectRadius: 0.08,
        fill: { color },
        line: { color: options.line || color, width: 0.7 }
    });
    slide.addShape(ShapeType.roundRect, {
        x: x + 0.05,
        y: y + 0.04,
        w: w - 0.1,
        h: h * 0.34,
        rectRadius: 0.05,
        fill: { color: C.white, transparency: 55 },
        line: { color: C.white, transparency: 100 }
    });
    slide.addText(text, {
        x: x + 0.1,
        y: y + 0.1,
        w: w - 0.2,
        h: h - 0.18,
        fontFace: options.mono ? "Noto Sans Mono" : "Noto Sans",
        fontSize: options.fontSize || 9,
        bold: true,
        color: options.textColor || C.white,
        align: "center",
        valign: "mid",
        margin: 0
    });
}

function addProcess(slide, steps, box, options = {}) {
    const gap = options.gap || 0.12;
    const w = (box.w - gap * (steps.length - 1)) / steps.length;
    steps.forEach((step, index) => {
        const x = box.x + index * (w + gap);
        slide.addShape(ShapeType.roundRect, {
            x,
            y: box.y,
            w,
            h: box.h,
            rectRadius: 0.04,
            fill: { color: options.fill || C.white, transparency: 3 },
            line: { color: options.line || C.line, width: 0.8 }
        });
        slide.addText([
            {
                text: String(index + 1).padStart(2, "0"),
                options: {
                    fontFace: "Noto Sans Mono",
                    fontSize: 7,
                    bold: true,
                    color: options.accent || C.blue,
                    breakLine: true,
                    paraSpaceAfterPt: 4
                }
            },
            {
                text: step,
                options: {
                    fontFace: "Trebuchet MS",
                    fontSize: options.fontSize || 11.5,
                    bold: true,
                    color: C.ink
                }
            }
        ], {
            x: x + 0.07,
            y: box.y + 0.08,
            w: w - 0.14,
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
                h: 0.22,
                fontFace: "Trebuchet MS",
                fontSize: 10,
                bold: true,
                color: options.accent || C.blue,
                align: "center",
                margin: 0
            });
        }
    });
}

function addImagePanel(slide, image, box, label, options = {}) {
    slide.addShape(ShapeType.roundRect, {
        x: box.x,
        y: box.y,
        w: box.w,
        h: box.h,
        rectRadius: 0.05,
        fill: { color: options.fill || C.white },
        line: { color: options.line || C.white, width: 1.0 }
    });
    if (label) {
        slide.addText(label.toUpperCase(), {
            x: box.x + 0.16,
            y: box.y + 0.12,
            w: box.w - 0.32,
            h: 0.18,
            fontFace: "Noto Sans Mono",
            fontSize: 7,
            bold: true,
            color: options.labelColor || C.blue,
            charSpacing: 0.7,
            margin: 0
        });
    }
    const top = label ? 0.38 : 0.16;
    addContainedImage(slide, image, {
        x: box.x + 0.16,
        y: box.y + top,
        w: box.w - 0.32,
        h: box.h - top - 0.16
    });
}

function addBulletPanel(slide, config) {
    slide.addShape(ShapeType.roundRect, {
        x: config.x,
        y: config.y,
        w: config.w,
        h: config.h,
        rectRadius: 0.06,
        fill: { color: config.fill || C.white, transparency: 3 },
        line: { color: C.white, width: 1.0 }
    });
    slide.addText(config.title, {
        x: config.x + 0.25,
        y: config.y + 0.2,
        w: config.w - 0.5,
        h: 0.36,
        fontFace: "Trebuchet MS",
        fontSize: 18,
        bold: true,
        color: config.accent || C.blue,
        margin: 0
    });
    config.items.forEach((item, index) => {
        slide.addShape(ShapeType.ellipse, {
            x: config.x + 0.3,
            y: config.y + 0.85 + index * 0.55,
            w: 0.14,
            h: 0.14,
            fill: { color: config.accent || C.blue },
            line: { color: config.accent || C.blue }
        });
        slide.addText(item, {
            x: config.x + 0.58,
            y: config.y + 0.76 + index * 0.55,
            w: config.w - 0.88,
            h: 0.32,
            fontFace: "Noto Sans",
            fontSize: 12,
            color: C.ink,
            margin: 0,
            valign: "mid"
        });
    });
}

function addNotes(slide, text) {
    slide.addNotes(text.replace(/\s+/g, " ").trim());
}

// 1. Portada
{
    const slide = pptx.addSlide();
    addWindowBackground(slide);
    addTitleBar(slide, "baseaccess://defensa/control-documental");
    slide.addShape(ShapeType.roundRect, {
        x: 0.72,
        y: 1.18,
        w: 2.35,
        h: 0.72,
        rectRadius: 0.04,
        fill: { color: C.white },
        line: { color: C.white }
    });
    addContainedImage(slide, IMG.iutecp, { x: 0.88, y: 1.32, w: 2.03, h: 0.44 });
    slide.addText("REPÚBLICA BOLIVARIANA DE VENEZUELA\nMINISTERIO DEL PODER POPULAR PARA LA EDUCACIÓN UNIVERSITARIA\nINSTITUTO UNIVERSITARIO DE TECNOLOGÍA “ELÍAS CALIXTO POMPA”\nEL TIGRE · ESTADO ANZOÁTEGUI", {
        x: 3.28,
        y: 1.15,
        w: 6.7,
        h: 0.8,
        fontFace: "Noto Sans",
        fontSize: 6.8,
        bold: true,
        color: C.navy,
        align: "center",
        margin: 0.02,
        breakLine: false
    });
    slide.addShape(ShapeType.roundRect, {
        x: 10.55,
        y: 1.12,
        w: 1.58,
        h: 1.58,
        rectRadius: 0.08,
        fill: { color: C.white },
        line: { color: C.white, width: 1.0 }
    });
    addContainedImage(slide, IMG.venangocupet, { x: 10.69, y: 1.26, w: 1.3, h: 1.3 });
    slide.addText("DESARROLLO DE UN PROTOTIPO DE SISTEMA PARA EL CONTROL, TRAZABILIDAD Y REPORTE DOCUMENTAL EN LA PRESIDENCIA DE LA EMPRESA MIXTA PETROLERA VENANGOCUPET, S.A.", {
        x: 1.0,
        y: 2.35,
        w: 11.3,
        h: 2.05,
        fontFace: "Trebuchet MS",
        fontSize: 23.5,
        bold: true,
        color: C.ink,
        align: "center",
        valign: "mid",
        margin: 0,
        breakLine: false
    });
    slide.addShape(ShapeType.roundRect, {
        x: 0.83,
        y: 4.86,
        w: 5.45,
        h: 1.28,
        rectRadius: 0.05,
        fill: { color: C.white, transparency: 16 },
        line: { color: C.white, width: 0.9 }
    });
    slide.addText([
        { text: "TUTOR INDUSTRIAL\n", options: { fontFace: "Noto Sans Mono", fontSize: 7, bold: true, color: C.blue } },
        { text: "Ing. Yasmin Sabaneta · C.I. 14.187.924\n\n", options: { fontFace: "Noto Sans", fontSize: 9.5, color: C.ink } },
        { text: "TUTOR ACADÉMICO\n", options: { fontFace: "Noto Sans Mono", fontSize: 7, bold: true, color: C.blue } },
        { text: "Ing. José Mejías · C.I. 4.273.815", options: { fontFace: "Noto Sans", fontSize: 9.5, color: C.ink } }
    ], {
        x: 1.08,
        y: 5.04,
        w: 4.95,
        h: 0.93,
        margin: 0,
        breakLine: false,
        valign: "mid"
    });
    slide.addShape(ShapeType.roundRect, {
        x: 7.05,
        y: 4.86,
        w: 5.45,
        h: 1.28,
        rectRadius: 0.05,
        fill: { color: C.white, transparency: 16 },
        line: { color: C.white, width: 0.9 }
    });
    slide.addText([
        { text: "AUTOR\n", options: { fontFace: "Noto Sans Mono", fontSize: 7, bold: true, color: C.blue } },
        { text: "Juliano Cardona\n", options: { fontFace: "Trebuchet MS", fontSize: 15, bold: true, color: C.ink } },
        { text: "C.I. 32.281.199 · Informática · IUTECP · 2026", options: { fontFace: "Noto Sans", fontSize: 9.5, color: C.muted } }
    ], {
        x: 7.35,
        y: 5.02,
        w: 4.85,
        h: 0.92,
        margin: 0,
        breakLine: false,
        valign: "mid",
        align: "right"
    });
    addStatusBar(slide, 1, "BASEACCESS · prototipo funcional · defensa de pasantías");
    addNotes(slide, "Muy buenas tardes. Presentarse como Juliano Cardona, estudiante de Informática del IUTECP. Indicar que las pasantías se realizaron en la Empresa Mixta Petrolera Venangocupet, S.A., específicamente en el Departamento de Presidencia. Leer el título oficial y explicar que el proyecto se centró en el control de los movimientos documentales mediante un prototipo llamado BaseAccess. Anticipar que la exposición seguirá los cinco capítulos del informe.");
}

// 2. Agenda
{
    const slide = pptx.addSlide();
    addChrome(slide, 2, null, "baseaccess://defensa/agenda", "Ruta cargada · cinco capítulos");
    addHeading(slide, "Agenda", "Ruta de la exposición", "Empresa → Problema → Fundamentos → Desarrollo → Resultados", {
        titleY: 1.68,
        subtitleY: 2.32
    });
    const items = [
        ["CAPÍTULO I", "Realidad organizacional"],
        ["CAPÍTULO II", "Diagnóstico situacional"],
        ["CAPÍTULO III", "Marco teórico"],
        ["CAPÍTULO IV", "Actividades realizadas"],
        ["CAPÍTULO V", "Conclusiones y recomendaciones"]
    ];
    items.forEach(([label, title], index) => {
        addGlassCard(slide, {
            x: 0.67 + index * 2.51,
            y: 3.22,
            w: 2.31,
            h: 2.15,
            label,
            title,
            titleSize: 14.5,
            align: "center",
            accent: index === 3 ? C.green : C.blue,
            fill: index === 3 ? "EAF8DE" : C.white
        });
    });
    addNotes(slide, "Presentar la agenda sin leer cada tarjeta. Explicar que primero se describirá la empresa y el área, luego la situación problemática y los objetivos, después los fundamentos teóricos, el desarrollo técnico del prototipo y finalmente los resultados con recomendaciones.");
}

// 3. Empresa y área
{
    const slide = pptx.addSlide();
    addChrome(slide, 3, 0, "baseaccess://capitulo-1/presidencia", "Proceso real identificado · recepción a despacho");
    addHeading(slide, "Capítulo I · Realidad organizacional", "Empresa y área de pasantía");
    slide.addShape(ShapeType.roundRect, {
        x: 0.72,
        y: 2.52,
        w: 2.55,
        h: 2.55,
        rectRadius: 0.08,
        fill: { color: C.white },
        line: { color: C.white, width: 1.1 }
    });
    addContainedImage(slide, IMG.venangocupet, { x: 0.9, y: 2.7, w: 2.19, h: 2.19 });
    [
        ["EMPRESA", "Empresa Mixta Petrolera Venangocupet, S.A."],
        ["SECTOR", "Hidrocarburos"],
        ["ÁREA", "Departamento de Presidencia"]
    ].forEach(([label, title], index) => {
        addGlassCard(slide, {
            x: 3.62,
            y: 2.48 + index * 0.9,
            w: 8.93,
            h: 0.72,
            label,
            title,
            titleSize: 14.5,
            accent: index === 2 ? C.green : C.blue,
            fill: index === 2 ? "EAF8DE" : C.white
        });
    });
    addProcess(slide, ["Recepción", "Revisión", "Registro", "Firma", "Egreso", "Despacho"], {
        x: 0.72,
        y: 5.42,
        w: 11.84,
        h: 0.92
    }, {
        fontSize: 10.5,
        gap: 0.1
    });
    addNotes(slide, "Explicar que Venangocupet fue constituida en 2012 y desarrolla actividades del sector de hidrocarburos. Las pasantías se realizaron en Presidencia, un punto de recepción, revisión, firma y despacho de correspondencia ejecutiva. Describir el recorrido observado: recepción, revisión ortográfica y de formato, registro, firma, egreso y despacho. Señalar que conocer el proceso real fue necesario antes de diseñar la solución.");
}

// 4. Situación problemática
{
    const slide = pptx.addSlide();
    addChrome(slide, 4, 1, "baseaccess://capitulo-2/diagnostico", "Oportunidad detectada · automatización limitada");
    addHeading(slide, "Capítulo II · Diagnóstico situacional", "Del registro manual al control automatizado");
    addBulletPanel(slide, {
        x: 0.75,
        y: 2.52,
        w: 5.75,
        h: 3.0,
        title: "Situación actual",
        accent: C.blue,
        items: [
            "Registros en hojas de cálculo",
            "Copiado repetitivo de datos",
            "Filtrado y consolidación manual",
            "Resúmenes preparados bajo demanda"
        ]
    });
    addBulletPanel(slide, {
        x: 6.82,
        y: 2.52,
        w: 5.75,
        h: 3.0,
        title: "Efectos posibles",
        accent: C.wine,
        fill: C.redLight,
        items: [
            "Duplicidad u omisión de movimientos",
            "Demoras en registro y consulta",
            "Menor trazabilidad del expediente",
            "Reportes no inmediatos"
        ]
    });
    slide.addText("“El control existía; la oportunidad estaba en automatizarlo.”", {
        x: 1.05,
        y: 5.83,
        w: 11.2,
        h: 0.44,
        fontFace: "Trebuchet MS",
        fontSize: 17,
        bold: true,
        italic: true,
        color: C.navy,
        align: "center",
        margin: 0
    });
    addNotes(slide, "Explicar que el control ya existía mediante hojas de cálculo, pero requería transcripción, actualización de estados, filtros y consolidaciones manuales. Cuando aumenta la cantidad de expedientes, esas tareas pueden generar duplicidades, omisiones, demoras y dificultad para responder rápidamente cuántos documentos ingresaron, cuáles están pendientes o cuál fue el recorrido de un expediente. La oportunidad de mejora fue automatizar registro, seguimiento y reportes.");
}

// 5. Árbol del problema y objetivos
{
    const slide = pptx.addSlide();
    addChrome(slide, 5, 1, "baseaccess://capitulo-2/arbol-y-objetivos", "Diagnóstico conectado con cuatro objetivos");
    addHeading(slide, "Capítulo II · Problema y objetivos", "Del diagnóstico al plan de desarrollo");
    addImagePanel(slide, IMG.problemTree, {
        x: 0.72,
        y: 2.5,
        w: 7.25,
        h: 3.9
    }, "Árbol del problema", { line: C.white, labelColor: C.wine });
    addGlassCard(slide, {
        x: 8.25,
        y: 2.5,
        w: 4.32,
        h: 1.18,
        label: "OBJETIVO GENERAL",
        title: "Desarrollar un prototipo automatizado",
        body: "Control, trazabilidad y reporte documental.",
        titleSize: 15,
        bodySize: 9,
        accent: C.green,
        fill: "EAF8DE"
    });
    [
        "Diagnosticar",
        "Determinar requerimientos",
        "Diseñar",
        "Implementar y validar"
    ].forEach((text, index) => {
        addGelPill(slide, `${String(index + 1).padStart(2, "0")}  ${text}`, 8.25, 3.92 + index * 0.58, 4.32, {
            h: 0.44,
            color: index === 3 ? C.green : C.blue,
            fontSize: 9,
            mono: true
        });
    });
    addNotes(slide, "Presentar el árbol del problema como una herramienta para separar causas, problema central y efectos. Resumir las causas en transcripción repetitiva, falta de validaciones y dependencia de hojas de cálculo; y los efectos en demoras, reportes no inmediatos y menor trazabilidad. Leer el objetivo general y recordar la secuencia de los cuatro objetivos: diagnosticar, determinar requerimientos, diseñar, implementar y validar.");
}

// 6. Fundamentos
{
    const slide = pptx.addSlide();
    addChrome(slide, 6, 2, "baseaccess://capitulo-3/fundamentos", "Marco conceptual cargado · cuatro fundamentos");
    addHeading(slide, "Capítulo III · Marco teórico", "Cuatro fundamentos del prototipo");
    [
        ["01", "Sistemas de información", "Capturar, almacenar, procesar y presentar datos."],
        ["02", "Gestión documental", "Controlar el ciclo y recorrido de los documentos."],
        ["03", "Modelo relacional", "Organizar información mediante tablas relacionadas."],
        ["04", "Trazabilidad documental", "Reconstruir el historial de cada expediente."]
    ].forEach(([label, title, body], index) => {
        addGlassCard(slide, {
            x: index % 2 === 0 ? 0.75 : 6.72,
            y: index < 2 ? 2.53 : 4.12,
            w: 5.85,
            h: 1.3,
            label,
            title,
            body,
            titleSize: 17,
            bodySize: 10,
            accent: index === 3 ? C.green : C.blue,
            fill: index === 3 ? "EAF8DE" : C.white
        });
    });
    slide.addText("DATOS  →  ORGANIZACIÓN  →  HISTORIAL  →  INFORMACIÓN ÚTIL", {
        x: 1.1,
        y: 5.82,
        w: 11.15,
        h: 0.38,
        fontFace: "Noto Sans Mono",
        fontSize: 11,
        bold: true,
        color: C.navy,
        align: "center",
        margin: 0
    });
    addNotes(slide, "Explicar solamente los cuatro fundamentos más relacionados con BaseAccess. Un sistema de información captura y presenta datos; la gestión documental controla el recorrido; el modelo relacional organiza entidades sin repetir toda la información; y la trazabilidad permite reconstruir movimientos, fechas, estados y responsables. Mencionar SQLite como implementación de la base de datos relacional.");
}

// 7. Desarrollo
{
    const slide = pptx.addSlide();
    addChrome(slide, 7, 3, "baseaccess://capitulo-4/desarrollo", "Nueve semanas resumidas en cuatro etapas");
    addHeading(slide, "Capítulo IV · Actividades realizadas", "Cuatro etapas de desarrollo", "Diagnóstico → diseño → implementación → validación");
    [
        ["1 · DIAGNÓSTICO", "Flujo actual + requerimientos", "Observar Presidencia y definir necesidades."],
        ["2 · DISEÑO", "Modelo relacional + interfaz", "Normalización, diccionario de datos y pantallas."],
        ["3 · IMPLEMENTACIÓN", "SQLite + escritorio + Wails", "Registro, consulta, historial y reportes."],
        ["4 · VALIDACIÓN", "Pruebas + depuración + documentación", "Datos representativos y revisión funcional."]
    ].forEach(([label, title, body], index) => {
        addGlassCard(slide, {
            x: 0.71 + index * 3.02,
            y: 2.82,
            w: 2.8,
            h: 2.42,
            label,
            title,
            body,
            titleSize: 16,
            bodySize: 9.3,
            accent: index === 3 ? C.green : C.blue,
            fill: index === 3 ? "EAF8DE" : C.white,
            align: "center"
        });
    });
    addGelPill(slide, "DIAGNOSTICAR", 1.0, 5.66, 2.35, { mono: true, fontSize: 8.5 });
    addGelPill(slide, "DISEÑAR", 3.98, 5.66, 2.35, { mono: true, fontSize: 8.5 });
    addGelPill(slide, "CONSTRUIR", 6.96, 5.66, 2.35, { mono: true, fontSize: 8.5 });
    addGelPill(slide, "PROBAR", 9.94, 5.66, 2.35, { color: C.green, mono: true, fontSize: 8.5 });
    addNotes(slide, "Resumir las nueve semanas en cuatro etapas. Primero se observó el flujo y se levantaron requerimientos. Después se diseñó la base de datos relacional y la interfaz. Luego se implementó BaseAccess como aplicación de escritorio con Wails y SQLite. Finalmente se probaron registro, consulta, historial y reportes, se corrigieron errores y se preparó documentación técnica y de usuario.");
}

// 8. Arquitectura
{
    const slide = pptx.addSlide();
    addChrome(slide, 8, 3, "baseaccess://prototipo/arquitectura", "BaseAccess en ejecución · arquitectura local");
    addHeading(slide, "Capítulo IV · Resultado técnico", "BaseAccess · prototipo funcional", "Una aplicación de escritorio que conserva el historial verificable del expediente.");
    addGelPill(slide, "APLICACIÓN DE ESCRITORIO", 1.0, 2.72, 3.25, { mono: true, fontSize: 8.5 });
    addGelPill(slide, "WAILS + WEBVIEW2", 5.04, 2.72, 3.25, { color: C.green, mono: true, fontSize: 8.5 });
    addGelPill(slide, "SQLITE LOCAL", 9.08, 2.72, 3.25, { mono: true, fontSize: 8.5 });
    addImagePanel(slide, IMG.architecture, {
        x: 0.75,
        y: 3.35,
        w: 11.82,
        h: 1.75
    }, "Arquitectura lógica", { line: C.white, labelColor: C.wine });
    ["Registro", "Consulta", "Historial", "Reportes"].forEach((text, index) => {
        addGlassCard(slide, {
            x: 1.0 + index * 3.0,
            y: 5.42,
            w: 2.65,
            h: 0.72,
            label: `MÓDULO ${index + 1}`,
            title: text,
            titleSize: 14.5,
            align: "center",
            accent: index === 2 ? C.green : C.blue,
            fill: index === 2 ? "EAF8DE" : C.white
        });
    });
    addNotes(slide, "Explicar la arquitectura de izquierda a derecha: el personal utiliza una interfaz visual; Wails integra la aplicación de escritorio; la lógica se encarga de registro, consulta e historial; los reportes se generan con la información almacenada; y SQLite conserva la base de datos local sin requerir un servidor adicional. Destacar los cuatro módulos funcionales: registro, consulta, historial y reportes.");
}

// 9. Demostración
{
    const slide = pptx.addSlide();
    addChrome(slide, 9, 3, "baseaccess://prototipo/demostracion", "Evidencia visual · datos DEMO");
    addHeading(slide, "Capítulo IV · Demostración", "El sistema existe y puede recorrerse", "Tres evidencias del prototipo funcional.");
    addImagePanel(slide, IMG.form, {
        x: 0.72,
        y: 2.8,
        w: 4.12,
        h: 1.48
    }, "Registro estructurado", { labelColor: C.blue });
    addImagePanel(slide, IMG.fronts, {
        x: 0.72,
        y: 4.48,
        w: 4.12,
        h: 1.48
    }, "Múltiples frentes", { labelColor: C.green });
    addImagePanel(slide, IMG.reports, {
        x: 5.08,
        y: 2.8,
        w: 7.5,
        h: 3.16
    }, "Reportes y filtros", { labelColor: C.wine });
    slide.addText("REGISTRO  →  CONSULTA  →  TRAZABILIDAD  →  REPORTE", {
        x: 1.0,
        y: 6.22,
        w: 11.3,
        h: 0.28,
        fontFace: "Noto Sans Mono",
        fontSize: 10,
        bold: true,
        color: C.navy,
        align: "center",
        margin: 0
    });
    addNotes(slide, "Mostrar que BaseAccess no quedó solamente en diagramas. Señalar el formulario de registro, la posibilidad de asociar varios documentos o frentes a un expediente y la exportación con filtros. Explicar que durante la validación se utilizaron datos representativos y se comprobaron los módulos. Aclarar que se obtuvo un prototipo funcional, no una plataforma empresarial definitiva.");
}

// 10. Conclusiones y recomendaciones
{
    const slide = pptx.addSlide();
    addChrome(slide, 10, 4, "baseaccess://capitulo-5/resultados", "Proceso completado · prototipo validado");
    addHeading(slide, "Capítulo V · Conclusiones y recomendaciones", "Resultados y siguientes pasos");
    [
        ["1 · DIAGNÓSTICO", "Operaciones manuales repetitivas"],
        ["2 · REQUERIMIENTOS", "Registro + historial + consultas + reportes"],
        ["3 · DISEÑO", "Base relacional + interfaz de escritorio"],
        ["4 · RESULTADO", "Prototipo funcional validado"]
    ].forEach(([label, title], index) => {
        addGlassCard(slide, {
            x: 0.72 + index * 3.02,
            y: 2.5,
            w: 2.8,
            h: 1.25,
            label,
            title,
            titleSize: 13.5,
            align: "center",
            accent: index === 3 ? C.green : C.blue,
            fill: index === 3 ? "EAF8DE" : C.white
        });
    });
    addBulletPanel(slide, {
        x: 0.72,
        y: 4.05,
        w: 6.35,
        h: 2.12,
        title: "Recomendaciones para Venangocupet",
        accent: C.blue,
        items: [
            "Migración gradual de registros históricos",
            "Capacitación del personal",
            "Respaldos periódicos de SQLite"
        ]
    });
    slide.addShape(ShapeType.roundRect, {
        x: 7.36,
        y: 4.05,
        w: 5.2,
        h: 2.12,
        rectRadius: 0.06,
        fill: { color: C.white, transparency: 3 },
        line: { color: C.white, width: 1.0 }
    });
    slide.addText("“La información ya existía; BaseAccess busca hacerla más fácil de registrar, consultar y seguir.”", {
        x: 7.7,
        y: 4.3,
        w: 4.52,
        h: 1.0,
        fontFace: "Trebuchet MS",
        fontSize: 15,
        bold: true,
        color: C.navy,
        align: "center",
        valign: "mid",
        margin: 0
    });
    slide.addText("Gracias por su atención.", {
        x: 7.72,
        y: 5.42,
        w: 4.48,
        h: 0.34,
        fontFace: "Trebuchet MS",
        fontSize: 17,
        bold: true,
        color: C.blue,
        align: "center",
        margin: 0
    });
    slide.addText("Quedo atento a sus preguntas.", {
        x: 7.72,
        y: 5.8,
        w: 4.48,
        h: 0.22,
        fontFace: "Noto Sans",
        fontSize: 9,
        color: C.muted,
        align: "center",
        margin: 0
    });
    addNotes(slide, "Relacionar las conclusiones con los cuatro objetivos: se diagnosticaron las limitaciones del control manual; se determinaron requerimientos de registro, historial, consulta y reportes; se diseñó una base relacional y una interfaz adaptada al flujo; y se implementó y validó un prototipo funcional. Recomendar migración gradual, capacitación y respaldos periódicos. Cerrar explicando que BaseAccess organiza información ya existente para facilitar su registro, consulta y seguimiento. Agradecer al jurado, a Venangocupet, al IUTECP y a los tutores.");
}

async function main() {
    await pptx.writeFile({ fileName: SALIDA, compression: true });
    console.log(`Presentación generada: ${SALIDA}`);
    console.log("Diapositivas: 10");
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
