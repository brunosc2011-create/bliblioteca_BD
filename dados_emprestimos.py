import sqlite3

conn = sqlite3.connect("biblioteca.db")

sql_create = """CREATE TABLE emprestimos (id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuairo_id INTEGER REFERENCESusuarios(id), 
                data DATE DEFAULT CURRENT_DATE())"""
conn.execute(sql_create)

conn.executemany("INSERT INTO emprestimos (id, usuario_id, data) VALUES(?, ?, ?)",
                 [(1, 1)],
                 [(2, 2)])

conn.commit()