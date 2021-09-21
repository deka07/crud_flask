import sqlite3

class Banco_db:

   def conectar_db(self):
      self.banco = sqlite3.connect('database.db')
      self.cursor = self.banco.cursor()


   def select_db(self):  
      self.conectar_db()
      self.cursor.execute("SELECT * fROM tb_produtos")
      self.cursor.fetchall()
      self.cursor.close()

   def adicionar(self):
      self.conectar_db()
      self.cursor.execute("INSERT INTO tb_produtos (id, produto, valor) VALUES (01, 'Iphonec11', '7.500')")
      self.cursor.fetchall()
      self.cursor.close()

   def listar(self):
      self.conectar_db()
      self.cursor.row_factory = sql.Row
      self.cursor.execute("SELECT * fROM tb_produtos")
      self.cursor.fetchall()
      self.cursor.close()
      
   