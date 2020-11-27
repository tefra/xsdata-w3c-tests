from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Dttype(Enum):
    VALUE_2002_01_01_T12_01_01_00_00 = "2002-01-01T12:01:01-00:00"


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
