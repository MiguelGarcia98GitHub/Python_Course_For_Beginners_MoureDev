# Lists

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))
print(my_list[0])

my_other_list = [35, 1.77, "Brais", "Moure"]

print(type(my_list))
print(type(my_other_list))
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list.count("Brais"))
print(my_other_list.count("Chinchilla"))

print(my_list + my_other_list)

print(type([1,2,3,4]))

my_list = ["Paco", 1.70, 60]
my_list.append("Hola")
print(my_list)
my_list.insert(0, "Test")
print(my_list)
my_list.remove("Test")
print(my_list)
my_list.pop()
print(my_list)
print(my_list.pop())
print(my_list)
my_list.pop(1)
print(my_list)
del(my_list[0])
print(my_list)
my_list = ["Paco", 1.70, 60]
print(my_list)
my_list.clear()
print(my_list)
my_list = ["Paco", 1.70, 60]
new_list = my_list.copy()
my_list.clear()
print(new_list)
new_list.reverse()
print(new_list)
letters_list = ["G", "U", "A", "D"]
letters_list.sort()
print(letters_list)
ints_list = [50, 20, 30, 70]
ints_list.sort()
print(ints_list)
sub_list = ints_list[0:2]
print(sub_list)