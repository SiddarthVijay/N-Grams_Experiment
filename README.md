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
