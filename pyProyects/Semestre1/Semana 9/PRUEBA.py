s="MCM"

a = list(s)
tot = 0
b = ["M","D","C","L","X","V","I"]
for x in range (0,8):
        numsito = b[x]
        cuentin = a.count(numsito) 
        print(a.index(numsito))