def calcule(num1,operateur,num2):
    if operateur == "+":
        return num1 + num2
    elif operateur == "-":
        return num1 - num2
    if operateur == "%":
        return num1 % num2
    if operateur == "*":
        return num1 * num2
    elif operateur == "/":
        return num1 / num2
print(calcule(2023,"-",2002)) 

