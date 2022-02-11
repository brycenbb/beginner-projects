def isPalim(word):
    # Gets rid of whitespace and makes everything lowercase
    word = word.replace(" ", "")
    word = word.lower()
  
   
    #gets rid of bad characters
    if not word.isalnum():
        word = "".join([i for i in word if i.isalnum()])

    
    for i in range(int(len(word)/2)):
        if word[i] != word[len(word)-1-i]:
            return False

    '''If I used the more efficent way of doing things, it would look like:'''
    #if word != word[::-1]: 
    #    return False

    return True


print(isPalim("appa"))