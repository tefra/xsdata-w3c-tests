from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class AttRef:
    class Meta:
        name = "attRef"

    aga1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    aga2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[AttRef] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
