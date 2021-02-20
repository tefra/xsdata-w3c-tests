from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDateTime


class DocValue(Enum):
    VALUE_0000_09_20_T00_00_00_Z = XmlDateTime(0, 9, 20, 0, 0, 0, 0, 0)
    VALUE_0000_09_20_T12_00_00_Z = XmlDateTime(0, 9, 20, 12, 0, 0, 0, 0)


@dataclass
class Doc:
    class Meta:
        name = "doc"

    value: Optional[DocValue] = field(
        default=None,
        metadata={
            "required": True,
            "explicit_timezone": "required",
        }
    )
