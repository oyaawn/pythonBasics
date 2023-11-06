import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    
    def test_bfsNonWeighted(self):
        g = Graph()
        g.addEdgeNoWeight(0, 1)
        g.addEdgeNoWeight(0, 2)
        g.addEdgeNoWeight(1, 2)
        g.addEdgeNoWeight(2, 0)
        g.addEdgeNoWeight(2, 3)
        g.addEdgeNoWeight(3, 3)
        self.assertEqual(g.bfsNonWeighted(2), [2, 0, 3, 1])
        
if __name__ == '__main__':
    unittest.main()def test_bfsNonWeighted(self):
    g = Graph()
    g.addEdgeNoWeight(0, 1)
    g.addEdgeNoWeight(0, 2)
    g.addEdgeNoWeight(1, 2)
    g.addEdgeNoWeight(2, 0)
    g.addEdgeNoWeight(2, 3)
    g.addEdgeNoWeight(3, 3)
    self.assertEqual(g.bfsNonWeighted(2), [2, 0, 3, 1])
    self.assertEqual(g.bfsNonWeighted(0), [0, 1, 2, 3])
    self.assertEqual(g.bfsNonWeighted(3), [3])