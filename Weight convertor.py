weight = float(input("What is your weight ? "))
unit = input("Is it in (K)g or (L)bs ? ")
if unit.upper() == 'K' :
    convert = (weight) * 2.2046
    print(f"Your are {convert} pound ")
else :
    convert = (weight) / 2.2046
    print(f" You are {convert} killo " )
