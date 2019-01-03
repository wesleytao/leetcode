# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        pre = None
        treestack = []
        treestack.append(root)
        result = []
        cumsum = 0  # define as the cumsum from last layer

        while treestack:
            node = treestack[-1]  # last one
            # treestack.pop()

            # no child
            if not node.right and not node.left:
                if (cumsum + node.val) == sum:
                    result.append(treestack.copy())  # we found one result
                else:
                    pass  # no good go back to last element
                pre = node
                treestack.pop()
                continue

            # one child
            elif node.right and not node.left:
                if pre != node.right:
                    cumsum += node.val
                    treestack.append(node.right)
                else:
                    cumsum -= node.val  # it means we have visited before deducted before going back
                    treestack.pop()
                pre = node
                continue

            elif node.left and not node.right:
                if pre != node.left:
                    cumsum += node.val
                    treestack.append(node.left)
                else:
                    cumsum -= node.val
                    treestack.pop()

                pre = node
                continue

            # two child              
            elif node.right and node.left:
                if pre == node.right:
                    # we visited them all
                    cumsum -= node.val
                    treestack.pop()

                elif pre == node.left:
                    # we visited parent before
                    treestack.append(node.right)
                    # cumsum += node.val

                else:
                    treestack.append(node.left)
                    cumsum += node.val

                pre = node
                continue


            else:
                raise ValueError("something wrong")
        return result

def main():
    # mylist = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    root = TreeNode(5)
    root.left = TreeNode(9)
    root.right = TreeNode(10)
    root.left.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root .right.right = TreeNode(1)
    sum = 16
    mysolution = Solution()
    a = mysolution.pathSum(root, sum)
    # print(a)
    result = [[item.val for item in sublist] for sublist in a]
    # for node in a:
    #     print(node)
    print(result)



if __name__ == "__main__":
    main()