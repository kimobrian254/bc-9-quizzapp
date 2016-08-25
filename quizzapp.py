from termcolor import colored, cprint
from pyfiglet import figlet_format
import quizzactions
import click, os
import cmd
import easygui


class Quizz(cmd.Cmd):

    intro = quizzactions.init_screen()
    prompt = "quiz@quizzapp>>>"

    def do_quiz_list(self, arg):
        """
        List the names of quizzes
        quiz_list
        """
        pass

    def do_remote_quizes(self, arg):
        """
        List quizes in the remore server
        remote_quizes
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
        pass

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
        print colored("Invalid Command", "red")


if __name__ == "__main__":
    try:
        Quizz().cmdloop()
    except KeyboardInterrupt:
        os.system("clear")
        cprint(figlet_format('Logged Out QuizzApp', font='digital'),
               'red', attrs=['bold', 'blink'])
