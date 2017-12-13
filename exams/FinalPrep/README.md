### 1. Install dependency

```sh
virtualenv exam-prep-venv

source exam-prep-venv/bin/activate

pip install -r requirements.txt
```

> Want to read more about [gRPC lib](http://www.grpc.io/docs/tutorials/basic/python.html)?

### 2. Generate Python gRPC binding code from a service definition .proto file.

* Look at the service interface definition [db.proto](https://github.com/sithu/cmpe273-spring17/blob/master/exams/final/db.proto) file to understand the input and output parameters and payloads.

> DO NOT CHANGE db.proto FILE OR YOU WILL GET ZERO!

```sh
python -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. db.proto
```

