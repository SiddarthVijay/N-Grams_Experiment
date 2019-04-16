from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

from experiment_answers import Answers
from data import Articles

app = Flask(__name__)

Articles = Articles()


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


class ChooseExperiment(Form):
    choice = StringField('Choice', [validators.Length(min=1, max=5)])
# class ExperimentFormA(Form):


@app.route('/')
def introduction():
    return render_template('introduction.html')


@app.route('/theory')
def theory():
    return render_template('theory.html')


@app.route('/objective')
def objective():
    return render_template('objective.html')


@app.route('/experiment', methods=['GET', 'POST'])
def experiment():
    form = ChooseExperiment(request.form)
    if request.method == 'POST' and form.validate():
        choice = form.choice.data

        if choice == 'A':
            flash('You have chosen Corpus A', 'success')
            return redirect(url_for('experiment_corpusA'))
        elif choice == 'B':
            flash('You have chosen Corpus B', 'success')
            return redirect(url_for('experiment_corpusB'))
        else:
            flash('This Corpus does not exist', 'success')
            return redirect(url_for('experiment'))
    return render_template('experiment.html', form=form)


@app.route('/experiment_corpusA', methods=['GET', 'POST'])
def experiment_corpusA():
    form = ChooseExperiment(request.form)
    return render_template('experiment_corpusA.html', form=form)


@app.route('/experiment_corpusB', methods=['GET', 'POST'])
def experiment_courpusB():
    form = ChooseExperiment(request.form)
    return render_template('experiment_corpusB.html', form=form)


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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('register.html', form=form)
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.secret_key = 'bZ\x85\xb2\xfc1$\xe6\n\xa1\xc0\xce\xdd\x9f\x815\xc0\xe4\xac\xc6\xfc\x0e\xa9\xa0V'
    app.run(debug=True)
