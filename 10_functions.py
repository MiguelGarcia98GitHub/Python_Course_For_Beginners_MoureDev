# Funciones

def my_function ():
    print("Esto es una función")

my_function()
my_function()
my_function()

def sum_two_values (first_value, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)

def sum_two_values_with_return (first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10, 5)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name("Brais", "Moure")
print_name(surname="Moure", name="Brais")

def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure", "MoureDev")

def print_texts(*texts):
    for text in texts:
        print(text.upper())

print_texts("Hola", "Python", "MoureDev")