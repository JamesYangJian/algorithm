# -*- coding: utf-8 -*-  

# 导入指定类和函数
from pybst.bstree import BSTree
from pybst.draw import plot_tree

# 创建一个树
tree=BSTree()

tree.insert(10, '') 
"""
insert()方法说明: 增加一个节点(key为10, value为a), key 必须是数值, value 看起来没什么用, 直接赋空字符串即可. 
因为没有指定 parent 参数, 而且是第一个没有指定 parent 的调用, 所以新节点为根节点.
在根节点生成后, 如调用 insert() 时仍没有指定 parent 的话, bst 包将按照二叉查找树的规则, 自动在合适的节点上增加子节点. 
但注意该函数返回值为空, 而不是新生成的节点, 要获得新节点, 需要使用get_node()方法. 
"""

# 获取key=10的节点
root_node=tree.get_node(10)

# 在key=10的节点上增加子节点, 因为bst包是二叉查找树, 所以如果三次指定了同一个parent_node, 
# 第3次新增的节点将是parent_node的孙子节点, 而不是直接子节点 
tree.insert(11, '', root_node)
tree.insert(5, '', root_node)
tree.insert(3, '', root_node)

node_5 = tree.get_node(5)
tree.insert(20, '', node_5)
tree.insert(30, '', root_node)

# 二叉查找树可视化, 该树共两个节点: 10 和 11
plot_tree(tree)