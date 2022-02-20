### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

# duraction = int(input('Введите любое колличество секунд от 1 до ... '))
# sec = duraction % (24 * 3600)
# hour = sec // 3600
# sec %= 3600
# min = sec // 60
# sec %= 60
# day = duraction // 86400
# if duraction < 60:
#     print(duraction, 'сек')
# elif duraction > 60 and duraction < 3600:
#     print(min, 'мин', sec, 'сек')
# elif duraction > 3600 and duraction < 86400:
#     print(hour, "час", min, 'мин', sec, 'сек')
# else:
#     print(day, 'дн', hour, 'час', min, 'мин', sec, 'сек')


### 2.
# a) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
# будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

# my_list = []
# num = 1
# while num <= 1000:
#     my_list.append(num ** 3)
#     num += 2
#
# # a. не получилось решить самостоятельно
# final_sum = 0
# for num in my_list:
#     check_sum = 0
#     for check_num in str(num):
#         check_sum += int(check_num)
#     if check_sum % 7 == 0:
#         final_sum += num
# print(final_sum)
#
# # b.c.
# final_sum = 0
# for num in my_list:
#     num += 17
#     check_sum = 0
#     for check_num in str(num):
#         check_sum += int(check_num)
#     if check_sum % 7 == 0:
#         final_sum += num
# print(final_sum)


### 3. Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

# num = int(input('Введите число процента от 1 до 100: '))
# if 4 < num % 100 <= 20:
#     print(num, 'процентов')
# elif num % 10 == 1:
#     print(num, 'процент')
# elif 1 < num % 10 < 5:
#     print(num, 'процента')
# else:
#     print(num, 'процентов')