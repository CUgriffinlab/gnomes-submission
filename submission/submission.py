def predict(home):
    """
    Predict function
    :input: the current state of the environment as a list
    :output:
    """
    if home.obs_dict['occupancy_status'] == 0:
        hvac_action = 0 # neutral, leave the hvac alone
        wh_action = -1 # turn off the water heater
        ev_action = 1 # charge the car
        action = [hvac_action, wh_action, ev_action]

    else: 
        action = home.action_space.sample() # choose a random action

    return action
