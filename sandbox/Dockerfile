# Install python
FROM python:3.9

# Install dragg
RUN pip install dragg

# Install dragg-comp
RUN pip install dragg-comp
RUN pip install cvxopt

# Copy parent directory
ADD . /dragg-comp-submission

# Install submission
RUN pip install /dragg-comp-submission/.

# Run simulation
WORKDIR  /dragg-comp-submission/sandbox/simulation
CMD python run_player.py & python run_aggregator.py
