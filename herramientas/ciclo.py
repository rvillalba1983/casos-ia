"""Diagrama de ciclo: pasos dispuestos en círculo con flechas, centro con lema."""
import math, sys, json, textwrap
from xml.sax.saxutils import escape

def ciclo(cfg):
    W, H = 1200, cfg.get("H", 830)
    cx, cy, R = 600, cfg.get("cy", 410), cfg.get("R", 270)
    pasos = cfg["pasos"]
    n = len(pasos)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
           f'<rect width="{W}" height="{H}" fill="{cfg["fondo"]}"/>',
           f'<text x="{W/2}" y="56" text-anchor="middle" font-family="Georgia, serif" font-size="30" font-style="italic" fill="{cfg["tinta"]}">{escape(cfg["titulo"])}</text>',
           f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{cfg["tinta"]}" stroke-opacity="0.18" stroke-width="3" stroke-dasharray="10 8"/>']
    # flechas sobre el círculo
    for i in range(n):
        a = -math.pi/2 + (i + 0.5) * 2*math.pi/n
        x, y = cx + R*math.cos(a), cy + R*math.sin(a)
        ang = math.degrees(a) + 90
        out.append(f'<path d="M-9 -8 L9 0 L-9 8 z" transform="translate({x:.1f} {y:.1f}) rotate({ang:.1f})" fill="{cfg["tinta"]}" opacity="0.5"/>')
    for i, (titulo, texto, color, quien) in enumerate(pasos):
        a = -math.pi/2 + i * 2*math.pi/n
        x, y = cx + R*math.cos(a), cy + R*math.sin(a)
        bw, bh = cfg.get("bw", 230), 104
        out.append(f'<rect x="{x-bw/2:.1f}" y="{y-bh/2:.1f}" width="{bw}" height="{bh}" rx="14" fill="#fff" stroke="{color}" stroke-width="2.5"/>')
        out.append(f'<circle cx="{x-bw/2+24:.1f}" cy="{y-bh/2+24:.1f}" r="15" fill="{color}"/>')
        out.append(f'<text x="{x-bw/2+24:.1f}" y="{y-bh/2+30:.1f}" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="16" font-weight="700" fill="#fff">{i+1}</text>')
        out.append(f'<text x="{x-bw/2+48:.1f}" y="{y-bh/2+30:.1f}" font-family="Helvetica, Arial, sans-serif" font-size="17" font-weight="700" fill="#2a2622">{escape(titulo)}</text>')
        for j, l in enumerate(textwrap.wrap(texto, 28)[:2]):
            out.append(f'<text x="{x-bw/2+16:.1f}" y="{y-bh/2+60+j*19:.1f}" font-family="Helvetica, Arial, sans-serif" font-size="14.5" fill="#4a4540">{escape(l)}</text>')
        out.append(f'<text x="{x+bw/2-12:.1f}" y="{y+bh/2-10:.1f}" text-anchor="end" font-family="Helvetica, Arial, sans-serif" font-size="11" font-weight="700" letter-spacing="1" fill="{color}">{escape(quien)}</text>')
    for j, l in enumerate(cfg["centro"]):
        out.append(f'<text x="{cx}" y="{cy-10+j*30}" text-anchor="middle" font-family="Georgia, serif" font-size="{24 if j==0 else 18}" font-style="italic" fill="{cfg["tinta"]}">{escape(l)}</text>')
    # leyenda
    lx = 60
    for et, col in cfg["leyenda"]:
        out.append(f'<rect x="{lx}" y="{H-42}" width="16" height="16" rx="4" fill="{col}"/>')
        out.append(f'<text x="{lx+24}" y="{H-29}" font-family="Helvetica, Arial, sans-serif" font-size="14" fill="#4a4540">{escape(et)}</text>')
        lx += 220
    out.append("</svg>")
    open(cfg["ruta"], "w").write("\n".join(out))

if __name__ == "__main__":
    ciclo(json.load(open(sys.argv[1]))); print("ok")
