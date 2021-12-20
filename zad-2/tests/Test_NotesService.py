import unittest
from modules.NotesStorage import NotesStorage
from modules.NotesService import NotesService
from modules.Note import Note
from unittest.mock import MagicMock, patch


class Test_NotesService(unittest.TestCase):
	def test_add_returning_added_note(self,):
		note = Note("test", 3)
		with patch.object(NotesStorage, "add", MagicMock(return_value=note)):
			notesService = NotesService()
			addedNote = notesService.add(note)
			self.assertIs(addedNote, note)
	def test_averageOf(self):
		allNotes = set([Note("test", 3), Note("test", 4)])
		with patch.object(NotesStorage, "getAllNotesOf", MagicMock(return_value=allNotes)):
			notesService = NotesService()
			self.assertAlmostEqual(notesService.averageOf("test"), 3.5)
	def test_averageOf_with_no_notes(self):
		with patch.object(NotesStorage, "getAllNotesOf", MagicMock(return_value=set())):
			notesService = NotesService()
			self.assertIsNone(notesService.averageOf("test"))
	def test_clear_return_value(self):
		with patch.object(NotesStorage, "clear", MagicMock(return_value=None)):
			notesService = NotesService()
			notesService.clear()
			self.assertIsNone(notesService.clear())
	def test_clear_is_called(self):
		with patch.object(NotesStorage, "clear", MagicMock(return_value=None)) as mockNotesStorageClear:
			notesService = NotesService()
			notesService.clear()
			mockNotesStorageClear.assert_called_once_with()