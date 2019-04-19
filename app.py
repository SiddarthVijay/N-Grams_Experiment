from flask import Flask, render_template, flash, redirect, url_for, request, logging
from flask_mysqldb import MySQL

from experiment_answers import corpusA, corpusB
from forms import *
from result_checker import resultCheck

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'dbpass123'
app.config['MYSQL_DB'] = 'ngrams'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Inititialize MySQL
mysql = MySQL(app)


# Root page
@app.route('/')
def introduction():
    return render_template('introduction.html')


# Theory page
@app.route('/theory')
def theory():
    return render_template('theory.html')


# Objective page
@app.route('/objective')
def objective():
    return render_template('objective.html')


# Experiment page
@app.route('/experiment', methods=['GET', 'POST'])
def experiment():
    '''
    This function redirects and controls the experiment landing page, where you can choose the Corpus you require
    '''
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


# Experiment page for Corpus A
@app.route('/experiment_corpusA', methods=['GET', 'POST'])
def experiment_corpusA():
    '''
    This function redirects and controls the experiment page for Corpus A
    '''
    form = ExperimentCorpusA(request.form)

    if request.method == 'POST' and form.validate():
        field_data = []

        # Storing form data into variables to run computations on them
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

        correct_result, wrong_result = resultCheck(field_data, corpusA)
        return render_template('results.html', correct=correct_result, wrong=wrong_result)
    return render_template('experiment_corpusA.html', form=form)


# Experiment page for Corpus B
@app.route('/experiment_corpusB', methods=['GET', 'POST'])
def experiment_corpusB():
    '''
    This function redirects and controls the experiment page for Corpus A
    '''
    form = ExperimentCorpusB(request.form)

    if request.method == 'POST' and form.validate():
        # Storing form data into variables to run computations on them
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

        correct_result, wrong_result = resultCheck(field_data, corpusB)

        return render_template('results.html', correct=correct_result, wrong=wrong_result)
    return render_template('experiment_corpusB.html', form=form)


# Quiz page
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


# Interactive Quiz page
@app.route('/take_quiz', methods=['GET', 'POST'])
def take_quiz():
    '''
    This function redirects to and controls the interactive quiz page
    '''
    form = TakeQuiz(request.form)

    if request.method == 'POST' and form.validate():
        correct = 0

        answer_data = []
        answer_data.append(form.question1.data)
        answer_data.append(form.question2.data)
        answer_data.append(form.question3.data)
        answer_data.append(form.question4.data)

        # Adding the user answers to the DB
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user_answers(q1, q2, q3, q4) VALUES(%s, %s, %s, %s)",
                    (answer_data[0], answer_data[1], answer_data[2], answer_data[3]))
        mysql.connection.commit()
        cur.close()

        # Get all questions from the database
        cur = mysql.connection.cursor()
        no_questions = cur.execute("SELECT question FROM qanda")
        if no_questions > 0:
            questions_data = cur.fetchall()
            questions_data_clean = []
            for qu in questions_data:
                questions_data_clean.append(qu['question'])
            print(questions_data_clean)

        mysql.connection.commit()
        cur.close()
        # Checking if the answers are right from the DB
        i = 0
        for ques in questions_data_clean:
            cur = mysql.connection.cursor()
            result = cur.execute(
                "SELECT * FROM qanda where question = %s", [ques])
            print("This is the result")
            print(result)

            if result > 0:
                data = cur.fetchone()
                answer = data['answer']
                print("The answer is: ")
                print(answer)
                print("The user answer is: ")
                print(answer_data[i])
                if answer == answer_data[i]:
                    correct += 1
                i += 1
        mysql.connection.commit()
        cur.close()

        wrong = 4 - correct
        return render_template('quiz_results.html', correct=correct, wrong=wrong)
    return render_template('take_quiz.html', form=form)


# Procedure page
@app.route('/procedure')
def procedure():
    return render_template('procedure.html')


# Further reading page
@app.route('/further_reading')
def further_reading():
    return render_template('further_reading.html')


if __name__ == '__main__':
    app.secret_key = 'bZ\x85\xb2\xfc1$\xe6\n\xa1\xc0\xce\xdd\x9f\x815\xc0\xe4\xac\xc6\xfc\x0e\xa9\xa0V'
    app.run(debug=True)
