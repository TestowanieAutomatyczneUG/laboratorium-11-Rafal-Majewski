from modules.Note import Note
from modules.NotesStorage import NotesStorage

class NotesService:
	def __init__(self) -> None:
		self.notesStorage = NotesStorage()
	def add(self, note: Note) -> Note:
		return self.notesStorage.add(note)
	def averageOf(self, name: str) -> float:
		targetNotes = self.notesStorage.getAllNotesOf(name)
		if len(targetNotes) == 0:
			return None
		notesSum = 0
		for note in targetNotes:
			notesSum += note.note
		return notesSum / len(targetNotes)
	def clear(self) -> None:
		return self.notesStorage.clear()