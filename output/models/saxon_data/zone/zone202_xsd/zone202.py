from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Period


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
        VALUE_0000_01 = Period("0000-01")
        VALUE_0000_02 = Period("0000-02")
        VALUE_0000_03 = Period("0000-03")
        VALUE_0000_04 = Period("0000-04")
        VALUE_0000_05 = Period("0000-05")
        VALUE_0000_06_Z = Period("0000-06Z")
        VALUE_0000_07 = Period("0000-07")
        VALUE_0000_08 = Period("0000-08")
        VALUE_0000_09 = Period("0000-09")
        VALUE_0000_10 = Period("0000-10")
        VALUE_0000_11 = Period("0000-11")
        VALUE_0000_12 = Period("-0000-12")
