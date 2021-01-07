"""Write a function that takes in a string of one or more words, 
and returns the same string, but with all five or more letter words reversed 
(Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. 
Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"""

def spin_words(sentence):
    list_s = sentence.split(' ')
    sentence_s = ''
    for el in list_s:
        l = len(el)
        if l > 4:
            f = el[::-1]
            sentence_s = sentence_s + ' ' + f
        else:
            sentence_s = sentence_s + ' ' + el
    return sentence_s.strip()

print(spin_words("Welcome worl press"))

def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])