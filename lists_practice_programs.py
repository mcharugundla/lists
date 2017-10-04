def count_same_chars(string):
    '''(str) -> int

    Return the number of occurences of a character and an adjacent character
    that are being same.
    
    >>>count_same_chars("abccdeffggh")
    3
    
    '''
    char_repeat = 0
    
    for each_char in range(len(string)-1):
        if string[each_char] == string[each_char + 1]:
            char_repeat += 1
            
    return char_repeat

print(count_same_chars("abccdeffggh"))
        

       
def shift_left(L):
    
    '''(List) -> Nonetype

    Shift each item in the list to its left and shift the first item
    to the last position

    >>>shift_left(["m","a","d","h","u"])
    ['a', 'd', 'h', 'u', 'm']

    Precondition: len(L) >=1
    
    '''
    first_item = L[0]
    
    for i in range(1,len(L)):
        L[i-1] = L[i]
        
    L[-1] = first_item
    
       
print(shift_left(["m","a","d","h","u"]))
    

        
        
