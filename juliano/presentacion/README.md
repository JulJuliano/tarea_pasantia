# Presentación breve de Juliano

Prototipo de seis diapositivas animadas creado con Python y Reveal.js.

## Generar

Desde la raíz del repositorio:

```bash
python juliano/presentacion/generar_presentacion.py
```

El script genera `juliano/presentacion/index.html` y reutiliza las imágenes de `juliano/imagenes/`.

## Presentar

Para que la presentación pueda acceder a las imágenes de `juliano/imagenes/`, inicia el servidor desde la raíz del repositorio:

```bash
python -m http.server 8000
```

Luego abre `http://localhost:8000/juliano/presentacion/` en el navegador. La presentación requiere conexión a internet para cargar Reveal.js desde jsDelivr.

Controles útiles:

- `F`: pantalla completa.
- `S`: vista del presentador con notas.
- Flechas: cambiar de diapositiva.
