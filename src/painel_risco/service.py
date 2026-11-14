"""Serviços de aplicação usados pela interface Streamlit.

INTEGRAÇÃO FUTURA: dados de novas origens devem passar pelo mesmo contrato
clean_records antes de serem exibidos. Manter funções sem estado de Streamlit
facilita testes offline e futura integração com outra interface.
"""
from __future__ import annotations

import pandas as pd

from .demo import generate_demo
from .pipeline import DataValidationError, clean_records


def prepare_dataset(source: str, uploaded_file) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Lê uma origem aprovada e devolve (dados brutos, dados validados).

    A origem CSV é fornecida pelo usuário; o serviço não atesta sua procedência.
    Não registrar ou enviar o conteúdo do upload a serviços externos.
    """
    if source == "Demo sintética":
        raw = generate_demo()
    elif source == "CSV próprio":
        if uploaded_file is None:
            raise DataValidationError("Um CSV deve ser selecionado")
        raw = pd.read_csv(uploaded_file, dtype={"id": "string"}, encoding="utf-8")
    else:
        raise DataValidationError(f"Origem desconhecida: {source}")
    return raw, clean_records(raw)


def filter_records(data: pd.DataFrame, severities: list[str], vehicles: list[str]) -> pd.DataFrame:
    """Aplica filtros como interseção; não altera o DataFrame original."""
    return data[data["gravidade"].isin(severities) & data["tipo_veiculo"].isin(vehicles)]
