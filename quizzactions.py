from termcolor import cprint, colored
from pyfiglet import figlet_format
from os.path import basename, splitext
from tabulate import tabulate
from timer import nonBlockingRawInput, AlarmException, alarmHandler
import sys
import os
import click
import time
import json
from colorama import init


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


