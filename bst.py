import queue
import sys

class tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def treeprint(root):
    if root==None:
        return
    print(root.data)
    treeprint(root.left)
    treeprint(root.right)


def treeprintdetail(root):
    if root==None:
        return
    print(root.data, end=":")
    if root.left!=None:
        print("left",root.left.data,end=" ")
    if root.right != None:
        print("right",root.right.data,end="")
    print("")
    treeprintdetail(root.left)
    treeprintdetail(root.right)

def treeinput():
    i=int(input())
    if i==-1:
        return None
    node=tree(i)
    leftnode=treeinput()
    rightnode=treeinput()
    node.left=leftnode
    node.right=rightnode
    return node


def count(node):
    if node==None:
        return 0
    l=count(node.left)
    r=count(node.right)
    return l+r+1

def sum(node):
    if node==None:
        return 0
    l = count(node.left)
    r = count(node.right)
    return l +r + node.data

def leafnode(root):
    if root==None:
        return 0
    if root.left==None and root.right==None:
        return 1
    l=leafnode(root.left)
    r=leafnode(root.right)
    return l+r

def depth(root,x):
    if x==0:
        print(root.data)
        return
    if root==None:
        return
    l=depth(root.left,x-1)
    r=depth(root.right,x-1)


def replaceWithDepth(root, level=0):
    if root==None:
        return
    replaceWithDepth(root.left, level+1)
    print(level)
    replaceWithDepth(root.right, level+1)

def delleaf(root):
    if root==None:
        return None
    if root.left==None and root.right==None:
        return None
    l=delleaf(root.left)
    r=delleaf(root.right)
    root.left=l
    root.right=r
    return root
def mirror(root):
    if root==None:
        return
    root.left,root.right=root.right,root.left
    mirror(root.left)
    mirror(root.right)
def height(root):
    if root==None:
        return 0
    l=height(root.left)
    r=height(root.right)
    return 1+max(l,r)
def isbalanced(root):
    if root==None:
        return
    lh=height(root.left)
    rh=height(root.right)
    if lh-rh>1 or rh-lh>1:
        return False
    ibl=isbalanced(root.left)
    ibr=isbalanced(root.right)
    if ibl and ibr:
        return True
    else:
        return False
def isbalancedbetter(root):
    if root==None:
        return 0,True
    lh,lbb=isbalancedbetter(root.left)
    rh,rbb=isbalancedbetter(root.right)
    height=1+max(lh,rh)
    if lh-rh>1 or rh-lh>1:
        return height,False
    if lbb and rbb:
        return height,True
    else:
        return height,False

def heightAndDiameter(root):
    if root==None:
        return 0,0
    l=height(root.left)
    r=height(root.right)
    return 1+max(l,r),l+r

def diameter(root):
    if root==None:
        return 0
    option1=height(root.left)+height(root.right)
    option2=diameter(root.left)
    option3=diameter(root.right)
    return max(option1,option2,option3)
def Betterdiameter(root):
    if root==None:
        return 0
    leftHight,leftDiameter=heightAndDiameter(root.left)
    rightHight,rightdiameter=heightAndDiameter(root.right)
    return max(leftDiameter,rightdiameter,leftHight+rightHight)

def LevelWiseInput():
    q=queue.Queue()
    rootData=int(input("Give Root "))
    if rootData==-1:
        return None
    root=tree(rootData)
    q.put(root)
    while ( not (q.empty())):
        current_node=q.get()
        print("enter left child of",current_node.data)
        LeftChilddata=int(input())
        if LeftChilddata!=-1:
            leftChild=tree(LeftChilddata)
            current_node.left=leftChild
            q.put(leftChild)
        print("enter right child of", current_node.data)
        rightChilddata = int(input())
        if rightChilddata != -1:
            rightChild = tree(rightChilddata)
            current_node.right = rightChild
            q.put(rightChild)
    return root

def PrinitLevelwise(root):
    q=queue.Queue()
    if root==None:
        return
    q.put(root)
    while(not(q.empty())):
        current_node=q.get()
        print(current_node.data,end=" ")
        if current_node.left!=None:
            print(": left child of",current_node.data,'is',current_node.left.data,end=" ")
            q.put( current_node.left)
        if current_node.right!=None:
            print(": right child of", current_node.data, 'is', current_node.right.data,end=" ")
            q.put(current_node.right)

        print(" ")

def insertDuplicateNode(root):
    if root==None:
        return
        newdata=root.data
        newnode=BinaryTreeNode(newdata)
        newnode.left=root.left
        root.left=newnode
        insertDuplicateNode(newnode.left)
        insertDuplicateNode(root.right)
        return root

def maxmin(root):
    if root==None:
        return -sys.maxsize,sys.maxsize
    maxi1,mini1=maxmin(root.left)
    maxi2,mini2=maxmin(root.right)

    return max(root.data,maxi1,maxi2),min(root.data,mini1,mini2)



def rootToLeafPathsSumToK(root, k, lst):
    if root==None:
        return
    if root.data<=k:
        lst.append(root.data)
    if root.data==k:
        print(lst)
    if root.data>k:
        return
    rootToLeafPathsSumToK(root.left,k-root.data,lst)
    rootToLeafPathsSumToK(root.right,k-root.data,lst)
    lst.pop()

def buildTreeWithPreIn(preorder,inorder):
    if len(preorder)==0:
        return None
    rootData=preorder[0]
    root=tree(rootData)
    rootIndexInoder=-1
    for i in range(0, len(inorder)):
        if inorder[i]==rootData:
            rootIndexInoder=i
            break
    if rootIndexInoder==-1:
        return
    leftInorder=inorder[0:rootIndexInoder]
    rightInorder=inorder[rootIndexInoder+1:]

    lenLeftSubTree=len(leftInorder)

    leftPreOrder=preorder[1:lenLeftSubTree+1]
    rightPreOrder=preorder[lenLeftSubTree+1:]

    leftChild=buildTreeWithPreIn(leftPreOrder,leftInorder)
    rightChild=buildTreeWithPreIn(rightPreOrder,rightInorder)
    root.left=leftChild
    root.right=rightChild
    return root









print("________________")
pre=[1,2,4,5,3,6,7]
inorder=[4,2,5,1,6,3,7]
root=buildTreeWithPreIn(pre,inorder)
treeprintdetail(root)



