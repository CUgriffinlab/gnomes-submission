Tutorial of Submission
============================
Getting Started
-------------------------------------------
#. You MUST register your team with the competition hosts. Please email cugriffinlab@gmail.com with:
	* Your team name
	* The names of all teammates
	* The GitHub usernames of all teammates

#. If you do not already have git and a GitHub account create one with the following links:
	#.	If you do not have a GitHub account, create one now. (https://github.com) 
	#.	If you do not have it already, download git (https://git-scm.com/downloads) 

#. Wait for us to make you a shiny new submission repository! It is important that we maintain ownership of the repository so we will let you know when one is created for you (we will aim to do so within 1 day of your request to join).

#.	Copy the repository from GitHub to your computer using git clone:
	* ``$ git clone https://github.com/cugriffinlab/YOUR-USERNAME-gnomes``. This will create a folder called your-username-gnomes with all the files in the your-username-gnomes repository

#.	Edit the submission file as described below and then commit/push them to your GitHub repository:
	* ``$ git commit submission/submission.py	-m “Custom message about improvement”``
	* ``$ git push``

Creating your submission
-----------------------------------------------
For a complete submission you should customize the reward function to evaluate performance and the predict function to determine the action to take.

While the GNOMES competition will provide holistic feedback on your performance, the reward function can be useful to provide step-by-step feedback on performance. This is similar to how the machine learning algorithm “Reinforcement Learning” works: certain observations and actions can be categorized as “good” or “bad” via the reward observed and you can build intuition without exact knowledge.

The predict function is more directly related to the performance of the agent and provides the action to be performed at the next timestep. You are predicting the best action(s) to take. The output in three parts describes the action for:

	#.	The HVAC setpoint
	#.	The water heater on/off status
	#.	The electric vehicle charge command

Once you change the submission/submission.py file no further changes need to be made. To be clear: you should only change the contents of submission.py; submission.py is the only file you are allowed to change and it is the only change that will be applicable to the competition performance.

Testing your submission (locally)
-------------------------------------------
To test your agent you can run the same simulation setup as the official competition on sandbox data. In real life you won’t be able to test performance on the real (future) weather data before deployment, you only have data from the past. Therefore the data we use to officially score you will be “new”, never seen before weather data (but with the same location and weather trends).

	* The steps to ensure the submission file is valid (i.e. no changes have been made that will break the submission):

		#.	Clone the repository using ``$ git clone https://github.com/cugriffinlab/your-username-gnomes.git``
		#.	Change to the current working directory using ``$ cd your-username-gnomes``
		#.	Install an editable version of your submission ``$ pip install --editable .``
		#.	Change into testing directory ``$ cd testing``
		#.	Run the tests ``$ python test_submission.py``

	* The steps for self-evaluation are as follows:

		#.	Download Docker (https://www.docker.com) which is a free software that allow you to replicate our setup easily. Docker will perform downloads and run the Python files in the order you need, without additional input.
		#.	Install Docker as directed. The downloaded file (\*.exe, \*.mkg) should guide you.
		#.	Check Docker is properly installed: go to your terminal or PowerShell and enter ``$ docker --version``
		#.	Change to the current working directory using ``$ cd dragg-comp-submission/sandbox``
		#.	Build the simulation using ``$ docker-compose build``
		#.	Run the simulation using ``$ docker-compose up --abort-on-container-exit``

Submitting and receiving official feedback
-----------------------------------------------------------
Your submission file must be updated and pushed to your repository in order to get official feedback. The official repository for the GNOMES competition will automatically evaluate all players’ submissions at 5AM Mountain Standard Time, if and only if their GitHub repositories are updated.