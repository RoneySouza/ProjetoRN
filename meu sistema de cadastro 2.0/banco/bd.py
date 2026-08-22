
import  mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "Lendario20.",
    database = "innature2.0"
)

cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS login(usuario VARCHAR(100) NOT NULL PRIMARY KEY,hash VARCHAR(100) NOT NULL)")

