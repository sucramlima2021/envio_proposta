import sqlite3
import pyodbc
conn = sqlite3.connect('conf.db')

cursor = conn.cursor()

cursor.execute("insert into valores_fixos(decesso) values('4000')")
cursor.execute("insert into configuracoes(caminho_bd) values('vazio')")
cursor.execute("insert into usuarios(nome, senha, tipo) values('admin', '123', 3)")
cursor.execute("insert into usuarios(nome, senha, tipo) values('admin2', '123', 2)")
cursor.execute("insert into usuarios(nome, senha, tipo) values('admin3', '123', 1)")
conn.commit()


conn.close()