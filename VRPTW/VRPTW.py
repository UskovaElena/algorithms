import math


class Shop:
    def __init__(self, a):
        self.id, self.x, self.y, self.demand, self.w_start, self.w_end, self.service_time = a


class Vehicle:
    def __init__(self, capacity):
        self.path = []
        self.time = 0
        self.cargo_remains = capacity


class VRPTW:

    def __init__(self):
        self.shops = []
        self.n_vehicles = 0
        self.capacity = 0
        self.distances = []
        self.vehicles = []
        self.visited = []

    # read file and fill fields of class
    def fill(self, path):
        with open(path) as f:
            self.n_vehicles, self.capacity = [int(a) for a in f.readline().replace('\n','').split(' ')[1:]]
            for line in f.readlines():
                self.shops.append(Shop([int(a) for a in line.replace('\n', '').split(' ')[1:-1]]))

        for i in range(len(self.shops) - 1):
            self.distances.append([])
            for j in range(i + 1, len(self.shops)):
                self.distances[i].append(math.sqrt(math.pow(self.shops[i].x - self.shops[j].x, 2) +
                                                 math.pow(self.shops[i].y - self.shops[j].y, 2)))


    #find first(initial) solution
    def initial_solution(self):
        self.vehicles.append(Vehicle(self.capacity))
        self.vehicles[-1].path.append(0)
        best_shop = 0
        best_time = self.distances[0][1]
        while self.vehicles[-1].cargo_remains > 0:         #0?
            for id in range(1, len(self.shops)):
                i = id
                j = self.vehicles[-1].path[-1]
                if id > self.vehicles[-1].path[-1]:
                    i, j = j, i
                if (id not in self.visited and
                     self.shops[id].w_start <= self.vehicles[-1].time + self.distances[i][j - i - 1] <= self.shops[id].w_end and
                     self.distances[i][j - i - 1] < best_time and
                     self.vehicles[-1].cargo_remains >= self.shops[id].demand):
                    best_shop = id
                    best_time = self.distances[0][id-1]

            print (best_shop not in self.visited, best_shop)
            self.vehicles[-1].path.append(best_shop)
            self.visited.append(best_shop)
            self.vehicles[-1].cargo_remains -= self.shops[best_shop].demand
            self.vehicles[-1].time += best_time + self.shops[best_shop].service_time
        print(self.vehicles[-1].path)




alg = VRPTW()
alg.fill("C:/repositories_git/algorithms/VRPTW/I1.txt")
alg.initial_solution()