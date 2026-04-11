# 1. Irregular shape
```
import random
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon

coords = [(1, 1), (10, 95), (40, 70), (50, 50),(30,20)]
map = Polygon(coords)

x_point = []
y_point = []

coords = [(1, 1), (10, 95), (40, 70), (50, 50),(30,20)]
map = Polygon(coords)

x, y = zip(*coords)
plt.plot(x + (x[0],), y + (y[0],), color="red")

inside = 0
outside = 0

for _ in range(1000):
    x_rand = random.uniform(0, 60)
    y_rand = random.uniform(0, 100)
    point = Point(x_rand, y_rand)
    if map.contains(point):
        inside += 1
        x_point.append(x_rand)
        y_point.append(y_rand)
    else:
        outside += 1
        plt.plot(x_rand, y_rand, 'ro', alpha=0.1)

plt.plot(x_point, y_point, 'go', alpha=0.1)
plt.title(f'Points Inside and Outside the Polygon\nInside: {inside}, Outside: {outside}')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

area_map = map.area
predicted_area = (inside / (inside + outside)) * (60 * 100)
print(f"Predicted Area: {predicted_area}, Actual Area: {area_map}")

plt.show()
```

# 2. Gambling game
```
import random
import matplotlib.pyplot as plt

class GamblingGame:
    def __init__(self):
        self.serial = 0
        self.cum_head = 0
        self.cum_tail = 0

    def run(self):
        while True:
             self.serial += 1
             random_num = random.randint(0, 1)
             if random_num == 0:
                 self.cum_head += 1
             else:
                 self.cum_tail += 1
             diff = abs(self.cum_head - self.cum_tail)
             if diff == 3:
                 return 8 - self.serial

if __name__ == "__main__":
    run = 50
    total_rev = 0

    while run > 0:
        game = GamblingGame()
        total_rev += game.run()
        run -= 1
    
    print("Total rev : ", total_rev)
```

# 3. Numerical
```
import random
import matplotlib.pyplot as plt

def fun(x):
    return x**3

class NumericalIntegration:
    def __init__(self, range_x_in, range_x_out, range_y_in, range_y_out, iteration=50):
        self.inside = 0
        self.outside = 0
        self.iteration = iteration
        self.range_x_in = range_x_in
        self.range_x_out = range_x_out
        self.range_y_in = range_y_in
        self.range_y_out = range_y_out

    def run(self):
        iteration = self.iteration
        while iteration > 0:
            random_num_x = random.uniform(self.range_x_in, self.range_x_out)
            random_num_y = random.uniform(self.range_y_in, self.range_y_out)

            y_real_value = fun(random_num_x)
            if random_num_y <= y_real_value:
                self.inside += 1
            else:
                self.outside += 1
            
            iteration -= 1
    
    def area_approximate(self):
        self.run()

        rectangle_area = (self.range_x_out - self.range_x_in) * (self.range_y_out - self.range_y_in)
        return (self.inside / (self.inside + self.outside) * rectangle_area)

areaFinder = NumericalIntegration(2, 5, 0, 140, 10000)
print(areaFinder.area_approximate())
```
# 4. Pi
```
import random, math
import matplotlib.pyplot as plt

def fun(x):
    return math.sqrt(1-x*x)

class PiEstimation:
    def __init__(self, range_x_in, range_x_out, range_y_in, range_y_out, iteration=50):
        self.inside = 0
        self.outside = 0
        self.iteration = iteration
        self.range_x_in = range_x_in
        self.range_x_out = range_x_out
        self.range_y_in = range_y_in
        self.range_y_out = range_y_out

    def run(self):
        iteration = self.iteration
        while iteration > 0:
            random_num_x = random.random()
            random_num_y = random.random()

            y_real_value = fun(random_num_x)
            if random_num_y <= y_real_value:
                self.inside += 1
            else:
                self.outside += 1
            
            iteration -= 1
    
    def area_approximate(self):
        self.run()
        return (self.inside / (self.inside + self.outside) * 4)

areaFinder = PiEstimation(0, 1, 0, 1, 1000000)
print(areaFinder.area_approximate())
```

# 5. Random walk
```
import random
import matplotlib.pyplot as plt

class RandomWalkProblem:
    def __init__(self, step_limit=100):
        self.x_pos = 0
        self.y_pos = 0
        self.step_limit = step_limit
        self.history = [(self.x_pos, self.y_pos)]
    
    def run(self):
        for _ in range(self.step_limit):
            ransom_num = random.randint(0, 9)
            if ransom_num <= 5:
                self.y_pos += 1 # Move up
            elif ransom_num <= 8:
                self.x_pos -= 1 # Move left
            else:
                self.x_pos += 1 # Move right
        return (self.x_pos, self.y_pos)
    
    def plot(self):
        x_vals = [pos[0] for pos in self.history]
        y_vals = [pos[1] for pos in self.history]

        plt.plot(x_vals, y_vals, marker='o')
        plt.title('Random Walk Path')
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.grid()
        plt.show()

    def multi_run(self, runs=10):
        results = []
        for _ in range(runs):
            result = self.run()
            results.append(result)
            self.x_pos = 0
            self.y_pos = 0
            self.history = [(self.x_pos, self.y_pos)]
        # print("Results of each run: ", results)

        plt.plot([res[0] for res in results], [res[1] for res in results], 'ro', alpha=0.1)
        plt.title('Random Walk End Positions')
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.xlim(-self.step_limit, self.step_limit)
        plt.ylim(-self.step_limit, self.step_limit)
        plt.grid()
        plt.show()

if __name__ == "__main__":
    walk = RandomWalkProblem(step_limit=100)
    walk.multi_run(1000)
```
# 6. walk 3D


