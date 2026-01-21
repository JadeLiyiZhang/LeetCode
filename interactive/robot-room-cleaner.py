# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        def move():
            if (self.x + self.dx, self.y + self.dy) not in cleaned and robot.move():
                dfs.append((self.dx, self.dy))
                self.x += self.dx
                self.y += self.dy
                return True
            return False

        def turnLeft():
            robot.turnLeft()
            if self.dx == -1 and self.dy == 0:
                self.dx, self.dy = 0, -1
            elif self.dx == 0 and self.dy == -1:
                self.dx, self.dy = 1, 0
            elif self.dx == 1 and self.dy == 0:
                self.dx, self.dy = 0, 1
            else:
                self.dx, self.dy = -1, 0
        
        def backtrack():
            i, j = dfs.pop()
            if self.dx == i and self.dy == j:
                robot.turnLeft()
                robot.turnLeft()
            elif self.dx == i or self.dy == j:
                pass
            elif (self.dx == -1 and self.dy == 0 and i == 0 and j == 1) or (self.dx == 0 and self.dy == 1 and i == 1 and j == 0) or (self.dx == 1 and self.dy == 0 and i == 0 and j == -1) or (self.dx == 0 and self.dy == -1 and i == -1 and j == 0):
                robot.turnLeft()
            else:
                robot.turnRight()
            robot.move()
            self.dx, self.dy = -i, -j
            self.x += self.dx
            self.y += self.dy
                
        """
        :type robot: Robot
        :rtype: None
        """
        cleaned = set()
        self.x, self.y = 0, 0
        self.dx, self.dy = -1, 0
        dfs = ['start']
        while dfs:
            if (self.x, self.y) not in cleaned:
                robot.clean()
                cleaned.add((self.x, self.y))
            # forward
            if move():
                continue
            # left
            turnLeft()
            if move():
                continue
            # backward
            turnLeft()
            if move():
                continue
            # right
            turnLeft()
            if move():
                continue
            # backtrack
            if dfs[-1] == 'start':
                return
            backtrack()