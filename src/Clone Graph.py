# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    def __init__(self):
        self.node_map = {}
        self.visit_queue = []

    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        self.visit_queue.append(node)
        while len(self.visit_queue) != 0:
            visit_node = self.visit_queue.pop(0)
            if visit_node.label not in self.node_map:
                copy_node = UndirectedGraphNode(visit_node.label)
            else:
                copy_node = self.node_map[visit_node.label]
            self.node_map[visit_node.label] = copy_node
            for n in visit_node.neighbors:
                if n.label in self.node_map:
                    self.node_map[visit_node.label].neighbors.append(
                        self.node_map[n.label])
                else:
                    self.visit_queue.append(n)
                    self.node_map[n.label] = UndirectedGraphNode(n.label)
                    self.node_map[visit_node.label].neighbors.append(
                        self.node_map[n.label])

        return self.node_map[node.label]
