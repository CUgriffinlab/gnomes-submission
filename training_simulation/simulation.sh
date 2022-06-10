# Pull redis docker
docker pull redis

# Start redis docker
docker run --name redis-docker -d redis

# Build simulation docker
docker build --tag simulation .

# Run simulation docker
docker run simulation