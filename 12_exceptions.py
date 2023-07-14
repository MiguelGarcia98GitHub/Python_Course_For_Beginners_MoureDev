# Exception Handling

numberOne = 5
numberTwo = 1
numberTwo = "1"

# try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

# try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:
    print("Esto se ejecutará siempre")


# Errores

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:  # solo si existe un error de tipo, sino especificamos es para cualquier error
    print("Se ha producido un TypeError")


# Obtenemos información del error

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError as e:
    print(e)
