import unittest
import shadowd.connector

class TestConnector(unittest.TestCase):
	def test_escape_key(self):
		input = shadowd.connector.Input()

		self.assertEqual(input.escape_key('foo'), 'foo')
		self.assertEqual(input.escape_key('foo|bar'), 'foo\\|bar')
		self.assertEqual(input.escape_key('foo\\|bar'), 'foo\\\\\\|bar')
		self.assertEqual(input.escape_key('foo||bar'), 'foo\\|\\|bar')
		self.assertEqual(input.escape_key('foo\\\\bar'), 'foo\\\\\\\\bar')

	def test_unescape_key(self):
		input = shadowd.connector.Input()

		self.assertEqual(input.unescape_key('foo'), 'foo')
		self.assertEqual(input.unescape_key('foo\\|bar'), 'foo|bar')
		self.assertEqual(input.unescape_key('foo\\\\bar'), 'foo\\bar')
		self.assertEqual(input.unescape_key('foo\\\\\\|bar'), 'foo\\|bar')

	def test_split_path(self):
		input = shadowd.connector.Input()

		test1 = input.split_path('foo')
		self.assertEqual(len(test1), 1)
		self.assertEqual(test1[0], 'foo')

		test2 = input.split_path('foo|bar')
		self.assertEqual(len(test2), 2)
		self.assertEqual(test2[0], 'foo')
		self.assertEqual(test2[1], 'bar')

		test3 = input.split_path('foo\\|bar')
		self.assertEqual(len(test3), 1)
		self.assertEqual(test3[0], 'foo\\|bar')

		test4 = input.split_path('foo\\\\|bar')
		self.assertEqual(len(test4), 2)
		self.assertEqual(test4[0], 'foo\\\\')
		self.assertEqual(test4[1], 'bar')

		test5 = input.split_path('foo\\\\\\|bar')
		self.assertEqual(len(test5), 1)
		self.assertEqual(test5[0], 'foo\\\\\\|bar')

		test6 = input.split_path('foo\\')
		self.assertEqual(len(test6), 1)
		self.assertEqual(test6[0], 'foo\\')