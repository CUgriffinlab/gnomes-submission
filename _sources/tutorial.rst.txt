Tutorial of Submission
============================
Getting Started
-------------------------------------------
#. You MUST register your team with the competition hosts. Please email cugriffinlab@gmail.com with:

	* Your team name
	* The names of all teammates
	* The GitHub usernames of all teammates. If you do not have a GitHub account, create one `here <https://github.com/join>`_.

#. This competition will use `github <https://github.com/about>`_ to track submissions and `docker <https://docs.docker.com/get-started/overview/>`_ to ensure consistency/fairness of simulation enviornments accross participants. Do not worry if this is your first time hearing about either of these, we will be providing step-by-step instructions for their usage.

	* Download and configure git following `these instructions <https://docs.github.com/en/get-started/quickstart/set-up-git>`_.
	* Test your configuration by opening the Terminal (Mac) or PowerShell (Windows) application and copy and paste ``git --version`` into the window. After pressing <Enter>, the current version of git should be printed. If not, email cugriffinlab@gmail.com for help.
	* Download and configure docker desktop by following `these instructions for mac <https://docs.docker.com/desktop/install/mac-install/>`_ or `these instructions for windows <https://docs.docker.com/desktop/install/windows-install/>`_.
	* Test your configuration by opening the Terminal (Mac) or PowerShell (Windows) application and copy and paste ``docker --version`` into the window. After pressing <Enter>, the current version of docker should be printed. If not, email cugriffinlab@gmail.com for help.

#. Wait for us to make you a shiny new submission repository! For security purposes, it is important that we maintain ownership of the repository, so we will let you know when one is created for you (we will aim to do so within 1 day of your request to join).

#. Copy the repository from GitHub to your computer using git clone:

	* ``$ git clone https://github.com/cugriffinlab/YOUR-USERNAME-gnomes``. This will create a folder called your-username-gnomes with all the files in the your-username-gnomes repository

#. Edit the submission file as described below and then commit/push them to your GitHub repository:

	* ``$ git commit submission/submission.py -m “Custom message about improvement”``
	* ``$ git push``

Creating your submission
-----------------------------------------------
For a complete submission you should customize the `reward()` function to evaluate performance and the `predict()` function to determine the action to take. In both of these functions you may use any of the available observations about your home. Here is a list of the valid keys to `home.obs_dict`.

	#. "t_in_current", current indoor temperature (deg C)
	#. "t_out_current", current indoor temperature (deg C)
	#. "t_out_6hr", predicted outdoor temperature in 6 hrs (deg C)
	#. "t_out_12hr", predicted outdoor temperature in 12 hrs (deg C)
	#. "h_out", current outdoor humidity (%)
	#. "h_out_6hr", predicted outdoor humidity in 6 hrs (%)
	#. "h_out_12hr", predicted outdoor humidity in 12 hrs (%)
	#. "time_of_day", time of day (0-24)
	#. "day_of_week", day of week (0-6)
	#. "occupancy", true/false value for occupancy status
	#. "my_demand", current net electric consumption (kW)
	

The reward function
^^^^^^^^^^^^^^^^^^^^^^^^^
While the GNOMES competition will provide holistic feedback on your performance, the `reward(home)` function can be useful to provide step-by-step feedback on performance. This is similar to how the machine learning algorithm “Reinforcement Learning” works: certain observations and actions can be categorized as “good” or “bad” (or anywhere in between) via the reward observed and you can build intuition without exact knowledge.

For example, let's say the competition reward algorithm was very complicated and nearly impossible to model but you notice it is strongly correlated with a low amount of energy consumed at any given timestep. You can "grade" your agent based off a very simple reward function such as:

``reward = -1 * home.obs_dict["my_demand"]``

We encourage you to try other transformations to get your home working well. You might look into different optimization objectives that you think could work to approximate the goals of the competition.

The predict function
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The `predict(home)` function is more directly related to the performance of the agent and provides the action to be performed at the next timestep. You are predicting the best action(s) to take. The output in three parts describes the action for:

	#.	The HVAC setpoint
	#.	The water heater on/off status
	#.	The electric vehicle charge command
	
The resulting action should be a list (or array) that is 3 entries long, and each entry should be a number between [-1,1]. For the HVAC this will change the setpoint between the lowest possible value and the highest possible value. For the water heater a low value (-1) will turn the water heater off, and a high value will turn the water heater on whenever possible, intermediate values will correspond to being on part of the time interval (e.g. 0 corresponds to a 50% duty cycle over the 15 minute interval). For the electric vehicle the charge is interpolated between the maximum possible charge (+5kW) and the maximum possible discharge (-5kW). 

Once you change the submission/submission.py file no further changes need to be made. To be clear: you should only change the contents of submission.py; submission.py is the only file you are allowed to change and it is the only change that will be applicable to the competition performance.

Testing your submission (locally)
-------------------------------------------
To test your agent you can run the same simulation setup as the official competition on sandbox data. In real life you won’t be able to test performance on the real (future) weather data before deployment, you only have data from the past. Therefore the data we use to officially score you will be “new”, never seen before weather data (but with the same location and weather trends).

	* The steps to ensure the submission file is valid (i.e. no changes have been made that will break the submission):

		#.	Open the Terminal (Mac) or Command Prompt (Windows) application and copy and paste the following commands into the window. Each time press <Enter> to run the command.
		
			* Optional: Change into the Documents folder. When you open Terminal/Command you will likely be in the home (or 'C://' drive), but you can change to Documents with ``cd Documents`` 
		
		#. 	Clone the repository using ``git clone https://github.com/cugriffinlab/your-username-gnomes.git``
		#.	Change to the current working directory using ``cd your-username-gnomes``
		#.	Build the tests using ``docker-compose -f ./testing/docker-compose.yml build``
		#.	Run the tests using ``docker-compose -f ./testing/docker-compose.yml up --abort-on-container-exit``. Submissions must pass all tests!

	* The steps for self-evaluation are as follows:

		#.	Open the Terminal (Mac) or Command Prompt (Windows) application and copy and paste the following commands into the window. Each time press <Enter> to run the command.
		
			* Optional: Change into the Documents folder. When you open Terminal/Command you will likely be in the home (or 'C://' drive), but you can change to Documents with ``cd Documents`` 
		
		#. 	Clone the repository using ``git clone https://github.com/cugriffinlab/your-username-gnomes.git``
		#.	Change to the current working directory using ``cd your-username-gnomes``
		#.	Build the simulation using ``docker-compose -f ./sandbox/docker-compose.yml build``
		#.	Run the simulation using ``docker-compose -f ./sandbox/docker-compose.yml up --abort-on-container-exit``
		#.  The results of the simulation are in the folder ``sandbox/outputs``. 
		
..
	[TODO Ash to write more about results, when decided]

Submitting and receiving official feedback
-----------------------------------------------------------
Your submission file must be updated and pushed to your repository in order to get official feedback. The official repository for the GNOMES competition will automatically evaluate all players’ submissions at 5AM Mountain Standard Time, if and only if their GitHub repositories are updated.

Check your score here! https://cugriffinlab.github.io/gnomes-admin/
