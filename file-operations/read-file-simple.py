

def read_file(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()

    return content


def main():
    file = "test.txt"
    result = read_file(file)
    print(result)

if __name__ == "__main__":
    main()
