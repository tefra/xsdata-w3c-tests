from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


@dataclass
class Doc:
    class Meta:
        name = "doc"

    value: Optional["Doc.Value"] = field(
        default=None,
        metadata={
            "explicit_timezone": "optional",
        }
    )

    class Value(Enum):
        VALUE_0000_01 = "0000-01"
        VALUE_0000_02 = "0000-02"
        VALUE_0000_03 = "0000-03"
        VALUE_0000_04 = "0000-04"
        VALUE_0000_05 = "0000-05"
        VALUE_0000_06_Z = "0000-06Z"
        VALUE_0000_07 = "0000-07"
        VALUE_0000_08 = "0000-08"
        VALUE_0000_09 = "0000-09"
        VALUE_0000_10 = "0000-10"
        VALUE_0000_11 = "0000-11"
        VALUE_0000_12 = "-0000-12"
