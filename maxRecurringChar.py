# Finding the Most Recurring Character

def maxRecurringChar(s):
    
#     first we create a list of unique letters from the given string
    
    uniqueLetters = list(set(s))
    
    newList = [] # empty list to store the tuple of word and it's occurence
    
    for i in uniqueLetters: #looping to find out which word comes how many times
        count = 0
        for j in s:
            if i == j:
                count+=1
            
        newList.append((count,i)) #appendig them as a tuple
            
    newDict  = dict(newList)    #creating dictonary of the list


    return newDict[max(newDict.keys())] #find out the max no of ocurrence and then return its value
    
print(maxRecurringChar('aababbbbbbbbbbbbbcada'))
