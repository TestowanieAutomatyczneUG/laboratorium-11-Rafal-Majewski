class FriendShips:
	def __init__(self):
		self.__friendsByPerson = {}
	def __insertPersonIfNotExists(self, person: str):
		if person not in self.__friendsByPerson:
			self.__friendsByPerson[person] = set()
	def makeFriends(self, person1: str, person2: str):
		self.__insertPersonIfNotExists(person1)
		self.__insertPersonIfNotExists(person2)
		self.__friendsByPerson[person1].add(person2)
		self.__friendsByPerson[person2].add(person1)
	def areFriends(self, person1: str, person2: str):
		# return person1 in self.__friendsByPerson and person2 in self.__friendsByPerson and person1 in self.__friendsByPerson[person2] and person2 in self.__friendsByPerson[person1]
		return person1 in self.__friendsByPerson[person2] and person2 in self.__friendsByPerson[person1]
	def isFriend(self, person: str, targetPerson: str):
		# return person in self.__friendsByPerson and targetPerson in self.__friendsByPerson[person]
		return targetPerson in self.__friendsByPerson[person]
	def addFriend(self, person: str, targetPerson: str):
		self.__insertPersonIfNotExists(person)
		self.__insertPersonIfNotExists(targetPerson)
		self.__friendsByPerson[person].add(targetPerson)
