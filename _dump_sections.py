import re
from pathlib import Path

html = Path(r"d:\persnol-website\portfolio-main\index.html").read_text(encoding="utf-8")
body = re.split(r"<script", html, maxsplit=1)[0]
ids = ["about", "skills", "projects", "contact"]
starts = []
for sid in ids:
    m = re.search(rf'<section id="{sid}"', body)
    starts.append((m.start(), sid))
starts.append((len(body), "end"))
for i in range(len(ids)):
    chunk = body[starts[i][0] : starts[i + 1][0]]
    pretty = re.sub(r"><", ">\n<", chunk)
    Path(rf"d:\persnol-website\portfolio-main\_sec_{ids[i]}.html").write_text(pretty, encoding="utf-8")
    print(ids[i], "lines", pretty.count("\n") + 1)
