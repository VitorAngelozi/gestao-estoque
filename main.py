from database import conectar
from produtos import listar_produtos

conexao = conectar()

produtos = listar_produtos(conexao)

for produto in produtos:
    print(f"Produto: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']}")
    print(f"Quantidade em estoque: {produto['estoque']}")

conexao.close()