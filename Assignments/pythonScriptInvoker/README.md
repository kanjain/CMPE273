### How to build a Docker Image with RocksDB and flask?

```sh
docker build -t pyhton-rocksdb-flask:latest .
```

### How to run app.py?

```sh
docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp pyhton-rocksdb-flask:latest python3.6 app.py
```
