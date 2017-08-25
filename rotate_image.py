# You are given an n x n 2D matrix that represents an image.
# Rotate the image by 90 degrees (clockwise).
# sample input:
# a = [[1,2,3],
#     [4,5,6],
#     [7,8,9]]

import unittest


def rotateImage(a):
    n = len(a)-1
    y = [] # create array to hold final answer
    x = [] # create temp array to hold first dimension
    for j in range(0,len(a)):
        for i in range(0,len(a)):
          # for each j, retrieve the absolute value of
          # i - matrix_size - 1.
          x.append(a[abs(i-n)][j])
          while len(x) == len(a): # when the first dimension is full
              y.append(x) # add it to the second dimension
              x = [] # empty the array of the first dimension
    return y



class TestRotateImage(unittest.TestCase):

    test1 =            [[1,2,3],
                        [4,5,6],
                        [7,8,9]]

    ans1 =             [[7,4,1],
                        [8,5,2],
                        [9,6,3]]

    test2 =            [[1]]

    ans2 =             [[1]]

    test3 =            [[10,9,6,3,7],
                        [6,10,2,9,7],
                        [7,6,3,8,2],
                        [8,9,7,9,9],
                        [6,8,6,8,2]]

    ans3 =             [[6,8,7,6,10],
                        [8,9,6,10,9],
                        [6,7,3,2,6],
                        [8,9,8,9,3],
                        [2,9,2,7,7]]

    test4 =            [[33,35,8,24,19,1,3,1,4,5],
                        [25,27,40,25,17,35,20,3,19,3],
                        [9,1,9,30,9,25,32,12,15,22],
                        [30,47,25,10,18,1,19,17,43,17],
                        [40,46,42,34,18,48,29,40,31,39],
                        [37,42,37,19,45,1,4,46,48,13],
                        [8,26,31,46,44,24,34,29,12,25],
                        [45,48,36,12,33,12,4,45,22,37],
                        [33,15,34,25,34,8,50,48,30,28],
                        [18,19,22,29,15,43,38,30,8,47]]

    ans4 =             [[18,33,45,8,37,40,30,9,25,33],
                        [19,15,48,26,42,46,47,1,27,35],
                        [22,34,36,31,37,42,25,9,40,8],
                        [29,25,12,46,19,34,10,30,25,24],
                        [15,34,33,44,45,18,18,9,17,19],
                        [43,8,12,24,1,48,1,25,35,1],
                        [38,50,4,34,4,29,19,32,20,3],
                        [30,48,45,29,46,40,17,12,3,1],
                        [8,30,22,12,48,31,43,15,19,4],
                        [47,28,37,25,13,39,17,22,3,5]]


    def setUp(self):
        pass

    def test_rotate_image_3x3(self):
        self.assertEqual(rotateImage(TestRotateImage.test1),TestRotateImage.ans1)

    def test_roate_image_1x1(self):
        self.assertEqual(rotateImage(TestRotateImage.test2),TestRotateImage.ans2)

    def test_rotate_image_5x5(self):
        self.assertEqual(rotateImage(TestRotateImage.test3),TestRotateImage.ans3)

    def test_rotate_image_large(self):
        self.assertEqual(rotateImage(TestRotateImage.test4),TestRotateImage.ans4)

if __name__ == '__main__':
    unittest.main(verbosity=2)
