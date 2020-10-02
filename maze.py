import get_key as gk
import os
from termcolor import colored as c
import time
from tkinter import *

os.system('color')

class Maze:
    
    def __init__(self, altura, largura, maze, tk_root):
        
        self.actual  = [0, 0]
        self.before  = [0, 0]
        self.element_before = 0

        self.altura  = altura
        self.largura = largura

        self.player = '@'
        
        self.maze = maze
        
        self.finish = False
        
        self.label = ['right', 'right', 'right', 'right', 'right', 'down', 'right', 'right', 'right', 'down', 'down', 'right', 'down', 'down', 
                      'left', 'down', 'down', 'down', 'left', 'left', 'down', 'down', 'right', 'right', 'down', 'right', 'right', 'right']

        self.label_counter = 0
        self.steps = 0
        
        self.sleeper = 0
        
        self.ia_steps = []
        self.ia_steps_count = 0
        self.ia_flag = False
        
        if tk_root != 0:
            text = Label(tk_root, text='0')
            text.grid(row=0,column=0)
            
            text_2 = Label(tk_root, text='@')
            text_2.grid(row=0,column=1)
    
    def set_ia_run(self, ia_steps):
        self.ia_steps = ia_steps
        self.ia_steps_count = 0
        self.ia_flag = True
    
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
        
        #condition = True
        condition = False
        
        if condition:
            if self.steps != 0:
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
        
        start = True
        maze = self.maze
        play = True
        while play:
            
            # Start
            if start == True:
                maze = self.next_position(maze, [0, 0], 'inicio')
                self.print_maze(maze)
                
                start = False
            
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
                        
            if key == 'q':
                play = False

            if self.finish:
                play = False
                
    def next_position(self, maze, position, key):
        
        if key == 'up':
            new_pos = position[0] - 1
            
            result = self.valid_position(new_pos, self.actual[1])
            if result == 0:
                self.previous_position(maze)
                self.actual[0] = new_pos
                self.save_position(maze)
                self.player_position(maze)
                #self.print_maze(maze)
                self.steps += 1
                
            elif result == 1:
                #print("Found a wall")
                pass
            
            elif result == 2:    
                #print("Out of bounds")
                pass
            
            elif result == 3:
                self.previous_position(maze)
                self.actual[0] = new_pos
                self.save_position(maze)
                self.player_position(maze)
                self.print_maze(maze)
                self.finish = True
                print(f"{c('You Win!', 'yellow')}")
                
            #print(f"Posição: {self.actual}")
        
        elif key == 'down':
            new_pos = position[0] + 1
            
            result = self.valid_position(new_pos, self.actual[1])
            if result == 0:
                self.previous_position(maze)
                self.actual[0] = new_pos
                self.save_position(maze)
                self.player_position(maze)
                self.print_maze(maze)
                self.steps += 1
            
            elif result == 1:
                #print("Found a wall")
                pass
            
            elif result == 2:    
                #print("Out of bounds")
                pass
            
            elif result == 3:
                self.previous_position(maze)
                self.actual[0] = new_pos
                self.save_position(maze)
                self.player_position(maze)
                self.print_maze(maze)
                self.finish = True
                print(f"{c('You Win!', 'yellow')}")
            
            #print(f"Posição: {self.actual}")

        elif key == 'left':
            new_pos = position[1] - 1
            
            result = self.valid_position(self.actual[0], new_pos)
            if result == 0:
                self.previous_position(maze)
                self.actual[1] = new_pos
                self.save_position(maze)
                self.player_position(maze)
                #self.print_maze(maze)
                self.steps += 1
            
            elif result == 1:
                #print("Found a wall")
                pass
            
            elif result == 2:    
                #print("Out of bounds")
                pass
            
            elif result == 3:
                self.previous_position(maze)
                self.actual[1] = new_pos
                self.save_position(maze)
                self.player_position(maze)
                self.print_maze(maze)
                self.finish = True
                print(f"{c('You Win!', 'yellow')}")
            
            #print(f"Posição: {self.actual}")
        
        elif key == 'right':
            new_pos = position[1] + 1
            
            result = self.valid_position(self.actual[0], new_pos)
            
            if result == 0:
                self.previous_position(maze)
                self.actual[1] = new_pos
                self.save_position(maze)
                self.player_position(maze)
                #self.print_maze(maze)
                self.steps += 1
            
            elif result == 1:
                #print("Found a wall")
                pass
            
            elif result == 2:    
                #print("Out of bounds")
                pass
            
            elif result == 3:
                self.previous_position(maze)
                self.actual[1] = new_pos
                self.save_position(maze)
                self.player_position(maze)
                self.print_maze(maze)
                self.finish = True
                print(f"{c('You Win!', 'yellow')}")
            
            #print(f"Posição: {self.actual}")
        
        elif key == 'inicio':
            self.save_position(maze)
            self.player_position(maze)
            #self.print_maze(maze)
            self.steps += 1
            #print(f"Posição: {self.actual}")
            
        else:
            print("Pressione uma tecla válida!")
            
        #print(f'Key Pressed: {self.ia_steps[self.ia_steps_count]}')
        #print(f'Steps da IA: {self.ia_steps_count}')
        #print()
        return maze

    def save_position(self, maze):
        
        self.element_before = maze[self.actual[0]][self.actual[1]]
        #print(f'Element Before: {self.element_before}')
            
        self.before = self.actual    
        #print(f'Position Before: {self.before}')
        
    def previous_position(self, maze):
        maze[self.before[0]][self.before[1]] = self.element_before
    
    def player_position(self, maze):
        
        maze[self.actual[0]][self.actual[1]] = '@'
    
    def valid_position(self, pos_x, pos_y):
        
        if (pos_x < 0) or (pos_x > 11) or (pos_y < 0) or (pos_y > 11):
            return 2
    
        elif self.maze[pos_x][pos_y] == '1':
            return 1
        
        elif self.maze[pos_x][pos_y] == 'S':
            return 3
        
        else:
            return 0    
    
def main(maze):
    
    altura  = len(maze[0]) 
    largura = len(maze)
    
    maze_obj = Maze(altura, largura, maze)
    maze_obj.run()

if __name__ == '__main__':
    
    maze = []
    
    maze.append(['E', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
    maze.append(['1', '1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '1'])
    maze.append(['1', '0', '0', '0', '0', '1', '1', '1', '0', '1', '1', '0'])
    maze.append(['1', '0', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0'])
    maze.append(['0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '1', '1'])
    maze.append(['1', '1', '0', '0', '0', '1', '0', '1', '0', '0', '1', '1'])
    maze.append(['1', '1', '1', '0', '1', '1', '0', '0', '0', '1', '1', '0'])
    maze.append(['0', '0', '1', '0', '0', '1', '0', '1', '0', '1', '1', '0'])
    maze.append(['0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0'])
    maze.append(['1', '1', '1', '0', '1', '0', '0', '1', '1', '1', '1', '0'])
    maze.append(['1', '1', '1', '0', '1', '0', '0', '0', '0', '1', '1', '1'])
    maze.append(['1', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', 'S'])
    
    main(maze)