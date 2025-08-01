#From Enums_Internal

class ArrayData:
    """Array container that stores values and element type"""
    def __init__(self, values=None, element_class=None, orig_type=""):
        self.values = values if values is not None else []
        self.element_class = element_class
        self.orig_type = orig_type
        
    def add_element(self, element):
        if self.element_class and not isinstance(element, self.element_class):
            raise TypeError(f"Expected {self.element_class.__name__}, got {type(element).__name__}")
        
        self.values.append(element)
        return len(self.values) - 1

class StructData:
    """Container for struct type that can hold 0 or more embedded structures"""
    def __init__(self, values=None, orig_type: str = ""):
        self.values = values if values is not None else []
        self.orig_type = orig_type
    
    def add_element(self, element):
        """Add an element to the struct if it matches the expected type"""
        if not isinstance(element, dict):
            raise TypeError(f"Expected dict for struct element, got {type(element).__name__}")
        self.values.append(element)
        return len(self.values) - 1

class ObjectData:
    def __init__(self, value: int = 0, orig_type: str = ""):
        self.value = value
        self.orig_type = orig_type

class ResourceData:
    def __init__(self, value: str = "", orig_type: str = ""):
        self.value = value
        self.orig_type = orig_type

class UserDataData:
    def __init__(self, value: int = 0, string: str = "", orig_type: str = ""):
        self.value = value
        self.string = string
        self.orig_type = orig_type

class BoolData:
    def __init__(self, value: bool = False, orig_type: str = ""):
        self.value = value
        self.orig_type = orig_type

class S8Data:
    def __init__(self, value: int = 0, orig_type: str = ""):
        self.value = value
        self.orig_type = orig_type

class U8Data:
    def __init__(self, value: int = 0, orig_type: str = ""):
        self.value = value
        self.orig_type = orig_type

class S16Data:
    def __init__(self, value: int = 0, orig_type: str = ""):
        self.value = value
        self.orig_type = orig_type

class U16Data:
    def __init__(self, value: int = 0, orig_type: str = ""):
        self.value = value
        self.orig_type = orig_type

class S32Data:
    def __init__(self, value: int = 0, orig_type: str = ""):
        self.value = value
        self.orig_type = orig_type

class U32Data:
    def __init__(self, value: int = 0, orig_type: str = ""):
        self.value = value
        self.orig_type = orig_type

class S64Data:
    def __init__(self, value: int = 0, orig_type: str = ""):
        self.value = value
        self.orig_type = orig_type

class U64Data:
    def __init__(self, value: int = 0, orig_type: str = ""):
        self.value = value
        self.orig_type = orig_type

class F32Data:
    def __init__(self, value: float = 0, orig_type: str = ""):
        self.value = value
        self.orig_type = orig_type

class F64Data:
    def __init__(self, value: float = 0, orig_type: str = ""):
        self.value = value
        self.orig_type = orig_type

class StringData:
    def __init__(self, value: str = "", orig_type: str = ""):
        self.value = value
        self.orig_type = orig_type

class Uint2Data:
    def __init__(self, x: int = 0, y: int = 0, orig_type: str = ""):
        self.x = x
        self.y = y
        self.orig_type = orig_type

class Uint3Data:
    def __init__(self, x: int = 0, y: int = 0, z: int = 0, orig_type: str = ""):
        self.x = x
        self.y = y 
        self.z = z
        self.orig_type = orig_type

class Int2Data:
    def __init__(self, x: int = 0, y: int = 0, orig_type: str = ""):
        self.x = x
        self.y = y
        self.orig_type = orig_type

class Int3Data:
    def __init__(self, x: int = 0, y: int = 0, z: int = 0, orig_type: str = ""):
        self.x = x
        self.y = y
        self.z = z
        self.orig_type = orig_type

class Int4Data:
    def __init__(self, x: int = 0, y: int = 0, z: int = 0, w: int = 0, orig_type: str = ""):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.orig_type = orig_type

class Float2Data:
    def __init__(self, x: float = 0, y: float = 0, orig_type: str = ""):
        self.x = x
        self.y = y
        self.orig_type = orig_type

class Float3Data:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, orig_type: str = ""):
        self.x = x
        self.y = y
        self.z = z
        self.orig_type = orig_type

class Float4Data:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, w: float = 0, orig_type: str = ""):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.orig_type = orig_type

class Mat4Data:
    def __init__(self, values = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0), orig_type: str = ""):
        self.values = []
        if isinstance(values, (tuple, list)):
            self.values.extend(float(v) for v in values[:16])
        while len(self.values) < 16:
            self.values.append(0.0)
        self.orig_type = orig_type

    def __iter__(self):
        return iter(self.values)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, idx):
        return self.values[idx]

    def __str__(self):
        return f"MAT4({', '.join(f'{v:.6f}' for v in self.values)})"

class Vec2Data:
    def __init__(self, x: float = 0, y: float = 0, orig_type: str = ""):
        self.x = x
        self.y = y
        self.orig_type = orig_type

class Vec3Data:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, orig_type: str = ""):
        self.x = x
        self.y = y
        self.z = z
        self.orig_type = orig_type

class Vec3ColorData:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, orig_type: str = ""):
        self.x = x
        self.y = y
        self.z = z
        self.orig_type = orig_type

class Vec4Data:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, w: float = 0, orig_type: str = ""):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.orig_type = orig_type

class QuaternionData:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, w: float = 0, orig_type: str = ""):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.orig_type = orig_type

class GuidData:
    def __init__(self, guid_str: str = None, raw_bytes: bytes = None, orig_type: str = ""):
        if not guid_str:
            guid_str = "00000000-0000-0000-0000-000000000000"
        if not raw_bytes:
            raw_bytes = b'\0' * 16
            
        self.guid_str = guid_str
        self.raw_bytes = raw_bytes  # Store original bytes
        self.orig_type = orig_type

class ColorData:
    def __init__(self, r: int = 0, g: int = 0, b: int = 0, a: int = 0, orig_type: str = ""):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.orig_type = orig_type

class AABBData:
    def __init__(self, min_x: float = 0, min_y: float = 0, min_z: float = 0, 
                 max_x: float = 0, max_y: float = 0, max_z: float = 0, orig_type: str = ""):
        self.min = Vec3Data(min_x, min_y, min_z)
        self.max = Vec3Data(max_x, max_y, max_z)
        self.orig_type = orig_type

class CapsuleData:
    def __init__(self, start: Vec3Data = Vec3Data(0,0,0, ""), end: Vec3Data = Vec3Data(0,0,0, ""), radius: float = 0, orig_type: str = ""):
        self.start = start
        self.end = end
        self.radius = radius
        self.orig_type = orig_type
        
class AreaData:
    def __init__(self, p0: Float2Data = Float2Data(0,0, ""), p1: Float2Data = Float2Data(0,0, ""), p2: Float2Data = Float2Data(0,0, ""), p3: Float2Data = Float2Data(0,0, ""), height: float = 0, bottom: float = 0, orig_type: str = ""):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.height = height
        self.bottom = bottom
        self.orig_type = orig_type

class ConeData:
    def __init__(self, position: Vec3Data = Vec3Data(0,0,0, ""), direction: Vec3Data = Vec3Data(0,0,0, ""), angle: float = 0, distance: float = 0, orig_type: str = ""):
        self.position = position
        self.direction = direction
        self.angle = angle
        self.distance = distance
        self.orig_type = orig_type

class LineSegmentData:
    def __init__(self, start: Vec3Data = Vec3Data(0,0,0, ""), end: Vec3Data = Vec3Data(0,0,0, ""), orig_type: str = ""):
        self.start = start
        self.end = end
        self.orig_type = orig_type

class OBBData:
    def __init__(self, values = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0), orig_type: str = ""):
        # OBB data is always 20 floats
        self.values = []
        if isinstance(values, (tuple, list)):
            self.values.extend(float(v) for v in values[:20])
        while len(self.values) < 20:
            self.values.append(0.0)
        self.orig_type = orig_type

    def __iter__(self):
        return iter(self.values)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, idx):
        return self.values[idx]

    def __str__(self):
        return f"OBB({', '.join(f'{v:.6f}' for v in self.values)})"

class PointData:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, orig_type: str = ""):
        self.x = x
        self.y = y
        self.z = z
        self.orig_type = orig_type

class PositionData:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, orig_type: str = ""):
        self.x = x
        self.y = y
        self.z = z
        self.orig_type = orig_type

class RangeData:
    def __init__(self, min: float = 0, max: float = 0, orig_type: str = ""):
        self.min = min
        self.max = max
        self.orig_type = orig_type

class RangeIData:
    def __init__(self, min: int = 0, max: int = 0, orig_type: str = ""):
        self.min = min
        self.max = max
        self.orig_type = orig_type

class SizeData:
    def __init__(self, width: float = 0, height: float = 0, orig_type: str = ""):
        self.width = width
        self.height = height
        self.orig_type = orig_type

class SphereData:
    def __init__(self, center: Vec3Data = Vec3Data(0,0,0, ""), radius: float = 0, orig_type: str = ""):
        self.center = center
        self.radius = radius
        self.orig_type = orig_type

class CylinderData:
    def __init__(self, center: Vec3Data = Vec3Data(0,0,0, ""), radius: float = 0, height: float = 0, orig_type: str = ""):
        self.center = center
        self.radius = radius
        self.height = height
        self.orig_type = orig_type

class RectData:
    def __init__(self, min_x: float = 0, min_y: float = 0, max_x: float = 0, max_y: float = 0, orig_type: str = ""):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        self.orig_type = orig_type

class GameObjectRefData:
    def __init__(self, guid_str: str = "", raw_bytes: bytes = None, orig_type: str = ""):
        if not guid_str:
            guid_str = "00000000-0000-0000-0000-000000000000"
        if not raw_bytes:
            raw_bytes = b'\0' * 16
        self.guid_str = guid_str
        self.raw_bytes = raw_bytes  # Store original bytes
        self.orig_type = orig_type

class RuntimeTypeData:
    def __init__(self, value: str = "", orig_type: str = ""):
        self.value = value
        self.orig_type = orig_type

class MaybeObject:
    def __init__(self, orig_type: str = ""):
        self.orig_type = orig_type
        
class RawBytesData:
    """Stores raw bytes exactly as read from file"""
    def __init__(self, raw_bytes: bytes = bytes(0), field_size: int = 1, orig_type: str = ""):
        self.raw_bytes = raw_bytes
        self.field_size = field_size
        self.orig_type = orig_type


TYPE_MAPPING = {
    "bool": BoolData,
    "s32": S32Data,
    "enum": S32Data,
    "int": S32Data,
    "uint": U32Data,
    "f32": F32Data,
    "f64": F64Data,
    "float": F32Data,
    "string": StringData,
    "resource": ResourceData, # Resources are strings so far (?)
    "gameobjectref": GameObjectRefData,
    "object": ObjectData,
    "vec2": Vec2Data,
    "vec3": Vec3Data,
    "vec4": Vec4Data,
    "keyframe": Vec4Data,
    "obb": OBBData,
    "userdata": UserDataData,
    "uint2": Uint2Data,
    "uint3": Uint3Data,
    "u8": U8Data,
    "u16": U16Data,
    "u32": U32Data,
    "u64": U64Data,
    "sphere": SphereData,
    "size": SizeData,
    "s8": S8Data,
    "s16": S16Data,
    "s64": S64Data,
    "runtimetype": RuntimeTypeData,
    "rect": RectData,
    "range": RangeData,
    "rangei": RangeIData,
    "quaternion": QuaternionData,
    "point": PointData,
    "mat4": Mat4Data,
    "linesegment": LineSegmentData,
    "int2": Int2Data,
    "int3": Int3Data,
    "int4": Int4Data,
    "guid": GuidData,
    "float2": Float2Data,
    "float3": Float3Data,
    "float4": Float4Data,
    "position": PositionData,
    "cylinder": CylinderData,
    "cone": ConeData,
    "color": ColorData,
    "capsule": CapsuleData,
    "area": AreaData,
    "aabb": AABBData,
    "data": RawBytesData,
    "struct": StructData,
}

def get_type_class(field_type: str, field_size: int = 4, is_native: bool = False, is_array: bool = False, align = 4, original_type = "", field_name = "") -> type:
    """Get the appropriate data type class based on field type and size"""

    if field_type == "data":
        if field_size == 16:
            if align == 8 and is_native:
                return GuidData
            else:
                return Vec4Data
        elif field_size == 80:
            return OBBData
        elif field_size == 64 and align == 16:
            return Mat4Data
        #elif field_size == 48 and align == 16:
        #    return CapsuleData
        elif field_size == 4 and is_native:
            return MaybeObject
        elif field_size == 1:
            return U8Data

    if field_type == "obb" and field_size == 16:
        return Vec4Data
    
    if field_type == "uri" and ("GameObjectRef" in original_type):
        return GameObjectRefData
    
    if field_type == "point" and ("Range" in original_type):
        return RangeData
    
    if field_type == "vec3" and "color" in field_name.lower():
        return Vec3ColorData
        
    if is_array and is_native and field_size == 4 and (field_type in ("s32", "u32")):
        return MaybeObject

    return TYPE_MAPPING.get(field_type, RawBytesData)
