def swapFileData():
    fileName=input("Enter file name: ")
    file1 = "text1.txt"
    file2 = "text2.txt"
    with open(file1, 'r') as a:
        data_a = a.read()
    with open(file2, 'r') as a:
        data_b = a.read()
    with open(file1,'w') as a:
        a.write(data_b)
    with open(file2,'w') as a:
        a.write(data_a)
    if(fileName == file1):
        print(data_b)
    if(fileName == file2):
        print(data_a)
swapFileData()