# Guia de manutenção e integração — Painel de Áreas de Risco

## Estrutura de responsabilidades

| Arquivo | Papel | Extensões |
| --- | --- | --- |
| `app.py` | Interface Streamlit e componentes visuais | Novas páginas, gráficos e mensagens |
| `src/painel_risco/service.py` | Seleção da origem e filtros puros | Integração com fonte adicional, **com autorização e testes** |
| `src/painel_risco/pipeline.py` | Leitura, limpeza, integridade e resumo | Novos campos, domínios de valores e validação |
| `src/painel_risco/demo.py` | Gerar cenário fictício reprodutível | Novos padrões de teste claramente sintéticos |
| `tests/` | Comportamento e inicialização da aplicação | Testes de regressão e erro de entrada |

## Como integrar novas fontes

1. Defina proveniência, licença, atualização e finalidade da base antes de integrá-la.
2. Converta para o esquema documentado em `DADOS.md`; o novo adaptador deve retornar um DataFrame com campos necessários.
3. Passe **todas** as origens por `clean_records` antes de filtrar ou renderizar.
4. Implemente a seleção da origem em `service.py`; evite colocar tratamento de dados na interface.
5. Teste com entradas ausentes, coordenadas inválidas, duplicatas e caracteres UTF-8.

## Validação

```bash
python -m pip install -e '.[dev]'
python -m pytest -q
python -m py_compile app.py src/painel_risco/*.py
streamlit run app.py
```

Os dados demonstrativos são **fictícios**. Contagem de ocorrências não é taxa de risco e o projeto não pode apoiar decisões operacionais de segurança viária sem dados reais, exposição adequada e validação independente.
