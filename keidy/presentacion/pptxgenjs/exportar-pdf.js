const path = require("path");
const { spawnSync } = require("child_process");

const CARPETA_PRESENTACION = path.resolve(__dirname, "..");
const archivos = [
    "Defensa_Keidy_10_laminas.pptx",
    "Estudio_Keidy_17_laminas.pptx"
].map((nombre) => path.join(CARPETA_PRESENTACION, nombre));

const resultado = spawnSync(
    "libreoffice",
    ["--headless", "--convert-to", "pdf", "--outdir", CARPETA_PRESENTACION, ...archivos],
    { stdio: "inherit" }
);

if (resultado.error) {
    console.error("No se pudo ejecutar LibreOffice:", resultado.error.message);
    process.exit(1);
}

if (resultado.status !== 0) {
    process.exit(resultado.status || 1);
}

console.log("PDF generados en:", CARPETA_PRESENTACION);
