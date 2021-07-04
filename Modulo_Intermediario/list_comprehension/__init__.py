
l1 = [1,2,3,4,5,6,7,8,9]
#ex3 = [(v, v2) for v in l1 for v2 in l1] # realizando dois for em uma linha
#ex3 = [(v, v2) for v in l1 for v2 in range(3)] # realizando dois for em uma linha
#print(ex3)
print()
l2 = []
c = 0
for v in l1:
    for v2 in l1:
        ex = (v, v2)
        l2.insert(c, ex)
        c += 1
print(l2)





