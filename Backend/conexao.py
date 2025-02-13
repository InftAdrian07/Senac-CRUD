

import mysql.connector
from mysql.connector import Error


class DatabaseConnection:
    def __init__(self):
        self.host = "192.168.122.26"
        self.user = "root"
        self.password = "ubuntu"
        self.database = "EMPRESA"
        self.connection = None
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect (host=self.host, user=self.user, password=self.password, database=self.database)
            if self.connection.is_connected():
                print("Conexão bem-sucedida ao banco de dados.")
        except Error as e:
            print(f"Erro ao conectar ao MYSQL: {e}")
   
    def close_connection(self):
        """Fecha a conexão com o banco de dados."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexão fechada.")

    def incluir_usuario(self, funcionario, cidade, salario, data_contratacao):
        cursor = self.connection.cursor()
        sql = f"INSERT INTO funcionario (funcionario,cidade,salario,data_contratacao) VALUES ({funcionario},{cidade},{salario},{data_contratacao})"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
        print("Registro incluido com sucesso")


        
       



db = DatabaseConnection()
db.incluir_usuario('Marcolino','Jaboticabal',43000,'1999-05-12')