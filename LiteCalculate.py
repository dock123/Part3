print("Для выхода из программы введите 'exit'")
while True:
    # первая переменная
    print("Первая переменная:")
    A = int(input())

    # вторая переменная
    print("Вторая переменная:")
    B = int(input())

    arifm=input(print("Введите арифметический знак (*,/,+,-)"))
    if arifm == "exit":
        break
    if arifm in("+","-","*","/"):
        if arifm == "+":
            print(" Ответ = ", A + B)
        elif arifm == "-":
            print(" Ответ = ", A - B)
        elif arifm == "*":
            print(" Ответ = ", A * B)
        elif arifm == "/":
            if B != 0:
                print(" Ответ = ", A / B)
            else:
                print("ERROR")
    else:
        print("ERROR")



