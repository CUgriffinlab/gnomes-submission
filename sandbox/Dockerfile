# Install python
FROM python:3.9

# Install dragg
RUN pip install dragg

# Install dragg-comp
RUN pip install dragg-comp
RUN pip install cvxopt

# Install submission
# RUN cd ../..
ADD . /dragg-comp-submission
RUN pip install /dragg-comp-submission/.

# Add simulation files
# ADD simulation sandbox/simulation

# Run simulation
WORKDIR  /dragg-comp-submission/sandbox/simulation
CMD python run_player.py & python run_aggregator.py
