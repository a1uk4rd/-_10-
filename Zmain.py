#1
a = input("Введите список через запятую: ").split(",")
a.reverse()
print(a)

#2
a = input("Введите список через запятую: ").split(",")
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
print(change(a))

#3
a = input("Введите список через запятую: ").split(",")
def to_list(*args):
    return list(args)
print(to_list(a))

#4
a = input("Введите список через запятую: ").split(",")
def useless(lst):
    return max(lst) / len(lst)
print(useless(a))
#5
a = input("Введите список через запятую: ").split(",")
def list_sort(lst):
    lst.sort()
    return lst
print(list_sort(a))

#6
a = input("Введите список через запятую: ").split(",")
def all_eq(lst):
    max_item = max(lst, key=lambda x: len(x))
    max_len = len(max_item)
    return [item.ljust(max_len, '_') for item in lst]
print(all_eq(a))

#screen 2

#1
a = int(input())
def to_float(num):
    if type(num) == int or float:
        return float(a)
    else:
        return ('Невозможно преобразовать')

print(to_float(a))

#2
a = int(input())
b = int(input())
c = int(input())
d = int(input())
def avg_5(a, b, c, d):
    return round((a + b + c + d) / 4, 5)
print(avg_5(a, b, c, d))

#3
a = int(input())
b = int(input())
def mul_to_int(a, b):
    c = a * b
    if type(c) == int:
        return int(c)
    elif type(c) == float:
        return float(c)
print(mul_to_int(a, b))

#4
import math
x = int(input())
r = ((3*x)/(4 * math.pi)) ** (1/3)
print(r)

#screen 3

#1
a = int(input())
def dislike_6(a):
    if a == 6.0 and type(a) == int or float:
        return ('Только не 6!')
    else:
        return True

#2
'''''
– Коммутативность (к)
A or B = B or A
A and B = B and A

– Дистрибутивность (д)
A and (B or C) == (A and B) or (A and C)
A or (B and C) == (A or B) and (A or C)

– Ассоциативность (а)
A or (B or C) == (A or B) or C == A or B or C
A and (B and C) == (A and B) and C == A and B and C

– Теорема Де Моргана (м)
not (A or B) == not A and not B
not (A and B) == not A or not B
not (A < B) == A >= B
not (not (A)) = A
'''''
def help_bool(letter):
    if letter == 'к':
        return 'A or B = B or A\nA and B = B and A'
    elif letter == 'а':
        return 'A or (B or C) == (A or B) or C == A or B or C\n' \
               'A and (B and C) == (A and B) and C == A and B and C'
    elif letter == 'д':
        return 'A and (B or C) == (A and B) or (A and C) \nA or (B and C) == (A or B) and (A or C)'
    elif letter == 'м':
        return 'not(A or B) == not A and not B \nnot(A and B) == not A or not B\n' \
               'not(A < B) == A >= B\nnot(not(A)) = A'
    else:
        return 'Возможные аргументы: к – Коммутативность, д – Дистрибутивность, а – Ассоциативность, ' \
               'м – Теорема Де Моргана'

#screen 6

#1
def to_dict(lst):
    return {element: element for element in lst}

#2
my_dict = {'first_one': 'we can do it'}
def biggest_dict(**kwargs):
    my_dict.update(**kwargs)
biggest_dict(k1=22, k2=31, k3=11, k4=91)
biggest_dict(name='Кирилл', age=16, weight=69, eyes_color='grey/blue')
print(my_dict)

#3
def count_it(sequence):
    num_frequency = {int(item): sequence.count(item) for item in sequence}
    sorted_num_frequency = sorted(num_frequency.items(), key=lambda element: element[1])
    return dict(sorted_num_frequency[-3:])

#4

#stroki 1
#1
def search_substr(subst, st):
    if subst.lower() in st.lower():
        return 'Есть контакт!'
    else:
        return 'Мимо!'

#2
def first_last(letter, st):
    first = st.find(letter)
    if first < 0:
        return None, None
    last = st.rfind(letter)
    return first, last

#3
from collections import Counter
def top3(st):
    counter_top3 = Counter(st.replace(' ', '')).most_common(3)
    return ', '.join([f'{letter} - {cnt}' for letter, cnt in counter_top3])

#4
def camel(st):
    new_st = ''
    letter_counter = 0
    for index, val in enumerate(st):
        if val.isalpha():
            if letter_counter % 2 == 0:
                new_st += val.upper()
            else:
                new_st += val.lower()
            letter_counter += 1
        else:
            new_st += val
    return new_st

#5
def shortener(st):
    while '(' in st or ')' in st:
        left = st.rfind('(')
        right = st.find(')', left)
        st = st.replace(st[left:right + 1], '')
    return st

#6
def cleaned_str(st):
    clean_lst = []
    for symbol in st:
        if symbol == '@' and clean_lst:
            clean_lst.pop()
        elif symbol != '@':
            clean_lst.append(symbol)
    return ''.join(clean_lst)

#Zadachi 2
#10
a1 = input("Введите список через запятую: ").split(",")
b = input("Введите список через запятую: ").split(",")
def tochki(x, y):
    if len(x) != len(y):
        return "Неравное кол-во точек"
    dots = []
    for i in range(len(x)):
        dots.append(f"({x[i]}; {y[i]})")
    return dots
print(tochki(a1, b))

#11
def gosti(guests):
    greetings = []
    for guest in guests:
        greetings.append(f"Добро пожаловать, {guest}!")
    return greetings
guests_list = input()
print(gosti(guests_list))

#12
def bukvi(a):
    if len(a) > len(set(a)):
        return True
aa1 = input()
print(bukvi(aa1))

#13
def probel(st):
    return ' '.join(st.split())
a = input()
print(probel(a))

#14
import math
def calculate_water_mass(radius, height):
    volume = math.pi * (radius ** 2) * height
    density = 1000  # кг/м³
    mass = volume * density
    return round(mass, 2)
radius = int(input())
height = int(input())
print(calculate_water_mass(radius, height))

#15
def umn(numbers_str):
    numbers = map(float, numbers_str.split())
    product = 1
    for number in numbers:
        product *= number
    return product
a = input()
print(umn(a))

#16
def calculate_total_volume(boxes):
    total_volume = 0
    for box in boxes:
        length, width, height = box
        volume = length * width * height
        total_volume += volume
    return total_volume
boxes = [(2, 3, 4), (1, 2, 1), (3, 3, 3)]
total_volume = calculate_total_volume(boxes)
print(f"Общий объем коробок: {total_volume}")

#17
def rounder(number):
    factor = 10 ** 3
    integer_part = int(number * factor)
    fractional_part = number * factor - integer_part
    if fractional_part >= 0.5:
        integer_part += 1
    return integer_part / factor


def pyph(dict):
    x = dict.get("x")[0] - dict.get("x")[1]
    y = dict.get("y")[0] - dict.get("y")[1]
    lenght = math.sqrt(x ** 2 + y ** 2)
    lenght = rounder(lenght)
    return lenght
 print(pyph({"x":[0; 5], "y":[0; 3]}))

#18
def perevod(input_string):
    leet_dict = {
        'a': '4',
        'b': '8',
        'e': '3',
        'g': '9',
        'i': '1',
        'l': '1',
        'o': '0',
        's': '5',
        't': '7',
        'z': '2'
    }
    encoded_string = ''
    for char in input_string:
        encoded_string += leet_dict.get(char.lower(), char)
    return encoded_string
input_str = "Hello, World!"
encoded_str = perevod(input_str)
print(f"Закодированная версия: {encoded_str}")

#19
def new_sum(numbers):
    result = []
    current_sum = 0
    for number in numbers:
        current_sum += number
        result.append(current_sum)
    return result
input_numbers = [5, 6, 7, 8, 9]
output_array = new_sum(input_numbers)
print(f"Результат: {output_array}")

#20
def vosrastayut_li(arr):
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            return False
    return True
numbers = [1, 2, 3, 4, 5]
print(vosrastayut_li(numbers))
numbers = [1, 3, 2, 4]
print(vosrastayut_li(numbers))

#21
def median(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
    else:
        return sorted_arr[mid]
numbers = [3, 1, 4, 2, 5]
print(median(numbers))
numbers = [3, 1, 4, 2]
print(median(numbers))

#7
def button_presses(message):
    presses = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
        'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
        'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
        'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
        'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
        'Z': 26, ' ': 0
    }

    total_presses = 0
    for char in message.upper():
        total_presses += presses.get(char, 0)
    return total_presses
message = "Happy New Year"
print(button_presses(message))

#8
def reverse(s):
    return s[::-1].swapcase()
input_string = "Happy New Year"
result = reverse(input_string)
print(result)

#9
def delete_enemies(names, enemies):
    return [name for name in names if name not in enemies]
names_list = ["Кирилл", "Владислав", "Илья", "Роман"]
enemies_list = ["Владислав", "Роман"]
filtered_names = delete_enemies(names_list, enemies_list)
print(filtered_names)

#zadachi 3
#1
def rock_paper_scissors(player1, player2):
    options = ['камень', 'ножницы', 'бумага']
    if player1 not in options or player2 not in options:
        return "Ошибка: игроки должны выбрать 'камень', 'ножницы' или 'бумага'."
    if player1 == player2:
        return "Ничья!"
    if (player1 == 'камень' and player2 == 'ножницы') or \
            (player1 == 'ножницы' and player2 == 'бумага') or \
            (player1 == 'бумага' and player2 == 'камень'):
        return "Игрок 1 выигрывает!"
    else:
        return "Игрок 2 выигрывает!"
result = rock_paper_scissors('камень', 'ножницы')
print(result)

#10
def distribution(coins):
    total_coins = sum(coins)
    return total_coins % 3 == 0
coins_array = [5, 10, 15]
result = distribution(coins_array)
if result:
    print("Монеты можно распределить поровну.")
else:
    print("Монеты нельзя распределить поровну.")

#2
def replace(text):
    while text.endswith('??') or text.endswith('!!'):
        if text.endswith('???'):
            text = text[:-3] + '?'
        elif text.endswith('!!!'):
            text = text[:-3] + '!'
    return text

# Пример использования
input_text = "Почему ты не готов к уроку???!!!"
result = replace(input_text)
print(result)

#3
def card_sum(cards):
    total = sum(cards)
    return total > 21
cards = [10, 5, 7]
result = card_sum(cards)
print(result)

#4
def sum_of_num(s):
    import re
    numbers = re.findall(r'\d+', s)
    total = sum(int(num) for num in numbers)
    return total
input_string = "abc123def45gh6"
result = sum_of_num(input_string)
print(result)

#5
def plus(s):
    if not s:
        return False
    for i in range(len(s)):
        if s[i].isalpha():
            if i == 0 or i == len(s) - 1 or s[i - 1] != '+' or s[i + 1] != '+':
                return False
    return True
input_string = "++a++b++c++"
result = plus(input_string)
print(result)

#6
def time(time_str):
    if 'AM' in time_str or 'PM' in time_str:
        time, period = time_str[:-2], time_str[-2:]
        hours, minutes = map(int, time.split(':'))
        if period == 'AM':
            if hours == 12:
                hours = 0
        else:  # PM
            if hours != 12:
                hours += 12
        return f"{hours:02}:{minutes:02}"
    else:
        hours, minutes = map(int, time_str.split(':'))
        period = 'AM'
        if hours >= 12:
            period = 'PM'
            if hours > 12:
                hours -= 12
        elif hours == 0:
            hours = 12
        return f"{hours}:{minutes:02} {period}"
time_12 = "09:30 PM"
time_24 = "19:20"
print(time(time_12))
print(time(time_24))

#7
def password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char in '!@#$%^&*()-_=+[]{}|;:,.<>?/' for char in password):
        score += 1
    return score
password2 = "pass"
password3 = "P@ssw0rd"
print(password_strength(password2))
print(password_strength(password3))

#8
def rus_number(num):
    if not (0 <= num <= 999):
        raise ValueError("Число должно быть от 0 до 999")
    units = [
        '', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять'
    ]
    teens = [
        'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
        'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать'
    ]
    tens = [
        '', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
        'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто'
    ]
    hundreds = [
        '', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот',
        'шестьсот', 'семьсот', 'восемьсот', 'девятьсот'
    ]
    if num == 0:
        return 'ноль'
    result = []
    if num >= 100:
        result.append(hundreds[num // 100])
        num %= 100
    if num >= 20:
        result.append(tens[num // 10])
        num %= 10
    if num >= 10:
        result.append(teens[num - 10])
        num = 0
    if num > 0:
        result.append(units[num])
    return ' '.join(result).strip()
print(rus_number(123))

#9
def lucky_numbers(n):
    if n % 2 != 0:
        return 0
    half_length = n // 2
    max_sum = 9 * half_length
    dp = [0] * (max_sum + 1)
    dp[0] = 1
    for _ in range(half_length):
        new_dp = [0] * (max_sum + 1)
        for digit in range(10):
            for sum_value in range(max_sum - digit + 1):
                new_dp[sum_value + digit] += dp[sum_value]
        dp = new_dp
    return dp
n = 17
print(lucky_numbers(n)[-1])