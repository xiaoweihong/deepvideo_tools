# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: genericobj.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import protobuf_test.common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='genericobj.proto',
  package='dg.model',
  syntax='proto3',
  serialized_pb=_b('\n\x10genericobj.proto\x12\x08\x64g.model\x1a\x0c\x63ommon.proto\"\x93\x01\n\x12NonMotorVehicleObj\x12\'\n\x08Metadata\x18\x01 \x01(\x0b\x32\x15.dg.model.SrcMetadata\x12\x1c\n\x03Img\x18\x02 \x01(\x0b\x32\x0f.dg.model.Image\x12\x36\n\x10NonMotorVehicles\x18\x03 \x03(\x0b\x32\x1c.dg.model.RecNonMotorVehicle*i\n\x16NonMotorVehicleGesture\x12\x15\n\x11\x41TTITUDE_POSITIVE\x10\x00\x12\x12\n\x0e\x41TTITUDE_RIGHT\x10\x01\x12\x11\n\rATTITUDE_LEFT\x10\x02\x12\x11\n\rATTITUDE_BACK\x10\x03*\xec\x01\n\x13NonMotorVehicleType\x12\x19\n\x15NONMOTOR_TYPE_UNKNOWN\x10\x00\x12\x19\n\x15NONMOTOR_TYPE_VEHICLE\x10\x01\x12\x1c\n\x18NONMOTOR_TYPE_PEDESTRIAN\x10\x02\x12\x1a\n\x16NONMOTOR_TYPE_VEHICLE2\x10\x03\x12\x1a\n\x16NONMOTOR_TYPE_VEHICLE3\x10\x04\x12\x16\n\x12NONMOTOR_TYPE_ROOF\x10\x05\x12\x16\n\x12NONMOTOR_TYPE_SEAL\x10\x06\x12\x19\n\x15NONMOTOR_TYPE_BICYCLE\x10\x07\x62\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])

_NONMOTORVEHICLEGESTURE = _descriptor.EnumDescriptor(
  name='NonMotorVehicleGesture',
  full_name='dg.model.NonMotorVehicleGesture',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ATTITUDE_POSITIVE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATTITUDE_RIGHT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATTITUDE_LEFT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATTITUDE_BACK', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=194,
  serialized_end=299,
)
_sym_db.RegisterEnumDescriptor(_NONMOTORVEHICLEGESTURE)

NonMotorVehicleGesture = enum_type_wrapper.EnumTypeWrapper(_NONMOTORVEHICLEGESTURE)
_NONMOTORVEHICLETYPE = _descriptor.EnumDescriptor(
  name='NonMotorVehicleType',
  full_name='dg.model.NonMotorVehicleType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONMOTOR_TYPE_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONMOTOR_TYPE_VEHICLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONMOTOR_TYPE_PEDESTRIAN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONMOTOR_TYPE_VEHICLE2', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONMOTOR_TYPE_VEHICLE3', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONMOTOR_TYPE_ROOF', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONMOTOR_TYPE_SEAL', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONMOTOR_TYPE_BICYCLE', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=302,
  serialized_end=538,
)
_sym_db.RegisterEnumDescriptor(_NONMOTORVEHICLETYPE)

NonMotorVehicleType = enum_type_wrapper.EnumTypeWrapper(_NONMOTORVEHICLETYPE)
ATTITUDE_POSITIVE = 0
ATTITUDE_RIGHT = 1
ATTITUDE_LEFT = 2
ATTITUDE_BACK = 3
NONMOTOR_TYPE_UNKNOWN = 0
NONMOTOR_TYPE_VEHICLE = 1
NONMOTOR_TYPE_PEDESTRIAN = 2
NONMOTOR_TYPE_VEHICLE2 = 3
NONMOTOR_TYPE_VEHICLE3 = 4
NONMOTOR_TYPE_ROOF = 5
NONMOTOR_TYPE_SEAL = 6
NONMOTOR_TYPE_BICYCLE = 7



_NONMOTORVEHICLEOBJ = _descriptor.Descriptor(
  name='NonMotorVehicleObj',
  full_name='dg.model.NonMotorVehicleObj',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Metadata', full_name='dg.model.NonMotorVehicleObj.Metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Img', full_name='dg.model.NonMotorVehicleObj.Img', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='NonMotorVehicles', full_name='dg.model.NonMotorVehicleObj.NonMotorVehicles', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=45,
  serialized_end=192,
)

_NONMOTORVEHICLEOBJ.fields_by_name['Metadata'].message_type = common__pb2._SRCMETADATA
_NONMOTORVEHICLEOBJ.fields_by_name['Img'].message_type = common__pb2._IMAGE
_NONMOTORVEHICLEOBJ.fields_by_name['NonMotorVehicles'].message_type = common__pb2._RECNONMOTORVEHICLE
DESCRIPTOR.message_types_by_name['NonMotorVehicleObj'] = _NONMOTORVEHICLEOBJ
DESCRIPTOR.enum_types_by_name['NonMotorVehicleGesture'] = _NONMOTORVEHICLEGESTURE
DESCRIPTOR.enum_types_by_name['NonMotorVehicleType'] = _NONMOTORVEHICLETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NonMotorVehicleObj = _reflection.GeneratedProtocolMessageType('NonMotorVehicleObj', (_message.Message,), dict(
  DESCRIPTOR = _NONMOTORVEHICLEOBJ,
  __module__ = 'genericobj_pb2'
  # @@protoc_insertion_point(class_scope:dg.model.NonMotorVehicleObj)
  ))
_sym_db.RegisterMessage(NonMotorVehicleObj)


# @@protoc_insertion_point(module_scope)