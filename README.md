# Blog · Casos cotidianos de uso de IA — primeras entradas

## Qué hay aquí

```
_posts/
  2026-10-26-litoques-un-disco-hecho-en-casa-con-ia.md   ← entrada 1
  2026-10-26-delito-libro-ilustrado-con-ia.md            ← entrada 2
assets/
  css/casos-ia.css          ← estilos de los bloques Problema · Proceso · Solución
  img/litoques/*.svg|png    ← cabecera + 6 diagramas
  img/delito/*.svg|png      ← cabecera + 5 diagramas
_notas-editoriales/         ← títulos alternativos, SEO, ideas para redes y hechos a verificar
                              (empieza por "_", así que Jekyll NO la publica)
```

## Cómo añadirlo a tu repositorio de GitHub Pages

1. Copia `_posts/` y `assets/` a la raíz del repositorio (fusionando con lo que ya tengas).
2. Haz commit y push. GitHub Pages construye el sitio solo.

No hace falta tocar el tema: cada post enlaza su propia hoja de estilos con `relative_url`, así que funciona igual en un sitio de usuario (`usuario.github.io`) que en uno de proyecto (`usuario.github.io/blog`), siempre que `baseurl` esté bien puesto en `_config.yml`.

## Requisitos mínimos de `_config.yml`

```yaml
lang: es
markdown: kramdown        # el que usa GitHub Pages por defecto
# Opcional, para URLs limpias del tipo /litoques-un-disco-hecho-en-casa-con-ia/
permalink: /:title/
plugins:
  - jekyll-seo-tag        # usa el campo `image:` como imagen al compartir en redes
```

## Bloques visuales disponibles para próximas entradas

```html
<div class="bloque bloque-problema" markdown="1">…</div>
<div class="bloque bloque-proceso" markdown="1">…</div>
<div class="bloque bloque-solucion" markdown="1">…</div>
<div class="bloque bloque-aprendizaje" markdown="1">…</div>
<div class="bloque bloque-rigor" markdown="1">…</div>

<span class="etiqueta hecho">Hecho</span>
<span class="etiqueta propuesta">Propuesta</span>
<span class="etiqueta pendiente">Por verificar</span>
<span class="etiqueta futuro">Posibilidad futura</span>
```

Los bloques se adaptan al modo oscuro y las figuras se pueden tocar en el móvil para verlas a tamaño completo.
