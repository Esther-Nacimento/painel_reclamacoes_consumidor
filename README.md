# Painel de Reclamações de Consumidores

🔗 **Acesse o painel online:**  
[https://painel-reclamacoes-consumidor.streamlit.app/](https://painel-reclamacoes-consumidor.streamlit.app/)

## Sobre o projeto

Este projeto apresenta um painel interativo para análise de reclamações de consumidores registradas no **Consumidor.gov.br**.

O objetivo é transformar dados tratados em uma visualização simples, informativa e acessível, permitindo observar padrões de reclamações por empresa, estado, área de mercado, classificação e período.

O painel foi desenvolvido como uma ferramenta de consulta e interpretação dos dados, destacando métricas importantes como volume de reclamações, resolução dos casos, nota média de satisfação e principais problemas relatados.

## O que o painel permite analisar

- Empresa com maior volume de reclamações
- Reclamações por estado
- Reclamações por área/segmento, como serviços financeiros, telecomunicações, transportes e comércio
- Total de reclamações registradas
- Quantidade de reclamações resolvidas
- Quantidade de reclamações não resolvidas
- Nota média de satisfação dos consumidores
- Ranking dos principais problemas relatados
- Comparativo entre empresas
- Resumo automático dos problemas mais frequentes

## Funcionalidades

O painel possui duas áreas principais:

### Panorama

Apresenta uma visão inicial dos dados analisados, com indicadores gerais, ranking de problemas, empresas com mais reclamações, evolução mensal e distribuição das classificações.

### Análise por empresa

Permite aplicar filtros para consultar uma empresa específica ou comparar todas as empresas dentro de um recorte selecionado. Os filtros disponíveis são:

- Empresa
- Estado
- Área/segmento
- Classificação
- Período

## Fonte dos dados

Os dados utilizados são públicos e têm origem no **Consumidor.gov.br**.

A base foi previamente tratada para padronizar campos, organizar datas, ajustar classificações e permitir a construção dos indicadores apresentados no painel.

## Tecnologias utilizadas

- Python
- Streamlit
- Pandas
- Plotly

## Como executar localmente

Clone o repositório:

```bash
git clone https://github.com/Esther-Nacimento/painel_reclamacoes_consumidor.git
```

Acesse a pasta do projeto:

```bash
cd painel_reclamacoes_consumidor
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o painel:

```bash
streamlit run app.py
```

## Estrutura do projeto

```text
painel_reclamacoes_consumidor/
├── app.py
├── requirements.txt
├── README.md
└── dados/
    └── reclamacoes_painel.csv
```

## Observação

Os indicadores têm finalidade informativa e devem ser interpretados considerando o período analisado, os filtros aplicados e a quantidade de registros disponíveis.
