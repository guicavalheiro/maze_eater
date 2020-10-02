import ia
from tkinter import *

# individuals_per_era=5, steps=100, rounds=200, mutation_percentage=0.10

class tk:
    
    def __init__(self, maze):
        self.maze = maze
        self.root = Tk()
        self.compose()
        
    def compose(self):
        
        # Criando local onde será printado o labirinto
        lab_frame = LabelFrame(self.root, text='Maze Frame', padx=10, pady=10)
        #lab_frame.grid(row=0, column=1)
        lab_frame.grid(row=0, column=1, padx=5, pady=5)
        
        # Criando local onde serão dispostos os controles
        control_frame = LabelFrame(self.root, text='Controller Frame', padx=10, pady=10)
        control_frame.grid(row=0, column=0, padx=5, pady=5)
        
        # Configurando interação com a variável de individuos por era
        individuals_per_era_label = Label(control_frame, text='Individuals Per Era  ')
        individuals_per_era_input = Entry(control_frame)
        
        individuals_per_era_label.grid(row=0, column=0)
        individuals_per_era_input.grid(row=0, column=1)
        
        # Configurando interação com a variável de steps por individuo
        steps_label = Label(control_frame, text='Individual Steps     ')
        steps_input = Entry(control_frame)

        steps_label.grid(row=2, column=0)
        steps_input.grid(row=2, column=1)
        
        # Configurando interação com a variável de número de rodadas
        rounds_label = Label(control_frame, text='Rounds amount        ')
        rounds_input = Entry(control_frame)
        
        rounds_label.grid(row=4, column=0)
        rounds_input.grid(row=4, column=1)
        
        # Configurando interação com a variável de porcentagem de mutação
        mutation_label = Label(control_frame, text='Mutation Percentual  ')
        mutation_input = Entry(control_frame)
        
        mutation_label.grid(row=6, column=0)
        mutation_input.grid(row=6, column=1)
        
        # Salvando todos valores inputados
        save_all = Button(control_frame, text='Save All', command= lambda: self.save_all(individuals_per_era_input.get(), steps_input.get(), rounds_input.get(), mutation_input.get(), lab_frame))
        save_all.grid(row=8, column=1)
        
        # Iniciar
        run = Button(control_frame, text='Run', command=self.run)
        run.grid(row=9,column=1)
        
        self.root.mainloop()  
    
    def save_all(self, individuals_amount, steps_amount, rounds_amount, mutation_amount, lab_frame):
        #self.individuals_per_era(individuals_amount)
        #self.steps(steps_amount)
        #self.rounds(rounds_amount)
        #self.mutation(mutation_amount)
        
        self.ia = ia.IA(self.maze, int(individuals_amount), int(steps_amount), int(rounds_amount), float(mutation_amount), lab_frame)

    def run(self):
        self.ia.make_run()
        
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
    
    tk = tk(maze)
    
    