# Herramientas para los diagramas

No se publican (excluidas en `_config.yml`). Ejecutar desde la raíz del repo.

- `mapa.py <config.json>`: tabla «mapa del caso» con filas por frente y columnas Problema / Proceso / Solución. Ejemplos en `diagramas/mapa-*.json`.
- `ciclo.py <config.json>`: ciclo de pasos en círculo con quién hace cada paso. Ejemplos en `diagramas/ciclo-*.json` (claves opcionales `H`, `cy`, `R`, `bw`).
- `render.py <carpeta_salida> <ficheros.svg|.html>`: renderiza con Playwright (Chromium) a PNG para revisar a ojo. Para las cabeceras, el PNG se copia junto al SVG y se usa como `image:` en el front matter (vista previa en redes).

El resto de diagramas (cabeceras, cadena de audio, cubierta a escala…) se escribieron a mano en SVG: 1200 px de ancho, Georgia para títulos, Helvetica/Arial para etiquetas.
