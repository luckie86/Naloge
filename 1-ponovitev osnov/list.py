list = [32, 81, 43, 16, 72, 99, 14, 50]

def min(list):
    x = 100
    for i in list:
        if i < x:
            x = i
    print x

min(list)


def max(list):
    x = 1
    for i in list:
        if i > x:
            x = i
    print x

max(list)

def average(list):
   listsum = sum(list)
   listlen = len(list)
   avg = listsum/listlen
   print avg

average(list)


def suma(list):
    suma = 0
    for x in list:
        suma += x
    print suma


suma(list)