
# Acidentes-de-carro-no-Brasil
Projeto de ciência de dados do curso de Ciência de Dados e Inteligência Artificial da Universidade do Oeste de Santa Catarina (UNOESC). 

## Tecnologias
- Python
- Pandas
- Git/GitHub
- SQLite
- DBeaver
- Matplotlib
- Plotly
- Scikit-learn

## Como executar o projeto
1. Crie o ambiente virtual python e instale as dependências do projeto.
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate
# Linux ou MacOS
source .venv/bin/activate

pip install -r requirements.txt
```
2. Execute o script `etl.py` (caso queira processar os dados)
3. Para análise gráfica, execute o script `analyze.py`
4. Para análise estatística (com regressão linear simples), execute o script `predict.py`

## Problema de Negócio
O governo do Brasil precisa entender quais as principais causas de acidentes de trânsito, quais os períodos, quais dias da semana, quais as regiões com mais acidentes e os horários com maior incidência, para poder destinar da melhor forma possível recursos para reduzir os acidentes. O projeto consiste em analisar dados dos acidentes no Brasil utilizando técnicas de Ciência de Dados para identificar padrões e tendências.

## Requisitos de Negócio
* Coletar dados de acidentes de transito no Brasil como dados de data, dia da semana, quantidade, horários.
* Analisar os dados de acidentes identificando quais os períodos do ano, dias da semana, horários e estados com maiores problemas.
* Criar um modelo preditivo para prever o número de acidentes nos próximos meses, utilizando técnicas de análise estatística.

## Explicação do Projeto
Com base no objetivo do projeto, foi localizado um dataset no Kaggle com dados de acidentes de veículos no Brasil. O dataset contém informações sobre a localização, data e quantidade de acidentes de trânsito. O projeto consiste em realizar uma análise exploratória dos dados, identificando os meses, dias da semana e estados com maior número de acidentes. Além disso, será criado um modelo preditivo para prever o número de acidentes nos próximos 12 meses.

Como primeira etapa, optou-se pela criação de um banco de dados SQLite para armazenamento dos dados do dataset, como uma área de staging, onde os dados serão armazenados antes de serem processados. Essa etapa é importante para garantir a integridade dos dados e facilitar o acesso aos dados para análise. Também visa a persistência dos dados para evitar dependência do dataset original, que pode ser alterado ou removido. Nessa primeira etapa, também foi realizada uma análise exploratória dos dados, identificando quais colunas e tipos de dados deveriam ser armazenados no banco de dados. A partir dessa análise, foram criadas as tabelas no banco de dados SQLite. Todos esses itens estão no script extract.py.

Na segunda etapa, foi realizada outra análise exploratória, visando entender quais transformações seriam necessárias para que os dados ficassem íntegros para utilização no projeto. Essa etapa é importante para garantir que os dados estejam prontos para serem utilizados na análise e no modelo preditivo. Nessa etapa, foram identificados os tipos de dados que deveriam ser utilizados, as colunas que deveriam ser removidas e as colunas que deveriam ser transformadas. Essas transformações foram realizadas no script transform.py.

Posteriormente, para finalizar o processo de ETL, foi criado um datawarehouse, onde os dados transformados foram armazenados. Essa etapa é importante para garantir que os dados estejam prontos para serem utilizados na análise e no modelo preditivo. O datawarehouse foi criado no script load.py.

Com os dados processados e armazenados no datawarehouse, foi realizada uma análise gráfica dos dados, utilizando a biblioteca Plotly Express. Essa etapa é importante para visualizar os dados e identificar padrões e tendências. A análise gráfica foi realizada no script analyze.py.

Na última etapa, foi criado um modelo estatístico, com a técnica de regressão linear simples, para prever o número de acidentes nos próximos 12 meses, no script predict.py.

## Resultados
Com a análise gráfica foi possível observar que o mês de julho é o mês com maior número de acidentes, seguido por janeiro e agosto os quais coincidem com os períodos de férias coletivas, visto também que há 2 horários de pico de acidentes, sendo eles as 07:00 horas e as 18:00 horas (este segundo com maior incidência), sendo que o segundo é de maior gravidade. Além disso, foi possível identificar que os estados com mais acidentes são Minas Gerais (MG), Santa Catarina (SC) e Paraná (PR). Os dias da semana com mais ocorrências são sábado seguido de domingo e posteriormente sexta-feira. Nota-se também que o índice de acidentes vem diminuindo de 2017 em diante.

Através de um modelo de regressão linear simples, foi possível prever que o número de acidentes deve continuar diminuindo nos próximos anos. Essa informação é importante para o governo do Brasil, pois pode ajudar a direcionar os recursos para as áreas mais afetadas e a desenvolver políticas públicas para reduzir o número de acidentes com foco nestas informações.

## Referências
- [Dataset](https://www.kaggle.com/datasets/mlippo/car-accidents-in-brazil-2017-2023?select=accidents_2017_to_2023_portugues.csv) 
in 13/06/2025