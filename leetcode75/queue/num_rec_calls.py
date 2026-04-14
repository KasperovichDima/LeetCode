from collections import deque


class RecentCounter:

    def __init__(self):
        self.q: deque[int] = deque()
        

    def ping(self, t: int) -> int:
        self.q.append(t)
        limit = t - 3_000

        while self.q[0] < limit:
            self.q.popleft()

        return len(self.q)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

rc = RecentCounter()

reqs = [1, 100, 3001, 3002]

for t in reqs:
    print(rc.ping(t))