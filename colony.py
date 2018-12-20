from ant import Ant

class Colony(object):
	def __init__(self, distro):  # pragma: no cover
		self.Q = 10
		self.RHO = 0.5
		self.ALPHA = 1.0
		self.BETA = 10.0
		self.redistributeNum = distro

	def start(self, graph, antNum):
		bestSolution = []
		bestLength = float('inf')

		#Create ants
		for r in range(self.redistributeNum):

			#Place the ants on each node
			ants = [Ant(graph, i) for i in range(antNum)]
			#Go through all the ants to find the best path and it costs
			for ant in ants:
				#Each ant goes through all the nodes
				for n in range(graph.length - 1):
					ant.selectNextNode(self.ALPHA, self.BETA)
				
				#Connect the last and the first node to create a circle
				ant.tourLength += graph.weights[ant.path[-1]][ant.path[0]]
			
				if ant.tourLength < bestLength:
					bestLength = ant.tourLength
					bestSolution = ant.path

				ant.updateTrail(self.Q)
			graph.updatePheromones(self.RHO, ants)
			
		return bestLength, bestSolution
