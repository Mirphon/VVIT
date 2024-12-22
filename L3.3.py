def Book(file_name, type):
    if type == 'line':
        try:
            file = open(file_name, 'r')
            for l in file:
                print(l)
                input()
        except FileNotFoundError:
            print('Леееее, файла не такого!!!')
    if type == 'all':
        try:
            ff = open(file_name, 'r')
            print(ff.read())
        except:
            print('Кого ты открываешь, открывашка?')
Book('Example.txt', 'line')