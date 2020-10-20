import pandas as pd
import matplotlib.pyplot as plt
import os

def plot(dir, csv_name):
    
    teste = pd.read_csv(f'{dir}/{csv_name}')
    
    plt.plot(teste['Father'])
    plt.plot(teste['Mother'])
    
    breaker = 100
    
    ticks = []
    ticks_label = []
    for index, tick in enumerate(teste['Generation']):
        
        if index == 0:
            ticks.append(tick)
            ticks_label.append(tick)
        
        elif index == len(teste['Generation']) - 1:
            ticks.append(tick)
            ticks_label.append(tick)
            
        elif tick % breaker == 0:    
            ticks.append(tick)
            ticks_label.append(tick)
    
    plt.xticks(ticks, ticks_label)
    #plt.xticks(range(len(teste['Generation'])), teste['Generation'])
    
    #axes = plt.gca()
    #axes.set_ylim([0, 26])
    
    #plt.show()
    plt.savefig(f'data/graphs/{csv_name}.png')
    plt.clf()
    
if __name__ == "__main__":
    
    files = os.listdir('data/champion_csv')
    for file in files:
        plot('data/csv', file)
        
    #csv_name = 'ipg15_steps70_rounds10000_mutation0.3.csv'
    #plot(csv_name)