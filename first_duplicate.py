#Given an array a that contains only numbers in the range from 1 to a.length
#find the first duplicate number for which the second occurrence has the minimal index.
#In other words, if there are more than 1 duplicated numbers,
#return the number for which the second occurrence has a smaller index than
#the second occurrence of the other number does. If there are no such elements, return -1.

import unittest

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

class TestFirstDuplicate(unittest.TestCase):

    test1 = [2, 3, 3, 1, 5, 2]

    ans1 = 3

    test2 = [2, 4, 3, 5, 1]

    ans2 = -1

    test3 = [1]

    ans3 = -1

    test4 = [2, 2]

    ans4 = 2

    def SetUp(self):
        pass

    def test_first_duplicate_mutiple_dups(self):
        self.assertEqual(firstDuplicate(TestFirstDuplicate.test1), TestFirstDuplicate.ans1)

    def test_first_duplicate_no_dups(self):
        self.assertEqual(firstDuplicate(TestFirstDuplicate.test2), TestFirstDuplicate.ans2)

    def test_first_duplicate_one_number(self):
        self.assertEqual(firstDuplicate(TestFirstDuplicate.test3), TestFirstDuplicate.ans3)

    def test_first_duplicate_only_dups(self):
        self.assertEqual(firstDuplicate(TestFirstDuplicate.test4), TestFirstDuplicate.ans4)

if __name__ == '__main__':
    unittest.main(verbosity=2)
