import pandas as pd

# Carregar o arquivo CSV com as coordenadas
localizacao_data = pd.read_csv("data/brutos/IBGE/municipios.csv")

# Carregar o arquivo original de instituições
instituicoes_data = pd.read_csv("data/brutos/EPCT/2022/instituicoes.csv")

# Realizar a junção entre os dois arquivos com base no município
dados_combinados = pd.merge(
  instituicoes_data,
  localizacao_data,
  left_on="NOME_MUNICIPIO_UNIDADE_ENSINO",
  right_on="NOME",
  how="left"
)

# Selecionar as colunas desejadas para salvar
dados_combinados = dados_combinados[
  [
    "SIGLA_INSTITUICAO",
    "NOME_INSTITUICAO",
    "NOME_UNIDADE_ENSINO",
    "ANO",
    "SIGLA_UF_UNIDADE_ENSINO",
    "NOME_MUNICIPIO_UNIDADE_ENSINO",
    "LATITUDE",
    "LONGITUDE",
  ]
]

# Salvar o novo arquivo CSV
dados_combinados.to_csv("data/processados/localizacao_ifs.csv", index=False)

print("Processamento concluído. Dados salvos em 'localizacao_ifs.csv'.")
