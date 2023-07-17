import mtb.bilanceSolver.bilanceGeneration as bilanceGeneration
from mtb.core.stringModifier import StringModifier


def calc(x):
    if (len(x) < 8):
        raise ValueError('String is to short')
    print(bilanceGeneration.generateUnknownFstruct())
    sm = StringModifier()
    reverse = sm.reverseString(x)
    return reverse


def multiply(x, y):
    return x * y
