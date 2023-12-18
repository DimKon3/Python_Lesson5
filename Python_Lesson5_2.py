gls = "aeiou"
kol_gls=0
line = input("Введите слово: ")
f = filter(str.isalpha, line)
clear_letter_low = "".join(f).lower()
for letter in gls:
    kol_letter=clear_letter_low.count(letter)
    if kol_letter!=0:
       print(f"Количество {letter}: {kol_letter}")
       kol_gls+=kol_letter
    else:
        print(letter,"- False")

print("Количество гласных:",kol_gls)
print("Количество согласных:",len(clear_letter_low)-kol_gls)