from termcolor import colored, cprint
from pyfiglet import figlet_format
import quizzactions
from timer import AlarmException, alarmHandler, nonBlockingRawInput
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
        quizzactions.list_quizz_files()

    def do_remote_quizes(self, arg):
    	"""
		List quizes in the remore server
		remote_quizes
    	"""
    	pass

    def do_download_quiz(self, quiz):
    	"""
		Downloads specified quiz from remote server
		download_quiz <quiz name>
    	"""
    	pass

    def do_upload_quiz(self, quiz):
    	"""
		Uploads apecified quiz to remote server
		upload_quiz <quiz name>
    	"""
    	pass

    def do_quiz_import(self, quiz):
    	"""
		Import a new quiz from a json file
		quiz_import <quiz name>
    	"""
    	# pass
        path = easygui.fileopenbox()
        print(path)

    def do_quiz_take(self, quiz):
    	"""
		Take the specified quiz
		quiz_take <quiz name>
    	"""
        try:
    	   answers = quizzactions.take_quiz(quiz)
        except:
            print colored("The command requires <quiz name> argument", "green")
    	

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
