from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional


class ListType(Enum):
    """
    :cvar VALUE_1:
    :cvar VALUE_2:
    :cvar VALUE_3:
    :cvar VALUE_4:
    :cvar VALUE_5:
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"


@dataclass
class AttRef:
    """
    :ivar att1:
    """
    class Meta:
        name = "attRef"

    att1: List[ListType] = field(
        default_factory=list,
        metadata=dict(
            type="Attribute",
            tokens=True
        )
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"

    elem: Optional[AttRef] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
