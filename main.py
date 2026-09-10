import sqlite3 as sqlite

conn = sqlite.connect("biblioteca.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios")

resultados = cursor.fetchall()

for lin in resultados:
    print(f"id: {lin[0]} | nome:{lin[1]}")

conn.close()