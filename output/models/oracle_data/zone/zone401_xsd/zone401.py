from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Doc:
    """
    :ivar value:
    """
    class Meta:
        name = "doc"

    value: Optional["Doc.Type"] = field(
        default=None,
    )

    class Type(Enum):
        """
        :cvar VALUE_0000_09_20_T00_00_00_Z:
        :cvar VALUE_0000_09_20_T12_00_00_Z:
        """
        VALUE_0000_09_20_T00_00_00_Z = "0000-09-20T00:00:00Z"
        VALUE_0000_09_20_T12_00_00_Z = "0000-09-20T12:00:00Z"
