weight = float(input("How much do you weigh?: "))
unit = input("Is that in K(g) or (L)bs?")

if unit.upper() == "K":
    converted = weight / .45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * .45
    print("In Kilograms, you weigh: " + str(converted))

print("Have a nice day")