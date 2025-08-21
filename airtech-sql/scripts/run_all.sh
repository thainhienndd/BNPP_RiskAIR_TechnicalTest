#!/usr/bin/env bash
set -euo pipefail

DB_NAME="${DB_NAME:-airtech_test}"
Q_DIR="queries"
OUT_DIR="results"

mkdir -p "$OUT_DIR"

run() {
  local qfile="$1"
  local base="$(basename "$qfile" .sql)"
  echo "[RUN] $qfile -> $OUT_DIR/${base}.csv"
  psql "$DB_NAME" -v ON_ERROR_STOP=1 -At -F',' \
    -c "\COPY ($(cat "$qfile")) TO STDOUT WITH CSV HEADER" > "$OUT_DIR/${base}.csv"
}

shopt -s nullglob
sql_files=("$Q_DIR"/*.sql)

if (( ${#sql_files[@]} == 0 )); then
  echo "Aucun fichier .sql trouvé dans: $Q_DIR"
  exit 1
fi

for q in "${sql_files[@]}"; do
  run "$q"
done

echo "Done. Résultats CSV dans $OUT_DIR/"
