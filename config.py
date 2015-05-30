class Config:
	def __init__(self, config_file):
		import json

		self.config_file = config_file

		with open(config_file, "r") as myfile:
			config = json.loads(myfile.read())

		self.db_host = config["db_host"]
		self.db_uname = config["db_uname"]
		self.db_passwd = config["db_passwd"]
		self.db_name = config["db_name"]

		self.db_table = config["db_table"]
		self.db_columns = tuple(config["db_columns"])
