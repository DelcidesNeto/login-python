def verificacao(email):
    import mysql.connector as mysql
    banco = mysql.connect(host='aws-sa-east-1.connect.psdb.cloud',
                          database='users',
                          user='k6as35kri5xcmlo9ops4',
                          password='pscale_pw_iyoSaFp3J1nda5qcpayYSkqLliNVsOSwNWR7YSZla5b',
                          ssl_verify_identity=True,
                          ssl_ca='cacert-2023-01-10.pem',
                          use_pure=True)
    if banco.is_connected():
        editar = banco.cursor()
        editar.execute(f"select email from users where email = '{email}';")
        dado = editar.fetchone()
        editar.close()
        if dado != None:
            return True
        else:
            return False


def adicionar_usuario(nome_usuario, email, senha):
    from random import randint
    import mysql.connector as mysql
    banco = mysql.connect(host='aws-sa-east-1.connect.psdb.cloud',
                          database='users',
                          user='k6as35kri5xcmlo9ops4',
                          password='pscale_pw_iyoSaFp3J1nda5qcpayYSkqLliNVsOSwNWR7YSZla5b',
                          ssl_verify_identity=True,
                          ssl_ca='cacert-2023-01-10.pem',
                          use_pure=True)
    if banco.is_connected():
        while True:
            id_usuario = f'{randint(0, 9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}'
            verificar = banco.cursor()
            verificar.execute('select id_usuario from users;')
            dados = str(verificar.fetchall()).replace("'", '').replace(' ', '').replace(',', '').replace('[', '').replace(']', '').replace('(', '').split(')')
            verificar.close()
            if id_usuario in dados:
                continue
            else:
                editar = banco.cursor()
                editar.execute(f"insert into users values (id, '{id_usuario}', '{nome_usuario}', '{email}', '{senha}');")
                banco.commit() #Utiliza-se o commit sempre após o comando ser relacionado à inserir dados em uma tabela
                banco.close()
                editar.close()
                break


def login(email=''):
    import mysql.connector as mysql
    banco = mysql.connect(host='aws-sa-east-1.connect.psdb.cloud',
                          database='users',
                          user='k6as35kri5xcmlo9ops4',
                          password='pscale_pw_iyoSaFp3J1nda5qcpayYSkqLliNVsOSwNWR7YSZla5b',
                          ssl_verify_identity=True,
                          ssl_ca='cacert-2023-01-10.pem',
                          use_pure=True)
    if banco.is_connected():
        editar = banco.cursor()
        editar.execute(f"select id_usuario, usuario, email, senha from users where email = '{email.lower()}';") #verificacao para login
        dado = editar.fetchone()
        banco.close()
        editar.close()
        return dado

