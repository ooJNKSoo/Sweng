from typing import Dict, Any
import networkx as nx
from networkx.utils import arbitrary_element, UnionFind, generate_unique_node
from itertools import chain, count
from collections import defaultdict, Mapping, Set


def lcaForDAG(graph, a, b):
	if graph.size() == 0:
		return None
	if not nx.is_directed_acyclic_graph(graph):
		return None
	
	nodes = graph.nodes()
	if a not in nodes or b not in nodes:
		return None

	sources = [n for n, deg in graph.in_degree if deg == 0]
	if len(sources) == 1:
		root = sources[0]
		super_root = None
	else:
		graph = graph.copy()
		super_root = root = generate_unique_node()
		for source in sources:
			graph.add_edge(root, source)

	span = nx.dfs_tree(graph, root)
	dag = nx.DiGraph((u, v) for u, v in graph.edges
	if u not in span or v not in span[u])

	span.add_nodes_from(graph)
	dag.add_nodes_from(graph)
	i = count()
	dist = {root: next(i)}

	for edge in nx.bfs_edges(span, root):
		for node in edge:
			if node not in dist:
				dist[node] = next(i)

	pos: Dict[Any, Any] = {}
	for node in nx.depth_first_search.dfs_preorder_nodes(graph, root):
		if node not in pos:
			pos[node] = next(i)

	pairs = [(a,b)]
	pairset = set(chain.from_iterable(pairs))

	ancestors = {}
	for v in pairset:
		my_ancestors = nx.dag.ancestors(dag, v)
		my_ancestors.add(v)
		ancestors[v] = sorted(my_ancestors, key=pos.get)

	def evalDAG(tree_lca, testRun):
		best_dist = None
		best = None
		indices = [0, 0]
		ancestorsX = [ancestors[a], ancestors[b]]

		def getNext(indices):
			i1, i2 = indices
			if i1 >= len(ancestors[a]) and i2 >= len(ancestors[b]):
				return None
			elif i1 >= len(ancestors[a]):
				return 1
			elif pos[ancestors[a][i1]] < pos[ancestors[b][i2]] or i2 >= len(ancestors[b]):
				return 0
			return 1;

		i = getNext(indices)
		cur = ancestorsX[i][indices[i]], i
		while i is not None:
			prev = cur
			indices[i] += 1
			i = getNext(indices)
			if i is not None:
				cur =ancestorsX[i][indices[i]], i

				if cur[1] != prev[1]:
					n1, n2 = prev[0], cur[0]
					if (n1, n2) in tree_lca:
						ans = tree_lca[n1, n2]
					else:
						ans = tree_lca[n2, n1]
					if not testRun and (best is None or
							dist[ans] > best_dist):
						best_dist = dist[ans]
						best = ans

		if not testRun and (super_root is None or best != super_root):
			return best

	tree_lca = defaultdict(int)
	evalDAG(tree_lca, True)

	for (pair, lca) in pairsLCA(span, root, tree_lca):
		tree_lca[pair] = lca

	return evalDAG(tree_lca, False)


def pairsLCA(graph, root=None, pairs=None):
	pair_dict = defaultdict(set)
	if not isinstance(pairs, (Mapping, Set)):
		pairs = set(pairs)
	for u, v in pairs:
		for n in (u, v):
			if n not in graph:
				msg = "node Invalid" % str(n)
				raise nx.NodeNotFound(msg)
		pair_dict[u].add(v)
		pair_dict[v].add(u)

	if root is None:
		for n, deg in graph.in_degree:
			if deg == 0:
				root = n
	if root is None:
		raise nx.NetworkXError("not a DAG")

	uf = UnionFind()
	ancestors = {}
	for node in graph:
		ancestors[node] = uf[node]

	colors = defaultdict(bool)
	for node in nx.dfs_postorder_nodes(graph, root):
		colors[node] = True
		for v in (pair_dict[node] if pairs is not None else graph):
			if colors[v]:
				if pairs is not None and (node, v) in pairs:
					yield (node, v), ancestors[uf[v]]
				if pairs is None or (v, node) in pairs:
					yield (v, node), ancestors[uf[v]]
		if node != root:
			parent = arbitrary_element(graph.pred[node])
			uf.union(parent, node)
			ancestors[uf[parent]] = parent
