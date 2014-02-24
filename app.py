# -*- coding:cp1252 -*-
from flask import Flask, render_template, flash, url_for, redirect, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def cadastro():
	if request.method == 'POST':
		nome_do_bar = str(request.form.get('nome_do_bar'))
		endereco = str(request.form.get('endereco'))
		horario_de_funcionamento = str(request.form.get('horario_de_funcionamento'))
		especialidade_da_casa = str(request.form.get('especialidade_da_casa'))
		if nome_do_bar and endereco and horario_de_funcionamento and especialidade_da_casa:
			db = open('db.txt', 'a')
			db.write(u'%s|%s|%s|%s\n' % (nome_do_bar, endereco, horario_de_funcionamento, especialidade_da_casa))
			db.close()
	return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


