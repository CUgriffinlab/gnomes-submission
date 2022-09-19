"""Player submission script"""

def reward(home):
    """
    Reward function
    """
    # print(home.obs_dict)
    reward = home.obs_dict['my_demand'] / 3.5
    return reward

def predict(home):
    """
    Predict function
    :input: the current state of the environment as a list
    :output:
    """
    threshold = 2 # kW

    if home.obs_dict['my_demand'] >= threshold:
        action = [0,0,0] # do nothing

    else: 
        action = list(home.action_space.sample()) # choose a random action
        print(action)
    return action