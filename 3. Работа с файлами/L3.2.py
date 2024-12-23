def file(name, type):
    user_text = input()
    if type == 'new':
        f = open(name, 'w')
        f.write(user_text)
        f.close()
    if type == 'old':
        f = open(name, 'a')
        f.write(user_text)
        f.close()
file('user_input.txt', 'old') #дозапись в файл
file('t.txt', 'new') #оздает новый файл или очищает прошлый и вписывает текст