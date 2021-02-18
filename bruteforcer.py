import os
from pathlib import Path

import requests

def my_function(x):
    symbols = [*range(48, 58), *range(65, 91), *range(97, 123)]
    for s in enumerate(x):
        if symbols[len(symbols) - 1] == symbols[symbols.index(ord(s[1]))]:
            x[s[0]] = chr(symbols[0])
        else:
            x[s[0]] = chr(symbols[symbols.index(ord(s[1])) + 1])
            break
    return "".join(x)


if __name__ == '__main__':
    if os.path.exists("download"):
        print("Image upload folder: " + os.path.abspath("download"))
    else:
        print("Make upload folder")
        Path("download").mkdir(parents=True, exist_ok=True)

    if os.path.exists("last.txt"):
        print("last position in: " + os.path.abspath("download"))
    else:
        print("Make file last.txt")
        fileLast = open("last.txt", "w")
        fileLast.write("00000")
        fileLast.close()

    if os.path.exists("links.txt"):
        print("links in: " + os.path.abspath("download"))
    else:
        print("Make file links.txt")
        file = open("links.txt", "w")
        file.close()

    lastR = open("last.txt", "r")
    links = open("links.txt", "a")
    name = str(lastR.read())

    while True:
        print(name)
        lastW = open(os.getcwd() + "/last.txt", "w")
        lastW.write(name)
        lastW.close()
        url = "https://s.micp.ru/" + name + ".jpg"
        response = requests.get(url)
        if str(response) == '<Response [200]>':
            file = open("download/" + name + ".png", "wb")
            links.write(url + str("\n"))
            file.write(response.content)
            file.close()

        name = my_function(list(name))

        if '00000' == name:
            links.close()
            lastR.close()
            break