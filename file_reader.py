from math import hypot
import sqlite3 as sql

class InputFileReader:

	def __init__(self):
		self.filename = "ciudades"
		self.file_content = []		
		self.cities = {}
		self.graph = {}
		self.connection = sql.connect('db/biicode.sqlite')
		self.db = self.connection.cursor()
		self.delete_tables()

	def delete_tables(self):
		self.db.execute('DELETE FROM City')
		self.db.execute('DELETE FROM Road')
		self.connection.commit()

	def read(self):
		f = open(self.filename)
		for line in f:
			if not line.rstrip('\n'):
				continue

			self.file_content.append(line.rstrip('\n'))

		cities_marker_pos = self.file_content.index('CITIES')
		roads_marker_pos = self.file_content.index('ROADS')

		self.parse_cities(self.file_content[1:roads_marker_pos])
		self.parse_roads(self.file_content[roads_marker_pos+1:])

		self.connection.commit()

		return self.graph, self.cities

	def parse_cities(self, cities):

		for city in cities:			
			city_info = city.split()

			if not city_info[0].upper() in self.cities:
				self.cities[city_info[0].upper()] = [float(city_info[1]), float(city_info[2])]
				self.graph[city_info[0].upper()] = {}
				self.insert_city(city_info[0], city_info[1], city_info[2])

	def parse_roads(self, roads):
		for road in roads:
			
			road_info = road.split()

			if not self.cities.has_key(road_info[0]) or not self.cities.has_key(road_info[1]):
				print "Road towards inexistent city (%s -> %s)! Discarding..." % (road_info[0], road_info[1])
				continue

			distance = self.calculate_distance(road_info[0], road_info[1])
			
			self.graph[road_info[0]][road_info[1]] = distance
			self.graph[road_info[1]][road_info[0]] = distance

			self.insert_road(road_info[0], road_info[1], distance)

	def calculate_distance(self, a, b):

		point_a = self.cities[a]
		point_b = self.cities[b]

		return hypot(point_b[0] - point_a[0], point_b[1] - point_a[1])

	def insert_city(self, name, x, y):
		self.db.execute('INSERT INTO City (Name, x, y) VALUES(?,?,?)', (name.upper(), x, y))
		

	def insert_road(self, source, dest, length):
		self.db.execute('INSERT INTO Road (source, dest, length) VALUES(?,?,?)', (source, dest, length))
		self.db.execute('INSERT INTO Road (source, dest, length) VALUES(?,?,?)', (dest, source, length))
