# Automatically generated by pb2py
from trezorlib import protobuf as p

t = p.MessageType('EthereumTxAck')
t.wire_type = 60
t.add_field(1, 'data_chunk', p.BytesType)
EthereumTxAck = t