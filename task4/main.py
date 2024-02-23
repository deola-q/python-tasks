# 9. (*) Написать функцию представления числа (до миллиона включительно) в виде строки.

do20 = [
    "", "один ", "два ", "три ", "четыре ", "пять ", "шесть ",
    "семь ", "восемь ", "девять ", "десять ", "одиннадцать ", "двенадцать ",
    "тринадцать ", "четырнадцать ", "пятнадцать ", "шестнадцать ",
    "семнадцать ", "восемнадцать ", "девятнадцать "
]
tenths = [
    "", "", "двадцать ", "тридцать ", "сорок ", "пятьдесят ",
    "шестьдесят ", "семьдесят ", "восемьдесят ", "девяносто "
]
hundredths = [
    "", "сто ", "двести ", "триста ", "четыреста ", "пятьсот ", "шестьсот ", "семьсот ",
    "восемьсот ", "девятьсот "
]
addWords = [
    "миллион ", "тысяч"
]


def convert_to_digit(n, suffix):
    if n == 0:
        return ""
    elif n <= 19:
        return do20[n] + suffix
    elif n < 100 and n % 10 != 0:
        return tenths[n // 10] + do20[n % 10] + suffix
    elif n < 100:
        return tenths[n // 10] + suffix
    elif (n < 1000) and (n % 100 <= 19) and (n % 100 >= 10):
        return hundredths[n // 100] + do20[n % 100] + suffix
    elif (n < 1000) and (n % 100 != 0):
        return hundredths[n // 100] + tenths[(n // 10) % 10] + do20[n % 10] + suffix
    else:
        return hundredths[n // 100] + suffix


def convert(n: int):
    if n == 0:
        return "Ноль"
    else:
        millions = convert_to_digit(n // 1000000, addWords[0])
        # миллионные доли в числе
        thousand = convert_to_digit((n // 1000) % 1000, addWords[1])
        if for_thous(n):
            thousand = thousand.replace('один', 'одна')
            thousand = thousand.replace("два", "две")
        hundredths = convert_to_digit(n % 1000, "")
        converted_number = millions + thousand + suffix_thous((n / 1000) % 1000) + hundredths
    # inter_answer = converted_number[0].rstrip()
    return converted_number.strip().capitalize()


def suffix_thous(number):
    if (number % 10 == 1) and (number % 100 != 11):
        return "a "
    elif (number % 100 >= 11) and (number % 100 <= 20):
        return " "
    elif (number % 10 >= 2) and (number % 10 <= 4):
        return "и "
    else:
        return " "


def for_thous(n):
    c = (n / 1000) % 1000
    return (c % 10 == 1 or c % 10 == 2) and c % 100 != 11


def test_function():
    with open('input4.txt', 'r') as f:
        num = int(f.readline())
        answer = convert(num)

    with open('output4.txt', 'w', encoding='utf-8') as f:
        f.write(answer)
