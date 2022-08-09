from datetime import datetime
import asyncio
import os
import random
import argparse

from dragg_comp.player import PlayerHome
from dragg_comp.rl_aggregator import RLAggregator
from submission import predict, reward

REDIS_URL = "redis://localhost"

class PlayerSubmission(PlayerHome):
	def __init__(self, redis_url=REDIS_URL):
		super().__init__()

	def get_reward(self):
		# redefines get_reward with the player's implementation
		my_reward = reward(self)
		return my_reward

if __name__=="__main__":

	parser = argparse.ArgumentParser()

	#-db DATABSE -u USERNAME -p PASSWORD -size 20
	parser.add_argument("-r", "--redis", help="Redis host URL", default=REDIS_URL)

	args = parser.parse_args()

	tic = datetime.now()
	env = PlayerSubmission(redis_url=args.redis)
	env.reset()
	for _ in range(env.num_timesteps * env.home.dt):
	    action = predict(env)
	    env.step(action) 

	asyncio.run(env.post_status("done"))
	toc = datetime.now()
	print(toc-tic)