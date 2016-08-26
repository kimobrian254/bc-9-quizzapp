from termcolor import colored, cprint
from pyfiglet import figlet_format
import quizzactions
import os
import sys
import cmd
import easygui
import warnings

warnings.filterwarnings("ignore")


class Quizz(cmd.Cmd):

    intro = quizzactions.init_screen()
    prompt = "quiz@quizzapp>>>"

    def do_quiz_list(self, arg):
        """
        List the names of quizzes
        quiz_list
        """
        if arg:
            print colored("This command does not take arguments", "red")
        else:
            quizzactions.list_quizz_files()

    def do_show_remote_quizzes(self, arg):
        """
                List quizes in the remote server
                remote_quizes
        """
        if arg:
            print colored("This command does not take arguments", "red")
        else:
            quizzactions.list_remote_quizzes()

    def do_easy_import(self, arg):
        """
        Easier way to select files
        """
        if arg:
            print colored("This command does not take arguments", "red")
        else:
            file_path = easygui.fileopenbox()
            if file_path:
                quizzactions.import_quiz(file_path)

    def do_logout(self, arg):
        """
        Exit from quizzapp console application
        """
        if arg:
            print colored("This command does not take arguments", "red")
        else:
            cprint(figlet_format('Logging Out QuizzApp', font='ogre'),
                   'red', attrs=['bold', 'blink'])
            sys.exit()

    def do_download_quiz(self, quiz_name):
        """
                Downloads specified quiz from remote server
                download_quiz <quiz name>
        """
        if not quiz_name:
            print colored("The Command Requires a Single Argument", "yellow")
        else:
            quizzactions.download_quiz(quiz_name)

    def do_upload_quiz(self, quiz_name):
        """
                Uploads apecified quiz to remote server
                upload_quiz <quiz name>
        """
        if not quiz_name:
            print colored("Commmand ", "red")
        else:
            quizzactions.upload_quiz(quiz_name)

    def do_quiz_import(self, quiz_path):
        """
                Import a new quiz from a json file
                quiz_import <quiz name>
        """
        quizzactions.import_quiz(quiz_path)

    def do_quiz_take(self, quiz):
        """
                Take the specified quiz
                quiz_take <quiz name>
        """
        if not quiz:
            print colored("The command requires <quiz name> argument", "yellow")
            return
        try:
            answers = quizzactions.take_quiz(quiz)
        except ValueError:
            print colored("The sample is larger than the poulation", "yellow")
        except Exception, e:
            print(e)
            print colored("\t\tNot Enough Questions in the Quizz", "yellow")

    def default(self, args):
        """
        Handles invalid commands
        """
        print colored("Invalid Command or Command Format", "red")


if __name__ == "__main__":
    try:
        Quizz().cmdloop()
    except KeyboardInterrupt:
        os.system("clear")
        cprint(figlet_format('Logged Out QuizzApp', font='digital'),
               'red', attrs=['bold', 'blink'])
