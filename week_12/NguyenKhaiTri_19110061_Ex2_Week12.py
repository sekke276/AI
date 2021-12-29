import gym 
import time

environment = gym.make("MountainCar-v0")
observation = environment.reset()

while True:
    action = environment.action_space.sample()
    observation,reward, done, extra_info = environment.step(action)
    environment.render();
    
    
    if done:
        environment.close()
        break
    