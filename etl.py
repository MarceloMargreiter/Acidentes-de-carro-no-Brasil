import extract

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





    ## PAREI NOS 01:10 DA AULA 1