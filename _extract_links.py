import re
from pathlib import Path

html = Path(r"d:\persnol-website\portfolio-main\index.html").read_text(encoding="utf-8")
body = re.split(r"<script", html, maxsplit=1)[0]
for m in re.finditer(r'<a\s[^>]*href="([^"]+)"[^>]*>(.*?)</a>', body, re.I | re.S):
    href = m.group(1)
    text = re.sub(r"<[^>]+>", "", m.group(2))
    text = re.sub(r"\s+", " ", text).strip()[:100]
    print(href, "|", text)
