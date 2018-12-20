import random

class Ant(object):
	def __init__(self, graph, start):
		self.graph = graph

		self.tourLength = 0.0
		self.startNode = start
		self.currentNode = self.startNode 

		self.path = []
		self.path.append(self.startNode)
		self.unvisitedNode = [i for i in range(self.graph.length)]
		
		self.unvisitedNode.remove(self.startNode)

		self.pheromonDelta = []

	def pheromonProduct(self, i, j, alpha, beta):
		result = 0 if i == j else self.graph.pheromones[i][j]**alpha * (1.0 / self.graph.weights[i][j])**beta
		return result

	#To determine the likelihoods of the next choice of node, base on pheromones
	def getProbabilities(self, denominator, alpha, beta):
		probabilities = [0 for i in range(self.graph.length)]
		for i in range(self.graph.length):
			if i in self.unvisitedNode:
				probabilities[i] = self.pheromonProduct(self.currentNode, i, alpha, beta) / float(denominator)
		return probabilities
		
	def getNextNode(self, probabilities):
		selectedLocation = 0
		rand = random.random()
		for i, probability in enumerate(probabilities):
			if i in self.unvisitedNode:
				rand -= probability
				if rand <= 0:
					selectedLocation = i
					break
		return selectedLocation

	def selectNextNode(self, alpha, beta):
		denominator = 0.0
		for i in self.unvisitedNode:
			denominator += float(self.pheromonProduct(self.currentNode, i, alpha, beta))

		probabilities = self.getProbabilities(denominator, alpha, beta)
		nextNode = self.getNextNode(probabilities)
		
		#Update paths once the location is selected
		self.unvisitedNode.remove(nextNode)
		self.path.append(nextNode)
		self.tourLength += self.graph.weights[self.currentNode][nextNode]

		self.currentNode = nextNode

	#Update trail due to pheromones
	def updateTrail(self, Q):
		self.pheromonDelta = [[0 for j in range(self.graph.length)] for i in range(self.graph.length)]
		for i in range(1, len(self.path)):
			start = self.path[i - 1]
			to = self.path[i]
			
			self.pheromonDelta[start][to] = Q / self.tourLength





		
		



