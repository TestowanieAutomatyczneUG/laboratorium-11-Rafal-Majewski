from typing import Iterable
import os


class CharacterCounter:
	def __init__(self, doLog=False) -> None:
		self.__countByCharacter = {}
		self.__doLog = doLog
		self.removeLogs()
	def removeLogs(self) -> None:
		if self.__doLog and os.path.exists("./log.txt"):
			os.remove("./log.txt")
	def _addLine(self, line: str) -> None:
		for character in line:
			if self.__doLog:
				with open("./log.txt", "a") as file:
					file.write(character)
			if character not in self.__countByCharacter:
				self.__countByCharacter[character] = 0
			self.__countByCharacter[character] += 1
	def addLine(self, line: str) -> None:
		if not isinstance(line, str):
			raise TypeError("Line must be a string")
		self._addLine(line)
	def addLines(self, lines: Iterable[str]) -> None:
		if not isinstance(lines, Iterable):
			raise TypeError("Lines must be iterable")
		for line in lines:
			if not isinstance(line, str):
				raise TypeError("All lines must be a string")
		for line in lines:
			self._addLine(line)
	def get(self) -> dict:
		return self.__countByCharacter.copy()
	def __str__(self) -> str:
		return str(self.__countByCharacter)
	def __repr__(self) -> str:
		return str(self.__countByCharacter)
	def addLinesFromFile(self, filepath: str) -> None:
		with open(filepath, "r") as file:
			for line in file:
				self._addLine(line)
	def loadFromString(self, string: str) -> None:
		entries = []
		for line in string.splitlines():
			head, *tail = line
			entries.append((head, int("".join(tail))))
		self.__countByCharacter = dict(entries)
	def loadFromFile(self, filepath: str) -> None:
		with open(filepath, "r") as file:
			self.loadFromString(file.read())
	def saveToString(self) -> str:
		return "".join([f"{character}{characterCount}\n" for character, characterCount in sorted(self.__countByCharacter.items())])
	def saveToFile(self, filepath: str) -> None:
		with open(filepath, "w") as file:
			file.write(self.saveToString())
			