from termcolor import cprint, colored
from pyfiglet import figlet_format
from os.path import splitext
from tabulate import tabulate
from firebase import firebase
from jsonschema import validate
from timer import AlarmException, alarmHandler, nonBlockingRawInput
from shutil import copy2
import os
import click
import json
import easygui

firebase = firebase.FirebaseApplication('https://python-ac720.firebaseio.com', None)


def init_screen():
    os.system("clear")
    cprint(figlet_format('QUIZZAPP', font='epic'),
           'red', attrs=['bold', 'blink'])

    print("Use the following Commands\n")
    commands = [
        ["remote_quizes", "", "List quizes on remore server"],
        ["quiz_list", "", "list of quizes on local library"],
        ["quiz_import", "<path to quizz file>", "Import quiz from file"],
        ["quiz_take", "<quiz name>", "Take a quiz"], ["download_quiz",
                                                      "<quiz name>", "Download quiz from remore repo"],
        ["upload_quizz ", "<quiz_name>", "Upload quiz to remote repo"]]

    print(tabulate(
        commands, headers=["Command", "Arguments", "Description"], tablefmt="psql"))


def list_quizz_files():
    """
    List all the quizzes in your library i.e json directory
    """
    click.echo(click.style("List of Available Quizzes",
                           fg="green", reverse=True))
    try:
        if os.listdir("json/") != []:
            for file in os.listdir("json/"):
                if file.endswith(".json"):
                    file_object = open("json/" + file)
                    click.echo(
                        click.style("> " + splitext(file)[0], fg="white"))
                else:
                    return "No json"
        else:
            print("No Quizzes")
            return "No Quizz Files"
    except OSError, e:
        print e


def take_quiz(quiz_name):
    with open('json/' + quiz_name + '.json') as quiz_file:
        data = json.load(quiz_file)
        answers = []
        for q, det in data.iteritems():
            init_screen()
            correct_ans = det['ans'].lower()
            ans = nonBlockingRawInput(det['choices'], det['question'], det['time'])
            if ans.lower().strip() not in ['a', 'b', 'c', 'd']:
                answers.append("0")
            else:
                if correct_ans == ans.lower().strip():
                    answers.append(ans.lower().strip())
                else:
                    answers.append("x")
            
            correct = 0
            total = len(answers)
            for x in answers:
                if x not in ['0','x']:
                    correct += 1
            results = [["Total questions", total],["Correct Answers", correct]]
            print("\n")
            print(tabulate(results, tablefmt = "fancy_grid"))



def download_quiz(quiz_name):
    result = firebase.get('/'+ quiz_name, None)
    try:
        with open('json/'+ quiz_name +'.json', 'w') as outfile:
            json.dump(result, outfile)
    except:
        print("Error Occurred Importing Quiz")

def list_remote_quizzes():
    result = firebase.get('/', None)
    for question in result.keys():
        print(question)

schema = {
    "type" : "object",
    "properties": {
        "question" : { "type" : "string"},
        "choices" : {  "type" : "object",
                        "properties": {
                            "A" : {"type" : "string"},
                            "B" : {"type" : "string"},
                            "C" : {"type" : "string"},
                            "D" : {"type" : "string"}
                        }
                    },
        "ans" : { "type" : "string" },
        "time" : { "type" : "number" }
    },
    "additionalProperties" : False,
    "required" : ['question', "choices", "ans", "time"]
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



    
