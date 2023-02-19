import os

def load():

    placement = []
    in_score = False
    with open("./resources/Records/Records.txt", "r") as file:      # we read everything if in our txt file
        data = file.read()

    if data != '':                                                  # we check that data != 0

        n = ['', '']
        for letter in data:                                         # we iterate over all the data
            if letter != '-':                                       # and we separate the numbers if there is a '-'
                if letter == ':':
                    in_score = True
                    continue

                if in_score:
                    n[1] += str(letter)
                else:
                    n[0] += str(letter)

            else:
                in_score = False
                placement.append(n)                                 # if next letter is '-' than we add it as an entry
                n = ['', '']                                        # into placement

    return placement


def in_tt(score):
    placement = load()
    if len(placement) < 20:
        return True

    for s, place in enumerate(placement):
        if place[1] < score:
            if s < 20:
                return True
            break
    return False


def save(score, name):
    placement = load()

    for s, place in enumerate(placement):

        if int(place[1]) < score:
            placement.insert(s, [str(name), str(score)])
            break

    if len(placement) == 0:
        placement.append([str(name), str(score)])

    os.remove('./resources/Records/Records.txt')

    with open('./resources/Records/Records.txt', 'w') as file:
        for place in placement:
            file.write(str(place[0]) + ':' + str(place[1]) + '-')

    return
