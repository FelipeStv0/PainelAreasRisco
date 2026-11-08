# Proveniência, dados e limitações

## Base histórica: origem não comprovada

A versão inicial da página mencionava acidentes de trânsito em Marília (SP) de 2016 a 2024, porém o repositório **não fornece registros históricos, órgão produtor, URL original, licença, data de extração, dicionário de dados nem metodologia reproduzível dessa base**. O conteúdo do dashboard externo não foi auditado. As imagens `mapa1.jpeg` e `mapa2.jpg` não possuem fonte e direitos documentados.

## Demonstração sintética

O módulo `painel_risco.demo` produz registros **inteiramente fictícios e determinísticos** usando um gerador pseudoaleatório com seed 42. Os pontos são coordenadas aleatórias próximas à região de Marília e **não correspondem a acidentes conhecidos**, nem modelam padrões reais de trânsito. IDs têm o prefixo `DEMO-`. O programa gera os exemplos em memória ou por comando; nenhum CSV fictício está versionado.

## Esquema para CSV próprio

| Campo | Tipo e restrição |
|---|---|
| `id` | texto não vazio; duplicados removidos pela primeira ocorrência |
| `data` | data ISO `AAAA-MM-DD` |
| `tipo_veiculo` | texto não vazio |
| `gravidade` | uma de `Sem vítimas`, `Com vítimas`, `Fatal` |
| `latitude` | número decimal de -90 a 90 |
| `longitude` | número decimal de -180 a 180 |

O pipeline descarta linhas inválidas. Não confere origem, direito de uso, localização no município, anonimização ou coerência substantiva das categorias. O uso de CSV próprio exige avaliação prévia de privacidade e licença.

## Checklist antes de publicar dados reais

Documentar entidade produtora, URL oficial da base, licença de uso, versão e data da extração, período de cobertura, significado dos campos, critérios de inclusão, limpeza/deduplicação, taxas de ausência e verificações espaciais. Não versionar dados pessoais identificáveis. Os direitos das imagens existentes também precisam de verificação.

## Interpretação estatística

Contagem de registros não equivale a risco viário ou probabilidade de acidente. Seriam necessários medidas de exposição ao tráfego, controle de vieses e subnotificação, representatividade, incerteza, delimitação espacial e validação independente antes de afirmar resultados operacionais.
