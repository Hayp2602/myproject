lang = 'EN'
lang_opt = input('Enter L to change language or other key to continue:  ')
while lang_opt == 'l':
    if lang == 'RU':
        lang = 'EN'
        lang_opt = input('Enter L to change language or other key to continue:  ')
    else:
        lang = 'RU'
        lang_opt = input('Введите L, чтобы сменить язык, или любую клавишу, чтобы продолжить:  ')
if lang == 'EN':
    f = 'Enter first number:  '
    o = 'Enter operation (+,-, /, *):  '
    s = 'Enter second number:  '
    r = 'Result: '
    e = 'Error'
    v = 'Enter "yes" to continue and other key to finish:  '
if lang == 'RU':
    f = 'Введите первое число:  '
    o = 'Введите операцию (+,-, /, *):  '
    s = 'Введите второе число:  '
    r = 'Результат: '
    e = 'Ошибка'
    v = 'Введите "yes", чтобы продолжить, и любую клавишу, чтобы закончить:  '
prodolzhit = 'yes'
while prodolzhit == 'yes':
    f_num = float(input(f))
    oper = input(o)
    sec_num = float(input(s))
    if oper == '+':
        print(r, f_num + sec_num)
    elif oper == '-':
        print(r, f_num - sec_num)
    elif oper == '/':
        print(r, f_num / sec_num)
    elif oper == '*':
        print(r, f_num * sec_num)
    else:
        print(e)
    prodolzhit = input(v)