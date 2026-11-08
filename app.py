"""Dashboard exploratório; não serve para decisões de segurança viária."""
from __future__ import annotations
import pandas as pd
import streamlit as st
from painel_risco.demo import generate_demo
from painel_risco.pipeline import DataValidationError, clean_records, summarize

st.set_page_config(page_title="Painel Áreas de Risco | Demonstração", page_icon="📊", layout="wide")
st.title("Acidentes de trânsito — demonstração exploratória")
st.warning("DADOS FICTÍCIOS POR PADRÃO. Nenhum indicador representa acidentes reais de Marília ou estima probabilidade de acidente.")
st.caption("Projeto independente; sem vínculo institucional comprovado com DSIN ou Prefeitura.")
with st.sidebar:
    st.header("Fonte")
    source = st.radio("Selecionar dados", ["Demo sintética", "CSV próprio"], index=0)
    file = st.file_uploader("CSV UTF-8 no esquema documentado", type=["csv"]) if source == "CSV próprio" else None
    st.caption("Não envie informações pessoais ou sensíveis.")
if source == "CSV próprio" and file is None:
    st.info("Selecione um CSV. O formato está descrito no README.")
    st.stop()
try:
    raw = generate_demo() if source == "Demo sintética" else pd.read_csv(file, dtype={"id": "string"}, encoding="utf-8")
    data = clean_records(raw)
except (DataValidationError, pd.errors.ParserError, pd.errors.EmptyDataError, UnicodeError, ValueError) as exc:
    st.error(f"Entrada inválida: {exc}")
    st.stop()
if data.empty:
    st.warning("Nenhuma linha válida após validação.")
    st.stop()
st.sidebar.header("Filtros")
severities = st.sidebar.multiselect("Gravidade", sorted(data["gravidade"].unique()), default=sorted(data["gravidade"].unique()))
vehicles = st.sidebar.multiselect("Veículo", sorted(data["tipo_veiculo"].unique()), default=sorted(data["tipo_veiculo"].unique()))
filtered = data[data["gravidade"].isin(severities) & data["tipo_veiculo"].isin(vehicles)]
st.metric("Registros exibidos (contagem, não taxa de risco)", len(filtered))
st.caption(f"Fonte: {'sintética (seed=42)' if source == 'Demo sintética' else 'CSV fornecido; origem não verificada'}. {len(raw)-len(data)} linhas descartadas.")
if filtered.empty:
    st.info("Nenhum registro corresponde aos filtros.")
    st.stop()
summary = summarize(filtered)
left, right = st.columns(2)
with left:
    st.subheader("Registros por gravidade")
    st.bar_chart(summary["por_gravidade"])
with right:
    st.subheader("Registros por veículo")
    st.bar_chart(summary["por_veiculo"])
st.subheader("Distribuição geográfica dos registros")
st.caption("Pontos representam registros; concentração de pontos não representa risco validado.")
st.map(filtered.rename(columns={"latitude": "lat", "longitude": "lon"})[["lat", "lon"]])
st.subheader("Registros por ano")
st.bar_chart(summary["por_ano"])
with st.expander("Dados tratados"):
    st.dataframe(filtered, use_container_width=True, hide_index=True)
    st.download_button("Baixar CSV filtrado", data=filtered.to_csv(index=False).encode("utf-8"), file_name="registros_filtrados.csv", mime="text/csv")
st.info("Limitações: sem exposição ao tráfego, correção de subnotificação, auditoria das fontes ou validação espacial.")
