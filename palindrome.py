import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards

if __name__ == "__main__":

    n = "Was it a cat I saw?"
    if(is_palindrome(n)):
        print("This is a plaindrome.")
    else:
        print("This is not a palindrome. Try Again.")
        
    
