import unittest


import networkx as nx
from LCA_DAG import lcaForDAG as lca


class DAGTestClass(unittest.TestCase):
	def testEmptyDAG(self):
		testGraph = nx.DiGraph()
		self.assertEqual(lca(testGraph, 1, 2), None)

	def testNodesNotPresent(self):
		testGraph = nx.DiGraph()
		testGraph.add_nodes_from([1,2,3,4])
		self.assertEqual(lca(testGraph, 7, 8), None)

	def testNotAcyclic(self):
		testGraph = nx.DiGraph()
		testGraph.add_nodes_from([1,2,3])
		testGraph.add_edges_from([(1,2), (2,3), (3,1)])
		self.assertEqual(lca(testGraph, 1, 2), None)

	def testRegularDAG(self):
		testGraph = nx.DiGraph()
		testGraph.add_nodes_from([1,2,3,4,5,6,7])
		testGraph.add_edges_from([(1,2), (1,4), (2,3), (3,6), (4,5), (5,6), (6,7)])
		self.assertEqual(lca(testGraph, 3, 4), 1)

	def testNoCommonAncestor(self):
		testGraph = nx.DiGraph()
		testGraph.add_nodes_from([1,2,3,4])
		testGraph.add_edges_from([(1,2), (3,4)])
		self.assertEqual(lca(testGraph, 2, 3), None)

	def testLCAisNode(self):
		testGraph = nx.DiGraph()
		testGraph.add_nodes_from([1,2,3,4])
		testGraph.add_edges_from([(1,2), (2,3), (3,4)])
		self.assertEqual(lca(testGraph, 2, 3), 2)

if __name__ == "__main__":
	unittest.main()