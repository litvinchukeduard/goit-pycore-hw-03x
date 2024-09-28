'''

В нас є список з чисел. [1, 2, 3, 4, 5, 6, 7, 8]

ПОтрібно написати функцію, яка буде перебирати усі числа у списку та виводити лише парні числа

2, 4, 6, 8
'''

lst = [1, 2, 3, 4, 5, 6, 7, 8]

# Ctrl l

"""
1. Створити функцію
2. Створити цикл for
3. Обмежити числа на парні
"""

def print_even_numbers(number_list):
    ''' Функція, чка виводить лише парні числа'''
    # pass
    for number in number_list:
        if number % 2 == 0:
            print(number)


print_even_numbers([1, 2, 3, 4, 5, 6, 7, 8])



# def other_function():
#     ...

# print_even_numbers() (Ctrl /) (Command /)


# print(6 % 2)