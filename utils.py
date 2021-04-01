from models import Pessoa, db_session


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
    q = db_session.query(Pessoa)
    pessoa = Pessoa.query.filter_by(id=3).first()
    pessoa.nome = 'Bernardo Lopes'
    pessoa.idade = 2
    pessoa.save()


def exclue():
    pessoa = Pessoa.query.filter_by(id=4).first()
    pessoa.delete()


if __name__ == '__main__':
    # insere()
    # edita()
    exclue()
    consulta()
