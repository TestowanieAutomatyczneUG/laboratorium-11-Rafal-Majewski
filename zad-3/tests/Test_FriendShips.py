import unittest
from modules.FriendShips import FriendShips


class Test_FriendShips(unittest.TestCase):
	def setUp(self):
		self.friendShips = FriendShips()

	def test_makeFriends_true_new_both_source_to_target(self):
		self.friendShips.makeFriends("Adam", "Eve")
		self.assertTrue(self.friendShips.isFriend("Adam", "Eve"))
	
	def test_makeFriends_true_new_both(self):
		self.friendShips.makeFriends("Adam", "Eve")
		self.assertTrue(self.friendShips.areFriends("Adam", "Eve"))

	def test_makeFriends_true_new_both_target_to_source(self):
		self.friendShips.makeFriends("Adam", "Eve")
		self.assertTrue(self.friendShips.isFriend("Eve", "Adam"))

	def test_makeFriends_true_target_to_source(self):
		self.friendShips.makeFriends("Adam", "Noah")
		self.friendShips.makeFriends("Noah", "Eve")
		self.friendShips.makeFriends("Adam", "Eve")
		self.assertTrue(self.friendShips.isFriend("Adam", "Eve"))

	def test_makeFriends_true(self):
		self.friendShips.makeFriends("Adam", "Noah")
		self.friendShips.makeFriends("Noah", "Eve")
		self.friendShips.makeFriends("Adam", "Eve")
		self.assertTrue(self.friendShips.areFriends("Adam", "Eve"))
	
	def test_makeFriends_true_source_to_target(self):
		self.friendShips.makeFriends("Adam", "Noah")
		self.friendShips.makeFriends("Noah", "Eve")
		self.friendShips.makeFriends("Adam", "Eve")
		self.assertTrue(self.friendShips.isFriend("Eve", "Adam"))

	def test_makeFriends_false_target_to_source(self):
		self.friendShips.makeFriends("Adam", "Noah")
		self.friendShips.makeFriends("Noah", "Eve")
		self.friendShips.makeFriends("Eve", "Sam")
		self.assertFalse(self.friendShips.isFriend("Adam", "Eve"))
	
	def test_makeFriends_false(self):
		self.friendShips.makeFriends("Adam", "Noah")
		self.friendShips.makeFriends("Noah", "Eve")
		self.friendShips.makeFriends("Eve", "Sam")
		self.assertFalse(self.friendShips.areFriends("Adam", "Eve"))

	
	def test_makeFriends_false_source_to_target(self):
		self.friendShips.makeFriends("Adam", "Noah")
		self.friendShips.makeFriends("Noah", "Eve")
		self.assertFalse(self.friendShips.isFriend("Eve", "Adam"))
	
	def test_addFriend_true_new_both_source_to_target(self):
		self.friendShips.addFriend("Adam", "Eve")
		self.assertTrue(self.friendShips.isFriend("Adam", "Eve"))
	
	def test_addFriend_false_new_both_target_to_source(self):
		self.friendShips.addFriend("Adam", "Eve")
		self.assertFalse(self.friendShips.isFriend("Eve", "Adam"))
	
	def test_isFriend_keyError(self):
		self.assertRaises(KeyError, self.friendShips.isFriend, "Adam", "Eve")
	
	def test_areFriends_keyError(self):
		self.assertRaises(KeyError, self.friendShips.areFriends, "Adam", "Eve")
	
	