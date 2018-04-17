#栈 先进后出
#栈可以说是一种数据结构，存数据可以用栈的形式往内存里存，栈可以存数据，
#模拟栈结构 压栈 向栈里存数据
stack = []
stack.append("a")
stack.append("b")
stack.append("c")
print(stack)

#出栈
res = stack.pop()
print(res)
print(stack)


#队列 先进后出
import collections

#创建队列
queue = collections.deque()
print(queue)

#加入队列
queue.append("a")
queue.append("b")
queue.append("c")
print(queue)

resqueue = queue.popleft()
print(resqueue)
print(queue)