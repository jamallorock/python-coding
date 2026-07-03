def count_status_codes(items):
    counter = {}

    for item in items:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

    return(counter)

def main():
    statuses = [200, 500, 200, 404, 500, 503, 200, 500]
    result = count_status_codes(statuses)
    print(result)

if __name__ == "__main__":
    main()