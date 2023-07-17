import numpy as np


def generateUnknownFstruct():
    fStruct = dict()
    massFlow = dict()
    enthFlow = dict()
    fractions = dict()
    species = dict()

    fStruct['temp'] = np.nan
    fStruct['press'] = np.nan
    fStruct['concStd'] = np.array([np.nan])

    massFlow['liquid'] = np.nan
    massFlow['gas'] = np.nan
    enthFlow['liquid'] = np.nan
    enthFlow['gas'] = np.nan

    fractions['mMultPhase'] = np.array([np.nan])
    fractions['Vgas'] = np.array([np.nan])
    fractions['mGas'] = np.array([np.nan])

    fStruct['massFlow'] = massFlow
    fStruct['enthFlow'] = enthFlow
    fStruct['fractions'] = fractions

    species['comp'] = np.nan
    species['load'] = np.nan

    fStruct['species'] = species

    return fStruct


def addNumbers(numbers):
    # if 10 in numbers: numbers.append(1)
    return sum(numbers)


def checkIfOdd(x):
    if x % 2 == 1:
        return True
    else:
        raise ValueError(f'{x} is even')
