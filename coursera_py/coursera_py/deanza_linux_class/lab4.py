# Name: Gregory Tuayev-Deane   
# Description: File contains two functions:
# 1. is_palindrome to check whether a given word is a palindrome
# 2. rotate_list to rotate the elements of a list to the right by 1 position

ASCII_A = 65
ASCII_Z = 90
ASCII_A_LOWER = 97
ASCII_Z_LOWER = 122

#function to check whether a character is alphabetic
def is_alphabetic(ch:str) -> bool:
    if (ord(ch)<ASCII_A) or (ord(ch)>ASCII_Z and ord(ch)<ASCII_A_LOWER) or (ord(ch)>ASCII_Z_LOWER):
        is_alphabetic = False
    else:
        is_alphabetic = True
    return is_alphabetic


def is_palindrome(word:str) -> bool:
    #convert all to lower, remove non alpha char's
    #reverse word and then compare to original
    print("_________IS PALINDROME__________")
    print("Input string: ", word)
    word_lower = word.lower()
    word_alphabetic_mask = [is_alphabetic(char) for char in word_lower]
    print("Alpha char boolean mask: ",word_alphabetic_mask)
    final_word = [w for w,wm in zip(word_lower,word_alphabetic_mask) if wm]
    print("Final word: ", final_word)
    reverse_word = final_word[::-1]
    print("Reverse word: ", reverse_word)
    if reverse_word == final_word:
        is_palindrome = True
        print("You entered a palindrome!")
    else:
        is_palindrome = False
    return is_palindrome
    

is_palindrome("abcb?A1")

def rotate_list(list_in:list) -> list:
    print("_________ROTATE LIST__________")
    print("Input list: ", list_in)
    last_el = [list_in[-1]]
    list_remain = list_in[:-1]
    list_out = last_el + list_remain
    print("Rotated list: ", list_out)
    return list_out

if __name__ == "__main__":
    is_palindrome("a}bcb?A/")
    is_palindrome("hashsah")
    rotate_list([1,2,4,5,6])
    rotate_list([4,5,6,7,8,9])

