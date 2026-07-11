def read_file(filename):
    with open(filename, "r") as file:
        return file.read()

def main():
    filename = "test.txt"
    content = read_file(filename)
    print(content)

if __name__ == "__main__":
  main()