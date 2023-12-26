from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class AttRef:
    class Meta:
        name = "attRef"

    ca1: object = field(
        default="abc",
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        },
    )
    ca2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    aga1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    aga2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ga2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        },
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
            "required": True,
        },
    )
    ga1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://xsdtesting",
        },
    )
