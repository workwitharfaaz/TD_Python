try:
    with open("sample.txt", "rt") as f:
        print(f"Reading file content: ")
        n = 0
        for line in f:
            n += 1
            print(f"Line {n}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")