
import get_key as gk
import os
from termcolor import colored as c
import time

os.system('color')


class Maze:
    
    def __init__(self, maze):
        self.maze = maze

    def gui_print_maze(self, maze):
        
        # teste = 'teste'
        # print(c(teste, 'yellow'))
        
        condition = True
        #condition = False
        
        if condition:
               
            #print(f'Steps      : {self.steps}')
            #print(f'Element Before: {self.element_before}')
            #print(f'Position Before: {self.before}')
            #print(f'')
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
            # if self.steps != 0:
            #     if self.ia_flag:
            #         print(f'Key Pressed: {self.ia_steps[self.ia_steps_count]}')
                
            # print(f'Steps      : {self.steps}')
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
            #time.sleep(self.sleeper)       

        else:
            pass
    
if __name__ == '__main__':
    
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
    
    maze_obj = Maze(maze_map)        
    maze_obj.print_maze(maze_obj.maze)