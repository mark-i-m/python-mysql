import config, mysql

# read config file
config = config.Config("config.txt")

# get connection 
mysql = mysql.MySQL(config.db_host, config.db_uname, config.db_passwd, config.db_name)

# insert
for id in range(10): 
	data = (id % 2, "Doe % d" % id, "John", "place", "ville") 
	mysql.insert_or_update(config.db_table, config.db_columns, data)

# close connection
mysql.close()
