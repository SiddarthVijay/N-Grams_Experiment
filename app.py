from flask import Flask, render_template
from data import Articles

app = Flask(__name__)

Articles = Articles()


@app.route('/')
def introduction():
    return render_template('introduction.html')


@app.route('/theory')
def theory():
    return render_template('theory.html')


@app.route('/objective')
def objective():
    return render_template('objective.html')


@app.route('/experiment')
def experiment():
    return render_template('experiment.html')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


@app.route('/procedure')
def procedure():
    return render_template('procedure.html')


@app.route('/further_reading')
def further_reading():
    return render_template('further_reading.html')


@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)


@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)


if __name__ == '__main__':
    app.run(debug=True)
