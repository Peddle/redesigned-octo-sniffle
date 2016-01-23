from collections import deque

def doOp(a,b,op):
  if op == '+':
    return a + b
  else:
    return a - b

def evaluate(expression):
  stack = deque()
  ops = deque()


  currOp = "+"

  i = 0


  while i < len(expression):

    currChar = expression[i]

    if currChar.isdigit():
      num = ""
      while i < len(expression) and expression[i].isdigit():
        num += expression[i]
        i+=1

      i -= 1

      prev = 0
      if len(stack):
        prev = stack.pop()

      currVal = doOp(prev, int(num), currOp)


      stack.append(currVal)
    elif currChar == '(':
      ops.append(currOp)
      stack.append(0)

      currOp = '+'

    elif currChar == ')':
      currOp = ops.pop()

      b = stack.pop()
      a = stack.pop()

      currVal = doOp(a,b,currOp)

      stack.append(currVal)
    else:
      currOp = currChar


    i+=1


  return stack.pop()

def main():
    print evaluate("5-(4-3)")

if __name__ == '__main__':
    main()