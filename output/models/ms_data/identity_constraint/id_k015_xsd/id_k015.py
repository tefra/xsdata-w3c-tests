from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class UidValue(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


@dataclass
class Uid:
    class Meta:
        name = "uid"

    pid: List[UidValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    uid: List[Uid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
