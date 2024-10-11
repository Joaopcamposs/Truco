import gym
from stable_baselines3 import PPO

# Criar um ambiente de truco personalizado com Gym seria necessário
# Mas como exemplo, vamos usar um ambiente básico do Gym
env = gym.make("CartPole-v1")

# Criando o agente de RL
model = PPO("MlpPolicy", env, verbose=1)

# Treinando o modelo
model.learn(total_timesteps=10000)

# Salvando o modelo
model.save("truco_model")

# Carregando e usando o modelo
model = PPO.load("truco_model")

obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, dones, info = env.step(action)
    env.render()
