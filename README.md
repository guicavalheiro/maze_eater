# Maze Eater

Função de aptidão: Nossa função de aptidão consiste em somar as coordenadas do nodo em que o indivíduo termina seus movimentos, com o intuito de selecionar aqueles que chegam mais próximo do fim do labirinto.

Operador genético: Torneio, selecionando o pai (melhor indivíduo) e a mãe (segundo melhor indivíduo) e cruzando os mesmos gerando 2 filhos. Também passamos o pai para a próxima geração, com o pai e os 2 filhos temos um total de 3 indivíduos que já estarão compondo a próxima geração, o restante dos indivíduos serão gerados aleatoriamente.