def only_5xx(items):
    counter = []

    for item in items:
        if item >= 500:
            counter.append(item)
            #if item in counter:
            #    counter[item] += 1
            #else:
            #    counter[item] = 1

    return(counter)

def main():
    statuses = [200, 500, 404, 503, 301, 502]
    result = only_5xx(statuses)
    print(result)

if __name__ == "__main__":
    main()