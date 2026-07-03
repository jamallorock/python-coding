def sum5xx(items):
    count = 0

    for item in items:
        if item >= 500:
            count += 1
            #counter.append(item)
            #if item in counter:
            #    counter[item] += 1
            #else:
            #    counter[item] = 1

    return(count)

def main():
    statuses = [200, 500, 404, 503, 301, 502]
    result = sum5xx(statuses)
    print(result)

if __name__ == "__main__":
    main()