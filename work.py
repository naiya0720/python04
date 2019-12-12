
y = 1
while y <= 9:
    z = 1
    while z <= y:
        print("%d * %d = %d" % (z, y, z * y), end="\t")
        z += 1
    print()
    y += 1


