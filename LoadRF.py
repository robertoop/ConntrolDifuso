import gym
from rl.agents import DDPGAgent
from rl.memory import SequentialMemory
import time
from RedesPrueba import *

from tensorflow.keras.optimizers import Adam

env = gym.make('Pendulum-v1',g=5)
nb_actions = env.action_space.shape[0]
nb_observaciones=env.observation_space.shape

Actor=GenActor(nb_observaciones,nb_actions)
Critico, action_input=GenCritico(nb_observaciones,nb_actions)

#Creamos Memoria para guardar lo que le pase
memory = SequentialMemory(limit=10000, window_length=1)

#LLamamos a nuestro agente de aprendizaje
agent = DDPGAgent(nb_actions=nb_actions, actor=Actor, critic=Critico, critic_action_input=action_input,
                  memory=memory)
agent.compile(Adam(learning_rate=.001, clipnorm=1.), metrics=['mae'])


observaciones=env.reset()
agent.load_weights(filepath="MiIA2.h5")

print(observaciones)


for i in range(5000):
    accion=agent.forward(observaciones)
    print ("Accion a tomar", accion)
    observaciones, reward, done, info = env.step (accion)
    #time.sleep (0.1)
    env.render ()
