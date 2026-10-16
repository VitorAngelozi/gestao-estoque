import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

conexao = psycopg.connect(
	host= os.getenv("DB_HOST"),
	port= os.getenv("DB_PORT"),
	dbname= os.getenv("DB_NAME"),
	user= os.getenv("DB_USERNAME"),
	password = os.getenv("DB_PASSWORD")

	)

cursor = conexao.cursor()
print(conexao.closed)
cursor.execute("SELECT * FROM tb_produtos")
produtos = cursor.fetchall()
for produto in produtos:
	print(f"Produto: {produto[1]}")
	print(f"Valor: {produto[2]}")
	print(f"Estoque: {produto[3]}")
	print("="*10)

cursor.close()
conexao.close()