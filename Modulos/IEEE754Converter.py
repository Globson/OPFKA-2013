from math import modf

def decToBin(decimal):
	binary = ""
	for i in range(50):
		if (decimal * 2) >= 1:
			binary += "1"
			decimal = (decimal * 2) - 1
		else:
			binary += "0"
			decimal *= 2
	return binary


def normalizer(binum):
	""" A função retorna uma lista de dois elementos.
		o primeiro é o numero normalizado, o segundo é o numero do expoente """
	string = ""
	exp = 1
	if binum[0] == "0":
		for i in range(0, len(binum)):
			exp -= 1
			if binum[i+1] == "1":
				string = "1." + binum[i+2:]
				break
	else:
		exp = binum.index(".") - 1
		string = "1." + binum[1:].replace(".", "")

	exp = bin(exp + 127)[2:].zfill(8)
	return [string, exp]


def Converter(num):
    num = float(num)
    SIGN = "1" if num < 0 else "0"

    if num == "infinity":
    	EXP = bin(255)[2:]
    	MAN = "0"*23
    elif num == "nan":
    	EXP = bin(255)[2:]
    	MAN = "1"*23
    elif str(num).replace(".", "").replace("-", "").count("0") == len(str(num).replace(".", "").replace("-", "")):
    	if str(num)[0] == "-":
    		SIGN = "1"
    	EXP = "0"*8
    	MAN = "0"*23

    else:
    	num = abs(num)
    	decimal, integer = modf(num)

    	integerbin = bin(int(integer))[2:]  # Valor Inteiro
    	decimalbin = decToBin(decimal)  # Valor Decimal
    	binaryNum = integerbin + "." + decimalbin  # Concatenação de inteiro + decimal
    	MAN, EXP = normalizer(binaryNum)  # Normalizando numero
    	MAN = MAN[2:25]

    IEE754 = (SIGN + EXP + MAN)
    # print (IEE754)
    # print ("Sinal: ", SIGN)
    # print ("Expoente: ", EXP)
    # print ("Mantissa: ", MAN)
    return IEE754
