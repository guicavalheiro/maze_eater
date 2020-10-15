import get_key as gk
import os
from termcolor import colored as c
import time
from tkinter import *
import copy

os.system('color')

class Maze:
    
    def __init__(self, altura, largura, maze, tk_root=0):
        
        self.actual    = [0, 0]
        self.before    = [0, 0]
        self.aux_coord = [0, 0]
        
        self.element_before = 0

        self.altura  = altura
        self.largura = largura

        self.player = '@'
        
        self.maze = maze
        self.start = True
        
        self.finish = False

        self.label_counter = 0
        self.steps = 0
        
        self.sleeper = 0
        
        self.ia_steps = []
        self.ia_steps_count = 0
        self.ia_flag = False
        
        self.ind_name = 'NOT_DEFINED'
        
        self.numero_de_movimentos = 50
        
        # if tk_root != 0:
        #     text = Label(tk_root, text='0')
        #     text.grid(row=0,column=0)
            
        #     text_2 = Label(tk_root, text='@')
        #     text_2.grid(row=0,column=1)

    def set_ia_run(self, ia_steps, ind_name):
        self.ia_steps = ia_steps
        self.ia_steps_count = 0
        self.ia_flag = True
        self.ind_name = ind_name
    
    def set_a_run(self):
        pass
    
    def gui_print_maze(self, maze):
        
        # teste = 'teste'
        # print(c(teste, 'yellow'))
        
        condition = True
        #condition = False
        
        if condition:
            # if self.steps != 0:
            #     if self.ia_flag:
            #         print(f'Key Pressed: {self.ia_steps[self.ia_steps_count]}')
                
            # print(f'Steps      : {self.steps}')
            # print(f'Element Before: {self.element_before}')
            # print(f'Position Before: {self.before}')
            # print(f'')
            
            for line in maze:
                for cell in line:
                    
                    if cell == 'E' or cell == 'S':
                        
                        return c(cell, 'white')

                    elif cell == '1':
                        return c(cell, 'red')
                    
                    elif cell == '0':
                        return c(cell, 'green')
                    
                    elif cell == '@':
                        return c(cell, 'yellow')
                    
                return ''
            print()    
            
            #print()     
            time.sleep(self.sleeper)       

    def print_maze(self, maze):
        
        # teste = 'teste'
        # print(c(teste, 'yellow'))
        
        condition = True
        #condition = False
        
        if condition:
            if self.steps != 0:
                #if self.ia_flag:
                print(f'\nInd name   : {self.ind_name}')
                print(f"Before     : {self.before}")
                #print(f'Aux        : {self.aux_coord}')
                print(f"Actual     : {self.actual}")
                if self.ia_flag:
                    print(f'Key Pressed: {self.ia_steps[self.ia_steps_count]}')
            
            print(f'Steps      : {self.steps}')
            #print(f'Element Before: {self.element_before}')
            #print(f'Position Before: {self.before}')
            #print(f'')
            for line in maze:
                for cell in line:
                    
                    if cell == 'E' or cell == 'S':
                        print(c(cell, 'white'), end=' ')
                    
                    elif cell == '1':
                        print(c(cell, 'red'), end=' ')
                    
                    elif cell == '0':
                        print(c(cell, 'green'), end=' ')
                        
                    elif cell == '@':
                        print(c(cell, 'yellow'), end=' ')
                    
                print()
            print()    
            
            #print()     
            time.sleep(self.sleeper)       

        else:
            pass
        
    def run(self):
        
        maze = self.maze
        play = True
        while play:
            
            # Start
            if self.start == True:
                maze = self.next_position(maze, [0, 0], 'inicio')
                self.print_maze(maze)
                
                self.start = False
            
            # Simulate Key
            if self.ia_flag:
                
                if self.ia_steps_count < len(self.ia_steps):
                    key = gk.simulate_key(self.ia_steps[self.ia_steps_count])

                    # Go to next position  
                    maze = self.next_position(maze, self.actual, key)    
                    self.print_maze(maze)
    
                    self.ia_steps_count += 1
                    
                else:
                    #print(f"Terminou os steps da IA\nActual Steps: {self.actual}")
                    play = False
                    #self.print_maze(maze)
            
            else:
                
                if self.steps < self.numero_de_movimentos:
                    # Get Key
                    key = gk.get_key()
                        
                    #key = gk.simulate_key(self.label[self.label_counter])
                    self.label_counter += 1
                    
                    # Go to next position  
                    maze = self.next_position(maze, self.actual, key)    
                    
                    if self.actual == [len(self.maze[0]) - 1, len(self.maze[1]) - 1]:
                        #print("ACABO ACABO ACABO!")
                        pass
                    
                    else:
                        self.print_maze(maze)
                        #print("--------------------------------------------")
                
                else:
                    print(f"Você ultrapassou o número de movimentos permitidos: {self.numero_de_movimentos}")
                    play = False
                                
            if key == 'q':
                play = False

            if self.finish:
                play = False
    
    def start_a_run(self, maze):
        
        # Start
        if self.start == True:
            maze = self.next_position(maze, [0, 0], 'inicio')
            self.print_maze(maze)
            
            self.start = False
        
    def a_run(self, move, maze):
    
        maze = self.next_position(maze, self.actual, move)    
        
        if self.finish:
            return False
        
        else:
            self.print_maze(maze)
            return True
        
    def next_position(self, maze, position, key):
        
        #print(f"Key: {key}")
        
        if key == 'up':
            new_pos = position[0] - 1
            
            result = self.valid_position(new_pos, self.actual[1])
            
            if result == 0:
                
                # Atualiza a posição atual com seu elemento original
                self.previous_position(maze)
                
                # Troca coordenada atual
                self.aux_coord = copy.copy(self.actual)
                self.actual[0] = new_pos
                
                # Salva o elemento da posição a ser ocupada
                self.save_position(maze)
                
                # Atualizar nova posição
                self.player_position(maze)
                
                # Printa e atualiza coordenadas dos elementos anteriores
                self.final_step(maze)
                
            elif result == 1:
                #print("Found a wall")
                pass
            
            elif result == 2:    
                #print("Out of bounds")
                pass
            
            elif result == 3:
                
                # Atualiza a posição atual com seu elemento original
                self.previous_position(maze)
                
                # Troca coordenada atual
                self.aux_coord = copy.copy(self.actual)
                self.actual[0] = new_pos
                
                # Salva o elemento da posição a ser ocupada
                self.save_position(maze)
                
                # Atualizar nova posição
                self.player_position(maze)
                
                # Atualiza coordenadas dos elementos anteriores
                self.final_step(maze)
                
                # Printa o maze
                self.print_maze(maze)
                
                self.finish = True
                #print(f"{c('You Win!', 'yellow')}")
        
        elif key == 'down':
            new_pos = position[0] + 1
            
            result = self.valid_position(new_pos, self.actual[1])
            if result == 0:
                
                # Atualiza a posição atual com seu elemento original
                self.previous_position(maze)
                
                # Troca coordenada atual
                self.aux_coord = copy.copy(self.actual)
                self.actual[0] = new_pos
                
                # Salva o elemento da posição a ser ocupada
                self.save_position(maze)
                
                # Atualizar nova posição
                self.player_position(maze)
                
                # Printa e atualiza coordenadas dos elementos anteriores
                self.final_step(maze)
            
            elif result == 1:
                #print("Found a wall")
                pass
            
            elif result == 2:    
                #print("Out of bounds")
                pass
            
            elif result == 3:
                
                # Atualiza a posição atual com seu elemento original
                self.previous_position(maze)
                
                # Troca coordenada atual
                self.aux_coord = copy.copy(self.actual)
                self.actual[0] = new_pos
                
                # Salva o elemento da posição a ser ocupada
                self.save_position(maze)
                
                # Atualizar nova posição
                self.player_position(maze)
                
                # Atualiza coordenadas dos elementos anteriores
                self.final_step(maze)
                
                # Printa o maze
                self.print_maze(maze)
                
                self.finish = True
                #print(f"{c('You Win!', 'yellow')}")

        elif key == 'left':
            new_pos = position[1] - 1
            
            result = self.valid_position(self.actual[0], new_pos)
            if result == 0:
                
                # Atualiza a posição atual com seu elemento original
                self.previous_position(maze)
                
                # Troca coordenada atual
                self.aux_coord = copy.copy(self.actual)
                self.actual[1] = new_pos
                
                # Salva o elemento da posição a ser ocupada
                self.save_position(maze)
                
                # Atualizar nova posição
                self.player_position(maze)
                
                # Printa e atualiza coordenadas dos elementos anteriores
                self.final_step(maze)
            
            elif result == 1:
                #print("Found a wall")
                pass
            
            elif result == 2:    
                #print("Out of bounds")
                pass
            
            elif result == 3:
                
                # Atualiza a posição atual com seu elemento original
                self.previous_position(maze)
                
                # Troca coordenada atual
                self.aux_coord = copy.copy(self.actual)
                self.actual[1] = new_pos
                
                # Salva o elemento da posição a ser ocupada
                self.save_position(maze)
                
                # Atualizar nova posição
                self.player_position(maze)
                
                # Atualiza coordenadas dos elementos anteriores
                self.final_step(maze)
                
                # Printa o maze
                self.print_maze(maze)
                
                self.finish = True
                #print(f"{c('You Win!', 'yellow')}")
        
        elif key == 'right':
            new_pos = position[1] + 1
            
            result = self.valid_position(self.actual[0], new_pos)
            
            if result == 0:
                
                # Atualiza a posição atual com seu elemento original
                self.previous_position(maze)
                
                # Troca coordenada atual
                self.aux_coord = copy.copy(self.actual)
                self.actual[1] = new_pos
                
                # Salva o elemento da posição a ser ocupada
                self.save_position(maze)
                
                # Atualizar nova posição
                self.player_position(maze)
                
                # Printa e atualiza coordenadas dos elementos anteriores
                self.final_step(maze)

            
            
            elif result == 1:
                #print("Found a wall")
                pass
            
            elif result == 2:    
                #print("Out of bounds")
                pass
            
            elif result == 3:
                
                # Atualiza a posição atual com seu elemento original
                self.previous_position(maze)
                
                # Troca coordenada atual
                self.aux_coord = copy.copy(self.actual)
                self.actual[1] = new_pos
                
                # Salva o elemento da posição a ser ocupada
                self.save_position(maze)
                
                # Atualizar nova posição
                self.player_position(maze)
                
                # Atualiza coordenadas dos elementos anteriores
                self.final_step(maze)
                
                # Printa o maze
                self.print_maze(maze)
                
                self.finish = True
                #print(f"{c('You Win!', 'yellow')}")
        
        elif key == 'inicio':
            
            # Salva elemento presente na posição atual
            self.save_position(maze)
            
            # Troca o elemento da posição pelo símbolo do jogador
            self.player_position(maze)
            
            # Salva a coordenada original
            self.aux_coord = copy.copy(self.actual)
            
        else:
            print("Pressione uma tecla válida!")
            
        #print(f'Key Pressed: {self.ia_steps[self.ia_steps_count]}')
        #print(f'Steps da IA: {self.ia_steps_count}')
        #print()
        return maze

    def save_position(self, maze):
        #print(f'Salvando em element before o elemento: {maze[self.actual[0]][self.actual[1]]}')
        self.element_before = maze[self.actual[0]][self.actual[1]]
        
    def previous_position(self, maze):
        #print(f'Colocando {self.element_before} em {self.before}')
        maze[self.actual[0]][self.actual[1]] = self.element_before
        
    def player_position(self, maze): 
        #print(f'Atualizando a posição {self.actual} com @')
        #print(self.actual)
        #print(maze)
        maze[self.actual[0]][self.actual[1]] = '@'
    
    def valid_position(self, pos_x, pos_y):
        
        #print(f"Pos_x: {pos_x}, Pos_y: {pos_y}")
        #print(f"Altura: {self.altura}, Largura: {self.largura}")
        
        if (pos_x < 0) or (pos_x >= self.altura) or (pos_y < 0) or (pos_y >= self.largura):
            #print("11111")
            self.steps += 1
            return 2
    
        elif self.maze[pos_x][pos_y] == '1':
            #print("22222")
            self.steps += 1
            return 1
        
        elif self.maze[pos_x][pos_y] == 'S':
            #print("33333")
            self.steps += 1
            return 3
        
        else:
            #print("44444")
            self.steps += 1
            return 0    
    
    def final_step(self, maze):
        #print(f"Atualizando {self.before} para {self.aux_coord}")
        self.before = self.aux_coord

def main(maze):
    
    altura  = len(maze) 
    largura = len(maze[0])
    
    maze_obj = Maze(altura, largura, maze)
    maze_obj.run()

if __name__ == '__main__':
    
    file_ = 'teste3.txt'
    
    with open(file_, 'r') as f:
        maze = f.readlines()
        maze = [l.strip('\n\r') for l in maze]
        
    maze_map  = []
    for line in maze:
        maze_line = []
        
        for cell in line:
            maze_line.append(cell)
        
        maze_map.append(maze_line)
        
    
    #print(maze_map)
    
    main(maze_map)