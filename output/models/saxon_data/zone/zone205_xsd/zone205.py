from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


@dataclass
class Doc:
    """
    :ivar value:
    """
    class Meta:
        name = "doc"

    value: Optional["Doc.Value"] = field(
        default=None,
        metadata={
            "explicit_timezone": "required",
        }
    )

    class Value(Enum):
        """
        :cvar VALUE_2010_09_20_T00_00_00_Z:
        :cvar VALUE_2010_09_20_T12_00_00_Z:
        """
        VALUE_2010_09_20_T00_00_00_Z = "2010-09-20T00:00:00Z"
        VALUE_2010_09_20_T12_00_00_Z = "2010-09-20T12:00:00Z"
