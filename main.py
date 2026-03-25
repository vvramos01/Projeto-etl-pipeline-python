import logging
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data
import config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run():
    try:
        df = extract_data(config.INPUT_PATH)
        df = transform_data(df)
        load_data(df, config.DB_PATH)
        logging.info("Pipeline executado com sucesso")
    except Exception as e:
        logging.error(f"Erro no pipeline: {e}")

if __name__ == "__main__":
    run()
