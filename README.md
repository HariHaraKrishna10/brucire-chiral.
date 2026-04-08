# Artemether Chiral Center Analyzer
# Brucine Chiral Compound Analyzer (Python)

A public educational website that visualizes a simplified 3D stereocenter model for **artemether** and lets learners switch between **R** and **S** configuration.
This project uses only Python standard library (no CSS file, no HTML file templates, no external packages).

## Features
- Brucine details
- Number of chiral centers
- R/S configuration list
- Student details
- 2D structure (Python-generated SVG)
- 3D structure (Python-generated SVG projection)

- Interactive 3D viewer (rotate + zoom)
- Toggle between R and S configuration
- Visualized substituent priorities (CIP-style learning aid)
- Short explanation of how R/S assignment is determined
## Student details
- Name: Nalla Hari Hara Krishna
- Reg No: RA2511026050036
- Dept: CSE-AIML
- SEC: A

## Run locally

Because this project uses JavaScript modules, run it with a local static server.
## Run

```bash
python3 -m http.server 8000
python app.py
```

Then open: <http://localhost:8000>
Then open:
- http://127.0.0.1:8000

## GitHub

```bash
git add .
git commit -m "Build Python-only Brucine site with no css/html files"
git push
```
