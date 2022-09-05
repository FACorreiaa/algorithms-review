# O (j + d) time | O (j + d) space
def topologicalSort(jobs, deps):
    jobGraph = createJobGraph(jobs, deps)
    return getOrderedJobs(jobGraph)


def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)
    # [x,y]
    for job, dep in deps:
        # adding edges
        graph.addDep(job, dep)
    return graph


def getOrderedJobs(graph):
    orderedJobs = []
    nodesWithNoPreReqs = list(
        filter(lambda node: node.numOfPrereqs == 0, graph.nodes))
    while len(nodesWithNoPreReqs):
        node = nodesWithNoPreReqs.pop()
        orderedJobs.append(node.job)
        removeDeps(node, nodesWithNoPreReqs)
    graphHasEdges = any(node.numOfPrereques for node in graph.nodes)
    return graphHasEdges if graphHasEdges else orderedJobs


def removeDeps(node, nodesWithNoPreReqs):
    while len(node.deps):
        dep = node.deps.pop()
        dep.numOfPrereques -= 1
        if dep.numOfPrereques == 0:
            nodesWithNoPreReqs.append(dep)


class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)

    def addDep(self, job, dep):
        jobNode = self.getNode(job)
        depNode = self.getNode(dep)
        jobNode.deps.append(depNode)
        depNode.numOfPrereqs += 1

    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]


class JobNode:
    def __init__(self, job):
        self.job = job
        self.deps = []
        self.numOfPrereques = 0
