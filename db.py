import mysql.connector


class Database:

	__connection = None
	__cursor = None
	def __init__(self):
		try:
			self.__connection = mysql.connector.connect(
			host = "localhost",
			user = "stephen",
			password = "followthespirit14",
			database = "tax_test")
		except mysql.connector.Error as err:
			if (err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR):
				print("Bad username or password")
				exit()
			elif(err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR):
				print("No such database")
				exit()
			else:
				print(err)
				exit()

		self.__cursor = self.__connection.cursor()



	def addWeek(self, input):
		#TO DO: REMOVE i, for week, in db, add another double for discount
		countsql = "SELECT COUNT(*) from data"
		self.__cursor.execute(countsql)
		count = self.__cursor.fetchone()

		sql = "INSERT INTO data VALUES (%i, %s, %s, %d, %d, %d, %d, %d, %d, %d)"
		values = (count[0] + 1, input.year, input.date, input.doordash, input.uber, input.grubhub,
					input.postmates, input.other, input.discount, input.getTotal())
		self.__cursor.execute(sql, values)
		self.__connection.commit()

	def getTotal(self):
		self.__cursor.execute("SELECT total FROM data")
		result = self.__cursor.fetchall()

		total = 0
		for x in result:
			total += x[0]
		return __total

	def getMileage(self):
		self.__cursor.execute("SELECT discount FROM data")
		result = self.__cursor.fetchall()
		total = 0

		for x in result:
			total += x[0]

		return __total

	def updateWeek(self, day):
		return

	def removeWeek():
		return
