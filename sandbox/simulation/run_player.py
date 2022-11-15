from datetime import datetime
import asyncio
import argparse

from dragg_comp.player import PlayerHome
# import submission.rbc as submission
import submission.rl as submission
from stable_baselines3 import SAC

REDIS_URL = "redis://localhost"

class PlayerSubmission(PlayerHome):
	def __init__(self, redis_url=REDIS_URL, rl_name="my_agent"):
		super().__init__(redis_url=redis_url)
		
		self.rl_name = rl_name
		if self.rl_name:
			self.update_states(submission.OBSERVATIONS)
		self.agent = None

	def get_reward(self):
		# redefines get_reward with the player's implementation
		my_reward = submission.reward(self)
		return my_reward

	def get_prediction(self):
		if self.rl_name:
			if not self.agent:
				self.agent = SAC.load(f"../../submission/{self.rl_name}")
			return self.agent.predict(self.get_obs())[0]
		else:
			return submission.predict(self)

if __name__=="__main__":

	parser = argparse.ArgumentParser()

	#-db DATABSE -u USERNAME -p PASSWORD -size 20
	parser.add_argument("-r", "--redis", help="Redis host URL", default=REDIS_URL)
	args = parser.parse_args()

	env = PlayerSubmission(redis_url=args.redis, rl_name=submission.RL_NAME)
	
	rl = True
	if rl:
		print("Training your RL agent...")
		model = submission.create_model(env)
		model.learn(submission.NUM_TIMESTEPS)
		model.save(f"../../submission/{env.rl_name}")

	obs = env.reset()
	tic = datetime.now()
	print("Testing your agent...")
	for _ in range(env.num_timesteps):
		if rl:
			action = env.get_prediction()
		else:
			action = predict(env)
		env.step(action)

	asyncio.run(env.post_status("done"))
	print(env.score())
	toc = datetime.now()
	print(toc-tic)

