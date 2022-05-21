#križić i kružić

go = 0

red = [" "," "," "," "," "," "," "," "," "]

potez = int(input("Na koju poziciju želite staviti x?"))

while go != 1:

    potez = int(input("Na koju poziciju želite staviti x?"))

    if red[potez-1] == " ":
        red[potez-1] = "x"
        go = 1

    else:
        print("Ovo polje je već zauzeto")

print(red[0:3])
print(red[3:6])
print(red[6:])
