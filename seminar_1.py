# №1 За день машина проезжает N км. Сколько дней необходимо, чтобы проехать M км. n = 700, m = 150
import math
# n = 700
# m = 750
# print(math.ceil(m/n))

# №2 Сумма цифр трехзначного числа
# n = 123
# a = n//100
# b = (n%100)//10
# c = n%10
# res = a+b+c
# print(res)

# №3 В школе решили набрать 3 новых матем. класса и оборудовать кабинеты партами. За каждой
# партой может сидеть два ученика. Известно количество учеников в каждом классе. Какое мин.
# количество парт необходимо преобрести.

# a = int(input("Укажите количество учеников в классе А: "))
# b = int(input("Укажите количество учеников в классе Б: "))
# c = int(input("Укажите количество учеников в классе В: "))
# print(math.ceil((a+b+c)/2))

# №4 Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.

# n = 60
# x = n/3
# p = int(x/2)
# k = int(x*2)
# print(p," ",k," ",p)

# Вам требуется написать программу, которая проверяет счастливость билета с номером n
# и выводит на экран yes или no.

# n = 385915
# a = n//100000
# b = n//10000%10
# c = n//1000%10
# d = n//100%10
# e = n//10%10
# f= n%10
# if a+b+c == d+e+f:
#     print("yes")
# else:
#     print("no")

# Определите, можно ли от шоколадки размером a × b долек отломить c долек, если
# разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

a = 15
b = 7
c = 14
if c%a == 0 or c%b == 0:
    print("yes")
else:
    print("no")