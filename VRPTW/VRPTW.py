class Shop:
    def __init__(self, a):
        self.id = a[0]
        self.x = a[1]
        self.y = a[2]
        self.demand = a[3]
        self.w_start = a[4]
        self.w_end = a[5]
        self.unloading = a[6]


class VRPTW:

    def __init__(self):
        self.shops = []
        self.n_vehicles = 0
        self.capacity_vehicles = 0

    def read_file(self, path):
        with open(path) as f:
            self.n_vehicles, self.capacity_vehicles  = f.readline().replace('\n','').split(' ')[1:]
            for line in f.readlines():
                self.shops.append(Shop([int(a) for a in line.replace('\n', '').split(' ')[1:-1]]))

alg = VRPTW()
alg.read_file("C:/Users/Polina/PycharmProject/VRPTW/I1.txt")