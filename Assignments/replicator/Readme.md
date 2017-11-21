#This is a python replicator

# Generate the proto file locally
python3.6 -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. replicationService.proto

#Run server
python3.6 master.py

#Run slave
python3.6 slave.py