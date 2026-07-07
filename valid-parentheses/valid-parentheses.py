def is_valid_parentheses(s):
    stack = []
    pairs = {
       "}" : "{",
       ")" : "(",
       "]" : "["
    }


    for char in s:
        if char in "([{":
            stack.append(char)
            #print(stack)
        elif char in pairs:
            print(pairs[char])
            if not stack:
                return False
            last_open = stack.pop()
            if last_open != pairs[char]:
                return False

    return len(stack) == 0

def main():
    s = "()[]{}"
    result = is_valid_parentheses(s)
    print(result)

if __name__ == "__main__":
  main()