from collections import defaultdict
from itertools import permutations
import numpy as np
import networkx as nx


# Define graph by edges
edges = [('1', '2'), ('2', '4'), ('1', '11'), ('4', '11')]
labels = np.random.ranf(len(edges))


class DAG:
    def __init__(self, edges, labels):
            self.edges = edges
            self.labels = labels
    
    def makeDAG(self):
        ''' topological ordering of nodes'''
        edges = self.edges        
        try:
            graph = nx.DiGraph()
            for i in self.edges:
                graph.add_edge(i[0],i[1])

            if nx.is_directed_acyclic_graph(graph) == True:    
                graph2 = defaultdict(list)
                for source, target in self.edges:
                    graph2[source].append(target)
                return graph2

        except (ValueError, IndexError) as err:
            return err

    def get_paths(self, vertex):
        '''Find all paths given a node'''
        try:
            def DFS(input_graph,vertex,visited=None,path=None):
                if visited is None: visited = []
                if path is None: path = [vertex]

                visited.append(vertex)

                paths = []
                for t in input_graph[vertex]:
                    if t not in visited:
                        final_path = path + [t]
                        paths.append(tuple(final_path))
                        paths.extend(DFS(input_graph, t, visited[:], final_path))
                return paths
        
            return DFS(self.makeDAG(),vertex)
        except:
            print('please pass a valid list of tuples representing directed acyclic grapgh ') 
    
    def get_longest_path_for_node(self, vertex):
        '''Find longes path for a given node'''
        try:    
            all_paths = self.get_paths(vertex) 
            data = dict(list(zip(self.edges, self.labels)))
                
            d = dict()

            for path in all_paths:
                print(path)
                edges = list(permutations(path,2))
                d[path] =  sum([data[edge] for edge in edges if edge in data.keys()])
            return max(d.items(), key = lambda k : k[1])
        except ValueError as err:
            print(f'Please enter a valid vertix or its is the bottom vertix in the DAG \n {err}' )

    

# Output

# paths = DAG(edges, labels)
# print(paths.get_paths('1'))
# print(paths.get_longest_path_for_node('1'))
# print(paths.get_longest_path_for_node('11'))
