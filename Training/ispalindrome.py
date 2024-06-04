batata = input("Put something here to check if it's palindrome: ")
def ispalindrome(var):
    if var == var[::-1]:
        return True
    else:
        return False

print(ispalindrome(batata))