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

```sh
SJSU coin is mapped to 0.0.0.0:3001
UCLA coin is mapped to 0.0.0.0:3000
SFSU coin is mapped to 0.0.0.0:3001
```
