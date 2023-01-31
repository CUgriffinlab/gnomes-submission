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
    if home.obs_dict['occupancy_status'] == 0:  # no one home
        hvac_action = 0  # neutral, leave the hvac alone
        wh_action = -1  # turn off the water heater
        ev_action = 1  # charge the car

    else:  # Someone is home
        hvac_action = 0  # no action
        wh_action = 0  # no action
        ev_action = 0  # no action

    action = [hvac_action, wh_action, ev_action]

    return action
