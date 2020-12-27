from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import List

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_28_v01"


class DTimeStampEnumeration(Enum):
    VALUE_1999_01_01_T12_00_00_Z = datetime(1999, 1, 1, 12, 0, tzinfo=timezone.utc)
    VALUE_2000_01_01_T12_00_00_Z = datetime(2000, 1, 1, 12, 0, tzinfo=timezone.utc)
    VALUE_2001_01_01_T12_00_00_123_09_00 = datetime(2001, 1, 1, 12, 0, 0, 123000, tzinfo=timezone(timedelta(days=-1, seconds=54000)))
    VALUE_2002_01_01_T12_00_00_123_09_00 = datetime(2002, 1, 1, 12, 0, 0, 123000, tzinfo=timezone(timedelta(seconds=32400)))


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_28_v01"

    eld_time_stamp_type: List[datetime] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeStampType",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    eld_time_stamp_enumeration: List[DTimeStampEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeStampEnumeration",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    eld_time_stamp_pattern: List[str] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeStampPattern",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "pattern": r"[2][0][0][0-9][-][0-1][1-2][-][0-2][1-8][T]*.*",
        }
    )
    eld_time_stamp_min_max_inclusive: List[datetime] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeStampMinMaxInclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_inclusive": datetime(2001, 1, 1, 12, 0, 0, 123000, tzinfo=timezone(timedelta(seconds=32400))),
            "max_inclusive": datetime(2002, 1, 1, 12, 0, 0, 123000, tzinfo=timezone(timedelta(seconds=32400))),
        }
    )
    eld_time_stamp_min_max_exclusive: List[datetime] = field(
        default_factory=list,
        metadata={
            "name": "eldTimeStampMinMaxExclusive",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "min_exclusive": datetime(1998, 1, 1, 12, 0, 0, 123000, tzinfo=timezone(timedelta(seconds=32400))),
            "max_exclusive": datetime(1999, 1, 1, 12, 0, 0, 123000, tzinfo=timezone(timedelta(seconds=32400))),
        }
    )
