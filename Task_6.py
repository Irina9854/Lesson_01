#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
#*Пример:*
#385916 -> yes
#123456 -> no

x = list(map(int, list(input("Введите номер билета: "))))
if len(x) != 6:
    print("Вы ввели неверное число")
else:
    left = sum(x[0:-3])
    right = sum(x[-3:])
    if left == right:
       print("yes")
    else:
       print("no")