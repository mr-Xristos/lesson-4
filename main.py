from num2words import num2words

number_operation = 'y'
number = 0

while number_operation == 'y':
    number +=1

    try:
        first_number = float(input("Введите первое число цифрой: "))
    except:
        print("нужно вводить цифру")

    operation = input('ВВедите операцию')

    try:
        second_number = float(input("Введите второе число цифрой: "))
    except:
        print("нужно вводить цифру")



    if operation == '+':
        print(num2words(float(first_number) + float(second_number)))
    elif operation == '-':
        print(num2words(float(first_number) - float(second_number)))
    elif operation == '/':
        if second_number == 0:
            print('не дели на ноль')
        else:
            print(num2words(float(first_number) / float(second_number)))
    elif operation == '*':
        print(num2words(float(first_number) * float(second_number)))
    elif operation == '**':
        print(num2words(float(first_number) ** float(second_number)))
    else:
        print('Вы ввели некоректное значение операции')

    print(" Количество совершенных операций : " + str(number))
    chois = None;
    while chois != "yes" or "no":
        chois = input(" Желаете продолжить? (yes or no) \n : ")
        if chois == "yes":
            break
        elif chois == "no":
            print(" спасибо что выбрали нас ")
            break
        else:
            print(" введите yes или no ")
    if chois == "yes":
        continue
    if chois == "no":
        break


