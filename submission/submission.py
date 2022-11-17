"""Player submission script"""

# RL_TRAINING = True
# RL_NAME = "test"
# N_TRAINING_TIMESTEPS = 500
# OBSERVATIONS = {
#         "leaving_horizon":  True,
#         "returning_horizon":True,
#         "occupancy_status": True,
#         "future_waterdraws":True,
#         "t_out":            True,
#         "t_out_6hr":        True,
#         "t_out_12hr":       True,
#         "ghi":              True,
#         "ghi_6hr":          True,
#         "ghi_12hr":         True,
#         "t_in":             True,
#         "t_wh":             True,
#         "e_ev":             True,
#         "time_of_day":      True,
#         "community_demand": True,
#         "my_demand":        True
#     }

def reward(home):
    """
    Reward function
    :input:
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

    if home.obs_dict['occupancy_status'] == 0:
        hvac_action = 0 # neutral, leave the hvac alone
        wh_action = -1 # turn off the water heater
        ev_action = 1 # charge the car
        action = [hvac_action, wh_action, ev_action]

    else: 
        action = home.action_space.sample() # choose a random action

    return action


