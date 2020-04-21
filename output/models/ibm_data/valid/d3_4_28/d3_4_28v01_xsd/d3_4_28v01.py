from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_28_v01"


class DTimeStampEnumeration(Enum):
    """
    :cvar VALUE_1999_01_01_T12_00_00_Z:
    :cvar VALUE_2000_01_01_T12_00_00_Z:
    :cvar VALUE_2001_01_01_T12_00_00_123_09_00:
    :cvar VALUE_2002_01_01_T12_00_00_123_09_00:
    """
    VALUE_1999_01_01_T12_00_00_Z = "1999-01-01T12:00:00Z"
    VALUE_2000_01_01_T12_00_00_Z = "2000-01-01T12:00:00Z"
    VALUE_2001_01_01_T12_00_00_123_09_00 = "2001-01-01T12:00:00.123-09:00"
    VALUE_2002_01_01_T12_00_00_123_09_00 = "2002-01-01T12:00:00.123+09:00"


@dataclass
class Root:
    """
    :ivar eld_time_stamp_type:
    :ivar eld_time_stamp_enumeration:
    :ivar eld_time_stamp_pattern:
    :ivar eld_time_stamp_min_max_inclusive:
    :ivar eld_time_stamp_min_max_exclusive:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_28_v01"

    eld_time_stamp_type: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeStampType",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    eld_time_stamp_enumeration: List[DTimeStampEnumeration] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeStampEnumeration",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    eld_time_stamp_pattern: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeStampPattern",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            pattern=r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*"
        )
    )
    eld_time_stamp_min_max_inclusive: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeStampMinMaxInclusive",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            min_inclusive="2001-01-01T12:00:00.123+09:00",
            max_inclusive="2002-01-01T12:00:00.123+09:00"
        )
    )
    eld_time_stamp_min_max_exclusive: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="eldTimeStampMinMaxExclusive",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            min_exclusive="1998-01-01T12:00:00.123+09:00",
            max_exclusive="1999-01-01T12:00:00.123+09:00"
        )
    )
