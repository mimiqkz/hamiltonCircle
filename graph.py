class Graph(object):
	def __init__(self, length, weights):  # pragma: no cover
		self.weights = weights
		self.length = length
		#2d matrix of corresponded pheromones
		self.pheromones = [[1 / (length * length) for j in range(length)] for i in range(length)]

	def updatePheromones(self, RHO, ants):
		for i, x in enumerate(self.pheromones):
			for j, y in enumerate(x):
				self.pheromones[i][j] *= RHO #evaporate
				for ant in ants:
					self.pheromones[i][j] += ant.pheromonDelta[i][j]
