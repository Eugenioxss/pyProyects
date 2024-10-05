def main():
    palindrome=input("Type a palindrome here: ")
    palindrome=palindrome.replace(" ","")
    palindrome=palindrome.lower()
    num_let=len(palindrome)

    alreves=palindrome[::-1]
 
    if palindrome==alreves:
        print("Your text is a palindrome")
    else:
        print("Your text is not a palindrome")


main()