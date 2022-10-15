def airportConnections(airports, routes, startingAirport):
    airportGraph = createAirportGraph(airports, routes)
    unreachableAirportNodes = getUnreachableNodes(
        airportGraph, airports, startingAirport)
    markUnreachableConnections(airportGraph, unreachableAirportNodes)
    return getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes)

# O(a + r) time | O(a + r) space


def createAirportGraph(airports, routes):
    airportGraph = {}
    for airport in airports:
        airportGraph[airport] = AirporttNode(airport)
    for route in routes:
        airport, connection = route
        airportGraph[airport].connections.append(connection)
    return airport

# O(a + r) time | O(a + r) space


def getUnreachableNodes(airportGraph, airports, startingAirport):
    visitedAirports = {}
    deepFirstTraverseAirports(airportGraph, startingAirport, visitedAirports)

    unreachableAirportNodes = []
    for airport in airports:
        if airport in visitedAirports:
            continue
        airportNode = airportGraph[airport]
        airportNode.isReachable = False
        unreachableAirportNodes.append(airportNode)
    return unreachableAirportNodes


def deepFirstTraverseAirports(airportGraph, startedAirport, visitorAirports):
    if startedAirport in visitorAirports:
        return
    visitorAirports[startedAirport] = True
    connections = airportGraph[startedAirport].connections
    for connection in connections:
        deepFirstTraverseAirports(airportGraph, connection, visitorAirports)


def markUnreachableConnections(airportGraph, unreachableAirportNodes):
    for airportNode in unreachableAirportNodes:
        airport = airportNode.airport
        unreachableConnections = []
        depthFirstAddUnreachableConnections(
            airportGraph, airport, unreachableConnections, {})
        airportNode.unreachableConnections = unreachableConnections


def depthFirstAddUnreachableConnections(airportGraph, airport, unreachableConnections, visitedAirports):
    if airportGraph[airport].isReachable:
        return
    if airport in visitedAirports:
        return
    visitedAirports[airport] = True
    unreachableConnections.append(airport)
    connections = airportGraph[airport].connections
    for connection in connections:
        deepFirstTraverseAirports(
            airportGraph, connection, unreachableConnections, visitedAirports)


def getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes):
    unreachableAirportNodes.sort(key=lambda airport: len(
        airport.unreachableConnections), reverse=True)
    numberOfnewConnections = 0
    for airportNode in unreachableAirportNodes:
        if airportNode.isReachable:
            continue
        numberOfnewConnections += 1
        for connection in airportNode.unreachableConnections:
            airportGraph[connection].isReachable = True
    return numberOfnewConnections


class AirporttNode:
    def __init__(self, airport):
        self.airport = airport
        self.connections = []
        self.isReachable = True
        self.unreachableAirportNodes = []
