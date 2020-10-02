import os
from termcolor import colored
os.system('color')


def coloring():
    print(colored('hello', 'red'), colored('world', 'green'))

def percentage():
    
    per = 0.11
    steps = 30
    
    result = per * steps
    result_int = int(per * steps)
    
    print(result)
    print(result_int)
    
if __name__ == "__main__":
    percentage()