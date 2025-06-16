from sklearn.linear_model import LinearRegression
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

def extract_data(db_name: str, table_name: str) -> pd.DataFrame:
    """
    Extrai os dados do Data Warehouse.

    Args:
        db_name (str): Nome do banco de dados.
        table_name (str): Nome da tabela.

    Returns:
        pd.DataFrame: DataFrame do pandas com os dados lidos.
    """
    conn = sqlite3.connect(db_name)
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    df["data_inversa"] = pd.to_datetime(df["data_inversa"])  # Converte a coluna para datetime
    conn.close()
    return df

def train_model(x: pd.DataFrame, y: pd.Series) -> LinearRegression:
    """
    Treina o modelo de regressão linear.

    Args:
        x (pd.DataFrame): DataFrame do pandas com os dados de entrada.
        y (pd.Series): Série do pandas com os dados de saída.

    Returns:
        LinearRegression: Modelo treinado.
    """
    model = LinearRegression()
    model.fit(x, y)
    print(f"Coeficientes: {model.coef_}")
    return model

def predict_accidents(df: pd.DataFrame) -> None:
    """
    Realiza a estimativa de acidentes por ano e mês.

    Args:
        df (pd.DataFrame): DataFrame do pandas com os dados.
    """
    df["mes_ano"] = df["data_inversa"].dt.to_period("M")  # Extrai ano e mês
    grouped_df = df.groupby("mes_ano").agg({"data_inversa": "count"}).reset_index()
    grouped_df["mes_ano"] = grouped_df["mes_ano"].astype(str)  # Converte para string

    # Transforma mes/ano para variável numérica (YYYYMM)
    grouped_df["mes_ano_numeric"] = grouped_df["mes_ano"].str.replace("-", "").astype(int)

    x = grouped_df[["mes_ano_numeric"]]
    y = grouped_df["data_inversa"]

    print(x, y)  # Debug

    # Treina o modelo de regressão linear
    model = train_model(x, y)

    # Gera previsões para os próximos 12 meses
    future_months = pd.date_range(start=df["data_inversa"].max(), periods=12, freq="ME").strftime("%Y%m").astype(int)
    future_df = pd.DataFrame({"mes_ano_numeric": future_months})
    predictions = model.predict(future_df)

    # Exibe previsões
    print(f"\nPrevisão de acidentes para os próximos 12 meses\n")
    future_df["predicted_number"] = predictions
    print(future_df)
    print(f"\nFim.\n")

    # Gráfico de histórico e previsão
    plt.plot(grouped_df["mes_ano_numeric"], grouped_df["data_inversa"], label="Histórico")
    plt.plot(future_df["mes_ano_numeric"], future_df["predicted_number"], label="Previsão", linestyle="--")
    plt.xlabel("Ano-Mês")
    plt.ylabel("Número de Acidentes")
    plt.title("Regressão Linear - Previsão de Acidentes")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


# def predict_accidents(df: pd.DataFrame, estado: str) -> None:
#     """
#     Realiza a estimativa de acidentes por ano e mês para um estado específico.

#     Args:
#         df (pd.DataFrame): DataFrame do pandas com os dados.
#         estado (str): Sigla do estado a ser filtrado.
#     """
#     # Filtra pelo estado específico
#     df = df[df["uf"] == estado]

#     df["mes_ano"] = df["data_inversa"].dt.to_period("M")  # Extrai ano e mês
#     grouped_df = df.groupby("mes_ano").agg({"data_inversa": "count"}).reset_index()
#     grouped_df["mes_ano"] = grouped_df["mes_ano"].astype(str)  # Converte para string

#     # Transforma mes/ano para variável numérica (YYYYMM)
#     grouped_df["mes_ano_numeric"] = grouped_df["mes_ano"].str.replace("-", "").astype(int)

#     x = grouped_df[["mes_ano_numeric"]]
#     y = grouped_df["data_inversa"]

#     print(x, y)  # Debug

#     # Treina o modelo de regressão linear
#     model = train_model(x, y)

#     # Gera previsões para os próximos 12 meses
#     future_months = pd.date_range(start=df["data_inversa"].max(), periods=12, freq="ME").strftime("%Y%m").astype(int)
#     future_df = pd.DataFrame({"mes_ano_numeric": future_months})
#     predictions = model.predict(future_df)

#     # Exibe previsões
#     #print(f"\nPrevisão de acidentes para os próximos 12 meses no estado {estado}\n")
#     future_df["predicted_number"] = predictions
#     print(future_df)
#     print(f"\nFim.\n")

#     # Gráfico de histórico e previsão
#     plt.plot(grouped_df["mes_ano_numeric"], grouped_df["data_inversa"], label="Histórico")
#     plt.plot(future_df["mes_ano_numeric"], future_df["predicted_number"], label="Previsão", linestyle="--")
#     plt.xlabel("Ano-Mês")
#     plt.ylabel("Número de Acidentes")
#     plt.title(f"Regressão Linear - Previsão de Acidentes ({estado})")
#     plt.legend()
#     plt.xticks(rotation=45)
#     plt.grid(True)
#     plt.show()



if __name__ == "__main__":
    # Carrega os dados do Data Warehouse
    db_name = "databases/datawarehouse.db"  # Atualize com o caminho do banco de dados
    table_name = "acidentes"  # Nova tabela
    df = extract_data(db_name, table_name)

    # Realiza a previsão para os próximos meses
    predict_accidents(df)



    # Realiza a previsão para os próximos meses de um determinado estado sugerido.
    #predict_accidents(df, "SP")  # Substitua "SP" pelo estado desejado
    