"""Tests for submitted functions"""

import unittest
import submission

import gym.spaces
import numpy as np

class MockPlayerHome:
    def __init__(self):
        self.action_space = gym.spaces.Box(-1 * np.ones(3), np.ones(3))
        self.obs_dict = {"t_in_current":True,
            "t_out_current":True,
            "t_out_6hr":True,
            "t_our_12hr":True,
            "h_out":True,
            "h_out_6hr":True,
            "h_out_12hr":True,
            "time_of_day":True,
            "day_of_week":True,
            "is_holiday":True,
            "occupancy":True, 
            "my_demand":True}

class SubmissionLib(unittest.TestCase):
    def test_reward(self):
        """
        General test for reward function
        """
        home = MockPlayerHome()
        reward = submission.reward(home)
        try:
            self.assertIsInstance(reward, float)
        except:
            self.assertIsInstance(reward, int, msg=f"Ensure the reward function returns a single numeric value. Currently returning a value of type {type(reward)}")

    def test_predict(self):
        """
        General test for predict function
        """
        home = MockPlayerHome()
        self.assertIsInstance(list(submission.predict(home)), list, msg="Ensure")


if __name__ == '__main__':
    unittest.main()
