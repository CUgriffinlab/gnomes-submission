# Pull redis docker
docker pull redis

# Build simulation docker
docker build --tag simulation .

# Start redis
docker run --name dragg-redis -d redis

# Run simulation docker
# docker run --name simulation --link dragg-redis:redis -d simulation
# docker run --name simulation --link dragg-redis:simulation --rm redis redis-cli -h redis -p 6379
# docker run -it --name simulation --link dragg-redis:simulation simulation redis redis-cli -h redis -p 6379
# docker run -t --name simulation --link dragg-redis:simulation -h redis simulation