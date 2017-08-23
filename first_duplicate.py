#Given an array a that contains only numbers in the range from 1 to a.length
#find the first duplicate number for which the second occurrence has the minimal index.
#In other words, if there are more than 1 duplicated numbers,
#return the number for which the second occurrence has a smaller index than
#the second occurrence of the other number does. If there are no such elements, return -1.

def firstDuplicate(a):
  index = [] #create an array to store indecies of the duplicates
  b = list(a)
  b.sort() #sort the array
  c = [i[0] for i in sorted(enumerate(a), key=lambda x:x[1])] #store the indecies of the sorted array
  for i in range(0,len(b)-1): #loop over sorted array
    if b[i] == b[i+1]: #since sorted, dups will be beside each other
      index.append(c[i+1]) #add index of dups to array
  if len(index) == 0:
    return -1 #if no dups, return -1
  else: #else, return the one with min index
      return a[min(index)]
