while True:
    filename = input("filename: ")
    if filename == "exit":
        quit()
    try:
        file = open(filename, "r")
        for line in file:
            print(line.rstrip().upper())
    except FileNotFoundError:
        print("Can't find file in current directory")