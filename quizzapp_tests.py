import unittest
import quizzactions
import warnings

warnings.filterwarnings("ignore")


class TestQuizzApp(unittest.TestCase):
	"""
	Testing functionality of different quizzapp functions
	"""
	
	def test_take_quiz(self):
		"""
		Test case if return type is 'list'
		"""
		self.assertIs(quizzactions.take_quiz("sports"), list, msg="Return type not a list")

	def test_take_quiz2(self):
		"""
		Test case if quizz does not Exist. Exception is Raised
		"""
		with self.assertRaises(Exception):
			quizzactions.take_quiz("sportshh")

	def test_download_quiz(self):
		"""
		Test if the quizz is not on the remote repo
		"""
		self.assertEqual(quizzactions.download_quiz("gfgggf"), False, msg="The Quizz is Available on the Remote Repo")

	def test_quizz_validation(self):
		"""
		Testing valid JSON data
		"""
		json_data = {
    		"question": "Who was the second president of Kenya",
		    "choices": {
		        "A": "Me",
		        "B": "You",
		        "C": "Him",
		        "D": "Her"
		    },
		    "answer": "C",
		    "time": 5
		}


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
		        "answer": {"type": "string"},
		        "time": {"type": "number"}
		    },
		    "additionalProperties": False,
		    "required": ['question', "choices", "answer", "time"]
		}
		self.assertEqual(quizzactions.validate_json(json_data, schema), "Valid JSON Format", msg="Invalid JSON format")


	def test_quizz_validation2(self):
		"""
		Tests for wrong JSON format quizz
		"""
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
		        "answer": {"type": "string"},
		        "time": {"type": "number"}
		    },
		    "additionalProperties": False,
		    "required": ['question', "choices", "answer", "time"]
		}

		wrong_data = {
		    "question": "hgjgf",
		    "choices": {
		        "A": "jjfg",
		        "B": "dhjkfd"
		    }
		}

		self.assertEqual(quizzactions.validate_json(wrong_data, schema), "Invalid JSON Format", msg="Invalid JSON format")

	def test_import_quiz(self):
		"""
		Test for importing a file that does not exist
		"""
		self.assertEqual(quizzactions.import_quiz("json.txt"),"Invalid Path", "The file Exists")

	def test_import_quiz2(self):
		"""
		Test for importing a file that is not *.json
		"""
		self.assertEqual(quizzactions.import_quiz("invalid.txt"),"Not A JSON File", "The file is a JSON File")

	def test_import_quiz3(self):
		"""
		Test for importing a file that is *.json but wrong format
		"""
		self.assertEqual(quizzactions.import_quiz("invalid.json"),"Invalid JSON Format", "The file is a valid Quizz File")


if __name__ == "__main__":
	unittest.main()