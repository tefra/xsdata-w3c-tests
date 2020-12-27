from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class Dttype(Enum):
    VALUE_2002_01_01_T12_01_01_00_00 = datetime(2002, 1, 1, 12, 1, 1, tzinfo=timezone.utc)


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
