"""Tests for submitted functions"""

import unittest
import submission


class SubmissionLib(unittest.TestCase):
    def test_reward(self):
        """
        General test for reward function
        """
        home = 0
        self.assertEquals(submission.reward(home), 0)

    def test_predicit(self):
        """
        General test for predict function
        """
        home = 0
        self.assertEquals(submission.predict(home), 0)


if __name__ == '__main__':
    unittest.main()
