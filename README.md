# N-Grams_Experiment

### Team Members:
* **Siddarth Vijay** - *2018113020*
* **Giri Prasath** - *2018111006*

### Aim: 
Rewrite the experiment of N-grams in V-Labs from PHP and Ajax to Python, Flask and Javascript.

### Softwares Used:
* HTML
* Javascript
* Python3
* Flask
* MySQL.

### Work Done:
* We started with changing the layout of the website and seperating it to parts according to its function and usage.
* Then we rewrote the experiment using python and sqlflask for computation and storage of data respectiely.

### Components of the project:
1. app.py:
- Hosts the website in the local server.
- Assigns layout for various webpages
- Creates and allocates memory for required storage elements.
- Assigns unique path for all pages.

2. experiment_answers.py:
- Contains the correct answers of each corpus of the experiment for cross checking if the users input are correct.

3. result_checker.py:
- Cross checks each answer of the user with the correct answers and returns number if correct answers and number of wrong answers.
- Chooses the corpus according to users input.

4. forms.py:
- Creates the forms used in the experiment and the quizzes.
- Integrates the formhelpers from WTForms.
5. templates/:
- Contains all the HTML files for the website
6. static/:
- Contains static resources for the website

### How To Setup The Database:
```
CREATE DATABASE ngrams;
USE ngrams;
CREATE TABLE qanda(id INT(11) AUTO_INCREMENT PRIMARY KEY, question VARCHAR(100), answer VARCHAR(30));
INSERT INTO qanda(question, answer) VALUES("What's the answer?", "answer");
INSERT INTO qanda(question, answer) VALUES("What's the solution?", "solution");
INSERT INTO qanda(question, answer) VALUES("What's the result?", "result");
INSERT INTO qanda(question, answer) VALUES("What's the conclusion?", "conclusion");
CREATE TABLE user_answers(id INT(11) AUTO_INCREMENT PRIMARY KEY, q1 varchar(100), q2 VARCHAR(100), q3 VARCHAR(100), q4 VARCHAR(100));
```

### How To Run The App
'''
git clone https://github.com/SiddarthVijay/N-Grams_Experiment.git
cd N-Grams_Experiment
python3 app.py
'''
