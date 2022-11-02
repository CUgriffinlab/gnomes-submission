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

    if home.obs_dict['occupancy'] == 0:
        hvac_action = 0 # neutral, leave the hvac alone
        wh_action = -1 # turn off the water heater
        ev_action = 1 # charge the car
        action = [hvac_action, wh_action, ev_action]

    else: 
        action = home.action_space.sample() # choose a random action

    return action