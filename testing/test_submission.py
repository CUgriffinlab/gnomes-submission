"""Tests for submitted functions"""

import unittest
import submission


class SubmissionLib(unittest.TestCase):
    def test_reward(self):
        """
        General test for reward function
        """
        self.assertEquals(submission.reward(), 0)

    def test_predicit(self):
        """
        General test for predict function
        """
        self.assertEquals(submission.predict(), 0)


if __name__ == '__main__':
    unittest.main()
