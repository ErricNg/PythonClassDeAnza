def test():
    '''
    The test docstring for the function test.
    '''
    print(18)

help(test)
print('#############################')
print(test.__doc__)
print('#############################')

class Test:
    '''
    This is the docstring for the class Test"
    '''
    
    def testAdd(self):
        '''
        This is the docstring for the method testAdd"
        '''
        print(4+8)


help(Test)
print('#############################')
help(Test.testAdd)
        
