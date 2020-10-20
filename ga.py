"""

Os dados do algoritmo genético serão um conjunto de teclas pressionadas em sequência

Dados: 'up', 'down', 'left', 'right'

"""

import random

class GeneticController:
    
    def __init__(self, individuals_per_generation=5, steps=30):
        self.generation = []
        self.individuals_per_generation = individuals_per_generation
        self.steps = steps
        self.name = 0
        #self.individual = Individual(steps) 
        
    def setting_first_generation(self):
        
        generation_individuals = {}
        for self.name in range(0, self.individuals_per_generation):
            ind = Individual(self.steps, self.name)
            ind.random_genetic()
            generation_individuals[ind.name] = ind
        
        self.generation.append(generation_individuals)
        
        # for era in self.generation:
        #     for individual in era:
        #         print(f'{len(individual.genetic)} : {individual.genetic}\n')
    
    def create_generation(self, ind_list):
        
        # Descobrindo quantos randoms precisamos criar
        random_to_create = self.individuals_per_generation - len(ind_list)
        
        generation_individuals = {}
        for individual in ind_list:
            generation_individuals[individual.name] = individual
        
        if random_to_create > 0:
            for create in range(0, random_to_create):
                individual = self.generate_random_individual()
                generation_individuals[individual.name] = individual
                
        self.generation.append(generation_individuals)
            
    def generate_individual(self):
        self.name += 1
        return Individual(self.steps, self.name)
    
    def generate_random_individual(self):
        self.name += 1
        ind = Individual(self.steps, self.name)
        ind.random_genetic()
        
        return ind            
   
class Individual:
    
    def __init__(self, steps, name):
        self.steps = steps
        self.name = name
        self.cromossomes = {0 : 'up', 1: 'down', 2: 'left', 3: 'right'}
        self.h = 0
        self.genetic = []
        self.reach = [] 
        
    def random_genetic(self):
        
        for st in range(0, self.steps):
            rd = random.randrange(0,4)      
            self.genetic.append(self.cromossomes[rd])
    
    def set_genetic(self, genetic):
        self.genetic = genetic
    
if __name__ == "__main__":
    
    gc = GeneticController()
    gc.setting_first_generation()
    #print(gc.steps)    