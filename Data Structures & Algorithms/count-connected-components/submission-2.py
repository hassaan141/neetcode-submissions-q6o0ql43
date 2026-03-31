class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        {
         2: [3, 1], 
         3: [2, 1], 
         1: [2, 3],
        }
        """

        graph = self.edgeToAdjacencyList(edges)
        print(graph)
        visited = set()
        total = 0
        flyingNodes = 0
        for node in graph:
            total += self.explore(graph, node, visited)
        
        print(f"visited set length {len(visited)}")
 

        return total + (n - len(visited))
        
    
    def explore(self, graph, node, visited):

        if node in visited:
            return 0
        
        visited.add(node)
        for neighbours in graph[node]:
            self.explore(graph, neighbours, visited)
        
        return 1

    def edgeToAdjacencyList(self, edges: List[List[int]]):

        graph = {}

        for n in edges:
            a, b = n

            if a not in graph:
                graph[a] = [ b ]
            else:
                graph[a].append(b)
            
            if b not in graph:
                graph[b] = [ a ]

            else:
                graph[b].append(a)

        return graph
