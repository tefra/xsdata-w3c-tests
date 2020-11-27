from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "a"


class Type(Enum):
    X = "x"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "a"

    value: Optional[Type] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
