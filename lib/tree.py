class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, target_id):
        return self._dfs(self.root, target_id)

    def _dfs(self, current_node, target_id):
        if current_node is None:
            return None

        # Check if the current node has the target ID
        if current_node.get('id') == target_id:
            return current_node

        # Recursively search in the children
        for child in current_node.get('children', []):
            result = self._dfs(child, target_id)
            if result:
                return result

        # If not found in current node or its children, return None
        return None