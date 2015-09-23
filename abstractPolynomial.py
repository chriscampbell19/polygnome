from abc import ABCMeta, abstractmethod
import polygnomeObject

class abstractPolynomial(polygnomeObject.polygnomeObject):
    __metaclass__ = ABCMeta
    """
    File: abstractPolynomial.py
    Author: Chris Campbell
    Email: c (dot) j (dot) campbell (at) ed (dot) ac (dot) uk
    Github: https://github.com/chriscampbell19
    Description: An abstract superclass for polynomials, monomials, generators and PBWmonomials.
    Most of the methods must be instantiated for yourself.
    """


    ##############################################################################
    ######  SORTING METHODS
    ##############################################################################
    @abstractmethod
    def isSorted(): pass

    @abstractmethod
    def sort(): pass

    @abstractmethod
    def safeSort(): pass

    ##############################################################################
    ######  MATHEMATICAL METHODS
    ##############################################################################
    @abstractmethod
    def isZero(self): pass

    def __eq__(self,other):
        self.sanityCheck()
        x = self - other
        x.sort()
        if x.isZero():
            return True
        else:
            return False


    @abstractmethod
    def __add__(self,other): pass

    @abstractmethod
    def __mul__(self,other): pass

    @abstractmethod
    def __sub__(self,other): pass
    ##############################################################################
    ######  PRINTING AND TYPING
    ##############################################################################

    @abstractmethod
    def __repr__(self): pass

    @abstractmethod
    def toLatex(self): pass
    ##############################################################################
    ######  Debugging and Testing Code
    ##############################################################################

    @abstractmethod
    def sanityCheck(self): pass
