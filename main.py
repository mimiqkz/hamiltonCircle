import sys
import math
import matplotlib.pyplot as plt
import numpy as np

from colony import Colony
from graph import Graph

def getNodes(file):
	nodes = []
	with open(file, 'r') as f:
		reader = f.readlines()
		for i, line in enumerate(reader):
			x, y = line.split()
			nodes.append(dict(x=float(x), y=float(y)))
	f.close
	return nodes

def nodeDistance(x1, y1, x2, y2):
	return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def getWeights(nodes):
	weights = []
	for i in range(len(nodes)):
		x1, y1 = nodes[i]['x'], nodes[i]['y']
		row = []
		for j in range(len(nodes)):
			x2, y2 = nodes[j]['x'], nodes[j]['y']
			row.append(nodeDistance(x1, y1, x2, y2))
		weights.append(row)
	return weights

def plotGraph(nodes, bestSolution):  # pragma: no cover
	x, y, path_x, path_y = [], [], [], []
	for n in nodes:
		x.append(n['x'])
		y.append(n['y'])

	for i, point in enumerate(bestSolution):
		path_x.append(x[point])
		path_y.append(y[point])
	
	#To connect and create a circle
	path_x.append(x[bestSolution[0]])
	path_y.append(y[bestSolution[0]])

	plt.title('The optimized path across all the nodes')
	plt.plot(path_x, path_y, '-o', color='black')
	plt.show()

def main():  # pragma: no cover
	#Get the nodes from file data
	nodes = getNodes('./data/dataset.tsv')
	#This is the number in which the ants are put back to its origin after each transversal
	redistributeNum = 100

	#Get the weight/cost of edges from the nodes
	weights = getWeights(nodes)
	graph = Graph(len(nodes), weights)
	
	antNum = len(nodes)  # The number of ant is set to equals the number of nodes
	colony = Colony(redistributeNum)

	bestLength, bestSolution = colony.start(graph, antNum)
	print("Path: ", bestSolution)
	print("Sum length:", round(bestLength,2))
	plotGraph(nodes, bestSolution)
	
if __name__ == '__main__':
	main()  # pragma: no cover
