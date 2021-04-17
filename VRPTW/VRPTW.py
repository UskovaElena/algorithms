import math
class Shop:
    def __init__(self, a):
        self.id, self.x, self.y, self.demand, self.w_start, self.w_end, self.unloading = a


class VRPTW:

    def __init__(self):
        self.shops = []
        self.n_vehicles = 0
        self.capacity_vehicles = 0
        self.distances = []

    # read file and fill fields of class
    def fill(self, path):
        with open(path) as f:
            self.n_vehicles, self.capacity_vehicles  = f.readline().replace('\n','').split(' ')[1:]
            for line in f.readlines():
                self.shops.append(Shop([int(a) for a in line.replace('\n', '').split(' ')[1:-1]]))

        for i in range(len(self.shops) - 1):
            self.distances.append([])
            for j in range(i + 1, len(self.shops)):
                self.distances[i].append(math.sqrt(math.pow(self.shops[i].x - self.shops[j].x, 2) +
                                                 math.pow(self.shops[i].y - self.shops[j].y, 2)))

    #find first(initial) solution
    def initial_solution(self):
        return



alg = VRPTW()
alg.fill("C:/Users/Polina/PycharmProject/VRPTW/I1.txt")