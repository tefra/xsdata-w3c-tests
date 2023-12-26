from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AttRef:
    class Meta:
        name = "attRef"

    att1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 2,
            "max_length": 3,
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
