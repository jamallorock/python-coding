def print_last_n_line(filename,n):
   with open(filename, "r") as file:
      lines = file.readlines()
      for line in lines[-n:]:
         print(line, end="")
    


def main():
    filename = "test.txt"
    content = print_last_n_line(filename,3)
    print(content)

if __name__ == "__main__":
  main()