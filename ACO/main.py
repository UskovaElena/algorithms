import math


def open_file(path):
    points = []
    with open(path) as f:
        f.readline()
        for line in f.readlines():
            city = line.split(',')
            points.append([float(city[1]), float(city[2])])
    return points


class AntColony:
    def __init__(self, coordinates):
        self.path = [0] * len(coordinates)
        self.distance = -1
        self.best_distance = -1
        self.best_path = [0] * len(coordinates)
        self.coordinates = coordinates
        self.pheromone = [[1] * (len(coordinates) - 1) for i in range(len(coordinates))]
        self.alpha = 1
        self.beta = 1
        self.ro = 0.5
        self.q = 1

    def run(self):

        return

    #  считаем расстояние между двумя пунктами
    def calc_len(self, city_from, city_to):
        return math.sqrt(self.ccoordinates[city_from][0] * self.ccoordinates[city_to][0] + self.ccoordinates[city_from][1] * self.ccoordinates[city_to][1])

    #  считаем произведение локальной и глобальной "хорошести"
    def calc_cost(self, city_from, city_to, ):
        return pow(self.pheromone[city_from][city_to], self.alpha) * pow(1/self.calc_len(city_from, city_to), self.beta)

    #  считаем сумму вероятноестей всех путей, в которые можем попасть
    def sum_available_ways(self, city_from, available_cities):
        sum = 0
        for city_to in available_cities:
            sum += self.calc_cost(city_from, city_to)
        return sum

    #  обновление феромонов (после нахождения пути)
    def update_pheromone(self):
        d_pheromone = self.q / self.distance
        for i in range(len(self.path) - 1):
            self.pheromone[self.path[i]][self.path[i + 1]] = \
                self.pheromone[self.path[i]][self.path[i + 1]] * self.ro + d_pheromone


ant = AntColony(open_file("C:\\Users\\Polina\\PycharmProject\\ant_colony_TSP\\cities.csv"))
