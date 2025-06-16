import extract
import transform
import load


# ===== EXTRACT =====

if __name__=="__main__":
    # Define o caminho do arquivo CSV
    file_path = "data/acidentes.csv"
    # Extrai os dados do arquivo CSV
    data = extract.extract_data(file_path)
    # Realiza a exploração de dados
    extract.data_exploration(data)
    # Cria a database SQLite
    db_name = "databases/stage.db"
    extract.create_database(db_name)
    # Cria a tabel
    table_name = "acidentes"
    extract.create_table(db_name, table_name)
    extract.insert_data(data, db_name, table_name)
    print(f"\n Extract completed. \n ")

# ===== TRANSFORM =====

    # Lê os dados da tabela SQLite
    stage_data = transform.read_sqlite(db_name, table_name)
    # Analisa os dados para verificar transformações necessárias
    stage_data = transform.analyse_data(stage_data)
    # Transforma coluna em tipo text novamente porque o SQLite não suporta Datetime.
    stage_data = transform.transform_data_inversa_to_date(stage_data)
    print(f"\nTransform completed.\n")

# ===== LOAD =====

     # Cria o datawarehouse
    db_name = "databases/datawarehouse.db"
    table_name = "acidentes"
    load.create_database(db_name)
    # Cria a tabela e insere os dados
    load.create_table(db_name, table_name)
    load.insert_data(stage_data, db_name, table_name)
    print(f"\nLoad completed.\n")


    ## PAREI NOS 01:12 DA AULA 2