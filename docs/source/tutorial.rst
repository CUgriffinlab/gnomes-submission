Tutorial of Submission
======================

Getting Started
---------------
#. You MUST register your team with the competition hosts. Please email cugriffinlab@gmail.com with:

	* Your team name
	* The names of all teammates (limit 2 members per team)
	* The GitHub usernames of all teammates. If you do not have a GitHub account, create one `here <https://github.com/join>`_.

#. This competition will use `github <https://github.com/about>`_ to track submissions and `docker <https://docs.docker.com/get-started/overview/>`_ to ensure consistency/fairness of simulation enviornments accross participants. Do not worry if this is your first time hearing about either of these, we will be providing step-by-step instructions for their usage.

	* Download and configure git following `these instructions <https://docs.github.com/en/get-started/quickstart/set-up-git>`_.
	* Test your configuration by opening the Terminal (Mac) or PowerShell (Windows) application and copy and paste ``git --version`` into the window. After pressing <Enter>, the current version of git should be printed. If not, email cugriffinlab@gmail.com for help.
	* Download and configure docker desktop by following `these instructions for mac <https://docs.docker.com/desktop/install/mac-install/>`_ or `these instructions for windows <https://docs.docker.com/desktop/install/windows-install/>`_.
	* Test your configuration by opening the Terminal (Mac) or PowerShell (Windows) application and enter the command ``$ docker --version`` into the window. Throughout this tutorial (and many help guides) we will use ``$`` to indicate system commands in Terminal/PowerShell. Do not include the ``$`` in the command. After pressing <Enter>, the current version of docker should be printed. If not, email cugriffinlab@gmail.com for help.

#. Wait for us to make you a shiny new submission repository! For security purposes, it is important that we maintain ownership of the repository, so we will let you know when one is created for you (we will aim to do so within 1 day of your request to join).

Using GitHub
------------

#. Copy the repository from GitHub to your computer using git clone:

	* ``$ git clone https://github.com/cugriffinlab/YOUR-USERNAME-gnomes``. This will create a folder called your-username-gnomes with all the files in the your-username-gnomes repository
	
If this is your first time using git, you may also have to set up your username and password with the following commands:

	* ``$ git config --global user.name "FIRSTNAME LASTNAME"``
	* ``$ git config --global user.email "YOURNAME@colorado.edu"``
	
Where you replace "FIRSTNAME LASTNAME" "YOURNAME" with your desired name/email.
	
#. Create a GitHub security token following the steps below. GitHub uses Personal Access Tokens as a method of two-factor authentication which is much more secure than simply using a password. The Personal Access Token will be a long string of randomly generated letters and numbers to enhance security and ensure it is hard to guess.
	* Create a personal access token
	* On git go to your username > settings.
	* Settings > Developer settings
	* Developer settings > Personal Access Tokens
	* Generate a new access token, select the button next to Repositories to give this access token permission to read/write to repositories associated with your account. The point of this access token is to access your git account from the command line, so that can be the “message”. The message isn’t important though (just a reminder for later).
	* Copy this token! If you forget it you might need to redo the following steps.
	* Set the remote to be a new URL that has read/write permissions to your Github account.
	* In your terminal, from the directory named YOUR-USERNAME-gnomes, use the following command, replacing the YOUR-USERNAME and PERSONAL-ACCESS-TOKEN fields:
`` $ git remote set-url origin https://YOUR-USERNAME:PERSONAL-ACCESS-TOKEN@github.com/cugriffinlab/YOUR-USERNAME-gnomes.git``


#. Edit the submission file as described below and then commit/push them to your GitHub repository:

	* ``$ git commit submission/submission.py -m “Custom message about improvement”``
	* ``$ git push``

Creating your submission
------------------------

For a complete submission you should customize the `predict()` function to determine an action for your gnome home to take. In both of these functions you may use any of the available observations about your home. Here is a list of the valid keys to `home.obs_dict`:

	#. "t_in", current indoor temperature (deg C)
	#. "t_wh", current temperature of the hot water tank (deg C)
	#. "t_out", current indoor temperature (deg C)
	#. "t_out_6hr", predicted outdoor temperature in 6 hrs (deg C)
	#. "t_out_12hr", predicted outdoor temperature in 12 hrs (deg C)
	#. "ghi", current outdoor humidity (%)
	#. "ghi_6hr", predicted outdoor humidity in 6 hrs (%)
	#. "ghi_12hr", predicted outdoor humidity in 12 hrs (%)
	#. "time_of_day", time of day (0-24)
	#. "day_of_week", day of week (0-6)
	#. "occupancy", true/false value for occupancy status
	#. "my_demand", current net electric consumption (kW)
	
If you're a beginner Python user, you might find `this basic tutorial <https://docs.google.com/document/d/1uhLihn5cZ-GQbUI86SKiO8q5rFj1STvrtLansYbwZ30/edit?usp=sharing>`_ useful.
	
The predict function
^^^^^^^^^^^^^^^^^^^^
The `predict(home)` function is directly related to the performance of the agent and provides the action to be performed at the next timestep. You are predicting the best action(s) to take. The output in three parts describes the action for:

	#.	The HVAC setpoint
	#.	The water heater on/off status
	#.	The electric vehicle charge command
	
The resulting action should be a list (or array) that is 3 entries long, and each entry should be a number between [-1,1]. For the HVAC this will change the setpoint between the lowest possible value and the highest possible value. For the water heater a low value (-1) will turn the water heater off, and a high value will turn the water heater on whenever possible, intermediate values will correspond to being on part of the time interval (e.g. 0 corresponds to an average power consumption of 50% over the 15 minute interval). For the electric vehicle the charge is interpolated between the maximum possible charge (+5kW) and the maximum possible discharge to the grid (-5kW). 

Once you change the submission/submission.py file no further changes need to be made to make a valid submission.

Testing your submission (locally)
---------------------------------

To test your agent you can run the same simulation setup as the official competition on sandbox data. In real life you won’t be able to test performance on the real (future) weather data before deployment, you only have data from the past. Therefore the data we use to officially score you will be “new”, never seen before weather data (but with the same location and weather trends).

Testing submission validity using Docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use Docker to manage the dependencies of the DRAGG engine. Note, this Docker impelentation is only officially supported on intel-based hardware. For other hardware, such as M1 Apple computers, use the non-docker instructions in the next section.

	#.	Open the Terminal (Mac) or Command Prompt (Windows) application and copy and paste the following commands into the window. Each time press <Enter> to run the command.
	
		* Optional: Change into the Documents folder. When you open Terminal/Command you will likely be in the home (or 'C://' drive), but you can change to Documents with ``$ cd Documents`` 
	
	#. 	Clone the repository using ``$ git clone https://github.com/cugriffinlab/your-username-gnomes.git``
	#.	Change to the current working directory using ``$ cd your-username-gnomes``
	#.	Use Docker to build the tests using ``$ docker-compose -f ./testing/docker-compose.yml build`` (make sure Docker is open on your computer).
	#.	Use Docker to run the tests using ``$ docker-compose -f ./testing/docker-compose.yml up --abort-on-container-exit``. Submissions must pass all tests!

Testing submission validity for non-docker setups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section is only to be used for non-intel setups.

	#. Follow steps 1-3 in the previous section

	#. Install python using `this tutorial <https://docs.python.org/3/using/mac.html>`_.

	#. Install DRAGG engine using ``$ pip install dragg``

	#. Install the DRAGG competition engine using ``$ pip install dragg-comp``

	#. Install your submission using ``$ pip install -e .``

	#. Test your submission by running ``$ python ./testing/test_submission.py``

Self-evaluation testing with Docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use Docker to manage the dependencies of the DRAGG engine. Note, this Docker impelentation is only officially supported on intel-based hardware. For other hardware, see the next section.

	#.	Open the Terminal (Mac) or Command Prompt (Windows) application and copy and paste the following commands into the window. Each time press <Enter> to run the command.
	
		* Optional: Change into the Documents folder. When you open Terminal/Command you will likely be in the home (or 'C://' drive), but you can change to Documents with ``$ cd Documents`` 
	
	#. 	Clone the repository using ``$ git clone https://github.com/cugriffinlab/your-username-gnomes.git``
	#.	Change to the current working directory using ``$ cd your-username-gnomes``
	#.	Build the simulation using ``$ docker-compose -f ./sandbox/docker-compose.yml build`` (make sure Docker is open on your computer).
	#.	Run the simulation using ``$ docker-compose -f ./sandbox/docker-compose.yml up --abort-on-container-exit``
	#.  The results of the simulation are in the folder ``sandbox/outputs``. 

Self-evaluation testing for non-docker setups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section is only to be used for non-intel setups.

	#. Follow steps 1-3 in the previous section

	#. Install python using `this tutorial <https://docs.python.org/3/using/mac.html>`_.

	#. Install DRAGG engine using ``$ pip install dragg``

	#. Install the DRAGG competition engine using ``$ pip install dragg-comp``

	#. Install your submission using ``$ pip install -e .``

	#. Install redis from `here <https://redis.io/download/>_`

		* Once you have installed redis, start the server using ``$ redis-server``

		* In another terminal window, you should be able to call ``$ redis-cli PING`` which should return ``PONG``.

	#. Install redis' python package using ``$ pip install redis``

	#. Open two new terminal windows

		* In each window, change the directory to the sandbox simulation folder using ``$ cd <your-username-gnomes>/sandbox/simulation``
	
		* In one terminal window, start the player submission using ``$ python run_player.py``

		* In the other terminal window, run the simualtion using ``$ python run_aggregator.py``

..
	[TODO Ash to write more about results, when decided]

Submitting and receiving official feedback
-----------------------------------------------------------
Your submission file must be updated and pushed to your repository in order to get official feedback. The official repository for the GNOMES competition will automatically evaluate all players’ submissions at 5AM Mountain Standard Time, if and only if their GitHub repositories are updated.

Check your score here! https://cugriffinlab.github.io/gnomes-admin/
