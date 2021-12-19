import unittest
import unittest.mock
from modules.CharacterCounter import CharacterCounter


class Test_CharacterCounter(unittest.TestCase):
	def test_constructor(self):
		characterCounter = CharacterCounter()
		self.assertEqual(characterCounter.get(), {})
	
	def test_addLine_abc(self):
		characterCounter = CharacterCounter()
		characterCounter.addLine("abc")
		self.assertEqual(characterCounter.get(), {"a": 1, "b": 1, "c": 1})

	def test_addLine_abnsdnaaa(self):
		characterCounter = CharacterCounter()
		characterCounter.addLine("abnsdnaaa")
		self.assertEqual(characterCounter.get(), {"a": 4, "s": 1, "b": 1, "d": 1, "n": 2})

	def test_saveToString_aafs(self):
		characterCounter = CharacterCounter()
		characterCounter.addLine("aafs")
		self.assertEqual(characterCounter.saveToString(), "a2\nf1\ns1\n")
	
	def test_loadFromString_aafs(self):
		characterCounter = CharacterCounter()
		characterCounter.loadFromString("a2\nf1\ns1\n")
		self.assertEqual(characterCounter.get(), {"a": 2, "f": 1, "s": 1})
	

	def test_saveToFile_with_content_aafs(self):
		characterCounter = CharacterCounter()
		characterCounter.addLine("aafs")
		with unittest.mock.patch("builtins.open") as mockOpen:
			characterCounter.saveToFile("./test.txt")
		mockOpen.assert_called_once_with("./test.txt", "w")

	def test_loadFromFile_with_content_aafs(self):
		characterCounter = CharacterCounter()
		with unittest.mock.patch("builtins.open", unittest.mock.mock_open(read_data="a2\nf1\ns1\n")) as mockOpen:
			characterCounter.loadFromFile("./test.txt")
		mockOpen.assert_called_once_with("./test.txt", "r")

	def test_loadFromFile_effect_with_content_aafs(self):
		characterCounter = CharacterCounter()
		with unittest.mock.patch("builtins.open", unittest.mock.mock_open(read_data="a2\nf1\ns1\n")) as mockOpen:
			characterCounter.loadFromFile("./test.txt")
		self.assertEqual(characterCounter.get(), {"a": 2, "f": 1, "s": 1})
	
	def test_loadFromWith_with_incorrect_content(self):
		characterCounter = CharacterCounter()
		with unittest.mock.patch("builtins.open", unittest.mock.mock_open(read_data="a2f1\ns1\n")):
			with self.assertRaises(ValueError):
				characterCounter.loadFromFile("./test.txt")
	
	def test_log_with_content_aafs_nddw(self):
		characterCounter = CharacterCounter(doLog=True)
		with unittest.mock.patch("builtins.open") as mockOpen:
			characterCounter.addLine("aa s")
			characterCounter.addLine("nddw")
		self.assertEqual(
			mockOpen.return_value.__enter__.return_value.write.call_args_list,
			[
				unittest.mock.call("a"),
				unittest.mock.call("a"),
				unittest.mock.call(" "),
				unittest.mock.call("s"),
				unittest.mock.call("n"),
				unittest.mock.call("d"),
				unittest.mock.call("d"),
				unittest.mock.call("w"),
			]
		)

	def test_if_constructor_checks_old_logs_existence(self):
		with unittest.mock.patch("os.path.exists") as mockOsPathExists:
			mockOsPathExists.return_value = False
			CharacterCounter(doLog=True)
		mockOsPathExists.assert_called_once_with("./log.txt")
	
	def test_if_constructor_removes_old_logs(self):
		with unittest.mock.patch("os.remove") as mockOsRemove:
			with unittest.mock.patch("os.path.exists") as mockOsPathExists:
				mockOsPathExists.return_value = True
				CharacterCounter(doLog=True)
		mockOsRemove.assert_called_once_with("./log.txt")