files = open("files.txt", mode="r+")
lister = []
for one in files.readlines():
    if "\n" in one:
        one = one[0:-1]
    lister.append(one)
print(lister)
for line in files.readlines():
    lister.append(line)
print(lister)
for object in lister:
    openobj = open(object, mode="w+")
    openobj.write(f"{lister.index(object)}")
    openobj.close()
    print(f"{object} created")
files.close()