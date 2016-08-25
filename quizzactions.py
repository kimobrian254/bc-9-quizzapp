from termcolor import cprint, colored
from pyfiglet import figlet_format
from os.path import splitext
from tabulate import tabulate
from firebase import firebase
from jsonschema import validate
from timer import AlarmException, alarmHandler, nonBlockingRawInput
from shutil import copy2
import os
import random
import click
import json
import easygui
import urllib
import time
import sys

firebase = firebase.FirebaseApplication(
    'https://python-ac720.firebaseio.com', None)


def init_screen():
    os.system("clear")
    cprint(figlet_format('\tQUIZZAPP', font='epic'),
           'red', attrs=['bold', 'blink'])

    print colored("\t\tUse the following Commands\n", "white")
    commands = [
        ["show_remote_quizzes", "", "List quizes on remore server"],
        ["quiz_list", "", "list of quizes on local library"],
        ["quiz_import", "<path to quizz file>", "Import quiz from file"],
        ["quiz_take", "<quiz name>", "Take a quiz"], ["download_quiz",
                                                      "<quiz name>", "Download quiz from remore repo"],
        ["upload_quizz ", "<quiz_name>", "Upload quiz to remote repo"],
        ["easy_import", "", "Simpler file selector to Import File"],
        ["logout", "", "Exit QuizzApp"]
    ]

    print colored(tabulate(commands, headers=["Command", "Arguments", "Description"], tablefmt="psql"), "green")
    print colored("\n\t\tEnter help <command name> to get help\n", "yellow")
    delay_print("\tThe Quizz App Allows a user to view quizzes stored both locally and remotely,"
                "\n\tupload local quizzes to remote host, download from remote to local and and"
                " \n\ttake quizzes and get graded.")
    print("\n")


def delay_print(s):
    for c in s:
        sys.stdout.write('%s' % c)
        sys.stdout.flush()
        time.sleep(0.1)


def list_quizz_files():
    """
    List all the quizzes in your library i.e json directory
    """
    click.echo(click.style("\tList of Locally Available Quizzes",
                           fg="blue", underline=True))

    if os.listdir("json/") != []:
        for file in os.listdir("json/"):
            if file.endswith(".json"):
                file_object = open("json/" + file)
                print colored("\t\t* " + splitext(file)[0], "white")
            else:
                return "No json"
    else:
        print("No Quizzes")
        return "No Quizz Files"


def randomize_quizes(quiz_name):
    """
    Present random quizzes to prevent prediction
    """
    quizlist = []
    with open('json/' + quiz_name + '.json') as quiz_file:
        data = json.load(quiz_file)
    randomqs = random.sample(data, 5)
    for key in randomqs:
        quizlist.append(data[key])
    return quizlist


def take_quiz(quiz_name):
    quizes = randomize_quizes(quiz_name)
    query_stats = dict()
    answers = []
    for quiz in quizes:
        init_screen()
        correct_ans = quiz['answer'].strip().lower()
        ans = nonBlockingRawInput(quiz['choices'], quiz[
                                  'question'], quiz['time'])
        answer = ans.lower().strip()
        if answer in ['a', 'b', 'c', 'd']:
            if answer == correct_ans:
                answers.append(answer)
            else:
                answers.append("x")
        elif len(answer) > 0 and answer != "timeout":
            answers.append("i")  # Invalid Choice
        else:
            answers.append('timeout')
    result = []
    timed_out = len([x for x in answers if x == "timeout"])
    wrong = len([x for x in answers if x == "x"])
    invalid = len([x for x in answers if x == "i"])
    correct = len(quizes) - (timed_out + wrong + invalid)
    result.append(timed_out)  # Timed out answers
    result.append(wrong)  # Wrong answers
    result.append(invalid)  # Invalid
    result.append(correct)  # Correct
    total_questions = len(quizes)  # Total questions
    results = [["Timed Out Questions", result[0]], ["Wrong Score", result[1]], ["Invalid Answers", result[2]], [
        "Total Questions", str(total_questions)], ["Correct Score", str(result[3]) + "/" + str(total_questions)]]
    print("\n")
    click.echo(click.style(tabulate(results, tablefmt="fancy_grid"), fg="green"))


def download_quiz(quiz_name):
    result = firebase.get('/' + quiz_name, None)
    if result == None:
        print colored("No results from remote DB", "red")
    try:
        with open('json/' + quiz_name + '.json', 'w') as outfile:
            json.dump(result, outfile)
    except:
        print("Error Occurred Importing Quiz")

schema = {
    "type": "object",
    "properties": {
        "question": {"type": "string"},
        "choices": {"type": "object",
                    "properties": {
                        "A": {"type": "string"},
                        "B": {"type": "string"},
                            "C": {"type": "string"},
                            "D": {"type": "string"}
                    }
                    },
        "ans": {"type": "string"},
        "time": {"type": "number"}
    },
    "additionalProperties": False,
    "required": ['question', "choices", "ans", "time"]
}


def validate_json(instance, schema):
    try:
        validate(instance, schema)
        return "Valid JSON Format"
    except Exception, e:
        return "Invalid JSON Format"


def import_quiz(quiz_path):
    if not os.path.isfile(quiz_path):
        print colored("File {0} Not found".format(quiz_path), "red")
        return "Invalid Path"
    if not quiz_path.endswith(".json"):
        print colored("The File {0} is not a JSON file".format(quiz_path), "red")
        return "Not A JSON File"
    with open(quiz_path) as quiz_file:
        try:
            data = json.load(quiz_file)
            for key, val in data.items():
                validation = validate_json(val, schema)
                if validation == "Invalid JSON Format":
                    return validation
            copy2(quiz_path, "json")
            print colored("Quizz File {0} Imported".format(quiz_path), "green")
        except ValueError, e:
            return "Invalid JSON"


def list_remote_quizzes():
    data = firebase.get("/", None)
    click.echo(click.style('\tList of Online Questions',
                           fg='green', underline="=", bold=True))
    for key, val in data.iteritems():
        click.echo(click.style("\t\t* " + key, fg="green"))
    click.echo(click.style(
        "\t\t<Download the querries to access them>", fg="yellow"))


def upload_quiz(quiz_name):
    try:
        with open('json/' + quiz_name + '.json', 'r') as infile:
            try:
                data = json.load(infile)
            except ValueError:
                print("Invalid JSON data")
            x = firebase.post('/math', data)
    except IOError, e:
        raise
