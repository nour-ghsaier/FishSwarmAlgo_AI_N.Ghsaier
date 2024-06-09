import numpy as np

class Biker:
    def __init__(self, speed, stamina, hydration, bike_weight, technique):
        self.speed = speed
        self.stamina = stamina
        self.hydration = hydration
        self.bike_weight = bike_weight
        self.technique = technique
        self.performance = None

    def evaluate_performance(self):
        # Example objective function: Maximize the weighted sum of parameters
        self.performance = 0.3 * self.speed + 0.2 * self.stamina + 0.15 * self.hydration + \
                           0.1 * (1 / self.bike_weight) + 0.25 * self.technique
                #--->to compute the biker's performance score based on these parameters.


#used to evaluate the performance of each biker and identify the biker with the best performance
class BikerRaceOptimizer:
    def __init__(self, bikers):
        self.bikers = bikers
        self.global_best_performance = None

    def optimize(self):
        for biker in self.bikers:
            biker.evaluate_performance()
            if self.global_best_performance is None or biker.performance > self.global_best_performance:
                self.global_best_performance = biker.performance

# Example usage
n_bikers = 5
bikers = [Biker(np.random.uniform(50, 100), np.random.uniform(50, 90), np.random.uniform(30, 70),
                np.random.uniform(45, 70), np.random.uniform(60, 90)) for _ in range(n_bikers)]

race_optimizer = BikerRaceOptimizer(bikers)
race_optimizer.optimize()

print("Global Best Performance:", race_optimizer.global_best_performance)
#the result represents the optimized performance achieved in the race


#A higher performance score suggests that the biker associated with this score has optimized
# the parameters to achieve the best possible performance in the race.