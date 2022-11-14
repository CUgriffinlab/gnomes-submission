from stable_baselines3 import SAC

RL_NAME = "my_agent"
NUM_TIMESTEPS = 25
OBSERVATIONS = {
	"leaving_horizon":	True,
	"returning_horizon":True,
	"occupancy_status": True,
	"future_waterdraws":True,
	"t_out":			True,
	"t_out_6hr":		True,
	"t_out_12hr":		True,
	"ghi":				True,
	"ghi_6hr":			True,
	"ghi_12hr":			True,
	"t_in":				True,
	"t_wh":				True,
	"e_ev":				True,
	"time_of_day":		True,
	"community_demand":	True,
	"my_demand": 		True
}

def rl_reward(home):
    """
    Reward function
    """
    # print(home.obs_dict)
    reward = home.obs_dict['my_demand'] / 3.5
    return reward

def create_model(home):
	model = SAC("MlpPolicy", home, verbose=1)
	return model