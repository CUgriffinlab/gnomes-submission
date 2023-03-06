Tutorial of Creating an RL Agent
========================================

Reinforcement learning (RL) is a method of black-box machine learning, meaning that the RL agent can produce actions that optimize performance without knowing the mechanics of the environment. Like a child learning new things, RL agents can try an action, observe the outcome, and extrapolate about which actions are good and bad and when without ever knowing the exact physics behind transitions from one state to the next. As the human behind the RL agent you will have to give the RL agent clues to sort the outcomes into "good" and "bad". You will also be able to define other parameters of the RL agent such as which algorithms it uses, the amount of time you allow it to train, and which observations the RL should consider. We have provided a framework for you in the ``rl_training.py`` file (found in the sister repo https://github.com/cugriffinglab/gnomes-rl) and a description of how to implement it to create a custom agent below: 

We suggest that you copy the ``training\`` folder from the gnomes-rl repository.

Components of submission
----------------------------

The reward* function
^^^^^^^^^^^^^^^^^^^^^^^^^
While the GNOMES competition will provide holistic feedback on your performance, the `reward(home)` function can be useful to provide step-by-step feedback on performance.

For example, let's say the competition reward algorithm was very complicated and nearly impossible to model but you notice it is strongly correlated with a low amount of energy consumed at any given timestep. You can "grade" your agent based off a very simple reward function such as:

``reward = -1 * home.obs_dict["my_demand"]``

but there is no techincal limit to how complicated your function can be (we don't necessarily recommend this reward signal either, but you get the idea):

``reward = -1 * home.obs_dict["my_demand"] ** (home.obs_dict["occupancy"]) * np.sin(home.obs_dict["h_out_6hr"])``

We encourage you to try other transformations to get your home working well. You might look into different optimization objectives that you think could work to approximate the goals of the competition.

Reward should take the input argument `home`, and output the reward as a single floating point value.

The normalization* function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This function is intended to (1) filter the values that the reinforcement learning agent can consider and (2) normalize them to stabilize learning.

Since RL agents built on the OpenAI gym platform expect the observation values as a list of numbers (e.g. floats) you will need to parse the observation dictionary (home.obs_dict) to a list. You can build this list in any way you like, but consider that the list should pass the values in the same order every time (e.g. if you pass the values as [temperature, occupancy] you should continue to use that order; passing them as [occupancy, temperature] might confuse the agent).

Deep reinforcement learning is based on a series of neural networks that describe the relationships of inputs (actions and states) and outputs (rewards). Neural networks are "trained" to classify this relationship through gradient descent which depends on the error between the observed and predicted output. If the model uses multiple inputs (say temperature and occupancy status) the scale of the temperature value (e.g. 20 deg C) compared to the occupancy status (e.g. 0 or 1) can cause issues in updating weights of the network. Therefore it is recommended to normalize your values to be approximately have a mean of 0 and standard deviation of 1.

Normalization should take the input argument ``home``, and output the observation as a list (any length >= 1) of floating point values.

The train* function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The train function is what you will run locally to create an agent. The agent can be saved and evaluated later on by the official scoring mechanism of GNOMES.

It will be your responsibility to train your agent, save it, and provide a ``predict()`` method in ``submission.py`` that calls the agent from whatever method you used to store it. We have provided a framework using the popular RL library Stable-Baselines3 for you to get started.

Helper functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You may add any arbitrary helper function to `rl_training.py`.

Custom imports 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You may use any custom Python package in `rl_training.py`. 

\*Indicates that you should keep these function names to make use of the ``train_player.py`` script. We will not be running ``train_player.py`` or similar as part of the submission/scoring process, so feel free to modify these scripts if they don't suit your application. We can offer limited one-on-one support (subject to the availability of the GNOMES support team) if you need help understanding how the environment is written and which variables are accessible for training.

Training
------------

Training using docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1) Build the training using ``docker-compose -f ./training/docker-compose.yml build``

2) Run the training using ``docker-compose -f ./training/docker-compose.yml up --abort-on-container-exit``

3) The trained network should appear in submission as ``my_agent.zip``. You *must* include this file with your submission. 

Training using non-docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1) Follow steps 1-4 from the `non-docker submission documentation <https://cugriffinlab.github.io/gnomes-submission/tutorial.html#self-evaluation-testing-for-non-docker-setups>`_.

2) Open two new terminal windows

* In each window, change the directory to the sandbox simulation folder using ``$ cd <your-username-gnomes>/training/simulation``

* In one terminal window, start the player submission using ``$ python train_player.py``

* In the other terminal window, run the simualtion using ``$ python run_aggregator.py``
    

Submitting and receiving official feedback
------------------------------------------------

The process for testing your agent is identical to the process you used for an RBC controller but you will have to modify ``submission.py`` to load the agent. We will walk you through that process below:

The predict function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
For each prediction we load the saved RL agent from Stable Baselines. The Stable Baselines agent contains a method ``predict`` that takes an argument of the vectorized observation list and returns the action. To provide this to the agent we use the normalization function previously defined in ``rl_training.py``. Remember to ensure that the ``predict()`` function is only returning a list of 3 floats that represent the desired action. For Stable Baselines this means calling the zero-indexed element of the ``predict()`` method. (In Stable Baselines predict returns the action + some extraneous data.)
   
Loading external files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Loading external files (such as a pre-trained agent) can be done by modifying the following line in ``<gnomes-your-username>/setup.py``:
   
``package_data={'': ['<your-file-name-here>']},``
   
Custom imports
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You may import any pip installable package to your submission function. Please note that we will not support manual dependecy conflict resolution so your submission package should therefore be pip installable. To include these functions in the pip install process we use for the scoring process modify ``<gnomes-your-username>/setup.py`` to include the custom package name under ``"install_requires"``.
