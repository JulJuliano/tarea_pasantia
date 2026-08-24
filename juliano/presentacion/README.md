# Presentación de defensa de Juliano

Presentación de **20 diapositivas** generada con Python y Reveal.js. La
narrativa recorre el problema documental, el modelo, la arquitectura, la
interfaz, la validación y el resultado del prototipo BaseAccess.

Los visuales se construyen de forma nativa con HTML y CSS: rutas, flujos,
tarjetas, matrices, expediente, arquitectura e interfaz simplificada. La
presentación no contiene etiquetas `<img>`, no usa rutas relativas de anexos y
no depende de `juliano/imagenes/` para regenerarse.

## Generar

Desde la raíz del repositorio:

```bash
python3 juliano/presentacion/generar_presentacion.py
```

El script genera `juliano/presentacion/index.html` con exactamente 20
secciones y una nota del expositor por diapositiva.

## Presentar

Inicia un servidor desde la raíz del repositorio:

```bash
python3 -m http.server 8000
```

Abre `http://localhost:8000/juliano/presentacion/`. Reveal.js se carga desde
jsDelivr, por lo que la sesión necesita conexión a internet para cargar el
motor de presentación.

Controles útiles:

- Flechas: cambiar de diapositiva.
- `F`: pantalla completa.
- `S`: vista del presentador con notas.
- `Esc`: salir de pantalla completa o de la vista del presentador.

La diapositiva 19, **“Demostración del prototipo”**, está diseñada como una
pausa para cambiar al portátil y ejecutar el recorrido en vivo:
`Registrar -> consultar historial -> exportar reporte`.

La composición es de página completa, sin barra lateral, encabezado, pie,
numeración, barra de progreso ni controles visuales. Adapta el lienzo a
1280x720 en escritorio y 390x844 en móvil, y respeta
`prefers-reduced-motion`.

## GitHub Pages

Cada push a `main` publica automáticamente la presentación mediante
`.github/workflows/deploy-pages.yml`. La URL esperada del repositorio es:

`https://juljuliano.github.io/tarea_pasantia/`
