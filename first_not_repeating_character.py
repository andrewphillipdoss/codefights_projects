#Given a string s, find and return the first instance of a
#non-repeating character in it. If there is no such character, return '_'.

def firstNotRepeatingCharacter(s):
    index = [] #create a list to house indecies of possible answers
    a = list(s)
    a.sort() #sort the string alphabetically
    b = [i[0] for i in sorted(enumerate(s), key=lambda x:x[1])] #index reference array for sorted
    if len(a) == 1: #if only 1 character in string
      return a[0]
    for i in range(1,len(a)-1):
        if a[0] != a[1]: #check first character
          index.append(b[0])
        if a[i] != a[i+1] and a[i] != a[i-1]: #check middle
          index.append(b[i])
        if a[len(a)-1] != a[len(a)-2]: #check last
          index.append(b[len(a)-1])
    if index != []: #if there are answers
      return s[min(index)] #return the one w/ the smalled index
    else:
      return "_" #if not, return _
