def square(values):
    if values != []:
        temp = values[0]
        values[0] = 0

    for i in range(1, len(values)):
        print(temp)
        sub = values[i]
        values[i] = temp ** 2
        temp = sub
    return values

values=[1,2,3,4]

print(square(values))

        