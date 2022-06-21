# Install python
FROM python:3

# Install dragg
RUN pip install dragg

# Install dragg-comp
RUN pip install dragg-comp

# Add local dragg-comp (TODO change dragg-comp to general toolset)
ADD dragg_comp /dragg_comp

# # Run simulation
# RUN cd dragg_comp
# RUN python player.py &
# RUN python rl_aggregator.py &
