import psycopg
import os
from dotenv import load_dotenv
from psycopg.rows import dict_row

load_dotenv()

conexao = psycopg.connect(
	host= os.getenv("DB_HOST"),
	port= os.getenv("DB_PORT"),
	dbname= os.getenv("DB_NAME"),
	user= os.getenv("DB_USERNAME"),
	password = os.getenv("DB_PASSWORD")

	)

cursor = conexao.cursor(row_factory=dict_row)
print(conexao.closed)

def cadastrar_produto(nome: str, preco: float, estoque: int):
    # Sua implementação
	cursor.execute(
    "INSERT INTO tb_produtos (nome, preco, estoque) VALUES (%s, %s, %s)", 
	(nome, preco, estoque)
	)
	conexao.commit()
	return True

def listar_produtos():
	cursor.execute(
		"SELECT * FROM tb_produtos"
	)
	produtos = cursor.fetchall()
	return produtos

def atualizar_preco(id: int, novo_preco: float):
	if novo_preco <= 0:
		return False
	cursor.execute(
		"UPDATE tb_produtos SET preco = %s WHERE id = %s",
		(novo_preco, id)
	)
	conexao.commit()
	if cursor.rowcount == 1:
		return True
	else:
		return False
atualizar_preco_mouse= atualizar_preco(1, 100)

assert atualizar_preco(1, -500) == False
assert atualizar_preco(999, 100) == False
if atualizar_preco_mouse:
	print("preco atualizado")
else:
	print("ocorreu algum erro")



#produtos = listar_produtos()
#for produto in produtos:
	#print(f"Produto: {produto['nome']}")
	#print(f"Valor: R${produto['preco']}")
	#print(f"Estoque: {produto['estoque']}")
	#print("="*10)

#cadastrar_mesa = cadastrar_produto("Mesa", 349.90, 2)
#if cadastrar_mesa:
	#print("Cadastrado!")
#else:
	#print("Erro ao cadastrar")

cursor.close()
conexao.close()