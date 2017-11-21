'''
################################## master.py #############################
# Assignment 2 (master)
################################## master.py #############################
'''
import time
import grpc
import replicationService_pb2
import replicationService_pb2_grpc
import rocksdb
import queue

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class MasterReplicator(replicationService_pb2.ReplicationServiceServicer):
    # Constructor
    def __init__(self):
        self.transaction_queue = queue.Queue()
        self.db = rocksdb.DB("assignment2-master.db", rocksdb.Options(create_if_missing=True))

    # Sync operation
    def sync(self, request, context):
        print("Master to slave connection established.")
        # Continuous loop
        while True:
            transaction = self.transaction_queue.get()
            if transaction.action == 'delete':
                print("Deque transaction action={}, key={}, value={}) to slave".format(transaction.action,
                                                                                       transaction.key,
                                                                                       transaction.value))
            else:
                print("Deque transaction action={}, key={}) to slave".format(transaction.action,
                                                                                       transaction.key,
                                                                                       transaction.value))
            yield transaction

    # Define a decorator named replicate_to_slave
    def replicate_to_slave(method):
        def wrapper_function(self, request, context):
            transaction = replicationService_pb2.ReplicationResponse(
                action=method.__name__,
                key=request.key.encode(),
                value=request.value.encode()
            )
            self.transaction_queue.put(transaction)
            # delegate the call to passed in method
            return method(self, request, context)
        return wrapper_function

    def get(self, request, context):
        print("Get key = {} from master-db".format(request.key))
        data = self.db.get(request.key.encode())
        # return value
        return replicationService_pb2.Response(value=data)

    # This will wrap the put method and call the same for slave.
    @replicate_to_slave
    def put(self, request, context):
        print("Put key = {} value = {} to master-db".format(request.key, request.value))
        self.db.put(request.key.encode(), request.value.encode())
        # return 0 for success
        return replicationService_pb2.Response(value='0')

    # This will wrap the put method and call the same for slave.
    @replicate_to_slave
    def delete(self, request, context):
        print("Delete key = {} from master-db".format(request.key))
        self.db.delete(request.key.encode())
        # return 0 for success
        return replicationService_pb2.Response(value='0')


# Code to run a process listening at port 5000
def run(host, port):
    '''
    Run the GRPC master
    '''
    # Can increase worker.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    replicationService_pb2_grpc.add_ReplicationServiceServicer_to_server(MasterReplicator(), server)
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