class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    def is_empty(self):
        return self.top is None
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0
def is_operand(ch):
    return ch.isalpha() or ch.isdigit()
def infix_to_postfix(expression):
    stack = Stack()
    output = []
    for char in expression:
        if is_operand(char):
            output.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while (not stack.is_empty()) and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  
        else:
            while (not stack.is_empty() and
                   precedence(char) <= precedence(stack.peek())):
                output.append(stack.pop())
            stack.push(char)
    while not stack.is_empty():
        output.append(stack.pop())

    return ''.join(output)
if __name__ == "__main__":
    expression = input()
    print(infix_to_postfix(expression))
