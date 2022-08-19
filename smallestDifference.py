# O(Nlog(N) + mLog(m)) Time | O(1) Space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallestDifference = float("inf")
    currentDif = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            currentDif = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            currentDif = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if smallestDifference > currentDif:
            smallestDifference = currentDif
            smallestPair = [firstNum, secondNum]
    return smallestPair
