import numpy as np 

class Node:
    def __init__(self, value = None, height = 0, left = None, right = None):
        self.value = value
        self.height = height
        self.left = left
        self.right = right


def AVL(nums):
    root = None 
    for value in nums:
        flag = []
        # 构建二叉搜索树
        root = insert(root, value)
        # 更新树的高度
        update(root)
        # 判断失衡点
        judge(root, flag)
        # 当存在失衡点
        if len(flag) == 3:
            # 按照失衡点的父节点分为两种情况
            if flag[0] == root:
                if flag[1] == "left" and flag[2] == "left":
                    newRoot = root.left
                elif flag[1] == "left" and flag[2] == "right":
                    newRoot = root.left.right
                elif flag[1] == "right" and flag[2] == "right":
                    newRoot = root.right
                elif flag[1] == "right" and flag[2] == "left":
                    newRoot = root.right.left

                if flag[1] == "left" and flag[2] == "left":
                    LLRotation(flag[0], root)
                elif flag[1] == "left" and flag[2] == "right":
                    LRRotation(flag[0], root)
                elif flag[1] == "right" and flag[2] == "right":
                    RRRotation(flag[0], root)
                else:
                    RLRotation(flag[0], root)

                root = newRoot
            else:
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

    return root

def insert(root, value):
    if root == None:
        root = Node(value, 0)
    elif value <= root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root

def judge(root, flag):
    if not root:
        return 

    leftHeight, rightHeight = -1, -1 
    if root.left:
        leftHeight = root.left.height
    if root.right:
        rightHeight = root.right.height
    if abs(leftHeight - rightHeight) < 2:
        if root.left:
            judge(root.left, flag)
        if root.right:
            judge(root.right, flag)
    else:
        if leftHeight > rightHeight:
            flag.append(root)
            flag.append("left")
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
            subLeft, subRight = -1, -1
            if root.right.left:
                subLeft = root.right.left.height
            if root.right.right:
                subRight = root.right.right.height
            if subLeft > subRight:
                flag.append("left")
            else:
                flag.append("right")

def LLRotation(curNode, root):
    newRoot = curNode.left
    curNode.left = newRoot.right
    newRoot.right = curNode 

def RRRotation(curNode, root):
    newRoot = curNode.right
    curNode.right = newRoot.left
    newRoot.left = curNode 

def LRRotation(curNode, root):
    newLeft = curNode.left.right
    RRRotation(curNode.left, root)
    curNode.left = newLeft
    LLRotation(curNode, root)

def RLRotation(curNode, root):
    newRight = curNode.right.left
    LLRotation(curNode.right, root)
    curNode.right = newRight
    RRRotation(curNode, root)

def search(root, node):
    if not root:
        return [] 
    if root.left == node:
        return [root, "left"]
    if root.right == node:
        return [root, "right"] 

    return search(root.left, node) or search(root.right, node)

def update(root):
    if root == None:
        return -1

    root.height = 1 + max(update(root.left), update(root.right))
    return root.height

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