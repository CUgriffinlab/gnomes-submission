# dragg-comp-submission
This repository will track your official submission to the NSF Career Competition. You are to only change `submission/submission.py`. Also included in this repository are materials to allow you to test if your submission will successfully simulate as well as get an idea of how your submission performs on training data. 

# How to make changes to your submission
This competition will use Github to track submissions. You will only be judged based on the contents of `submission/submission.py`. We will *not* accept submissions via other means.

This tutorial assumes the use of a terminal or PowerShell with GitHub command line usage. [Here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) are installation instructions for git if you do not have it installed on your local machine.
1. Clone the repository using `$ git clone https://github.com/CUgriffinlab/dragg-comp-submission.git`
2. Change to the current working directory using `$ cd career-comp-submission`
3. Make changes to the file `submission/submission.py`
4. When you are done making changes save your file. 
5. Stage the changes using `$ git add submission/submission.py`
6. Commit your changes using ` git commit -m "Custom message about improvement"`
7. Update this repository by pushing your changes using `$ git push`

# How to test your submission
Before submission, it is a good idea to test if your submission will successfully simulate.

1. Clone the repository using `$ git clone https://github.com/CUgriffinlab/dragg-comp-submission.git`
2. Change to the current working directory using `$ cd career-comp-submission`
3. Install an editable version of your submission `$ pip install --editable .`
4. Change into testing directory `$ cd testing`
5. Run the tests `$ python test_submission.py`

These tests will also run automatically whenever pushes are made to this repository. 

# How to test your submission's performance in a sandbox simulation
Throughout this competition, you may want to check how your submission will perform on some sandbox data.

1. Clone the repository using `$ git clone https://github.com/CUgriffinlab/dragg-comp-submission.git`
2. Download and Run Docker Desktop. For more information on Docker visit [here](https://docs.docker.com/desktop/). To ensure 
that it is installed correctly go to your terminal or PowerShell and enter `$ docker --version`
3. Change to the current working directory using `$ cd dragg-comp-submission/sandbox`
4. Build the simulation using `$ docker-compose build`
5. Run the simulation using `$ docker-compose up --abort-on-container-exit`
