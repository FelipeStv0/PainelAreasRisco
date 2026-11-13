"""A fronteira de serviço pode ser utilizada sem renderizar Streamlit."""
from io import StringIO
import pandas as pd
import pytest

from painel_risco.pipeline import DataValidationError
from painel_risco.service import prepare_dataset, filter_records


def test_prepare_demo_and_filter():
    raw, cleaned = prepare_dataset("Demo sintética", None)
    assert len(raw) == len(cleaned) == 160
    sub = filter_records(cleaned, ["Fatal"], ["Automóvel"])
    assert all(sub["gravidade"] == "Fatal")
    assert all(sub["tipo_veiculo"] == "Automóvel")
    assert len(cleaned) == 160


def test_uploaded_csv_preserves_identifier_and_validates():
    csv = StringIO(
        "id,data,tipo_veiculo,gravidade,latitude,longitude\n"
        "0007,2024-01-01,Automóvel,Sem vítimas,-22.2,-49.9\n"
    )
    raw, clean = prepare_dataset("CSV próprio", csv)
    assert raw.loc[0, "id"] == "0007"
    assert clean.loc[0, "id"] == "0007"


def test_invalid_data_source_fails_closed():
    with pytest.raises(DataValidationError, match="Origem desconhecida"):
        prepare_dataset("API pública", None)
    with pytest.raises(DataValidationError, match="CSV"):
        prepare_dataset("CSV próprio", None)
