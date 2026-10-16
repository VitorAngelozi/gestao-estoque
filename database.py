import psycopg
import os
from dotenv import load_dotenv
from psycopg.rows import dict_row

load_dotenv()

#conexao com banco de dados pelo env
def conectar():
    conexao = psycopg.connect(
        host= os.getenv("DB_HOST"),
        port= os.getenv("DB_PORT"),
        dbname= os.getenv("DB_NAME"),
        user= os.getenv("DB_USERNAME"),
        password = os.getenv("DB_PASSWORD")
        )
    return conexao
#cria cursos que vai fazer a conexao com bd e transformar as colunas em dic
cursor = conexao.cursor(row_factory=dict_row)


