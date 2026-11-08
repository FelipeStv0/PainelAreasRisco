# Painel Áreas de Risco — Marília (SP)

Página **estática e independente** de apresentação de um projeto exploratório sobre visualização de acidentes de trânsito na cidade de Marília, São Paulo.

> **Limite essencial:** este repositório contém apenas o front-end de apresentação (`index.html`, `styles.css`, `script.js` e imagens). **Não contém** o pipeline de coleta/limpeza dos dados, os registros de acidentes, os notebooks de análise nem o código-fonte da aplicação Streamlit. Os resultados e gráficos ilustrados **não foram reproduzidos ou validados** a partir dos arquivos disponíveis.

## O que você encontra aqui

- Página responsiva em HTML, CSS e JavaScript, sem dependências de instalação.
- Contexto e propostas de visualização de acidentes.
- Imagens ilustrativas de gráfico e mapa (dados e métodos de criação não documentados).
- Link para um [dashboard Streamlit hospedado externamente](https://dashboardareaderisco-mariliasp.streamlit.app/), cuja disponibilidade e conteúdo são independentes desta página.
- [Registro de origem e limitações dos dados](DADOS.md).

## Executar localmente

**Opção 1 — sem instalação:** clone ou baixe o repositório e abra `index.html` em um navegador moderno. O front-end não precisa de Node.js, Python nem banco de dados.

```bash
git clone https://github.com/FelipeStv0/PainelAreasRisco.git
cd PainelAreasRisco
```

**Opção 2 — servidor HTTP local (recomendado para simular hospedagem):** com Python 3 instalado, execute na pasta do projeto:

```bash
python -m http.server 8000
```

Abra **http://localhost:8000/**. Finalize com `Ctrl+C`.

No Windows, caso `python` não esteja disponível, tente `py -m http.server 8000`.

**O que não é possível executar a partir deste repositório:** o app Streamlit e o processamento dos dados. Para isso seriam necessários, no mínimo, o código Python original, dados acessíveis legalmente, dependências, versões e instruções específicas. Não há um `requirements.txt` legítimo para essa parte neste projeto.

## Estrutura

```text
PainelAreasRisco/
├── index.html                # Página de apresentação
├── styles.css                # Layout responsivo
├── script.js                 # Inicialização mínima do front-end
├── acidente de carro.jpeg    # Imagem de banner
├── mapa1.jpeg                # Exemplo de mapa (origem não documentada)
├── mapa2.jpg                 # Exemplo de gráfico (origem não documentada)
├── DADOS.md                  # Proveniência e lacunas
└── README.md
```

Os arquivos de marca DSIN foram removidos da versão atual por falta de comprovação de autorização; podem permanecer acessíveis no histórico Git. Não os reutilize sem permissão.

## Dados e metodologia

O HTML anterior mencionava registros de acidentes entre **2016 e 2024**, incluindo tipo de veículo, data, coordenadas e endereço. Entretanto, **não há base de dados nem referência primária documentada** que permita confirmar os campos, o intervalo ou a cobertura. Para preencher a fonte corretamente, consulte [DADOS.md](DADOS.md), que lista as informações pendentes, sem atribuir os dados a um órgão por suposição.

As etapas de higienização, exploração e visualização descritas na página são uma **proposta metodológica**, não uma implementação auditável deste repositório.

Contagem de acidentes não equivale automaticamente a probabilidade de acidente ou nível de risco. Sem denominadores de exposição, controle de vieses e validação, **não utilize este material para precificação, decisões operacionais, políticas públicas ou avaliação de segurança de vias**.

## Verificação manual

1. Abra a página localmente e navegue pelas seções do menu.
2. Inspecione em telas de celular e desktop; confira que os links e as imagens estão acessíveis.
3. Verifique se o botão do dashboard abre o site externo em nova aba. A página local deve continuar utilizável caso o serviço não esteja no ar.
4. Confira a presença do aviso de escopo e de fonte não verificada.

Não há testes automatizados de processamento de dados ou de Streamlit neste repositório. A disponibilidade do endereço externo não foi verificada nesta revisão.

## Identidade e autoria institucional

Esta versão **não declara vínculo, patrocínio, parceria ou endosso da DSIN, da Prefeitura de Marília ou de qualquer instituição**. Logotipo, menus corporativos e alegações de atuação em nome da DSIN foram retirados da página. A remoção completa de marcas do histórico Git, caso necessária, exige avaliação e procedimento específicos.

Caso exista autorização institucional documentada, ela pode ser contextualizada em alteração posterior, indicando natureza da colaboração, responsável e permissão de uso da marca.

## Próximas etapas para uma análise reproduzível

- Obter e documentar fontes primárias, licenças e período de coleta.
- Publicar pipeline de ingestão e tratamento com testes e dados anonimizados, quando legalmente permitido.
- Versionar a aplicação Streamlit separadamente ou integrá-la aqui com dependências fixadas.
- Documentar critérios geoespaciais, vieses de cobertura, validação e limitações de uso.

**Status:** apresentação estática disponível; análise de acidentes e dashboard externo não reproduzíveis a partir deste repositório.
