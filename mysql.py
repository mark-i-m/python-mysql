import MySQLdb

# NOTE: must call close() to close connection
class MySQL:

	def __init__(self, host, uname, passwd, dbname):
		self.host = host
		self.uname = uname
		self.password = passwd
		self.db = dbname

		self.cnx = MySQLdb.connect(self.host, self.uname, self.password, self.db)
		self.cursor = self.cnx.cursor()

	def get_insert_str(self, cols):
		ret = "("
		for i in range(len(cols)-1):
			ret += " %s, "
		return ret + "%s )"	

	def insert_or_update(self, table, columns, data):
		"""
		check if the data being inserted is unique in the pk. if it is,
		then insert it into the db. If not update the existing record.
		"""
		# data to insert
		ins_command = ("REPLACE INTO " + table 
			+ " " + (self.get_insert_str(columns) % columns) 
			+ " VALUES " + self.get_insert_str(columns))

		# Insert new data
		print ins_command % data
		self.cursor.execute(ins_command, data)

		# Make sure data is committed to the database
		self.cnx.commit()

	def close(self):
		# close connection
		self.cursor.close()
		self.cnx.close()
