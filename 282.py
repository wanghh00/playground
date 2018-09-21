# 282. Expression Add Operators
# Given a string that contains only digits 0-9 and a target value, 
# return all possibilities to add binary operators (not unary) +, -, or * 
# between the digits so they evaluate to the target value.
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        pass

def combination(lst, n):
    tmp = [lst[0] for x in xrange(n)]

    for n in xrange(len(lst)):
        for x in lst:
            tmp[n] = x
            print tmp

def premutation(lst):
    result = [None for x in xrange(len(lst))]
    premutil(lst, result, n)

def premutil(lst):
    if 

combination('abc',3)

