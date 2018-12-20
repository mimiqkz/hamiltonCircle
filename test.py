from main import getNodes, nodeDistance, getWeights
from ant import Ant
from graph import Graph
from colony import Colony

def test_nodeDistance():
	x1, y1 = 1, 0
	x2, y2 = 6, 0
	distance = nodeDistance(x1, y1, x2, y2)
	assert distance == 5

def test_getNodes():
	file = './data/miniset.tsv'
	data = [{'x': 1.0, 'y': 2.0}, {'x': 3.0, 'y': 4.0}, {'x': 5.0, 'y': 5.0}, 
	{'x': 3.0, 'y': 1.0}, {'x': 6.0, 'y': 8.0}, {'x': 13.0, 'y': 0.0}]
	nodes = getNodes(file)
	assert len(nodes) == 6
	assert data == nodes

def test_getWeights():
	p = [{'x': 1.0, 'y': 0.0}, {'x': 6.0, 'y': 0.0}]
	w = [[0.0, 5.0], [5.0, 0.0]]
	weights = getWeights(p)
	assert w == weights

def test_start():
	c = Colony(100)
	w = [[0.0, 5.0], [5.0, 0.0]]
	g = Graph(2, w)
	bestLength, bestSolution = c.start(g, 2)
	assert bestLength == 10.0

test_nodeDistance()
test_getNodes()
test_getWeights()
test_start()
