from termcolor import colored
import click
import cmd
from quizzactions import Actions


class Quizz(cmd.Cmd):

    action = Actions()
    intro = action.init_screen()
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

    def do_EOF(self, line):
        return True


if __name__ == "__main__":
	try:
		Quizz().cmdloop()
	except:
		pass
