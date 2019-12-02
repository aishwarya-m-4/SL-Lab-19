# Menu driven program to convert degree F to degree C or vise versa and save it as list of tuples

temps = []


def CtoF():

    temp = int(input("Enter the temperature "))
    f = (temp*9/5) + 32
    val = (str(temp)+"C", str(f)+"F")
    temps.append(val)
    print(temp, "degree C = ", f, "degree F")


def FtoC():

    temp = int(input("Enter the temperature "))
    c = (temp - 32) * 5/9
    val = (str(temp)+"F", str(c)+"C")
    temps.append(tuple(val))
    print(temp, "degree C = ", c, "degree F")


while True:
    option = input(
        "\ni)Enter C to enter temperature in Celsius\nii)Enter F to enter temp in Farenheit\niii)Enter P to view all conversions\niv)Enter 0 to quit: ")
    # compute(option)
    if option == "C":
        CtoF()
    elif option == "F":
        FtoC()
    elif option == "P":
        print(temps)
    elif option == "0":
        exit()
    else:
        print("Invalid input")
