def adi():

    temps = []

    origTemps = []

    amount = int(input("please enter amount of temps: "))

    for i in range(amount):

        temp = int(input(f"please enter the {i+1} temp: "))

        origTemps.append((temp))

        temps.append(abs(temp))

    mostCloseToZero = min(temps)

    posit = origTemps.count(mostCloseToZero)

    neg = origTemps.count(-mostCloseToZero)

    if posit != 0 :

        if neg != 0:

            return(mostCloseToZero , -mostCloseToZero)  

    else:

        return(-mostCloseToZero)

   

    return(mostCloseToZero)

    print("error you are stupid")


print(adi())