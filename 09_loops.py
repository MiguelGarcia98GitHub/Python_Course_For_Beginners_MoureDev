# Loops
 
# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print("Mi condicion es mayor o igual que 10")


my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)
    print(f"This element is: {element}")


my_dict_values = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

for key in my_dict_values:
    print(f"The key is {key}");
    if key == "Edad":
        # break
        continue
    else:
        print("Se ejecuta")
else:
    print("El bucle for del diccionario ha finalizado")
