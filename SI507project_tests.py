import sqlite3
import unittest
from SI507project_tools import *

class SQLiteDBTests(unittest.TestCase):

	def setUp(self):
		self.conn = sqlite3.connect("parks.db") 
		self.cur = self.conn.cursor()

	def test_for_parks_table(self):
		self.cur.execute("select name, location, pysical_address, state_id, type_id from park where name = 'Horseshoe Bend'")
		data = self.cur.fetchone()
		self.assertEqual(data,('Horseshoe Bend', 'Daviston, AL','\n11288 Horseshoe Bend Road\n Daviston, AL\n36256     \n', 1, 2), "Testing data that results from selecting park Horseshoe Bend")

	def test_for_state_table(self):
		res = self.cur.execute("select * from state")
		data = res.fetchall()
		self.assertTrue(data, 'Testing that you get a result from making a query to the state table')

	def test_state_foreign_key_park(self):
		res = self.cur.execute("select * from park INNER JOIN state ON park.state_id = state.id")
		data = res.fetchall()
		self.assertTrue(data, "Testing that result of selecting based on relationship between parks and states does work")
		self.assertTrue(len(data) in [489, 489], "Testing that there is in fact the amount of data entered that there should have been -- based on this query of everything in both tables.{}".format(len(data)))

	def test_type_foreign_key_park(self):
		res = self.cur.execute("select * from park INNER JOIN type ON park.type_id = type.id")
		data = res.fetchall()
		self.assertTrue(data, "Testing that result of selecting based on relationship between parks and types does work")
		self.assertTrue(len(data) in [489, 489], "Testing that there is in fact the amount of data entered that there should have been -- based on this query of everything in both tables.{}".format(len(data)))

	def tearDown(self):
		self.conn.commit()
		self.conn.close()


class CVSTests(unittest.TestCase):
	def test_park_data(self):
		self.park_file = open('park_data.csv','r')
		self.row_reader = self.park_file.readlines()
		# print(self.row_reader) # For debug
		self.assertTrue(self.row_reader[1].split(",")[0], "Testing that there is a Name / first value in the row at index 1")
		self.assertTrue(self.row_reader[25].split(",")[0], "Testing that there is a Name / first value in the row at index 25")
		self.park_file.close()

	def test_park_data2(self):
		self.park_file = open('park_data.csv','r')
		self.row_reader = self.park_file.readlines()
		self.assertTrue(len(self.row_reader) == 4943, "Testing that there are {} lines in park_data".format(len(self.row_reader)))
		self.park_file.close()


class ParkInfoClassTest(unittest.TestCase):

	def setUp(self):
		self.park_instance = session.query(Park).filter_by(name="Little River Canyon").first()
		self.park_info = ParkInfo(self.park_instance)
	
	def testStr(self):
		self.assertEqual(self.park_info.__str__(), "The park is Little River Canyon", "Test the __str__() function")

	def testGetInfo(self):
		self.assertEqual(self.park_info.get_info()["name"], "Little River Canyon", "Test the get_info() function")

	def tearDown(self):
		del(self.park_info)

if __name__ == '__main__':
    unittest.main(verbosity=2)













