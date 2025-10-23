class TestClass:
    def __init__(self):
        ''' Constructs new TestClass object
        >>> t = TestClass()
        >>> print(t._TestClass__secret)
        42
        '''
        self.__secret = 42
    def print(self):
        print(self.__secret)

