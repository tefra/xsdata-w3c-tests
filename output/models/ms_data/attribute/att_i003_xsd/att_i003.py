from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


@dataclass
class AttRef:
    class Meta:
        name = "attRef"

    att1: Optional["AttRef.Att1"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    class Att1(Enum):
        AK = "AK"
        AL = "AL"
        AR = "AR"


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem: Optional[AttRef] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
