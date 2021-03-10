import math


def open_file(path):
    points = []
    with open(path) as f:
        f.readline()
        for line in f.readlines():
            city = line.split(',')
            points.append([float(city[1]), float(city[2])])
    return points


def calc_len(x, y):
    return math.sqrt(x*x + y*y)


class AntColony:
    def __init__(self, coordinates):
        self.path = [0] * len(coordinates)
        self.distance = -1
        self.coordinates = coordinates
        self.alpha = 1
        self.beta = 1
        self.ro = 0.5
        self.q = 1

    def run(self):

        return

    def update_pheromone(self):
        return


ant = AntColony(open_file("C:\\Users\\Polina\\PycharmProject\\ant_colony_TSP\\cities.csv"))
