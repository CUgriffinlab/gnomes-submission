# Install python
FROM python:3

# Install dragg
RUN pip install dragg

# Install dragg-comp
RUN pip install dragg-comp
RUN pip install cvxopt

# Add local dragg-comp (TODO change dragg-comp to general toolset)
ADD dragg_comp /dragg_comp

# Run simulation
EXPOSE 6379
WORKDIR  /dragg_comp
CMD python rl_aggregator.py
#CMD python player.py & python rl_aggregator.py
