word = input("Please, type a word: ")
def palindromeOrNot(word = ""):   
    if word:
        i = 0
        j = len(word) - 1
        isPalindromeFound = False
        while not isPalindromeFound:
            if word[i] == word[j]:
                i += 1
                j -= 1
            elif word[i] != word[j]:
                print("Your word is not palindrome.")
                isPalindromeFound = True
            if i == j:
                print("Your word is palindrome.")
                isPalindromeFound = True   
    else:
        print("You haven't typed a word.")
palindromeOrNot(word)
input("Press Enter to close the program...")


