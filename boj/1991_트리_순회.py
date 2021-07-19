class Node:
   def __init__(self,value):
      self.value = value
      self.left= None
      self.right= None

def Preorder(node):
   if node.value =='.':
      return
   print(node.value,end='')
   Preorder(node.left)
   Preorder(node.right)

def Inorder(node):
   if node.value == '.':
      return
   Inorder(node.left)
   print(node.value,end='')
   Inorder(node.right)

def Postorder(node):
   if node.value == '.':
      return
   Postorder(node.left)
   Postorder(node.right)
   print(node.value,end='')

cur=None
def search(start,target):
   global cur
   if start.value == target:
      cur=start
      return
   if start.left != None:
      search(start.left,target)
   if start.right != None:
      search(start.right,target)


n=int(input())
head=None
for i in range(n):
   root,left,right=input().split(' ')
   if i == 0:
      head=Node(root)
      head.left=Node(left)
      head.right=Node(right)
   else:
      search(head,root)
      cur.left=Node(left)
      cur.right=Node(right)
      
Preorder(head)
print()
Inorder(head)
print()
Postorder(head)
