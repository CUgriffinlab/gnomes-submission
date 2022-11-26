# for an RBC agent

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

# for an RL agent
from submission.rl_training import *

def predict(home):
    agent = SAC.load("../../submission/my_test")
    norm_obs = normalization(home)
    action = agent.predict(norm_obs)[0]
    return action