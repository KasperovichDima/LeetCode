# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:TreeNode|None=None, right:TreeNode|None=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionR:
    def maxDepth(self, root:TreeNode|None) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
    

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        
        # Наш список дел: (какой узел проверить, на какой он глубине)
        todo_list = [(root, 1)]
        max_seen_depth = 0
        
        # Пока в списке дел что-то есть...
        while todo_list:
            # Берем последний узел из списка (вычеркиваем его)
            current_node, current_depth = todo_list.pop()
            
            if current_node:
                # Если эта глубина больше той, что мы видели раньше — запоминаем
                if current_depth > max_seen_depth:
                    max_seen_depth = current_depth
                
                # Добавляем детей в список дел, чтобы проверить их позже
                # Их глубина будет на 1 больше текущей
                if current_node.left:
                    todo_list.append((current_node.left, current_depth + 1))
                if current_node.right:
                    todo_list.append((current_node.right, current_depth + 1))
                    
        return max_seen_depth



def build_tree(nodes: list) -> TreeNode|None:
    """Строит дерево из списка (BFS order)"""
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        node = queue.pop(0)
        
        # Левый ребенок
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        
        # Правый ребенок
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    return root



s = Solution()


assert s.maxDepth(build_tree([3, 9, 20, None, None, 15, 7])) == 3
assert s.maxDepth(build_tree([])) == 0
assert s.maxDepth(build_tree([1, 2, None, 3, None, 4])) == 4
assert s.maxDepth(build_tree([1, None, 2])) == 2
