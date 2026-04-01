
class Solution:
    """
    + right
    - left
    """
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        self.res: list[int] = [asteroids[0]]
        for i in range(1, len(asteroids)):
            if self.they_will_collide(asteroids[i]):
                self.process_collision(asteroids[i])
            else:
                self.res.append(asteroids[i])

        return self.res
    
    def they_will_collide(self, asteroid: int) -> bool:
        return bool(self.res) and (self.res[-1] > 0 and asteroid < 0)
    
    def process_collision(self, asteroid: int) -> None:
        """Here we know that this asteroid will collide with previous one.
        
        3 scenarios:
        1. they r eq - annihilation
        2. new one is bigger than last - destroy all smaller prev
        3. new one is smaller and just explodes.
        """
        while self.res and self.res[-1] > 0:

            if abs(asteroid) < self.res[-1]:
                return # new one exploded
            elif abs(asteroid) == self.res[-1]:
                self.res.pop()
                return # total annihillation
            else:
                self.res.pop() # new one hits old one
            
        self.res.append(asteroid)
                
    
s = Solution()

assert (s.asteroidCollision(asteroids = [5,10,-5])) == [5,10]
assert (s.asteroidCollision(asteroids = [8,-8])) == []
assert (s.asteroidCollision(asteroids = [10,2,-5])) == [10]
assert (s.asteroidCollision(asteroids = [3,5,-6,2,-1,4])) == [-6,2,4]
assert (s.asteroidCollision(asteroids = [-2,-2,1,-2])) == [-2,-2,-2]
assert (s.asteroidCollision(asteroids = [8,-8, 11])) == [11]
