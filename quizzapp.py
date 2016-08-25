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
        pass

    def do_show_remote_quizzes(self, arg):
        """
                List quizes in the remote server
                remote_quizes
        """
        pass

    def do_easy_import(self, arg):
        """
        Easier way to select files
        """
        pass

    def do_elogout(self, arg):
        """
        Exit from quizzapp console application
        """
        pass

    def do_download_quiz(self, quiz_name):
        """
                Downloads specified quiz from remote server
                download_quiz <quiz name>
        """
        pass

    def do_upload_quiz(self, quiz_name):
        """
                Uploads apecified quiz to remote server
                upload_quiz <quiz name>
        """
        pass

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
        pass

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
