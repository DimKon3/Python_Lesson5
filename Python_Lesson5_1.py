chislo=int(input("Введите любое целое число: "))
if (chislo>0)and((chislo%2)==0):
    print("Число",chislo," положительное четное число")
elif (chislo<0)and((chislo%2)==0):
    print("Число",chislo," отрицательное четное число")
elif chislo==0:
    print("Нулевое число")
else:
    print(chislo, "число не является четным")
