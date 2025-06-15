import pandas as pd
import sqlite3

def read_sqlite(db_name: str, table_name: str) -> pd.DataFrame:
    """
    Lê os dados de uma tabela em um banco de dados SQLite e retorna um DataFrame do pandas.

    Args:
        pd.DataFrame: DataFrame do pandas com os dados lidos.
    """
    conn = sqlite3.connect(db_name)

    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

    conn.close()

    return df


def analyse_data(df: pd.DataFrame) -> None:
    """
    Anlálise inicial dos dados para entender a estutura e o conteúdo.

    Args:
        df (pd.DataFrame): DataFrame do pandas com os dados:
    """
    print("\nData Analysis: \n")
    df["data_inversa"] = pd.to_datetime(df["data_inversa"]) 
    # Obter apenas os anos, meses e dias únicos separadamente.
    anos_unicos = df["data_inversa"].dt.year.unique()
    meses_unicos = df["data_inversa"].dt.month.unique()
    dias_unicos = df["data_inversa"].dt.day.unique()
    print("\nUnique years:", anos_unicos) 
    print("\nUnique month:", meses_unicos)
    print("\nUnique days:", dias_unicos)
    print("\nDays of the week:", df["dia_semana"].unique())
    #print("Time:", df["horario"].unique())
    print("\nStates:", df["uf"].unique())
            # Verifica se existem datas diferentes para cada combinação de dias da semana.
    duplicates = df.groupby(["data_inversa"])["dia_semana"].nunique()
    duplicates = duplicates[duplicates > 1]
    if not duplicates.empty:
        print("\nDuplicated dates for each week \n ")
        print(duplicates)

    return df



def transform_data_inversa_to_date(df: pd.DataFrame) ->  pd.DataFrame:
    """
    Altera a coluna "data_inversa" de String para Datetime.

    Args:
        df (pd.DataFrame): DataFrame do pandas com os dados.

    Returns:
        pd.DataFrame: DataFrame do pandas com a coluna "data_inversa" em formato texto novamente.
    """
    df["data_inversa"] = df["data_inversa"].astype(str)  

    return df

    


if __name__ == "__main__":
    db_name = "databases/stage.db"
    table_name = "acidentes"
    df = read_sqlite(db_name, table_name)
    analyse_data(df)
    transform_data_inversa_to_date(df)

    print(df.head())
    print(df.dtypes)
