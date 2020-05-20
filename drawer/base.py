from graphviz import Digraph


class MyDiGraph:
    class GraphAttributes:
        name = 'Tree'
        label = """<<FONT POINT-SIZE="30" FACE="ubuntu">{}</FONT><BR ALIGN="CENTER"/>>"""
        rankdir = 'TB'

    class NodeAttributes:
        node_label = """<<FONT POINT-SIZE="18" FACE="ubuntu">%s</FONT><BR ALIGN="CENTER"/>>"""

    def __init__(self, format='pdf'):
        self.digraph = Digraph(format=format)
        self.digraph.attr(name=MyDiGraph.GraphAttributes.name, rankdir=MyDiGraph.GraphAttributes.rankdir)

    def add_node(self, key, value):
        if value == 'null':
            self.digraph.node(key, MyDiGraph.NodeAttributes.node_label % value,
                              shape='point', width='.2', height='.2')

        else:
            self.digraph.node(key, MyDiGraph.NodeAttributes.node_label % value,
                              shape='circle', width='1', height='1')

    def add_edge(self, source, destination):
        self.digraph.edge(source, destination)

    def view(self):
        self.digraph.view()