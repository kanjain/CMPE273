# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import replicationService_pb2 as replicationService__pb2


class ReplicationServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.sync = channel.unary_stream(
        '/ReplicationService/sync',
        request_serializer=replicationService__pb2.ReplicationRequest.SerializeToString,
        response_deserializer=replicationService__pb2.ReplicationResponse.FromString,
        )
    self.delete = channel.unary_unary(
        '/ReplicationService/delete',
        request_serializer=replicationService__pb2.Request.SerializeToString,
        response_deserializer=replicationService__pb2.Response.FromString,
        )
    self.put = channel.unary_unary(
        '/ReplicationService/put',
        request_serializer=replicationService__pb2.Request.SerializeToString,
        response_deserializer=replicationService__pb2.Response.FromString,
        )
    self.get = channel.unary_unary(
        '/ReplicationService/get',
        request_serializer=replicationService__pb2.Request.SerializeToString,
        response_deserializer=replicationService__pb2.Response.FromString,
        )


class ReplicationServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def sync(self, request, context):
    """Master-Slave Sync operation 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def delete(self, request, context):
    """Operations on the db 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def put(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def get(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ReplicationServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'sync': grpc.unary_stream_rpc_method_handler(
          servicer.sync,
          request_deserializer=replicationService__pb2.ReplicationRequest.FromString,
          response_serializer=replicationService__pb2.ReplicationResponse.SerializeToString,
      ),
      'delete': grpc.unary_unary_rpc_method_handler(
          servicer.delete,
          request_deserializer=replicationService__pb2.Request.FromString,
          response_serializer=replicationService__pb2.Response.SerializeToString,
      ),
      'put': grpc.unary_unary_rpc_method_handler(
          servicer.put,
          request_deserializer=replicationService__pb2.Request.FromString,
          response_serializer=replicationService__pb2.Response.SerializeToString,
      ),
      'get': grpc.unary_unary_rpc_method_handler(
          servicer.get,
          request_deserializer=replicationService__pb2.Request.FromString,
          response_serializer=replicationService__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ReplicationService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
