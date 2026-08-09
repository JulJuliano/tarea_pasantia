#!/usr/bin/env bash
set -Eeuo pipefail

BASE_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
KROKI_URL="${KROKI_URL:-http://127.0.0.1:8000}"

if ! curl --fail --silent --show-error --connect-timeout 5 "$KROKI_URL" >/dev/null; then
  printf 'Kroki no responde en %s. Inicia compose.yaml antes de continuar.\n' "$KROKI_URL" >&2
  exit 1
fi

render_source() {
  local source="$1"
  local output_dir="$2"
  local extension="${source##*.}"
  local diagram_type
  local output

  case "$extension" in
    mmd) diagram_type=mermaid ;;
    puml) diagram_type=plantuml ;;
    dot) diagram_type=graphviz ;;
    *)
      printf 'Extension no soportada: %s\n' "$source" >&2
      return 1
      ;;
  esac

  output="$output_dir/$(basename "${source%.*}").png"
  printf '%s -> %s\n' "$source" "$output"

  if ! curl --fail-with-body --silent --show-error \
    --connect-timeout 10 --max-time 120 \
    -X POST -H 'Content-Type: text/plain' \
    --data-binary "@$source" \
    "$KROKI_URL/$diagram_type/png" \
    -o "$output"; then
    rm -f "$output"
    return 1
  fi

  if [[ "$(file --brief --mime-type "$output")" != "image/png" ]]; then
    printf 'La respuesta no es un PNG valido: %s\n' "$output" >&2
    rm -f "$output"
    return 1
  fi
}

for student in juliano keidy amaal; do
  source_dir="$BASE_DIR/$student"
  output_dir="$source_dir/png"
  mkdir -p "$output_dir"

  for source in "$source_dir"/*.mmd "$source_dir"/*.puml "$source_dir"/*.dot; do
    [[ -f "$source" ]] || continue
    render_source "$source" "$output_dir"
  done
done

printf 'Anexos PNG generados en %s/{juliano,keidy,amaal}/png.\n' "$BASE_DIR"
