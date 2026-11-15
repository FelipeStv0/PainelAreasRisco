# Road Safety Data Dashboard — Exploratory Demo

**Language:** [English](README_EN.md) | [Português](README.md)

An independent project for exploring road accident records with charts, filters, and a map. It includes a **Streamlit dashboard**, a separate static HTML/CSS/JavaScript presentation page, CSV validation, and automated tests.

> **Important:** The original historical dataset for Marília (2016–2024) is **not available in this repository**, and its source was not documented. By default, this dashboard uses **fully synthetic data**. It does **not show real accidents or measure road accident risk**. There is no confirmed official connection to the City of Marília or DSIN. Do not use this demonstration for real safety decisions.

## What the project includes

- A Streamlit dashboard with accident record counts.
- Filters for vehicle type and incident severity.
- Charts by severity, vehicle, and year.
- A map showing the locations of **synthetic records**.
- CSV upload, field validation, and CSV export.
- Reproducible example data, automatic tests, and GitHub Actions.
- A static presentation page maintained separately from the Python application.

**The dashboard shows record counts, not accident rates or a validated risk model.**

## Technology stack

| Technology | Role |
| --- | --- |
| Python | Data processing |
| Pandas | Cleaning CSV files and summarizing data |
| Streamlit | Dashboard interface |
| HTML, CSS, JavaScript | Static project presentation |
| pytest | Automated unit and application startup tests |
| GitHub Actions | CI checks in Python 3.10 and 3.12 |

## Quick start — Windows PowerShell

Requirements: Python 3.10+ and Git.

~~~powershell
git clone https://github.com/FelipeStv0/PainelAreasRisco.git
cd PainelAreasRisco
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m streamlit run app.py
~~~

Open the local address displayed in your terminal, usually **http://localhost:8501**.

If PowerShell does not allow environment activation, run the commands with the Python executable inside `.venv\Scripts\` directly:

~~~powershell
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m streamlit run app.py
~~~

On Linux/macOS, create an environment with `python3 -m venv .venv`, activate it using `source .venv/bin/activate`, then install and start the application.

No external API key or database is needed for the demonstration.

## Try the dashboard

Select **"Demo sintética"** (synthetic demo) in the sidebar. The app creates **160 synthetic records** with a fixed random seed (`seed=42`). You can:
1. Filter by severity and vehicle type.
2. Explore charts and the map.
3. View the cleaned records.
4. Export the filtered dataset as a CSV file.

The default data is fictional. The interface is currently in Portuguese.

To save a synthetic CSV file locally:

~~~powershell
python -m painel_risco.demo --output data/demo_sintetico.csv --rows 160 --seed 42
~~~

## Upload your own CSV

Select **"CSV próprio"** (your own CSV) in the sidebar. The file must be UTF-8 and have these six columns:

~~~csv
id,data,tipo_veiculo,gravidade,latitude,longitude
EXAMPLE-001,2024-01-01,Automóvel,Sem vítimas,-22.217,-49.950
~~~

This example row is fictional. The column names and accepted severity values remain in **Portuguese**, because they are part of the existing data format.

Rules:
- `data` uses `YYYY-MM-DD`.
- `gravidade` must be `Sem vítimas`, `Com vítimas`, or `Fatal`.
- Latitude is between -90 and 90; longitude is between -180 and 180.
- IDs must be unique.

The data pipeline removes records with missing required fields, invalid dates or coordinates, unsupported severity values, and duplicate IDs (keeping the first occurrence).

**It does not verify** where the records came from, usage rights, the real city, personal identity, or privacy compliance. Do not upload personal or sensitive information.

See [data format and limitations](DADOS.md) (Portuguese).

## Static presentation page

You can also open `index.html` in a browser or start a simple server:

~~~powershell
python -m http.server 8000
~~~

Then open **http://localhost:8000**.

The static page includes a link to an older external application. That older application is **separate from the current Streamlit project**, and its live status has not been verified. Do not present it as a working part of the current code.

## Tests and continuous integration

~~~powershell
python -m pip install -e '.[dev]'
python -m pytest -q
python -m py_compile app.py src/painel_risco/*.py
~~~

The [CI workflow](.github/workflows/ci.yml) runs on Python 3.10 and 3.12. It tests deterministic data generation, validation rules, duplicate handling, summaries, file loading, and basic Streamlit startup.

The code includes a test that checks synthetic data generation for deprecation warnings. **Passing tests does not replace full manual browser testing or checks with real-world data.**

## Project structure

| Path | Purpose |
| --- | --- |
| `app.py` | Streamlit interface, charts, filters, and export |
| `src/painel_risco/service.py` | Data source selection and filters |
| `src/painel_risco/pipeline.py` | CSV cleaning, validation, and summaries |
| `src/painel_risco/demo.py` | Reproducible synthetic example records |
| `tests/` | Unit tests and application startup test |
| `index.html`, `styles.css`, `script.js` | Separate static presentation |
| `DADOS.md` | Data format, sources, and limitations |
| `docs/GUIA_MANUTENCAO.md` | Maintenance and future integrations |
| `pyproject.toml` | Python dependencies |

The service layer keeps data processing separate from the interface, making future changes easier to test.

## Limits and future work

This project has **no validated accident risk prediction model**. It also has no traffic exposure data, reliable underreporting estimates, or full geographic validation. Maps and counts are not enough to estimate road safety risk.

The older images `mapa1.jpeg` and `mapa2.jpg` have unverified sources and usage rights. Before adding real data, confirm its source, license, date range, column definitions, transformations, and privacy requirements.

The next step would be to use an authorized real dataset, document its quality, and validate the results before making any claims about road safety.

---

**Project type:** independent, educational portfolio demonstration. The default dataset is synthetic and must not be presented as real accident information.
