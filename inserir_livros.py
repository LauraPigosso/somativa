from conexao import conexao


def limpa():
    cursor = conexao.cursor()
    cursor.execute("TRUNCATE tabela")
    conexao.commit()

def inserir(editora, nome, preco):


    inserir_usuarios = f"""INSERT INTO tabela(editora, nome, preco)
        values
        ("{editora}", "{nome}", {preco});"""
    cursor = conexao.cursor()

    cursor.execute(inserir_usuarios)
    conexao.commit()
