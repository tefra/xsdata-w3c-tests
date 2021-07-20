from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class AttRef:
    class Meta:
        name = "attRef"

    ca1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ca2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    aga1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    aga2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ga2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
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
    ga1: str = field(
        default="abc",
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        }
    )
