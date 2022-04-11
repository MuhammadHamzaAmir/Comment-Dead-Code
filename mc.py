# super class
class test:

    # public data member
    var1 = None

    # protected data member
    _var2 = None

    # private data member
    __var3 = None

    # constructor
    def __init__(self, var1, var2, var3):
         self.var1 = var1
         self._var2 = var2
         self.__var3 = var3

    # public member function
    def displayPublicMembers(self):

         # accessing public data members
        print("Public Data Member: ", self.var1)

     # protected member function
    def _displayProtectedMembers(self):

         # accessing protected data members
        print("Protected Data Member: ", self._var2)

     # private member function
    def __displayPrivateMembers(self):

         # accessing private data members
        print("Private Data Member: ", self.__var3)

     # public member function
    def accessPrivateMembers(self):

         # accessing private member function
        self.__displayPrivateMembers()
