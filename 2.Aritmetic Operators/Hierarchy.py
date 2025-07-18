num1 = 100
num2 = 50
num3 = 25
num4 = 10

print(num1 + num2 * num3)
print((num1 + num2) * num3)
print((num1 + num2) * num3 - num4)
print((num1 + num2) * (num3 - num4))
print((num1 + num2) * (num3 - num4) / (num3 - num4))
print((num1 + num2) * (num3 - num4) / (num1 - num1)) #Thi will generate an error because of a division by cero