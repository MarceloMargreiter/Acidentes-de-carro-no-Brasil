import pandas as pd
import sqlite3
import plotly.express as px


def extract_data(db_name: str, table_name: str) -> pd.DataFrame:
    """
    Extrai os dadados do Data Warehouse.

    Args:
        db_name (str): Nome do banco de dados.
        table_name (str): Nome da tabela.
    Returns:
        pd.DataFrame: DataFrame do pandas com os dados lidos.
    """
    conn = sqlite3.connect(db_name)
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    # Converte a coluna month_year para o formato datetime
    df["month_year"] = pd.to_datetime(df["month_year"], format="%m/%Y")
    conn.close()
    return df


def fires_by_state(df: pd.DataFrame) -> None:
    """
    Agrupa os dados por estado e soma o número de incêndios.

    Args:
        df (pd.DataFrame): DataFrame do pandas com os dados.
    """
    grouped_df = df.groupby("state").agg({"number": "sum"}).reset_index()
    grouped_df = grouped_df.sort_values("number", ascending=False)

    fig = px.bar(
        grouped_df,
        x="state",
        y="number",
        title="Total de incêndios por estado",
        labels={"state": "Estado", "number": "Número de Incêndios"},
        text="number",  # Adiciona os rótulos nas colunas
    )
    fig.update_traces(textangle=-90, textposition="outside")  # Rotaciona os rótulos em 90 graus
    fig.update_layout(
        xaxis_title="Estado",
        yaxis_title="Número de Incêndios",
        title_x=0.5,
    )
    fig.show()


def fires_by_year(df: pd.DataFrame) -> None:
    """
    Agrupa os dados por ano e soma o número de incêndios.

    Args:
        df (pd.DataFrame): DataFrame do pandas com os dados.
    """
    grouped_df = df.groupby("year").agg({"number": "sum"}).reset_index()

    fig = px.bar(
        grouped_df,
        x="year",
        y="number",
        title="Total de incêndios por ano",
        labels={"year": "Ano", "number": "Número de Incêndios"},
        text="number",  # Adiciona os rótulos nas colunas
    )
    fig.update_traces(textangle=-90, textposition="outside")  # Rotaciona os rótulos em 90 graus
    fig.update_layout(
        xaxis_title="Ano",
        yaxis_title="Número de Incêndios",
        title_x=0.5,
    )
    fig.show()


def fires_by_month(df: pd.DataFrame) -> None:
    """
    Agrupa os dados por mês e soma o número de incêndios, ordenando do maior para o menor.

    Args:
        df (pd.DataFrame): DataFrame do pandas com os dados.
    """
    grouped_df = df.groupby("month").agg({"number": "sum"}).reset_index()
    grouped_df = grouped_df.sort_values("number", ascending=False)  # Ordena do maior para o menor

    fig = px.bar(
        grouped_df,
        x="month",
        y="number",
        title="Total de incêndios por mês",
        labels={"month": "Mês", "number": "Número de Incêndios"},
        text="number",  # Adiciona os rótulos nas colunas
    )
    fig.update_traces(textangle=-90, textposition="outside")  # Rotaciona os rótulos em 90 graus
    fig.update_layout(
        xaxis_title="Mês",
        yaxis_title="Número de Incêndios",
        title_x=0.5,
    )
    fig.show()


def fires_by_year_and_month(df: pd.DataFrame) -> None:
    """
    Agrupa os dados por ano e mês e soma o número de incêndios.

    Args:
        df (pd.DataFrame): DataFrame do pandas com os dados.
    """
    grouped_df = df.groupby(["month_year"]).agg({"number": "sum"}).reset_index()
    grouped_df = grouped_df.sort_values("month_year", ascending=True)  # Ordena do maior para o menor
    fig = px.bar(
        grouped_df,
        x="month_year",
        y="number",
        title="Total de incêndios por ano e mês",
        labels={"month_year": "Ano e Mês", "number": "Número de Incêndios"},
        text="number",  # Adiciona os rótulos nas colunas
    )
    fig.update_traces(textangle=-90, textposition="outside")  # Rotaciona os rótulos em 90 graus
    fig.update_layout(
        xaxis_title="Ano e Mês",
        yaxis_title="Número de Incêndios",
        title_x=0.5,
    )
    fig.show()


if __name__ == "__main__":
    # Le os dados da tabela SQLite
    db_name = "databases/datawarehouse.db"
    table_name = "fires"
    data_sqlite = extract_data(db_name, table_name)
    fires_by_state(data_sqlite)
    fires_by_year(data_sqlite)
    fires_by_month(data_sqlite)
    fires_by_year_and_month(data_sqlite)