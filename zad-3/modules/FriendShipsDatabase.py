from modules.FriendShips import FriendShips
import re

class InvalidQueryError(ValueError):
	pass

class InvalidActionError(ValueError):
	pass

class WrongSignError(InvalidQueryError):
	pass

class FriendShipsDatabase:
	__queryRegex = re.compile(r"^\s*(?P<action>\w+(\s+\w+)*)\s*:\s*(?P<person1>\w+)\s*(?P<sign>,|(->))\s*(?P<person2>\w+)\s*$")

	def __init__(self):
		self.friendShips = FriendShips()

	def __makeFriends(self, person1, person2):
		self.friendShips.makeFriends(person1, person2)
		return True

	def __areFriends(self, person1, person2):
		return self.friendShips.areFriends(person1, person2)

	def __isFriend(self, person, targetPerson):
		return self.friendShips.isFriend(person, targetPerson)

	def __addFriend(self, person, targetPerson):
		self.friendShips.addFriend(person, targetPerson)
		return True

	def run(self, query: str):
		matchResult = FriendShipsDatabase.__queryRegex.match(query)
		if matchResult is None:
			raise InvalidQueryError(f"Invalid query: {query}")
		action = " ".join([word.lower() for word in matchResult.group("action").split()])
		resolverByAction = {
			"make friends": self.__makeFriends,
			"are friends": self.__areFriends,
			"is friend": self.__isFriend,
			"add friend": self.__addFriend,
		}
		if action not in resolverByAction:
			raise InvalidActionError(f"Invalid action: {action}")
		sign = matchResult.group("sign")
		requiredSignByAction = {
			"make friends": ",",
			"are friends": ",",
			"is friend": "->",
			"add friend": "->",
		}
		if sign != requiredSignByAction[action]:
			raise WrongSignError(f"Invalid sign in query: {query}")

		person1 = matchResult.group("person1")
		person2 = matchResult.group("person2")
		return resolverByAction[action](person1, person2)
