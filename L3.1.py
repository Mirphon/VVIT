def Book(file_name, type):
    if type == 'line':
        file = open(file_name, 'r')
        for l in file:
            print(l)
            input()
    if type == 'all':
        ff = open(file_name, 'r')
        print(ff.read())
Book('Example.txt', 'all')
