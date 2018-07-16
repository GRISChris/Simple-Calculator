#despacito

print("Calculator 2")

FirstNum = False
SecondNum = False
RetryNum = False
RestartQuestion = False

def retry(Num1, RestartQuestion):
	retry = input("are you finished calculating this number? [Y/N]\n").lower()
	while RestartQuestion == False:
		if retry in ("y", "yes"):
			quit()
		elif retry in ("n", "no"):
			CalcReset(Num1, False)
		else:
			print("no\n")

def Calculation(Num1, Num2):
	Ask = input("What do you want to do with it? [+,-,*,/,%]\n")
	if Ask in ("+", "-", "*", "/", "%"):
		if Ask == "+":
			Num1 = Num1 + Num2
		elif Ask == "-":
			Num1 = Num1 - Num2
		elif Ask == "*":
			Num1 = Num1 * Num2
		elif Ask == "/":
			Num1 = Num1/Num2
		elif Ask == "%":
			Num1 = Num1%Num2
		
		print("The Result is %f" % Num1)
		retry(Num1, False)
	else:
		print("what")
		Calculation(Num1, Num2)


def CalcReset(Num1, RetryNum):
	print("Okay, your current number from last result is %d " % Num1)
	Num2 = float(input("Please input number 2\n"))
	while RetryNum == False:
			try:
				RetryNum == True
				Calculation(Num1, Num2)
			except ValueError:
				print("no")


while FirstNum == False:
	try:
		Num1 = float(input("pls input number 1\n"))
		FirstNum == True
		while SecondNum == False:
			Num2 = float(input("pls input number 2\n"))
			SecondNum == True
			Calculation(Num1, Num2)
	except ValueError:
		print("no\n")
