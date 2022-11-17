RL_TRAINING = False
RL_NAME = None


from datetime import datetime
import asyncio
import argparse

from dragg_comp.player import PlayerHome
from submission.submission import *
# from stable_baselines3 import SAC

REDIS_URL = "redis://localhost"

class PlayerSubmission(PlayerHome):
	def __init__(self, redis_url=REDIS_URL, rl_name="my_agent"):
		super().__init__(redis_url=redis_url)
		
		self.rl_name = rl_name
		if self.rl_name:
			self.update_states(OBSERVATIONS)
		self.agent = None

	def get_reward(self):
		# redefines get_reward with the player's implementation
		my_reward = reward(self)
		return my_reward

	def get_prediction(self):
		return predict(self)

if __name__=="__main__":

	parser = argparse.ArgumentParser()

	#-db DATABSE -u USERNAME -p PASSWORD -size 20
	parser.add_argument("-r", "--redis", help="Redis host URL", default=REDIS_URL)
	args = parser.parse_args()

	env = PlayerSubmission(redis_url=args.redis, rl_name=RL_NAME)
	
	if RL_TRAINING:
		print("Training your RL agent...")
		model = create_model(env)
		model.learn(NUM_TIMESTEPS)
		model.save(f"../../submission/{env.rl_name}")

	obs = env.reset()
	tic = datetime.now()
	print("Testing your agent...")
	for _ in range(env.num_timesteps):
		action = env.get_prediction()
		env.step(action)

	asyncio.run(env.post_status("done"))
	print(env.score())
	toc = datetime.now()
	print(toc-tic)

