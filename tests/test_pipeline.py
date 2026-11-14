import warnings

import pandas as pd
import pytest
from painel_risco.demo import generate_demo
from painel_risco.pipeline import DataValidationError, clean_records, load_csv, summarize

def test_demo_is_deterministic_and_clean():
    a = generate_demo(10, seed=10)
    pd.testing.assert_frame_equal(a, generate_demo(10, seed=10))
    assert len(clean_records(a)) == 10
    assert set(a["id"].str.startswith("DEMO-")) == {True}


def test_demo_does_not_emit_deprecation_warnings():
    """Garante que a geração de datas não reintroduza APIs depreciadas."""
    with warnings.catch_warnings():
        warnings.simplefilter("error", DeprecationWarning)
        demo = generate_demo(160, seed=42)
    assert len(demo) == 160
    assert all(value.startswith("2024-") for value in demo["data"])
    assert demo["id"].iloc[0] == "DEMO-00001"

def test_reject_missing_columns():
    with pytest.raises(DataValidationError, match="Colunas obrigatórias"):
        clean_records(pd.DataFrame({"id": ["1"]}))

def test_invalid_rows_and_duplicate_ids_removed():
    df = generate_demo(3)
    repeated = df.iloc[[0]].copy()
    invalid = df.iloc[[1]].copy()
    invalid["latitude"] = 91
    result = clean_records(pd.concat([df, repeated, invalid], ignore_index=True))
    assert len(result) == 3
    assert result["id"].is_unique

def test_reject_unknown_severity_and_bad_date():
    data = generate_demo(3)
    data.loc[0, "gravidade"] = "Desconhecida"
    data.loc[1, "data"] = "ontem"
    assert len(clean_records(data)) == 1

def test_summary_counts():
    result = clean_records(generate_demo(25))
    totals = summarize(result)
    assert totals["total"] == 25
    assert int(totals["por_gravidade"].sum()) == 25
    assert int(totals["por_veiculo"].sum()) == 25

def test_missing_csv(tmp_path):
    with pytest.raises(DataValidationError, match="Arquivo não encontrado"):
        load_csv(tmp_path / "absent.csv")

def test_roundtrip_csv(tmp_path):
    path = tmp_path / "sample.csv"
    generate_demo(5).to_csv(path, index=False)
    assert len(clean_records(load_csv(path))) == 5

def test_no_rows_allowed():
    with pytest.raises(ValueError):
        generate_demo(0)
