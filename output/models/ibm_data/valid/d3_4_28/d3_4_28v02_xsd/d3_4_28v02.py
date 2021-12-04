from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_28_v02"


class DTimeStampEnumeration(Enum):
    VALUE_1998_01_01_T12_00_00_Z = XmlDateTime(1998, 1, 1, 12, 0, 0, 0, 0)
    VALUE_2002_01_01_T12_00_00_990_08_00 = XmlDateTime(2002, 1, 1, 12, 0, 0, 990000, -480)


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_28_v02"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    attrd_time_stamp_type: Optional[XmlDateTime] = field(
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
    attrd_time_stamp_min_max_inclusive: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "attrdTimeStampMinMaxInclusive",
            "type": "Attribute",
            "min_inclusive": XmlDateTime(2003, 1, 1, 12, 0, 0, 990000, -480),
            "max_inclusive": XmlDateTime(2004, 1, 1, 12, 0, 0, 990000, -480),
        }
    )
    attrd_time_stamp_min_max_exclusive: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "attrdTimeStampMinMaxExclusive",
            "type": "Attribute",
            "min_exclusive": XmlDateTime(1998, 1, 1, 12, 0, 0, 0, 0),
            "max_exclusive": XmlDateTime(1999, 1, 1, 12, 0, 0, 0, 0),
        }
    )
