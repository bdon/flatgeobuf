# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FlatGeobuf

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Feature(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Feature()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFeature(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Feature
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Feature
    def Geometry(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from FlatGeobuf.Geometry import Geometry
            obj = Geometry()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Feature
    def Properties(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Feature
    def PropertiesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Feature
    def PropertiesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Feature
    def PropertiesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # Feature
    def Columns(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from FlatGeobuf.Column import Column
            obj = Column()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Feature
    def ColumnsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Feature
    def ColumnsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def FeatureStart(builder): builder.StartObject(3)
def Start(builder):
    return FeatureStart(builder)
def FeatureAddGeometry(builder, geometry): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(geometry), 0)
def AddGeometry(builder, geometry):
    return FeatureAddGeometry(builder, geometry)
def FeatureAddProperties(builder, properties): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(properties), 0)
def AddProperties(builder, properties):
    return FeatureAddProperties(builder, properties)
def FeatureStartPropertiesVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def StartPropertiesVector(builder, numElems):
    return FeatureStartPropertiesVector(builder, numElems)
def FeatureAddColumns(builder, columns): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(columns), 0)
def AddColumns(builder, columns):
    return FeatureAddColumns(builder, columns)
def FeatureStartColumnsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def StartColumnsVector(builder, numElems):
    return FeatureStartColumnsVector(builder, numElems)
def FeatureEnd(builder): return builder.EndObject()
def End(builder):
    return FeatureEnd(builder)