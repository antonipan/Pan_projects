import random


def input_text():
    msg = input()
    return msg

def random_joke():
    with open('zodiac.txt', 'r') as data:
        somelist = list(data.readlines())
        some_el = somelist[random.randint(0, len(somelist)-1)]
        some_el = some_el.rstrip('\n')
        print(some_el)
random_joke()
