# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: token.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='token.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0btoken.proto\"U\n\x04\x44\x61ta\x12\x1f\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x10.Data.EntryEntry\x1a,\n\nEntryEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"W\n\x0fTransferRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x12\n\nfromWallet\x18\x02 \x01(\t\x12\x10\n\x08toWallet\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x05\"\"\n\x10TransferResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"\x07\n\x05\x45mpty\"#\n\x0cInfoResponse\x12\x13\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x05.Data2[\n\x05Token\x12\x31\n\x08transfer\x12\x10.TransferRequest\x1a\x11.TransferResponse\"\x00\x12\x1f\n\x04info\x12\x06.Empty\x1a\r.InfoResponse\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DATA_ENTRYENTRY = _descriptor.Descriptor(
  name='EntryEntry',
  full_name='Data.EntryEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Data.EntryEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Data.EntryEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=100,
)

_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='Data.entry', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DATA_ENTRYENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=100,
)


_TRANSFERREQUEST = _descriptor.Descriptor(
  name='TransferRequest',
  full_name='TransferRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='TransferRequest.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fromWallet', full_name='TransferRequest.fromWallet', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='toWallet', full_name='TransferRequest.toWallet', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='TransferRequest.amount', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=189,
)


_TRANSFERRESPONSE = _descriptor.Descriptor(
  name='TransferResponse',
  full_name='TransferResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='TransferResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=191,
  serialized_end=225,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=234,
)


_INFORESPONSE = _descriptor.Descriptor(
  name='InfoResponse',
  full_name='InfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='InfoResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=271,
)

_DATA_ENTRYENTRY.containing_type = _DATA
_DATA.fields_by_name['entry'].message_type = _DATA_ENTRYENTRY
_INFORESPONSE.fields_by_name['data'].message_type = _DATA
DESCRIPTOR.message_types_by_name['Data'] = _DATA
DESCRIPTOR.message_types_by_name['TransferRequest'] = _TRANSFERREQUEST
DESCRIPTOR.message_types_by_name['TransferResponse'] = _TRANSFERRESPONSE
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['InfoResponse'] = _INFORESPONSE

Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(

  EntryEntry = _reflection.GeneratedProtocolMessageType('EntryEntry', (_message.Message,), dict(
    DESCRIPTOR = _DATA_ENTRYENTRY,
    __module__ = 'token_pb2'
    # @@protoc_insertion_point(class_scope:Data.EntryEntry)
    ))
  ,
  DESCRIPTOR = _DATA,
  __module__ = 'token_pb2'
  # @@protoc_insertion_point(class_scope:Data)
  ))
_sym_db.RegisterMessage(Data)
_sym_db.RegisterMessage(Data.EntryEntry)

TransferRequest = _reflection.GeneratedProtocolMessageType('TransferRequest', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERREQUEST,
  __module__ = 'token_pb2'
  # @@protoc_insertion_point(class_scope:TransferRequest)
  ))
_sym_db.RegisterMessage(TransferRequest)

TransferResponse = _reflection.GeneratedProtocolMessageType('TransferResponse', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERRESPONSE,
  __module__ = 'token_pb2'
  # @@protoc_insertion_point(class_scope:TransferResponse)
  ))
_sym_db.RegisterMessage(TransferResponse)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'token_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  ))
_sym_db.RegisterMessage(Empty)

InfoResponse = _reflection.GeneratedProtocolMessageType('InfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _INFORESPONSE,
  __module__ = 'token_pb2'
  # @@protoc_insertion_point(class_scope:InfoResponse)
  ))
_sym_db.RegisterMessage(InfoResponse)


_DATA_ENTRYENTRY.has_options = True
_DATA_ENTRYENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class TokenStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.transfer = channel.unary_unary(
          '/Token/transfer',
          request_serializer=TransferRequest.SerializeToString,
          response_deserializer=TransferResponse.FromString,
          )
      self.info = channel.unary_unary(
          '/Token/info',
          request_serializer=Empty.SerializeToString,
          response_deserializer=InfoResponse.FromString,
          )


  class TokenServicer(object):

    def transfer(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def info(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_TokenServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'transfer': grpc.unary_unary_rpc_method_handler(
            servicer.transfer,
            request_deserializer=TransferRequest.FromString,
            response_serializer=TransferResponse.SerializeToString,
        ),
        'info': grpc.unary_unary_rpc_method_handler(
            servicer.info,
            request_deserializer=Empty.FromString,
            response_serializer=InfoResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Token', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaTokenServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def transfer(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def info(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaTokenStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def transfer(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    transfer.future = None
    def info(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    info.future = None


  def beta_create_Token_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('Token', 'info'): Empty.FromString,
      ('Token', 'transfer'): TransferRequest.FromString,
    }
    response_serializers = {
      ('Token', 'info'): InfoResponse.SerializeToString,
      ('Token', 'transfer'): TransferResponse.SerializeToString,
    }
    method_implementations = {
      ('Token', 'info'): face_utilities.unary_unary_inline(servicer.info),
      ('Token', 'transfer'): face_utilities.unary_unary_inline(servicer.transfer),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Token_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('Token', 'info'): Empty.SerializeToString,
      ('Token', 'transfer'): TransferRequest.SerializeToString,
    }
    response_deserializers = {
      ('Token', 'info'): InfoResponse.FromString,
      ('Token', 'transfer'): TransferResponse.FromString,
    }
    cardinalities = {
      'info': cardinality.Cardinality.UNARY_UNARY,
      'transfer': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Token', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
