# quizzapp

### Introduction
Quizzapp is a console application that enables a user to do the following:
* List all quizzes in the users library
*  Import a new quizz from a JSON file and the quizz 
should contain the actual question, multiple choices and the correct answer.
* A user gets a score based on the answer they issue to a question
* A user can be timed when taking a question
* Use an online repo of quizzes where he can upload and download quizzes

The Quizzapp application has the following benefitting features
* Every question is timed and the next question autmatically appears on time out
* The application choses random questions making is less unpredictable and more fun
* With the use of the JSON files, validation of the JSON files and the structure of the content ensures only well structured questions are imported.
* ```easy_import``` command easiens path identification by allowing user to select path

## Installation and Use
*	Create a virtual Environment on your local machine with ```virtualenv env```
*	Switch into the virtual environment with ``` cd env``` and activate with ```. bin/activate```
* Clone the repo with ```git clone https://github.com/Kimokoti/bc-9-quizzapp```
*	Switch into the project directory with ```cd bc-9-quizzapp```
* Install the requirement packages with ```pip install -r requirements.txt```
* Run the project with ```python quizzapp.py```

The project presents a console with instructions on how to use it.

