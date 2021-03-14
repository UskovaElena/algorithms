import math
import random
import numpy as np
import copy

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
        self.distance = 0
        self.best_distance = 0
        self.best_path = [0] * len(coordinates)
        self.coordinates = coordinates
        self.pheromone = [[1] * (len(coordinates)) for i in range(len(coordinates))]
        self.alpha = 1
        self.beta = 1
        self.ro = 0.5
        self.q = 1

    def run(self):
        if self.distance < self.best_distance or self.best_distance == 0:
            self.best_distance = self.distance
            self.best_path = copy.deepcopy(self.path)
        self.distance = 0
        city_from = random.randint(0, len(self.coordinates) - 1)
        available_cities = [i for i in range(len(self.coordinates))]
        available_cities.remove(city_from)
        self.path[0] = city_from
        for i in range(1, len(self.coordinates)):
            sum_available = self.sum_available_ways(city_from, available_cities)

            # определяем в какую вершину пойдем
            probabilities = [self.calc_cost(city_from, city_to)/sum_available for city_to in available_cities]
            next_city = np.random.choice(available_cities, p=probabilities)

            available_cities.remove(next_city)
            self.path[i] = next_city
            self.distance += self.calc_len(city_from, next_city)
            city_from = next_city

    #  считаем расстояние между двумя пунктами
    def calc_len(self, city_from, city_to):
        return math.sqrt(pow(self.coordinates[city_from][0] - self.coordinates[city_to][0], 2) + pow(self.coordinates[city_from][1] - self.coordinates[city_to][1], 2))

    #  считаем произведение локальной и глобальной "хорошести"   ЧИСЛИТЕЛЬ
    def calc_cost(self, city_from, city_to):
        return pow(self.pheromone[city_from][city_to], self.alpha) * pow(1/self.calc_len(city_from, city_to), self.beta)

    #  считаем сумму вероятноестей всех путей, в которые можем попасть    ЗНАМЕНАТЕЛЬ
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


# ant = AntColony(open_file("C:\\Users\\Polina\\PycharmProject\\ant_colony_TSP\\cities.csv"))
ant = AntColony(open_file("C:\\repositories_git\\algorithms\ACO\\cities.csv"))
print(ant.pheromone)
for i in range(100):
    ant.run()
    print(ant.path, ant.distance)
print(ant.best_distance)
