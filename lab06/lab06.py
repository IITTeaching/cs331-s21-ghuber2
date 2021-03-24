from unittest import TestCase


################################################################################
# STACK IMPLEMENTATION (DO NOT MODIFY THIS CODE)
################################################################################

class Stack:
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next  = next

    def __init__(self):
        self.top = None

    def push(self, val):
        self.top = Stack.Node(val, self.top)

    def pop(self):
        assert self.top, 'Stack is empty'
        val = self.top.val
        self.top = self.top.next
        return val

    def peek(self):
        return self.top.val if self.top else None

    def empty(self):
        return self.top == None

    def __bool__(self):
        return not self.empty()

    def __repr__(self):
        if not self.top:
            return ''
        return '--> ' + ', '.join(str(x) for x in self)

    def __iter__(self):
        n = self.top
        while n:
            yield n.val
            n = n.next

################################################################################
# CHECK DELIMITERS
################################################################################
def check_delimiters(expr):
    """Returns True if and only if `expr` contains only correctly matched delimiters, else returns False."""
    delim_openers = '{([<'
    delim_closers = '})]>'

    ### BEGIN SOLUTION
    stack=Stack()
    for char in list(expr):
        if char in delim_openers:
            stack.push(char)
        if char in delim_closers :
            if not stack.empty() and delim_openers.index(stack.peek())==delim_closers.index(char):
                stack.pop()
            else:
                return False
        
    return stack.empty()
        
    ### END SOLUTION

################################################################################
# CHECK DELIMITERS - TEST CASES
################################################################################
# points: 5
def test_check_delimiters_1():
    tc = TestCase()
    tc.assertTrue(check_delimiters('()'))
    tc.assertTrue(check_delimiters('[]'))
    tc.assertTrue(check_delimiters('{}'))
    tc.assertTrue(check_delimiters('<>'))

# points:5
def test_check_delimiters_2():
    tc = TestCase()
    tc.assertTrue(check_delimiters('([])'))
    tc.assertTrue(check_delimiters('[{}]'))
    tc.assertTrue(check_delimiters('{<()>}'))
    tc.assertTrue(check_delimiters('<({[]})>'))

# points: 5
def test_check_delimiters_3():
    tc = TestCase()
    tc.assertTrue(check_delimiters('([] () <> [])'))
    tc.assertTrue(check_delimiters('[{()} [] (<> <>) {}]'))
    tc.assertTrue(check_delimiters('{} <> () []'))
    tc.assertTrue(check_delimiters('<> ([] <()>) <[] [] <> <>>'))

# points: 5
def test_check_delimiters_4():
    tc = TestCase()
    tc.assertFalse(check_delimiters('('))
    tc.assertFalse(check_delimiters('['))
    tc.assertFalse(check_delimiters('{'))
    tc.assertFalse(check_delimiters('<'))
    tc.assertFalse(check_delimiters(')'))
    tc.assertFalse(check_delimiters(']'))
    tc.assertFalse(check_delimiters('}'))
    tc.assertFalse(check_delimiters('>'))

# points: 5
def test_check_delimiters_5():
    tc = TestCase()
    tc.assertFalse(check_delimiters('( ]'))
    tc.assertFalse(check_delimiters('[ )'))
    tc.assertFalse(check_delimiters('{ >'))
    tc.assertFalse(check_delimiters('< )'))

# points: 5
def test_check_delimiters_6():
    tc = TestCase()
    tc.assertFalse(check_delimiters('[ ( ] )'))
    tc.assertFalse(check_delimiters('((((((( ))))))'))
    tc.assertFalse(check_delimiters('< < > > >'))
    tc.assertFalse(check_delimiters('( [] < {} )'))

################################################################################
# INFIX -> POSTFIX CONVERSION
################################################################################

def infix_to_postfix(expr):
    """Returns the postfix form of the infix expression found in `expr`"""
    # you may find the following precedence dictionary useful
    prec = {'*': 2, '/': 2,
            '+': 1, '-': 1}
    ops = Stack()
    postfix = []
    toks = expr.split()
    top=ops.peek()
    ### BEGIN SOLUTION
    for tok in toks:
      flag=False
      while not flag:
        flag=True
        top=ops.peek()
        if tok.isdigit():
          postfix.append(tok)
        elif ops.empty() or ops.peek()=="(":
          ops.push(tok)
        elif tok=="(":
          ops.push(tok)
        elif tok ==")":
          val=ops.pop()
          while val!="(":
            postfix.append(val)
            val=ops.pop()
        elif top in prec:
          if prec[top]<prec[tok]:
            ops.push(tok)
          if prec[top]==prec[tok]:
            postfix.append(ops.pop())
            ops.push(tok)
          if prec[top]>prec[tok]:
            postfix.append(ops.pop())
            flag=False
        else:
          print("elso")
          ops.push(tok)
        
    while not ops.empty():
      postfix.append(ops.pop())
      
    ### END SOLUTION
    return ' '.join(postfix)

################################################################################
# INFIX -> POSTFIX CONVERSION - TEST CASES
################################################################################

# points: 10
def test_infix_to_postfix_1():
    tc = TestCase()
    tc.assertEqual(infix_to_postfix('1'), '1')
    tc.assertEqual(infix_to_postfix('1 + 2'), '1 2 +')
    tc.assertEqual(infix_to_postfix('( 1 + 2 )'), '1 2 +')
    tc.assertEqual(infix_to_postfix('1 + 2 - 3'), '1 2 + 3 -')
    tc.assertEqual(infix_to_postfix('1 + ( 2 - 3 )'), '1 2 3 - +')

# points: 10
def test_infix_to_postfix_2():
    tc = TestCase()
    tc.assertEqual(infix_to_postfix('1 + 2 * 3'), '1 2 3 * +')
    tc.assertEqual(infix_to_postfix('1 / 2 + 3 * 4'), '1 2 / 3 4 * +')
    tc.assertEqual(infix_to_postfix('1 * 2 * 3 + 4'), '1 2 * 3 * 4 +')
    tc.assertEqual(infix_to_postfix('1 + 2 * 3 * 4'), '1 2 3 * 4 * +')

# points: 10
def test_infix_to_postfix_3():
    tc = TestCase()
    tc.assertEqual(infix_to_postfix('1 * ( 2 + 3 ) * 4'), '1 2 3 + * 4 *')
    tc.assertEqual(infix_to_postfix('1 * ( 2 + 3 * 4 ) + 5'), '1 2 3 4 * + * 5 +')
    tc.assertEqual(infix_to_postfix('1 * ( ( 2 + 3 ) * 4 ) * ( 5 - 6 )'), '1 2 3 + 4 * * 5 6 - *')

################################################################################
# QUEUE IMPLEMENTATION
################################################################################
class Queue:
    def __init__(self, limit=10):
        self.data = [None] * limit
        self.head = -1
        self.tail = -1
        

    ### BEGIN SOLUTION
    ### END SOLUTION

    def enqueue(self, val):
        ### BEGIN SOLUTION
        
        if self.tail-self.head+1==len(self.data):
          raise RuntimeError
        if(self.head==-1):
          self.head=0
        self.tail+=1
        if self.tail>=len(self.data):
          self.tail=0
        if(self.data[self.tail]!=None):
          raise RuntimeError
        self.data[self.tail]=val
        ### END SOLUTION

    def dequeue(self):
        ### BEGIN SOLUTION
        if self.head==len(self.data):
          self.head=0
        if self.tail==-1 and self.head==-1 :
          raise RuntimeError
        val=self.data[self.head]
        self.data[self.head]=None
        self.head+=1
        if self.head-1==self.tail and not self.data[0] and len(self.data) == self.head:
          self.head = -1
          self.tail = -1
        return val
        
        ### END SOLUTION

    def resize(self, newsize):
        assert(len(self.data) < newsize)
        ### BEGIN SOLUTION
        temp=[None]*newsize
        idx=self.head
        i=0
        while self.data[idx]!=None and idx!=self.tail+1:
          temp[i]=self.data[idx]
          idx+=1
          if idx==len(self.data):
            idx=0
          if(idx==self.head):
            break
          i+=1
        self.data=temp
        self.head=0
        self.tail=i

        ### END SOLUTION

    def empty(self):
        ### BEGIN SOLUTION
        return self.head>self.tail or (self.tail==self.head and self.tail==0) or (self.tail==self.head and self.data[self.tail]==None)

        ### END SOLUTION

    def __bool__(self):
        return not self.empty()

    def __str__(self):
        if not(self):
            return ''
        return ', '.join(str(x) for x in self)

    def __repr__(self):
        return str(self)

    def __iter__(self):
        ### BEGIN SOLUTION
        idx=self.head
        while self.data[idx]!=None and idx!=self.tail+1:
          yield(self.data[idx])
          idx+=1
          if idx==len(self.data):
            idx=0

        ### END SOLUTION

################################################################################
# QUEUE IMPLEMENTATION - TEST CASES
################################################################################

# points: 13
def test_queue_implementation_1():
    tc = TestCase()

    q = Queue(5)
    tc.assertEqual(q.data, [None] * 5)

    for i in range(5):
        q.enqueue(i)

    with tc.assertRaises(RuntimeError):
        q.enqueue(5)
    
    for i in range(5):
        tc.assertEqual(q.dequeue(), i)

    tc.assertTrue(q.empty())

# points: 13
def test_queue_implementation_2():
	tc = TestCase()

	q = Queue(10)

	for i in range(6):
	    q.enqueue(i)

	tc.assertEqual(q.data.count(None), 4)

	for i in range(5):
	    q.dequeue()

	tc.assertFalse(q.empty())
	tc.assertEqual(q.data.count(None), 9)
	tc.assertEqual(q.head, q.tail)
	tc.assertEqual(q.head, 5)

	for i in range(9):
	    q.enqueue(i)

	with tc.assertRaises(RuntimeError):
	    q.enqueue(10)

	for x, y in zip(q, [5] + list(range(9))):
	    tc.assertEqual(x, y)

	tc.assertEqual(q.dequeue(), 5)
	for i in range(9):
	    tc.assertEqual(q.dequeue(), i)

	tc.assertTrue(q.empty())

# points: 14
def test_queue_implementation_3():
	tc = TestCase()

	q = Queue(5)
	for i in range(5):
	    q.enqueue(i)
	for i in range(4):
	    q.dequeue()
	for i in range(5, 9):
	    q.enqueue(i)

	with tc.assertRaises(RuntimeError):
	    q.enqueue(10)

	q.resize(10)

	for x, y in zip(q, range(4, 9)):
	    tc.assertEqual(x, y)

	for i in range(9, 14):
	    q.enqueue(i)

	for i in range(4, 14):
	    tc.assertEqual(q.dequeue(), i)

	tc.assertTrue(q.empty())
	tc.assertEqual(q.head, -1)

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "*" + "\n" + f.__name__)

def say_success():
    print("SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_check_delimiters_1,
              test_check_delimiters_2,
              test_check_delimiters_3,
              test_check_delimiters_4,
              test_check_delimiters_5,
              test_check_delimiters_6,
              test_infix_to_postfix_1,
              test_infix_to_postfix_2,
              test_infix_to_postfix_3,
              test_queue_implementation_1,
              test_queue_implementation_2,
              test_queue_implementation_3]:
        say_test(t)
        t()
        say_success()


if __name__ == '__main__':
    main()
