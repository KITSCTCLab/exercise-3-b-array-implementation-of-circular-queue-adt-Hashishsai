class Evaluate:
  
  """This class validates and evaluate postfix expression.
  Attributes:
      top: An integer which denotes the index of the element at the top of the stack currently.
      size_of_stack: An integer which represents the size of stack.
      stack: A List which acts as a Stack.
  """
    # Write your code here
    

  def __init__(self, size):

    """Inits Evaluate with top, size_of_stack and stack.
    Arguments:
      size_of_stack: An integer to set the size of stack.
    """
    self.top = -1
    self.size_of_stack = size
    self.stack = [None]*size


  def isEmpty(self):
    """
    Check whether the stack is empty.
    Returns:
      True if it is empty, else returns False.
    """
    return (self.top==-1)


  def pop(self):

    """
    Do pop operation if the stack is not empty.
    Returns:
      The data which is popped out if the stack is not empty.
    """
    if not self.isEmpty():

      k=self.stack[self.top]
      self.top-=1
    return k


  def push(self, operand):
    """
    Push the operand to stack if the stack is not full.
    Arguments:
      operand: The operand to be pushed.
    """
    self.top+=1
    self.stack[self.top]=operand


  def validate_postfix_expression(self, expression):
    """
    Check whether the expression is a valid postfix expression.
    Arguments:
      expression: A String which represents the expression to be validated.
    Returns:
      True if the expression is valid, else returns False.
    """
    operatorcon=0
    operandcon=0
    flag=0
    for i in expression:

      if(not(i=="-" or i=="+" or i=="*" or i=="/" or i=="^")):

        k=int(i)
      if(i=="-" or i=="+" or i=="*" or i=="/" or i=="^"):

        operatorcon+=1
        flag=1
      elif(isinstance(k,int)):    
        operandcon+=1
        flag=1
      else:
        flag=0
        break
    if(flag==1 and operandcon==(operatorcon+1)):
      return True
    else:
      return False


  def evaluate_postfix_expression(self, expression):
    """
    Evaluate the postfix expression
    Arguments:
      expression: A String which represents the the expression to be evaluated
    Returns:
      The result of evaluated postfix expression.
    """
    flag=0
    for i in expression:

      if(not(i=="-" or i=="+" or i=="*" or i=="/" or i=="^")):

        self.push(i)
      else:
        self.push(i)
        operator=self.pop()
        secoperator=self.pop()
        if(operator=="+"):

          self.stack[self.top]=int(self.stack[self.top])+int(secoperator)
        elif(operator=="-"):
          self.stack[self.top]=int(self.stack[self.top])-int(secoperator)
        elif(operator=="*"):
          self.stack[self.top]=int(self.stack[self.top])*int(secoperator)
        elif(operator=="/"):
          flag=1
          self.stack[self.top]=int(self.stack[self.top])/int(secoperator)
        else:
          self.stack[self.top]=int(self.stack[self.top])^int(secoperator)
    
    return int(self.stack[self.top])


# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')


On Tue, Aug 2, 2022, 11:31 AM URK21CO3027 DIDDIKATI HASHISH SAI <diddikatihashish@karunya.edu.in> wrote:
class Solution:
    """This class implements linear queue.
      Attributes:
          stack: A list which maintains the content of stack.
          queue: A list which maintains the content of queue.
          top: An integer which denotes the index of the element at the top of the stack.
          front: An integer which denotes the index of the element at the front of the queue.
          rear: An integer which denotes the index of the element at the rear of the queue.
          size: An integer which represents the size of stack and queue.
      """

    # Write your code here
    def __init__(self, size):
        """Inits Solution with stack, queue, size, top, front and rear.
        Arguments:
          size: An integer to set the size of stack and queue.
        """
        self.stack = []
        self.queue = []
        self.size = size
        self.top = -1
        self.rear = -1
        self.front = -1

    def is_stack_empty(self):
        """
        Check whether the stack is empty.
        Returns:
          True if it is empty, else returns False.
        """
        return self.top == -1

    def is_queue_empty(self):
        """
        Check whether the queue is empty.
        Returns:
          True if it is empty, else returns False.
        """
        return self.front == -1 or self.front > self.rear

    def is_stack_full(self):
        """
        Check whether the stack is full.
        Returns:
          True if it is full, else returns False.
        """
        return self.top == self.size - 1

    def is_queue_full(self):
        """
        Check whether the queue is full.
        Returns:
          True if it is full, else returns False.
        """
        return self.rear == self.size - 1

    def push_character(self, character):
        """
        Push the character to stack, if stack is not full.
        Arguments:
            character: A character that will be pushed to the stack.
        """
        if not self.is_stack_full():
            self.stack.append(character)
            self.top += 1

    def enqueue_character(self, character):
        """
        Enqueue the character to queue, if queue is not full.
        Arguments:
            character: A character that will be enqueued to queue.
        """
        if not self.is_queue_full():
            if  self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue.append(character)

    def pop_character(self):
        """
        Do pop operation if the stack is not empty.
        Returns:
          The data that is popped out if the stack is not empty.
        """
        if not self.is_stack_empty():
            self.top -= 1
            return self.stack.pop(self.top + 1)

    def dequeue_character(self):
        """
        Do dequeue operation if the queue is not empty.
        Returns:
          The data that is dequeued if the queue is not empty.
        """
        if not self.is_queue_empty():
            self.front += 1
            return self.queue[self.front - 1] 
                


# read the string text
text = input()

# find the length of text
length_of_text = len(text)

# Create the Solution class object
solution = Solution(length_of_text)

# push/enqueue all the characters of string text to stack
for index in range(length_of_text):
    solution.push_character(text[index])
    solution.enqueue_character(text[index])

is_palindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both characters
If the comparison fails, set is_palindrome as False.
'''
for index in range(length_of_text):
    if solution.pop_character() != solution.dequeue_character():
        is_palindrome = False


# finally print whether string text is palindrome or not.
if is_palindrome:
    print("The word, " + text + ", is a palindrome.")
else:
    print("The word, " + text + ", is not a palindrome.")
