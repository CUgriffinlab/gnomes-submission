from datetime import datetime
import asyncio
import os
import random

from dragg_comp.player import PlayerHome
from dragg_comp.rl_aggregator import RLAggregator
from submission import predict, reward

class PlayerSubmission(PlayerHome):
	def __init__(self):
		super().__init__()

	def get_reward(self):
		# redefines get_reward with the player's implementation
		my_reward = reward(self)
		return my_reward

if __name__=="__main__":
	tic = datetime.now()
	env = PlayerSubmission()
	env.reset()
	for _ in range(env.num_timesteps * env.home.dt):
	    action = predict(env)
	    env.step(action) 

	asyncio.run(env.post_status("done"))
	toc = datetime.now()
	print(toc-tic)