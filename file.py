# Добавляем новые строки кода

lst = [i for i in range(10)]
print(lst)

def factorial(n):
    if n < 0:
        return "Факториал отрицательного числа не определен."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Приводим к нижнему регистру и убираем пробелы
    return s == s[::-1]  # Сравниваем строку с её обратной версией
