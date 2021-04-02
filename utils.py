from models import Pessoa, db_session, Usuario


def insere():
    pessoa = Pessoa(nome='Janaina', idade=27)
    pessoa.save()


def consultaOne(nome):
    pessoa = Pessoa.query.filter_by(nome=nome)
    for p in pessoa:
        print(p.nome)


def consulta():
    pessoa = Pessoa.query.all()
    for p in pessoa:
        print(p.nome)


def edita():
    pessoa = Pessoa.query.filter_by(id=3).first()
    pessoa.nome = 'Bernardo Lopes'
    pessoa.idade = 2
    pessoa.save()


def exclue():
    pessoa = Pessoa.query.filter_by(id=4).first()
    pessoa.delete()


def insere_usuario():
    usuario = Usuario(login='Kennedy', senha='1234')
    usuario.save()


def consulta_usuario():
    usuario = Usuario.query.all()
    for p in usuario:
        print(p.login, p.senha)


if __name__ == '__main__':
    insere_usuario()
    # edita()
    # exclue()
    consulta_usuario()
