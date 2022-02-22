import tkinter as gui
import tkcalendar as cal
import input
import calc
import db

def onClickGo():

	total = 0

	inputObj = input.Input()
	inputObj.date = dateLabel.cget("text")
	inputObj.year = inputObj.date[6:]
	inputObj.doordash = float(doordash.get())
	inputObj.uber = float(uber.get())
	inputObj.grubhub = float(grubhub.get())
	inputObj.postmates = float(postmates.get())
	inputObj.discount = float(discount.get())
	inputObj.other = float(other.get())
	inputObj.setTotal()

	#database.addWeek(inputObj)
	tc = calc.TaxCalculator(inputObj.getTotal()) # MUST RETURN FROM DATABASE, CHANGE
	tc.setMileage(inputObj.discount)

	#tc = calc.TaxCalculator(db.getTotal())
	#tc.setMileage(db.getMileage())
	tc.calculate()

	grossIncomeOut.configure(text = round(tc.getProfit(), 2))
	selfEmployTaxOut.configure(text = round(tc.getSelfEmployTax(), 2))
	subjectIncomeOut.configure(text = round(tc.getTaxableIncome(), 2))
	incomeTaxOut.configure(text = round(tc.getIncomeTax(), 2))
	tithingOut.configure(text = round(tc.getTithing(), 2))
	afterTaxIncomeOut.configure(text = round(tc.getAfterTaxIncome(), 2))
	seperateOut.configure(text = round(tc.getSeperateOut(), 2))

	if not outputFrame.winfo_ismapped():
		packOutput()

def onClickWeek():
	weekWindow = gui.Toplevel(window)

def packOutput():
	outputFrame.pack()
	for i in range(len(staticOutLabels)):
		staticOutLabels[i].grid(row = i, column = 0, padx = 5, pady = 5)
	grossIncomeOut.grid(row = 0, column = 1, padx = 5, pady = 5)
	selfEmployTaxOut.grid(row = 1, column = 1, padx = 5, pady = 5)
	subjectIncomeOut.grid(row = 2, column = 1, padx = 5, pady = 5)
	incomeTaxOut.grid(row = 3, column = 1, padx = 5, pady = 5)
	tithingOut.grid(row = 4, column = 1, padx = 5, pady = 5)
	afterTaxIncomeOut.grid(row = 5, column = 1, padx = 5, pady = 5)
	seperateOut.grid(row = 6, column = 1, padx = 5, pady = 5)

def change_label(event):
	dateLabel.config(text = calendar.get_date())

window = gui.Tk()
database = db.Database()

calendar = cal.Calendar(window, selectmode = "day", year = 2021, month = 4, day = 1)
calendar.bind("<<CalendarSelected>>", change_label)

#INPUT
entryFrame = gui.Frame()

dateLabel = gui.Label(entryFrame, text = calendar.get_date())

userInputLabels = [
	gui.Label(entryFrame, text = "Week of:"),
	gui.Label(entryFrame, text = "Doordash:"),
	gui.Label(entryFrame, text = "Uber:"),
	gui.Label(entryFrame, text = "Grubhub:"),
	gui.Label(entryFrame, text = "Postmates:"),
	gui.Label(entryFrame, text = "Other:"),
	gui.Label(entryFrame, text = "Mileage Discount:"),
]


doordash = gui.Entry(entryFrame)
uber = gui.Entry(entryFrame)
grubhub = gui.Entry(entryFrame)
postmates = gui.Entry(entryFrame)
other = gui.Entry(entryFrame)
discount = gui.Entry(entryFrame)

buttonFrame = gui.Frame()
goButton = gui.Button(buttonFrame, text = "Go", command = onClickGo)
weekButton = gui.Button(buttonFrame, text = "See all", command = onClickWeek)


#OUTPUT
outputFrame = gui.Frame()
staticOutLabels = [
	gui.Label(outputFrame, text = "Gross Income: "),
	gui.Label(outputFrame, text = "Self-Employment Tax: "),
	gui.Label(outputFrame, text = "Fed Income Taxable Income: "),
	gui.Label(outputFrame, text = "Income Tax: "),
	gui.Label(outputFrame, text = "Tithing: "),
	gui.Label(outputFrame, text = "Made After Tax and Tithe:"),
	gui.Label(outputFrame, text = "Seperate: "),
]

grossIncomeOut = gui.Label(outputFrame, text = 0)
selfEmployTaxOut = gui.Label(outputFrame, text = 0, fg = "red")
subjectIncomeOut = gui.Label(outputFrame, text = 0)
incomeTaxOut = gui.Label(outputFrame, text = 0, fg = "red")
tithingOut = gui.Label(outputFrame, text = 0, fg = "red")
afterTaxIncomeOut = gui.Label(outputFrame, text = 0)
seperateOut = gui.Label(outputFrame, text = 0)



#PACKING
calendar.pack(padx = 5, pady = 5)

entryFrame.pack()
for i in range(len(userInputLabels)):
	userInputLabels[i].grid(row = i, column = 0, padx = 5, pady = 5)

dateLabel.grid(row = 0, column = 1, padx = 5, pady = 5)
doordash.grid(row = 1, column = 1, padx = 5, pady = 5)
uber.grid(row = 2, column = 1, padx = 5, pady = 5)
grubhub.grid(row = 3, column = 1, padx = 5, pady = 5)
postmates.grid(row = 4, column = 1, padx = 5, pady = 5)
other.grid(row = 5, column = 1, padx = 5, pady = 5)
discount.grid(row = 6, column = 1, padx = 5, pady = 5)

buttonFrame.pack()
goButton.pack()

window.mainloop()
