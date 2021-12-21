import unittest
from modules.FriendShips import FriendShips
from modules.FriendShipsDatabase import FriendShipsDatabase, WrongSignError, InvalidQueryError, InvalidActionError
from unittest.mock import MagicMock, patch

class Test_FriendShips(unittest.TestCase):
	def setUp(self):
		self.friendShipsDatabase = FriendShipsDatabase()
	
	def test_makeFriends_correct(self):
		with patch.object(FriendShips, "makeFriends", MagicMock(return_value=None)):
			self.assertTrue(self.friendShipsDatabase.run("MAKE FRIENDS: Adam, Eve"))
	
	def test_makeFriends_correct_if_called(self):
		with patch.object(FriendShips, "makeFriends", MagicMock(return_value=None)) as mock_FriendShips_makeFriends:
			self.friendShipsDatabase.run("MAKE FRIENDS: Adam, Eve")
			mock_FriendShips_makeFriends.assert_called_once_with("Adam", "Eve")
	
	def test_makeFriends_incorrect_too_many_persons(self):
		self.assertRaises(InvalidQueryError, self.friendShipsDatabase.run, "MAKE FRIENDS: Adam, Eve, Adam")

	def test_makeFriends_incorrect_wrong_sign(self):
		self.assertRaises(WrongSignError, self.friendShipsDatabase.run, "MAKE FRIENDS: Adam -> Eve")
	
	def test_invalidAction(self):
		self.assertRaises(InvalidActionError, self.friendShipsDatabase.run, "TEST: Adam, Eve")
	
	def test_areFriends_correct_true(self):
		with patch.object(FriendShips, "makeFriends", MagicMock(return_value=None)):
			self.friendShipsDatabase.run("MAKE FRIENDS: Adam, Eve")
			with patch.object(FriendShips, "areFriends", MagicMock(return_value=True)):
				self.assertTrue(self.friendShipsDatabase.run("ARE FRIENDS: Adam, Eve"))
	
	def test_areFriends_correct_false(self):
		with patch.object(FriendShips, "makeFriends", MagicMock(return_value=None)):
			self.friendShipsDatabase.run("MAKE FRIENDS: Adam, Noah")
			self.friendShipsDatabase.run("MAKE FRIENDS: Eve, Noah")
			with patch.object(FriendShips, "areFriends", MagicMock(return_value=False)):
				self.assertFalse(self.friendShipsDatabase.run("ARE FRIENDS: Adam, Eve"))


	def test_isFriend_correct_true(self):
		with patch.object(FriendShips, "addFriend", MagicMock(return_value=None)):
			self.friendShipsDatabase.run("ADD FRIEND: Adam -> Eve")
			with patch.object(FriendShips, "isFriend", MagicMock(return_value=True)):
				self.assertTrue(self.friendShipsDatabase.run("IS FRIEND: Adam -> Eve"))
	
	def test_isFriend_correct_false(self):
		with patch.object(FriendShips, "addFriend", MagicMock(return_value=None)):
			self.friendShipsDatabase.run("ADD FRIEND: Adam -> Eve")
			with patch.object(FriendShips, "isFriend", MagicMock(return_value=False)):
				self.assertFalse(self.friendShipsDatabase.run("IS FRIEND: Eve -> Adam"))
	
	def test_isFriend_incorrect_wrong_sign(self):
		self.assertRaises(WrongSignError, self.friendShipsDatabase.run, "IS FRIEND: Adam , Eve")

	def test_isFriend_keyError(self):
		with patch.object(FriendShips, "isFriend", MagicMock(side_effect=KeyError)):
			self.assertRaises(KeyError, self.friendShipsDatabase.run, "IS FRIEND: Adam -> Eve")
	
	def test_areFriends_keyError(self):
		with patch.object(FriendShips, "areFriends", MagicMock(side_effect=KeyError)):
			self.assertRaises(KeyError, self.friendShipsDatabase.run, "ARE FRIENDS: Adam, Eve")

	def test_isFriend_if_called(self):
		with patch.object(FriendShips, "isFriend", MagicMock(return_value=True)):
			self.friendShipsDatabase.run("IS FRIEND: Adam -> Eve")
			FriendShips.isFriend.assert_called_once_with("Adam", "Eve")
	
	def test_areFriends_if_called(self):
		with patch.object(FriendShips, "areFriends", MagicMock(return_value=True)):
			self.friendShipsDatabase.run("ARE FRIENDS: Adam, Eve")
			FriendShips.areFriends.assert_called_once_with("Adam", "Eve")
	
	def test_addFriend_if_called(self):
		with patch.object(FriendShips, "addFriend", MagicMock(return_value=None)):
			self.friendShipsDatabase.run("ADD FRIEND: Adam -> Eve")
			FriendShips.addFriend.assert_called_once_with("Adam", "Eve")
