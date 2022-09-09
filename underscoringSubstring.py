# O(N) time | O(N) space
def underscoringSubstring(string, substring):
    locations = collapse(getLocations(string, substring))
    return underscorify(string, locations)


def getLocations(string, substring):
    locations = []
    startId = 0
    while startId < len(string):
        nextId = string.find(substring, startId)
        if nextId != -1:
            locations.append([nextId, nextId + len(substring)])
            startId = nextId + 1
        else:
            break


def collapse(locations):
    if not len(locations):
        return locations
    newLocations = [locations[0]]
    previous = newLocations[0]
    for i in range(1, len(locations)):
        current = locations[i]
        if current[0] <= previous[1]:
            previous[1] = current[1]
        else:
            newLocations.append(current)
            previous = current
    return newLocations


def underscorify(string, locations):
    locationsId = 0
    stringId = 0
    inBetweenUnderscores = False
    finalChars = []
    i = 0
    while stringId < len(string) and locationsId < len(locations):
        if stringId == locations[locationsId][i]:
            finalChars.append("_")
            inBetweenUnderscores = not inBetweenUnderscores
            if not inBetweenUnderscores:
                locationsId += 1
            i = 0 if i == 1 else 1
        finalChars.append(string[stringId])
        stringId += 1
    if locations < len(locations):
        finalChars.append("_")
    elif stringId < len(string):
        finalChars.append(string[stringId])
    return "".join(finalChars)
