from collections import deque


class MySolution:
    def predictPartyVictory(self, senate: str) -> str:
        banned_indexes: set[int] = set()
        r_votes = d_votes = 0
        last = ''
        while True:
            num_of_banned_before = len(banned_indexes)
            for i, s in enumerate(senate):
                if i in banned_indexes:
                    continue

                if s == 'R':
                    if d_votes:
                        banned_indexes.add(i)
                        d_votes = max(0, d_votes - 1)
                    else:
                        last = 'R'
                        r_votes += 1
          
                else:
                    if r_votes:
                        banned_indexes.add(i)
                        r_votes = max(0, r_votes - 1)
                    else:
                        last = 'D'
                        d_votes += 1
            
            if len(banned_indexes) == num_of_banned_before:
                return 'Radiant' if last == 'R' else 'Dire'
            

class Solution:
    """Another example of 'make it hard and stupid'."""

    def predictPartyVictory(self, senate: str) -> str:
        rq: deque[int] = deque()
        dq: deque[int] = deque()

        for i, s in enumerate(senate):
            q = rq if s == 'R' else dq
            q.append(i)

        while rq and dq:
            r = rq.popleft()
            d = dq.popleft()
            win_q = rq if r < d else dq
            win_q.append(min(r, d) + len(senate))

        return 'Radiant' if rq else 'Dire'


s = Solution()

assert s.predictPartyVictory("RD") == "Radiant"
assert s.predictPartyVictory("RDD") == "Dire"
assert s.predictPartyVictory("RRDR") == "Radiant"
assert s.predictPartyVictory("RRDDD") == "Radiant"
assert s.predictPartyVictory("RRR") == "Radiant"
assert s.predictPartyVictory("RDRDRD") == "Radiant"
assert s.predictPartyVictory("DDRRR") == "Dire"