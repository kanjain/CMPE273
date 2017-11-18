#This is a python replicator
my-grpc-python-replication-service

docker build -t my-grpc-python-replication-service:1.0 .
docker run -it --rm --name master-slave-running-app -v "$PWD":/usr/src/myapp -w /usr/src/myapp my-grpc-python-replication-service:1.0 python3.6 -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. replicationService.proto


docker run -it --rm --name master-slave-running-app -v "$PWD":/usr/src/myapp -w /usr/src/myapp my-grpc-python-replication-service:1.0 python3.6 master.py
docker run -it --rm --name master-slave-running-app -v "$PWD":/usr/src/myapp -w /usr/src/myapp my-grpc-python-replication-service:1.0 python3.6 slave.py
docker run -it --rm --name master-slave-running-app -v "$PWD":/usr/src/myapp -w /usr/src/myapp my-grpc-python-replication-service:1.0 python3.6 test_client.py


Additional notes for docker management
One liner to stop / remove all of Docker containers:
docker rm $(docker ps -a -q)
One liner to stop / remove all of Docker images:
docker rmi $(docker images -q)