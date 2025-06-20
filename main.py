import mysql.connector as connector

conexao = connector.connect(
    host="localhost",
    user="root",
    passwd="your_password",
    database="your_database"
)
cursor = conexao.cursor()

## CRUD



## C = CREATE
#nome_produto = "Maça"
#valor_produto = 4
#add_value = f'INSERT INTO vendas(nome_produto, valor) VALUES("{nome_produto}", {valor_produto})'
#cursor.execute(add_value)
#conexao.commit() ## Edita o banco de dados


## R = READ
#read_velue = 'SELECT * FROM vendas'
#cursor.execute(read_velue)
#resultado = cursor.fetchall()
#print(resultado)


## U = UPDATE
#nome_produto = "Abacaxi"
#valor_produto = 8
#comando = f'UPDATE vendas SET valor = {valor_produto} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit()

# D = DELETE
#nome_produto = "Abacaxi"
#valor_produto = 8
#comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"' #estou tentando deletar o produto pelo nome_priduto
#cursor.execute(comando)
#conexao.commit()


cursor.close()
conexao.close()