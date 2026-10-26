"""Genera un diagrama 'mapa del caso': filas = frentes, columnas = problema / proceso / solución."""
import textwrap, sys, json
from xml.sax.saxutils import escape

def mapa(titulo, filas, fondo, tinta, ruta):
    W = 1220
    x0, colw, gap = 190, 320, 20
    cols = [("PROBLEMA", "#b5402a", "#fbeee9"), ("PROCESO", "#b7791f", "#fdf5e6"), ("SOLUCIÓN", "#2f7d4f", "#eaf6ee")]
    lh, fs = 22, 16.5
    y = 150
    cuerpo = []
    for nombre, celdas in filas:
        lineas = [textwrap.wrap(c, 34) for c in celdas]
        h = max(len(l) for l in lineas) * lh + 30
        cuerpo.append(f'<text x="{x0-20}" y="{y + h/2 + 6}" text-anchor="end" font-family="Georgia, serif" font-size="21" font-weight="700" fill="{tinta}">{escape(nombre)}</text>')
        for i, (ls, (_, col, bg)) in enumerate(zip(lineas, cols)):
            x = x0 + i * (colw + gap)
            cuerpo.append(f'<rect x="{x}" y="{y}" width="{colw}" height="{h}" rx="10" fill="{bg}" stroke="{col}" stroke-width="1.5"/>')
            cuerpo.append(f'<rect x="{x}" y="{y}" width="6" height="{h}" rx="3" fill="{col}"/>')
            for j, t in enumerate(ls):
                cuerpo.append(f'<text x="{x+20}" y="{y + 28 + j*lh}" font-family="Helvetica, Arial, sans-serif" font-size="{fs}" fill="#2a2622">{escape(t)}</text>')
            if i < 2:
                ax = x + colw + 2
                cuerpo.append(f'<path d="M{ax} {y+h/2-7} l14 7 l-14 7 z" fill="{tinta}" opacity="0.55"/>')
        y += h + 16
    H = y + 30
    cab = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {int(H)}" width="{W}" height="{int(H)}">',
           f'<rect width="{W}" height="{int(H)}" fill="{fondo}"/>',
           f'<text x="{W/2}" y="58" text-anchor="middle" font-family="Georgia, serif" font-size="32" font-style="italic" fill="{tinta}">{escape(titulo)}</text>']
    for i, (n, col, _) in enumerate(cols):
        x = x0 + i * (colw + gap)
        cab.append(f'<rect x="{x}" y="92" width="{colw}" height="36" rx="18" fill="{col}"/>')
        cab.append(f'<text x="{x+colw/2}" y="117" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="17" font-weight="700" letter-spacing="2" fill="#fff">{["① ","② ","③ "][i]}{n}</text>')
    open(ruta, "w").write("\n".join(cab + cuerpo + ["</svg>"]))

if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1]))
    mapa(cfg["titulo"], cfg["filas"], cfg["fondo"], cfg["tinta"], cfg["ruta"])
    print("ok", cfg["ruta"])
