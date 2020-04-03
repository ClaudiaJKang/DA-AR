from sys import stdin

read = lambda: stdin.readline().rstrip()


def preorder(node):
    global cnt, tree
    if node.child == []:
        cnt += 1
    for child in node.child:
        preorder(tree[child])


class Node:
    def __init__(self):
        self.child = []

    def setChild(self, node):
        self.child.append(node)

    def removeChild(self, node):
        self.child.remove(node)


n = int(read())
tree = [Node() for _ in range(n)]
cnt = 0
parent = list(map(int, read().split()))
root = 0

for i in range(n):
    if parent[i] != -1:
        tree[parent[i]].setChild(i)
    else:
        root = i

if n != 1:
    i = int(read())
    if parent[i] == -1:
        cnt = 0

    else:
        tree[parent[i]].removeChild(i)
        preorder(tree[root])

print(cnt)
