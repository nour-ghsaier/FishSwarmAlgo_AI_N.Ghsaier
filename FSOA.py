import numpy as np #used for numerical computation


#Fish Class represents an individual fish in the swarm
class Fish:
    def __init__(self, n_dim, lower_bound, upper_bound):
        self.position = np.random.uniform(lower_bound, upper_bound, n_dim) #sampled from a uniform distribution within the specified lower and upper bounds in each dimension of the search space
        self.velocity = np.zeros(n_dim) #initial velocity=0
        self.fitness = None #will hold the fitness value of the fish evaluated based on the objective function
        self.personal_best_position = self.position.copy() # will be updated as the fish explores the search space
        self.personal_best_fitness = None # //

    #to calculate the fitness value of fish based on obj func
    def evaluate_fitness(self, objective_function):
        self.fitness = objective_function(self.position) # pass the current position to the obj func
        #update the attributes if current fitness is better than previous
        if self.personal_best_fitness is None or self.fitness < self.personal_best_fitness:
            self.personal_best_fitness = self.fitness
            self.personal_best_position = self.position.copy()




#FishSwarmOptimizer class responsible for managing the swarm and optimizing the objective function
class FishSwarmOptimizer:
    def __init__(self, objective_function, n_dim, n_fish=10, max_iter=100,
                 visual_range=0.5, step_size=0.1, lower_bound=-10, upper_bound=10):

        self.objective_function = objective_function
        self.n_dim = n_dim
        self.n_fish = n_fish
        self.max_iter = max_iter
        self.visual_range = visual_range
        self.step_size = step_size
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        #a list contain instances of Fish class (each fish with random position within specified bounds)
        self.swarm = [Fish(n_dim, lower_bound, upper_bound) for _ in range(n_fish)]
        #used to store the global best position and fitness found by the swarm
        self.global_best_position = None
        self.global_best_fitness = None

# performs the optimization process
    def optimize(self):
        for _ in range(self.max_iter):
            for fish in self.swarm: # to evaluate the fitness of each fish in the swarm
                fish.evaluate_fitness(self.objective_function)
                if self.global_best_fitness is None or fish.fitness < self.global_best_fitness:
                    self.global_best_fitness = fish.fitness
                    self.global_best_position = fish.position.copy()


            for fish in self.swarm: # iterates over each pair of fish in the swarm to facilitate interaction between them
                for other_fish in self.swarm:
                    if other_fish.personal_best_fitness < fish.personal_best_fitness:
                        d = np.linalg.norm(other_fish.personal_best_position - fish.personal_best_position) #to calculate the euclidean distance between the personal best positions of the two fish
                        if d < self.visual_range:
                            c = np.random.uniform(0, 1, self.n_dim) # same dimensionality as the problem space
                            #to update the velocity of the current fish based on the difference between the personal best position of the other fish and its own position
                            fish.velocity += self.step_size * c * (other_fish.personal_best_position - fish.position)

                fish.position += fish.velocity #update the position of each fish by adding its velocity vector
                fish.position = np.clip(fish.position, self.lower_bound, self.upper_bound) #to ensure that the new position is within the bounds of the search space
        #to return the global best position and fitness found by the swarm after the optimization process is complete
        return self.global_best_position, self.global_best_fitness



# Example usage
def sphere_function(x):
    return np.sum(x**2)

n_dim = 10  # Dimensionality of the problem
n_fish = 60  # Number of fish in the swarm
max_iter = 100  # Maximum number of iterations
#instance of FishSwarmOptimizer
fso = FishSwarmOptimizer(objective_function=sphere_function, n_dim=n_dim, n_fish=n_fish, max_iter=max_iter)
best_position, best_fitness = fso.optimize()
print("Best position:", best_position)
print("Best fitness:", best_fitness)
