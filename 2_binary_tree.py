# Definition for a binary tree node.
class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def levelOrderBottom(self, root: TreeNode) -> list:
        
        depth = self.find_depth(root)
        matrix = []
        
        for i in reversed(range(depth)):
            
            matrix.append(self.get_at_index(root, i))
            
        return matrix
    
    
    def find_depth(self, node) -> int:
        
        left_val = 0
        right_val = 0
        
        if node == None:
            return 0
        else:
            if node.left is not None:
                left_val = self.find_depth(node.left)

            if node.right is not None:
                right_val = self.find_depth(node.right)
        
        return 1 + (left_val if left_val > right_val else right_val)

    
    def get_at_index(self, node, i, curr_index=0) -> list:
        
        if curr_index == i:
            return [node.val]
        else:
            
            left_val, right_val = [], []
            
            if node.left is not None:
                left_val = self.get_at_index(node.left, i, curr_index+1)
            
            if node.right is not None:
                right_val = self.get_at_index(node.right, i, curr_index+1)
            
            return left_val + right_val
        
        

def main():
    
    node_list = [3,9,20,None,None,15,7]
    
    node_15 = TreeNode(15)
    node_7 = TreeNode(7)
    node_20 = TreeNode(20, node_15, node_7)
    node_9 = TreeNode(9)
    node_3 = TreeNode(3, node_9, node_20)
    node_4 = TreeNode(4, node_3)
    
    s = Solution()
    
    print(f"{s.levelOrderBottom(node_4)}")
    
    return 0

if __name__ == '__main__':
    exit(main())
