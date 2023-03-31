from os.path import normpath
import numpy as np

class EnvSimulation(): # Classe que simula o ambiente
    def __init__(self, agent, n, prob=0.2): # Inicializa o objeto EnvSimulation, com o agente e o tamanho do ambiente e a probabilidade de uma posição estar suja 20%
        self.agent = agent
        self.n = n
        self.prob = prob
        self.verbose = True
        
    def print_environment(self, env): # Imprime o ambiente
        print(env)
    
    def get_total_positions_dirty(self, env): # Retorna o número de posições sujas
      return np.sum(env)

    def create_environment(self): # Cria o ambiente com as posições sujas

        def convert_to_boolean(x, prob=0.2): # Converte o ambiente em booleano
            return True if x < prob else False  

        self.env = np.random.random((self.n,self.n)) # Cria uma matriz com valores aleatórios entre 0 e 1
        func_vectorized = np.vectorize(convert_to_boolean) # Converte a função convert_to_boolean em vetorizada
        self.env = func_vectorized(self.env, self.prob) # Aplica a função convert_to_boolean em cada elemento da matriz
        return self.env

    def run_simulation(self, env): # Executa a simulação
        costs = 0
        i = 0

        while (self.get_total_positions_dirty(env) != 0): # Enquanto houver posições sujas, o agente limpa
              action = self.agent.get_action(env) # Recebe a ação do agente
              if (self.verbose): # Imprime as informações
                  perceptions, dirty = self.agent.get_perceptions(env)
                  p_x, p_y = self.agent.x, self.agent.y
                  print("step {} - action {} - position {} - dirty {}".format(i, action[0].upper(), (p_x, p_y), dirty))
              if (action == "suck"):
                  if (self.agent.suck(env)):
                      costs += 1
              else:
                  if (self.agent.move(action, env)):
                      costs += 1
              i+=1
        return costs
    
    def run_simulation_model(self,env):
        costs = 0
        self.agent.model_move(env)