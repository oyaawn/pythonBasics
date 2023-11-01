x=0

def func1():
    global x
    print('we are finished')
    x+=1
    if(x>10):
        exit()
    func1()


func1()

