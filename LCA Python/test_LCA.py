import unittest
from LCA import findLCA, Node

class TestLCA(unittest.TestCase):

    """
          1
         / \
        2   3
       /   / \
      4   6   7
    """
    def test_lca(self):
        root = Node(1) 
        root.left = Node(2) 
        root.right = Node(3) 
        root.left.left = Node(4) 
        root.right.left = Node(6) 
        root.right.right = Node(7) 
        nullroot = None



        # Test no node
        self.assertEqual(None, findLCA(nullroot, 5, 3))
        
        # Test available nodes
        self.assertEqual(1, findLCA(root, 2, 3).key)
        self.assertEqual(3, findLCA(root, 6, 7).key)
        
        # Test node of ancestor
        self.assertEqual(1, findLCA(root, 1, 7).key)
        self.assertEqual(1, findLCA(root, 4, 7).key)



if __name__ == "__main__":
    unittest.main()