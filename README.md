# Painel Áreas de Risco — demonstração exploratória

Projeto independente de visualização de registros de acidentes de trânsito. Contém página estática em HTML/CSS/JS, dashboard Streamlit, pipeline de validação de CSV e testes automatizados.

> **Aviso:** a base original relacionada a Marília (SP), mencionada na apresentação histórica como 2016–2024, não está disponível e sua origem não foi documentada. O dashboard inicia com **dados inteiramente sintéticos** e **não representa acidentes reais**. Não há vínculo institucional comprovado com DSIN ou Prefeitura de Marília. Não use os mapas e contagens como estimativas de risco ou para decisões sobre segurança viária.

## Demonstração rápida para portfólio

A demonstração está pronta para ser iniciada **sem chaves de API ou dados reais**. Execute os comandos da próxima seção e abra o endereço local exibido pelo Streamlit (normalmente http://localhost:8501).

Para apresentar o projeto, mantenha a fonte **Demo sintética** selecionada e mostre os filtros por veículo e gravidade, os gráficos, o mapa e a exportação CSV. Explique que o processamento está em `src/painel_risco/pipeline.py` e que **nenhuma contagem representa risco real**. Não apresente o dashboard externo histórico como resultado deste código.

**Validação:** o teste `tests/test_app.py` verifica a inicialização do Streamlit com 160 registros fictícios. Esse teste não substitui uma inspeção visual no navegador.

## Executar o dashboard (Windows PowerShell)

Requisitos: Python 3.10+ e Git. Em uma pasta de sua escolha:

```powershell
git clone https://github.com/FelipeStv0/PainelAreasRisco.git
cd PainelAreasRisco
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m streamlit run app.py
```

Se a ativação do PowerShell estiver bloqueada, execute sem ativar:
```powershell
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Em Linux/macOS: crie o ambiente com `python3 -m venv .venv`, ative com `source .venv/bin/activate` e execute os dois últimos comandos. O terminal informa o endereço do Streamlit, normalmente **http://localhost:8501**. Não é necessário API, banco de dados ou token para a demonstração.

## Dados sintéticos e CSV próprio

Por padrão, o app gera 160 registros fictícios de forma determinística, com `seed=42`. Se quiser gerar um arquivo físico:

```powershell
python -m painel_risco.demo --output data/demo_sintetico.csv --rows 160 --seed 42
```

No menu lateral do Streamlit, escolha **CSV próprio** para carregar dados **UTF-8** com seis campos obrigatórios:

```csv
id,data,tipo_veiculo,gravidade,latitude,longitude
EXEMPLO-001,2024-01-01,Automóvel,Sem vítimas,-22.217,-49.950
```

Essa linha é **ilustrativa**, não uma ocorrência real. Data no formato `AAAA-MM-DD`; gravidade deve ser exatamente `Sem vítimas`, `Com vítimas` ou `Fatal`. Coordenadas em graus decimais (latitude de -90 a 90; longitude de -180 a 180). IDs devem ser únicos.

O pipeline elimina registros com campos ausentes, datas/coordenadas inválidas, gravidade fora do conjunto e IDs duplicados (preserva a primeira ocorrência). **Não** verifica município, licenciamento dos dados, identidade de vítimas, conformidade com LGPD ou proveniência. Não envie dados pessoais ou sensíveis, especialmente para implantações públicas.

## Página de apresentação

Para abrir o front-end estático, abra `index.html` no navegador ou execute:

```powershell
python -m http.server 8000
```

Acesse **http://localhost:8000**. A página estática conserva um link para a aplicação histórica hospedada externamente; ela é **independente** do novo `app.py`, e seu estado não foi verificado.

## Testes e CI

```powershell
python -m pip install -e '.[dev]'
python -m pytest -q
python -m py_compile app.py src/painel_risco/*.py
```

O workflow em `.github/workflows/ci.yml` roda testes e compilação no GitHub Actions em Python 3.10 e 3.12. Os testes verificam geração determinística, contrato de colunas, descarte de dados inválidos, deduplicação, leitura, contagens e inicialização básica do Streamlit. Não incluem testes de navegador completos nem validam o dashboard histórico ou dados reais.

## Organização

```text
app.py                         # Streamlit: filtros, contagens, mapa e exportação
src/painel_risco/pipeline.py   # Validação, limpeza e resumo
src/painel_risco/demo.py       # Dados sintéticos determinísticos
tests/test_pipeline.py        # Testes unitários
tests/test_app.py             # Teste de inicialização do Streamlit
.github/workflows/ci.yml      # Integração contínua
pyproject.toml                 # Dependências Python
index.html, styles.css, script.js  # Apresentação estática
DADOS.md                      # Fontes, contrato e limitações
```

## Limitações e próximas etapas

O dashboard mostra **contagens**, não risco de acidentes. Não há denominadores de exposição ao tráfego, auditoria de subnotificação, validação geoespacial, modelo de ML ou previsão. As imagens `mapa1.jpeg` e `mapa2.jpg` são legadas e a origem/direitos não foram comprovados. Antes de integrar dados reais, identificar fonte primária, licença, período, dicionário de dados, transformações e privacidade. Consulte [DADOS.md](DADOS.md).
