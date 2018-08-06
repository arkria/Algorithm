import numpy as np
import unittest
import mySortAlgorithm as mySort

class SortAlgoTest(unittest.TestCase):

    def testArray(self):
        for i in range(100):
            testArray = np.random.randint(0,100,size = 30)
            temp = testArray.copy()
            myAns = mySort.bubbleSort(temp)
            testArray.sort()
            ans = (myAns == testArray)
            self.failUnless(ans.all(), 'algorithm failed')

if __name__ == '__main__':
    # unittest.main()

    test1 = [0,3,2,5,7,8,6,4,1,9]
    test2 = test1.copy()
    test1.sort()
    p = mySort.mergeSort(test2)
    print(test1)
    print(p)