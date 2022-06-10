# career-comp-submission
This repository will track your official submission to the NSF Career Competition. You are to only change `submission/submission.py`. Also included in this repository are materials to allow you to test if your submission will succesfully simulate as well as get an idea for how your submission will do on training data. 

# How to test your submission
1. Clone the repository using `$ git clone https://github.com/kravitsjacob/career-comp-submission.git`
2. Change to the current working directory using `$ cd career-comp-submission`
3. Install an editable version of paxplot `$ pip install --editable .`
4. Change into testing directory `$ cd testing`
5. Run the tests `$ python test_submission.py`

These test will also run automatically whenever pushes are made to this repository. 

# How test your submission's performance on training simulation
This tutorial assumes the use of gitbash or a Unix-like terminal with github command line usage
1. Clone the repository using `$ git clone https://github.com/kravitsjacob/dragg-comp-submission.git`
2. Download and Run Docker Desktop. For more information on Docker visit: https://docs.docker.com/desktop/. To ensure 
that it is installed correctly go to your Unix-like terminal and enter `$ docker --version`
3. Change to the current working directory using command prompt/terminal `$ cd dragg-comp-submission/training_simulation`
4. Run the simulation using `$ bash simulation.sh`
