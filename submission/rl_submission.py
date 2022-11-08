from stable_baselines3 import SAC

RL_NAME = "my_agent"
NUM_TIMESTEPS = 25

def reward(home):
    """
    Reward function
    """
    # print(home.obs_dict)
    reward = home.obs_dict['my_demand'] / 3.5
    return reward

def create_model(home):
	model = SAC("MlpPolicy", home, verbose=1)
	return model