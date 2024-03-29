# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

Number = int(input('Введите шестизначный номер билета: '))

if Number < 100000 or Number > 999999:
    print('Это число не является шестизначным, попробуйте еще раз')
else:

    First = int(Number//1000)
    Second = int(Number % 1000)

    if First % 10 + First//100 + First//10 % 10 == Second % 10 + Second//100 + Second//10 % 10:
        print("Твой билет - СЧАСТЛИВЫЙ! Скорее съешь его!")
    else:
        print("Этот билет не счастливый, лучше не ешь :(")
