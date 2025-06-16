import pandas as pd
import sqlite3
import plotly.express as px


def extract_data(db_name: str, table_name: str) -> pd.DataFrame:  ## OK ====================
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
    # Converte a coluna data_inversa para o formato datetime
    df["data_inversa"] = pd.to_datetime(df["data_inversa"])
    conn.close()
    return df


def acidents_by_state(df: pd.DataFrame) -> None:   ## OK ====================
    """
    Agrupa os dados por estado e conta o número de acidentes.

    Args:
        df (pd.DataFrame): DataFrame do pandas com os dados.
    """
    grouped_df = df.groupby("uf").agg({"data_inversa": "count"}).reset_index()
    grouped_df = grouped_df.sort_values("data_inversa", ascending=False)

    fig = px.bar(
        grouped_df,
        x="uf",
        y="data_inversa",
        title="Total de acidentes por estado",
        labels={"uf": "Estado", "data_inversa": "Número de Acidentes"},
        text="data_inversa",  # Adiciona os rótulos nas colunas
    )
    fig.update_traces(textangle=0, textposition="outside")  # Rotaciona os rótulos em 90 graus
    fig.update_layout(
        xaxis_title="Estado",
        yaxis_title="Número de Acidentes",
        title_x=0.5,
    )
    fig.show()

def acidents_by_year(df: pd.DataFrame) -> None:
    """
    Agrupa os dados por ano e conta o número de acidentes.

    Args:
        df (pd.DataFrame): DataFrame do pandas com os dados.
    """
    df["ano"] = pd.to_datetime(df["data_inversa"]).dt.year  # Extrai apenas o ano
    grouped_df = df.groupby("ano").agg({"data_inversa": "count"}).reset_index()
    grouped_df = grouped_df.sort_values("ano")  # Mantém a ordem cronológica

    fig = px.bar(
        grouped_df,
        x="ano",
        y="data_inversa",
        title="Total de acidentes por ano",
        labels={"ano": "Ano", "data_inversa": "Número de Acidentes"},
        text="data_inversa",
    )

    fig.update_traces(
        texttemplate="%{text:,}".replace(",", "."),  # Ajusta separador de milhar
        textposition="outside"
    )

    fig.update_layout(
        xaxis_title="Ano",
        yaxis_title="Número de Acidentes",
        title_x=0.5,
        xaxis_dtick=1  # Garante que todos os anos sejam exibidos no eixo X
    )

    fig.show()

def acidents_by_month(df: pd.DataFrame) -> None:
    """
    Agrupa os dados por mês e conta o número de acidentes.

    Args:
        df (pd.DataFrame): DataFrame do pandas com os dados.
    """
    df["mes"] = pd.to_datetime(df["data_inversa"]).dt.month  # Extrai apenas o mês
    grouped_df = df.groupby("mes").agg({"data_inversa": "count"}).reset_index()
    grouped_df = grouped_df.sort_values("mes")  # Mantém a ordem cronológica

    fig = px.bar(
        grouped_df,
        x="mes",
        y="data_inversa",
        title="Total de acidentes por mês",
        labels={"mes": "Mês", "data_inversa": "Número de Acidentes"},
        text="data_inversa",
    )

    fig.update_traces(
        texttemplate="%{text:,}".replace(",", "."),  # Ajusta separador de milhar
        textposition="outside"
    )

    fig.update_layout(
        xaxis_title="Mês",
        yaxis_title="Número de Acidentes",
        title_x=0.5,
        xaxis_dtick=1  # Garante que todos os meses sejam exibidos no eixo X
    )

    fig.show()



def acidents_by_hour(df: pd.DataFrame) -> None:  ## OK ====================
    """
    Agrupa os dados por hora (desconsiderando minutos e segundos) e conta o número de acidentes.

    Args:
        df (pd.DataFrame): DataFrame do pandas com os dados.
    """
    df["horario"] = pd.to_datetime(df["horario"]).dt.hour  # Extrai apenas a hora
    grouped_df = df.groupby("horario").agg({"data_inversa": "count"}).reset_index()
    grouped_df = grouped_df.sort_values("horario")  # Mantém a ordem cronológica

    fig = px.bar(
        grouped_df,
        x="horario",
        y="data_inversa",
        title="Total de acidentes por horario do dia",
        labels={"horario": "Horario", "data_inversa": "Número de Acidentes"},
        text="data_inversa",
    )

    fig.update_traces(
        texttemplate="%{text:,}".replace(",", "."),  # Ajusta separador de milhar
        textposition="outside"
    )

    fig.update_layout(
        xaxis_title="Hora do dia",
        yaxis_title="Número de Acidentes",
        title_x=0.5,
        xaxis_dtick=1  # Garante que todas as horas sejam exibidas no eixo X
    )

    fig.show()



def acidents_by_weekday(df: pd.DataFrame) -> None:
    """
    Agrupa os dados por dia da semana e conta o número de acidentes.

    Args:
        df (pd.DataFrame): DataFrame do pandas com os dados.
    """
    grouped_df = df.groupby("dia_semana").agg({"data_inversa": "count"}).reset_index()
    grouped_df = grouped_df.sort_values("data_inversa", ascending=False)  # Ordena pelo número de acidentes

    fig = px.bar(
        grouped_df,
        x="dia_semana",
        y="data_inversa",
        title="Total de acidentes por dia da semana",
        labels={"dia_semana": "Dia da Semana", "data_inversa": "Número de Acidentes"},
        text="data_inversa",
    )

    fig.update_traces(
        texttemplate="%{text:,}".replace(",", "."),  # Ajusta separador de milhar
        textposition="outside"
    )

    fig.update_layout(
        xaxis_title="Dia da Semana",
        yaxis_title="Número de Acidentes",
        title_x=0.5
    )

    fig.show()

def acidents_by_month_year(df: pd.DataFrame) -> None:
    """
    Agrupa os dados por mês e ano e conta o número de acidentes.

    Args:
        df (pd.DataFrame): DataFrame do pandas com os dados.
    """
    df["mes_ano"] = pd.to_datetime(df["data_inversa"]).dt.to_period("M")  # Extrai mês e ano
    grouped_df = df.groupby("mes_ano").agg({"data_inversa": "count"}).reset_index()
    grouped_df["mes_ano"] = grouped_df["mes_ano"].astype(str)  # Converte para string para exibição correta
    grouped_df = grouped_df.sort_values("mes_ano")  # Mantém a ordem cronológica

    fig = px.bar(
        grouped_df,
        x="mes_ano",
        y="data_inversa",
        title="Total de acidentes por mês e ano",
        labels={"mes_ano": "Mês/Ano", "data_inversa": "Número de Acidentes"},
        text="data_inversa",
    )

    fig.update_traces(
        texttemplate="%{text:,}".replace(",", "."),  # Ajusta separador de milhar
        textposition="outside"
    )

    fig.update_layout(
        xaxis_title="Mês/Ano",
        yaxis_title="Número de Acidentes",
        title_x=0.5,
        xaxis_tickangle=-45  # Inclina os rótulos para melhor legibilidade
    )

    fig.show()




if __name__ == "__main__":
    # Lê os dados da tabela SQLite
    db_name = "databases/datawarehouse.db"
    table_name = "acidentes"
    data_sqlite = extract_data(db_name, table_name)
    acidents_by_year(data_sqlite)
    acidents_by_month(data_sqlite)
    acidents_by_month_year(data_sqlite)
    acidents_by_hour(data_sqlite)
    acidents_by_weekday(data_sqlite)
    acidents_by_state(data_sqlite)