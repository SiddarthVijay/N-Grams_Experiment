from flask import Flask, render_template, flash, redirect, url_for, session, request, logging

from experiment_answers import Answers
from data import Articles
from forms import *

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
    form = ExperimentCorpusA(request.form)

    if request.method == 'POST':
        field_data = []

        field_row1 = []
        field_row1.append(form.field1_1.data)
        field_row1.append(form.field1_2.data)
        field_row1.append(form.field1_3.data)
        field_row1.append(form.field1_4.data)
        field_row1.append(form.field1_5.data)
        field_row1.append(form.field1_6.data)
        field_row1.append(form.field1_7.data)

        field_row2 = []
        field_row2.append(form.field2_1.data)
        field_row2.append(form.field2_2.data)
        field_row2.append(form.field2_3.data)
        field_row2.append(form.field2_4.data)
        field_row2.append(form.field2_5.data)
        field_row2.append(form.field2_6.data)
        field_row2.append(form.field2_7.data)

        field_row3 = []
        field_row3.append(form.field3_1.data)
        field_row3.append(form.field3_2.data)
        field_row3.append(form.field3_3.data)
        field_row3.append(form.field3_4.data)
        field_row3.append(form.field3_5.data)
        field_row3.append(form.field3_6.data)
        field_row3.append(form.field3_7.data)

        field_row4 = []
        field_row4.append(form.field4_1.data)
        field_row4.append(form.field4_2.data)
        field_row4.append(form.field4_3.data)
        field_row4.append(form.field4_4.data)
        field_row4.append(form.field4_5.data)
        field_row4.append(form.field4_6.data)
        field_row4.append(form.field4_7.data)

        field_row5 = []
        field_row5.append(form.field5_1.data)
        field_row5.append(form.field5_2.data)
        field_row5.append(form.field5_3.data)
        field_row5.append(form.field5_4.data)
        field_row5.append(form.field5_5.data)
        field_row5.append(form.field5_6.data)
        field_row5.append(form.field5_7.data)

        field_row6 = []
        field_row6.append(form.field6_1.data)
        field_row6.append(form.field6_2.data)
        field_row6.append(form.field6_3.data)
        field_row6.append(form.field6_4.data)
        field_row6.append(form.field6_5.data)
        field_row6.append(form.field6_6.data)
        field_row6.append(form.field6_7.data)

        field_row7 = []
        field_row7.append(form.field7_1.data)
        field_row7.append(form.field7_2.data)
        field_row7.append(form.field7_3.data)
        field_row7.append(form.field7_4.data)
        field_row7.append(form.field7_5.data)
        field_row7.append(form.field7_6.data)
        field_row7.append(form.field7_7.data)

        field_data.append(field_row1)
        field_data.append(field_row2)
        field_data.append(field_row3)
        field_data.append(field_row4)
        field_data.append(field_row5)
        field_data.append(field_row6)
        field_data.append(field_row7)

        print(field_data)
    return render_template('experiment_corpusA.html', form=form)


@app.route('/experiment_corpusB', methods=['GET', 'POST'])
def experiment_corpusB():
    form = ExperimentCorpusB(request.form)

    if request.method == 'POST':
        field_data = []

        field_row1 = []
        field_row1.append(form.field1_1.data)
        field_row1.append(form.field1_2.data)
        field_row1.append(form.field1_3.data)
        field_row1.append(form.field1_4.data)
        field_row1.append(form.field1_5.data)
        field_row1.append(form.field1_6.data)
        field_row1.append(form.field1_7.data)
        field_row1.append(form.field1_8.data)
        field_row1.append(form.field1_9.data)
        field_row1.append(form.field1_10.data)
        field_row1.append(form.field1_11.data)

        field_row2 = []
        field_row2.append(form.field2_1.data)
        field_row2.append(form.field2_2.data)
        field_row2.append(form.field2_3.data)
        field_row2.append(form.field2_4.data)
        field_row2.append(form.field2_5.data)
        field_row2.append(form.field2_6.data)
        field_row2.append(form.field2_7.data)
        field_row2.append(form.field2_8.data)
        field_row2.append(form.field2_9.data)
        field_row2.append(form.field2_10.data)
        field_row2.append(form.field2_11.data)

        field_row3 = []
        field_row3.append(form.field3_1.data)
        field_row3.append(form.field3_2.data)
        field_row3.append(form.field3_3.data)
        field_row3.append(form.field3_4.data)
        field_row3.append(form.field3_5.data)
        field_row3.append(form.field3_6.data)
        field_row3.append(form.field3_7.data)
        field_row3.append(form.field3_8.data)
        field_row3.append(form.field3_9.data)
        field_row3.append(form.field3_10.data)
        field_row3.append(form.field3_11.data)

        field_row4 = []
        field_row4.append(form.field4_1.data)
        field_row4.append(form.field4_2.data)
        field_row4.append(form.field4_3.data)
        field_row4.append(form.field4_4.data)
        field_row4.append(form.field4_5.data)
        field_row4.append(form.field4_6.data)
        field_row4.append(form.field4_7.data)
        field_row4.append(form.field4_8.data)
        field_row4.append(form.field4_9.data)
        field_row4.append(form.field4_10.data)
        field_row4.append(form.field4_11.data)

        field_row5 = []
        field_row5.append(form.field5_1.data)
        field_row5.append(form.field5_2.data)
        field_row5.append(form.field5_3.data)
        field_row5.append(form.field5_4.data)
        field_row5.append(form.field5_5.data)
        field_row5.append(form.field5_6.data)
        field_row5.append(form.field5_7.data)
        field_row5.append(form.field5_8.data)
        field_row5.append(form.field5_9.data)
        field_row5.append(form.field5_10.data)
        field_row5.append(form.field5_11.data)

        field_row6 = []
        field_row6.append(form.field6_1.data)
        field_row6.append(form.field6_2.data)
        field_row6.append(form.field6_3.data)
        field_row6.append(form.field6_4.data)
        field_row6.append(form.field6_5.data)
        field_row6.append(form.field6_6.data)
        field_row6.append(form.field6_7.data)
        field_row6.append(form.field6_8.data)
        field_row6.append(form.field6_9.data)
        field_row6.append(form.field6_10.data)
        field_row6.append(form.field6_11.data)

        field_row7 = []
        field_row7.append(form.field7_1.data)
        field_row7.append(form.field7_2.data)
        field_row7.append(form.field7_3.data)
        field_row7.append(form.field7_4.data)
        field_row7.append(form.field7_5.data)
        field_row7.append(form.field7_6.data)
        field_row7.append(form.field7_7.data)
        field_row7.append(form.field7_8.data)
        field_row7.append(form.field7_9.data)
        field_row7.append(form.field7_10.data)
        field_row7.append(form.field7_11.data)

        field_row8 = []
        field_row8.append(form.field8_1.data)
        field_row8.append(form.field8_2.data)
        field_row8.append(form.field8_3.data)
        field_row8.append(form.field8_4.data)
        field_row8.append(form.field8_5.data)
        field_row8.append(form.field8_6.data)
        field_row8.append(form.field8_7.data)
        field_row8.append(form.field8_8.data)
        field_row8.append(form.field8_9.data)
        field_row8.append(form.field8_10.data)
        field_row8.append(form.field8_11.data)

        field_row9 = []
        field_row9.append(form.field9_1.data)
        field_row9.append(form.field9_2.data)
        field_row9.append(form.field9_3.data)
        field_row9.append(form.field9_4.data)
        field_row9.append(form.field9_5.data)
        field_row9.append(form.field9_6.data)
        field_row9.append(form.field9_7.data)
        field_row9.append(form.field9_8.data)
        field_row9.append(form.field9_9.data)
        field_row9.append(form.field9_10.data)
        field_row9.append(form.field9_11.data)

        field_row10 = []
        field_row10.append(form.field10_1.data)
        field_row10.append(form.field10_2.data)
        field_row10.append(form.field10_3.data)
        field_row10.append(form.field10_4.data)
        field_row10.append(form.field10_5.data)
        field_row10.append(form.field10_6.data)
        field_row10.append(form.field10_7.data)
        field_row10.append(form.field10_8.data)
        field_row10.append(form.field10_9.data)
        field_row10.append(form.field10_10.data)
        field_row10.append(form.field10_11.data)

        field_row11 = []
        field_row11.append(form.field11_1.data)
        field_row11.append(form.field11_2.data)
        field_row11.append(form.field11_3.data)
        field_row11.append(form.field11_4.data)
        field_row11.append(form.field11_5.data)
        field_row11.append(form.field11_6.data)
        field_row11.append(form.field11_7.data)
        field_row11.append(form.field11_8.data)
        field_row11.append(form.field11_9.data)
        field_row11.append(form.field11_10.data)
        field_row11.append(form.field11_11.data)

        field_data.append(field_row1)
        field_data.append(field_row2)
        field_data.append(field_row3)
        field_data.append(field_row4)
        field_data.append(field_row5)
        field_data.append(field_row6)
        field_data.append(field_row7)
        field_data.append(field_row8)
        field_data.append(field_row9)
        field_data.append(field_row10)
        field_data.append(field_row11)

        print(field_data)
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
