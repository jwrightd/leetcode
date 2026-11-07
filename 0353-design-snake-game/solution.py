class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        # have the height x width grid
        # food arr positions
        # lowkey i think we just need to make the grid and place the food

        # then we need a queue to contain the snake as we move, queue[-1] is the head
        # also makes sense to have a set of the indices so we can o1 check when we move
        self.foodIdx = 0
        self.food = food
        self.queue = [(0, 0)]
        self.snake = set()
        self.snake.add((0,0))
        self.width = width
        self.height = height
        self.score = 0



    def move(self, direction):
        """
        :type direction: str
        :rtype: int
        """
        # need to check if we hit side or ourself
        directions = {}
        directions["U"] = [-1, 0]
        directions["D"] = [1, 0]
        directions["R"] = [0, 1]
        directions["L"] = [0, -1]
        
        headY, headX = self.queue[-1]
        updateY, updateX = directions[direction]
        newY, newX = headY + updateY, headX + updateX

        if newX < 0 or newX >= self.width or newY < 0 or newY >= self.height:
            return -1 # hit wall

        found = False
        if self.foodIdx < len(self.food):
            foodY, foodX = self.food[self.foodIdx]
            if newY == foodY and newX == foodX:
                self.score += 1
                self.foodIdx += 1
                found = True

        if (newY, newX) in self.snake:
            if found or (newY, newX) != self.queue[0]:
                return -1 
        if not found:
            removed = self.queue.pop(0)
            self.snake.remove(removed)
        
        # we need to update state
        self.queue.append((newY, newX))
        self.snake.add((newY, newX))
        
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
