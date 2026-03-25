import sqlite3
import logging
import config

def load_data(df, db_path):
    logging.info("Carregando dados no banco")

    conn = sqlite3.connect(db_path)
    df.to_sql(config.TABLE_NAME, conn, if_exists='replace', index=False)
    conn.close()
