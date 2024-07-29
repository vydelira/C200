def estPopSize(t1, c, t2):
    estPopSize = ((t1 * c)/t2)
    return estPopSize

LifeData = [["Bison", 20, 10, 2], ["Wolf", 10, 15, 4], ["Prairie Dog", 15, 15, 1], ["Mountain Lion", 10, 8, 1]]

for d in LifeData:
    print(d[0] + " estimated population size= " + str(estPopSize(d[1], d[2], d[3])))
