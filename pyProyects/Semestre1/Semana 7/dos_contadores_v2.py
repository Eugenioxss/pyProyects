def main():
    a=int(input("A value: "))
    b=int(input("B value: "))
    for i in range (b, 0, -1):
        print(a, i)
        a+=2

main()