# WAP to create a dictionary and display keys and values
d = {
    "Apple": 1,
    "Banana": 2,
    "Orange": 3
}
print(d)
print(type(d))
for key, value in d.items():
    print(key, ":", value)
