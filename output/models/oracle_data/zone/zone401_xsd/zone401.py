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
            "explicit_timezone": "required",
        }
    )

    class Value(Enum):
        VALUE_0000_09_20_T00_00_00_Z = "0000-09-20T00:00:00Z"
        VALUE_0000_09_20_T12_00_00_Z = "0000-09-20T12:00:00Z"
