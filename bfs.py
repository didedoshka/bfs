class queue():
    def __init__(self):
        self.items = []
    def offer(self, item):
        self.items.append(item)
    def poll(self):
        return self.items.pop(0)
    def empty(self):
        return not len(self.items)


g = []

n = int(input())
for k in range(n):
    g.append([int(f) for f in input().split()])

start, end = [int(s) for s in input().split()]; start -= 1; end -= 1

d = [None] * n

def bfs(s):
    q = queue()
    d[s] = 0
    q.offer(s)
    while not q.empty():
        v = q.poll()
        for i in range(n):
            if g[v][i] == 1 and d[i] is None:
                d[i] = d[v] + 1
                q.offer(i)

bfs(start)

if d[end] is None:
    print(-1)
    exit(0)

print(d)