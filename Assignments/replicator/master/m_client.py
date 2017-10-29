'''
################################## server.py #############################
# Assignment 2 (server)
# RocksDB provides two convenient APIs, GetLatestSequenceNumber() and GetUpdatesSince().
# For push-based models, the master tracks the latest sequence numbers for all slaves and proactively sends data to them whenever it has newer updates.
################################## server.py #############################
'''
import time
import grpc
import datastore_pb2
import datastore_pb2_grpc
import uuid
import rocksdb

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class MyDatastoreServicer(datastore_pb2.DatastoreServicer):
    def __init__(self):
        self.db = rocksdb.DB("lab1.db", rocksdb.Options(create_if_missing=True))

    def put(self, request, context):
        print("put")
        key = uuid.uuid4().hex
        var = key.encode('utf-8')
        temp = request.data
        var1 = temp.encode('utf-8')
        self.db.put(var, var1)
        # TODO - save key and value into DB converting request.data string to utf-8 bytes 

        return datastore_pb2.Response(data=key)

    def get(self, request, context):
        print("get")
        # TODO - retrieve the value from DB by the given key. Needs to convert request.data string to utf-8 bytes. 
        value = None
        key = request.data
        var2 = key.encode('utf-8')
        value = (self.db.get(var2)).decode('utf-8')
        return datastore_pb2.Response(data=value)



# Code to run a process listening at port 5000
def run(host, port):
    '''
    Run the GRPC server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    datastore_pb2_grpc.add_DatastoreServicer_to_server(MyDatastoreServicer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()

    try:
        while True:
            print("Server started at...%d" % port)
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run('0.0.0.0', 5000)