# Install python
FROM python:3.8

# Install dragg
RUN pip install dragg

# Install dragg-comp
RUN pip install dragg-comp
RUN pip install cvxopt

# Add local dragg-comp (TODO change dragg-comp to general toolset)
ADD dragg_comp /dragg_comp

# Run simulation
WORKDIR  /dragg_comp
CMD python player.py & python rl_aggregator.py
