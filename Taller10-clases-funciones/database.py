import sqlite3

class Database:
    def __init__(self, db_name: str = "taller_mecanico.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        """Establece la conexión con la base de datos"""
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            print(f"Conexión establecida con {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")