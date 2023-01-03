RL_TRAINING = False
RL_NAME = None

from datetime import datetime
import asyncio
import argparse
import pandas as pd

from dragg_comp.player import PlayerHome

REDIS_URL = "redis://localhost"

if __name__=="__main__":

	try:
		from submission.submission import *
		parser = argparse.ArgumentParser()

		#-db DATABSE -u USERNAME -p PASSWORD -size 20
		parser.add_argument("-r", "--redis", help="Redis host URL", default=REDIS_URL)

		args = parser.parse_args()

		env = PlayerHome(redis_url=args.redis)

		obs = env.reset()
		tic = datetime.now()
		print("Testing your agent...")
		for _ in range(env.num_timesteps):
			action = predict(env)
			env.step(action)

		asyncio.run(env.post_status("done"))
		print(env.score())
		toc = datetime.now()
		print(toc-tic)
	except:
		df = pd.DataFrame(
			{
				'std_demand': ['Invalid Submission'],
				'max_demand': ['Invalid Submission'],
				'l2_dev_avg': ['Invalid Submission'],
			}
		)
		df.to_csv('./outputs/score.csv')