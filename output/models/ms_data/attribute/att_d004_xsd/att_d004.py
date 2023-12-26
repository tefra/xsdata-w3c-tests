from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class ListType(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"


@dataclass
class AttRef:
    class Meta:
        name = "attRef"

    att1: List[ListType] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem: Optional[AttRef] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
