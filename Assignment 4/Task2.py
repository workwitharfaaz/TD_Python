with open("output.txt", "w") as f:
    content = input("Enter text to write to the file: ") + "\n"
    f.write(content)
    print("Data successfully written to output.txt.\n")
with open("output.txt", "a") as f:
    a_content = input("Enter additional text to append: ") + "\n"
    f.write(a_content)
    print("Data successfully appended.\n")
with open("output.txt", "r") as f:
    print(f"Final content of output.txt:")
    for line in f:
        print(line.strip())