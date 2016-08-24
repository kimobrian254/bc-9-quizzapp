from termcolor import cprint, colored
from pyfiglet import figlet_format
from os.path import basename
from tabulate import tabulate
import sys, os, click, time
from colorama import init
init(strip=not sys.stdout.isatty())


class Actions(object):

    def __init__(self):
        self.quizzlist = []

    def init_screen(self):
        os.system("clear")
        cprint(figlet_format('QUIZZAPP', font='epic'),
               'red', attrs=['bold', 'blink'])

        move=["/","|","\\","-",""]
        text = "Use the following commands"
        for char in text:
        	time.sleep(0.2)
        	sys.stderr.write(char)
        print("\n")
        commands = [
        	["remote_quizes", "", "List quizes on remore server"],
        	["quiz_list", "", "list of quizes on local library"],
        	["quiz_import", "<path to quizz file>",	"Import quiz from file"],
        	["quiz_take", "<quiz name>", "Take a quiz"], ["download_quiz", 
        	"<quiz name>", "Download quiz from remore repo"], 
        	["upload_quizz ", "<quiz_name>", "Upload quiz to remote repo"]]

        print(tabulate(commands, headers = ["Command", "Arguments", "Description"], tablefmt = "psql"))

