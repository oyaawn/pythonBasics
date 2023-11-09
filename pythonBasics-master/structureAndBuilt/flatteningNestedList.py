damn=[1,2,[3,4,[5,6],7],8]
record=[]

def listFlat(damn, record):
    for i in damn:
        if isinstance(i, list):  # Using isinstance() instead of type() because it can handle inherited classes. isinstance function returns boolean
            listFlat(i, record)
        else:
            record.append(i)
    return record

print(listFlat(damn, record)) 