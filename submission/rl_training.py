from stable_baselines3 import SAC
import numpy as np

def reward(home):
    """
    Reward function
    :input:
    """
    # print(home.obs_dict)
    reward = home.obs_dict['my_demand'] / 3.5
    return reward

def normalization(home):
    normalized_obs = []
    for name, value in sorted(home.obs_dict.items()):
        if "t_out" in name:
            norm_value = norm_helper(value, np.max(home.home.all_oat), np.min(home.home.all_oat))
        elif "t_in" in name:
            norm_value = norm_helper(value, 22, 18)
        elif "time_of_day" in name:
            norm_value = norm_helper(value, 24, 0)
        elif "ghi" in name:
            norm_value = norm_helper(value, np.max(home.home.all_ghi), 0)
        else:
            norm_value = value
        normalized_obs += [norm_value]
    return normalized_obs

def train(home): # could also make training_env and arg of train 
    # training_env = 
    num_training_steps = 50
    agent = SAC("MlpPolicy", home, verbose=1)
    agent.learn(num_training_steps)
    agent.save("../../submission/my_test.zip")

def norm_helper(value, exp_max, exp_min):
    """ This helper function returns a value that
    is approximately between [-1,1] given a value,
    the expected max and the expected min. """
    return 2 * (value / (exp_max - exp_min)) - 1
