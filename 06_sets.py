# Sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_set = {"Pepe", "Gutierrez", 40}
my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set))

print(len(my_other_set))

print(my_other_set)

my_other_set.add("MoureDev")

print(my_other_set)

print("Moure" in my_other_set)
print("Mouri" in my_other_set)

my_other_set.remove("Moure")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

my_other_set.update(my_set)
print(my_other_set)

my_set = {"Brais", "Moure", 35}
my_list = list(my_set)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_new_set))
print(my_new_set.difference(my_set))
