import logging
import config

def transform_data(df):
    logging.info("Transformando dados")

    if 'nome' not in df.columns:
        raise ValueError("Coluna 'nome' não encontrada")

    df = df.dropna()
    df = df[df['quantidade'] > 0]

    df['nome'] = df['nome'].str.title()
    df['valor_total'] = df['quantidade'] * df['preco']

    df = df.sort_values(by='valor_total', ascending=False)

    df.to_csv(config.PROCESSED_PATH, index=False)

    return df
