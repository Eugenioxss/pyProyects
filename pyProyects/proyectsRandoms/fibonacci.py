def main():
    fibolist=[1,1]
    numi=int(input("Dame un número: "))
    if numi == 1:
        print(fibolist.pop(-1))
    elif numi == 2:
        print(fibolist)
    else:
        for i in range (2,numi):
            fibolist.append(fibolist[-1]+fibolist[-2])
        print(fibolist)

main()