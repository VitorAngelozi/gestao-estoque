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

def buscar_produto(id: int):
	if id < 0:
		return False
	cursor.execute(
		"SELECT * FROM tb_produtos WHERE id = %s",
		(id,)
	)
	busca = cursor.fetchone()
	return busca
