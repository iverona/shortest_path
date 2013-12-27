import unittest
from ShortestPath import ShortestPath
from file_reader import InputFileReader
from my_exceptions import DestNotFoundException, SourceNotFoundException

class TestShortestPath(unittest.TestCase):

	def setUp(self):
		self.net = {
					'A': {'C':1, 'B':3},
			        'B': {'D':1, 'G':5},
			        'C': {'F':5, 'D':2},
			        'D': {'F':2, 'E':4}, 
			        'E': {'H':1, 'G':2},
			        'F': {'H':3},
			        'G': {},
			        'H': {}
       				}

		self.known_path = (['A', 'C', 'D', 'F', 'H'], 8)
		self.known_path_file = (['W', 'R', 'P', 'N', 'M', 'K', 'I', 'J'], 2263.8175340937455)

	def test_shortest_path(self):
		self.assertEqual(self.known_path, ShortestPath().find(self.net, s='A', t='H'))

	def test_from_file(self):
		finput, cities = InputFileReader().read()
		self.assertEqual(self.known_path_file, ShortestPath().find(finput, s='W', t='J'))

	def test_min_path(self):
		self.assertEqual(['A'], ShortestPath().find(self.net, s='A', t='A'))

	# def test_wrong_source(self):
	# 	self.assertRaises(SourceNotFoundException, ShortestPath().find(self.net, s='Z', t='A'))



if __name__ == '__main__':
    unittest.main()