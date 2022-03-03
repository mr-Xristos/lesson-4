#translate = {1 : 'один', 2 : 'два', 3 : 'три', 4 : 'четыре', 5 : 'пять'}

first_number = input('Введите первое число')
operation = input('ВВедите операцию')
second_number = input('Введите второе число')
if operation == '+':
    print(int(first_number) + int(second_number))
elif operation == '-':
    print(int(first_number) - int(second_number))
elif operation == '/':
    print(int(first_number) / int(second_number))
elif operation == '*':
    print(int(first_number) * int(second_number))
elif operation == '**':
    print(int(first_number) ** int(second_number))