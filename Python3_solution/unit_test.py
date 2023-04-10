import unittest
import LongestDAG

class TestSolutions(unittest.TestCase):
    def setUp(self):
        print('About to test the function')
    
    def test1_edges(self):
        ''' Tests if a flat list is passed instead of 1-D list of tuples'''
        test_edges = ['a', 'b' 'c']
        res1 = solution2.DAG(test_edges, solution2.labels).makeDAG()
        correct_res = solution2.DAG(solution2.edges, solution2.labels).makeDAG()
        self.assertTrue(isinstance(res1,IndexError))
   
    def test2_makeDAG(self):
        ''' Tests if a string is passed instead of 1-D list of tuples'''
        test_edges = 'abc'
        res1 = solution2.DAG(test_edges, solution2.labels).makeDAG()
        correct_res = solution2.DAG(solution2.edges, solution2.labels).makeDAG()
        self.assertTrue(isinstance(res1,IndexError))

    def test3_makeDAG(self):
        ''' Tests if the edges are not 1-D list'''
        test_edges = ['abc', 'dd']
        res1 = solution2.DAG(test_edges, solution2.labels).makeDAG()
        correct_res = solution2.DAG(solution2.edges, solution2.labels).makeDAG()
        self.assertIsNone(res1) 

    def test4_makeDAG(self):
        ''' Tests if the input list of edges is an acyclic DAG'''
        test_edges = [("root", "c"), ("c", "b"), ("c", "e"), ("c", "c"), ("b", "d"), ("d", "e")]
        res1 = solution2.DAG(test_edges, solution2.labels).makeDAG()
        correct_res = solution2.DAG(solution2.edges, solution2.labels).makeDAG()
        self.assertIsNone(res1)
        

    def test_get_all_paths(self):      
        ''' Tests if the edges are not 1-D list'''
        key  = '11' 
        res1 = solution2.DAG(solution2.edges, solution2.labels).get_longest_path_for_node('11')
        correct_res = solution2.DAG(solution2.edges, solution2.labels).get_longest_path_for_node('1')
        self.assertFalse(isinstance(res1,ValueError))

    def tearDown(self):
        print('Cleaning up')



if __name__ == '__main__':
    unittest.main()
