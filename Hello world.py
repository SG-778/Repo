"""print("Hello world")
print("Sergei")
print("Donetsk")
print("I'm learning the programming language Python")
print(2020)
print(2 + 2)
print("01.29.2025")"""
from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK
from unittest.util import three_way_cmp

#print("On the first day of Christmas my true love gave to me")
#print("a partridge in a pear tree")
#print("On a second day of Christmas my true love gave to me")
#print("Two turtle doves and a partridge in a pear tree")

#print("five little monkeys\njumping on a bed\nand running late")

#fsr_num = int(input('Enter your age: '))
#sec_num = int(input('Enter your SSN: '))
#trd_num = int(input('Enter a year: '))
#together = fsr_num + sec_num + trd_num
#print(f'{fsr_num} + {sec_num} + {trd_num} = {together}')

#orig = int(input('origin num: '))
#prev_num = orig - 1
#next = orig + 1
#print(f'Previous num: {prev_num}')
#print(f'next number is: {next}')

#new1 = float(input("What is the cathetus1: "))
#new2 = float(input('What is the cathetus2: '))
#trian = 1/2*(new1 * new2)
#print(f'square = {trian}')

#name = input('What is your name, dear?: ')
#age = input('How old are you?: ')
#print(f'{name} is the best and your age, {age} years suits you')

#dig1 = int(input('What is the number 1?: '))
#dig2 = int(input("What is the number 2?: "))
#add = dig1 + dig2
#div = dig1 / dig2
#subs = dig1 - dig2
#mult = dig1 * dig2
#print(f'add = {add}, div = {div}, subs = {subs}, mult = {mult}')

#sides = int(input('How many sides?: '))
#if sides < 3:
 #   print("polygon must have at least 3")
#else:
    #all_tog = 180 * (sides - 2)
    #print(f'The sum of all angles = {all_tog}')

#dist = int(input('What is the dist(km)?: '))
#speed = int(input('What is your speed: '))
#time = speed / dist
#print(f'Your time will be = {time}')

#dist_km = int(input('How many km?: '))
#dist_m = dist_km * 1000
#dist_cm = dist_m * 100
#print(f'Distance in m = {dist_m}, in cm = {dist_cm}')
#farh = float(input('How many Farenh?: '))
#celc = (farh - 32) * 5 / 9
#print(f'{farh} in celcius = {celc}')

#price = int(input('Whats the price?: '))
#tip_perc = price * 0.2
#tax_perc = price * 0.04
#print(f'With price {price} the tips will be {tip_perc} and taxes {tax_perc}')
#tot = tip_perc + tax_perc + price
#print(tot)

#pr = float(input("Whats the orig price ($): "))
#disc = int(input('What is disc percent? (%):  '))
# NOT CORRECT full_pr = (100 * pr)/disc
#10% = 40$
#100% = x$
#full_pr = pr / (100 - disc) * 100
#print(f'Full price is {full_pr}')
#print(round(full_pr, 2))

#fst_cl = int(input('How many kids in a class?: '))
#sc_cl = int(input('How many in a second cl?: '))
#trd_cl = int(input('How many in third?: '))
#desks = [fst_cl, sc_cl, trd_cl]
#needed = max(desks) // 2 + max(desks) % 2
#print(f'IN total {needed} needed.')
#its = 'season'
#print(len(its))

#text = input('Write smth')
#n = text[4]
#print(n)
#text = 'coode'
#print(text[4])

#fst_nm = input('What id your fst name?: ')
#lst_nm = input('What is your lst name?: ')
#full = fst_nm + " " +  lst_nm
#print(f'Full name is: {full} ')

#name = input('What is your name?: ')
#print(f'Your name is {name}')
#print(f'{name}, Your name has {len(name)} letters')
#print(f'{name}, your name starts with letter \"{name[0]}\"')
#print(f'{name}, your name ends with letter \"{name[-1]}\"')

#fav = ("My favorite poem is: \n Мороз и солнце, \n День чудесный.")
#print(fav)

#greet = "Happy Birthday! "
#print(greet * 3)

#greet = input('Enter the word: ')
#print(greet[::-1])

#name = input("Whats the name? ")
#print(f'Hello {name[::-1]}' )

#word = 'posledstvie'
#print(word[2:-2])

#word1 = input('Frst word: ')
#word2 = input('Secnd word: ')
#print(f"{word1[::-1]} {word2[::-1]}")

#smt1 = input('Enter word ')
#smt2 = input('Enter another ')
#the words: Kolbasa and ratatui
#inside = smt1[:3]
#inside2 = smt1[-4:]
#print(f"{inside}{smt2[:7]}{inside2}")


#st = '1234567890'
#f = '+' + st[0:3]
#s = ' ' + st[3:6]
#t = '-' + st[6:10]
#final = f + s + t
#print(final)

#slovo = 'marmelad'
#add = len(slovo) + 4
#border = '*' * add
#result = (f'{border}\n* {slovo} *\n{border}')
#print(result)

#first = int(input ("Enter first num: "))
#sec = int(input('Enter sec num: '))
#absolut = first - sec
#print(f'{abs(absolut)}')
#Функцию abs() нужно применить к absolut
#Неправильный формат print() — f'(abs{absolut})' не сработает так, как ты ожидаешь.

#price = 124
#delivery = price * 0.03
#total_price = price + delivery
#print(round(total_price, 2))

#grades = (77.3, 80.3, 95.4, 33.4, 46.5)
#aver = sum(grades) / len(grades)
#print(f'{round(aver)}')
# либо так print(round(aver))
#Вместо жёсткого числа 5 лучше использовать len(grades), чтобы код работал с разными списками оценок.

#word = input('Enter your word: ')
#n = word[3]
#if n != 's':
#   print('N/A')
#else: print('yes')

#char = input('Enter symbol: ').lower() Чтобы распознавало также и большие буквы
#if char in ('a', 'o', 'e', 'y'):
#    print('Yes, its vowel')
#Забыл про 'in'

#name = 'Sergei'
#if name[0] in ('a','o','e','y'):
#    print('Yes, starts w vowel')
#else:
#    print('Not vowel')

#name = input('Whats your name?: ')
#if len(name) >= 5:
#    print('Your name is long!')
#else:
#    print('Your name is short')

#answer = input("Are you ok? ").lower()  # Получаем ответ пользователя и приводим к нижнему регистру
#if answer == "no":
#    print("Get better!")
#else:
#    print("Cool!")

#name = input('What name?: ')
#time = int(input('what time?:'))
#if time <= 6 > 0:
#    print(f'Good morning, {name}')
#else:
#    print(f'fuck you, {name}')


#GPT
#a = float(input("Введите первое число (a): "))  # Ввод первого числа
#operation = input("Введите операцию (+, -, *, /, %, //): ")  # Ввод операции

# Выполнение операции
#if operation == "+":
#    result = a + b
#elif operation == "-":
#    result = a - b
#elif operation == "*":
#    result = a * b
#elif operation == "/":
#    if b != 0:
#        result = a / b
#    else:
#        result = "Ошибка! Деление на ноль."
#elif operation == "%":
#    if b != 0:
#        result = a % b
#    else:
#        result = "Ошибка! Деление на ноль."
#elif operation == "//":
#    if b != 0:
#        result = a // b
#    else:
#        result = "Ошибка! Деление на ноль."
#else:
#    result = "Неизвестная операция!"

# Вывод результата
#print(f"{a} {operation} {b} = {result}")


#price = float(input("Введите цену товара: "))  # Вводим цену товара

# Проверка условий скидок
#if price >= 300:
#    discount = 0.30  # Скидка 30%
#elif price >= 200:
#    discount = 0.20  # Скидка 20%
#elif price >= 100:
#    discount = 0.10  # Скидка 10%
#else:
#    discount = 0  # Нет скидки

# Рассчитываем итоговую стоимость
#final_price = price * (1 - discount)

# Выводим результат
#print(f"Итоговая стоимость товара: {round(final_price, 2)}")


#current_color = input("Введите текущий цвет сигнала светофора ('red', 'yellow', 'green'): ").lower()
#
#if current_color == 'red':
#    next_color = 'green'
#elif current_color == 'green':
#    next_color = 'yellow'
#elif current_color == 'yellow':
#    next_color = 'red'
#else:
#    next_color = 'Неизвестный цвет!'

#print(f"Следующий цвет сигнала светофора: {next_color}")


#num_of_day = int(input("Введите номер дня недели (1-7): "))
#day = "Weekend" if num_of_day == 6 or num_of_day == 7 else "Work day"
#print(f"Сегодня: {day}")

#number = int(input("Введите число: "))

#print(number * 2 if number > 0 else -number)

#name = input("Введите имя и фамилию (например, 'Alice Moon'): ")

# Разделяем строку на имя и фамилию
#first_name, last_name = name.split()
#email = f"{first_name}.{last_name}@company.com"
#print(f"Адрес электронной почты: {email}")


#time = input("Введите время в формате 'HH:MM:SS': ")
# Разделяем строку вручную
#hour = int(time[0:2])  # Берем первые два символа для часов
#minute = int(time[3:5])  # Берем два символа для минут
#second = int(time[6:8])  # Берем два символа для секунд
#
#total_seconds = hour * 3600 + minute * 60 + second
#print(f"Часы: {hour}, Минуты: {minute}, Секунды: {second}")
#print(f"Общее количество секунд: {total_seconds}")

#task = input('enter word:')
#if task.islower() == True:

#    print("Has only lowers")

#word = 'programmer'
#i = word.find('r')
#d = word.rfind('r')
#print(i, d)

#slovo = 'training'
#n = 5
#print(slovo[5] * n)

#phrase = 'Winter is magic'
#f, s, t = phrase.split()
#print(t,s,f)

#phrase = "My eyes are green too!"
#user = input("what color is your eyes?: ")
#
#new = phrase.replace('green', user)
#print(new)

#text = "If you want to be somebody, somebody really special, be yourself."
#o = text.count('o')
#e = text.count('e')
#if o > e:
#    print(f'o = {o}')
#else:
#    print(f'e = {e}')

#name = (input('Enter name: '))
#last = (input("entr last name: "))
#mid = (input('enter middle: '))
#tot_len = max(len(name),len(last), len(mid))
#print(name.rjust(tot_len))
#print(mid.rjust(tot_len))
#print(last.rjust(tot_len))

#word = input("Введите слово: ")  # Вводим слово
#length = len(word) + 4  # Длина рамки = длина слова + 4 (по 2 '*' с каждой стороны)
#border = '*' * length  # Верхняя и нижняя границы

# Формируем результат
#result = f"{border}\n* {word} *\n{border}"

#name = input('Enter your name: ')
#cons = 'pstdrw'
#if name[0].lower() in cons:
#    print(f"Your {name} starts with consonent")
#else:
#    print(f'{name} starts with vowel')

#Удаление пробелов в начале → lstrip()
#Замена пробелов в конце → rstrip().replace(' ', '!')
#Каждое слово с заглавной буквы → title()

#s = 'I love sex'
#vowels = 'aoeiu'
#for v in vowels:
#    s = s.replace(v,'')
#print(s)

#word1 = input('Enter your word: ')
#word_change = 'shitty'
#word1 = word1.replace('nice', word_change)
#print(word1)

#num = 2
#while num <= 30:
#    print(num)
#    num += 2


#num = 0.2
#while num <= 3.4:
#    print(round(num, 1))
#    num += 0.2


#x = 0
#for num in range(5, 42):
#   if num %2 != 0:
#    x += num
# num += 1 => НЕ НУЖНО ЗДЕСЬ Т.К. for УВЕЛИЧИВАЕТ num автоматически
#print(f"sum = {x}")

#x = 1
#for mult in range(-1, -12, -1):
#    x *= mult то же самое что x = x * mult
#    print(f'mult = {mult}, x = {x}')

#stroka = ('z')
#new = stroka * 30
#print(len(new), new)

#sheeps = ''
#count = 1
#while count <= 30:
#    sheeps += f"{count} sheep ..."
#    count += 1
#print(sheeps)
#Если print включен в блок то будет построково но не одной строкой

#result = ''
#for count in range(10,0,-1):
 #   result += f"{count} second{'s' if count > 1 else ''}..."
 #   if count == 1:
 #       result += f"{count} second..."
#print(result)

#km = 5
#day = 1
#n = int(input("How many km need: "))
#while km <= n+1:
#    day += 1
#    km += km * 0.05
#    print(km)

#n = int(input('How many words needed: '))
#day = 1
#words = 5
#today = 5
#while words < n:
#    day += 1
#    today += 2
#    words += today
#print(f"{day} days for {n} words")

#num = 1
#tot = 0
#for num in range(0,101):
#    tot += num
#print(tot)

#n = 1
#res = 0
#for n in range(52):
#    if n % 2 != 0:
#        res += n
#        print(f"{res} = {n}")


#tot = 0
#for n in range(1001):
#     if n % 3 == 0:
#         tot +=1
#print(tot)
#но как понять КАКИЕ ИМЕННО ЭТО ТЧИСЛА

#even = 0
#odd = 0
#sum_even = 0
#for plus in range(101):
#    if plus % 2 == 0:
#        even += 1
#        sum_even += plus
#    else:
#        odd += 1
#print(odd, even, sum_even)



#n = int(input("n = "))
#k = int(input("k = "))
#res = 0
#for job in range(k):
#    res += n * n
#print(res)
#res = 0
#1-й проход: res = 0 + 3*3 = 9 ( при n = 3, k = 4)
#2-й проход: res = 9 + 3*3 = 18
#3-й проход: res = 18 + 3*3 = 27
#4-й проход: res = 27 + 3*3 = 36


#n = 7
#fuck = 1
#for num in range(1, n +1):
#    fuck *= num
#print(fuck)

#total = 200
#spent = 0
#for num in range(1,11):
#    spent += 3
#    total -= spent
#print(total)

#n = int(input('How many str?: '))
#for symbol in range(1, n + 1):
#    print(symbol * "*")

#n = int(input("How many str?: "))
#for i in range(1, n + 1):
#    step = i * "#"
#    print(step)

#t = 'hello'
#for g in range(len(t)):
#    print(t[g])

#stroka = input("enter your speech: ")
#for h in range(len(stroka)):
#    print(h, "-", stroka[h])

#g = input('type: ')
#vow = 0
#for h in range(len(g)):
#    if g[h].isupper():
#        vow += 1
#print(vow)

#k = input('give me text: ')
#vow = 'aoeiuAOEIU'
#numba = 0
#for cnt in k:
#    if cnt in vow:
#        numba += 1
#print(numba)

#n = "Python"
#new = ''
#for tt in n:
#    new += ' ' + tt
#print(new)

#n = "Bananas,2apples,sweets and 8plums"
#new = ''
#for hh in n:
#    new += hh
#    if  not hh.isalpha():
#        new += ' '
#print(new)

#stroka = 'summer'
#vowels = 'aouie'
#new = ''
#for letter in stroka:
#    if letter in vowels:
#        new += letter.upper()
#    else:
#        new += letter
#print(new)

#stroka = 'Bananas'
#vowels = 'aouie'
#for vowel in vowels:
#    stroka = stroka.replace(vowel, "*")
#print(stroka)

#its = 'holidays'
#vowels = 'aouie'
#for x in vowels:
#    its = its.replace(x, '')
#print(its)

#dano = 'coinsidence'
#new = ''
#new2 = ''
#for index, letter in enumerate(dano):
#    if index % 2 == 0:
#        new += letter
#    if index % 2 != 0:
#        new2 += letter
#print (new, new2)

dano = input("enter: ")
mal = 0
bol = 0
for l in dano:
    if l.isalpha():
        if l.islower():
            mal += 1
        elif l.isupper():
            bol += 1
if mal > bol:
    print(dano.lower())
elif bol > mal:
    print(dano.upper())
else:
    print(dano.lower())