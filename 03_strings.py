my_new_line_string = "Este es un string \ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un string \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es " + name + " " + surname + "y mi edad es" + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(d)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:2]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:4]
print(language_slice)

# Reserve

reverse_language = language[::-1]
print(reverse_language)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print("1.07".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.lower().isupper())
print(language.capitalize().isupper())
print(language.startswith("Pyth"))


