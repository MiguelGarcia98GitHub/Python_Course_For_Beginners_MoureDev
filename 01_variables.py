# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)

# Algunas Funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", "MoureDev", 35
print(name, surname, age, alias)

# Pedir datos al usuario por consola
"""
 first_name = input("¡Cuál es tu nombre? ")
 age = input("¿Cuantos años tienes? ")
 print(first_name)
 print(age)
"""


name = 35
age = "Brais"
print(name)
print(age)


# Forzamos el tipo
address: str = "Mi dirección"
address = 32;
print(address)