# ETL Pipeline em Python Atualizado 2026

## Descrição

Este projeto implementa um pipeline ETL (Extract, Transform, Load) utilizando Python. O objetivo é processar dados de vendas a partir de arquivos CSV, aplicar transformações e armazenar os resultados em um banco de dados.

## Tecnologias utilizadas

* Python
* Pandas
* SQLite
* SQLAlchemy

## Estrutura do projeto

```
data/
 ├── raw/          # dados brutos
 ├── processed/    # dados tratados

etl/
 ├── extract.py
 ├── transform.py
 ├── load.py
 ├── pipeline.py

config.py
main.py
requirements.txt
```

## Etapas do pipeline

### Extract

Leitura dos dados a partir de um arquivo CSV localizado em `data/raw`.

### Transform

* Remoção de valores nulos
* Padronização de dados
* Cálculo de novas métricas
* Ordenação dos dados

### Load

Os dados processados são armazenados em um banco de dados utilizando SQLAlchemy.

## Como executar

1. Instalar as dependências:

```
pip install -r requirements.txt
```

2. Executar o pipeline:

```
python main.py
```

## Exemplo de dados

Entrada (`data/raw`):

```
nome,quantidade,preco
joao,2,10
maria,5,7
carlos,3,12
```

Saída:

* Arquivo CSV em `data/processed`
* Tabela no banco de dados com os dados transformados

## Observações

* O arquivo `.env` pode ser utilizado para configurar a conexão com o banco de dados
* O projeto pode ser adaptado para outros formatos de entrada e bancos de dados

```
```
