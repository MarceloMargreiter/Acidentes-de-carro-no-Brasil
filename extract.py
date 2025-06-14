import pandas as pd
import sqlite3


def extract_data(file_path: str) -> pd.DataFrame:
    """
    Extrai dados de um arquivo CSV e retorna um DataFrame do pandas.

    Args:
        file_path (str); Caminho do arquivo CSV.

    Returns:
        ps.DataFramen: DataFrame do pandas coom os dados extraídos.
    """
    df = pd.read_csv(file_path, encoding="utf-8")
    print(df.head())

    return df


def data_exploration(df: pd.DataFrame) -> None:
    """
    Realiza uma exploração inicial dos dados.

    Args:
        df (pd.DataFrame): DataFrame do pandas com os dados.
    """
    print("Data Exploration:")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    print("Column names:", df.columns.tolist())
    print("Data types:")
    print(df.dtypes)
    print("Missing values:")
    print(df.isnull().sum())
    print("First 5 rows:")
    print(df.head())

def create_database(db_name: str) -> None:
    """
    Cria um banco de dados SQLite.

    Args:
        db_name (str): Nome do banco de dados.
    """
    conn = sqlite3.connect(db_name)
    conn.close()
    print(f"Database {db_name} created")

def create_table(db_name: str, table_name: str) -> None:
    """
    Cria uma tabela no banco de dados SQLite.

    Args:
        db_name (str): Nome do banco de dados.
        table_name (str): Nome da tabela.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            data_inversa TEXT,
            dia_semana TEXT,
            horario TEXT,
            uf TEXT,
            latitude FLOAT,
            longitude FLOAT,
            UNIQUE(data_inversa, horario, uf, latitude, longitude)
        )
    """)
    conn.commit()
    conn.close
    print(f"Table {table_name} created in {db_name}")


def insert_data(df: pd.DataFrame, db_name: str, table_name: str) -> None:
    '''
    Insere dados em uma tabela do banci de dados SQLite.

    Args:
        df (pd.DataFrame): DataFrame do pandas com os dados.
        db_name (str): Nome do banco de dados.
        table_name (str): Nome da tabela.
    '''
    conn = sqlite3.connect(db_name)
    sql: str = f'''
        INSERT OR REPLACE INTO {table_name} (data_inversa, dia_semana, horario, uf, latitude, longitude)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
    for _, row in df.iterrows():
        conn.execute(sql, (row["data_inversa"], row["dia_semana"], row["horario"], row["uf"], row["latitude"], row["longitude"]))
    conn.commit()
    print(f"Inserted {len(df)} rows into {table_name}")
    conn.close()
    print(f"Data inserted into {table_name} in {db_name}")    


