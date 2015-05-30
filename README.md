# python-mysql
A quick and dirty interface for inserting into a mysql db using a json config file

`config.py` defines a simple interface to read the config file, which is in json format.

`mysql.py` defines a very simple interface to the mysql db. It has only one method: `insert_or_update()`. This method takes the table, columns, and data which we want to insert. If inserting the data would violate a unique constraint or pk of the table, then the old row is dropped first.

`entry.py` is a simple example.

`config.txt` is a sample config file.
