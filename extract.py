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