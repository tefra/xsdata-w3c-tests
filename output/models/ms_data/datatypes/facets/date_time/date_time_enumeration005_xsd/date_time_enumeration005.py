from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlDateTime


class Dttype(Enum):
    VALUE_2002_01_01_T12_01_01_00_00 = XmlDateTime(2002, 1, 1, 12, 1, 1, 0, 0)


@dataclass
class Doc:
    class Meta:
        name = "doc"

    value: Optional[Dttype] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
