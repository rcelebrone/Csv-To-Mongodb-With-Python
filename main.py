import sys
from typing import TextIO
from pymongo import MongoClient

SEPARADOR_CSV = ","

#
def main():
    try:
        nome_arquivo = sys.argv[1]
    except IndexError:
        print("Informe o nome do arquivo\n",">>> python main.py dados.csv")
        return

    resultado = importar(nome_arquivo)
    if resultado is not None:
        if resultado.acknowledged:
                print(len(resultado.inserted_ids), 
                    "documentos foram inseridos.")
        else:
            print("nenhum documento inserido.")
    else:
        print("não tem dados para importar.")

    return resultado

#
def converter(csv: TextIO) -> list[dict]:
    primeira_linha = next(csv, None)
    if primeira_linha is None:
        return []

    cabecalho = ajusta_linha(primeira_linha)
    dados = []
    for linha in csv:
        colunas = ajusta_linha(linha)
        documento = zip(cabecalho, colunas)
        documento = dict(documento)
        dados.append(documento)

    return dados

#
def ajusta_linha(linha: str):
    return linha.strip().split(SEPARADOR_CSV)

#
def importar(arquivo: str):
    dados = []
    with open(arquivo) as arq:
        dados = converter(arq)
        print(dados)
    
    if dados == []:
        return None
    
    resultado = []
    with MongoClient('localhost:27017',
                  username='root',
                 password='abc123') as client:
        db = client["mongo-server"]
        resultado = db.estoque.insert_many(dados)

    return resultado

#
if __name__ == "__main__":
    main()