import os

from pip._vendor import requests


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
    lastR = open(os.getcwd() + "/grabber/last.txt", "r")
    links = open(os.getcwd() + "/grabber/links.txt", "a")
    name = str(lastR.read())

    while True:
        print(name)
        lastW = open(os.getcwd() + "/grabber/last.txt", "w")
        lastW.write(name)
        lastW.close()
        url = "https://s.micp.ru/" + name + ".jpg"
        response = requests.get(url)
        if str(response) == '<Response [200]>':
            file = open(os.getcwd() + "/grabber/download/" + name + ".png", "wb")
            links.write(url + str("\n"))
            file.write(response.content)
            file.close()

        name = my_function(list(name))

        if '00000' == name:
            links.close()
            lastR.close()
            break