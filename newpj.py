import math
import random



AllCities = [[16.47, 96.10], [16.47, 94.44], [22.39, 93.37], [25.23, 97.24], [22.00, 96.05], [20.47, 97.02],
             [17.20, 96.29], [20.09, 92.52], [16.30, 97.38], [14.05, 98.12], [16.53, 97.38], [21.52, 95.59],
             [19.41, 97.13], [20.09, 94.54]]

def distancecal (city1 , city2):
    x = (city1[0] + city2[0]) ** 2
    y = (city1[1] + city2[1]) ** 2
    return math.sqrt(x + y)

individual = []
fittest = 10000
fittestpath = []
fittestoffspring = 10000
Final_best_path = []

for All in range(10):
    for o in range(100):
        for i in range(1111):
            individual = AllCities
            random.shuffle(individual)
            for q in range(8):
                r = random.randint(0, 13)
                r2 = random.randint(0, 13)
                w = individual[r]
                individual.pop(r)
                individual.insert(r2, w)

            n = 0
            m = 1
            fitness = 0
            for c in range(13):
                c1 = individual[n]
                c2 = individual[m]
                result = distancecal(c1, c2)
                fitness = result + fitness
                n += 1
                m += 1
            if fitness < fittest:
                fittest = fitness
                fittestpath = individual

        for mutation in range(2):
            rm = random.randint(0, 13)
            rm2 = random.randint(0, 13)
            w1 = fittestpath[rm]
            fittestpath.pop(rm)
            fittestpath.insert(rm2, w1)

        z = 0
        m = 1
        offspringfitness = 0
        for v in range(13):
            s1 = fittestpath[z]
            s2 = fittestpath[m]
            result2 = distancecal(s1, s2)
            offspringfitness = result2 + offspringfitness
            z += 1
            m += 1
        if offspringfitness < fittestoffspring:
            fittestoffspring = offspringfitness
            Final_best_path = fittestpath


print('Best estimated path is:' )
print(Final_best_path)
print('And the fitness of this path is:')
print(fittestoffspring)