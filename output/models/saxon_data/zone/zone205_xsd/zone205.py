from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


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
        VALUE_2010_09_20_T00_00_00_Z = datetime(2010, 9, 20, 0, 0, tzinfo=timezone.utc)
        VALUE_2010_09_20_T12_00_00_Z = datetime(2010, 9, 20, 12, 0, tzinfo=timezone.utc)
