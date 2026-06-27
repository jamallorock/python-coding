import os
import sys


def frequency_counter(items):
    counts = {}
    for item in items:
      if item in counts:
          counts[item] += 1
      else:
          counts[item] = 1
    return(counts)



def main():
    #items = ["error", "info", "error", "warning", "info", "error","info","info","info","info","info"]
    items = [200, 500, 200, 404, 500, 503, 200, 500]
    result = frequency_counter(items)
    print(result)

if __name__ == "__main__":
    main()