rom http.server import BaseHTTPRequestHandler, HTTPServer


BRUCINE = {
    "name": "Brucine",
    "formula": "C23H26N2O4",
    "chiral_count": 7,
    "rs": ["C1:S", "C5:R", "C6:S", "C7:S", "C9:R", "C10:R", "C11:S"],
}

STUDENT = {
    "name": "Nalla Hari Hara Krishna",
    "reg_no": "RA2511026050036",
    "dept": "CSE-AIML",
    "sec": "A",
}

ATOMS = [
    ("C1", 0.0, 0.0, 0.0),
    ("C5", 1.4, 0.8, 0.5),
    ("C6", -1.2, 1.0, 0.3),
    ("C7", 0.4, -1.3, 1.0),
    ("C9", 2.2, 1.2, 0.9),
    ("C10", -2.0, 1.7, 0.7),
    ("C11", 1.1, -2.1, 1.8),
    ("O", 0.2, 0.2, -1.6),
    ("N1", -0.9, 2.0, -0.2),
    ("N2", 0.5, -2.4, 0.1),
]

BONDS = [(0, 1), (0, 2), (0, 3), (0, 7), (1, 4), (2, 5), (3, 6), (2, 8), (3, 9)]


def svg_2d() -> str:
    w, h, s, ox, oy = 700, 360, 85, 350, 180
    out = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">']
    out.append(f'<rect x="0" y="0" width="{w}" height="{h}" fill="white" stroke="black"/>')

    def p(idx):
        _, x, y, _ = ATOMS[idx]
        return ox + x * s, oy - y * s

    for i, j in BONDS:
        x1, y1 = p(i)
        x2, y2 = p(j)
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="black"/>')

    for label, x, y, _ in ATOMS:
        px, py = ox + x * s, oy - y * s
        out.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="7" fill="gold" stroke="black"/>')
        out.append(f'<text x="{px+9:.1f}" y="{py-9:.1f}" font-size="12">{label}</text>')

    out.append('<text x="10" y="20" font-size="16">Brucine 2D Structure (Python Generated)</text>')
    out.append('</svg>')
    return "".join(out)


def svg_3d() -> str:
    w, h, s, ox, oy = 700, 420, 90, 350, 230
    proj = []
    for name, x, y, z in ATOMS:
        px = ox + (x - 0.6 * z) * s
        py = oy - (y + 0.45 * z) * s
        proj.append((name, px, py, z))

    out = [f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">']
    out.append(f'<rect x="0" y="0" width="{w}" height="{h}" fill="white" stroke="black"/>')

    for i, j in BONDS:
        a, b = proj[i], proj[j]
        out.append(f'<line x1="{a[1]:.1f}" y1="{a[2]:.1f}" x2="{b[1]:.1f}" y2="{b[2]:.1f}" stroke="black"/>')

    for name, px, py, z in sorted(proj, key=lambda t: t[3]):
        r = 6 + (z + 2.5)
        out.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r:.1f}" fill="lightblue" stroke="black"/>')
        out.append(f'<text x="{px+10:.1f}" y="{py-10:.1f}" font-size="12">{name}</text>')

    out.append('<text x="10" y="20" font-size="16">Brucine 3D Structure (Python Projection)</text>')
    out.append('</svg>')
    return "".join(out)


def page() -> str:
    rs_items = "".join(f"<li>{item}</li>" for item in BRUCINE["rs"])
    return f"""
<!doctype html>
<html>
<head><meta charset='utf-8'><title>Brucine Analyzer</title></head>
<body>
<h1>Brucine Chiral Compound Analyzer (Python)</h1>
<h2>Compound Details</h2>
<p>Name: {BRUCINE['name']}</p>
<p>Molecular Formula: {BRUCINE['formula']}</p>
<p>Number of Chiral Centers: {BRUCINE['chiral_count']}</p>
<h3>R/S Configuration</h3>
<ul>{rs_items}</ul>

<h2>Student Details</h2>
<p>Name: {STUDENT['name']}</p>
<p>Reg No: {STUDENT['reg_no']}</p>
<p>Dept: {STUDENT['dept']}</p>
<p>SEC: {STUDENT['sec']}</p>

<h2>2D Structure</h2>
{svg_2d()}

<h2>3D Structure</h2>
{svg_3d()}
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/":
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")
            return
        content = page().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


def run(host: str = "127.0.0.1", port: int = 8000):
    server = HTTPServer((host, port), Handler)
    print(f"Serving on http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
