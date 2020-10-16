from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_28_v02"


class BdTimeStampEnumeration(Enum):
    """
    :cvar VALUE_1998_01_01_T12_00_00_Z:
    :cvar VALUE_2000_01_01_T12_00_00_123_Z:
    :cvar VALUE_2001_01_01_T12_00_00_08_00:
    :cvar VALUE_2002_01_01_T12_00_00_990_08_00:
    """
    VALUE_1998_01_01_T12_00_00_Z = "1998-01-01T12:00:00Z"
    VALUE_2000_01_01_T12_00_00_123_Z = "2000-01-01T12:00:00.123Z"
    VALUE_2001_01_01_T12_00_00_08_00 = "2001-01-01T12:00:00+08:00"
    VALUE_2002_01_01_T12_00_00_990_08_00 = "2002-01-01T12:00:00.990-08:00"


class DTimeStampEnumeration(Enum):
    """
    :cvar VALUE_1998_01_01_T12_00_00_Z:
    :cvar VALUE_2000_01_01_T12_00_00_123_Z:
    :cvar VALUE_2001_01_01_T12_00_00_08_00:
    :cvar VALUE_2002_01_01_T12_00_00_990_08_00:
    """
    VALUE_1998_01_01_T12_00_00_Z = "1998-01-01T12:00:00Z"
    VALUE_2000_01_01_T12_00_00_123_Z = "2000-01-01T12:00:00.123Z"
    VALUE_2001_01_01_T12_00_00_08_00 = "2001-01-01T12:00:00+08:00"
    VALUE_2002_01_01_T12_00_00_990_08_00 = "2002-01-01T12:00:00.990-08:00"


@dataclass
class Root:
    """
    :ivar value:
    :ivar attrd_time_stamp_type:
    :ivar attrd_time_stamp_enumeration:
    :ivar attrd_time_stamp_pattern:
    :ivar attrd_time_stamp_min_max_inclusive:
    :ivar attrd_time_stamp_min_max_exclusive:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_28_v02"

    value: Optional[str] = field(
        default=None,
    )
    attrd_time_stamp_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "attrdTimeStampType",
            "type": "Attribute",
        }
    )
    attrd_time_stamp_enumeration: Optional[DTimeStampEnumeration] = field(
        default=None,
        metadata={
            "name": "attrdTimeStampEnumeration",
            "type": "Attribute",
        }
    )
    attrd_time_stamp_pattern: Optional[str] = field(
        default=None,
        metadata={
            "name": "attrdTimeStampPattern",
            "type": "Attribute",
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T][0]*.*",
        }
    )
    attrd_time_stamp_min_max_inclusive: Optional[str] = field(
        default=None,
        metadata={
            "name": "attrdTimeStampMinMaxInclusive",
            "type": "Attribute",
            "min_inclusive": "2003-01-01T12:00:00.990-08:00",
            "max_inclusive": "2004-01-01T12:00:00.990-08:00",
        }
    )
    attrd_time_stamp_min_max_exclusive: Optional[str] = field(
        default=None,
        metadata={
            "name": "attrdTimeStampMinMaxExclusive",
            "type": "Attribute",
            "min_exclusive": "1998-01-01T12:00:00Z",
            "max_exclusive": "1999-01-01T12:00:00Z",
        }
    )
