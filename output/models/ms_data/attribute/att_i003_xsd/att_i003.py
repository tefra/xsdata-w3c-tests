from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class AttRefAtt1(Enum):
    AK = "AK"
    AL = "AL"
    AR = "AR"


@dataclass
class AttRef:
    class Meta:
        name = "attRef"

    att1: Optional[AttRefAtt1] = field(
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
        }
    )
