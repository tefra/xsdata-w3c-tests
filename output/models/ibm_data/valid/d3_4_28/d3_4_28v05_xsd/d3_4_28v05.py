from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://xstest-tns/schema11_D3_4_28_v05"


@dataclass
class ElEnumerationA:
    class Meta:
        name = "elEnumerationA"
        namespace = "http://xstest-tns/schema11_D3_4_28_v05"

    value: Optional["ElEnumerationA.Value"] = field(
        default=None,
    )

    class Value(Enum):
        VALUE_2000_02_02_T02_00_00_123_Z = "2000-02-02T02:00:00.123Z"
        VALUE_2002_02_02_T02_00_00_09_00 = "2002-02-02T02:00:00+09:00"


@dataclass
class ElEnumerationB:
    class Meta:
        name = "elEnumerationB"
        namespace = "http://xstest-tns/schema11_D3_4_28_v05"

    value: Optional["ElEnumerationB.Value"] = field(
        default=None,
    )

    class Value(Enum):
        VALUE_2007_02_02_T01_00_00_123_Z = "2007-02-02T01:00:00.123Z"
        VALUE_2006_02_02_T01_00_00_123_09_00 = "2006-02-02T01:00:00.123-09:00"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_4_28_v05"

    el_enumeration_a: List["Root.ElEnumerationA"] = field(
        default_factory=list,
        metadata={
            "name": "elEnumerationA",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )
    el_enumeration_b: List["Root.ElEnumerationB"] = field(
        default_factory=list,
        metadata={
            "name": "elEnumerationB",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 3,
        }
    )

    class ElEnumerationA(Enum):
        VALUE_2000_02_02_T02_00_00_123_Z = "2000-02-02T02:00:00.123Z"
        VALUE_2002_02_02_T02_00_00_09_00 = "2002-02-02T02:00:00+09:00"

    class ElEnumerationB(Enum):
        VALUE_2007_02_02_T01_00_00_123_Z = "2007-02-02T01:00:00.123Z"
        VALUE_2006_02_02_T01_00_00_123_09_00 = "2006-02-02T01:00:00.123-09:00"
