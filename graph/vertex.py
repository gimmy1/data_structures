class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}
    
    def add_edge(self, vertex, weight=0):
        print("Adding edge to {0}".format(vertex))
        self.edges[vertex] = weight

    def get_edges(self):
        """ convenience method to return edges connected to self """
        return list(self.edges.keys())

    
grand_central = Vertex('Grand Central Station')
forty_second_street = Vertex('42nd Street Station')

grand_central.add_edge(forty_second_street.value)