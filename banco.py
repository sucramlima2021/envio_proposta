import sqlite3

conn = sqlite3.connect('conf.db')

cursor = conn.cursor()

sql_tabela_valores_fixos = '''CREATE TABLE IF NOT EXISTS valores_fixos (
	id integer PRIMARY KEY,
    decesso text NOT NULL
)'''

sql_tabela_configuracoes = '''CREATE TABLE IF NOT EXISTS configuracoes (
	id integer PRIMARY KEY,
	caminho_bd text NOT NULL
)'''

sql_tabela_usuarios = '''CREATE TABLE IF NOT EXISTS usuarios (
	id integer PRIMARY KEY,
	nome text NOT NULL,
    senha text NOT NULL,
    tipo integer NOT NULL
)'''


cursor.execute(sql_tabela_valores_fixos)
cursor.execute(sql_tabela_configuracoes)
cursor.execute(sql_tabela_usuarios)





conn.commit()
conn.close()