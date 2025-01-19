from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import urllib.request, json

app = Flask(__name__)
app.secret_key = 'Teste'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cursos.sqlite3'
db = SQLAlchemy(app)

frutas = []
registros = []


class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(100))
    ch = db.Column(db.Integer)

    def __init__(self, nome, descricao, ch):
        self.nome = nome
        self.descricao = descricao
        self.ch = ch



@app.route('/', methods=["GET", "POST"])
def principal():
    if request.method == "POST":
        nova_fruta = request.form.get('fruta')
        if nova_fruta:
            frutas.append(nova_fruta)
            
    return render_template("index.html", frutas=frutas)


@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    if request.method == "POST":
        aluno = request.form.get("aluno")
        nota = request.form.get("nota")
        if aluno and nota:
            registros.append({"aluno": aluno, "nota": nota})

    return render_template("sobre.html", registros=registros)





@app.route('/filmes/<propriedades>', methods=['GET', 'POST'])
def filmes(propriedades):
    if propriedades == "Mais Populares":
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=1c770b7c9a2cfd1d969d06b14f3e232b"
    
    elif propriedades == "Kids":
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=1c770b7c9a2cfd1d969d06b14f3e232b"

    elif propriedades == "2010":
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=1c770b7c9a2cfd1d969d06b14f3e232b"

    elif propriedades == "Drama":
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key=1c770b7c9a2cfd1d969d06b14f3e232b"

    elif propriedades == "Tom_Cruise":    
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=1c770b7c9a2cfd1d969d06b14f3e232b"


    resposta = urllib.request.urlopen(url)

    dados = resposta.read()
    jsondata = json.loads(dados)

    return render_template("filmes.html", filmes=jsondata['results'])


@app.route('/cursos')
def lista_cursos():
    page = request.args.get('page', 1, type=int)
    per_page = 4
    todos_cursos = Curso.query.paginate(page=page, per_page=per_page)
    
    return render_template('cursos.html', cursos=todos_cursos)

    


@app.route('/cria_curso', methods=['GET', 'POST'])
def cria_curso():
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    ch = request.form.get('ch')

    if request.method == 'POST':
        if not nome or not descricao or not ch:
            flash("Preencha todos os campos do formulario", "error")
        else:
            curso = Curso(nome, descricao, ch)
            db.session.add(curso)
            db.session.commit()
            return redirect(url_for('lista_cursos'))
    return render_template('novo_curso.html')



@app.route('/<int:id>/atualiza_curso', methods=['GET', 'POST'])
def atualiza_curso(id):
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        ch = request.form['ch']
        
        Curso.query.filter_by(id=id).update({'nome': nome, 'descricao':descricao, 'ch': ch})
        db.session.commit()
        return redirect(url_for('lista_cursos'))

    curso = Curso.query.filter_by(id=id).first()
    return render_template('atualiza_curso.html', curso=curso)




@app.route('/<int:id>/remove_curso')
def remove_curso(id):
    curso = Curso.query.filter_by(id=id).first()
    db.session.delete(curso)
    db.session.commit()
    return redirect(url_for('lista_cursos'))



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
