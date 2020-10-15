import ga
import a
import maze
import copy
import pandas as pd
import random
import os
from tkinter import *

class IA:
    
    def __init__(self, maze_, individuals_per_generation=10, steps=1000, rounds=10, mutation_percentage=0.30, tk_root=0):
        
        self.gc = ga.GeneticController(individuals_per_generation, steps)
        self.maze = self.config_maze(maze_, tk_root)
        self.new_maze = copy.deepcopy(self.maze)
        self.rounds = rounds
        self.generation_cont = 0
        self.steps = steps
        self.mutation_percentage = mutation_percentage
        self.dict_data = {}
        self.stop_breeding = 1000
        self.stop_breeding_count = 0
        self.old_mother = 0
        self.old_father = 0
    
    # Genetic Algorithm
    
    def save_data(self, father, mother):
        self.dict_data[self.generation_cont] = [self.generation_cont, father.h, mother.h]
    
    def to_csv(self):
        self.data = pd.DataFrame.from_dict(self.dict_data, orient='index', columns=['Generation', 'Father', 'Mother']) 
        self.data.to_csv(f'ipg{self.gc.individuals_per_generation}_steps{self.steps}_rounds{self.rounds}_mutation{self.mutation_percentage}.csv')
    
    def to_txt(self, winner):
        
        with open(f'ipg{self.gc.individuals_per_generation}_steps{self.steps}_rounds{self.rounds}_mutation{self.mutation_percentage}.txt', 'w') as w:
            for direction in winner.genetic:
                w.write(f'{direction}\n')
      
    def config_maze(self, maze_, tk_root):
        altura  = len(maze_) 
        largura = len(maze_[0]) 
        maze_obj = maze.Maze(altura, largura, maze_, tk_root)
        return maze_obj
        
    def reset_maze(self):    
        self.new_maze = copy.deepcopy(self.maze)
        
    def make_run(self):
        
        while (self.generation_cont < self.rounds) and (self.stop_breeding_count < self.stop_breeding):
            print(f"\nGENERATION: {self.generation_cont}")
            
            # Setting first era randomly
            if self.generation_cont == 0:
                self.gc.setting_first_generation()
            
            individuals_dict = self.gc.generation[self.generation_cont]    
            for ind in individuals_dict:
                ind = individuals_dict[ind]
                
                self.new_maze.set_ia_run(ind.genetic, ind.name)
                self.new_maze.run()
                self.analyse_run(ind.name)
                self.reset_maze()
                
            father, mother, end = self.select_best()
            
            if end:
                self.to_txt(father)
                print("\nAtingiu o final do labirinto! Parabéns!")
                break
            
            self.save_data(father, mother)
            
            self.breeding_analyse(father, mother)
            
            first_son, second_son = self.tournament_selection(father, mother)
            
            self.gc.create_generation([father, first_son, second_son])

            self.generation_cont += 1         
        
        self.to_csv()
    
    def breeding_analyse(self, father, mother):
        
        if mother.h > self.old_mother and father.h > self.old_father:
            self.old_mother = mother.h
            self.old_father = father.h
            self.stop_breeding_count = 0
            
        elif father.h > self.old_father:
            self.old_father = father.h
            self.stop_breeding_count = 0
            
        else:
            self.stop_breeding_count += 1
            print(f"\nGeração não melhora a {self.stop_breeding_count} rounds")
    
    def analyse_run(self, id_):
        
        self.gc.generation[self.generation_cont][id_].reach = self.new_maze.actual
        self.gc.generation[self.generation_cont][id_].h = (self.new_maze.actual[0] + 1) + (self.new_maze.actual[1] + 1)
        
    def select_best(self):
        
        father = [0, 0]
        mother = [0, 0]
        
        individuals_dict = self.gc.generation[self.generation_cont] 
        for run in self.gc.generation[self.generation_cont]:
            
            run = individuals_dict[run]
            
            if run.h > mother[1] and run.h > father[1]:
                mother = father
                father = [run.name, run.h]
            
            elif run.h > mother[1]:
                mother = [run.name, run.h]           
            
            print(f'\nId     : {run.name}')
            print(f'H      : {run.h}')
            print(f'Actual : {run.reach} or {run.reach[0] + 1}, {run.reach[1] + 1}')
            
        print()
        print(f'Father ID: {father[0]}  Father H: {father[1]}')
        print(f'Mother ID: {mother[0]}  Mother H: {mother[1]}')
        print('\n-------------------------------------------')
        
        # Tornar generico
        if father[1] == 24:
            return self.gc.generation[self.generation_cont][father[0]], self.gc.generation[self.generation_cont][mother[0]], True
        
        else:
            return self.gc.generation[self.generation_cont][father[0]], self.gc.generation[self.generation_cont][mother[0]], False

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
    
    def mutation(self, to_mutate):
        
        amount_to_mutate =  int(self.steps * self.mutation_percentage)
        genes_dict = {0 : 'up', 1: 'down', 2: 'left', 3: 'right'}
        
        # Ele vai iterar de 0 até a quantidade de genes resultante da porcentagem fornecida 
        for stop in range(0, amount_to_mutate):
            
            # Vai gerar um número aleatório entre 0 e a quantidade de steps (que é igual a quantidade de carga genética)
            gene_to_mutate = random.randrange(0, self.steps)
            
            direction = random.randrange(0, 4)
            
            to_mutate.genetic[gene_to_mutate] = genes_dict[direction]
    
    # A* algorithm
    
    def test_a(self):
        
        ind_length = 15
        self.a = a.A()
        self.maze.start_a_run(self.maze.maze)
        cont = 0
        algorithm = True
        while algorithm:
             
            self.a.create_individual(self.maze.actual, self.maze.maze)
            
            move = self.walk()
            algorithm = self.maze.a_run(move, self.maze.maze)
        
            cont += 1
            
    def walk(self):
        
        print(f"Individuo {self.a.queue[0].id} veio do nodo: {self.a.queue[0].came_from}")
        print(f"Possuí os seguintes movimentos: {self.a.queue[0].possible_moves}")
        
        if len(self.a.queue[0].possible_moves) > 1:
            key = self.a.euclidean_distance(self.a.queue[0].possible_moves, self.maze.actual, self.maze.maze)
            #key = self.a.analyse_move(self.a.queue[0].possible_moves, self.maze.actual, self.maze.maze, key)
            move = self.a.queue[0].possible_moves.pop(self.a.queue[0].possible_moves.index(key))
        
        else:
            move = self.a.queue[0].possible_moves.pop(0)
            
        print(f"Andou na direção {move}")
        print(f"Sobrou os seguintes movimentos: {self.a.queue[0].possible_moves}")
        
        if self.a.queue[0].possible_moves == []:
            print("Popped!")
            self.a.pop()
        
        return move
        
def main(file_):
    
    with open(file_, 'r') as f:
        maze = f.readlines()
        maze = [l.strip('\n\r') for l in maze]
        
    maze_map  = []
    for line in maze:
        maze_line = []
        
        for cell in line:
            maze_line.append(cell)
        
        maze_map.append(maze_line)
    
    ia = IA(maze_map)
    ia.make_run()
    
if __name__ == '__main__':
    
    file_ = 'teste.txt'
    main(file_)