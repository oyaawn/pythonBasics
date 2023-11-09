damn=[1,2,[3,4,[5,6],7],8]

def listFlat(damn):
    for i in damn:
        if type(i) == list:
            listFlat(i)
        else:
            print(i)

listFlat(damn)
