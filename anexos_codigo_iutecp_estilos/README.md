# Anexos IUTECP generados por codigo

## Estructura

- `juliano/`, `keidy/`, `amaal/`: fuentes Mermaid, PlantUML y GraphViz.
- `*/png/`: imagenes PNG generadas a partir de las fuentes.
- `compose.yaml`: Kroki local con una red Docker fija fuera de la LAN actual.
- `generar_png.sh`: conversor reproducible mediante la API local de Kroki.

## Kroki local

La red `iutecp-kroki` usa `172.31.240.0/24`, que no coincide con la LAN `192.168.10.0/24` ni con la interfaz VPN observada. El gateway se publica solo en `127.0.0.1:8000`.

Desde esta carpeta:

```bash
sudo docker compose -f compose.yaml up -d
./generar_png.sh
```

Para detenerlo:

```bash
sudo docker compose -f compose.yaml down
```

Los informes no se modifican durante esta etapa. Los PNG quedan separados para revisarlos antes de incorporarlos a `*/imagenes/` y regenerar los informes.
