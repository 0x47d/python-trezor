# Automatically generated by pb2py
from trezorlib import protobuf as p
from .HDNodeType import HDNodeType

t = p.MessageType('HDNodePathType')
t.add_field(1, 'node', p.EmbeddedMessage(HDNodeType), flags=p.FLAG_REQUIRED)
t.add_field(2, 'address_n', p.UVarintType, flags=p.FLAG_REPEATED)
HDNodePathType = t