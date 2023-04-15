import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from Agent import Agent
from EnvSimulation import EnvSimulation

'''
n_max = 100
steps_model = []

for i in range(n_max):
    ag = Agent()
    es = EnvSimulation(ag, n=5)
    env = es.create_environment()
    es.run_simulation_model(env)
    steps_model.append(ag.costs)
for i in range(n_max):
    ag = Agent()
    es = EnvSimulation(ag, n=10)
    env = es.create_environment()
    es.run_simulation_model(env)
    steps_model.append(ag.costs)
for i in range(n_max):
    ag = Agent()
    es = EnvSimulation(ag, n=100)
    env = es.create_environment()
    es.run_simulation_model(env)
    steps_model.append(ag.costs)
    

print(steps_model)


 
agent_model = {
    "5x5" : np.mean(steps_model[0:n_max-1]),
    "10x10" : np.mean(steps_model[n_max:n_max*2-1]),
    "100x100" : np.mean(steps_model[2*n_max:n_max*3-1])
}
print(agent_model)


'''

n_max = 10
steps_model = []

'''
#Agent Simple Reflex
for i in range(n_max):
    ag = Agent()
    es = EnvSimulation(ag, n=5)
    env = es.create_environment()
    steps_model.append(es.run_simulation(env))
for i in range(n_max):
    ag = Agent()
    es = EnvSimulation(ag, n=10)
    env = es.create_environment()
    steps_model.append(es.run_simulation(env))
for i in range(n_max):
    ag = Agent()
    es = EnvSimulation(ag, n=100)
    env = es.create_environment()
    es.run_simulation(env)
    steps_model.append(es.run_simulation(env))
    
'''

ag = Agent()
es = EnvSimulation(ag, n=100)
env = es.create_environment()
es.run_simulation(env)
steps_model.append(es.run_simulation(env))


#print(steps_model)


 
agent_simple = {
    "5x5" : np.mean(steps_model[0:n_max-1]),
    "10x10" : np.mean(steps_model[n_max:n_max*2-1]),
    "100x100" : np.mean(steps_model[2*n_max:n_max*3-1])
}
print(agent_simple)








'''mean_performance = []
mean_performance.append(np.mean(steps_model[0:2]))
mean_performance.append(np.mean(steps_model[3:5]))
mean_performance.append(np.mean(steps_model[6:8]))
print(mean_performance)
plt.bar(agent_1.keys(), mean_performance)
plt.ylabel("Mean performance")
plt.show()'''
