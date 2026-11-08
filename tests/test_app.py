"""Teste de inicialização do dashboard Streamlit, sem navegador externo."""
from pathlib import Path

from streamlit.testing.v1 import AppTest


def test_demo_starts_and_displays_synthetic_data():
    app = AppTest.from_file(str(Path(__file__).resolve().parents[1] / "app.py"))
    app.run(timeout=30)
    assert not app.exception, [str(error.message) for error in app.exception]
    assert len(app.metric) == 1
    assert app.metric[0].value == "160"
    assert any("FICTÍCIOS" in warning.message for warning in app.warning)
