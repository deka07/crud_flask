from sqlite3.dbapi2 import Cursor
from flask import Flask, render_template, redirect, request, url_for
import sqlite3 

app = Flask(__name__)

@app.route("/index", methods = ['POST', 'GET'])
def index():
    # Conenctando com o banco:
    banco = sqlite3.connect('database.db')
    cursor = banco.cursor()
    cursor.row_factory = sqlite3.Row

    cursor.execute("SELECT * fROM tb_produtos")
    rows = cursor.fetchall()

    return render_template('/index.html', rows = rows)


@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    
    if request.method == "POST":
        produto = request.form.get('add-1')
        valor = request.form.get('add-2')

        banco = sqlite3.connect('database.db')
        cursor = banco.cursor()
        
        try:
            cursor.execute('INSERT INTO tb_produtos (produto, valor) VALUES (?,?)', (produto, valor))
            banco.commit()
            msg = 'Salvo!'
                
        except sqlite3.Error:
            banco.rollback()
            msg = 'Erro!'

        finally:
            banco.close()
            return redirect(url_for('index'))
            
    
    return render_template("cadastro.html")


if __name__ == "__main__":
    app.run(debug=True)