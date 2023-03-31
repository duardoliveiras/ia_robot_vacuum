from collections import deque

def bfs(matriz, x, y):
    n = len(matriz)
    visitado = [[False for _ in range(n)] for _ in range(n)]
    fila = deque([(x, y)])
    visitado[x][y] = True
    visitados = [(x, y)]
    
    caminho = [(x, y)]


    while fila:
        i, j = fila.popleft()
      
        # Adicionar os vizinhos não visitados à fila
        if i > 0 and not visitado[i-1][j]:  # Vizinho acima
            fila.append((i-1, j))
            caminho.append((i-1, j))

            visitado[i-1][j] = True
            visitados.append((i-1, j))
   
           
            
            
        if j > 0 and not visitado[i][j-1]:  # Vizinho à esquerda
            fila.append((i, j-1))
            caminho.append((i, j-1))
          
            visitado[i][j-1] = True
            visitados.append((i, j-1))

     
            
            
        if i < n-1 and not visitado[i+1][j]:  # Vizinho abaixo
            fila.append((i+1, j))
            caminho.append((i+1, j)) 

            visitado[i+1][j] = True
            visitados.append((i+1, j))
            
            
            
            
        if j < n-1 and not visitado[i][j+1]:  # Vizinho à direita
            fila.append((i, j+1))
            caminho.append((i, j+1))
            
            visitado[i][j+1] = True
            visitados.append((i, j+1))
    
       

    # Printar o caminho percorrido
    for i, j in caminho:
        print(f"({i}, {j}, {matriz[i][j]})")

# Exemplo de uso
matriz = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
x, y = 1, 1  # Ponto de partida aleatório
bfs(matriz, x, y)