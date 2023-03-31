import numpy as np

class Agent():
    def __init__(self, n=5):  # Inicializa o objeto Agent, com a posição aleatória no ambiente n x n = 5 x 5
        position = np.random.randint(0, n, 2)  # Valor aleatório entre 0 e n, com 2 valores (tupla)
        self.x = position[0] # Posição x do agente
        self.y = position[1] # Posição y do agente
        self.costs = 0 # Custo total do agente

        
    def print_position(self, Agent): # Retorna a posição do agente
      print(self.x, self.y)

    def get_perceptions(self, environment): # Retorna as percepções do agente
        north, south, west, east = True, True, True, True # Inicializa as percepções como verdadeiras
        dim = environment.shape[0] # Dimensão do ambiente
        
        if self.y == 0: # Se o agente estiver na borda do ambiente, a percepção é falsa
          west = False
        if self.y == dim-1:
          east = False
        if self.x == 0:
          north = False
        if self.x == dim-1:
          south = False
        perceptions = { # Dicionário com as percepções
            "north" : north, 
            "south" : south, 
            "west" : west, 
            "east" : east
        }
        dirty = environment[self.x][self.y] # Retorna se a posição atual está suja
        return perceptions, dirty # Retorna as percepções e se a posição atual está suja
      

    def get_action(self, env): # Retorna a próxima ação do agente baseada nas suas percepções e na posição atual.
      perceptions, dirty = self.get_perceptions(env) # Recebe as percepções e se a posição atual está suja
      actions = ["north", "east", "west", "south", "suck"] # Lista de ações
      
      while True:
        if dirty == True: # Se estiver sujo, o agente limpa
          return "suck"
        action = np.random.choice(actions) # Escolhe uma ação aleatória
        
        if ((action == "north") and (perceptions["north"])): # Se a ação for para o norte e a percepção para o norte for verdadeira, 
            return "north"                                   # ou seja o agente não está na borda do ambiente, retorna a ação     
        elif ((action == "south") and (perceptions["south"])):
          return "south"
        elif ((action == "west") and (perceptions["west"])):
          return "west" 
        elif ((action == "east") and (perceptions["east"])):
          return "east"               
      return action    
          
    def move(self, action, env): # Move o agente para a direção escolhida
        perceptions, dirty = self.get_perceptions(env) # Recebe as percepções e se a posição atual está suja
        if ((action == 'north') and (perceptions['north'])): # Se a ação for para o norte e a posição norte está livre, então subtrai 1 da posição y. Ou seja, suba uma linha na matriz
          self.x -= 1
          return True
        elif ((action == 'south') and (perceptions['south'])):
          self.x += 1   
          return True     
        elif ((action == 'west') and (perceptions['west'])):
          self.y -= 1
          return True
        elif ((action == 'east') and (perceptions['east'])):
          self.y += 1
          return True
        else:
          return False 
    
    def print_step(self, env, action, dirty):
      #print("step {costs} - action: {action} - position {self.x},{self.y} - dirty {dirty}".format(costs=self.costs, self=self, action=action, dirty=dirty))
      self.costs += 1
      
    def model_move(self, env):
       k=0
       n = len(env[0])
       
       while self.x > 0:
          self.print_step(env, "north", env[self.x][self.y])
          dirty = env[self.x][self.y]
          if dirty:
             env[self.x][self.y] = False
             self.print_step(env, "suck", env[self.x][self.y])
          self.x -= 1
          
       while self.y > 0:
          self.print_step(env, "west", env[self.x][self.y])
          dirty = env[self.x][self.y]
          if dirty:
            env[self.x][self.y] = False
            self.print_step(env, "suck", env[self.x][self.y])
          self.y -= 1
         
 
       camada = 0
       ajuste = 0
       
       while camada <= n:
    
        for j in range(camada,n-1-camada+ajuste):  # primeira linha ate a ultima coluna
            self.y += 1
            dirty = env[self.x][self.y]
            self.print_step(env, "east", dirty)
  
            if dirty:
               env[self.x][self.y] = False
               self.print_step(env, "suck", env[self.x][self.y])
  
            ajuste = 1   
            
        for i in range(camada,n-1-camada): # ultima coluna ate a ultima linha
            self.x += 1
            dirty = env[self.x][self.y]
            self.print_step(env, "south", dirty)

            if dirty:
               env[self.x][self.y] = False
               self.print_step(env, "suck", env[self.x][self.y])
  
            
        for j in range(n-1-camada, camada, -1): # ultima linha ate a primeira coluna
            self.y -= 1
            dirty = env[self.x][self.y]
            self.print_step(env, "west", dirty)

            if dirty:
               env[self.x][self.y] = False
               self.print_step(env, "suck", env[self.x][self.y])
  
        for i in range(n-1-camada, camada+1, -1): # primeira coluna ate a primeira linha
            self.x -= 1
            dirty = env[self.x][self.y]
            self.print_step(env, "north", dirty)
            
            if dirty:
               env[self.x][self.y] = False
               self.print_step(env, "suck", env[self.x][self.y])
  
        camada+=1
    

    def suck(self, env): # Limpa a posição atual do agente
        perceptions, dirty = self.get_perceptions(env) # Recebe as percepções e se a posição atual está suja
        if (dirty): # Se a posição atual estiver suja, limpa e retorna True
          env[self.x][self.y] = False
          return True
        else:
          return False