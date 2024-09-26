def main():
    neg=""
    numint=int(input("Ingresa tu numero: "))
    if(numint<0):
        numint=0-numint
        neg="-"
    num=str(numint)
    num_len=len(num)
    numalr=""
    if num_len>7:
        print("Numero demasiado largo")
    else:
            numalr=num[::-1]
    print(neg+numalr)
main()