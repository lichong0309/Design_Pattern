

class Component(object):
    def __init__(self, node_name):
        self.node_name = node_name

    def process(self):
        pass


class TreeNode(Component):

    def __init__(self, node_name):
        super(TreeNode, self).__init__(node_name)
        self.node_list = []

    def process(self):
        self._process_cur_node()
        self._process_sub_node()

    def add_node(self, node):
        self.node_list.append(node)

    def remove_node(self, node):
        self.node_list.pop(node)

    def _process_cur_node(self):
        print('process cur node:', self.node_name)

    def _process_sub_node(self):
        for sub_node in self.node_list:
            sub_node.process()


class LeafNode(Component):

    def process(self):
        print('process leaf node:', self.node_name)


if __name__ == '__main__':
    root_node = TreeNode('root')
    tree_node1 = TreeNode('tree_node1')
    tree_node2 = TreeNode('tree_node2')
    tree_node3 = TreeNode('tree_node3')
    leaf_node1 = LeafNode('leaf_node1')
    leaf_node2 = LeafNode('leaf_node2')

    root_node.add_node(tree_node1)
    root_node.add_node(tree_node2)
    tree_node1.add_node(tree_node3)
    tree_node3.add_node(leaf_node1)
    tree_node3.add_node(leaf_node2)

    root_node.process()
