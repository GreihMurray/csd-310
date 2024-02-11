import mysql.connector
from mysql.connector import errorcode

config = {
	"user": "root",
	"password": "toor",
	"host": "127.0.0.1",
	"database": "movies",
	"raise_on_warnings": True
}

def query1(cursor):
	cursor.execute("SELECT * FROM studio")
	studios = cursor.fetchall()

	print("\n-- DISPLAYING Studio RECORDS --")

	for studio in studios:
		print("Studio ID: " + str(studio[0]))
		print("Studio Name: " + studio[1] + "\n")

def query2(cursor):
	cursor.execute("SELECT * FROM genre")
	genres = cursor.fetchall()

	print("\n-- DISPLAYING Genre RECORDS --")

	for genre in genres:
		print("Genre ID: " + str(genre[0]))
		print("Genre Name: " + genre[1] + "\n")

def query3(cursor):
	cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
	films = cursor.fetchall()

	print("\n-- DISPLAYING Short Film RECORDS --")

	for film in films:
		print("Genre ID: " + str(film[0]))
		print("Genre Name: " + str(film[1]) + "\n")


def query4(cursor):
	cursor.execute("SELECT GROUP_CONCAT(film_name), film_director FROM film GROUP BY film_director ")
	data = cursor.fetchall()

	print("\n-- DISPLAYING GROUPED Director RECORDS --")

	for data in data:
		print("Genre ID: " + str(data[0]))
		print("Genre Name: " + str(data[1]) + "\n")


def query5(cursor):
	cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director ASC")
	data = cursor.fetchall()

	print("\n-- DISPLAYING Director RECORDS in Order --")

	for data in data:
		print("Genre ID: " + str(data[0]))
		print("Genre Name: " + str(data[1]) + "\n")


def main():
	db = None

	try:
		db = mysql.connector.connect(**config)
		print("\n Database user {} connected on host {} with database {}".format(config["user"], config["host"],
																				 config["database"]))

	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Username or password is invalid")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Specified database does not exist")
		else:
			print(err)

	cursor = db.cursor()
	query1(cursor)
	query2(cursor)
	query3(cursor)
	query4(cursor)
	query5(cursor)


if __name__ == "__main__":
	main()
