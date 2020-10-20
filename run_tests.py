import ia

class Teste:
    
    def __init__(self, ipg, steps, rounds, mutation, stop_breeding):
        
        self.ipg = ipg
        self.steps = steps
        self.rounds = rounds
        self.mutation = mutation
        self.stop_breeding = stop_breeding

def generate_random_tests(maze):
    
    individual_per_generation = [5, 10, 25]
    steps = [30, 50, 75]
    rounds = [50, 100, 250, 500]
    mutation = [0.10, 0.20, 0.30, 0.40]
    stop_breeding = [30, 50, 150, 350]
    
    test_list = []
    dict_test = {}
    id_ = 0
    
    for ind in individual_per_generation:
        for stp in steps:
            for rnd in rounds:
                for mtn in mutation:
                    for stop in stop_breeding:
                        test_list.append(Teste(ind, stp, rnd, mtn, stop))
    
    for index, config in enumerate(test_list):
        robot = ia.IA(maze, config.ipg, config.steps, config.rounds, config.mutation, config.stop_breeding, 'Fast')
        robot.make_run()

        print(f"Testando... {index}/{len(test_list)}")
    
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
    
    generate_random_tests(maze_map)
    
if __name__ == '__main__':
    
    file_ = 'teste.txt'
    main(file_)
