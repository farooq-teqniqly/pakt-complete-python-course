
try:
    while True:
        content = input("Enter some text (CTRL + C then ENTER to quit): ")

        with open("data.txt", "a+") as writer:
            writer.write(content + "\n")

        with open("data.txt", "r") as reader:
            print(reader.read())
except KeyboardInterrupt:
    print("Goodbye.")


