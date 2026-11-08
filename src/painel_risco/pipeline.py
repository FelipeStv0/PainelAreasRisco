"""Validação de registros CSV para análises exploratórias. Não estima risco."""
from __future__ import annotations
from pathlib import Path
import pandas as pd

REQUIRED = ("id", "data", "tipo_veiculo", "gravidade", "latitude", "longitude")
SEVERITIES = frozenset({"Sem vítimas", "Com vítimas", "Fatal"})

class DataValidationError(ValueError):
    """Esquema ou dados inválidos."""

def load_csv(path: str | Path) -> pd.DataFrame:
    file_path = Path(path)
    if not file_path.is_file():
        raise DataValidationError(f"Arquivo não encontrado: {file_path}")
    try:
        return pd.read_csv(file_path, encoding="utf-8", dtype={"id": "string"})
    except (pd.errors.EmptyDataError, pd.errors.ParserError, UnicodeError) as exc:
        raise DataValidationError(f"CSV inválido: {exc}") from exc

def clean_records(frame: pd.DataFrame) -> pd.DataFrame:
    missing = sorted(set(REQUIRED) - set(frame.columns))
    if missing:
        raise DataValidationError("Colunas obrigatórias ausentes: " + ", ".join(missing))
    df = frame.loc[:, REQUIRED].copy()
    for col in ("id", "tipo_veiculo", "gravidade"):
        df[col] = df[col].astype("string").str.strip().replace("", pd.NA)
    df["data"] = pd.to_datetime(df["data"], format="%Y-%m-%d", errors="coerce")
    for col in ("latitude", "longitude"):
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=list(REQUIRED))
    df = df[df["gravidade"].isin(SEVERITIES)]
    df = df[df["latitude"].between(-90, 90) & df["longitude"].between(-180, 180)]
    df = df.drop_duplicates(subset=["id"], keep="first")
    return df.sort_values(["data", "id"]).reset_index(drop=True)

def summarize(frame: pd.DataFrame) -> dict[str, object]:
    return {
        "total": int(len(frame)),
        "por_gravidade": frame["gravidade"].value_counts().sort_index(),
        "por_veiculo": frame["tipo_veiculo"].value_counts().sort_index(),
        "por_ano": frame.groupby(frame["data"].dt.year).size().sort_index(),
    }
