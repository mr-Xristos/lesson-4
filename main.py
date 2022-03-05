from number_to_string import get_string_by_number

first_number = input('Введите первое число')
operation = input('ВВедите операцию')
second_number = input('Введите второе число')

#operation = get_string_by_number(operation)

if operation == '+':
    print(get_string_by_number(int(first_number) + int(second_number)))
elif operation == '-':
    print(get_string_by_number(int(first_number) - int(second_number)))
elif operation == '/':
    print(get_string_by_number(int(first_number) / int(second_number)))
elif operation == '*':
    print(get_string_by_number(int(first_number) * int(second_number)))
elif operation == '**':
    print(get_string_by_number(int(first_number) ** int(second_number)))
else:
    print('Вы ввели некоректное значение операции')


