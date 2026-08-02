import  mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "Lendario20.",
    database = "innature"
)

cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS produtos(id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(100) NOT NULL,preco DECIMAL(10,2) NOT NULL,quantidade int NOT NULL)")

