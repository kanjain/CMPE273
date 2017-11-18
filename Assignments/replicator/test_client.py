'''
################################## test_client.py #############################
# Assignment 2 (test_client)
################################## test_client.py #############################
'''

import grpc
import replicationService_pb2

class ReplicationServiceTest():
    def __init__(self, host, port):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = replicationService_pb2.ReplicationServiceStub(self.channel)

    def put(self, key, data):
        return self.stub.put(replicationService_pb2.Request(key=key, value=data))

    def delete(self, key):
        return self.stub.delete(replicationService_pb2.Request(key=key))

# Code to run a process listening at port 5000
def run(host, port):
    '''
    Run the GRPC server
    '''
    test = ReplicationServiceTest(host, port)

    print('key = k1, value = v1')
    response = test.put('k1', 'v1')
    print(response.value == '0' if 'HTTP 200 OK' else "Failed")
    print('key = k2, value = v2')
    response = test.put('k2', 'v2')
    print(response.value == '0' if 'HTTP 200 OK' else "Failed")
    print('delete key = v1')
    response = test.delete('v1')
    print(response.value == '0' if 'HTTP 200 OK' else "Failed")

if __name__ == '__main__':
    run('0.0.0.0', 5000)