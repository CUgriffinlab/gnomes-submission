# Install python
FROM python:3.9

# Copy parent directory
ADD . /dragg-comp-submission

# Install submission
RUN pip install /dragg-comp-submission/.

# Run simulation
WORKDIR  /dragg-comp-submission/sandbox/simulation
CMD python run_aggregator.py -r "redis://redis" & python run_player.py -r "redis://redis" 
