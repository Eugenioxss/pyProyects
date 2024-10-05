def equilibrio(str1,str2):
    for i in str1:
        if i not in str2:
            return "No equilibrio"
        else:
            return "Si equilibrio"

def main():
    str1=input("Dame el str1: ")
    str2=input("Dame el str2: ")
    print(equilibrio(str1,str2,))

main()