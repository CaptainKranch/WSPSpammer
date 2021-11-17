with open("quijote.txt", "r") as file:
    content = file.read()
    var = content.split(" ")
    print(len(var))