import extract

if __name__=="__main__":
    # Define o caminho do arquivo CSV
    file_path = "data/acidentes.csv"
    # Extrai os dados do arquivo CSV
    data = extract.extract_data(file_path)
    # Realiza a exploração de dados
    extract.data_exploration(data)



    ## PAREI NOS 01:10 DA AULA 1