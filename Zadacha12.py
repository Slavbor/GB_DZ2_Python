# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

number1 = int(input("Введите сумму чисел: "))
number2 = int(input("Введите произведение чисел: "))
for i in range(number1):
    for j in range(number1):
        if j + i == number1 and j * i == number2:
            print(i, j)
            exit()
print("Не соответствует условию.")



