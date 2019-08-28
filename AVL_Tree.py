import numpy as np 

# 定义节点类，比通常的树节点多了一个高度值/深度值
class Node:
    def __init__(self, value = None, height = 0, left = None, right = None):
        self.value = value
        # 高度值/深度值
        self.height = height
        self.left = left
        self.right = right

# AVL树主算法
def AVL(nums):
    root = None 
    for value in nums:
        flag = []
        # 构建二叉搜索树
        root = insert(root, value)
        # 更新树的高度
        update(root)
        # 判断失衡点和失衡种类
        judge(root, flag)
        # 当存在失衡点
        if len(flag) == 3:
            # 按照失衡点的父节点分为两种情况
            # 当失衡点为根节点时
            if flag[0] == root:
                # 根据失衡种类判断新的根节点
                # 左左失衡
                if flag[1] == "left" and flag[2] == "left":
                    newRoot = root.left
                # 左右失衡
                elif flag[1] == "left" and flag[2] == "right":
                    newRoot = root.left.right
                # 右右失衡
                elif flag[1] == "right" and flag[2] == "right":
                    newRoot = root.right
                # 右左失衡
                elif flag[1] == "right" and flag[2] == "left":
                    newRoot = root.right.left
                # 根据失衡种类采取不同的平衡操作
                # 左左失衡
                if flag[1] == "left" and flag[2] == "left":
                    LLRotation(flag[0], root)
                # 左右失衡
                elif flag[1] == "left" and flag[2] == "right":
                    LRRotation(flag[0], root)
                # 右右失衡
                elif flag[1] == "right" and flag[2] == "right":
                    RRRotation(flag[0], root)
                # 右左失衡
                else:
                    RLRotation(flag[0], root)
                # 根节点要更新
                root = newRoot
            else:
                # 失衡节点不是根节点，遍历得到其父节点
                father = search(root, flag[0])

                if flag[1] == "left" and flag[2] == "left":
                    newLeft = flag[0].left
                    LLRotation(flag[0], root)
                    if father[1] == "left":
                        father[0].left = newLeft
                    else:
                        father[0].right = newLeft
                elif flag[1] == "left" and flag[2] == "right":
                    newLeft = flag[0].left.right
                    LRRotation(flag[0], root)
                    if father[1] == "left":
                        father[0].left = newLeft
                    else:
                        father[0].right = newLeft
                elif flag[1] == "right" and flag[2] == "right":
                    newRight = flag[0].right
                    RRRotation(flag[0], root)
                    if father[1] == "left":
                        father[0].left = newRight
                    else:
                        father[0].right = newRight 
                else:
                    newRight = flag[0].right.left
                    RLRotation(flag[0], root)
                    if father[1] == "left":
                        father[0].left = newRight
                    else:
                        father[0].right = newRight
        # 重新更新树的高度
        update(root)
        
    # 返回根节点
    return root

# 插入节点操作，与一般的二叉搜索树没有区别
def insert(root, value):
    if root == None:
        root = Node(value, 0)
    elif value <= root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root

# 判断失衡点以及失衡种类，因为判断在每次insert操作之后，所以同一时间只可能存在一种失衡情况
def judge(root, flag):
    if not root:
        return 

    # 当没有孩子节点时，其孩子节点高度被赋值为-1
    leftHeight, rightHeight = -1, -1 
    if root.left:
        leftHeight = root.left.height
    if root.right:
        rightHeight = root.right.height
    # 该节点不失衡，递归去判断左右孩子节点
    if abs(leftHeight - rightHeight) < 2:
        if root.left:
            judge(root.left, flag)
        if root.right:
            judge(root.right, flag)
    # 该节点失衡
    else:
        if leftHeight > rightHeight:
            flag.append(root)
            flag.append("left")
            # 进一步判断子树的情况
            subLeft, subRight = -1, -1
            if root.left.left:
                subLeft = root.left.left.height
            if root.left.right:
                subRight = root.left.right.height
            if subLeft > subRight:
                flag.append("left")
            else:
                flag.append("right")
        else:
            flag.append(root)
            flag.append("right")
            # 进一步判断子树的情况
            subLeft, subRight = -1, -1
            if root.right.left:
                subLeft = root.right.left.height
            if root.right.right:
                subRight = root.right.right.height
            if subLeft > subRight:
                flag.append("left")
            else:
                flag.append("right")

# 左左操作
def LLRotation(curNode, root):
    newRoot = curNode.left
    curNode.left = newRoot.right
    newRoot.right = curNode 

# 右右操作
def RRRotation(curNode, root):
    newRoot = curNode.right
    curNode.right = newRoot.left
    newRoot.left = curNode 
    
# 左右操作和左右操作的时候，实际上是左左操作和右右操作的两种情况组合，
# 对子树操作的时候，不要忘记将更新后的子树的根节点赋予子树源跟节点的父节点的左孩子/右孩子
# 左右操作
def LRRotation(curNode, root):
    newLeft = curNode.left.right
    RRRotation(curNode.left, root)
    curNode.left = newLeft
    LLRotation(curNode, root)

# 左右操作
def RLRotation(curNode, root):
    newRight = curNode.right.left
    LLRotation(curNode.right, root)
    curNode.right = newRight
    RRRotation(curNode, root)

# 寻找失衡节点的父节点
def search(root, node):
    if not root:
        return [] 
    if root.left == node:
        return [root, "left"]
    if root.right == node:
        return [root, "right"] 

    return search(root.left, node) or search(root.right, node)

# 更新树的高度
def update(root):
    if root == None:
        return -1

    root.height = 1 + max(update(root.left), update(root.right))
    return root.height

# 打印树，因为只用了DLR，打出后不美观，之后会进一步处理
def printTree(root):
    if not root:
        return 

    print(root.value, root.height)
    printTree(root.left)
    printTree(root.right)


if __name__ == "__main__":
    nums = list(np.random.randint(low = 1, high = 100, size = 8))
    print(nums)
    root = AVL(nums)
    printTree(root)
