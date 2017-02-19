data1 = 'This is the first line.'


def write_to_file(data):
    file = open('testfile.txt', 'a')
    file.write(data1 + ' \n')
    print('The information was successfully added.')
    file.close()


def read_file_data():
    file = open('testfile.txt', 'r')
    for item in file:
        print(item)


if __name__ == '__main__':
    write_to_file(data1)
    read_file_data()
