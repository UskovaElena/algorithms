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
        self.pheromone = [[1 for j in range(len(coordinates))] for i in range(len(coordinates))]
        self.alpha = 1
        self.beta = 1
        self.ro = 0.5
        self.q = 1

    def run(self, city_from):
        self.distance = 0
        local_available_cities = [i for i in range(len(self.coordinates))]
        local_available_cities.remove(city_from)
        self.path[0] = city_from
        for i in range(1, len(self.coordinates)):
            sum_available = self.sum_available_ways(city_from, local_available_cities)

            # определяем в какую вершину пойдем
            probabilities = [self.calc_cost(city_from, city_to)/sum_available for city_to in local_available_cities]
            next_city = np.random.choice(local_available_cities, p=probabilities)

            local_available_cities.remove(next_city)
            self.path[i] = next_city
            self.distance += self.calc_len(city_from, next_city)
            city_from = next_city

        if self.distance < self.best_distance or self.best_distance == 0:
            self.best_distance = self.distance
            self.best_path = copy.deepcopy(self.path)
        self.update_pheromone()

    #  считаем расстояние между двумя пунктами
    def calc_len(self, city_from, city_to):
        return math.sqrt(pow(self.coordinates[city_from][0] - self.coordinates[city_to][0], 2) +
                         pow(self.coordinates[city_from][1] - self.coordinates[city_to][1], 2))

    #  считаем произведение локальной и глобальной "хорошести"   ЧИСЛИТЕЛЬ
    def calc_cost(self, city_from, city_to):
        return pow(self.pheromone[city_from][city_to], self.alpha) * pow(1/self.calc_len(city_from, city_to), self.beta)

    #  считаем сумму вероятноестей всех путей, в которые можем попасть    ЗНАМЕНАТЕЛЬ
    def sum_available_ways(self, city_from, local_available_cities):
        sum = 0
        for city_to in local_available_cities:
            sum += self.calc_cost(city_from, city_to)
        return sum

    #  обновление феромонов (после нахождения пути муравья)
    def update_pheromone(self):
        for i in range(len(self.pheromone)):
            for j in range(len(self.pheromone[i])):
                self.pheromone[i][j] = (1 - self.ro) * self.pheromone[i][j]
        d_pheromone = self.q / self.distance
        for i in range(len(self.path) - 1):
            self.pheromone[self.path[i]][self.path[i + 1]] += d_pheromone
            self.pheromone[self.path[i+1]][self.path[i]] += d_pheromone


# ant = AntColony(open_file("C:\\Users\\Polina\\PycharmProject\\ant_colony_TSP\\cities.csv"))
ant = AntColony(open_file("C:\\repositories_git\\algorithms\\ACO\\cities.csv"))
available_cities = [i for i in range(len(ant.coordinates))]
for i in range(len(ant.coordinates)):
    city_from_ = random.choice(available_cities)
    available_cities.remove(city_from_)
    for j in range(200):
        ant.run(city_from_)
        print(ant.path, ant.distance)
    ant.pheromone
print(ant.best_distance)
print(ant.best_path)
