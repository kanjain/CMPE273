"""
You must use hashlib to hash the node ('0.0.0.0:3000') and key ('mykey') combination.
Example:
x = '0.0.0.0:3000' + 'my-key'
x = node + key
hash = hashlib.md5(x).hexdigest()

More@https://docs.python.org/2/library/hashlib.html
"""
# TODO: Add any required import
import hashlib
from client import DBClient


class ConsistentHash(object):

    def __init__(self, nodes=None):
        """
        Initialize an instance with a node list and others.
        A node means a server host name and its listening port. E.g. '0.0.0.0:3000'
        :param nodes: a list of DB server nodes to register.
        """
        nodes = nodes or {}
        self._nodes = set(nodes)

        hash_tuples = [(node, self.my_hash(str(node))) for node in range(self.nodes)]

        # Sort the hash tuples based on just the hash values
        hash_tuples.sort(lambda x, y: cmp(x[1], y[1]))
        self.hash_tuples = hash_tuples

    def my_hash(key):
        key = key.encode()
        return (int(hashlib.md5(key).hexdigest(), 16) % 1000000) / 1000000.0

    def get_node(self, key):
        """
        Find the hash value and the next higher node with hash value.
        value among all nodes.
        :param key: a string key name.
        :return the highest node.
        """
        h = self.my_hash(key)
        # edge case where we cycle past hash value of 1 and back to 0.
        # in this case the last tuple has the highest hash value.
        # if your h has a value higher than the last value, then just return the first.
        if h > self.hash_tuples[-1]:
            return self.hash_tuples[0]

        for i in enumerate(self.hash_tuples):
            if h > self.hash_tuples[i][1]:
                return self.hash_tuples[i]


        # just return the first one
        return self.hash_tuples[0]


class ConsistentHashDBClient(ConsistentHash):
    """
    This class extends from the above RendezvousHash class and
    integrates DBClient (see@client.py) with RendezvousHash so that
    client can PUT and GET to the DB servers while the rendezvous hash shards
    the data across multiple DB servers.
    DO NOT USE ANY STATIC CLASS VARIABLES!
    """

    def __init__(self, db_servers=None):
        """
        1. Initialize the super/parent RendezvousHash class.
        Class inheritance@http://www.python-course.eu/python3_inheritance.php
        2. Create DBClient instance for all servers and save them in a dictionary.
        :param db_servers: a list of DB servers: ['0.0.0.0:3000', '0.0.0.0:3001', '0.0.0.0:3002']
        """
        self.db_servers = db_servers
        self.db_clients = {}
        self.ring = ConsistentHash(nodes=self.db_servers)

        for server in self.db_servers:
            [host, port] = server.split(":")
            self.db_clients[server] = DBClient(host=host, port=int(port))

    def put(self, key, value):
        """
        1. Get the highest Rendezvous node for the given key.
        2. Retrieve the DBClient instance reference by the node.
        3. Save the value into DB via client's put().
        :param key: a string key.
        :param value: a string key-value pair dictionary to be stored in DB.
        :return a PutResponse - see@db.proto
        NOTE: Both key and value must be the string type.
        """
        node = self.ring.get_node(key)
        client = self.db_clients[node]

        return client.put(key, value)

    def get(self, key):
        """
        1. Get the highest Rendezvous node for the given key.
        2. Retrieve the DBClient instance reference by the node.
        3. Get the value by the key via client's get().
        :param key: a string key.
        :param value: a string key-value pair dictionary to be stored in DB.
        :return a GetResposne - see@db.proto
        """
        node = self.ring.get_node(key)
        client = self.db_clients[node]

        return client.get(key)

    def info(self):
        """
        Return a list of InfoResponse from all servers.
        1. Invoke DB client's info() to retrieve server info for all servers.
        """
        server_info = []
        for node in self.db_servers:
            client = self.db_clients[node]
            server_info.append(client.info())

        return server_info

