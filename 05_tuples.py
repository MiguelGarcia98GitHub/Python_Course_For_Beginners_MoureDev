# Tuples

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure")
my_other_tuple = (35, 60, 30)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Moure"))
print(my_tuple.index("Brais"))


my_sum_tuple = my_tuple + my_other_tuple

print(my_sum_tuple)
print(type(my_sum_tuple))
print(my_sum_tuple[2:4])

my_sum_tuple = list(my_sum_tuple)
print(my_sum_tuple)
print(type(my_sum_tuple))

del my_tuple
print(my_tuple)
