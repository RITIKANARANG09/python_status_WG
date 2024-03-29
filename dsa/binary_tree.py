from node import Node

class BinaryTree:
    def __init__(self,head:Node):
        self.head=head

    def add(self,new_node:Node):
        current_node=self.head
        while current_node:
            if current_node.value==new_node.value:
                raise ValueError('A node with that value already exists')
            elif new_node.value<current_node.value:
                if current_node.left:
                    current_node=current_node.left
                else:
                    current_node.left=new_node
                    break
            elif new_node.value>current_node.value:
                if current_node.right:
                    current_node=current_node.right
                else:
                    current_node.right=new_node
                    break

    def inorder(self):
        self._inorder_recursive(self.head)

    def _inorder_recursive(self,head):
      if not head:
          return
      self._inorder_recursive(head.left)
      print(head)
      self._inorder_recursive(head.right)

    def find(self,value):
        current_node=self.head
        while current_node:
            if value>current_node.value:
                current_node=current_node.right
            elif value<current_node.value:
                current_node=current_node.left
            else:
                return current_node
        raise LookupError(f'A node with value {value} was not found.')

    def find_parent(self,value:int)->Node:
        if self.head and self.head.value==value
            return self.head

        current_node=self.head
        while current_node:
            if (current_node.left and current_node.left.value==value) or \
                    (current_node.right and current_node.right
                    .value):
                return current_node
            elif value>current_node.value:
                current_node=current_node.right
            elif value<current_node.left.value:
                current_node=current_node.left

    def find_rightmost(self,node:Node)->Node:
        current_node=node
        while current_node.right:
            current_node=current_node.right
        return current_node
    def delete(self,value:int):
        to_delete=self.find(value)
        to_delete_parent=self.find_parent(value)

        if to_delete.left and to_delete.right:
            #2 child
            rightmost=self.find_rightmost(to_delete.left)
            rightmost_parent=self.find_parent(rightmost.value)

            if to_delete==to_delete_parent.right:
                if rightmost_parent != to_delete:
                    rightmost_parent.right = rightmost.left
                    rightmost.left = to_delete.left
                rightmost.right=to_delete.right
                to_delete_parent.right=rightmost
            elif to_delete==to_delete_parent.left:
                if rightmost_parent != to_delete:
                    rightmost_parent.right = rightmost.left
                    rightmost.left = to_delete.left
                rightmost.right=to_delete.right
                to_delete_parent.left=rightmost
            else:
                if rightmost_parent!=to_delete:
                    rightmost_parent.right = rightmost.left
                    rightmost.left = to_delete.left
                rightmost.right=to_delete.right
                self.head=rightmost
        elif to_delete.left or to_delete.right:
            #1 child
            if to_delete==to_delete_parent.left:
                to_delete_parent.left=to_delete.left or to_delete.right
            elif to_delete==to_delete_parent.right:
                to_delete_parent.right=to_delete.left or to_delete.right
            else:
                self.head=to_delete.right or to_delete.left
        else:
            if to_delete==to_delete_parent.left:
                to_delete_parent.left=None
            elif to_delete==to_delete_parent.right:
                to_delete_parent.right=None
            else:
                self.head=None

