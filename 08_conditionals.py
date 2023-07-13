# Conditionals

my_condition = True


if my_condition:
    print("Se ejecuta la condición del primer if")

my_condition = 5 * 2

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

if my_condition >= 10:
    print("Tercer if")

if my_condition > 10:
    print("Es mayor que 10")
else:
    print("Es menor o igual que 10")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor o igual a 10 o mayor o igual a 20")



if my_condition != 9:
    print("No es 9")


if my_condition == 4:
    print("Es un 4")
elif my_condition == 3:
    print("Es un 3")
else: print("No es ni 3 ni 4")


if 0:
    print("Condition: 0")

if 1:
    print("Condition 1")

if 2:
    print("Condition 2")

if "":
    print("Condition string vacío")

if "a":
    print("Condición string con contenido")

if not 0:
    print("Condicion no es 0")