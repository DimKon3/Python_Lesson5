gls = "aeiou"
line = input("Введите слово: ")
f = filter(str.isalpha, line)
clear_letter_low = "".join(f).lower()
for letter in gls:
    if clear_letter_low.count(letter)!=0:
       print("Количество",letter,":",clear_letter_low.count(letter))
    else:
        print(letter,"- False")