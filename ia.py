import ga
import maze
import copy
import pandas as pd
import random
from tkinter import *

class IA:
    
    def __init__(self, maze_, individuals_per_era=5, steps=30, rounds=10, mutation_percentage=0.10, tk_root=0):
        
        self.gc   = ga.GeneticController(individuals_per_era, steps)
        self.maze = self.config_maze(maze_, tk_root)
        self.new_maze = copy.deepcopy(self.maze)
        self.rounds = rounds
        self.era_cont = 0
        self.steps = steps
        self.mutation_percentage = mutation_percentage
    
    def config_maze(self, maze_, tk_root):
        altura  = len(maze_[0]) 
        largura = len(maze_) 
        maze_obj = maze.Maze(altura, largura, maze_, tk_root)
        return maze_obj
        
    def reset_maze(self):    
        self.new_maze = copy.deepcopy(self.maze)
        
    def make_run(self):
        
        while self.era_cont < self.rounds:
            
            # Setting first era randomly
            if self.era_cont == 0:
                self.gc.setting_first_era()
            
            individuals_dict = self.gc.era[self.era_cont]    
            for ind in individuals_dict:
                ind = individuals_dict[ind]
                
                self.new_maze.set_ia_run(ind.genetic)
                self.new_maze.run()
                self.analyse_run(ind.name)
                self.reset_maze()
                
            father, mother = self.select_best()
            first_son, second_son = self.tournament_selection(father, mother)
            
            self.gc.create_era([father, first_son, second_son])

            self.era_cont += 1         
                
    def analyse_run(self, id_):
        
        self.gc.era[self.era_cont][id_].reach = self.new_maze.actual
        self.gc.era[self.era_cont][id_].h = (self.new_maze.actual[0] + 1) + (self.new_maze.actual[1] + 1)
        
    def select_best(self):
        
        father = [0, 0]
        mother = [0, 0]
        
        #print(len(self.gc.era[self.era_cont]))
        print('-------------------------------------------')
        print(f'\nEra: {self.era_cont}')
        individuals_dict = self.gc.era[self.era_cont] 
        for run in self.gc.era[self.era_cont]:
            
            run = individuals_dict[run]
            
            if run.h > mother[1] and run.h > father[1]:
                mother = father
                father = [run.name, run.h]
            
            elif run.h > mother[1]:
                mother = [run.name, run.h]
            
            else:
                pass            
            
            print(f'\nId     : {run.name}')
            print(f'H      : {run.h}')
            print(f'Actual : {run.reach} or {run.reach[0] + 1}, {run.reach[1] + 1}')
            
        print()
        print(f'Father ID: {father[0]}  Father H: {father[1]}')
        print(f'Mother ID: {mother[0]}  Mother H: {mother[1]}')
        
        return self.gc.era[self.era_cont][father[0]], self.gc.era[self.era_cont][mother[0]]

    def tournament_selection(self, father, mother):
           
        # Setando ponto de corte
        cutting_point = int(self.steps / 2)
        
        # Breeding
        first_son  = self.gc.generate_individual()
        second_son = self.gc.generate_individual()
        
        first_son.set_genetic(father.genetic[:cutting_point] + mother.genetic[cutting_point:]) 
        second_son.set_genetic(mother.genetic[:cutting_point] + father.genetic[cutting_point:])
        
        self.mutation(first_son)
        self.mutation(second_son)
        
        return first_son, second_son
        
        # print(father.genetic)
        # print(mother.genetic)
        # print(first_son)
        # print(second_son)
        
        # genetic_dict = { 'Father': father.genetic, 'First_Son': first_son, 'Mother': mother.genetic, 'Second_Son': second_son }
        # genetic_df = pd.DataFrame(genetic_dict)
        # print(genetic_df)
    
    def mutation(self, to_mutate):
        
        amount_to_mutate =  int(self.steps * self.mutation_percentage)
        genes_dict = {0 : 'up', 1: 'down', 2: 'left', 3: 'right'}
        
        # Ele vai iterar de 0 até a quantidade de genes resultante da porcentagem fornecida 
        for stop in range(0, amount_to_mutate):
            
            # Vai gerar um número aleatório entre 0 e a quantidade de steps (que é igual a quantidade de carga genética)
            gene_to_mutate = random.randrange(0, self.steps)
            
            direction = random.randrange(0, 4)
            
            to_mutate.genetic[gene_to_mutate] = genes_dict[direction]
            
def main():
    
    maze_map = []
    
    maze_map.append(['E', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
    maze_map.append(['1', '1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '1'])
    maze_map.append(['1', '0', '0', '0', '0', '1', '1', '1', '0', '1', '1', '0'])
    maze_map.append(['1', '0', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0'])
    maze_map.append(['0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '1', '1'])
    maze_map.append(['1', '1', '0', '0', '0', '1', '0', '1', '0', '0', '1', '1'])
    maze_map.append(['1', '1', '1', '0', '1', '1', '0', '0', '0', '1', '1', '0'])
    maze_map.append(['0', '0', '1', '0', '0', '1', '0', '1', '0', '1', '1', '0'])
    maze_map.append(['0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0'])
    maze_map.append(['1', '1', '1', '0', '1', '0', '0', '1', '1', '1', '1', '0'])
    maze_map.append(['1', '1', '1', '0', '1', '0', '0', '0', '0', '1', '1', '1'])
    maze_map.append(['1', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', 'S'])
    
    ia = IA(maze_map)
    ia.make_run()

if __name__ == '__main__':
    
    main()