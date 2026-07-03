def duplicateDetector(items):
    seen = set()
    for item in items:
        if item in seen:
            return True

        seen.add(item) 
    return False

def main():
    items = ["Aga","Agata","Adam","Artur"]
    result = duplicateDetector(items)
    print(result)

if __name__ == "__main__":
    main()