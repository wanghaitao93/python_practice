# -*- encoding=utf-8 -*-
import Queue

# 参考http://www.cnblogs.com/itogo/p/5635629.html

# 队列 First in First Out
# class Queue.Queue(maxsize=0)
q = Queue.Queue()
for i in range(5):
    q.put(i)
while q.qsize():
    print q.get()

# 栈 Last in First Out
# class Queue.LifoQueue(maxsize=0)
s = Queue.LifoQueue()
for i in range(5):
    s.put(i)
while s.qsize():
    print s.get()
    
# 优先队列 
# class Queue.PriorityQueue(maxsize=0)
class Job(object):
    def __init__(self, priority):
        self.priority = priority
        self.describe = 'for: %s' % priority 
        print 'put:', priority 
        return
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

q_p = Queue.PriorityQueue()
q_p.put(Job(3))
q_p.put(Job(2))
q_p.put(Job(4))
q_p.put(Job(1))

while(q_p.qsize()):
    print q_p.get().describe


# 双端队列
from collections import deque
d = deque('bc')
d.append('d')
d.appendleft('a')
print d

d.pop()
d.popleft()
print d

d = deque()
d.append(['aa', 'bb'])
d += ['cc', 'dd']
print d








