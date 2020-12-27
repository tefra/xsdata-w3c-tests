from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_28_v02"


class BdTimeStampEnumeration(Enum):
    VALUE_1998_01_01_T12_00_00_Z = datetime(1998, 1, 1, 12, 0, tzinfo=timezone.utc)
    VALUE_2000_01_01_T12_00_00_123_Z = datetime(2000, 1, 1, 12, 0, 0, 123000, tzinfo=timezone.utc)
    VALUE_2001_01_01_T12_00_00_08_00 = datetime(2001, 1, 1, 12, 0, tzinfo=timezone(timedelta(seconds=28800)))
    VALUE_2002_01_01_T12_00_00_990_08_00 = datetime(2002, 1, 1, 12, 0, 0, 990000, tzinfo=timezone(timedelta(days=-1, seconds=57600)))


class DTimeStampEnumeration(Enum):
    VALUE_1998_01_01_T12_00_00_Z = "1998-01-01T12:00:00Z"
    VALUE_2000_01_01_T12_00_00_123_Z = datetime(2000, 1, 1, 12, 0, 0, 123000, tzinfo=timezone.utc)
    VALUE_2001_01_01_T12_00_00_08_00 = datetime(2001, 1, 1, 12, 0, tzinfo=timezone(timedelta(seconds=28800)))
    VALUE_2002_01_01_T12_00_00_990_08_00 = "2002-01-01T12:00:00.990-08:00"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_28_v02"

    value: Optional[str] = field(
        default=None,
    )
    attrd_time_stamp_type: Optional[datetime] = field(
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
    attrd_time_stamp_min_max_inclusive: Optional[datetime] = field(
        default=None,
        metadata={
            "name": "attrdTimeStampMinMaxInclusive",
            "type": "Attribute",
            "min_inclusive": datetime(2003, 1, 1, 12, 0, 0, 990000, tzinfo=timezone(timedelta(days=-1, seconds=57600))),
            "max_inclusive": datetime(2004, 1, 1, 12, 0, 0, 990000, tzinfo=timezone(timedelta(days=-1, seconds=57600))),
        }
    )
    attrd_time_stamp_min_max_exclusive: Optional[datetime] = field(
        default=None,
        metadata={
            "name": "attrdTimeStampMinMaxExclusive",
            "type": "Attribute",
            "min_exclusive": datetime(1998, 1, 1, 12, 0, tzinfo=timezone.utc),
            "max_exclusive": datetime(1999, 1, 1, 12, 0, tzinfo=timezone.utc),
        }
    )
