from __future__ import annotations

class Note:
	def __init__(self, name: str, note: float) -> None:
		self.name = name
		self.note = note
	def __str__(self) -> str:
		return f"""Note(name = "{self.__name}", note = {self.__note})"""
	def __repr__(self) -> str:
		return f"""Note(name = "{self.__name}", note = {self.__note})"""
	def __eq__(self, other: Note) -> bool:
		return self.__name == other.name and self.__note == other.note
	def __ne__(self, other: Note) -> bool:
		return self.__name != other.name or self.__note != other.note

	@property
	def name(self) -> str:
		return self.__name
	@property
	def note(self) -> float:
		return self.__note
	@note.setter
	def note(self, note: float) -> None:
		try:
			if note < 2 or note > 6:
				raise ValueError("Note should be between 2 and 6")
		except TypeError:
			raise TypeError("Note should be a float")

		self.__note = note
	@name.setter
	def name(self, name: str) -> None:
		if name is None:
			raise ValueError("Name cannot be None")
		try:
			if len(name) == 0:
				raise ValueError("Name cannot be empty")
		except TypeError:
			raise TypeError("Name should be a string")
		self.__name = name
	
	def __hash__(self) -> int:
		return hash(self.__name) + hash(self.__note)