import mysql.connector
from mysql.connector import errorcode

config = {
	"user": "root",
	"password": "toor",
	"host": "127.0.0.1",
	"database": "movies",
	"raise_on_warnings": True
}

try:
	db = mysql.connector.connect(**config)
	print("\n Database user {} connected on host {} with database {}".format(config["user"], config["host"], config["database"]))
	input("\n\nPress any key to continue")

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Username or password is invalid")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Specified database does not exist")
	else:
		print(err)

finally:
	db.close()