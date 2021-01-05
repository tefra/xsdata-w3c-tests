from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlDateTime


@dataclass
class Doc:
    class Meta:
        name = "doc"

    value: Optional["Doc.Value"] = field(
        default=None,
        metadata={
            "explicit_timezone": "required",
        }
    )

    class Value(Enum):
        VALUE_0000_09_20_T00_00_00_Z = XmlDateTime(0, 9, 20, 0, 0, 0, 0, 0)
        VALUE_0000_09_20_T12_00_00_Z = XmlDateTime(0, 9, 20, 12, 0, 0, 0, 0)
