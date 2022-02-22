class Input:
	year = ""
	date = ""
	doordash = 0
	uber = 0
	grubhub = 0
	postmates = 0
	other = 0
	discount = 0
	__total = 0
	def __init__(self):
		return

	def setTotal(self):
		self.__total = self.doordash + self.uber + self.grubhub + self.postmates + self.other

	def getTotal(self):
		return self.__total
