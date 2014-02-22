# -*- coding:cp1252 -*-
from flask import Flask, render_template, flash, url_for, redirect, request

app = Flask('CadastroDeBares')

@app.route('/', methods=['GET', 'POST'])
def cadastro():
	if request.method == 'POST':
		nome_do_bar = str(request.form.get('nome_do_bar'))
		endereco = str(request.form.get('endereco'))
		horario_de_funcionamento = str(request.form.get('horario_de_funcionamento'))
		especialidade = str(request.form.get('especialidade'))
		db = open('db.txt', 'a')
		db.write(nome_do_bar + endereco + horario_de_funcionamento + especialidade)
		db.close()
	return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

