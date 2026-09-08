const path = require("path");
const { spawnSync } = require("child_process");

const CARPETA_PRESENTACION = path.resolve(__dirname, "..");
const ARCHIVO = path.join(CARPETA_PRESENTACION, "Defensa_Juliano_10_laminas.pptx");

const resultado = spawnSync(
    "libreoffice",
    ["--headless", "--convert-to", "pdf", "--outdir", CARPETA_PRESENTACION, ARCHIVO],
    { stdio: "inherit" }
);

if (resultado.error) {
    console.error("No se pudo ejecutar LibreOffice:", resultado.error.message);
    process.exit(1);
}

if (resultado.status !== 0) {
    process.exit(resultado.status || 1);
}

console.log("PDF generado en:", CARPETA_PRESENTACION);
