import pandas as pd
import bd

from conexao import conexao, cursor


def limpa():
    cursor = conexao.cursor()
    cursor.execute("TRUNCATE tabela")
    conexao.commit()


def lista_livros_filtro(marca):
    if marca == "todos":
        sql = 'SELECT * from tabela'
    else:
        sql = f"SELECT * from tabela WHERE editora = '{marca}'"
    cursor.execute(sql)
    return cursor.fetchall()


def listar_livros():
    sql = 'SELECT * from tabela'
    cursor.execute(sql)
    return cursor.fetchall()


def inserir(editora, nome, preco):
    inserir_usuarios = f"""INSERT INTO tabela(editora, nome, preco)
        values
        ("{editora}", "{nome}", {preco});"""
    cursor = conexao.cursor()

    cursor.execute(inserir_usuarios)
    conexao.commit()


def toxlsx():
    bda = bd.bd()
    d = bda.listar()
    df = pd.DataFrame(d, columns=["editora", "nome", "preco"])
    df.to_excel('livros.xlsx', index=False, header=True)


def tocsv():
    bda = bd.bd()
    d = bda.listar()
    df = pd.DataFrame(d, columns=["editora", "nome", "preco"])
    df.to_csv('livros.csv', sep=';', encoding='utf-8', index=False)
