from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AttRef:
    class Meta:
        name = "attRef"

    foo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att2: Optional[object] = field(
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
        }
    )
