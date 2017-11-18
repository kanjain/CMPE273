'''
################################## slave.py #############################
# Assignment 2 (slave)
################################## slave.py #############################
'''
import grpc
import replicationService_pb2
import rocksdb

class SlaveReplicator():
    def __init__(self, host, port):
        self.db = rocksdb.DB("assignment2-slave.db", rocksdb.Options(create_if_missing=True))
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = replicationService_pb2.ReplicationServiceStub(self.channel)

    def sync(self):
        syncQueue = self.stub.sync(replicationService_pb2.ReplicationRequest())
        print("Connection established from slave to master")
        for transaction in syncQueue:
            if transaction.action == 'put':
                print("Put key = {}, value = {} to slave-db".format(transaction.key, transaction.value))
                self.db.put(transaction.key.encode(), transaction.value.encode())
            elif transaction.action == 'delete':
                print("Delete key = {} from slave-db".format(transaction.key))
                self.db.delete(transaction.key.encode())
            else: #(get operation not supported).
                pass

def run(host, port):
    '''
    Run the GRPC slave
    '''
    slave = SlaveReplicator(host, port)
    slave.sync()


if __name__ == '__main__':
    run('0.0.0.0', 5000)