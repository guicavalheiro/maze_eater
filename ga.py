"""

Os dados do algoritmo genético serão um conjunto de teclas pressionadas em sequência

Dados: 'up', 'down', 'left', 'right'

"""

import random

class GeneticController:
    
    def __init__(self, individuals_per_era=5, steps=30):
        self.era = []
        self.individuals_per_era = individuals_per_era
        self.steps = steps
        self.name = 0
        #self.individual = Individual(steps) 
        
    def setting_first_era(self):
        
        era_individuals = {}
        for self.name in range(0, self.individuals_per_era):
            ind = Individual(self.steps, self.name)
            ind.random_genetic()
            era_individuals[ind.name] = ind
        
        self.era.append(era_individuals)
        
        # for era in self.era:
        #     for individual in era:
        #         print(f'{len(individual.genetic)} : {individual.genetic}\n')
    
    def create_era(self, ind_list):
        
        # Descobrindo quantos randoms precisamos criar
        random_to_create = self.individuals_per_era - len(ind_list)
        #print(f'{random_to_create}')
        
        era_individuals = {}
        for individual in ind_list:
            era_individuals[individual.name] = individual
        
        if random_to_create > 0:
            for create in range(0, random_to_create):
                individual = self.generate_random_individual()
                era_individuals[individual.name] = individual
                
        self.era.append(era_individuals)
            
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
    gc.setting_first_era()
    #print(gc.steps)    