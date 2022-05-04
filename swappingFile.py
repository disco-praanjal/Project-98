def swapFileData():
    file =  input("Enter the file name:- ")

    data_a = open(file,'w')
    data_b = open(file,'w')

    with open(file, 'r') as a:
    data_a = a.read()

    with open(file, 'w') as a:
    a.write(data_b)

countWordsFromFile()
