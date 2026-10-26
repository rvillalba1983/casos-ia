import sys, pathlib, re
from playwright.sync_api import sync_playwright

out = pathlib.Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    for f in sys.argv[2:]:
        f = pathlib.Path(f).resolve()
        if f.suffix == ".svg":
            m = re.search(r'viewBox="0 0 (\d+) (\d+)"', f.read_text())
            w, h = int(m.group(1)), int(m.group(2))
            pg = b.new_page(viewport={"width": w, "height": h})
            pg.goto(f.as_uri())
            pg.screenshot(path=str(out / (f.parent.name + "-" + f.stem + ".png")))
        else:
            pg = b.new_page(viewport={"width": 420, "height": 900})
            pg.goto(f.as_uri())
            pg.screenshot(path=str(out / (f.stem + ".png")), full_page=True)
        pg.close()
    b.close()
print("ok")
