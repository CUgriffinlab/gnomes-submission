"""Template for submission"""


def predict(home):
    """
    Simple rule-based prediction function as a template

    Parameters
    ----------
    home : dragg_comp.player.PlayerHome
        Your home

    Returns
    -------
    list
        List of actions corresponding to hvac, wh, and electric vehicle
    """
    # Rule-based control
    if home.obs_dict['occupancy_status'] == 0:  # no one home
        hvac_action = 0  # neutral, leave the hvac alone
        wh_action = -1  # turn off the water heater
        ev_action = 1  # charge the car
        action = [hvac_action, wh_action, ev_action]

    else:  # Someone is home
        action = home.action_space.sample()  # choose a random action

    # Ensure all actions are positive
    action = [0 if i < 0 else i for i in action]

    return action
