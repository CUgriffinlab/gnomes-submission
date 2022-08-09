import asyncio 
import sys
from dragg_comp.rl_aggregator import RLAggregator

if __name__=="__main__":
    if len(sys.argv)>1:
        a = RLAggregator(sys.argv[1], sys.argv[2])
    else:
        a = RLAggregator()
    asyncio.run(a.open_server())