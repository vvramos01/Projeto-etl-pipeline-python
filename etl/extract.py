import pandas as pd
import logging

def extract_data(path):
    logging.info("Extraindo dados")
    df = pd.read_csv(path)
    return df
