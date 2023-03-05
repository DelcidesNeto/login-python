from flask import Flask, render_template, request, redirect, session
from funcao import verificacao, adicionar_usuario, login

site = Flask(__name__)
site.config['SECRET_KEY'] = 'Neto@tvsd.com.br'
mensagem_login = ['']
mensagem_cadastro = ['']
nome_user = ['']
mensagem_perfil = ['']


@site.route('/')
def index():
    try:
        if session['usuario_logado'] != None:
            return redirect('/perfil') 
    except:
        return render_template('index.html')
    else:
        return render_template('index.html')


@site.route('/pag_cadastro')
def pag_cadastro():
    mensagem_login[0] = ''
    mensagem_perfil[0] = ''
    return render_template('cadastro.html', msg = mensagem_cadastro[0])


@site.route('/cadastrar', methods=['post'])
def cadastro():
    usuario = request.form['usuario'].capitalize()
    email = request.form['email'].lower()
    senha = request.form['senha']
    if verificacao(email) not in [False]:
        mensagem_cadastro[0] = 'Este email já foi cadastrado! Cadastre-se utilizando outro e-mail!'
        return redirect('/pag_cadastro')
    else:
        adicionar_usuario(usuario, email, senha)
        mensagem_cadastro[0] = 'Cadastro realizado com sucesso!'
        return redirect('/pag_cadastro')


@site.route('/pag_login')
def pag_login():
    try: #Adicionei o try, pois se você limpar os dados do seu navegador, dará um erro, para resolver utilizei o try com o except redefinindo o usuario logado para None fazendo assim o logout automático para evitar bugs no sistema e redirecionando novamente para a pagina de login para que o realize novamente
        if nome_user[0] == '':
            session['usuario_logado'] = None
        mensagem_cadastro[0] = ''
        mensagem_perfil[0] = ''
        if session['usuario_logado'] == None:
            return render_template('login.html', msg = mensagem_login[0])
        else:
            mensagem_perfil[0] = 'Para fazer login saia da sua conta!'
            return redirect('/perfil')
    except:
        session['usuario_logado'] = None
        return redirect('/pag_login')


@site.route('/logar', methods=['post'])
def logar():
    email = request.form['email'].lower()
    senha = request.form['senha']
    dado = login(email)
    if dado == None:
        mensagem_login[0] = 'Este e-mail não está cadastrado, cadastre para usá-lo'
        return redirect('/pag_login')
    elif dado[2] == email and dado[3] == senha:
        mensagem_login[0] = ''
        session['usuario_logado'] = dado[0]
        nome_user[0] = dado[1]
        return redirect('/perfil')
    else:
        mensagem_login[0] = 'Login ou senha incorretos'
        return redirect('/pag_login')


@site.route('/perfil')
def perfil():
    return render_template('perfil.html', nome_usuario = nome_user[0], msg = mensagem_perfil[0])


@site.route('/logout')
def logout():
    session['usuario_logado'] = None
    return redirect('/perfil')


if __name__ == '__main__':
    site.run(debug=True)
