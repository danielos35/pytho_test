a = 1992
c = 18.8


def bici(year):
    first = year/4
    intFirst = int(first)

    second = year/100
    intSecond = int(second)

    third =year/400
    intThird = int(third)



    if first - intFirst == 0 and third - intThird ==0:
        print(True)
    elif second - intSecond == 0 :
        print(False)


bici(a)















