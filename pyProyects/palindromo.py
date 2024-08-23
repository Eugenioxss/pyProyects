palindrome=input("Type a palindrome here: ")
palindrome=palindrome.replace(" ","")
palindrome=palindrome.lower()
num_let=len(palindrome)

precheck=""
check=""

def full_check(pl,pre,num,chk):
    pre=pl[num:num+1]
    num-=1
    chk=chk+pre
    pre=chk
    return pl,pre,num,chk

while num_let>-1:
    palindrome,precheck,num_let,check=full_check(palindrome,precheck,num_let,check)
    
if num_let==-1 and palindrome==check:
    print("Your text is a palindrome")
elif num_let==-1 and palindrome!=check:
    print("Your text is not a palindrome")
