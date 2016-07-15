my_file = input("Enter a file within the current directory: ")
try:
    fhand = open(my_file)
except:
    print("bad file name")
else:
    for line in fhand:
        if line.startswith("From:"):
            print(line.rstrip())
