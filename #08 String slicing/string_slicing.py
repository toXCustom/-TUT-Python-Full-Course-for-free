# slicing = creat a substring by extracting elements from another string
#           indencing[] or slice()
#           [start:stop:step]

name = "Pawel Mroz"

first_name = name[0:5]
last_name = name[6:10]
funky_name = name[0:8:2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)

print(website1[slice])
print(website2[slice])