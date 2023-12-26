from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AttRef:
    class Meta:
        name = "attRef"

    att1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    att2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
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
    foo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
