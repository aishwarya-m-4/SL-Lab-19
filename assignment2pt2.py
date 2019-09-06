dist={
    1:"Sam",
    2:"Ram",
    3:"John",
    4:"Candy",
    5:"Gale",
    6:"Ames"
}

for i in dist.keys():
    if(i%2==0):
        print(dist.get(i))
