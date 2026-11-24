# 用 _template/page.html 產生兩校網頁：python3 build.py
from pathlib import Path
SCHOOLS = {
    "jiangong": {"SCHOOL": "建功國小", "SITE_URL": ""},
    "shekou":   {"SCHOOL": "社口國小", "SITE_URL": "https://skes.tc.edu.tw/"},
}
root = Path(__file__).parent
tpl = (root / "_template/page.html").read_text(encoding="utf-8")
for folder, v in SCHOOLS.items():
    html = tpl
    for k, val in v.items():
        html = html.replace("{{" + k + "}}", val)
    assert "{{" not in html
    (root / folder / "index.html").write_text(html, encoding="utf-8")
    print("built", folder)
