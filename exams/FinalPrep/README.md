### 1. Install dependency

```sh
virtualenv exam-prep-venv

source exam-prep-venv/bin/activate

pip install -r requirements.txt
```

> Want to read more about [gRPC lib](http://www.grpc.io/docs/tutorials/basic/python.html)?

### 2. Generate Python gRPC binding code from a service definition .proto file.


> DO NOT CHANGE db.proto FILE OR YOU WILL GET ZERO!

```sh
python -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. token.proto
```

> PROBLEM 1 output for HRW.
```sh
SJSU coin is mapped to 0.0.0.0:3001
UCLA coin is mapped to 0.0.0.0:3000
SFSU coin is mapped to 0.0.0.0:3001
```


> TEST
```sh
python3 coin_server_mapping.py

python3 coin.py


python3 server.py 0.0.0.0:3000 UCLA
python3 server.py 0.0.0.0:3001 SFSU,SJSU

python3 client.py
```
