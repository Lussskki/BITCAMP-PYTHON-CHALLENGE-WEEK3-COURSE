name = input("What's your name? ")

with open("saved-properties.txt", "a") as file:
    file.write(f"{name} \n")