from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class MyEnum(Enum):
    """
    :cvar VALUE_1:
    :cvar VALUE_2:
    :cvar VALUE_3:
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


@dataclass
class Regex:
    """
    :ivar att:
    """
    att: Optional[MyEnum] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            pattern=r"[13]"
        )
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"

    elem: List[Regex] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
