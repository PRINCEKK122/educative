from Stack.stack import Stack

# Implement a function called sort_stack() which takes a stack and sorts all of its elements in ascending
# order such that when they are popped and printed, they come out in ascending order.
# So the element that was pushed last to the stack has to be the smallest.
def sort_stack(stack: Stack):
    temp_stack = Stack()
    while not stack.is_empty():
        value = stack.pop()
        if temp_stack.peek() is not None and value >= temp_stack.peek():
            temp_stack.push(value)
        else:
            while not temp_stack.is_empty() and value < temp_stack.peek():
                stack.push(temp_stack.pop())
            temp_stack.push(value)
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack

if __name__ == "__main__":
    stack = Stack()
    stack.push(2)
    stack.push(97)
    stack.push(4)
    stack.push(-20)
    stack.push(-2)

    print("Sorted stack", sort_stack(stack))
    print(2)