# Definition for a undirected graph node
import collections


class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node: return None
        map = {node: UndirectedGraphNode(node.label)}
        queue = collections.deque([(node, map[node])])
        while queue:
            src, dst = queue.pop()
            for v in src.neighbors:
                if v not in map:
                    map[v] = UndirectedGraphNode(v.label)
                    queue.appendleft((v, map[v]))
                dst.neighbors.append(map[v])
        return map[node]
