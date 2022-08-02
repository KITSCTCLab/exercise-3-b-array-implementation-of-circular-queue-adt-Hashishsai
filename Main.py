import operator
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
    self.stack = []


  def isEmpty(self):
    """
    Check whether the stack is empty.
    Returns:
      True if it is empty, else returns False.
    """
    return self.top == -1


  def mypop(self):
    """
    Do pop operation if the stack is not empty.
    Returns:
      The data which is popped out if the stack is not empty.
    """
    if not self.isEmpty():
        x = self.stack.pop()
        self.top = self.top - 1
        return x


  def push(self, operand):
    """
    Push the operand to stack if the stack is not full.
    Arguments:
      operand: The operand to be pushed.
    """
    self.top += 1
    self.stack.append(operand)


  def validate_postfix_expression(self, expression):
    """
    Check whether the expression is a valid postfix expression.
    Arguments:
      expression: A String which represents the expression to be validated.
    Returns:
      True if the expression is valid, else returns False.
    """
    counter_digit = counter_operand = 0
    for token in expression:
        if token.isdigit():
            counter_digit += 1
        else:
            counter_operand += 1
    return counter_digit == counter_operand + 1


  def evaluate_postfix_expression(self, expression):
    """
    Evaluate the postfix expression
    Arguments:
      expression: A String which represents the the expression to be evaluated
    Returns:
      The result of evaluated postfix expression.
    """
    ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
    }
    for token in expression:
        if token.isdigit():
            self.push(int(token))
        else:
            operand2 = self.mypop()
            operand1 = self.mypop()
            result = ops[token](operand1, operand2)
            self.push(int(result))
    return self.stack[0]
